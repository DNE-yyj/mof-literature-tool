from __future__ import annotations

import json
import shutil
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch

from core import build_parser, run_cli


REPO_ROOT = Path(__file__).resolve().parents[1]


OPENALEX_PAYLOAD = {
    "results": [
        {
            "id": "https://openalex.org/W1",
            "display_name": "Machine-learned interatomic potentials for water diffusion in MOF-303",
            "doi": "https://doi.org/10.1000/mof303",
            "publication_date": "2026-03-03",
            "publication_year": 2026,
            "type": "journal-article",
            "cited_by_count": 5,
            "primary_location": {
                "landing_page_url": "https://example.org/mof303",
                "source": {"display_name": "Journal of Mock Materials"},
            },
            "authorships": [
                {"author": {"display_name": "Alice Example"}},
                {"author": {"display_name": "Bob Example"}},
            ],
            "abstract_inverted_index": {
                "We": [0],
                "develop": [1],
                "a": [2],
                "machine-learned": [3],
                "interatomic": [4],
                "potential": [5],
                "for": [6],
                "water": [7],
                "diffusion": [8],
                "in": [9],
                "MOF-303.": [10],
            },
        }
    ]
}


CROSSREF_PAYLOAD = {
    "message": {
        "items": [
            {
                "DOI": "10.1000/mof303",
                "title": ["Machine-learned interatomic potentials for water diffusion in MOF-303"],
                "container-title": ["Journal of Mock Materials"],
                "author": [{"given": "Alice", "family": "Example"}],
                "abstract": "<jats:p>We develop a machine-learned interatomic potential for water diffusion in MOF-303.</jats:p>",
                "published-online": {"date-parts": [[2026, 3, 3]]},
                "URL": "https://doi.org/10.1000/mof303",
                "type": "journal-article",
                "is-referenced-by-count": 8,
            },
            {
                "DOI": "10.1000/cofmlip",
                "title": ["Machine-learning interatomic potentials for flexible COFs with van der Waals interactions"],
                "container-title": ["Journal of Transferable Methods"],
                "author": [{"given": "Carol", "family": "Example"}],
                "abstract": (
                    "<jats:p>We present a machine-learning interatomic-potential workflow for flexible COFs "
                    "with van der Waals interactions and discuss transfer to framework materials.</jats:p>"
                ),
                "published-online": {"date-parts": [[2026, 2, 20]]},
                "URL": "https://doi.org/10.1000/cofmlip",
                "type": "journal-article",
                "is-referenced-by-count": 3,
            },
            {
                "DOI": "10.1000/oxidediffusion",
                "title": ["Equivariant diffusion models for inverse design of oxide catalysts"],
                "container-title": ["Nature Materials"],
                "author": [{"given": "Dana", "family": "Example"}],
                "abstract": (
                    "<jats:p>We introduce a generative diffusion model with E(3)-equivariant graph neural networks "
                    "and uncertainty-aware active learning for crystal oxide catalyst discovery.</jats:p>"
                ),
                "published-online": {"date-parts": [[2026, 1, 15]]},
                "URL": "https://doi.org/10.1000/oxidediffusion",
                "type": "journal-article",
                "is-referenced-by-count": 12,
            },
            {
                "DOI": "10.1000/imageforgery",
                "title": [
                    "Multi-Modal Deep Learning for Image Forgery Detection: Visual Artifacts and Metadata Consistency Analysis"
                ],
                "container-title": ["Journal of Transferable AI Methods"],
                "author": [{"given": "Evan", "family": "Example"}],
                "abstract": (
                    "<jats:p>We introduce a multimodal transfer learning method that combines visual artifacts "
                    "and metadata consistency analysis for robust out-of-distribution detection.</jats:p>"
                ),
                "published-online": {"date-parts": [[2026, 4, 10]]},
                "URL": "https://doi.org/10.1000/imageforgery",
                "type": "journal-article",
                "is-referenced-by-count": 6,
            },
            {
                "DOI": "10.1002/anie.8169897",
                "title": [
                    "Underexplored Catalysts as General Structures: Application of Machine Learning Techniques for Reaction-Specific Datasets"
                ],
                "container-title": ["Angewandte Chemie International Edition"],
                "author": [{"given": "Jiajing", "family": "Li"}],
                "abstract": (
                    "<jats:p>We apply machine learning techniques to sparse and historically biased "
                    "reaction-specific datasets to identify underexplored catalysts with broad catalyst generality.</jats:p>"
                ),
                "published-online": {"date-parts": [[2026, 7, 10]]},
                "URL": "https://doi.org/10.1002/anie.8169897",
                "type": "journal-article",
                "is-referenced-by-count": 2,
            },
            {
                "DOI": "10.1021/jacs.6c04989",
                "title": [
                    "Strength of Interlayer Metal-Metal Coupling as Key Active Site Configuration and Atomic Descriptor for Single-Atom Catalysts"
                ],
                "container-title": ["Journal of the American Chemical Society"],
                "author": [{"given": "Liangliang", "family": "Xu"}],
                "abstract": (
                    "<jats:p>Guided by simulations and machine learning, we identify active site configuration "
                    "and atomic descriptor relationships for single-atom catalysts using data mining and subgroup discovery.</jats:p>"
                ),
                "published-online": {"date-parts": [[2026, 7, 9]]},
                "URL": "https://doi.org/10.1021/jacs.6c04989",
                "type": "journal-article",
                "is-referenced-by-count": 1,
            },
        ]
    }
}


