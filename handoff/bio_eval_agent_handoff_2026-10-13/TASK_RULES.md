# Task-specific rules

These are proposed execution instructions grounded in the included catalogs. The verified official release controls a faithful reproduction. A/B/C/D/E/F are the earlier compatibility analysis, not the source papers' taxonomy.

All 64 biological IDs are covered once below; original metrics, splits and URLs remain in task_registry.json. More than one setting can use the same data, so do not treat 64 settings as independent datasets.

## First wave

`P18; P23–P26; P30–P32; B01–B03; B06–B08` — 14 settings, subject to access/protocol verification. Run other accessible work if one is blocked.

## DISCRETE_PROTEIN — P01, P02, P03, P09, P10, P11, P16

**Task names:** Solubility — PEER; Binary localization — DeepLoc/PEER; Subcellular localization — DeepLoc; Stability classification — NatureLM/PEER; Human protein–protein interaction — PEER; Yeast protein–protein interaction — PEER; Reaction class — zero-/few-shot

**Implement:** Render the complete sequence(s) and fixed label vocabulary. Keep solubility, membrane association, cellular compartment, stability classification and reaction categories separate.

**Score:** Use the catalog's original accuracy/normalization. A prompted LLM is a separately labeled baseline where the source fits a supervised head. Report invalid-label frequency; do not map answers using knowledge of the gold class.

**Text/context:** Native sequence/labels/objective always remain. Optional descriptions may be tested only if authorized and do not state the target property. Labels' definitions are instructions, not gold labels.

**Gate:** P09 is blocked until its exact stability binarization and split are recovered; do not convert TAPE regression yourself and call it NatureLM reproduction.

## CONTINUOUS_PROTEIN — P04, P05, P06, P07, P08

**Task names:** Beta-lactamase activity — PEER; AAV variant fitness — FLIP; Thermostability — FLIP/Meltome; GFP fluorescence — TAPE; Protein stability regression — TAPE

**Implement:** Build a documented sequence-to-score adapter using the original assay definition, score direction, normalization and input window. Do not replace regression with listwise ranking without naming a different variant.

**Score:** Spearman on the native assay/task split; preserve official aggregation. Keep constants/ties and undefined correlations visible. Do not mix numerical values from unrelated assays. Add numeric calibration/error only as separately labeled supplemental metrics when units are established.

**Text/context:** Assay identity and required conditions remain in NO_AUX. Do not supply the tested variant's measured outcome. Any few-shot measured examples must be from a permitted training/dev pool, fixed before scoring.

**Gate:** New text-baseline adapters required. No automatic fitting of the original supervised heads in the first pass.

## MULTILABEL_FUNCTION — P12, P13, P14, P15, P28, P29

**Task names:** Enzyme Commission labels — DeepFRI split; GO biological process — DeepFRI split; GO molecular function — DeepFRI split; GO cellular component — DeepFRI split; BioReason-Pro temporal GO test; Bio-posttrain species-held-out GO test

**Implement:** Recover exact EC/GO vocabulary, ontology version, propagation and allowed context. Implement the complete output-to-label-score mapping before collecting outputs.

**Score:** P12–P15: original micro-AP/AUPR and Fmax. P28: original Fmax and information-weighted Fmax. P29: original propagated GO-F1. These are not interchangeable. Hard label lists alone do not reproduce the original score-threshold curves. Use an explicitly documented score method or report a separately named fixed-label-F1 variant; never invent per-term probabilities.

**Text/context:** Keep gold annotations and answer-revealing functional descriptions scorer-side. Preliminary predictor outputs or other annotations are included only when the source permits them, with origin/date logged. Never choose the queried term vocabulary from each case's gold positives.

**Gate:** P29 needs the actual species-heldout split; do not substitute P28's temporal test. Freeze a valid score protocol; do not assume sparse prompted confidence values are calibrated.

## PROTEINGYM — P17

**Task names:** ProteinGym DMS substitution benchmark

**Implement:** Use a documented sequence-to-score baseline for the original DMS data. Prefer P18 for the first fixed textual ranking comparison rather than recreating it.

**Score:** Per-assay Spearman and official suite summaries. Do not claim amino-acid likelihood-ratio scoring unless the model/API actually exposes the needed probabilities.

**Text/context:** Pin any structures/MSAs/annotations as an additional input regime. No tested DMS labels in solver context.

**Gate:** Raw release and per-assay aggregation must be verified. It overlaps P18 in evidence and is not independent replication.

## PG_LLM_NATIVE — P18

**Task names:** PG-LLM / ProteinGym-LLM ranking

**Implement:** Use the frozen official release, full reference/variant sequences, fixed question template, candidate IDs, set sizes and seed-specific order. Preserve official ranking direction.

