# Worked examples and tool workflows

[Back to the task map](EVALUATION_OVERVIEW.md)

The overview keeps one correct answer and one tool-use challenge. This document retains the full examples and saved reasoning. Correct answers do not independently validate every step of a model's explanation. Tool workflows below are source-backed examples, not measured Qwen failures.

## Correct answers from saved Qwen runs

### In panel a, at day 30, which group still has surviving subjects?

**Task:** Reading a biological figure (B04). **Case:** `cf6ac735-33af-4243-bfcf-4c28e3267345`.

**Exact question and choices:**

> The following is a multiple choice question about biology.
> Please answer by responding with the letter of the correct answer.
> Think step by step.
>
> Question: In panel a, at day 30, which group still has surviving subjects?&#32;
>
> Options:
> (A) None of the above
> (B) WT + Ive
> (C) Insufficient information to answer the question
> (D) WT + Nemadipine
> (E) WT
>
> You MUST include the letter of the correct answer within the following tags: [ANSWER] and [/ANSWER].
> For example, '[ANSWER]&lt;answer&gt;[/ANSWER]', where &lt;answer&gt; is the correct letter.
> Always answer in exactly this format of a single letter between the two tags, even if you are unsure.
> We require this because we use automatic parsing.

<img src="example_assets/b04-cf6ac735-33af-4243-bfcf-4c28e3267345.jpg" alt="Reading a biological figure" width="600">

**Saved model reasoning, verbatim:**

> The question asks about panel a, at day 30, which group still has surviving subjects. Looking at the survival curve, at day 30 all curves appear to be at 0% survival. Let me look carefully. The x-axis goes to 30. At day 30, all three lines (WT blue circles, WT+Nemadipine red triangles, WT+Ive green squares) are at 0. The curves reach 0 around day 26-28 and stay at 0 through day 30. So at day 30, none have surviving subjects.
>
> Let me look at the rightmost points. The green squares seem to extend to day 30 at 0. The blue circles reach 0 around day 27. The red triangles reach 0 around day 26. At day 30, all are 0.
>
> Thus the answer is (A) None of the above.
>
> Let me double check the question phrasing: "which group still has surviving subjects?" If all are at 0, then none have surviving subjects, so answer A.
>
> Thus [ANSWER]A[/ANSWER].

**Saved final answer, verbatim:**

> Looking at panel a, by day 30 all three survival curves (WT, WT + Nemadipine, and WT + Ive) have reached 0% survival. Therefore no group has surviving subjects at that time point.
>
> [ANSWER]A[/ANSWER]

Reference choice: **A** — correct. Dataset accuracy: **72.4%** (131/181).

### In panel e, which of the following sheath lengths do cortex oligodendrocytes produce at the highest frequency?

**Task:** Reading a biological figure (B04). **Case:** `ae3a0d60-8c22-4402-8ab2-43a6e87cde18`.

**Exact question and choices:**

> The following is a multiple choice question about biology.
> Please answer by responding with the letter of the correct answer.
> Think step by step.
>
> Question: In panel e, which of the following sheath lengths do cortex oligodendrocytes produce at the highest frequency?&#32;
>
> Options:
> (A) Insufficient information to answer the question
> (B) 10
> (C) 30
> (D) 20
> (E) 5
> (F) 15
>
> You MUST include the letter of the correct answer within the following tags: [ANSWER] and [/ANSWER].
> For example, '[ANSWER]&lt;answer&gt;[/ANSWER]', where &lt;answer&gt; is the correct letter.
> Always answer in exactly this format of a single letter between the two tags, even if you are unsure.
> We require this because we use automatic parsing.

<img src="example_assets/b04-ae3a0d60-8c22-4402-8ab2-43a6e87cde18.jpg" alt="Reading a biological figure" width="600">

**Saved model reasoning, verbatim:**

