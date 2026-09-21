# Literature Update

- Generated: `2026-09-21T06:16:51`
- Profile: `mof_latest_custom`
- Since: `2025-09-21`
- Papers retained: `3`

## Overview

Collected 3 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 1 papers and `DFT` in 3. `Adsorption/separation` themes appear more often (3) than `catalysis` themes (3). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

## Innovation Patterns

- Several recent papers still focus on single-system mechanistic insight rather than broad screening.
- Machine-learning models are commonly used as surrogates for expensive adsorption, electronic-structure, or catalytic calculations.
- DFT remains the main source of labels, descriptors, or mechanistic interpretation even in ML-heavy studies.

## Common Gaps

- Many screening papers still rely on idealized, defect-free structures and do not fully capture flexibility, humidity, or multicomponent conditions.
- ML papers often leave transferability and uncertainty outside the training distribution only partially resolved.
- Catalysis papers frequently identify thermodynamic trends without equally strong kinetic or explicit-environment treatment.

## Next Opportunities

- Connect adsorption descriptors to humid, multicomponent, and process-level targets instead of reporting only uptake/selectivity.
- For catalysis, combine DFT, microkinetics, and uncertainty-aware ML rather than stopping at static intermediate energetics.
- For transferable COF-side methods, port them to MOFs by adding node-aware descriptors, charge treatment, and local cluster corrections around metal sites.

## Paper Briefs

### 1. Concerted, Facile CO2 Hydrogenation in Ni-MOF-74 Revealed by Machine Learning Interatomic Potential-Based Enhanced Sampling Simulations

- Date: `2026-09-15`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15008834/v1
- Tags: adsorption, catalysis, co2, dft, h2, interatomic_potential, md, ml, mof, separation
- Authors: Dhananjay, Nishtha Sharma, Tarak Karmakar
- Why it matters: Metal-organic frameworks (MOFs) with open metal sites are promising heterogeneous catalysts, but the atomistic and dynamic details that govern their reactivity are difficult to access experimentally due to spatiotemporal resolution limits.
- Innovation: Metal-organic frameworks (MOFs) with open metal sites are promising heterogeneous catalysts, but the atomistic and dynamic details that govern their reactivity are difficult to access experimentally due to spatiotemporal resolution limits.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 2. Towards a Metal-Organic Framework with Pore-Confined Electrons

- Date: `2026-09-12`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.13939
- Tags: adsorption, catalysis, crystal, dft, h2, mof, porous_material
- Authors: Julia H. Baratta, Andrew S. Rosen
- Why it matters: Electrides are an unconventional class of materials in which electrons are localized in crystallographic void spaces rather than solely around atomic nuclei, giving rise to appealing properties such as low work functions, strong electron-donating character, and even superconductivity.
- Innovation: Electrides are an unconventional class of materials in which electrons are localized in crystallographic void spaces rather than solely around atomic nuclei, giving rise to appealing properties such as low work functions, strong electron-donating character, and even superconductivity.
- Likely limitations: Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 3. Boosting CO 2 Hydrogenation to Formic Acid Through Secondary Metal Promotion in Fe 3 O ‐Based MOF Catalysts

- Date: `2026-09-11`
- Journal: Journal of Computational Chemistry
- Link: https://doi.org/10.1002/jcc.70509
- Tags: adsorption, catalysis, dft, h2, mof
- Authors: Pavee Apilardmongkol, Manussada Ratanasak, Sirilak Kongkaew, Wilasinee Santiwarodom, Thanawit Kuamit
- Why it matters: ABSTRACT Metal–organic framework (MOF) catalysts are promising platforms for hydrogen energy systems, enabling CO 2 conversion to formic acid (HCOOH), a liquid organic hydrogen carrier (LOHC) for hydrogen storage and release.
- Innovation: ABSTRACT Metal–organic framework (MOF) catalysts are promising platforms for hydrogen energy systems, enabling CO 2 conversion to formic acid (HCOOH), a liquid organic hydrogen carrier (LOHC) for hydrogen storage and release.
- Likely limitations: Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.