**Score:** Original per-assay Spearman and official aggregation across candidate sets/seeds. Test the parser on toy rankings. Handle duplicates, omissions, invented IDs, truncation and ties per source; otherwise flag protocol blocker instead of secretly repairing outputs.

**Text/context:** NATIVE ONLY by default. The given assay description is essential input. No NO_AUX/WITH_AUX, new retrieval context, prompt optimization or model selection using these frozen evaluations.

**Gate:** Verify and obey the release's evaluation-only conditions before running. Catalog release sizes/versions are leads, not newly downloaded data.

## PFA_SINGLE — P19

**Task names:** PFArena T1: single-mutant generation

**Implement:** Use official T1 input and up-to-40 single-substitution proposal budget, preserving wild-type numbering and the measured reference universe.

**Score:** Official Recall@40 and normalized maximum recovered score. Audit no-op, duplicate, invalid and unmeasured proposals using official rules. An unmeasured proposal is not an experimentally confirmed failure.

**Text/context:** Keep reference protein and design objective. No target-specific mutation measurements.

**Gate:** Exact official benchmark payload/prompt/scorer must be obtained. Do not reconstruct targets from a paper and label them the release.

## PFA_RANK_NO_MEAS — P20

**Task names:** PFArena T2: measurement-free multi-mutant ranking

**Implement:** Rank the supplied multiple-mutation candidates with the native reference/objective and no target-specific measured data.

**Score:** Official Spearman, NDCG, Recall@K and normalized best-score metrics with the exact gain transform, cutoff and direction.

**Text/context:** No added outcomes. Permitted optional text requires a separately authorized variant, not a silent change.

**Gate:** Exact official payload and scorer required.

## PFA_RANK_ANCHOR — P21

**Task names:** PFArena T3: anchor-informed ranking

**Implement:** Rank candidates extending the supplied tested mutant. Preserve the anchor's measured value and candidate-extension relationships.

**Score:** Use T3's official ranking metrics. Do not compare to T2 as if the provided evidence were identical.

**Text/context:** The anchor measurement is REQUIRED, not optional 'extra text'; removing it changes the task.

**Gate:** Exact official payload and scorer required.

## PFA_RANK_COMPONENTS — P22

**Task names:** PFArena T4: single-mutant-informed ranking

**Implement:** Rank supplied multiple mutants using the permitted individual-substitution measurements.

**Score:** Use T4's official ranking metrics and exact candidate/reference definitions.

**Text/context:** Single-mutant measurements are REQUIRED task inputs; multi-mutant target outcomes remain scorer-side. Do not remove the permitted measurements under NO_AUX.

**Gate:** Exact official payload and scorer required.

## PROTEIN_DESCRIPTION — P23, P24, P25, P26, P27

**Task names:** Mol-Instructions: Protein function generation; Mol-Instructions: Catalytic activity generation; Mol-Instructions: Domain and motif generation; Mol-Instructions: Functional description generation; NatureLM protein description

**Implement:** Supply full sequence and the source instruction. Distinguish function, catalytic reaction, domain/motif description and broader functional summary. Use the correct split per task.

**Score:** Official ROUGE-L configuration and response preprocessing. Do not silently substitute ROUGE-Lsum or change stemming/tokenization. Any reference-grounded biological judging is supplemental and separately configured; do not claim ROUGE establishes factual correctness.

**Text/context:** No gold descriptions/GO labels or paper conclusions that give away the target. Permitted metadata-only context requires an allowlist. A task explicitly providing passages is a different reading protocol.

**Gate:** P23–P26: use released Mol-Instructions test partitions. P27: blocked until exact NatureLM temporal description test is available.

## MUTATION_EXPLANATION — P30

**Task names:** MutaDescribe mutation explanation

**Implement:** Render the original reference/variant, exact mutation and authorized original protein context. Preserve Easy/Medium/Hard and temporal tests as distinct splits.

**Score:** Original BLEU-2/ROUGE-L plus semantic categories when the judge protocol is actually available. Fix judge model/prompt, blind solver identity, and keep the judge separate from answer generation. Without a configured judge/budget, report lexical scores only. No fake human-reviewed score.

**Text/context:** The held-out mutation explanation is gold, not context. General wild-type function is included only as allowed by the original text baseline.

**Gate:** Use real files and official loader if the HF viewer has mixed schemas. Do not rerun judging until the answer looks favorable.

## MUTATION_KNOWN_POSITION — P31

**Task names:** MutaDescribe mutation engineering — position supplied

**Implement:** Provide protein, desired effect and the designated residue position. Ask for the replacement amino acid.

**Score:** Official replacement-residue accuracy; preserve indexing and wild-type residue checks.

**Text/context:** The desired effect and position are required task inputs, even though they contain answer-related information. Only optional additional text can be ablated.

