# GO_molecular_function_0022: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0022.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **D** — ubiquitin-protein transferase activity

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MPVILNFSSERVLSESELEALRHVGRVSQSEQLVVRGRTMRLHHISFMDSFSVEPVSGGLLDRLSARGHRLLAENLEIQLNRGHTFLQAFRLYMEQSRATPCTRQNVSSAIQNKINSHAFTVSHQDFSCHEQHLNCPITLCIPETGVFVRNAKNSEICSLYDHNALTELIRRNAPHPLSREPFVPEMIVSKDECHFNLIEQYFCILATQNICTRI

[Multiple Choices]
A. phosphopantothenoylcysteine decarboxylase activity
B. amidophosphoribosyltransferase activity
C. nucleic acid binding
D. ubiquitin-protein transferase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the recorded 215-aa E. coli O157:H7 NleG8 protein. Its UniProt entry identifies it as an E3 ubiquitin-protein ligase and records experimental evidence for ubiquitin transfer activity, supporting choice D. The evidence is an annotation citing a publication, not an independently reviewed primary-paper result here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a sufficiently specific, general biological argument to identify this particular protein’s ubiquitin-transfer activity. The alternatives name distinct functions, but recognizing which one applies requires protein-specific functional knowledge.


**Missing item-specific fact**

> That this sequence is NleG8, an E3 ubiquitin-protein ligase with experimentally supported ubiquitin-transfer activity.


**Reason**

> The sequence is the only biological input, and no organism or protein annotation is given. The decisive NleG8 identity and its experimental functional characterization are external, item-specific facts; reviewer-only database evidence cannot make the question reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched functional evidence supports D, and the listed alternatives describe different activities. No competing option is comparably supported by the supplied evidence.


### Important caveats

- The exact author source snapshot is unknown, although the sequence matches both the current and checked historical UniProt records.
- The reviewer-only experimental evidence supports the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific, general biological argument to identify this particular protein’s ubiquitin-transfer activity. The alternatives name distinct functions, but recognizing which one applies requires protein-specific functional knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence is NleG8, an E3 ubiquitin-protein ligase with experimentally supported ubiquitin-transfer activity.",
    "reason": "The sequence is the only biological input, and no organism or protein annotation is given. The decisive NleG8 identity and its experimental functional characterization are external, item-specific facts; reviewer-only database evidence cannot make the question reasoning-supported."
  },
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the recorded 215-aa E. coli O157:H7 NleG8 protein. Its UniProt entry identifies it as an E3 ubiquitin-protein ligase and records experimental evidence for ubiquitin transfer activity, supporting choice D. The evidence is an annotation citing a publication, not an independently reviewed primary-paper result here."
  },
  "important_caveats": [
    "The exact author source snapshot is unknown, although the sequence matches both the current and checked historical UniProt records.",
    "The reviewer-only experimental evidence supports the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched functional evidence supports D, and the listed alternatives describe different activities. No competing option is comparably supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the recorded 215-aa E. coli O157:H7 NleG8 protein. Its UniProt entry identifies it as an E3 ubiquitin-protein ligase and records experimental evidence for ubiquitin transfer activity, supporting choice D. The evidence is an annotation citing a publication, not an independently reviewed primary-paper result here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific, general biological argument to identify this particular protein’s ubiquitin-transfer activity. The alternatives name distinct functions, but recognizing which one applies requires protein-specific functional knowledge.",
    "missing_item_specific_fact": "That this sequence is NleG8, an E3 ubiquitin-protein ligase with experimentally supported ubiquitin-transfer activity.",
    "reason": "The sequence is the only biological input, and no organism or protein annotation is given. The decisive NleG8 identity and its experimental functional characterization are external, item-specific facts; reviewer-only database evidence cannot make the question reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched functional evidence supports D, and the listed alternatives describe different activities. No competing option is comparably supported by the supplied evidence."
  },
  "important_caveats": [
    "The exact author source snapshot is unknown, although the sequence matches both the current and checked historical UniProt records.",
    "The reviewer-only experimental evidence supports the key but was not available to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8XAN6 (NleG8, E. coli O157:H7) is annotated as 'E3 ubiquitin-protein ligase NleG' with EC 2.3.2.27, supported by experimental evidence (ECO:0000269, PubMed:36511702). The GO annotation GO:0061630 (ubiquitin protein ligase activity) is is_a GO:0004842 (ubiquitin-protein transferase activity), which matches option D exactly. The catalytic activity reaction (C6/H4) confirms ubiquitin transferase function. Sequence match is confirmed (SHA256 identical, 215 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO4](#evidence-go4), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the 215-aa sequence contains a compact cysteine-rich motif (…DECHFNLIEQYFCILATQNICTRI) with Cys residues spaced at intervals consistent with a U-box domain (a modified RING-finger fold). U-box domains are well-established structural hallmarks of E3 ubiquitin-protein ligases. The small protein size (~215 aa), bacterial origin, and absence of catalytic residues characteristic of phosphopantothenoylcysteine decarboxylase (FMN-dependent decarboxylase) or amidophosphoribosyltransferase (large glutamine amidotransferase) further disfavor options A and B. Option C (nucleic acid binding) lacks any recognizable DNA/RNA-binding motif (e.g., helix-turn-helix, zinc finger with specific spacing, or arginine-rich patch). Thus, the Cys-rich C-terminal signature pointing to a U-box/E3 ligase fold provides a concrete structural-biology argument distinguishing D.


**Missing item-specific fact**

> Precise confirmation that this specific Cys pattern is a bona fide U-box (rather than a generic Cys-rich or zinc-binding motif) would benefit from the crystal structure (PDB 6XNJ, residues 206–215 in complex with GOPC), but the sequence-level Cys spacing is a legitimate and commonly used heuristic in structural biology.


**Reason**

> A biologist examining the sequence can note the C-terminal cysteine-rich compact region, recognize it as consistent with a U-box/RING-like fold, and connect that fold to E3 ubiquitin ligase activity. The other options require specific catalytic architectures (FMN-binding pocket for PPCDC, glutamine amidotransferase domain for PRPP amidotransferase) that are absent from the sequence. This constitutes a defensible biological reasoning chain, though U-box recognition from raw sequence is non-trivial and benefits from structural-biology expertise.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C (nucleic acid binding) is extremely broad but no recognizable nucleic-acid-binding motif is present. Options A and B require specific enzymatic active-site architectures not evident in the sequence. The Cys-rich C-terminal region uniquely points toward D among the four choices.


### Important caveats

- The UniProt entry was first publicly released 2025-06-18; the benchmark's exact author source snapshot is unknown. However, the sequence version 1 dates to 2002-03-01 and is unchanged, so the sequence itself was available long before the functional annotation.
- The GO annotation evidence code is EXP (experimental, PubMed:36511702, 2023), meaning the E3 ligase activity was established experimentally, not merely by computational inference.
- U-box domain identification from sequence alone is a heuristic; the definitive confirmation came from X-ray crystallography (PDB 6XNJ, residues 206–215). A model relying solely on sequence would be applying a well-known but imperfect structural motif prediction.
- The reviewer-only evidence was absent from the evaluated model input; the model must rely on the raw sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the 215-aa sequence contains a compact cysteine-rich motif (…DECHFNLIEQYFCILATQNICTRI) with Cys residues spaced at intervals consistent with a U-box domain (a modified RING-finger fold). U-box domains are well-established structural hallmarks of E3 ubiquitin-protein ligases. The small protein size (~215 aa), bacterial origin, and absence of catalytic residues characteristic of phosphopantothenoylcysteine decarboxylase (FMN-dependent decarboxylase) or amidophosphoribosyltransferase (large glutamine amidotransferase) further disfavor options A and B. Option C (nucleic acid binding) lacks any recognizable DNA/RNA-binding motif (e.g., helix-turn-helix, zinc finger with specific spacing, or arginine-rich patch). Thus, the Cys-rich C-terminal signature pointing to a U-box/E3 ligase fold provides a concrete structural-biology argument distinguishing D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise confirmation that this specific Cys pattern is a bona fide U-box (rather than a generic Cys-rich or zinc-binding motif) would benefit from the crystal structure (PDB 6XNJ, residues 206–215 in complex with GOPC), but the sequence-level Cys spacing is a legitimate and commonly used heuristic in structural biology.",
    "reason": "A biologist examining the sequence can note the C-terminal cysteine-rich compact region, recognize it as consistent with a U-box/RING-like fold, and connect that fold to E3 ubiquitin ligase activity. The other options require specific catalytic architectures (FMN-binding pocket for PPCDC, glutamine amidotransferase domain for PRPP amidotransferase) that are absent from the sequence. This constitutes a defensible biological reasoning chain, though U-box recognition from raw sequence is non-trivial and benefits from structural-biology expertise."
  },
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "H5",
      "GO4",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8XAN6 (NleG8, E. coli O157:H7) is annotated as 'E3 ubiquitin-protein ligase NleG' with EC 2.3.2.27, supported by experimental evidence (ECO:0000269, PubMed:36511702). The GO annotation GO:0061630 (ubiquitin protein ligase activity) is is_a GO:0004842 (ubiquitin-protein transferase activity), which matches option D exactly. The catalytic activity reaction (C6/H4) confirms ubiquitin transferase function. Sequence match is confirmed (SHA256 identical, 215 aa)."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released 2025-06-18; the benchmark's exact author source snapshot is unknown. However, the sequence version 1 dates to 2002-03-01 and is unchanged, so the sequence itself was available long before the functional annotation.",
    "The GO annotation evidence code is EXP (experimental, PubMed:36511702, 2023), meaning the E3 ligase activity was established experimentally, not merely by computational inference.",
    "U-box domain identification from sequence alone is a heuristic; the definitive confirmation came from X-ray crystallography (PDB 6XNJ, residues 206–215). A model relying solely on sequence would be applying a well-known but imperfect structural motif prediction.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on the raw sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (nucleic acid binding) is extremely broad but no recognizable nucleic-acid-binding motif is present. Options A and B require specific enzymatic active-site architectures not evident in the sequence. The Cys-rich C-terminal region uniquely points toward D among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8XAN6 (NleG8, E. coli O157:H7) is annotated as 'E3 ubiquitin-protein ligase NleG' with EC 2.3.2.27, supported by experimental evidence (ECO:0000269, PubMed:36511702). The GO annotation GO:0061630 (ubiquitin protein ligase activity) is is_a GO:0004842 (ubiquitin-protein transferase activity), which matches option D exactly. The catalytic activity reaction (C6/H4) confirms ubiquitin transferase function. Sequence match is confirmed (SHA256 identical, 215 aa).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4", "H5", "GO4", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the 215-aa sequence contains a compact cysteine-rich motif (…DECHFNLIEQYFCILATQNICTRI) with Cys residues spaced at intervals consistent with a U-box domain (a modified RING-finger fold). U-box domains are well-established structural hallmarks of E3 ubiquitin-protein ligases. The small protein size (~215 aa), bacterial origin, and absence of catalytic residues characteristic of phosphopantothenoylcysteine decarboxylase (FMN-dependent decarboxylase) or amidophosphoribosyltransferase (large glutamine amidotransferase) further disfavor options A and B. Option C (nucleic acid binding) lacks any recognizable DNA/RNA-binding motif (e.g., helix-turn-helix, zinc finger with specific spacing, or arginine-rich patch). Thus, the Cys-rich C-terminal signature pointing to a U-box/E3 ligase fold provides a concrete structural-biology argument distinguishing D.",
    "missing_item_specific_fact": "Precise confirmation that this specific Cys pattern is a bona fide U-box (rather than a generic Cys-rich or zinc-binding motif) would benefit from the crystal structure (PDB 6XNJ, residues 206–215 in complex with GOPC), but the sequence-level Cys spacing is a legitimate and commonly used heuristic in structural biology.",
    "reason": "A biologist examining the sequence can note the C-terminal cysteine-rich compact region, recognize it as consistent with a U-box/RING-like fold, and connect that fold to E3 ubiquitin ligase activity. The other options require specific catalytic architectures (FMN-binding pocket for PPCDC, glutamine amidotransferase domain for PRPP amidotransferase) that are absent from the sequence. This constitutes a defensible biological reasoning chain, though U-box recognition from raw sequence is non-trivial and benefits from structural-biology expertise."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (nucleic acid binding) is extremely broad but no recognizable nucleic-acid-binding motif is present. Options A and B require specific enzymatic active-site architectures not evident in the sequence. The Cys-rich C-terminal region uniquely points toward D among the four choices."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released 2025-06-18; the benchmark's exact author source snapshot is unknown. However, the sequence version 1 dates to 2002-03-01 and is unchanged, so the sequence itself was available long before the functional annotation.",
    "The GO annotation evidence code is EXP (experimental, PubMed:36511702, 2023), meaning the E3 ligase activity was established experimentally, not merely by computational inference.",
    "U-box domain identification from sequence alone is a heuristic; the definitive confirmation came from X-ray crystallography (PDB 6XNJ, residues 206–215). A model relying solely on sequence would be applying a well-known but imperfect structural motif prediction.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on the raw sequence and general biological knowledge."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record describes the protein as an E3 ubiquitin-protein ligase and reports an experimentally supported ubiquitin-transfer reaction. That activity fits option D, ubiquitin-protein transferase activity.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short, cysteine-containing sequence is consistent with a bacterial NleG-type effector; transferable knowledge of this protein family links its conserved C-terminal region to E3 ubiquitin-ligase activity. That favors D over the unrelated metabolic enzyme activities in A and B and nucleic acid binding in C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference offers a meaningful basis for choosing D without needing this exact protein's database annotation. The family assignment may be uncertain from sequence alone, but the options make the inference discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, ubiquitin-protein transferase activity is the clearly fitting function.


