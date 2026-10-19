# Completed biological evaluation work: reviewer guide

Prepared October 19, 2026, Pacific time. This document summarizes completed work and points to the records needed to review it. It is not a progress dashboard or a claim that the entire catalog is finished.

## Scope and method

We evaluated a fixed **Qwen3.8-27B** checkpoint in original BF16 precision, served locally with vLLM. The main catalog retains 57 settings; seven BioReason-family settings are archived separately. Of the retained settings, **24 have reported metrics for their declared run scope**, and **seven additional settings have finished generation/scoring attempts but undefined primary metrics**. Declared scope can be a released public subset; completion does not imply a full paper replication. A recovered 59-case P36 attempt is additional partial evidence, not another completed full benchmark.

The workflow records source inputs and case identities, sends the declared task input to the model, saves model responses, and applies the task's native scorer or an explicitly named adaptation. Historical artifact availability is qualified below. Protocols differ by task: P43 uses a one-token conditional-likelihood interface; most other settings generate answers. The reported conditions include 1,024-, 4,096- and 16,384-token output budgets. Some runs combine preserved 4K outputs with a later 16K continuation on different cases; they cannot establish the causal benefit of a larger budget.

**Start with the [results and published comparisons](RESULTS_AT_A_GLANCE.md).** It contains the completed settings, dataset names, metrics, paper references and qualifications. The [decision table](EVALUATION_DECISION_TABLE.md) additionally distinguishes original runs, replays, offline corrections, partial attempts and settings without verified results.

## Findings to review

| Evidence | Completed finding | Interpretation and limit |
|---|---|---|
| Scientific figure/table questions | FigQA: 137/181 correct (75.7%); archived replay 131/181 (72.4%). TableQA: 216/244 (88.5%); replay 215/244 (88.1%). | Promising answer recovery on these public tasks. Source/mapping/image audits are available. Different paper prompts, decoding, image handling and unknown pretraining exposure prevent a controlled superiority claim. |
| Literature questions | LitQA2: 77/197 correct (39.1%). Two public cases were held before inference. | A measured reviewed-subset result. Correct answer labels do not validate the accompanying reasoning. |
| Protein localization | P03: 724/2,773 correct (26.1%), with 2,722 parsed answers (98.2%). | A relatively interpretable weak prediction result under this interface. Even counting all 51 invalid answers as correct gives 27.95%, below the test set's descriptive 29.14% majority-class reference. That retrospective reference is not a trained baseline. |
| Protein stability | P08: 12,616/12,851 finite predictions; parsed-only Spearman −0.121588. | Keeping those predictions fixed, any finite values in the 235 invalid slots still give full-test Spearman at most −0.067800. This is a sensitivity bound, not a completed score. The prompt's scale definition remains an interface qualification. |
| Reaction classification | P16 original: 9/5,651 correct (0.159%). A separately frozen terminal-number extraction diagnostic gives 12/5,651 (0.212%). | This specific formatting repair recovers very few correct labels. Poor class recovery persists under the tested full-sequence, joint-description generative protocol. |
| Drug–target interaction | P43 AUROC: BindingDB 0.5036; BioSNAP 0.5336; Human 0.4747. All three component tests scored without invalid outputs. | Weak discrimination under the prespecified one-token likelihood interface. Results remain separate by dataset and do not assess extended reasoning or tools. |
| Answer-delivery failures | SeqQA: 86/600 parsed; cloning: 0/33; GFP prediction: 1,382/27,217 numeric answers; GFP design: 0/200 accepted candidates. | These results primarily document output-budget/format limitations. They do not establish that clear biological predictions or valid designs were produced and found incorrect. |
| Scoring/metric limitations | P12–P15 compatibility repairs completed, but full AP/Fmax remain undefined. Medical-VQA and protein-description metrics have documented extraction or lexical-overlap limitations. | Removing a scorer crash does not recover absent predictions. Native lexical scores are not automatically semantic correctness or biological explanation quality. |
| Partial sequence-generation evidence | P36: exact raw-format 0/59; outer-whitespace-only diagnostic 5/59 complete sequences. | Whitespace recovery changes no residues and establishes syntax only. Biological function is unassessed. Archived ROUGE also uses the input prompt as an alternative reference. |

## Audit, corrections and reproducibility

- [Integrity audit](EVALUATION_INTEGRITY_AUDIT_2026-10-18.md): parsing, truncation, case alignment, image correspondence and limitations of paper comparisons.
- [Prediction-task audit](PREDICTION_TASK_AUDIT_2026-10-19.md): P03 class balance/invalid-answer bound and P43's likelihood interface.
- [P08 sensitivity proof](P08_SENSITIVITY_DIAGNOSTIC_2026-10-19.md) and [P36 whitespace diagnostic](P36_WHITESPACE_DIAGNOSTIC_2026-10-19.md): independent offline checks preserving original scores.
- [Protein-function failure analysis](DEEPFRI_FAILURE_ANALYSIS_2026-10-19.md): output-schema failures and reference comparisons on identical parsed subsets.
- [Reaction extraction diagnostic](REACTION_EXTRACTION_DIAGNOSTIC_2026-10-19.md): frozen extraction rule and results alongside the unchanged original score.
- [Scorer compatibility repair](SCORER_COMPATIBILITY_REPAIR_2026-10-19.md): all four completed corrections, invalid counts, code/provenance archive and separately named score records.
- [Structured results](RESULTS_AT_A_GLANCE.json), [structured decision table](EVALUATION_DECISION_TABLE.json), [saved run records](../results/runs/) and [evaluation code](../scripts/): task/run identifiers, source links, hashes and available detailed artifacts.
- [Worked examples](WORKED_EXAMPLES.md): selected saved responses and reasoning. Examples illustrate individual outputs; they are not a representative accuracy estimate or an independently verified explanation-quality score.

**Evidence availability is incomplete for some historical runs.** Several original detailed-score/raw-response files are absent from the current workspace and checked releases; their aggregate records and recorded hashes remain. In particular, complete original outputs for P01 and V01–V05 have not been recovered, so proposed extraction diagnostics on those runs are blocked. Links that fall back to aggregate JSON do not restore the missing per-case evidence. The audit distinguishes fresh checks, archived checks and findings based on retained summaries.

Available original artifacts remain unchanged; missing historical raw files have not been reconstructed. Offline corrections are separately named, retain the original denominators and do not selectively regenerate failures. Published specialist-model results provide context; different training, representations, inputs and inference settings prevent treating the table as a controlled model ranking.

For review, the central questions are whether each input/output contract is appropriate, whether extraction matches the intended answer semantics, whether denominators and failure accounting are correct, and whether each stated conclusion stays within the evidence available for that run. New pilots, proposed reruns and unfinished catalog settings are outside this completed-work summary; they are tracked in the [separate action plan](EVALUATION_REPAIR_PLAN_2026-10-19.md).

The [GPT-6-luna comparison preparation](GPT6_LUNA_QWEN_COMPARISON_PLAN_2026-10-19.md) identifies stable archived Qwen conditions and exact common cases for a future model comparison. It contains no new GPT benchmark results.