**Gate:** Recover exact candidate/normalization rules and original split.

## MUTATION_UNKNOWN_POSITION — P32

**Task names:** MutaDescribe mutation engineering — position unknown

**Implement:** Provide protein and desired effect, without the target position. Return up to the official 50 allowed single substitutions.

**Score:** Official Recall@50 of the annotated mutation. Validate indexing, replacement alphabet, unique proposals and no-ops. This is annotated-mutation recovery, not experimentally measured hit rate.

**Text/context:** Keep desired effect. Do not append the reference mutation or use gold labels to repair proposals.

**Gate:** Recover exact candidate/normalization rules and original split.

## LOW_N_HEAD — P33

**Task names:** MutaPLM low-N fitness regression

**Implement:** Preserve the low-N training/validation/test protocol and fitted regression head.

**Score:** Original Spearman across heldouts and seeds.

**Text/context:** Few-shot chat prompting on the seed measurements is a NEW protocol, not the fitted-head result.

**Gate:** Deferred special protocol: no head training or fabricated reproduction in this baseline-only pass.

## ITERATIVE_OPTIMIZATION — P34

**Task names:** MutaPLM iterative sequence optimization

**Implement:** Preserve starting sequence, objective, external scorer, search depth, proposals and scorer-query budgets.

**Score:** Reported predicted-fitness trajectories and dispersion. Log every oracle call and count failures.

**Text/context:** Solver-side feedback defines an iterative track; do not compare silently against one-shot inference.

**Gate:** Deferred until the official scorer/landscape versions and iteration budget are configured. Oracle scores are not new wet-lab measurements.

## RETRIEVAL — P35

**Task names:** ProtST text-to-protein retrieval

**Implement:** Need a frozen protein corpus, query set, relevance annotations and retrieval/reranking protocol.

**Score:** Use original defined retrieval measures/case diagnostics. Do not turn selected case studies into a nonexistent global recall benchmark.

**Text/context:** Ranking a small handpicked shortlist is not full-corpus retrieval. No gold annotations in the candidate text unless the original task intentionally exposes them.

**Gate:** Deferred; exact scored retrieval test needs to be established.

## QUALITATIVE_DESIGN — P36, P39

**Task names:** BioT5+ description-guided protein design; NatureLM heme-binding case study

**Implement:** Keep description-conditioned or heme-conditioned generation as documented qualitative cases.

**Score:** Report cases/proxy screens only. No fabricated general benchmark score or measured binding success.

**Text/context:** Use only requested conditions; generated self-descriptions do not validate function.

**Gate:** Deferred: fixed labeled benchmark/evaluator not established in the catalog.

## UNCONDITIONAL_GENERATION — P37

**Task names:** NatureLM unconditional generation

**Implement:** Generate protein strings with the same requested sample count, length rules and sampling policy across solvers.

**Score:** Original diversity/length distributions and fixed OmegaFold confidence pipeline; count invalid sequences.

**Text/context:** Adding functional guidance turns unconditional generation into a different task; NO_AUX/WITH_AUX is not applicable by default.

**Gate:** Deferred until evaluator versions and compute budget are fixed. Structural confidence is not measured function.

## CONDITIONAL_GENERATION — P38

**Task names:** NatureLM stability/solubility-conditioned generation

**Implement:** Generate sequences for the fixed requested stability/solubility conditions.

**Score:** Original fixed property scorer plus diversity metrics; keep evaluator checkpoint and any cutoffs constant.

**Text/context:** The property request is REQUIRED context. Scorer remains off the solver side unless an iterative protocol is expressly defined.

**Gate:** Deferred pending biological scorer/compute. Success is predictor-defined.

## RABD_STRUCTURE — P40

**Task names:** RAbD CDR-H3 redesign

**Implement:** Use the original target/framework complex with H3 masked, exact renumbering and permitted structural context.

**Score:** Original AAR and structural metrics (RMSD/lDDT/TM-score/DockQ as appropriate to the paper). Align the same atoms/regions. Native recovery is not binding.

**Text/context:** Text-only H3 recovery can be a separately named SEQUENCE_ONLY subtest, not reproduction of the coordinate-generation benchmark. No native loop sequence leakage through context or coordinates.

**Gate:** Full geometry evaluation deferred. Requires processed RAbD complexes and a structural output pipeline.

## SABDAB_STRUCTURE — P41

**Task names:** Proteo-R1 all-CDR SAbDab holdout

**Implement:** Use processed all-CDR holdout with exact release-time and H3-cluster split. Preserve fixed antigen/framework/docking assumptions and mask withheld loop information.

**Score:** Original structural/recovery/interface metrics and separately labeled energy proxies.

**Text/context:** Never expose native masked loop coordinates/features. Text serialization does not establish the same structural evaluation.