### Important caveats

- The functional annotation is reviewer-only evidence, not an original input; it supports the key but is not the basis for the transferability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short, cysteine-containing sequence is consistent with a bacterial NleG-type effector; transferable knowledge of this protein family links its conserved C-terminal region to E3 ubiquitin-ligase activity. That favors D over the unrelated metabolic enzyme activities in A and B and nucleic acid binding in C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference offers a meaningful basis for choosing D without needing this exact protein's database annotation. The family assignment may be uncertain from sequence alone, but the options make the inference discriminating."
  },
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes the protein as an E3 ubiquitin-protein ligase and reports an experimentally supported ubiquitin-transfer reaction. That activity fits option D, ubiquitin-protein transferase activity."
  },
  "important_caveats": [
    "The functional annotation is reviewer-only evidence, not an original input; it supports the key but is not the basis for the transferability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, ubiquitin-protein transferase activity is the clearly fitting function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes the protein as an E3 ubiquitin-protein ligase and reports an experimentally supported ubiquitin-transfer reaction. That activity fits option D, ubiquitin-protein transferase activity.",
    "evidence_ids": ["H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short, cysteine-containing sequence is consistent with a bacterial NleG-type effector; transferable knowledge of this protein family links its conserved C-terminal region to E3 ubiquitin-ligase activity. That favors D over the unrelated metabolic enzyme activities in A and B and nucleic acid binding in C.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference offers a meaningful basis for choosing D without needing this exact protein's database annotation. The family assignment may be uncertain from sequence alone, but the options make the inference discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, ubiquitin-protein transferase activity is the clearly fitting function."
  },
  "important_caveats": [
    "The functional annotation is reviewer-only evidence, not an original input; it supports the key but is not the basis for the transferability judgment."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q8XAN6) annotates this protein as 'E3 ubiquitin-protein ligase NleG' with EC 2.3.2.27, supported by experimental evidence (ECO:0000269, PubMed:36511702). The GO annotation GO:0061630 (ubiquitin protein ligase activity) is a child of GO:0004842 (ubiquitin-protein transferase activity), which is the text of option D. The catalytic activity comment explicitly describes the ubiquitin transfer reaction. The sequence match is confirmed (215 aa, SHA256 match).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO4](#evidence-go4), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 215-aa protein has a cysteine-rich C-terminal region (~8 cysteines, with a cluster in the last ~80 residues including the terminal Cys), which is structurally consistent with U-box or RING-like E3 ligase catalytic domains found in many ubiquitin ligases (e.g., U-box proteins, RING E3s). Option B (amidophosphoribosyltransferase, PurF) is eliminated by size: bacterial PurF is ~550 aa with a glutamine amidotransferase domain, far larger than 215 aa. Option A (phosphopantothenoylcysteine decarboxylase, CoaE) requires an FMN-binding flavoprotein domain with specific catalytic residues absent here. Option C (nucleic acid binding) is a broad category but the sequence lacks canonical nucleic-acid-binding motifs (HTH, RGG, classic C2H2 zinc fingers with proper spacing); the cysteine spacing pattern is more consistent with a cross-brace U-box/RING topology than with nucleic acid contact. Knowledge of bacterial T3SS effectors (NleG family) that mimic host E3 ligases via a C-terminal U-box domain provides family-level context: small (~200 aa) effectors with a conserved C-terminal cysteine cluster conferring ubiquitin ligase activity. Together, the size constraint, cysteine clustering pattern, and absence of motifs for A/B/C make D the most defensible choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides concrete features (small size eliminating B, absence of FMN motifs for A, cysteine-rich C-terminal cluster suggestive of U-box/RING E3 ligase rather than nucleic acid binding) that, combined with transferable knowledge of E3 ligase domain architecture and bacterial effector mimicry, meaningfully distinguish D from the other options without requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is clearly eliminated by size. Option A lacks required FMN-binding motifs. Option C is less consistent with the cysteine clustering pattern than D. While C is a broad term, the specific cysteine spacing and absence of nucleic acid binding motifs make D the stronger inference. No two options are equally defensible given the sequence features.


### Important caveats

- The cysteine pattern is suggestive but not definitive for E3 ligase activity; other small cysteine-rich proteins exist with different functions.
- Recognition of this as an NleG-family protein specifically would require prior knowledge of E. coli T3SS effectors, but the U-box/RING cysteine-cluster inference is transferable from many E3 ligase families.
- The GO term in option D (GO:0004842, ubiquitin-protein transferase activity) is the parent of the annotated GO:0061630 (ubiquitin protein ligase activity), so the broader term is technically correct.
- The experimental evidence (PubMed:36511702, 2023) postdates the original sequence deposition (2002); the annotation was added later, meaning the benchmark key reflects relatively recent experimental characterization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 215-aa protein has a cysteine-rich C-terminal region (~8 cysteines, with a cluster in the last ~80 residues including the terminal Cys), which is structurally consistent with U-box or RING-like E3 ligase catalytic domains found in many ubiquitin ligases (e.g., U-box proteins, RING E3s). Option B (amidophosphoribosyltransferase, PurF) is eliminated by size: bacterial PurF is ~550 aa with a glutamine amidotransferase domain, far larger than 215 aa. Option A (phosphopantothenoylcysteine decarboxylase, CoaE) requires an FMN-binding flavoprotein domain with specific catalytic residues absent here. Option C (nucleic acid binding) is a broad category but the sequence lacks canonical nucleic-acid-binding motifs (HTH, RGG, classic C2H2 zinc fingers with proper spacing); the cysteine spacing pattern is more consistent with a cross-brace U-box/RING topology than with nucleic acid contact. Knowledge of bacterial T3SS effectors (NleG family) that mimic host E3 ligases via a C-terminal U-box domain provides family-level context: small (~200 aa) effectors with a conserved C-terminal cysteine cluster conferring ubiquitin ligase activity. Together, the size constraint, cysteine clustering pattern, and absence of motifs for A/B/C make D the most defensible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides concrete features (small size eliminating B, absence of FMN motifs for A, cysteine-rich C-terminal cluster suggestive of U-box/RING E3 ligase rather than nucleic acid binding) that, combined with transferable knowledge of E3 ligase domain architecture and bacterial effector mimicry, meaningfully distinguish D from the other options without requiring recall of this specific protein's database entry."
  },
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "GO4",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q8XAN6) annotates this protein as 'E3 ubiquitin-protein ligase NleG' with EC 2.3.2.27, supported by experimental evidence (ECO:0000269, PubMed:36511702). The GO annotation GO:0061630 (ubiquitin protein ligase activity) is a child of GO:0004842 (ubiquitin-protein transferase activity), which is the text of option D. The catalytic activity comment explicitly describes the ubiquitin transfer reaction. The sequence match is confirmed (215 aa, SHA256 match)."
  },
  "important_caveats": [
    "The cysteine pattern is suggestive but not definitive for E3 ligase activity; other small cysteine-rich proteins exist with different functions.",
    "Recognition of this as an NleG-family protein specifically would require prior knowledge of E. coli T3SS effectors, but the U-box/RING cysteine-cluster inference is transferable from many E3 ligase families.",
    "The GO term in option D (GO:0004842, ubiquitin-protein transferase activity) is the parent of the annotated GO:0061630 (ubiquitin protein ligase activity), so the broader term is technically correct.",
    "The experimental evidence (PubMed:36511702, 2023) postdates the original sequence deposition (2002); the annotation was added later, meaning the benchmark key reflects relatively recent experimental characterization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is clearly eliminated by size. Option A lacks required FMN-binding motifs. Option C is less consistent with the cysteine clustering pattern than D. While C is a broad term, the specific cysteine spacing and absence of nucleic acid binding motifs make D the stronger inference. No two options are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q8XAN6) annotates this protein as 'E3 ubiquitin-protein ligase NleG' with EC 2.3.2.27, supported by experimental evidence (ECO:0000269, PubMed:36511702). The GO annotation GO:0061630 (ubiquitin protein ligase activity) is a child of GO:0004842 (ubiquitin-protein transferase activity), which is the text of option D. The catalytic activity comment explicitly describes the ubiquitin transfer reaction. The sequence match is confirmed (215 aa, SHA256 match).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "GO4", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 215-aa protein has a cysteine-rich C-terminal region (~8 cysteines, with a cluster in the last ~80 residues including the terminal Cys), which is structurally consistent with U-box or RING-like E3 ligase catalytic domains found in many ubiquitin ligases (e.g., U-box proteins, RING E3s). Option B (amidophosphoribosyltransferase, PurF) is eliminated by size: bacterial PurF is ~550 aa with a glutamine amidotransferase domain, far larger than 215 aa. Option A (phosphopantothenoylcysteine decarboxylase, CoaE) requires an FMN-binding flavoprotein domain with specific catalytic residues absent here. Option C (nucleic acid binding) is a broad category but the sequence lacks canonical nucleic-acid-binding motifs (HTH, RGG, classic C2H2 zinc fingers with proper spacing); the cysteine spacing pattern is more consistent with a cross-brace U-box/RING topology than with nucleic acid contact. Knowledge of bacterial T3SS effectors (NleG family) that mimic host E3 ligases via a C-terminal U-box domain provides family-level context: small (~200 aa) effectors with a conserved C-terminal cysteine cluster conferring ubiquitin ligase activity. Together, the size constraint, cysteine clustering pattern, and absence of motifs for A/B/C make D the most defensible choice.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides concrete features (small size eliminating B, absence of FMN motifs for A, cysteine-rich C-terminal cluster suggestive of U-box/RING E3 ligase rather than nucleic acid binding) that, combined with transferable knowledge of E3 ligase domain architecture and bacterial effector mimicry, meaningfully distinguish D from the other options without requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is clearly eliminated by size. Option A lacks required FMN-binding motifs. Option C is less consistent with the cysteine clustering pattern than D. While C is a broad term, the specific cysteine spacing and absence of nucleic acid binding motifs make D the stronger inference. No two options are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The cysteine pattern is suggestive but not definitive for E3 ligase activity; other small cysteine-rich proteins exist with different functions.",
    "Recognition of this as an NleG-family protein specifically would require prior knowledge of E. coli T3SS effectors, but the U-box/RING cysteine-cluster inference is transferable from many E3 ligase families.",
    "The GO term in option D (GO:0004842, ubiquitin-protein transferase activity) is the parent of the annotated GO:0061630 (ubiquitin protein ligase activity), so the broader term is technically correct.",
    "The experimental evidence (PubMed:36511702, 2023) postdates the original sequence deposition (2002); the annotation was added later, meaning the benchmark key reflects relatively recent experimental characterization."
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
  "requested_accession": "Q8XAN6",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "ebd4800979a86f7074a5ae32983d282e50962a3735f30deb653b969a18f418ac",
  "benchmark_sequence_length": 215,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 130,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-03-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "current_source_sequence_sha256": "ebd4800979a86f7074a5ae32983d282e50962a3735f30deb653b969a18f418ac",
  "current_source_sequence_length": 215,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 129,
  "selected_historical_version": {
    "accession": "Q8XAN6",
    "database": "Swiss-Prot",
    "entryVersion": 129,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "NLEG8_ECO57",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "selected_historical_source_sequence_sha256": "ebd4800979a86f7074a5ae32983d282e50962a3735f30deb653b969a18f418ac",
  "selected_historical_source_sequence_length": 215,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 129,
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q8XAN6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":130,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli O157:H7\",\"taxonId\":83334}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"value\":\"2.3.2.27\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"E3 ubiquitin-protein ligase NleG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"value\":\"Effector proteins function to alter host cell physiology and promote bacterial survival in host tissues. This protein is an E3 ubiquitin-protein ligase that probably interferes with the host's ubiquitination pathway and targets host proteins for proteasomal degradation. Can ubiquitinate ubiquitin, giving rise to polyubiquitin chains (in vitro) (PubMed:36511702). Does not complement an nleG8 deletion in C.rodentium (PubMed:36511702)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.2.27\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"name\":\"S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"id\":\"GO:0061630\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:ubiquitin protein ligase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Popov G.\",\"Fiebig-Comyn A.\",\"Syriste L.\",\"Little D.J.\",\"Skarina T.\",\"Stogios P.J.\",\"Birstonas S.\",\"Coombes B.K.\",\"Savchenko A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36511702\"},{\"database\":\"DOI\",\"id\":\"10.1128/iai.00505-22\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0050522\",\"id\":\"36511702\",\"journal\":\"Infect. Immun.\",\"lastPage\":\"e0050522\",\"publicationDate\":\"2023\",\"title\":\"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for Different Roles during Citrobacter rodentium Infection in Mice.\",\"volume\":\"91\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6XNJ\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.85 ANGSTROMS) OF 206-215 IN COMPLEX WITH HUMAN GOPC\",\"FUNCTION\",\"SUBUNIT\",\"INTERACTION WITH HOST GOPC\",\"SUBCELLULAR LOCATION\",\"DOMAIN\",\"MOTIF\",\"MUTAGENESIS OF ILE-138 AND 212-CYS--ILE-215\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   NLEG8_ECO57             Reviewed;         215 AA.\nAC   Q8XAN6; A0A0H3JIV3; A0A6M0JK84; Q7AEM3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2002, sequence version 1.\nDT   28-JAN-2026, entry version 129.\nDE   RecName: Full=E3 ubiquitin-protein ligase NleG {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};\nGN   Name=nleG8 {ECO:0000303|PubMed:36511702};\nGN   Synonyms=nleG {ECO:0000312|EMBL:BAB35247.1};\nGN   ORFNames=ECs_1824 {ECO:0000312|EMBL:BAB35247.1};\nOS   Escherichia coli O157:H7.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=83334;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 129,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "source_locator": "lines 26-35",
  "excerpt": "RN   [2] {ECO:0007744|PDB:6XNJ}\nRP   X-RAY CRYSTALLOGRAPHY (1.85 ANGSTROMS) OF 206-215 IN COMPLEX WITH HUMAN\nRP   GOPC, FUNCTION, SUBUNIT, INTERACTION WITH HOST GOPC, SUBCELLULAR LOCATION,\nRP   DOMAIN, MOTIF, AND MUTAGENESIS OF ILE-138 AND 212-CYS--ILE-215.\nRX   PubMed=36511702; DOI=10.1128/iai.00505-22;\nRA   Popov G., Fiebig-Comyn A., Syriste L., Little D.J., Skarina T.,\nRA   Stogios P.J., Birstonas S., Coombes B.K., Savchenko A.;\nRT   \"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for\nRT   Different Roles during Citrobacter rodentium Infection in Mice.\";\nRL   Infect. Immun. 91:e0050522-e0050522(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 129,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "source_locator": "lines 42-49",
  "excerpt": "CC   -!- FUNCTION: Effector proteins function to alter host cell physiology and\nCC       promote bacterial survival in host tissues. This protein is an E3\nCC       ubiquitin-protein ligase that probably interferes with the host's\nCC       ubiquitination pathway and targets host proteins for proteasomal\nCC       degradation. Can ubiquitinate ubiquitin, giving rise to polyubiquitin\nCC       chains (in vitro) (PubMed:36511702). Does not complement an nleG8\nCC       deletion in C.rodentium (PubMed:36511702).\nCC       {ECO:0000269|PubMed:36511702}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 129,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "source_locator": "lines 50-54",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine +\nCC         [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-\nCC         cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.;\nCC         EC=2.3.2.27; Evidence={ECO:0000269|PubMed:36511702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 129,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "source_locator": "lines 86-86",
  "excerpt": "DR   GO; GO:0061630; F:ubiquitin protein ligase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 129,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 27781-27793",
  "excerpt": "[Term]\nid: GO:0003676\nname: nucleic acid binding\nnamespace: molecular_function\nalt_id: GO:0000496\ndef: \"Binding to a nucleic acid.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsynonym: \"base pairing\" NARROW []\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0003676"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 34028-34054",
  "excerpt": "[Term]\nid: GO:0004044\nname: amidophosphoribosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O.\" [EC:2.4.2.14, RHEA:14905]\nsynonym: \"5'-phosphoribosylpyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"5-phosphoribosyl-1-pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"5-phosphoribosylamine:diphosphate phospho-alpha-D-ribosyltransferase (glutamate-amidating)\" RELATED [EC:2.4.2.14]\nsynonym: \"5-phosphororibosyl-1-pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"alpha-5-phosphoribosyl-1-pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine 5-phosphoribosylpyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine phosphoribosyldiphosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine phosphoribosylpyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine ribosylpyrophosphate 5-phosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribose pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribosyl pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribosyldiphosphate 5-amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribosylpyrophosphate glutamyl amidotransferase activity\" RELATED [EC:2.4.2.14]\nxref: EC:2.4.2.14\nxref: KEGG_REACTION:R01072\nxref: MetaCyc:PRPPAMIDOTRANS-RXN\nxref: Reactome:R-HSA-73815 \"5-phospho-alpha-D-ribose 1-diphosphate (PRPP) + H2O + L-glutamine <=> 5-phosphoribosylamine + L-glutamate +pyrophosphate\"\nxref: RHEA:14905\nis_a: GO:0016763 ! pentosyltransferase activity\nproperty_value: skos:exactMatch EC:2.4.2.14\nproperty_value: skos:exactMatch RHEA:14905\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004044"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 45927-45946",
  "excerpt": "[Term]\nid: GO:0004633\nname: phosphopantothenoylcysteine decarboxylase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: N-[(R)-4-phosphonatopantothenoyl]-L-cysteinate + H+ = CO2 + pantetheine 4'-phosphate.\" [EC:4.1.1.36, RHEA:16793]\nsynonym: \"4-phosphopantothenoyl-L-cysteine decarboxylase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"4-phosphopantotheoylcysteine decarboxylase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"N-((R)-4'-phosphopantothenoyl)-L-cysteine carboxy-lyase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"N-[(R)-4'-phosphopantothenoyl]-L-cysteine carboxy-lyase (pantotheine-4'-phosphate-forming)\" RELATED [EC:4.1.1.36]\nsynonym: \"N-[(R)-4'-phosphopantothenoyl]-L-cysteine carboxy-lyase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"PPC-decarboxylase activity\" RELATED [EC:4.1.1.36]\nxref: EC:4.1.1.36\nxref: KEGG_REACTION:R03269\nxref: MetaCyc:P-PANTOCYSDECARB-RXN\nxref: Reactome:R-HSA-196840 \"3xPPCDC:3FMN decarboxylates PPC\"\nxref: RHEA:16793\nis_a: GO:0016831 ! carboxy-lyase activity\nproperty_value: skos:exactMatch EC:4.1.1.36\nproperty_value: skos:exactMatch RHEA:16793\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004633"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 51005-51151",
  "excerpt": "[Term]\nid: GO:0004842\nname: ubiquitin-protein transferase activity\nnamespace: molecular_function\nalt_id: GO:0004840\nalt_id: GO:0004841\ndef: \"Catalysis of the transfer of ubiquitin from one protein to another via the reaction X-Ub + Y = Y-Ub + X, where both X-Ub and Y-Ub are covalent linkages.\" [GOC:BioGRID, GOC:jh2, PMID:9635407]\nsynonym: \"E2\" BROAD []\nsynonym: \"E3\" BROAD []\nsynonym: \"ubiquitin conjugating enzyme activity\" NARROW []\nsynonym: \"ubiquitin ligase activity\" NARROW []\nsynonym: \"ubiquitin protein ligase activity\" NARROW []\nsynonym: \"ubiquitin protein-ligase activity\" NARROW []\nsynonym: \"ubiquitin-conjugating enzyme activity\" NARROW []\nxref: KEGG_REACTION:R03876\nxref: Reactome:R-HSA-1234163 \"Cytosolic VBC complex ubiquitinylates hydroxyprolyl-HIF-alpha\"\nxref: Reactome:R-HSA-1234172 \"Nuclear VBC complex ubiquitinylates HIF-alpha\"\nxref: Reactome:R-HSA-1253282 \"ERBB4 ubiquitination by WWP1/ITCH\"\nxref: Reactome:R-HSA-1358789 \"Self-ubiquitination of RNF41\"\nxref: Reactome:R-HSA-1358790 \"RNF41 ubiquitinates ERBB3\"\nxref: Reactome:R-HSA-1358792 \"RNF41 ubiquitinates activated ERBB3\"\nxref: Reactome:R-HSA-1363331 \"Ubiquitination of p130 (RBL2) by SCF (Skp2)\"\nxref: Reactome:R-HSA-168915 \"K63-linked ubiquitination of RIP1 bound to the activated TLR complex\"\nxref: Reactome:R-HSA-173542 \"SMURF2 ubiquitinates SMAD2\"\nxref: Reactome:R-HSA-173545 \"Ubiquitin-dependent degradation of the SMAD complex terminates TGF-beta signaling\"\nxref: Reactome:R-HSA-174057 \"Multiubiquitination of APC/C-associated Cdh1\"\nxref: Reactome:R-HSA-174104 \"Ubiquitination of Cyclin A by APC/C:Cdc20 complex\"\nxref: Reactome:R-HSA-174144 \"Ubiquitination of Securin by phospho-APC/C:Cdc20 complex\"\nxref: Reactome:R-HSA-174159 \"Ubiquitination of Emi1 by SCF-beta-TrCP\"\nxref: Reactome:R-HSA-174195 \"Ubiquitination of cell cycle proteins targeted by the APC/C:Cdh1complex\"\nxref: Reactome:R-HSA-174227 \"Ubiquitination of Cyclin B by phospho-APC/C:Cdc20 complex\"\nxref: Reactome:R-HSA-179417 \"Multiubiquitination of Nek2A\"\nxref: Reactome:R-HSA-180540 \"Multi-ubiquitination of APOBEC3G\"\nxref: Reactome:R-HSA-180597 \"Ubiquitination of CD4 by Vpu:CD4:beta-TrCP:SKP1 complex\"\nxref: Reactome:R-HSA-182986 \"CBL-mediated ubiquitination of CIN85\"\nxref: Reactome:R-HSA-182993 \"Ubiquitination of stimulated EGFR (CBL)\"\nxref: Reactome:R-HSA-183051 \"CBL ubiquitinates Sprouty\"\nxref: Reactome:R-HSA-183084 \"CBL escapes CDC42-mediated inhibition by down-regulating the adaptor molecule Beta-Pix\"\nxref: Reactome:R-HSA-183089 \"CBL binds and ubiquitinates phosphorylated Sprouty\"\nxref: Reactome:R-HSA-1852623 \"Ubiquitination of NICD1 by FBWX7\"\nxref: Reactome:R-HSA-187575 \"Ubiquitination of phospho-p27/p21\"\nxref: Reactome:R-HSA-1912357 \"ITCH ubiquitinates DTX\"\nxref: Reactome:R-HSA-1912386 \"Ubiquitination of NOTCH1 by ITCH in the absence of ligand\"\nxref: Reactome:R-HSA-1918092 \"CHIP (STUB1) mediates ubiquitination of ERBB2\"\nxref: Reactome:R-HSA-1918095 \"CUL5 mediates ubiquitination of ERBB2\"\nxref: Reactome:R-HSA-1977296 \"NEDD4 ubiquitinates ERBB4jmAcyt1s80 dimer\"\nxref: Reactome:R-HSA-1980074 \"Ubiquitination of DLL/JAG ligands upon binding to NOTCH1\"\nxref: Reactome:R-HSA-1980118 \"ARRB mediates NOTCH1 ubiquitination\"\nxref: Reactome:R-HSA-201425 \"Ubiquitin-dependent degradation of the Smad complex terminates BMP2 signalling\"\nxref: Reactome:R-HSA-202453 \"Auto-ubiquitination of TRAF6\"\nxref: Reactome:R-HSA-202534 \"Ubiquitination of NEMO by TRAF6\"\nxref: Reactome:R-HSA-205118 \"TRAF6 polyubiquitinates NRIF\"\nxref: Reactome:R-HSA-209063 \"Beta-TrCP ubiquitinates NFKB p50:p65:phospho IKBA complex\"\nxref: Reactome:R-HSA-211734 \"Ubiquitination of PAK-2p34\"\nxref: Reactome:R-HSA-2169050 \"SMURFs/NEDD4L ubiquitinate phosphorylated TGFBR1 and SMAD7\"\nxref: Reactome:R-HSA-2172172 \"Ubiquitination of DLL/JAG ligands upon binding to NOTCH2\"\nxref: Reactome:R-HSA-2179276 \"SMURF2 monoubiquitinates SMAD3\"\nxref: Reactome:R-HSA-2186747 \"Ubiquitination of SKI/SKIL by RNF111/SMURF2\"\nxref: Reactome:R-HSA-2186785 \"RNF111 ubiquitinates SMAD7\"\nxref: Reactome:R-HSA-2187368 \"STUB1 (CHIP) ubiquitinates SMAD3\"\nxref: Reactome:R-HSA-2213017 \"Auto-ubiquitination of TRAF3\"\nxref: Reactome:R-HSA-264444 \"Autoubiquitination of phospho-COP1(Ser-387 )\"\nxref: Reactome:R-HSA-2682349 \"RAF1:SGK:TSC22D3:WPP ubiquitinates SCNN channels\"\nxref: Reactome:R-HSA-2730904 \"Auto-ubiquitination of TRAF6\"\nxref: Reactome:R-HSA-2737728 \"Ubiquitination of DLL/JAG ligands upon binding to NOTCH1 HD domain mutants\"\nxref: Reactome:R-HSA-2769007 \"Ubiquitination of DLL/JAG ligands upon binding to NOTCH1 PEST domain mutants\"\nxref: Reactome:R-HSA-2900765 \"Ubiquitination of DLL/JAG ligands upon binding to NOTCH1 HD+PEST domain mutants\"\nxref: Reactome:R-HSA-3000335 \"SCF-beta-TrCp1/2 ubiquitinates phosphorylated BORA\"\nxref: Reactome:R-HSA-3134804 \"STING ubiquitination by TRIM32 or TRIM56\"\nxref: Reactome:R-HSA-3134946 \"DDX41 ubiquitination by TRIM21\"\nxref: Reactome:R-HSA-3249386 \"DTX4 ubiquitinates p-S172-TBK1 within NLRP4:DTX4:dsDNA:ZBP1:TBK1\"\nxref: Reactome:R-HSA-3780995 \"NHLRC1 mediated ubiquitination of EPM2A (laforin) and PPP1RC3 (PTG) associated with glycogen-GYG2\"\nxref: Reactome:R-HSA-3781009 \"NHLRC1 mediated ubiquitination of EPM2A and PPP1RC3 associated with glycogen-GYG1\"\nxref: Reactome:R-HSA-3788724 \"Cdh1:APC/C ubiquitinates EHMT1 and EHMT2\"\nxref: Reactome:R-HSA-3797226 \"Defective NHLRC1 does not ubiquitinate EPM2A (laforin) and PPP1R3C (PTG) (type 2B disease)\"\nxref: Reactome:R-HSA-4332236 \"CBL neddylates TGFBR2\"\nxref: Reactome:R-HSA-446877 \"TRAF6 is K63 poly-ubiquitinated\"\nxref: Reactome:R-HSA-450358 \"Activated TRAF6 synthesizes unanchored polyubiquitin chains upon TLR stimulation\"\nxref: Reactome:R-HSA-451418 \"Pellino ubiquitinates IRAK1\"\nxref: Reactome:R-HSA-5357757 \"BIRC(cIAP1/2) ubiquitinates RIPK1\"\nxref: Reactome:R-HSA-5362412 \"SYVN1 ubiquitinates Hh C-terminal fragments\"\nxref: Reactome:R-HSA-5483238 \"Hh processing variants are ubiquitinated\"\nxref: Reactome:R-HSA-5607725 \"SCF-beta-TRCP ubiquitinates p-7S-p100:RELB in active NIK:p-176,S180-IKKA dimer:p-7S-p100:SCF-beta-TRCP\"\nxref: Reactome:R-HSA-5607728 \"beta-TRCP ubiquitinates IkB-alpha in p-S32,33-IkB-alpha:NF-kB complex\"\nxref: Reactome:R-HSA-5607756 \"TRAF6 oligomer autoubiquitinates\"\nxref: Reactome:R-HSA-5607757 \"K63polyUb-TRAF6 ubiquitinates TAK1\"\nxref: Reactome:R-HSA-5610742 \"SCF(beta-TrCP) ubiquitinates p-GLI1\"\nxref: Reactome:R-HSA-5610745 \"SCF(beta-TrCP) ubiquitinates p-GLI2\"\nxref: Reactome:R-HSA-5610746 \"SCF(beta-TrCP) ubiquitinates p-GLI3\"\nxref: Reactome:R-HSA-5652009 \"RAD18:UBE2B or RBX1:CUL4:DDB1:DTL monoubiquitinates PCNA\"\nxref: Reactome:R-HSA-5655170 \"RCHY1 monoubiquitinates POLH\"\nxref: Reactome:R-HSA-5660753 \"SIAH1:UBE2L6:Ubiquitin ubiquitinates SNCA\"\nxref: Reactome:R-HSA-5667107 \"SIAH1, SIAH2 ubiquitinate SNCAIP\"\nxref: Reactome:R-HSA-5667111 \"PARK2 K63-Ubiquitinates SNCAIP\"\nxref: Reactome:R-HSA-5668454 \"K63polyUb-cIAP1,2 ubiquitinates TRAF3\"\nxref: Reactome:R-HSA-5668534 \"cIAP1,2 ubiquitinates NIK in cIAP1,2:TRAF2::TRAF3:NIK\"\nxref: Reactome:R-HSA-5675470 \"BIRC2/3 (cIAP1/2) is autoubiquitinated\"\nxref: Reactome:R-HSA-5684250 \"SCF betaTrCP ubiquitinates NFKB p105 within p-S927, S932-NFkB p105:TPL2:ABIN2\"\nxref: Reactome:R-HSA-5691108 \"SKP1:FBXL5:CUL1:NEDD8 ubiquitinylates IREB2\"\nxref: Reactome:R-HSA-5693108 \"TNFAIP3 (A20) ubiquitinates RIPK1 with K48-linked Ub chains\"\nxref: Reactome:R-HSA-68712 \"The geminin component of geminin:Cdt1 complexes is ubiquitinated, releasing Cdt1\"\nxref: Reactome:R-HSA-69598 \"Ubiquitination of phosphorylated CDC25A\"\nxref: Reactome:R-HSA-741386 \"RIP2 induces K63-linked ubiquitination of NEMO\"\nxref: Reactome:R-HSA-75824 \"Ubiquitination of Cyclin D1\"\nxref: Reactome:R-HSA-870449 \"TRIM33 monoubiquitinates SMAD4\"\nxref: Reactome:R-HSA-8948709 \"DTX4 ubiquitinates p-S172-TBK1 within NLRP4:DTX4:STING:TBK1:IRF3\"\nxref: Reactome:R-HSA-8956106 \"VHL:EloB,C:NEDD8-CUL2:RBX1 complex ubiquitinylates HIF-alpha\"\nxref: Reactome:R-HSA-9013069 \"Ubiquitination of DLL/JAG ligands upon binding to NOTCH3\"\nxref: Reactome:R-HSA-9013974 \"Auto-ubiquitination of TRAF3 within activated TLR3 complex\"\nxref: Reactome:R-HSA-9014342 \"K63-linked ubiquitination of RIP1 bound to the activated TLR complex\"\nxref: Reactome:R-HSA-918224 \"DDX58 is K63 polyubiquitinated\"\nxref: Reactome:R-HSA-936412 \"RNF125 mediated ubiquitination of DDX58, IFIH1 and MAVS\"\nxref: Reactome:R-HSA-936942 \"Auto ubiquitination of oligo-TRAF6 bound to p-IRAK2\"\nxref: Reactome:R-HSA-936986 \"Activated TRAF6 synthesizes unanchored polyubiquitin chains\"\nxref: Reactome:R-HSA-9628444 \"Activated TRAF6 synthesizes unanchored polyubiquitin chains upon TLR3 stimulation\"\nxref: Reactome:R-HSA-9645394 \"Activated TRAF6 synthesizes unanchored polyubiquitin chains upon ALPK1:ADP-heptose stimulation\"\nxref: Reactome:R-HSA-9645414 \"Auto ubiquitination of TRAF6 bound to ALPK1:ADP-heptose:TIFA oligomer\"\nxref: Reactome:R-HSA-9688831 \"STUB1 ubiquitinates RIPK3 at K55, K363\"\nxref: Reactome:R-HSA-9701000 \"BRCA1:BARD1 heterodimer autoubiquitinates\"\nxref: Reactome:R-HSA-9750946 \"TRAF2,6 ubiquitinates NLRC5\"\nxref: Reactome:R-HSA-975118 \"TRAF6 ubiquitinqtes IRF7 within the activated TLR7/8 or 9 complex\"\nxref: Reactome:R-HSA-975147 \"Auto ubiquitination of oligo-TRAF6 bound to p-IRAK2 at endosome membrane\"\nxref: Reactome:R-HSA-9758604 \"Ubiquitination of IKBKG by TRAF6\"\nxref: Reactome:R-HSA-9766227 \"MDM2 mediates CDH1 ubiquitination\"\nxref: Reactome:R-HSA-9793444 \"ITCH polyubiquitinates MLKL at K50\"\nxref: Reactome:R-HSA-9793485 \"PRKN polyubiquitinates RIPK3\"\nxref: Reactome:R-HSA-9793679 \"LUBAC ubiquitinates RIPK1 at K627\"\nxref: Reactome:R-HSA-9796346 \"MIB2 ubiquitinates RIPK1 at K377, K604, K634\"\nxref: Reactome:R-HSA-9796387 \"STUB1 ubiquitinates RIPK1 at K571, K604, K627\"\nxref: Reactome:R-HSA-9796626 \"MIB2 ubiquitinates CFLAR\"\nxref: Reactome:R-HSA-9815507 \"MIB2 ubiquitinates CYLD at K338, K530\"\nxref: Reactome:R-HSA-9817362 \"SPATA2:CYLD-bound LUBAC ubiquitinates RIPK1 at K627 within the TNFR1 signaling complex\"\nxref: Reactome:R-HSA-983140 \"Transfer of Ub from E2 to substrate and release of E2\"\nxref: Reactome:R-HSA-983153 \"E1 mediated ubiquitin activation\"\nxref: Reactome:R-HSA-983156 \"Polyubiquitination of substrate\"\nxref: Reactome:R-HSA-9833155 \"Ubiquitination of STAT2\"\nxref: Reactome:R-HSA-9834070 \"PRKN ubiquitinates MOM substrates\"\nxref: Reactome:R-HSA-9861563 \"CTLH E3 ligase ubiquitinates LDHA\"\nxref: Reactome:R-HSA-9861640 \"CTLH E3 ligase ubiquitinates PKM-1\"\nxref: Reactome:R-HSA-9929350 \"Ubiquitination of CD274 by BTRC-SCF E3-ligase complex\"\nxref: Reactome:R-HSA-9934753 \"CBLL1 ubiquitinates CDH1\"\nxref: Reactome:R-HSA-9948301 \"ZNF598 K63 polyubiquitinates RPS10 (eS10) and RPS20 (uS10) of the 40S ribosomal subunit\"\nxref: Reactome:R-HSA-9954721 \"NEDD8-K699-CUL2:ELOB:ELOC:RBX1:KLHDC10 K48 polyubiquitinates alanine-tailed nascent peptide\"\nxref: Reactome:R-HSA-9955146 \"S.flexneri ipaH9.8 ubiquitinates GBPs\"\nxref: Reactome:R-HSA-9970191 \"RBBP6 activates CPSF complex\"\nis_a: GO:0019787 ! ubiquitin-like protein transferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004842"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 358126-358254",
  "excerpt": "[Term]\nid: GO:0061630\nname: ubiquitin protein ligase activity\nnamespace: molecular_function\nalt_id: GO:0090302\nalt_id: GO:0090622\nalt_id: GO:1904264\nalt_id: GO:1904822\ndef: \"Catalysis of the transfer of ubiquitin to a substrate protein via the reaction X-ubiquitin + S = X + S-ubiquitin, where X is either an E2 or E3 enzyme, the X-ubiquitin linkage is a thioester bond, and the S-ubiquitin linkage is an amide bond: an isopeptide bond between the C-terminal glycine of ubiquitin and the epsilon-amino group of lysine residues in the substrate or, in the linear extension of ubiquitin chains, a peptide bond the between the C-terminal glycine and N-terminal methionine of ubiquitin residues.\" [GOC:BioGRID, GOC:dph, GOC:mah, GOC:tb, PMID:22863777]\ncomment: This enzyme catalyzes a transferase reaction.\nsynonym: \"E3\" BROAD [GOC:dph]\nsynonym: \"ER-associated E3 ligase\" RELATED [PMID:24019521]\nsynonym: \"protein ubiquitination activity\" EXACT [GOC:dph]\nsynonym: \"ubiquitin ligase activity\" EXACT [GOC:dph]\nxref: EC:2.3.2.26\nxref: EC:2.3.2.27\nxref: EC:2.3.2.31\nxref: EC:2.3.2.33\nxref: EC:2.3.2.36\nxref: Reactome:R-HSA-1225956 \"Inefficient ubiquitination of ligand-responsive p-6Y-EGFR mutants by p-Y371-CBL\"\nxref: Reactome:R-HSA-1504190 \"DVL is ubiquitinated by CUL3:KLHL12:RBX1\"\nxref: Reactome:R-HSA-183036 \"Ubiquitination of stimulated EGFR (CBL:GRB2)\"\nxref: Reactome:R-HSA-201445 \"Ubiquitin-dependent degradation controls basal levels of R-Smad1/5/8\"\nxref: Reactome:R-HSA-3322429 \"XIAP monoubiquinates TLE\"\nxref: Reactome:R-HSA-3640861 \"RNF146 ubiquitinates ADP-ribosylated AXIN\"\nxref: Reactome:R-HSA-4608852 \"SMURF1/2 ubiquitinates PRICKLE1\"\nxref: Reactome:R-HSA-4641129 \"AXIN is ubiquitinated by SMURF2\"\nxref: Reactome:R-HSA-4641159 \"DVL1 is ubiquitinated by HECW1\"\nxref: Reactome:R-HSA-4641246 \"ZNRF3 autoubiquitinates to promote its internalization\"\nxref: Reactome:R-HSA-4641253 \"ZNRF3 ubiquitinates FZD to promote its downregulation\"\nxref: Reactome:R-HSA-5246693 \"APC is K63-polyubiquitinated\"\nxref: Reactome:R-HSA-5610737 \"NUMB:ITCH bind and ubiquitnate GLI1\"\nxref: Reactome:R-HSA-5632648 \"SMURF1/2 ubiquitinates PTCH1\"\nxref: Reactome:R-HSA-5635856 \"SPOP:CUL3:RBX1 ubiquitinates GLI2,3\"\nxref: Reactome:R-HSA-5635864 \"NUMB:ITCH ubiquitinates GLI1\"\nxref: Reactome:R-HSA-5654672 \"CBL ubiquitinates FRS2 and FGFR1\"\nxref: Reactome:R-HSA-5654677 \"CBL ubiquitinates FRS2 and FGFR2\"\nxref: Reactome:R-HSA-5654679 \"CBL ubiquitinates FRS2 and FGFR3\"\nxref: Reactome:R-HSA-5654684 \"CBL ubiquitinates FRS2 and FGFR4\"\nxref: Reactome:R-HSA-5658424 \"KBTBD7:CUL3:RBX1 ubiquitinates NF1\"\nxref: Reactome:R-HSA-5674022 \"BRAP autoubiquitinates\"\nxref: Reactome:R-HSA-5682858 \"RNF8 and RNF168 ubiquitinate H2AFX\"\nxref: Reactome:R-HSA-5684071 \"RNF4 ubiquitinates MDC1\"\nxref: Reactome:R-HSA-5687081 \"MAPK6 is ubiquitinated at the N-terminal\"\nxref: Reactome:R-HSA-5689111 \"PARK2 autoubiquitinates\"\nxref: Reactome:R-HSA-5690827 \"TNFAIP3 (A20) ubiquitinates RIPK1\"\nxref: Reactome:R-HSA-6781867 \"ERCC8:DDB1:CUL4:RBX1 ubiquitinates ERCC6 and RNA Pol II\"\nxref: Reactome:R-HSA-6782943 \"UV-DDB ubiquitinates XPC\"\nxref: Reactome:R-HSA-6785361 \"Monoubiquitination of FANCD2:FANCI\"\nxref: Reactome:R-HSA-6790487 \"RNF111 ubiquitinates SUMOylated XPC\"\nxref: Reactome:R-HSA-6798373 \"MDM2 ubiquitinates DYRK2\"\nxref: Reactome:R-HSA-6804253 \"MDM2 ubiquitinates JMY\"\nxref: Reactome:R-HSA-6804441 \"RNF34 or RFFL ubiquitinates phosphorylated TP53\"\nxref: Reactome:R-HSA-6804724 \"MDM2 ubiquitinates phosphorylated MDM4\"\nxref: Reactome:R-HSA-6804879 \"MDM2 ubiquitinates TP53\"\nxref: Reactome:R-HSA-6804942 \"MDM2 homodimers auto-ubiquitinate\"\nxref: Reactome:R-HSA-6807106 \"PTEN undergoes monoubiquitination\"\nxref: Reactome:R-HSA-6807134 \"NEDD4, WWP2, CHIP and XIAP polyubiquitinate PTEN\"\nxref: Reactome:R-HSA-68946 \"Phosphorylated Orc1 is ubiquitinated while still associated with chromatin\"\nxref: Reactome:R-HSA-69015 \"Cytoplasmic phosphorylated Cdc6 is ubiquitinated by the anaphase-promoting complex\"\nxref: Reactome:R-HSA-8848829 \"CBL autoubiquitinates\"\nxref: Reactome:R-HSA-8851011 \"TRIM27 polyubiquitinates PTEN\"\nxref: Reactome:R-HSA-8854041 \"SCF-FBXL7 ubiquitinates AURKA\"\nxref: Reactome:R-HSA-8854051 \"SCF-FBXL18 ubiquitinates FBXL7\"\nxref: Reactome:R-HSA-8854628 \"MYLIP dimer ubiquitinates VLDLR on Lys-839\"\nxref: Reactome:R-HSA-8866546 \"RNF5 and RNF185 ubiquitinate misfolded CFTR\"\nxref: Reactome:R-HSA-8866856 \"RNF5 and RNF185 ubiquitinate CFTR F508del\"\nxref: Reactome:R-HSA-8867288 \"OS9:SEL1:ERAD E3 ligase:DERL2 ubiquitinates unfolded protein:(GlcNAc)2 (Man)9-5\"\nxref: Reactome:R-HSA-8875183 \"CBL monoubiquitinates activated MET\"\nxref: Reactome:R-HSA-8875431 \"LRIG1 undergoes ubiquitination\"\nxref: Reactome:R-HSA-8876258 \"CBL monoubiquitinates InlB-bound MET\"\nxref: Reactome:R-HSA-8877003 \"CBLL1 ubiqutinates the InlA-bound CDH1 complex\"\nxref: Reactome:R-HSA-8938773 \"RNF144A polyubiquitinates PRKDC\"\nxref: Reactome:R-HSA-8938815 \"RNF152 polyubiquitinates RRAGA\"\nxref: Reactome:R-HSA-8939335 \"RNF181 polyubiquinates BCL10\"\nxref: Reactome:R-HSA-8939706 \"SCF(SKP2) polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-8942101 \"RNF20:RNF40 monoubiquitinates Histone H2B\"\nxref: Reactome:R-HSA-8943003 \"SHPRH polyubiquitinates monoubiquitinated PCNA\"\nxref: Reactome:R-HSA-8943040 \"HLTF polyubiquitinates monoubiquitinated PCNA\"\nxref: Reactome:R-HSA-8943080 \"TMEM129 polyubiquitinates HLA (MHC class I heavy chain) bound to cytomegalovirus US11\"\nxref: Reactome:R-HSA-8948775 \"MKRN1 polyubiquitinates PTEN\"\nxref: Reactome:R-HSA-8948832 \"RNF146 polyubiquitinates PARylated PTEN\"\nxref: Reactome:R-HSA-8952382 \"MDM2 polyubiquitinates RUNX3\"\nxref: Reactome:R-HSA-8952419 \"SMURFs ubiquitinate RUNX3\"\nxref: Reactome:R-HSA-8953946 \"PEX2:PEX10:PEX12 monoubiquitinates PEX5S,L at cysteine-11\"\nxref: Reactome:R-HSA-8956026 \"CUL9:RBX1 ubiquitinates BIRC5\"\nxref: Reactome:R-HSA-8956684 \"ITCH polyubiquitinates TP73\"\nxref: Reactome:R-HSA-9008076 \"WWP1 polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-9009308 \"STUB1 polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-9009403 \"SMURF1 polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-9011300 \"ZSWIM8 ubiquitinates ROBO3.1\"\nxref: Reactome:R-HSA-9021523 \"WWP2 ubiquitinates NOTCH3\"\nxref: Reactome:R-HSA-9033485 \"PEX2:PEX10:PEX12 monoubiquitinates PEX5L at cysteine-11\"\nxref: Reactome:R-HSA-934604 \"Phosphorylated SPRY2 is ubiquitinated by CBL\"\nxref: Reactome:R-HSA-936462 \"PIN1 mediated IRF3 degradation\"\nxref: Reactome:R-HSA-936475 \"Negative regulation of DDX58/IFIH1 signaling by RNF216\"\nxref: Reactome:R-HSA-9604629 \"FBXW7 promotes ubiquitination of p-NICD4\"\nxref: Reactome:R-HSA-9685195 \"SARS-CoV-1 9b recruits ITCH to MAVS\"\nxref: Reactome:R-HSA-9686920 \"PELI1 ubiquitinates RIPK3 at K363\"\nxref: Reactome:R-HSA-9686969 \"APC/C:Cdh1 polyubiquitinates SKP2\"\nxref: Reactome:R-HSA-9705738 \"SOCS1,3 ubiquitinates CSF3R in SOCS1,3:p-4Y-CSF3R:CSF3 dimer:LYN:p-Y-JAK1:p-JAK2:p-SYK:p-HCK:p-TYK2:CUL5:ELOB:ELOC:RNF7\"\nxref: Reactome:R-HSA-9706354 \"Ubiquitination of FLT3\"\nxref: Reactome:R-HSA-9706356 \"CBL mutants don't ubiquitinate FLT3\"\nxref: Reactome:R-HSA-9708517 \"FBXL17 ubiquitinates BACH1 (in BACH1:FBXL17:SCF (SKP2))\"\nxref: Reactome:R-HSA-9733316 \"p-Y-CBL autoubiquitinates and multiubiquitinates p-Y561-CSF1R in CSF1 dimer:p-Y561-CSF1R dimer:p-Y-CBL\"\nxref: Reactome:R-HSA-9755304 \"MUL1 ubiquitinates UBXN7\"\nxref: Reactome:R-HSA-9755505 \"KEAP1:NEDD8-CUL3:RBX1 complex ubiquitinates NFE2L2\"\nxref: Reactome:R-HSA-9759154 \"TRIM21 ubiquitinates SQSTM1\"\nxref: Reactome:R-HSA-9759172 \"KEAP1:CUL3:RBX1 ubiquitinates p-S349 SQSTM1 oligomer\"\nxref: Reactome:R-HSA-9762091 \"NFE2L2 is ubiquitinated by BTRC:SKP1:CUL1:RBX1\"\nxref: Reactome:R-HSA-9766645 \"CUL3:RBX1 ubiquitinates KEAP1\"\nxref: Reactome:R-HSA-990526 \"Recruitment of ITCH and K48 ubiquitination of MAVS\"\nxref: Reactome:R-HSA-9929490 \"CD274 ubiquitination by SPOP:CUL3:RBX1 complex\"\nxref: Reactome:R-HSA-9931298 \"Ubiquitination of CD274 by ERAD complex\"\nxref: Reactome:R-HSA-9931430 \"MIB2-mediated K63-ubiquitination of CD274\"\nxref: Reactome:R-HSA-9932510 \"BTRC:CUL1:SKP1:RBX1 (SCF-beta-TrCP1) ubiquitinylates phosphorylated PER1,2,3\"\nxref: Reactome:R-HSA-9932512 \"FBXL3:CUL1:SKP1:RBX1 ubiquitinylates phosphorylated CRY1,2\"\nxref: Reactome:R-HSA-9945766 \"NS3 is ubiquitinated\"\nxref: Reactome:R-HSA-9946390 \"NS1 dimer is ubiquitinated\"\nxref: Reactome:R-HSA-9948362 \"LTN1 K48 polyubiquitinates the nascent peptide in NEMF:60S ribosomal subunit:peptidyl-tRNA with nascent peptide\"\nxref: Reactome:R-HSA-9954737 \"RCHY1 K48 polyubiquitinates alanine-tailed nascent peptide\"\nis_a: GO:0004842 ! ubiquitin-protein transferase activity\nis_a: GO:0061659 ! ubiquitin-like protein ligase activity\nproperty_value: skos:narrowMatch EC:2.3.2.26\nproperty_value: skos:narrowMatch EC:2.3.2.27\nproperty_value: skos:narrowMatch EC:2.3.2.31\nproperty_value: skos:narrowMatch EC:2.3.2.33\nproperty_value: skos:narrowMatch EC:2.3.2.36\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0061630"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