def fake_fetch_json(url: str, *, headers: dict[str, str] | None = None, timeout: int = 30) -> dict[str, object]:
    if "openalex" in url:
        return OPENALEX_PAYLOAD
    if "crossref" in url:
        return CROSSREF_PAYLOAD
    raise AssertionError(f"Unexpected URL: {url}")


class LiteratureToolTests(unittest.TestCase):
    def setUp(self) -> None:
        tmp_root = REPO_ROOT / "tests" / "tmp_literature"
        tmp_root.mkdir(parents=True, exist_ok=True)
        self.output_dir = tmp_root / f"run_{uuid.uuid4().hex[:8]}"

    def tearDown(self) -> None:
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir, ignore_errors=True)

    @patch("core.fetch_json", side_effect=fake_fetch_json)
    def test_cli_writes_outputs_and_deduplicates(self, _mock_fetch: object) -> None:
        parser = build_parser()
        args = parser.parse_args(
            [
                "--profile",
                "mof_latest",
                "--days",
                "400",
                "--limit",
                "5",
                "--rows-per-query",
                "5",
                "--output-dir",
                str(self.output_dir),
            ]
        )
        outputs = run_cli(args)

        report_text = outputs["report"].read_text(encoding="utf-8")
        papers = json.loads(outputs["json"].read_text(encoding="utf-8"))

        self.assertTrue(outputs["report"].is_file())
        self.assertTrue(outputs["json"].is_file())
        self.assertTrue(outputs["tsv"].is_file())
        self.assertEqual(len(papers), 1)
        self.assertIn("Machine-learned interatomic potentials for water diffusion in MOF-303", report_text)
        self.assertIn("MOF relevance", report_text)
        self.assertGreaterEqual(papers[0]["citation_count"], 8)
        self.assertIn("interatomic_potential", papers[0]["tags"])

    @patch("core.fetch_json", side_effect=fake_fetch_json)
    def test_transfer_profile_keeps_cof_method_paper(self, _mock_fetch: object) -> None:
        parser = build_parser()
        args = parser.parse_args(
            [
                "--profile",
                "cof_transfer_methods",
                "--query",
                "covalent organic framework machine learning interatomic potential",
                "--days",
                "400",
                "--limit",
                "5",
                "--rows-per-query",
                "5",
                "--output-dir",
                str(self.output_dir),
            ]
        )
        outputs = run_cli(args)
        papers = json.loads(outputs["json"].read_text(encoding="utf-8"))
        titles = {paper["title"] for paper in papers}
        self.assertIn("Machine-learning interatomic potentials for flexible COFs with van der Waals interactions", titles)

    @patch("core.fetch_json", side_effect=fake_fetch_json)
    def test_materials_ml_transfer_profile_keeps_non_mof_method_paper(self, _mock_fetch: object) -> None:
        parser = build_parser()
        args = parser.parse_args(
            [
                "--profile",
                "materials_ml_transfer",
                "--query",
                "materials generative model diffusion inverse design crystal structure",
                "--days",
                "1095",
                "--limit",
                "5",
                "--rows-per-query",
                "5",
                "--output-dir",
                str(self.output_dir),
            ]
        )
        outputs = run_cli(args)
        papers = json.loads(outputs["json"].read_text(encoding="utf-8"))
        oxide_paper = next(
            paper for paper in papers if paper["title"] == "Equivariant diffusion models for inverse design of oxide catalysts"
        )

        self.assertNotIn("mof", oxide_paper["tags"])
        self.assertIn("generative_model", oxide_paper["tags"])
        self.assertIn("equivariant_ml", oxide_paper["tags"])
        self.assertIn("priority_journal", oxide_paper["tags"])
        self.assertIn("transfer to MOFs", oxide_paper["mof_relevance"])

    @patch("core.fetch_json", side_effect=fake_fetch_json)
    def test_materials_ml_transfer_profile_keeps_distant_cross_domain_method(self, _mock_fetch: object) -> None:
        parser = build_parser()
        args = parser.parse_args(
            [
                "--profile",
                "materials_ml_transfer",
                "--query",
                "multimodal transfer learning metadata consistency out-of-distribution",
                "--days",
                "1095",
                "--limit",
                "5",
                "--rows-per-query",
                "5",
                "--output-dir",
                str(self.output_dir),
            ]
        )
        outputs = run_cli(args)
        papers = json.loads(outputs["json"].read_text(encoding="utf-8"))
        image_paper = next(
            paper for paper in papers if paper["title"].startswith("Multi-Modal Deep Learning for Image Forgery")
        )

        self.assertIn("image_analysis", image_paper["tags"])
        self.assertIn("multimodal", image_paper["tags"])
        self.assertEqual(image_paper["transfer_distance"], "distant cross-domain method")
        self.assertIn("structure images", image_paper["mof_transfer_route"])

    @patch("core.fetch_json", side_effect=fake_fetch_json)
    def test_reaction_catalyst_transfer_profile_keeps_user_seed_papers(self, _mock_fetch: object) -> None:
        parser = build_parser()
        args = parser.parse_args(
            [
                "--profile",
                "reaction_catalyst_ml_transfer",
                "--days",
                "3650",
                "--limit",
                "10",
                "--rows-per-query",
                "5",
                "--output-dir",
                str(self.output_dir),
            ]
        )
        outputs = run_cli(args)
        papers = json.loads(outputs["json"].read_text(encoding="utf-8"))
        by_doi = {paper["doi"].lower(): paper for paper in papers if paper["doi"]}

        angew = by_doi["10.1002/anie.8169897"]
        jacs = by_doi["10.1021/jacs.6c04989"]

        self.assertIn("reaction_dataset", angew["tags"])
        self.assertIn("catalyst_descriptor", jacs["tags"])
        self.assertIn("MOF catalytic reaction families", angew["next_steps"])
        self.assertIn("MOF nodes", jacs["next_steps"])

    @patch("core.fetch_json", side_effect=fake_fetch_json)
    def test_mof_method_prior_art_profile_keeps_mof_method_paper(self, _mock_fetch: object) -> None:
        parser = build_parser()
        args = parser.parse_args(
            [
                "--profile",
                "mof_ml_method_prior_art",
                "--query",
                "metal-organic framework machine learned interatomic potential molecular dynamics",
                "--days",
                "3650",
                "--limit",
                "5",
                "--rows-per-query",
                "5",
                "--output-dir",
                str(self.output_dir),
            ]
        )
        outputs = run_cli(args)
        papers = json.loads(outputs["json"].read_text(encoding="utf-8"))
        titles = {paper["title"] for paper in papers}

        self.assertIn("Machine-learned interatomic potentials for water diffusion in MOF-303", titles)
        self.assertNotIn("Equivariant diffusion models for inverse design of oxide catalysts", titles)

    @patch("core.fetch_json", side_effect=fake_fetch_json)
    def test_config_driven_run_uses_queries_and_timestamped_output_root(self, _mock_fetch: object) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        config_path = self.output_dir / "weekly_config.json"
        config_path.write_text(
            json.dumps(
                {
                    "profile": "mof_adsorption",
                    "days": 400,
                    "limit": 5,
                    "rows_per_query": 5,
                    "queries": [
                        "metal-organic framework water adsorption machine learning",
                        "MOF-303 water diffusion interatomic potential",
                    ],
                    "output_root": "scheduled_reports",
                    "timestamped_output": True,
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        parser = build_parser()
        args = parser.parse_args(
            [
                "--config",
                str(config_path),
            ]
        )
        outputs = run_cli(args)
        self.assertTrue(outputs["report"].is_file())
        self.assertIn("scheduled_reports", str(outputs["report"]))
        manifest = json.loads(outputs["manifest"].read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["queries"]), 2)
        self.assertTrue(manifest["outputs"]["report"].endswith("report.md"))


if __name__ == "__main__":
    unittest.main()