**Gate:** Deferred until processed split and model/evaluator are available.

## GFP_GENERATED — P42

**Task names:** STRIDE GFP generated-candidate evaluation

**Implement:** Use the fixed reference GFP, proposal/edit budget and original replace-only/full-edit settings.

**Score:** Fixed SaProt predicted fluorescence, success, uniqueness and novelty. Save actual sequences and invalid-edit counts.

**Text/context:** Use no outcome-driven retries or gold-measured labels for candidate selection. Any iterative feedback must match the original regime.

**Gate:** Deferred until scorer/configured budget; these generated cases are not TAPE's wet-lab held-out test.

## DRUG_TARGET — P43

**Task names:** Drug–target interaction — BioSNAP/Human/BindingDB

**Implement:** Supply original SMILES/protein inputs, exact dataset split and negative-label definition.

**Score:** Original AUROC from documented numeric predictions; report the score-generation method. A yes/no-only output is not an equivalent reproduction of continuous-score ranking.

**Text/context:** No original target affinity/interaction label in input. Keep BioSNAP/Human/BindingDB separate.

**Gate:** New text adapter; secondary to protein-first scope, requires each source's exact definitions.

## EXPLANATION_ASSESSMENT — P44

**Task names:** BioReason-Pro explanation assessment

**Implement:** Need a fixed explanation subset, source evidence, input allowlist and independent rubric.

**Score:** Run specified judge/expert evaluation only if available; do not substitute selected anecdotes for a quantitative benchmark.

**Text/context:** Separate generated explanation, teacher-only context and reference evidence.

**Gate:** Deferred until exact subset and scoring protocol are recovered; no human-review claims without actual review.

## LAB_TEXT — B01, B02, B03, B06, B07, B08

**Task names:** LAB-Bench / LitQA2; LAB-Bench / DbQA; LAB-Bench / SuppQA; LAB-Bench / ProtocolQA; LAB-Bench / SeqQA; LAB-Bench / Cloning scenarios

**Implement:** Use original question, choices/scenario/sequences and abstention rules. In the first pass, reproduce the tool-free baseline, not a new browser agent.

**Score:** Official accuracy; where abstention is allowed, report precision among answered items and coverage together. Preserve refusal versus abstention versus transport-failure distinctions.

**Text/context:** B01–B03: closed-book, provided-evidence and retrieval variants differ; default NATIVE, with any open-book extension explicitly permitted and separately named. B06–B08: the scenario, protocol and sequence are required, not removable auxiliary text.

**Gate:** Verify public dataset revision and six textual categories. Do not include FigQA/TableQA in the text-only count.

## IMAGE_QA — B04, B05, V01, V02, V03, V04, V05, V06, V07

**Task names:** LAB-Bench / FigQA; LAB-Bench / TableQA; VQA-RAD; SLAKE — English; PathVQA; ImageCLEF-VQA 2019; PMC-VQA held-out evaluation; LLaVA-Med visual conversation; Ryze extraction component tests

**Implement:** Use required original images plus textual questions in a VISION track. B05 TableQA is an image of a table. V07 contains separate component datasets, not one interchangeable protein task.

**Score:** Use each native image-QA scorer (closed/open accuracy, token recall, judge rubric or source-specific measure). Keep PMC-VQA initial/clean splits and LLaVA-Med conversation grading separate.

**Text/context:** TEXT+transcription is a changed experiment; removing images is an input-ablation diagnostic, not a faithful original benchmark. No gold-derived captions.

**Gate:** Deferred from the first TEXT pass; need real image assets, a vision-capable endpoint and applicable evaluation budget.

## GENOMIC — N01, N02, N03, N04

**Task names:** BioReason KEGG pathway/disease test; BioReason VEP-Coding; BioReason VEP-Non-SNV; Bio-posttrain KEGG network holdout

**Implement:** Use exact raw reference/variant representation, required pathway context and original sequence window. N04 is a distinct network-heldout adaptation.

**Score:** Native disease-label accuracy/macro-F1 or variant-class accuracy/F1; do not merge distinct targets. Normalize through a fixed rule.

**Text/context:** No gold disease answers or teacher rationales. Allowed pathway information remains input. Serialized raw DNA is not an Evo2 embedding.

**Gate:** Secondary to protein-first scope. N04 needs its actual adapted split; N01's original test cannot stand in for it.

## EXPRESSION — N05

**Task names:** Bio-posttrain MEDEA target selection

**Implement:** Need the original expression representations or a verified information-preserving raw measurement-to-text mapping.

**Score:** Original normalized gene-answer accuracy on the actual heldout disease/split.

**Text/context:** Candidate genes and disease/cell context alone are not the full expression-conditioned input. Do not omit the measurements and call it equivalent.

**Gate:** Deferred; raw expression mapping and exact split unresolved.