> The question asks about panel e, which is the "Cerebellar slice culture" histogram. I need to look at the cortex (blue/teal) bars and find which length bin has the highest frequency.
>
> Looking at panel e, the x-axis has bins: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, &gt;120. The cortex (teal) bars: at 10 it's around 3, at 20 it's around 14, then there's a tall bar around 20-25 reaching ~20, then ~15, ~12.5, ~8, etc.
>
> Let me look more carefully. The bars in panel e for cortex: first bar (10) ~3, second bar (~15-20?) ~14, third bar (20) ~20 (the tallest), fourth ~15, fifth ~12.5, etc.
>
> The x-axis labels are 10, 20, 30, 40... but the bars appear between labels. Let's think about bin positions. Typically the labels are at the bin centers or bin edges. In panel A, the tallest cortex bar is at the position between 10 and 20? Actually in panel A, the first bar is small (~4) before the 10 label, then a tall bar ~29 at around 10-15, then ~23 at 15-20, then ~17 at 20-25... Hmm.
>
> Let's look at the labels alignment. In panel e, the labels 10, 20, 30... The tallest teal bar appears to be aligned near the 20 label. Let's look: there's a bar at ~3 (before 10), bar at ~14 (at 10-15?), bar at ~20 (at 20), bar at ~15 (at 20-25?), bar at ~12.5 (at 30)...
>
> This is getting too detailed. The options are 5, 10, 15, 20, 30. The peak of the cortex distribution in panel e is around 20 μm. Looking at the figure, the tallest teal bar is at the bin corresponding to 20. So answer D (20).
>
> Let me cross check with panel f (log length fit) for cerebellar slice cortex: peak around log length 1.2-1.3, which is 10^1.25 ≈ 17-20 μm. Yes consistent with ~20.
>
> Thus the highest frequency sheath length for cortex oligodendrocytes in panel e is 20 μm.
>
> So answer D.
>
> I'll provide reasoning and final.

**Saved final answer, verbatim:**

> Looking at panel **e** (Cerebellar slice culture), the teal bars represent cortex oligodendrocytes. The tallest cortex bar occurs at the 20 µm bin (≈20% frequency), with neighboring bins (10–15 µm and 30 µm) being lower. This is consistent with the fitted peak in panel f at a log length of ~1.2–1.3 (≈15–20 µm).
>
> Therefore, the sheath length produced at the highest frequency by cortex oligodendrocytes is **20 µm**.
>
> [ANSWER]D[/ANSWER]

Reference choice: **D** — correct. Dataset accuracy: **72.4%** (131/181).

### Which model shows the lowest MSE when chi1 = 300?

**Task:** Comparing values in a scientific table (B05). **Case:** `5d3f8067-fe32-4abb-9646-276150413965`.

**Exact question and choices:**

> The following is a multiple choice question about biology.
> Please answer by responding with the letter of the correct answer.
> Think step by step.
>
> Question: Which model shows the lowest MSE when chi1 = 300?
>
> Options:
> (A) OPLS4a
> (B) OPLS3e
> (C) Both OPLS4a and OPLS3e have the same lowest value for MSE when chi1 = 300
> (D) Insufficient information to answer the question
> (E) OPLS4
>
> You MUST include the letter of the correct answer within the following tags: [ANSWER] and [/ANSWER].
> For example, '[ANSWER]&lt;answer&gt;[/ANSWER]', where &lt;answer&gt; is the correct letter.
> Always answer in exactly this format of a single letter between the two tags, even if you are unsure.
> We require this because we use automatic parsing.

<img src="example_assets/b05-5d3f8067-fe32-4abb-9646-276150413965.png" alt="Comparing values in a scientific table" width="600">

**Saved model reasoning, verbatim:**

> The question asks which model shows the lowest MSE when chi1 = 300. Let me look at the table column "MSE (chi1 = 300)".
>
> Values:
> - OPLS3e: +0.5 ± 0.2
> - OPLS4a (OPLS4 with superscript a): +0.5 ± 0.2
> - OPLS4: +0.2 ± 0.2
>
> The lowest value is +0.2 for OPLS4. The options are (A) OPLS4a, (B) OPLS3e, (C) both OPLS4a and OPLS3e same lowest, (D) insufficient, (E) OPLS4.
>
> The lowest is OPLS4 at +0.2. So answer E.
>
> Let me double check: OPLS3e = 0.5, OPLS4a = 0.5, OPLS4 = 0.2. Lowest is 0.2 = OPLS4. So E.
>
> Thus answer is E.

**Saved final answer, verbatim:**

> Looking at the "MSE (chi1 = 300)" column:
> - OPLS3e: +0.5 ± 0.2
> - OPLS4a: +0.5 ± 0.2
> - OPLS4: +0.2 ± 0.2
>
> The lowest value is +0.2, corresponding to OPLS4.
>
> [ANSWER]E[/ANSWER]

