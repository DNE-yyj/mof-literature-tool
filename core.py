from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import math
import os
import re
import textwrap
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

MODULE_ROOT = Path(__file__).resolve().parent

try:
    from literature_tool.profiles import PROFILES, QueryProfile, get_profile
except ImportError:
    from profiles import PROFILES, QueryProfile, get_profile


DEFAULT_PROFILE = "mof_latest"
DEFAULT_DAYS = 365
DEFAULT_LIMIT = 20
DEFAULT_ROWS_PER_QUERY = 20
DEFAULT_OUTPUT_DIR = MODULE_ROOT / "output"
DEFAULT_OPENAI_MODEL = "gpt-5.4-mini"


TAG_RULES: dict[str, tuple[str, ...]] = {
    "mof": ("metal-organic framework", "metal organic framework", " mof", "mof-", "mofs"),
    "cof": ("covalent organic framework", "covalent organic frameworks", " cof", "cof-", "cofs"),
    "adsorption": ("adsorption", "adsorbent", "uptake", "isotherm", "guest-host"),
    "separation": ("separation", "selectivity", "purification", "capture"),
    "catalysis": ("catalysis", "catalyst", "reaction pathway", "turnover"),
    "photocatalysis": ("photocatalysis", "photocatalytic", "photoelectro"),
    "electrocatalysis": ("electrocatalysis", "electrocatalytic", "electrochemical"),
    "water": ("water adsorption", "water harvesting", "humidity", "water uptake", "h2o", " water ", " aqueous ", "hydration"),
    "co2": ("co2", "carbon capture", "carbon dioxide", "dac", "direct air capture"),
    "h2": ("hydrogen", "h2 evolution", "her"),
    "dft": ("density functional theory", "dft", "first-principles", "first principles", "ab initio"),
    "ml": ("machine learning", "deep learning", "graph neural network", "transformer", "data-driven", "surrogate model"),
    "high_throughput": ("high-throughput", "high throughput", "screening", "database", "benchmark"),
    "interatomic_potential": (
        "interatomic potential",
        "interatomic potentials",
        "interatomic-potential",
        "machine learned interatomic potential",
        "machine learned interatomic potentials",
        "machine-learned interatomic potential",
        "machine-learned interatomic potentials",
        "machine learning potential",
        "neural network potential",
        "potential energy surface",
    ),
    "gcmc": ("gcmc", "grand canonical monte carlo"),
    "md": ("molecular dynamics", "md simulation", "diffusion", "dynamics"),
    "force_field": ("force field", "uff", "dreiding"),
    "review": ("review", "perspective", "roadmap"),
}


SENTENCE_PRIORITY = (
    "we develop",
    "we present",
    "we report",
    "we demonstrate",
    "we introduce",
    "this work presents",
    "this study presents",
    "here we",
    "herein we",
    "a machine-learning",
    "a machine learning",
    "high-throughput",
    "descriptor",
)


@dataclass
class Paper:
    title: str
    authors: list[str]
    journal: str
    publication_date: str
    year: int | None
    doi: str | None
    url: str
    abstract: str
    type: str
    source_id: str
    sources: list[str] = field(default_factory=list)
    queries: list[str] = field(default_factory=list)
    citation_count: int = 0
    score: float = 0.0
    tags: list[str] = field(default_factory=list)
    takeaway: str = ""
    innovation: str = ""
    limitations: str = ""
    next_steps: str = ""
    mof_relevance: str = ""

    def dedupe_key(self) -> str:
        if self.doi:
            return f"doi::{normalize_doi(self.doi)}"
        return f"title::{normalize_title(self.title)}"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class CorpusSummary:
    overview: str
    innovation_points: list[str]
    common_limitations: list[str]
    next_opportunities: list[str]


def today_local() -> dt.date:
    return dt.date.today()


def normalize_doi(value: str) -> str:
    return value.strip().lower().replace("https://doi.org/", "").replace("http://doi.org/", "")


