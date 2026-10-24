# Biology evaluations used by OpenAI and Anthropic

Checked **October 23, 2026** (America/Los_Angeles).

**Both OpenAI and Anthropic publicly document using LABBench2.** Their biology evaluations also cover protein prediction, scientific questions, literature research and computational analysis. The table below gives confirmed examples from their own publications, with links to the methods and releases.

[All completed project results](RESULTS_AND_REMAINING_WORK.md) · [Remaining evaluation work](ENGINEERING_PROGRESS.md)

## Which evaluations do they use?

| Evaluation and year | Documented company use | Inputs, tools and availability |
|---|---|---|
| **LABBench2 — 2026**<br>Biology research questions spanning literature, databases, figures, tables and other research materials. | **OpenAI:** GPT-Rosalind, April 2026; reported improvements over GPT-5.4 on 6 of 11 tasks. [OpenAI report](https://openai.com/index/introducing-gpt-rosalind/)<br><br>**Anthropic:** Claude Opus 4.8, May 2026, with results on patent, clinical-trial, table and supplementary-material questions. [System card, §8.16.8](https://www.anthropic.com/claude-opus-4-8-system-card#page=235) | Text and some text + image/file tasks. Anthropic describes live-web research; OpenAI's announcement does not specify its exact tool configuration. The benchmark supports web/code evaluation conditions. Public release: **1,892 tasks, 11 categories**. [Benchmark release](https://edisonscientific.com/news/labbench2-an-improved-benchmark), [paper](https://arxiv.org/abs/2604.09554). |
| **LAB-Bench — 2024**<br>The original biology knowledge-work benchmark, including literature, figure, protocol and sequence tasks. | **OpenAI:** o1 system card, December 2024, evaluates an **open-ended adaptation of 108 ProtocolQA questions**. [System card, §5.5.6](https://cdn.openai.com/o1-system-card-20241205.pdf#page=24)<br><br>**Anthropic:** Claude 4 system card, May 2025, evaluates FigQA, ProtocolQA, SeqQA and CloningScenarios. [System card, §7.2.4.7](https://assets.anthropic.com/m/6c940a1b69ed6a1c/original/Claude-4-System-Card.pdf#page=99) | Public benchmark. Text, with images for FigQA. Anthropic's reported run used no search or bioinformatics tools. OpenAI's open-ended ProtocolQA adaptation differs from the original multiple-choice task. **LAB-Bench and LABBench2 are different releases.** [Original paper](https://arxiv.org/abs/2407.10362). |
| **BioMysteryBench — 2026**<br>Answer biological questions by analysing anonymized experimental datasets. | **Anthropic:** created the benchmark and published Claude evaluations in April 2026. [Anthropic release](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) | Data files, code execution, installed bioinformatics packages and permitted database access. The current full release has **90 problems** after a July answer-key audit; the original announcement described 99. Full access requires an evaluation-only agreement; an ungated five-problem preview is available. [Full release and terms](https://huggingface.co/datasets/Anthropic/BioMysteryBench-full), [preview](https://huggingface.co/datasets/Anthropic/BioMysteryBench-preview). |
| **BixBench — 2025**<br>Computational biology and data-analysis questions. | **OpenAI:** GPT-Rosalind, April 2026. The announcement names **BixBench**, without establishing that it used the later BixBench3 release. [OpenAI report](https://openai.com/index/introducing-gpt-rosalind/) | Biological datasets and computational analysis in an agent environment. Public benchmark; the OpenAI announcement does not give the exact harness. [Original paper](https://arxiv.org/abs/2503.00096). |
| **LifeSciBench — 2026**<br>750 expert-authored life-science tasks, assessed with detailed response rubrics. | **OpenAI:** GPT-Rosalind and GPT-5.5 in the June 2026 release; the paper also evaluates GPT-5.4. [OpenAI report](https://openai.com/index/introducing-life-sci-bench/) | Text plus supporting artifacts, including figures, PDFs, tables and scientific files. Single-turn requests; the published methods permit Internet browsing. [Paper and methods](https://cdn.openai.com/pdf/b4299379-0a97-4ffa-8b9b-c3fbb299caa9/lifescibench_preprint.pdf). |
| **GeneBench-Pro — 2026**<br>129 computational-biology problems with synthetic datasets and known grading targets. | **OpenAI:** GPT-5.6 Sol, June 2026. [OpenAI methods and results](https://openai.com/index/introducing-genebench-pro/) | Iterative data analysis in a workspace with Python, scientific libraries and bioinformatics tools. Ten representative questions are openly presented; those ten are not the full 129-problem evaluation. |
| **FrontierScience — announced 2025; paper 2026**<br>Expert scientific questions across **biology, chemistry and physics**. | **OpenAI:** GPT-5.2 and other models in its December 2025 announcement. [OpenAI release](https://openai.com/index/frontierscience/) | Text questions, with Olympiad and research tracks. A 160-question gold set is public. The announcement does not establish the exact tool allowance. Headline whole-suite scores should not be relabelled as biology-only results. [Paper](https://arxiv.org/abs/2601.21165). |
| **ProteinGym Hard — Anthropic's 2026 evaluation**<br>Protein mutation-effect ranking using a selected subset of ProteinGym. The underlying ProteinGym benchmark paper is from **2023**. | **Anthropic:** Claude Opus 4.8 system card, §8.16.5. The stated metric is rank correlation against experimental measurements. [System card](https://www.anthropic.com/claude-opus-4-8-system-card#page=234) | Sequence-based prediction; the reported environment allows code/package tools. ProteinGym is public, but this card does not establish a public release of Anthropic's exact Hard subset. [ProteinGym paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/cac723e5ff29f65e3fcbb0739ae91bee-Paper-Datasets_and_Benchmarks.pdf). |
| **BioPipelineBench Verified — reported 2026**<br>Execution of externally checked bioinformatics workflows. | **Anthropic:** Claude Opus 4.8 system card, §8.16.1. [System card](https://www.anthropic.com/claude-opus-4-8-system-card#page=233) | Code execution and package tools. Public reporting is confirmed; a downloadable public task corpus is not established by this source. |

“Documented use” means the company itself reports evaluating models on the benchmark. A third-party paper that tests GPT or Claude models does not, by itself, establish company use. This is a selection of documented evaluations, rather than a complete inventory of private tests.

**Our LABBench2 evaluation is a separate, closed-book text condition:** 542 reviewed questions from LitQA3, TrialQA, DbQA2, PatentQA and SuppQA2, with no browsing or other solver tools. It should be compared with Anthropic's tool-enabled results only with that difference stated. Its unfinished generation/judging work is tracked in the [work document](ENGINEERING_PROGRESS.md).

## LiveProteinBench results

LiveProteinBench was released in **December 2025** and tests 12 protein-property and function tasks. Its paper evaluated earlier GPT and Claude models; we extended the evaluation with newer Qwen models and GPT-6 Luna. The paper results and our project runs below use **text inputs, including protein sequences**, without structure images. [Benchmark paper](https://arxiv.org/html/2512.22257v1#S3).

| Model | Accuracy |
|---|---:|
| [**GPT-6 Luna**](LIVEPROTEINBENCH_GPT6_LUNA_HIGH32K_RESULT.md) | **65.32%** |
| GPT-5 † | 60.49% |
| OpenAI o3 † | 56.04% |
| Claude 3.7 Sonnet † | 51.47% |
| **Qwen3.5-4B fine-tuned ‡** | **41.3%** |
| GPT-4o † | 38.39% |
| [**Qwen3.8-27B**](LIVEPROTEINBENCH_QWEN27B_OWN_OUTPUT_RESULT.md) | **34.56%** |
| [**Qwen3.5-4B — thinking off**](LIVEPROTEINBENCH_QWEN35_4B_POSTTRAINED_EXISTING_OUTPUTS.md) | **33.35%** |
| [**Qwen3.5-4B — thinking, 32K limit**](LIVEPROTEINBENCH_QWEN35_4B_POST_NATIVE_THINKING32K_V3_RESULT.md) | **28.92%** |

† Reported by the [LiveProteinBench paper, Table 5](https://arxiv.org/html/2512.22257v1#A4.T5).

‡ Separately provided fine-tuned model result, reported by the user. Its evaluation cohort and settings were not specified.

The paper uses 1,797 questions; our completed project runs use a reviewed subset of 1,736. Inference settings differ between runs; full details for our project runs are linked from the model names.

[Browse Luna's complete questions, protein inputs, answers and visible explanations](LIVEPROTEINBENCH_GPT6_LUNA_EXPLANATIONS.md). Accuracy scores the answers, not the scientific validity of the explanations.

## Three real LiveProteinBench examples

These are actual questions from the released dataset, with all four choices and complete protein sequences. The original task wording is shown below; the full model instruction is expandable. Sequence line breaks are added only for readability.

### 1. Cofactor prediction

**Case:** `cofactor_0133` · [Official question data](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json) · [Saved Luna answer](https://github.com/Some-random/bio-evaluation/blob/59c9ea984d418945c96331f25c99fd60a56c6cfe/reports/liveproteinbench_gpt6_luna_explanations/cofactor.md?plain=1#L3083)

**Question — original task wording:**

<blockquote>The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor..</blockquote>

<details>
<summary>Complete protein sequence (912 amino acids)</summary>

```text
MGRDARRLPLLPFLLLLLAAAAGVAESATDAEAIHDLARSVPALGWDGDNVCGFEGVTCE
RGGAGKVTELNLADRGLSGTLPDSLSSLTSLTALQLQGNALTGAVPSLARMGSLARLALD
GNAFTSLPPDFLHGLTSLQYLTMENLPLPPWPVPDAIANCSSLDTFSASNASISGPFPAV
LATLVSLRNLRLSYNNLTGGLPPELSSLIAMESLQLNNQRSDDKLSGPIDVIASMKSLKL
LWIQSNKFTGPIPDLNGTQLEAFNVRDNMLTGVVPPSLTGLMSLKNVSLSNNNFQGPKPA
FAAIPGQDEDSGNGFCLNTPGPCSPLTTTLLQVAEGFGYPYELAKTWKGNDPCSPAWVGI
VCTSSDVSMINLSRKNLSGRISPALANLTRLARLDLSNNNLTGVIPDVLTTLPSLTVLNV
ANNRLTGEVPKFKPSVNVLAQGNLFGQSSGSSGGGGGSDGDSSSSDSAGGGKSKPNTGMI
IGIIVAVIILFACIALLVHHRKKKNVEKFRPVSTKTSPAESEMMKIQVVGANGISNGSSA
FPTELYSHVSAANSSNISELFESHGMQLSVEVLLKATNNFSEDCILGRGGFGVVFKGNLN
GKLVAVKRCDSGTMGTKGQEEFLAEIDVLRKVRHRHLVALLGYCTHGNERLLVYEYMSGG
TLREHLCDLQQSGFIPLTWTQRMTIALDVARGIEYLHGLAQETFIHRDLKPSNILLDQDL
RAKVSDFGLVKLAKDTDKSLMTRIAGTFGYLAPEYATTGKVTTKVDVYAYGVILMEMITG
RKVLDDSLPDDETHLVTIFRRNILDKEKFRKFVDPTLELSAEGWTSLLEVADLARHCTAR
EPYQRPDMCHCVNRLSSLVDQWKPTNIDEDDYEGETSEMGLHQQLEKWRCDDFTISDSDT
FGSFNVPRKYNG
```

</details>

**Choices:**

- **A.** Ca(2+)
- **B.** Mn(2+)
- **C.** [2Fe-2S] cluster
- **D.** pantetheine 4'-phosphate

**Reference answer:** **B** — Mn(2+).

**Luna’s recorded choice:** **B** — correct.

<details>
<summary>Full original model instruction</summary>

<pre>You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

* Protein Sequence: The amino acid sequence of the protein.
* Multiple Choices: Candidate answers for the protein-related question.

Please think step-by-step about this problem:
1. Analyze the protein sequence carefully.
2. Consider the biological context and function.
3. Evaluate each multiple-choice option.
4. Provide your reasoning process.
5. Finally, give your answer.

Provide your response in the following format:
1. reasoning: [Your detailed reasoning here]
2. answer: Your final answer, which should be "A", "B", "C" or "D".
</pre>

</details>

### 2. Optimal pH prediction

**Case:** `ph_0052` · [Official question data](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/ph.json) · [Saved Luna answer](https://github.com/Some-random/bio-evaluation/blob/59c9ea984d418945c96331f25c99fd60a56c6cfe/reports/liveproteinbench_gpt6_luna_explanations/ph.md?plain=1#L1104)

**Question — original task wording:**

<blockquote>The current task is about Protein Optimal pH Prediction, which is to predict the optimal pH for a protein's activity. The optimal pH is the specific pH at which an enzyme exhibits its maximum catalytic rate. This property is critically dependent on the ionization states of amino acid residues, especially those in the active site. Based on the provided protein sequence, which dictates these properties, you must predict the pH range in which the enzyme functions most effectively..</blockquote>

<details>
<summary>Complete protein sequence (221 amino acids)</summary>

```text
MVSFTTLLTAVATAVSAVTASPLEALKRGIQPGTGVHDGYFYSFWTDGRGYVDFNNGPRG
SYRVSWSNVNNWVGGKGWNPGPPRRIAYNGTWNNWNVNSYLALYGWTTNPLVEYYIVEAY
GSYNPSSGAARLGTIEDDGGVYDIYRTRRINQPSIIGTASFDQYWSVRRQKRVGGTIDTG
KHFDEWRRQGNLQLGAWNYMIMATEGYQSSGSAEIEVRSLD
```

</details>

**Choices:**

- **A.** 4.9
- **B.** 7.6
- **C.** 5.2
- **D.** 7.0

**Reference answer:** **D** — 7.0.

**Luna’s recorded choice:** **C** — incorrect.

<details>
<summary>Full original model instruction</summary>

<pre>You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Optimal pH Prediction, which is to predict the optimal pH for a protein's activity. The optimal pH is the specific pH at which an enzyme exhibits its maximum catalytic rate. This property is critically dependent on the ionization states of amino acid residues, especially those in the active site. Based on the provided protein sequence, which dictates these properties, you must predict the pH range in which the enzyme functions most effectively.. The inputs provided by the user for this task include:

* Protein Sequence: The amino acid sequence of the protein.
* Multiple Choices: Candidate answers for the protein-related question.

Please think step-by-step about this problem:
1. Analyze the protein sequence carefully.
2. Consider the biological context and function.
3. Evaluate each multiple-choice option.
4. Provide your reasoning process.
5. Finally, give your answer.

Provide your response in the following format:
1. reasoning: [Your detailed reasoning here]
2. answer: Your final answer, which should be "A", "B", "C" or "D".
</pre>

</details>

### 3. Transmembrane region prediction

**Case:** `transmembrane_0081` · [Official question data](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) · [Saved Luna answer](https://github.com/Some-random/bio-evaluation/blob/59c9ea984d418945c96331f25c99fd60a56c6cfe/reports/liveproteinbench_gpt6_luna_explanations/transmembrane.md?plain=1#L1910)

**Question — original task wording:**

<blockquote>The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane..</blockquote>

<details>
<summary>Complete protein sequence (96 amino acids)</summary>

```text
MNVPTAPTPNKHLNIPDLRFEKVFKKALHRELAPSSSLSRKAGVITKVVVRDVLLMPLLQ
SFVLSLALMGVKEWLSYIRLKGRTLGDRIRQRLFPI
```

</details>

**Choices:**

- **A.** 53..72
- **B.** 53..71
- **C.** 53..71; 395..420
- **D.** 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329

**Reference answer:** **B** — 53..71.

**Luna’s recorded choice:** **B** — correct.

<details>
<summary>Full original model instruction</summary>

<pre>You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

* Protein Sequence: The amino acid sequence of the protein.
* Multiple Choices: Candidate answers for the protein-related question.

Please think step-by-step about this problem:
1. Analyze the protein sequence carefully.
2. Consider the biological context and function.
3. Evaluate each multiple-choice option.
4. Provide your reasoning process.
5. Finally, give your answer.

Provide your response in the following format:
1. reasoning: [Your detailed reasoning here]
2. answer: Your final answer, which should be "A", "B", "C" or "D".
</pre>

</details>

Examples: Copyright © 2026 LiveProteinBench contributors (Rong and colleagues), reproduced under [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Protein sequence resource: [UniProt](https://www.uniprot.org/help/license). Only presentation formatting was added; question wording, choices, reference answers and sequence residues are unchanged.