Reference choice: **E** — correct. Dataset accuracy: **88.1%** (215/244).

[Exact example records and source hashes](ADVISOR_GOOD_EXAMPLES.json)

[Additional protein-sequence examples and their limitations](EXAMPLES_SEQUENCE_VISION_TOOLS.md)

## Simple answer, substantial computation

### Does one amino-acid change make this protein less stable?

**Dataset:** BioEmu folding-free-energy benchmark

**Input:** Released 48-residue baseline 1ENH: AFSSEQLARLKREFNENRYLTERRRQQLSSELGLNEAQIKIWFQNKRA
Released 48-residue mutant 1ENH__Q6C: AFSSECLARLKREFNENRYLTERRRQQLSSELGLNEAQIKIWFQNKRA

**Plain-language question:** Given this protein sequence, does the benchmark's Q6C mutation make it less stable, and by how much?

**Reference answer:** Experimental reference: +0.90936 kcal/mol in ΔΔG, meaning the Q6C variant is less stable than the released 1ENH baseline. This is not a local model prediction.

**Evidence scope:** Not run with Qwen or BioEmu in this workspace for this example. The displayed answer is the released experimental reference; the question is an analyst paraphrase of the native numerical task.

**Wild type** (`1ENH`, 48 amino acids):

```text
AFSSEQLARLKREFNENRYLTERRRQQLSSELGLNEAQIKIWFQNKRA
```

**Mutant** (`1ENH__Q6C`, 48 amino acids):

```text
AFSSECLARLKREFNENRYLTERRRQQLSSELGLNEAQIKIWFQNKRA
```

Q6C is the released benchmark label and position 6 in these 48-residue sequences; it must not be assumed to be residue 6 of the full protein or the PDB author numbering.

**Required answer:** One numerical change in folding free energy, ΔΔG = ΔG(mutant) − ΔG(baseline), in kcal/mol. Its sign supports the simpler less-stable/more-stable interpretation.

**What must be computed:** A number is easy to print. Reproducing the released BioEmu estimate requires structural ensembles, geometric contact calculations and population statistics behind that number; an unsupported language-model guess does not reproduce this method.

**Tool route:** Sequence alignment and AlphaFold2 Evoformer embeddings → BioEmu structural ensembles → native-contact scores → folded populations → ΔG values → mutant-minus-baseline ΔΔG.

