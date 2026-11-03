# catalytic_activity_0196: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0196.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **C** — cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
METVESSSSAELLRAQTHFSRQVFSFQNFAALKCALQLGIPDAIKQHGKPMNLSELTSALPINPSKAPCIHRLMRLLVNAGYFAQENECFALTSLGRLLLKDDPLHIRALVLSEFHTALVMPWFALSEWFKNDDVAPFATAHGKSFWDYTSCDPELRNVFDGAMACDSHLIAKALVTEFKYLFEGLKSLVDVGGGNGTLARSIAKAFTNLKCTVCDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKSILHDWSDENCVKILKNCKRAISGKDKGGKVIVIDGVVELQKKAGNDDPGLDNMDMQMLVLFNSKERNEKEWAKLFSDAGFSDYGIVRTFGWWCIMELSP

[Multiple Choices]
A. tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-adenosyl-L-homocysteine + H(+)
B. L-proline betaine + NADPH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NADP(+) + H2O
C. cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)
D. N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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
```

</details>

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the archived and current UniProt sequence for IpeOMT1. Its catalytic-activity annotation names the cephaeline-to-emetine reaction and cites experimental evidence (ECO:0000269, PubMed 20061395), supporting choice C. The primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest a SAM-dependent plant O-methyltransferase, making the O-methylation in C more plausible than the N-methylations in A and D or the oxidative reaction in B. They do not establish that this protein acts on cephaeline specifically.


**Missing item-specific fact**

> The substrate specificity of this particular protein—its ability to methylate cephaeline to emetine—is not given in the input and requires protein-specific annotation or experimental knowledge.


**Reason**

> General enzyme-family clues can narrow the reaction type, but distinguishing the exact substrate and product requires an item-specific fact absent from the sequence prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched annotation supports C among the listed choices; the evidence provided does not establish another listed reaction for this protein.


### Important caveats

- The cited evidence is a UniProt annotation with an experimental evidence code, not an independent review of the underlying study.
- The actual source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest a SAM-dependent plant O-methyltransferase, making the O-methylation in C more plausible than the N-methylations in A and D or the oxidative reaction in B. They do not establish that this protein acts on cephaeline specifically.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The substrate specificity of this particular protein—its ability to methylate cephaeline to emetine—is not given in the input and requires protein-specific annotation or experimental knowledge.",
    "reason": "General enzyme-family clues can narrow the reaction type, but distinguishing the exact substrate and product requires an item-specific fact absent from the sequence prompt."
  },
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived and current UniProt sequence for IpeOMT1. Its catalytic-activity annotation names the cephaeline-to-emetine reaction and cites experimental evidence (ECO:0000269, PubMed 20061395), supporting choice C. The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The cited evidence is a UniProt annotation with an experimental evidence code, not an independent review of the underlying study.",
    "The actual source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports C among the listed choices; the evidence provided does not establish another listed reaction for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived and current UniProt sequence for IpeOMT1. Its catalytic-activity annotation names the cephaeline-to-emetine reaction and cites experimental evidence (ECO:0000269, PubMed 20061395), supporting choice C. The primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest a SAM-dependent plant O-methyltransferase, making the O-methylation in C more plausible than the N-methylations in A and D or the oxidative reaction in B. They do not establish that this protein acts on cephaeline specifically.",
    "missing_item_specific_fact": "The substrate specificity of this particular protein—its ability to methylate cephaeline to emetine—is not given in the input and requires protein-specific annotation or experimental knowledge.",
    "reason": "General enzyme-family clues can narrow the reaction type, but distinguishing the exact substrate and product requires an item-specific fact absent from the sequence prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports C among the listed choices; the evidence provided does not establish another listed reaction for this protein."
  },
  "important_caveats": [
    "The cited evidence is a UniProt annotation with an experimental evidence code, not an independent review of the underlying study.",
    "The actual source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt D3KY98 (OMT1_CARIP) exactly (350 AA, SHA256 confirmed). The recommended name is 'Cephaeline 6'-O-methyltransferase IpeOMT1' (EC 2.1.1.396), and the primary catalytic activity annotation (evidence ECO:0000269|PubMed:20061395, experimental) states exactly: cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+). This matches Choice C verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a 'VIVIDG' motif consistent with the Rossmann-like methyltransferase fold and SAM-binding, which could narrow the enzyme to a SAM-dependent methyltransferase. If one could also establish plant origin, choices A (animal PNMT) and D (animal COMT) might be disfavored, and B (oxidative demethylation requiring NADPH/O2) is mechanistically inconsistent with an OMT fold. However, determining that the specific substrate is cephaeline (a complex benzylisoquinoline alkaloid) rather than any of the thousands of other plant OMT substrates requires knowing this is IpeOMT1 from the ipecac alkaloid biosynthesis pathway (Nomura & Kutchan 2010). No sequence feature visible in the primary structure identifies cephaeline as the substrate.


**Missing item-specific fact**

> The specific identity of this protein as IpeOMT1 from Carapichea ipecacuanha and its experimentally determined preference for cephaeline 6'-O-methylation (EC 2.1.1.396), which is only obtainable from the UniProt annotation or the primary literature (PubMed:20061395).


**Reason**

> While the methyltransferase fold can be inferred from sequence motifs, the precise substrate (cephaeline vs. tyramine vs. a catecholamine vs. any of hundreds of other plant OMT substrates) cannot be deduced from the primary sequence. Selection of C over A and D ultimately depends on recognizing this as a plant O-methyltransferase acting on a benzylisoquinoline alkaloid, which is an item-specific database/literature fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the experimental annotation, C is the unique recommended catalytic activity. The other choices describe reactions catalyzed by mechanistically or taxonomically distinct enzymes (animal N-methyltransferases for A and D; a P450-type oxidative demethylase for B). No ambiguity in the correct answer itself, though the reasoning path to select C from sequence alone is weak.


### Important caveats

- The UniProt entry also lists multiple alternative OMT activities (norcoclaurine, deacetylisoipecoside, norprotosinomenine methylation) for this same protein, meaning the enzyme is promiscuous. The 'recommended' activity (cephaeline → emetine) is the one used for the question key.
- The entry was first publicly released in 2025-06-18; the underlying experimental data (PubMed:20061395, 2010) predates this. The evaluated model would not have had access to this Swiss-Prot entry at typical training cutoffs, making the question effectively a memorization test of the 2010 paper.
- Sequence-based identification of plant OMTs is possible in principle (VIVIDG motif, ~350 AA, plant-like composition), but distinguishing among hundreds of plant OMT substrates from sequence alone is not feasible without structural or database information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a 'VIVIDG' motif consistent with the Rossmann-like methyltransferase fold and SAM-binding, which could narrow the enzyme to a SAM-dependent methyltransferase. If one could also establish plant origin, choices A (animal PNMT) and D (animal COMT) might be disfavored, and B (oxidative demethylation requiring NADPH/O2) is mechanistically inconsistent with an OMT fold. However, determining that the specific substrate is cephaeline (a complex benzylisoquinoline alkaloid) rather than any of the thousands of other plant OMT substrates requires knowing this is IpeOMT1 from the ipecac alkaloid biosynthesis pathway (Nomura & Kutchan 2010). No sequence feature visible in the primary structure identifies cephaeline as the substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as IpeOMT1 from Carapichea ipecacuanha and its experimentally determined preference for cephaeline 6'-O-methylation (EC 2.1.1.396), which is only obtainable from the UniProt annotation or the primary literature (PubMed:20061395).",
    "reason": "While the methyltransferase fold can be inferred from sequence motifs, the precise substrate (cephaeline vs. tyramine vs. a catecholamine vs. any of hundreds of other plant OMT substrates) cannot be deduced from the primary sequence. Selection of C over A and D ultimately depends on recognizing this as a plant O-methyltransferase acting on a benzylisoquinoline alkaloid, which is an item-specific database/literature fact."
  },
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt D3KY98 (OMT1_CARIP) exactly (350 AA, SHA256 confirmed). The recommended name is 'Cephaeline 6'-O-methyltransferase IpeOMT1' (EC 2.1.1.396), and the primary catalytic activity annotation (evidence ECO:0000269|PubMed:20061395, experimental) states exactly: cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+). This matches Choice C verbatim."
  },
  "important_caveats": [
    "The UniProt entry also lists multiple alternative OMT activities (norcoclaurine, deacetylisoipecoside, norprotosinomenine methylation) for this same protein, meaning the enzyme is promiscuous. The 'recommended' activity (cephaeline → emetine) is the one used for the question key.",
    "The entry was first publicly released in 2025-06-18; the underlying experimental data (PubMed:20061395, 2010) predates this. The evaluated model would not have had access to this Swiss-Prot entry at typical training cutoffs, making the question effectively a memorization test of the 2010 paper.",
    "Sequence-based identification of plant OMTs is possible in principle (VIVIDG motif, ~350 AA, plant-like composition), but distinguishing among hundreds of plant OMT substrates from sequence alone is not feasible without structural or database information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental annotation, C is the unique recommended catalytic activity. The other choices describe reactions catalyzed by mechanistically or taxonomically distinct enzymes (animal N-methyltransferases for A and D; a P450-type oxidative demethylase for B). No ambiguity in the correct answer itself, though the reasoning path to select C from sequence alone is weak."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt D3KY98 (OMT1_CARIP) exactly (350 AA, SHA256 confirmed). The recommended name is 'Cephaeline 6'-O-methyltransferase IpeOMT1' (EC 2.1.1.396), and the primary catalytic activity annotation (evidence ECO:0000269|PubMed:20061395, experimental) states exactly: cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+). This matches Choice C verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a 'VIVIDG' motif consistent with the Rossmann-like methyltransferase fold and SAM-binding, which could narrow the enzyme to a SAM-dependent methyltransferase. If one could also establish plant origin, choices A (animal PNMT) and D (animal COMT) might be disfavored, and B (oxidative demethylation requiring NADPH/O2) is mechanistically inconsistent with an OMT fold. However, determining that the specific substrate is cephaeline (a complex benzylisoquinoline alkaloid) rather than any of the thousands of other plant OMT substrates requires knowing this is IpeOMT1 from the ipecac alkaloid biosynthesis pathway (Nomura & Kutchan 2010). No sequence feature visible in the primary structure identifies cephaeline as the substrate.",
    "missing_item_specific_fact": "The specific identity of this protein as IpeOMT1 from Carapichea ipecacuanha and its experimentally determined preference for cephaeline 6'-O-methylation (EC 2.1.1.396), which is only obtainable from the UniProt annotation or the primary literature (PubMed:20061395).",
    "reason": "While the methyltransferase fold can be inferred from sequence motifs, the precise substrate (cephaeline vs. tyramine vs. a catecholamine vs. any of hundreds of other plant OMT substrates) cannot be deduced from the primary sequence. Selection of C over A and D ultimately depends on recognizing this as a plant O-methyltransferase acting on a benzylisoquinoline alkaloid, which is an item-specific database/literature fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental annotation, C is the unique recommended catalytic activity. The other choices describe reactions catalyzed by mechanistically or taxonomically distinct enzymes (animal N-methyltransferases for A and D; a P450-type oxidative demethylase for B). No ambiguity in the correct answer itself, though the reasoning path to select C from sequence alone is weak."
  },
  "important_caveats": [
    "The UniProt entry also lists multiple alternative OMT activities (norcoclaurine, deacetylisoipecoside, norprotosinomenine methylation) for this same protein, meaning the enzyme is promiscuous. The 'recommended' activity (cephaeline → emetine) is the one used for the question key.",
    "The entry was first publicly released in 2025-06-18; the underlying experimental data (PubMed:20061395, 2010) predates this. The evaluated model would not have had access to this Swiss-Prot entry at typical training cutoffs, making the question effectively a memorization test of the 2010 paper.",
    "Sequence-based identification of plant OMTs is possible in principle (VIVIDG motif, ~350 AA, plant-like composition), but distinguishing among hundreds of plant OMT substrates from sequence alone is not feasible without structural or database information."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The historical UniProt record for the exact matched sequence lists the cephaeline-to-emetine reaction as catalytic activity and cites experimental evidence (ECO:0000269; PubMed 20061395).

Citations as saved: [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is about 350 residues long and contains a glycine-rich motif consistent with the SAM-binding region of plant small-molecule O-methyltransferases. That transferable family-level pattern favors a SAM-dependent oxygen methylation: C is the only offered SAM reaction that methylates oxygen, whereas A and D methylate nitrogen and B is an NADPH/O2-dependent reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition can meaningfully distinguish C among these choices without identifying the exact substrate from sequence alone. The sequence motif does not independently establish cephaeline specificity, but that finer detail is not needed to distinguish the offered reactions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C matches the expected O-methyltransferase reaction class among the offered choices.


### Important caveats

- The exact cephaeline substrate specificity is supported here by reviewer-only annotation evidence, not established by the sequence motif alone.
- The historical database annotation cites experimental evidence, but the underlying publication was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is about 350 residues long and contains a glycine-rich motif consistent with the SAM-binding region of plant small-molecule O-methyltransferases. That transferable family-level pattern favors a SAM-dependent oxygen methylation: C is the only offered SAM reaction that methylates oxygen, whereas A and D methylate nitrogen and B is an NADPH/O2-dependent reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition can meaningfully distinguish C among these choices without identifying the exact substrate from sequence alone. The sequence motif does not independently establish cephaeline specificity, but that finer detail is not needed to distinguish the offered reactions."
  },
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "H4"
    ],
    "judgment": "supported",
    "reason": "The historical UniProt record for the exact matched sequence lists the cephaeline-to-emetine reaction as catalytic activity and cites experimental evidence (ECO:0000269; PubMed 20061395)."
  },
  "important_caveats": [
    "The exact cephaeline substrate specificity is supported here by reviewer-only annotation evidence, not established by the sequence motif alone.",
    "The historical database annotation cites experimental evidence, but the underlying publication was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C matches the expected O-methyltransferase reaction class among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The historical UniProt record for the exact matched sequence lists the cephaeline-to-emetine reaction as catalytic activity and cites experimental evidence (ECO:0000269; PubMed 20061395).",
    "evidence_ids": ["H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is about 350 residues long and contains a glycine-rich motif consistent with the SAM-binding region of plant small-molecule O-methyltransferases. That transferable family-level pattern favors a SAM-dependent oxygen methylation: C is the only offered SAM reaction that methylates oxygen, whereas A and D methylate nitrogen and B is an NADPH/O2-dependent reaction.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition can meaningfully distinguish C among these choices without identifying the exact substrate from sequence alone. The sequence motif does not independently establish cephaeline specificity, but that finer detail is not needed to distinguish the offered reactions."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C matches the expected O-methyltransferase reaction class among the offered choices."
  },
  "important_caveats": [
    "The exact cephaeline substrate specificity is supported here by reviewer-only annotation evidence, not established by the sequence motif alone.",
    "The historical database annotation cites experimental evidence, but the underlying publication was not independently reviewed here."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer-only UniProt evidence (C4, C5, H1, H2, H4) confirms that the sequence (350 aa, exact match to D3KY98) is annotated as 'Cephaeline 6'-O-methyltransferase IpeOMT1' (EC 2.1.1.396), with the recommended catalytic activity being exactly 'cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)', supported by experimental evidence (ECO:0000269|PubMed:20061395, Nomura & Kutchan 2010). The sequence matches the source record in both current and historical (entry version 56) snapshots.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 350-residue sequence contains the conserved 'VGGGNG' glycine-rich SAM-binding motif (~positions 178-183), a hallmark of plant O-methyltransferases (OMTs) involved in lignin, flavonoid, and alkaloid biosynthesis. Plant OMTs are a well-characterized family (~350-360 aa) that catalyze SAM-dependent methylation of phenolic oxygen atoms, not nitrogen. This immediately eliminates Choice B (requires NADPH/O2, a cytochrome P450-type demethylation with entirely different cofactors and no SAM-binding motif). Choices A and D describe N-methyltransferase reactions (methylating an amine nitrogen), which is mechanistically inconsistent with the plant OMT family architecture identified by the GGGNG motif and overall sequence length. Choice C is the only option describing an O-methylation (cephaeline phenolic OH → emetine methoxy group) using SAM, matching the plant OMT family's characteristic reaction chemistry. A knowledgeable model recognizing the plant OMT family from the sequence can eliminate B (wrong cofactor), A and D (wrong atom methylated), leaving C as the sole O-methylation option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GGGNG SAM-binding motif and ~350 aa length are transferable features of the plant OMT family learned from many characterized plant methyltransferases (e.g., caffeic acid OMT, isoflavone OMTs, benzylisoquinoline OMTs). This family-level knowledge distinguishes O-methylation (C) from N-methylation (A, D) and P450 oxidation (B) without needing to recall this specific protein's database annotation. The specific substrate (cephaeline→emetine) need not be identified independently; it is the only O-methyltransferase reaction offered.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice B is eliminated by cofactor mismatch (NADPH/O2 vs SAM). Choices A and D are N-methyltransferases, inconsistent with the plant OMT family identified from the sequence. Only C describes an O-methylation with SAM, matching the family. No ambiguity among the offered alternatives.


### Important caveats

- The reviewer-only evidence confirms the annotation experimentally (ECO:0000269, PubMed 20061395), but this evidence was not available to the evaluated model.
- The protein also has multiple secondary catalytic activities (norcoclaurine OMT, norprotosinomenine OMT, deacetylisoipecoside OMT) per the UniProt entry, but none of these are offered as alternative choices, so they do not create ambiguity.
- The model's inference relies on recognizing the plant OMT family from the GGGNG motif and sequence length; if a model failed to recognize this motif, it might struggle to distinguish among SAM-dependent options A, C, and D purely on sequence features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 350-residue sequence contains the conserved 'VGGGNG' glycine-rich SAM-binding motif (~positions 178-183), a hallmark of plant O-methyltransferases (OMTs) involved in lignin, flavonoid, and alkaloid biosynthesis. Plant OMTs are a well-characterized family (~350-360 aa) that catalyze SAM-dependent methylation of phenolic oxygen atoms, not nitrogen. This immediately eliminates Choice B (requires NADPH/O2, a cytochrome P450-type demethylation with entirely different cofactors and no SAM-binding motif). Choices A and D describe N-methyltransferase reactions (methylating an amine nitrogen), which is mechanistically inconsistent with the plant OMT family architecture identified by the GGGNG motif and overall sequence length. Choice C is the only option describing an O-methylation (cephaeline phenolic OH → emetine methoxy group) using SAM, matching the plant OMT family's characteristic reaction chemistry. A knowledgeable model recognizing the plant OMT family from the sequence can eliminate B (wrong cofactor), A and D (wrong atom methylated), leaving C as the sole O-methylation option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GGGNG SAM-binding motif and ~350 aa length are transferable features of the plant OMT family learned from many characterized plant methyltransferases (e.g., caffeic acid OMT, isoflavone OMTs, benzylisoquinoline OMTs). This family-level knowledge distinguishes O-methylation (C) from N-methylation (A, D) and P450 oxidation (B) without needing to recall this specific protein's database annotation. The specific substrate (cephaeline→emetine) need not be identified independently; it is the only O-methyltransferase reaction offered."
  },
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only UniProt evidence (C4, C5, H1, H2, H4) confirms that the sequence (350 aa, exact match to D3KY98) is annotated as 'Cephaeline 6'-O-methyltransferase IpeOMT1' (EC 2.1.1.396), with the recommended catalytic activity being exactly 'cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)', supported by experimental evidence (ECO:0000269|PubMed:20061395, Nomura & Kutchan 2010). The sequence matches the source record in both current and historical (entry version 56) snapshots."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation experimentally (ECO:0000269, PubMed 20061395), but this evidence was not available to the evaluated model.",
    "The protein also has multiple secondary catalytic activities (norcoclaurine OMT, norprotosinomenine OMT, deacetylisoipecoside OMT) per the UniProt entry, but none of these are offered as alternative choices, so they do not create ambiguity.",
    "The model's inference relies on recognizing the plant OMT family from the GGGNG motif and sequence length; if a model failed to recognize this motif, it might struggle to distinguish among SAM-dependent options A, C, and D purely on sequence features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B is eliminated by cofactor mismatch (NADPH/O2 vs SAM). Choices A and D are N-methyltransferases, inconsistent with the plant OMT family identified from the sequence. Only C describes an O-methylation with SAM, matching the family. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only UniProt evidence (C4, C5, H1, H2, H4) confirms that the sequence (350 aa, exact match to D3KY98) is annotated as 'Cephaeline 6'-O-methyltransferase IpeOMT1' (EC 2.1.1.396), with the recommended catalytic activity being exactly 'cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)', supported by experimental evidence (ECO:0000269|PubMed:20061395, Nomura & Kutchan 2010). The sequence matches the source record in both current and historical (entry version 56) snapshots.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 350-residue sequence contains the conserved 'VGGGNG' glycine-rich SAM-binding motif (~positions 178-183), a hallmark of plant O-methyltransferases (OMTs) involved in lignin, flavonoid, and alkaloid biosynthesis. Plant OMTs are a well-characterized family (~350-360 aa) that catalyze SAM-dependent methylation of phenolic oxygen atoms, not nitrogen. This immediately eliminates Choice B (requires NADPH/O2, a cytochrome P450-type demethylation with entirely different cofactors and no SAM-binding motif). Choices A and D describe N-methyltransferase reactions (methylating an amine nitrogen), which is mechanistically inconsistent with the plant OMT family architecture identified by the GGGNG motif and overall sequence length. Choice C is the only option describing an O-methylation (cephaeline phenolic OH → emetine methoxy group) using SAM, matching the plant OMT family's characteristic reaction chemistry. A knowledgeable model recognizing the plant OMT family from the sequence can eliminate B (wrong cofactor), A and D (wrong atom methylated), leaving C as the sole O-methylation option.",
    "missing_item_specific_fact": "",
    "reason": "The GGGNG SAM-binding motif and ~350 aa length are transferable features of the plant OMT family learned from many characterized plant methyltransferases (e.g., caffeic acid OMT, isoflavone OMTs, benzylisoquinoline OMTs). This family-level knowledge distinguishes O-methylation (C) from N-methylation (A, D) and P450 oxidation (B) without needing to recall this specific protein's database annotation. The specific substrate (cephaeline→emetine) need not be identified independently; it is the only O-methyltransferase reaction offered."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B is eliminated by cofactor mismatch (NADPH/O2 vs SAM). Choices A and D are N-methyltransferases, inconsistent with the plant OMT family identified from the sequence. Only C describes an O-methylation with SAM, matching the family. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation experimentally (ECO:0000269, PubMed 20061395), but this evidence was not available to the evaluated model.",
    "The protein also has multiple secondary catalytic activities (norcoclaurine OMT, norprotosinomenine OMT, deacetylisoipecoside OMT) per the UniProt entry, but none of these are offered as alternative choices, so they do not create ambiguity.",
    "The model's inference relies on recognizing the plant OMT family from the GGGNG motif and sequence length; if a model failed to recognize this motif, it might struggle to distinguish among SAM-dependent options A, C, and D purely on sequence features."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "D3KY98",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "ab6b8f525c4405adcc9e2f43d65d1e3b7ba98c49c094274d62c7598adf3167f9",
  "benchmark_sequence_length": 350,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 58,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-04-20",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "current_source_sequence_sha256": "ab6b8f525c4405adcc9e2f43d65d1e3b7ba98c49c094274d62c7598adf3167f9",
  "current_source_sequence_length": 350,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 56,
  "selected_historical_version": {
    "accession": "D3KY98",
    "database": "Swiss-Prot",
    "entryVersion": 56,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OMT1_CARIP",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "selected_historical_source_sequence_sha256": "ab6b8f525c4405adcc9e2f43d65d1e3b7ba98c49c094274d62c7598adf3167f9",
  "selected_historical_source_sequence_length": 350,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 56,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"D3KY98\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":58,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-04-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.128\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"(R,S)-norcoclaurine 6-O-methyltransferase IpeOMT1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Coclaurine synthase IpeOMT1\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"(R,S)-norprotosinomenine 6-O-methyltransferase IpeOMT1\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"7-O-methyl-N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Ipecac/benzylisoquinoline alkaloid O-methyltransferase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI79243.1\",\"source\":\"EMBL\"}],\"value\":\"IpeOMT1\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Isococlaurine 6-O-methyltransferase IpeOMT1\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.396\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Cephaeline 6'-O-methyltransferase IpeOMT1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Emetine synthase IpeOMT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80660\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.396\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"name\":\"cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80659\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:149548\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231587\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80664\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"name\":\"deacetylisoipecoside + S-adenosyl-L-methionine = 6-O-methyldeacetylisoipecoside + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80663\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58091\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229555\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80668\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"name\":\"7-O-methyldeacetylisoipecoside + S-adenosyl-L-methionine = 6,7-O,O-dimethyldeacetylisoipecoside + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80667\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231626\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231627\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:19942\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.128\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"name\":\"norcoclaurine + S-adenosyl-L-methionine = coclaurine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19941\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58481\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58482\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80696\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"name\":\"(S)-norprotosinomenine + S-adenosyl-L-methionine = (S)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80695\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231630\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231632\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/comments/6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80700\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"name\":\"(R)-norprotosinomenine + S-adenosyl-L-methionine = (R)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80699\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231631\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231633\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Nomura T.\",\"Kutchan T.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20061395\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.086157\"}],\"citationType\":\"journal article\",\"firstPage\":\"7722\",\"id\":\"20061395\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"7738\",\"publicationDate\":\"2010\",\"title\":\"Three new O-methyltransferases are sufficient for all O-methylation reactions of ipecac alkaloid biosynthesis in root culture of Psychotria ipecacuanha.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI79243.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "source_locator": "lines 1-29",
  "excerpt": "ID   OMT1_CARIP              Reviewed;         350 AA.\nAC   D3KY98;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-APR-2010, sequence version 1.\nDT   28-JAN-2026, entry version 56.\nDE   RecName: Full=Cephaeline 6'-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            Short=Emetine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.396 {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=(R,S)-norcoclaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            Short=Coclaurine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.128 {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=(R,S)-norprotosinomenine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=7-O-methyl-N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=Ipecac/benzylisoquinoline alkaloid O-methyltransferase 1 {ECO:0000303|PubMed:20061395};\nDE            Short=IpeOMT1 {ECO:0000303|PubMed:20061395, ECO:0000312|EMBL:BAI79243.1};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=Isococlaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nGN   Name=OMT1 {ECO:0000303|PubMed:20061395};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 56,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "source_locator": "lines 6-22",
  "excerpt": "DE   RecName: Full=Cephaeline 6'-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            Short=Emetine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.396 {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=(R,S)-norcoclaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            Short=Coclaurine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.128 {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=(R,S)-norprotosinomenine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=7-O-methyl-N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=Ipecac/benzylisoquinoline alkaloid O-methyltransferase 1 {ECO:0000303|PubMed:20061395};\nDE            Short=IpeOMT1 {ECO:0000303|PubMed:20061395, ECO:0000312|EMBL:BAI79243.1};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=Isococlaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 56,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "source_locator": "lines 30-40",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAI79243.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, PATHWAY, AND TISSUE\nRP   SPECIFICITY.\nRC   TISSUE=Root;\nRX   PubMed=20061395; DOI=10.1074/jbc.m109.086157;\nRA   Nomura T., Kutchan T.M.;\nRT   \"Three new O-methyltransferases are sufficient for all O-methylation\nRT   reactions of ipecac alkaloid biosynthesis in root culture of Psychotria\nRT   ipecacuanha.\";\nRL   J. Biol. Chem. 285:7722-7738(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 56,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "source_locator": "lines 54-61",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-\nCC         homocysteine + H(+); Xref=Rhea:RHEA:80659, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:149548,\nCC         ChEBI:CHEBI:231587; EC=2.1.1.396;\nCC         Evidence={ECO:0000269|PubMed:20061395};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80660;\nCC         Evidence={ECO:0000269|PubMed:20061395};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 56,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "source_locator": "lines 62-69",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=deacetylisoipecoside + S-adenosyl-L-methionine = 6-O-\nCC         methyldeacetylisoipecoside + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:80663, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:58091, ChEBI:CHEBI:59789, ChEBI:CHEBI:229555;\nCC         Evidence={ECO:0000269|PubMed:20061395};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80664;\nCC         Evidence={ECO:0000269|PubMed:20061395};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 56,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "source_locator": "lines 70-77",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=7-O-methyldeacetylisoipecoside + S-adenosyl-L-methionine =\nCC         6,7-O,O-dimethyldeacetylisoipecoside + S-adenosyl-L-homocysteine +\nCC         H(+); Xref=Rhea:RHEA:80667, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231626, ChEBI:CHEBI:231627;\nCC         Evidence={ECO:0000269|PubMed:20061395};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80668;\nCC         Evidence={ECO:0000269|PubMed:20061395};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 56,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "source_locator": "lines 78-85",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=norcoclaurine + S-adenosyl-L-methionine = coclaurine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:19941,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58481,\nCC         ChEBI:CHEBI:58482, ChEBI:CHEBI:59789; EC=2.1.1.128;\nCC         Evidence={ECO:0000269|PubMed:20061395};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19942;\nCC         Evidence={ECO:0000269|PubMed:20061395};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 56,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "source_locator": "lines 86-93",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(S)-norprotosinomenine + S-adenosyl-L-methionine = (S)-6-O-\nCC         methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:80695, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231630, ChEBI:CHEBI:231632;\nCC         Evidence={ECO:0000269|PubMed:20061395};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80696;\nCC         Evidence={ECO:0000269|PubMed:20061395};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 56,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "source_locator": "lines 94-101",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(R)-norprotosinomenine + S-adenosyl-L-methionine = (R)-6-O-\nCC         methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:80699, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231631, ChEBI:CHEBI:231633;\nCC         Evidence={ECO:0000269|PubMed:20061395};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80700;\nCC         Evidence={ECO:0000269|PubMed:20061395};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 56,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 196. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