def normalize_title(value: str) -> str:
    lowered = value.lower()
    lowered = re.sub(r"[^a-z0-9]+", " ", lowered)
    return re.sub(r"\s+", " ", lowered).strip()


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    text = html.unescape(value)
    text = re.sub(r"</?(jats:)?[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_date_string(value: str | None) -> dt.date | None:
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            parsed = dt.datetime.strptime(value, fmt)
            if fmt == "%Y":
                return dt.date(parsed.year, 1, 1)
            if fmt == "%Y-%m":
                return dt.date(parsed.year, parsed.month, 1)
            return parsed.date()
        except ValueError:
            continue
    return None


def reconstruct_openalex_abstract(abstract_index: dict[str, list[int]] | None) -> str:
    if not abstract_index:
        return ""
    tokens: list[tuple[int, str]] = []
    for token, positions in abstract_index.items():
        for position in positions:
            tokens.append((position, token))
    ordered = [token for _, token in sorted(tokens)]
    return clean_text(" ".join(ordered))


def fetch_json(url: str, *, headers: dict[str, str] | None = None, timeout: int = 30) -> dict[str, Any]:
    request = Request(url, headers=headers or {})
    with urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8")
    return json.loads(body)


def base_headers(mailto: str | None = None) -> dict[str, str]:
    user_agent = "mof-literature-tool/0.1 (+https://example.invalid)"
    if mailto:
        user_agent = f"{user_agent}; mailto:{mailto}"
    return {
        "Accept": "application/json",
        "User-Agent": user_agent,
    }


def fetch_openalex(query: str, *, from_date: str, rows: int, mailto: str | None = None) -> list[Paper]:
    params = {
        "search": query,
        "per-page": str(rows),
        "page": "1",
        "sort": "publication_date:desc",
        "filter": f"from_publication_date:{from_date}",
    }
    if mailto:
        params["mailto"] = mailto
    url = f"https://api.openalex.org/works?{urlencode(params)}"
    payload = fetch_json(url, headers=base_headers(mailto))
    papers: list[Paper] = []
    for item in payload.get("results", []):
        paper = parse_openalex_paper(item, query=query)
        if paper is not None:
            papers.append(paper)
    return papers


def parse_openalex_paper(item: dict[str, Any], *, query: str) -> Paper | None:
    title = clean_text(item.get("display_name"))
    if not title:
        return None
    doi = item.get("doi")
    primary_location = item.get("primary_location") or {}
    source = primary_location.get("source") or {}
    url = (
        primary_location.get("landing_page_url")
        or doi
        or item.get("id")
        or ""
    )
    authors = [
        clean_text(authorship.get("author", {}).get("display_name"))
        for authorship in item.get("authorships", [])
        if clean_text(authorship.get("author", {}).get("display_name"))
    ]
    journal = clean_text(source.get("display_name"))
    abstract = reconstruct_openalex_abstract(item.get("abstract_inverted_index"))
    publication_date = clean_text(item.get("publication_date"))
    year = item.get("publication_year")
    return Paper(
        title=title,
        authors=authors,
        journal=journal,
        publication_date=publication_date,
        year=year if isinstance(year, int) else None,
        doi=clean_text(doi) or None,
        url=url,
        abstract=abstract,
        type=clean_text(item.get("type")) or "unknown",
        source_id=clean_text(item.get("id")) or title,
        sources=["openalex"],
        queries=[query],
        citation_count=int(item.get("cited_by_count") or 0),
    )


def crossref_publication_date(item: dict[str, Any]) -> str:
    for key in ("published-online", "published-print", "published", "issued"):
        parts = item.get(key, {}).get("date-parts", [])
        if not parts:
            continue
        first = parts[0]
        values = [str(part) for part in first[:3]]
        if len(values) == 1:
            return values[0]
        if len(values) == 2:
            return f"{values[0]}-{int(values[1]):02d}"
        return f"{values[0]}-{int(values[1]):02d}-{int(values[2]):02d}"
    return ""


def fetch_crossref(query: str, *, from_date: str, rows: int, mailto: str | None = None) -> list[Paper]:
    params = {
        "query.bibliographic": query,
        "rows": str(rows),
        "sort": "published",
        "order": "desc",
        "filter": f"from-pub-date:{from_date},type:journal-article",
    }
    if mailto:
        params["mailto"] = mailto
    url = f"https://api.crossref.org/works?{urlencode(params)}"
    payload = fetch_json(url, headers=base_headers(mailto))
    papers: list[Paper] = []
    for item in payload.get("message", {}).get("items", []):
        paper = parse_crossref_paper(item, query=query)
        if paper is not None:
            papers.append(paper)
    return papers


def parse_crossref_paper(item: dict[str, Any], *, query: str) -> Paper | None:
    title_list = item.get("title") or []
    title = clean_text(title_list[0] if title_list else "")
    if not title:
        return None
    authors = []
    for author in item.get("author", []):
        given = clean_text(author.get("given"))
        family = clean_text(author.get("family"))
        full = f"{given} {family}".strip()
        if full:
            authors.append(full)
    journal_list = item.get("container-title") or []
    journal = clean_text(journal_list[0] if journal_list else "")
    abstract = clean_text(item.get("abstract"))
    publication_date = crossref_publication_date(item)
    parsed_date = parse_date_string(publication_date)
    doi = clean_text(item.get("DOI")) or None
    url = clean_text(item.get("URL")) or (f"https://doi.org/{doi}" if doi else "")
    return Paper(
        title=title,
        authors=authors,
        journal=journal,
        publication_date=publication_date,
        year=parsed_date.year if parsed_date else None,
        doi=doi,
        url=url,
        abstract=abstract,
        type=clean_text(item.get("type")) or "unknown",
        source_id=doi or title,
        sources=["crossref"],
        queries=[query],
        citation_count=int(item.get("is-referenced-by-count") or 0),
    )


def merge_papers(primary: Paper, incoming: Paper) -> Paper:
    merged = Paper(**primary.to_dict())
    merged.sources = sorted(set(primary.sources + incoming.sources))
    merged.queries = sorted(set(primary.queries + incoming.queries))
    merged.citation_count = max(primary.citation_count, incoming.citation_count)
    if len(incoming.abstract) > len(primary.abstract):
        merged.abstract = incoming.abstract
    if len(incoming.authors) > len(primary.authors):
        merged.authors = incoming.authors
    if not merged.journal and incoming.journal:
        merged.journal = incoming.journal
    if not merged.publication_date and incoming.publication_date:
        merged.publication_date = incoming.publication_date
        merged.year = incoming.year
    if not merged.url and incoming.url:
        merged.url = incoming.url
    if not merged.doi and incoming.doi:
        merged.doi = incoming.doi
    return merged


def dedupe_papers(papers: list[Paper]) -> list[Paper]:
    by_key: dict[str, Paper] = {}
    for paper in papers:
        key = paper.dedupe_key()
        if key in by_key:
            by_key[key] = merge_papers(by_key[key], paper)
        else:
            by_key[key] = paper
    return list(by_key.values())


def tag_paper(paper: Paper) -> list[str]:
    haystack = f"{paper.title} {paper.abstract}".lower()
    tags = [name for name, phrases in TAG_RULES.items() if any(phrase in haystack for phrase in phrases)]
    if "mof" not in tags and re.search(r"\bmof\b", haystack):
        tags.append("mof")
    if "cof" not in tags and re.search(r"\bcof\b", haystack):
        tags.append("cof")
    if "review" not in tags and ("review" in paper.type.lower() or "review" in paper.title.lower()):
        tags.append("review")
    return sorted(set(tags))


def keyword_hits(text: str, keywords: tuple[str, ...]) -> int:
    lowered = text.lower()
    return sum(1 for keyword in keywords if keyword.lower() in lowered)


def paper_matches_profile(paper: Paper, profile: QueryProfile) -> bool:
    haystack = f"{paper.title} {paper.abstract}".lower()
    if not any(token.lower() in haystack for token in profile.must_have_any):
        return False
    if any(keyword.lower() in haystack for keyword in profile.exclude_keywords):
        return False
    if profile.required_any_tags and not set(profile.required_any_tags).intersection(paper.tags):
        return False
    if profile.required_any_method_tags and not set(profile.required_any_method_tags).intersection(paper.tags):
        return False
    return True


def score_paper(paper: Paper, profile: QueryProfile) -> float:
    parsed_date = parse_date_string(paper.publication_date)
    age_days = 365
    if parsed_date is not None:
        age_days = max((today_local() - parsed_date).days, 0)
    recency_score = max(0.0, 6.0 - age_days / 90.0)
    keyword_score = float(keyword_hits(f"{paper.title} {paper.abstract}", profile.boost_keywords))
    citation_score = math.log1p(max(paper.citation_count, 0))
    abstract_bonus = 1.0 if paper.abstract else 0.0
    review_bonus = 1.0 if "review" in paper.tags else 0.0
    method_bonus = 0.5 if {"dft", "ml"} <= set(paper.tags) else 0.0
    return recency_score + keyword_score + citation_score + abstract_bonus + review_bonus + method_bonus


def split_sentences(text: str) -> list[str]:
    if not text:
        return []
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    cleaned = [sentence.strip() for sentence in sentences if sentence.strip()]
    return cleaned


def choose_key_sentence(paper: Paper) -> str:
    sentences = split_sentences(paper.abstract)
    lowered_sentences = [(sentence, sentence.lower()) for sentence in sentences]
    for sentence, lowered in lowered_sentences:
        if any(token in lowered for token in SENTENCE_PRIORITY):
            return sentence
    if sentences:
        return sentences[0]
    return paper.title


def infer_limitations(paper: Paper) -> str:
    tags = set(paper.tags)
    points: list[str] = []
    if "ml" in tags:
        points.append("Likely sensitive to training-set coverage and transferability across chemistries.")
    if "dft" in tags and "md" not in tags:
        points.append("Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.")
    if "high_throughput" in tags or "gcmc" in tags or "force_field" in tags:
        points.append("Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.")
    if "catalysis" in tags and "md" not in tags:
        points.append("Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.")
    if "cof" in tags and "mof" not in tags:
        points.append("Direct transfer to MOFs will require explicit metal-node chemistry and stronger electrostatics.")
    if not points:
        points.append("Abstract-level evidence is promising, but validation breadth is unclear without reading the full paper.")
    return " ".join(points[:2])


def infer_next_steps(paper: Paper) -> str:
    tags = set(paper.tags)
    steps: list[str] = []
    if "adsorption" in tags or "separation" in tags:
        steps.append("Test humid or multicomponent conditions and connect material metrics to process-level targets.")
    if "catalysis" in tags:
        steps.append("Add kinetics, explicit environment effects, and active-site reconstruction checks.")
    if "interatomic_potential" in tags:
        steps.append("Extend training to guest-loaded, distorted, and diffusion-transition configurations.")
    if "cof" in tags and "mof" not in tags:
        steps.append("Port the workflow to MOFs with node-aware descriptors or cluster corrections around metal sites.")
    if "ml" in tags:
        steps.append("Benchmark uncertainty and out-of-domain behavior before broad screening claims.")
    if not steps:
        steps.append("Validate the method on a broader material set and compare against experimental observables.")
    return " ".join(steps[:2])


def infer_mof_relevance(paper: Paper) -> str:
    tags = set(paper.tags)
    if "mof" in tags:
        return "Directly relevant to MOF work."
    if "cof" in tags and "interatomic_potential" in tags:
        return "Method is transferable to MOFs if metal-node electrostatics and coordination chemistry are added."
    if "cof" in tags and ("ml" in tags or "high_throughput" in tags):
        return "Workflow is likely transferable to MOFs with node-aware descriptors and stronger charge treatment."
    return "Potentially useful as a neighboring-method reference."


def annotate_paper(paper: Paper, profile: QueryProfile) -> Paper:
    paper.tags = tag_paper(paper)
    paper.score = score_paper(paper, profile)
    paper.takeaway = choose_key_sentence(paper)
    paper.innovation = choose_key_sentence(paper)
    paper.limitations = infer_limitations(paper)
    paper.next_steps = infer_next_steps(paper)
    paper.mof_relevance = infer_mof_relevance(paper)
    return paper


def collect_papers(
    *,
    profile: QueryProfile,
    from_date: str,
    rows_per_query: int,
    mailto: str | None = None,
) -> list[Paper]:
    collected: list[Paper] = []
    for query in profile.queries:
        collected.extend(fetch_openalex(query, from_date=from_date, rows=rows_per_query, mailto=mailto))
        collected.extend(fetch_crossref(query, from_date=from_date, rows=rows_per_query, mailto=mailto))
    deduped = dedupe_papers(collected)
    annotated = [annotate_paper(paper, profile) for paper in deduped]
    filtered = [paper for paper in annotated if paper_matches_profile(paper, profile)]
    filtered.sort(key=lambda paper: paper.score, reverse=True)
    return filtered


def aggregate_tag_counts(papers: list[Paper]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for paper in papers:
        for tag in paper.tags:
            counts[tag] = counts.get(tag, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def build_rule_based_corpus_summary(papers: list[Paper], *, profile: QueryProfile) -> CorpusSummary:
    counts = aggregate_tag_counts(papers)
    total = len(papers)
    ml_count = counts.get("ml", 0)
    dft_count = counts.get("dft", 0)
    adsorption_count = counts.get("adsorption", 0)
    catalysis_count = counts.get("catalysis", 0) + counts.get("photocatalysis", 0) + counts.get("electrocatalysis", 0)
    mlip_count = counts.get("interatomic_potential", 0)
    overview_bits = [
        f"Collected {total} deduplicated papers for profile `{profile.name}`.",
        f"`ML` appears in {ml_count} papers and `DFT` in {dft_count}.",
        f"`Adsorption/separation` themes appear more often ({adsorption_count}) than `catalysis` themes ({catalysis_count})."
        if adsorption_count >= catalysis_count
        else f"`Catalysis` themes appear more often ({catalysis_count}) than `adsorption/separation` themes ({adsorption_count}).",
    ]
    if mlip_count:
        overview_bits.append(f"`Interatomic-potential` or MLIP-style work appears in {mlip_count} papers and is a notable transfer path from COF-side methods to MOFs.")
    innovation_points = [
        "Data-driven screening is increasingly paired with physically grounded descriptors rather than pure geometry-only filters."
        if counts.get("high_throughput", 0)
        else "Several recent papers still focus on single-system mechanistic insight rather than broad screening."
    ]
    if ml_count:
        innovation_points.append("Machine-learning models are commonly used as surrogates for expensive adsorption, electronic-structure, or catalytic calculations.")
    if dft_count:
        innovation_points.append("DFT remains the main source of labels, descriptors, or mechanistic interpretation even in ML-heavy studies.")
    if mlip_count:
        innovation_points.append("ML interatomic potentials are emerging as the clearest route to capture framework flexibility and guest dynamics beyond static screening.")
    common_limitations = [
        "Many screening papers still rely on idealized, defect-free structures and do not fully capture flexibility, humidity, or multicomponent conditions.",
        "ML papers often leave transferability and uncertainty outside the training distribution only partially resolved.",
        "Catalysis papers frequently identify thermodynamic trends without equally strong kinetic or explicit-environment treatment.",
    ]
    next_opportunities = [
        "Connect adsorption descriptors to humid, multicomponent, and process-level targets instead of reporting only uptake/selectivity.",
        "For catalysis, combine DFT, microkinetics, and uncertainty-aware ML rather than stopping at static intermediate energetics.",
        "For transferable COF-side methods, port them to MOFs by adding node-aware descriptors, charge treatment, and local cluster corrections around metal sites.",
    ]
    return CorpusSummary(
        overview=" ".join(overview_bits),
        innovation_points=innovation_points[:3],
        common_limitations=common_limitations[:3],
        next_opportunities=next_opportunities[:3],
    )


def extract_json_object(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?", "", stripped).strip()
        stripped = re.sub(r"```$", "", stripped).strip()
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object found in model response.")
    return json.loads(stripped[start : end + 1])


def openai_chat_completion(prompt: str, *, api_key: str, model: str) -> str:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are helping summarize computational-chemistry literature for a MOF researcher. "
                    "Return only valid JSON."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "temperature": 0.2,
    }
    data = json.dumps(payload).encode("utf-8")
    request = Request(
        "https://api.openai.com/v1/chat/completions",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urlopen(request, timeout=120) as response:
        body = response.read().decode("utf-8")
    parsed = json.loads(body)
    content = parsed["choices"][0]["message"]["content"]
    if isinstance(content, list):
        text_bits = [item.get("text", "") for item in content if item.get("type") == "text"]
        return "\n".join(bit for bit in text_bits if bit)
    if isinstance(content, str):
        return content
    raise ValueError("Unexpected OpenAI response content format.")


def maybe_upgrade_summary_with_openai(
    papers: list[Paper],
    *,
    profile: QueryProfile,
    model: str,
    enabled: bool,
) -> CorpusSummary:
    fallback = build_rule_based_corpus_summary(papers, profile=profile)
    if not enabled:
        return fallback
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return fallback
    selection = papers[: min(len(papers), 12)]
    paper_lines = []
    for index, paper in enumerate(selection, start=1):
        paper_lines.append(
            textwrap.dedent(
                f"""
                [{index}] Title: {paper.title}
                Journal: {paper.journal}
                Date: {paper.publication_date}
                Tags: {", ".join(paper.tags)}
                Abstract: {paper.abstract}
                """
            ).strip()
        )
    prompt = textwrap.dedent(
        f"""
        Summarize the following recent literature set for a MOF researcher.
        Focus on high-level field synthesis, not full-paper paraphrase.

        Return JSON with this exact schema:
        {{
          "overview": "string",
          "innovation_points": ["string", "string", "string"],
          "common_limitations": ["string", "string", "string"],
          "next_opportunities": ["string", "string", "string"]
        }}

        Profile: {profile.name}
        Papers:
        {os.linesep.join(paper_lines)}
        """
    ).strip()
    try:
        content = openai_chat_completion(prompt, api_key=api_key, model=model)
        data = extract_json_object(content)
        return CorpusSummary(
            overview=clean_text(data.get("overview")),
            innovation_points=[clean_text(item) for item in data.get("innovation_points", []) if clean_text(item)][:3] or fallback.innovation_points,
            common_limitations=[clean_text(item) for item in data.get("common_limitations", []) if clean_text(item)][:3] or fallback.common_limitations,
            next_opportunities=[clean_text(item) for item in data.get("next_opportunities", []) if clean_text(item)][:3] or fallback.next_opportunities,
        )
    except Exception:
        return fallback


def build_markdown_report(
    papers: list[Paper],
    *,
    profile: QueryProfile,
    from_date: str,
    summary: CorpusSummary,
    generated_at: str,
) -> str:
    lines = [
        "# Literature Update",
        "",
        f"- Generated: `{generated_at}`",
        f"- Profile: `{profile.name}`",
        f"- Since: `{from_date}`",
        f"- Papers retained: `{len(papers)}`",
        "",
        "## Overview",
        "",
        summary.overview,
        "",
        "## Innovation Patterns",
        "",
    ]
    for point in summary.innovation_points:
        lines.append(f"- {point}")
    lines.extend(["", "## Common Gaps", ""])
    for point in summary.common_limitations:
        lines.append(f"- {point}")
    lines.extend(["", "## Next Opportunities", ""])
    for point in summary.next_opportunities:
        lines.append(f"- {point}")
    lines.extend(["", "## Paper Briefs", ""])
    for index, paper in enumerate(papers, start=1):
        authors = ", ".join(paper.authors[:5]) if paper.authors else "Unknown authors"
        lines.extend(
            [
                f"### {index}. {paper.title}",
                "",
                f"- Date: `{paper.publication_date or 'unknown'}`",
                f"- Journal: {paper.journal or 'unknown'}",
                f"- Link: {paper.url or (f'https://doi.org/{paper.doi}' if paper.doi else 'N/A')}",
                f"- Tags: {', '.join(paper.tags) if paper.tags else 'uncategorized'}",
                f"- Authors: {authors}",
                f"- Why it matters: {paper.takeaway}",
                f"- Innovation: {paper.innovation}",
                f"- Likely limitations: {paper.limitations}",
                f"- Next step: {paper.next_steps}",
                f"- MOF relevance: {paper.mof_relevance}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(
    papers: list[Paper],
    *,
    output_dir: Path,
    profile: QueryProfile,
    from_date: str,
    summary: CorpusSummary,
    generated_at: str,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "report.md"
    json_path = output_dir / "papers.json"
    csv_path = output_dir / "papers.tsv"
    manifest_path = output_dir / "manifest.json"

    report_path.write_text(
        build_markdown_report(
            papers,
            profile=profile,
            from_date=from_date,
            summary=summary,
            generated_at=generated_at,
        ),
        encoding="utf-8",
    )
    json_path.write_text(
        json.dumps([paper.to_dict() for paper in papers], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    csv_lines = [
        "\t".join(
            [
                "title",
                "publication_date",
                "journal",
                "doi",
                "url",
                "citation_count",
                "score",
                "tags",
                "innovation",
                "limitations",
                "next_steps",
            ]
        )
    ]
    for paper in papers:
        row = [
            paper.title,
            paper.publication_date,
            paper.journal,
            paper.doi or "",
            paper.url,
            str(paper.citation_count),
            f"{paper.score:.3f}",
            ",".join(paper.tags),
            paper.innovation,
            paper.limitations,
            paper.next_steps,
        ]
        csv_lines.append("\t".join(value.replace("\t", " ").replace("\n", " ") for value in row))
    csv_path.write_text("\n".join(csv_lines) + "\n", encoding="utf-8")
    manifest = {
        "generated_at": generated_at,
        "profile": profile.name,
        "from_date": from_date,
        "paper_count": len(papers),
        "queries": list(profile.queries),
        "outputs": {
            "report": str(report_path),
            "json": str(json_path),
            "tsv": str(csv_path),
        },
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return {
        "report": report_path,
        "json": json_path,
        "tsv": csv_path,
        "manifest": manifest_path,
    }


def load_json_config(path: Path | None) -> tuple[dict[str, Any], Path | None]:
    if path is None:
        return {}, None
    resolved = path.expanduser().resolve()
    payload = json.loads(resolved.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Config must be a JSON object: {resolved}")
    return payload, resolved


def resolve_setting(args: argparse.Namespace, config: dict[str, Any], name: str, default: Any) -> Any:
    if hasattr(args, name):
        return getattr(args, name)
    if name in config:
        return config[name]
    return default


def resolve_config_path(config_value: str | None, *, config_path: Path | None) -> Path | None:
    if not config_value:
        return None
    path = Path(config_value)
    if path.is_absolute() or config_path is None:
        return path
    return (config_path.parent / path).resolve()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Collect and summarize recent MOF/COF literature.")
    parser.add_argument(
        "--config",
        type=Path,
        default=argparse.SUPPRESS,
        help="Optional JSON config file for repeatable or scheduled runs.",
    )
    parser.add_argument(
        "--profile",
        default=argparse.SUPPRESS,
        choices=sorted(PROFILES),
        help=f"Built-in query profile to run. Default: {DEFAULT_PROFILE}.",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=argparse.SUPPRESS,
        help=f"Look back this many days from today. Default: {DEFAULT_DAYS}.",
    )
    parser.add_argument(
        "--query",
        action="append",
        help="Optional custom query. Repeat to replace the profile's built-in query list with your own.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=argparse.SUPPRESS,
        help=f"Retain this many top-ranked papers after deduplication. Default: {DEFAULT_LIMIT}.",
    )
    parser.add_argument(
        "--rows-per-query",
        type=int,
        default=argparse.SUPPRESS,
        help=f"Fetch this many rows per source per query before deduplication. Default: {DEFAULT_ROWS_PER_QUERY}.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=argparse.SUPPRESS,
        help=f"Directory for the generated report and raw metadata. Default: {DEFAULT_OUTPUT_DIR}.",
    )
    parser.add_argument(
        "--mailto",
        default=argparse.SUPPRESS,
        help="Optional email for OpenAlex/Crossref polite pool usage.",
    )
    parser.add_argument(
        "--use-openai",
        action="store_true",
        default=argparse.SUPPRESS,
        help="If OPENAI_API_KEY is set, upgrade the field-level summary with an LLM.",
    )
    parser.add_argument(
        "--openai-model",
        default=argparse.SUPPRESS,
        help=f"Model name for optional OpenAI summarization. Default: {DEFAULT_OPENAI_MODEL}.",
    )
    return parser


def run_cli(args: argparse.Namespace) -> dict[str, Path]:
    config, config_path = load_json_config(getattr(args, "config", None))
    profile_name = resolve_setting(args, config, "profile", DEFAULT_PROFILE)
    base_profile = get_profile(profile_name)
    profile = base_profile
    query_override = getattr(args, "query", None)
    if query_override is None:
        config_queries = config.get("queries")
        if isinstance(config_queries, list):
            query_override = [str(item) for item in config_queries if str(item).strip()]
    if query_override:
        profile = QueryProfile(
            name=f"{base_profile.name}_custom",
            description=f"{base_profile.description} Custom query override.",
            queries=tuple(query_override),
            must_have_any=base_profile.must_have_any,
            boost_keywords=base_profile.boost_keywords,
            required_any_tags=base_profile.required_any_tags,
            required_any_method_tags=base_profile.required_any_method_tags,
            exclude_keywords=base_profile.exclude_keywords,
        )
    days = int(resolve_setting(args, config, "days", DEFAULT_DAYS))
    limit = int(resolve_setting(args, config, "limit", DEFAULT_LIMIT))
    rows_per_query = int(resolve_setting(args, config, "rows_per_query", DEFAULT_ROWS_PER_QUERY))
    mailto = resolve_setting(args, config, "mailto", None)
    use_openai = bool(resolve_setting(args, config, "use_openai", False))
    openai_model = str(resolve_setting(args, config, "openai_model", DEFAULT_OPENAI_MODEL))
    now = dt.datetime.now().replace(microsecond=0)
    generated_at = now.isoformat()
    timestamp_label = now.strftime("%Y%m%d_%H%M%S")
    explicit_output_dir = getattr(args, "output_dir", None)
    if explicit_output_dir is not None:
        output_dir = explicit_output_dir
    else:
        config_output_dir = resolve_config_path(config.get("output_dir"), config_path=config_path)
        config_output_root = resolve_config_path(config.get("output_root"), config_path=config_path)
        timestamped_output = bool(config.get("timestamped_output", True))
        if config_output_dir is not None:
            output_dir = config_output_dir
        elif config_output_root is not None:
            output_dir = config_output_root / timestamp_label if timestamped_output else config_output_root
        else:
            output_dir = DEFAULT_OUTPUT_DIR
    output_dir = Path(output_dir)
    from_date = (today_local() - dt.timedelta(days=max(days, 1))).isoformat()
    papers = collect_papers(
        profile=profile,
        from_date=from_date,
        rows_per_query=max(rows_per_query, limit),
        mailto=mailto,
    )
    selected = papers[: max(limit, 1)]
    summary = maybe_upgrade_summary_with_openai(
        selected,
        profile=profile,
        model=openai_model,
        enabled=use_openai,
    )
    outputs = write_outputs(
        selected,
        output_dir=output_dir,
        profile=profile,
        from_date=from_date,
        summary=summary,
        generated_at=generated_at,
    )
    return outputs