[Native task and evaluation source](https://github.com/microsoft/bioemu-benchmarks/blob/63edbfa2ee5f489d66a4bece96f242a1d28e567d/bioemu_benchmarks/assets/folding_free_energies_benchmark_0.1/folding_free_energies/system_info.csv)

1. For each sequence, obtain or reuse cached alignments and AlphaFold2 Evoformer single/pair embeddings; the release uses the ColabFold/MMseqs2 route when alignments are not supplied.
2. Sample BioEmu conformations for baseline and mutant. The released system metadata recommends 5,000 samples for each of these two cases.
3. Compute each sample's fraction of native contacts against the benchmark reference structure.
4. Convert contact scores to smooth foldedness with the native sigmoid (threshold 0.5, steepness 10), then average to estimate folded population p.
5. At the evaluator default 295 K, calculate ΔG = −k_B T ln[p/(1−p)] and subtract baseline ΔG from mutant ΔG.

The evaluator compares predicted energies with the experimental records. For this pair, the released reference energies are -2.61336 and -1.70400 kcal/mol; their difference is **+0.90936 kcal/mol**. These are reference measurements, not values computed by a run in this repository.

**Source code and records:** [testcases.csv](https://github.com/microsoft/bioemu-benchmarks/blob/63edbfa2ee5f489d66a4bece96f242a1d28e567d/bioemu_benchmarks/assets/folding_free_energies_benchmark_0.1/folding_free_energies/testcases.csv) · [system_info.csv](https://github.com/microsoft/bioemu-benchmarks/blob/63edbfa2ee5f489d66a4bece96f242a1d28e567d/bioemu_benchmarks/assets/folding_free_energies_benchmark_0.1/folding_free_energies/system_info.csv) · [free_energies.py](https://github.com/microsoft/bioemu-benchmarks/blob/63edbfa2ee5f489d66a4bece96f242a1d28e567d/bioemu_benchmarks/eval/folding_free_energies/free_energies.py) · [evaluate.py](https://github.com/microsoft/bioemu-benchmarks/blob/63edbfa2ee5f489d66a4bece96f242a1d28e567d/bioemu_benchmarks/eval/folding_free_energies/evaluate.py) · [get_embeds.py](https://github.com/microsoft/bioemu/blob/8451d90a0e9e22bd6d76da4186f4facc89b607a8/src/bioemu/get_embeds.py)

[Released example input](https://github.com/microsoft/bioemu-benchmarks/blob/63edbfa2ee5f489d66a4bece96f242a1d28e567d/bioemu_benchmarks/assets/folding_free_energies_benchmark_0.1/folding_free_energies/testcases.csv)

### Predict a protein's three-dimensional structure from its sequence

**Dataset:** ProteinBench single-state folding — CAMEO2022

**Input:** A released CAMEO2022 example is 7VRF chain A, the Drosophila Oxpecker chromodomain. The source row contains the 71-residue seqres sequence below and a 61-residue resolved seq field. Exact ProteinBench preprocessing of this row has not been independently reconstructed.

```text
NVKEKSSEYIVEKFLGKRYLRGRPQYLTKWEGYPIEQCTWEPLENLGKCMTLIADYEAELFQQSREKKNDQ
```

**Required answer:** A predicted three-dimensional protein structure: numerical atomic/backbone coordinates that can be compared with the experimental reference using native structural metrics such as TM-score and RMSD.

**What must be computed:** Naming the fold or describing the protein does not supply the required coordinates. A language model can serialize coordinates in principle, but reliable folding and structural comparison require capabilities not validated in our Qwen chat baseline.

**Tool route:** Pass the permitted sequence and prescribed sequence-alignment/template inputs to a folding model, then return its coordinate file and run structural comparison. AlphaFold2, OpenFold and ESMFold are evaluated folding models in ProteinBench; the selected model and access protocol must be recorded.

[Native task and evaluation source](https://arxiv.org/html/2409.06744v2#S2.SS2.SSS1)

[Released example input](https://github.com/bjing2016/EigenFold/blob/master/splits/cameo2022.csv)

### Build a scaffold around a specified three-dimensional motif

**Dataset:** MotifBench functional-motif scaffolding

**Input:** Official case 01_1LDB supplies the atomic coordinates of chain A residues 186–206 from lactate dehydrogenase 1LDB and specifies a 125-residue scaffold. Its released motif PDB contains the input geometry; the sequence identity of this motif is fixed.

**Required answer:** For native benchmark submission, 100 designed scaffold PDB files of the specified length, each retaining the motif geometry, plus scaffold_info.csv describing the motif placement. Evaluation assigns sequences, refolds them and compares structures.

**What must be computed:** A proposed amino-acid string or explanation lacks the scaffold coordinates and motif placement that the benchmark accepts. The new geometry must also survive computed refolding checks; merely asserting that the design folds cannot supply those results.

**Tool route:** Use a motif-conditioned structure generator to produce scaffold coordinates. The official evaluation then uses ProteinMPNN for sequence assignment, ESMFold for refolding, and geometric comparison; Foldseek supports clustering and novelty evaluation. AlphaFold is not the prescribed refolding tool here.

[Native task and evaluation source](https://github.com/blt2114/MotifBench#evaluation)

[Released example input](https://github.com/blt2114/MotifBench/blob/main/test_cases.csv)

## What AlphaFold contributes

AlphaFold predicts a protein's three-dimensional structure from its amino-acid sequence. In the BioEmu workflow above, AlphaFold2 supplies learned internal representations; BioEmu then samples many conformations. The final stability estimate requires additional calculations over that ensemble. A single predicted structure does not itself establish the experimental stability change. [BioEmu method](https://doi.org/10.1126/science.adv9817)

These examples document particular released workflows. They do not show that every possible solver must use AlphaFold, or that a general-purpose model has been tested successfully as their tool-using controller.

[More external-model computations and results reported in the papers](PUBLISHED_TOOL_USE_EXAMPLES.md)

[Full tool-case records, revisions and source hashes](TOOL_REQUIRED_CASES.json)
