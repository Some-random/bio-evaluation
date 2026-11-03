# GO_molecular_function_0002: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0002.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **B** — endopeptidase activity

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | uncertain | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MKNNKISGFQWAMTIFVFFVITMALSIMLRDFQSIIGVKHFIFEVTDLAPLIAAIICILVFKYKKVQLAGLKFSISLKVIERLLLALILPLIILIIGMYSFNTFADSFILLQSTGLSVPITHILIGHILMAFVVEFGFRSYLQNIVETKMNTFFASIVVGLMYSVFSANTTYGTEFAAYNFLYTFSFSMILGELIRATKGRTIYIATTFHASMTFGLIFLFSEEIGDLFSIKVIAISTAIVAVGYIGLSLIIRGIAYLTTRRNLEELEPNNYLDHVNDDEETNHTEAEKSSSNIKDAEKTGVATASTVGVAKNDTENTVADEPSIHEGTEKTEPQHHIGNQTESNHDEDHDITSESVESAESVKQAPQSDDLTNDSNEDEIEQSLKEPVTYKEDRRSSVVIDAEKHIEKTEEQSSDKNK

[Multiple Choices]
A. dUMP kinase activity
B. endopeptidase activity
C. DNA binding
D. endonuclease activity
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

> The exact sequence has a UniProt GO annotation for endopeptidase activity, but its evidence is computational (IEA:UniProtKB-ARBA), not direct experimental confirmation. The accompanying functional description instead characterizes LyrA as probably non-catalytic in SagB-mediated peptidoglycan processing, so the annotation should not be treated as experimentally established.

Citations as saved: [C1](#evidence-c1), [C6](#evidence-c6), [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and suggests a multipass membrane protein, which weighs against soluble kinase, DNA-binding, and endonuclease functions. But it does not provide a clear basis for assigning endopeptidase activity; the sequence-level clues do not establish that this membrane protein catalyzes peptide-bond hydrolysis.


**Missing item-specific fact**

> Distinguishing B requires the protein-specific GO annotation or other external functional evidence; the supplied sequence alone does not identify the reported ARBA assignment.


**Reason**

> General sequence reasoning can disfavor several choices, but does not meaningfully establish B. The key depends on an item-specific annotation absent from the model input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence does not clearly support any listed activity. B matches the database annotation, but the provided functional description points to a likely non-catalytic regulatory or scaffold role rather than endopeptidase activity.


### Important caveats

- The annotation and historical record match the supplied sequence, but the author's exact source snapshot is unknown.
- The GO annotation is computational; the cited functional description does not directly establish endopeptidase catalysis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and suggests a multipass membrane protein, which weighs against soluble kinase, DNA-binding, and endonuclease functions. But it does not provide a clear basis for assigning endopeptidase activity; the sequence-level clues do not establish that this membrane protein catalyzes peptide-bond hydrolysis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing B requires the protein-specific GO annotation or other external functional evidence; the supplied sequence alone does not identify the reported ARBA assignment.",
    "reason": "General sequence reasoning can disfavor several choices, but does not meaningfully establish B. The key depends on an item-specific annotation absent from the model input."
  },
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C6",
      "C5",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence has a UniProt GO annotation for endopeptidase activity, but its evidence is computational (IEA:UniProtKB-ARBA), not direct experimental confirmation. The accompanying functional description instead characterizes LyrA as probably non-catalytic in SagB-mediated peptidoglycan processing, so the annotation should not be treated as experimentally established."
  },
  "important_caveats": [
    "The annotation and historical record match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation is computational; the cited functional description does not directly establish endopeptidase catalysis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not clearly support any listed activity. B matches the database annotation, but the provided functional description points to a likely non-catalytic regulatory or scaffold role rather than endopeptidase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence has a UniProt GO annotation for endopeptidase activity, but its evidence is computational (IEA:UniProtKB-ARBA), not direct experimental confirmation. The accompanying functional description instead characterizes LyrA as probably non-catalytic in SagB-mediated peptidoglycan processing, so the annotation should not be treated as experimentally established.",
    "evidence_ids": ["C1", "C6", "C5", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and suggests a multipass membrane protein, which weighs against soluble kinase, DNA-binding, and endonuclease functions. But it does not provide a clear basis for assigning endopeptidase activity; the sequence-level clues do not establish that this membrane protein catalyzes peptide-bond hydrolysis.",
    "missing_item_specific_fact": "Distinguishing B requires the protein-specific GO annotation or other external functional evidence; the supplied sequence alone does not identify the reported ARBA assignment.",
    "reason": "General sequence reasoning can disfavor several choices, but does not meaningfully establish B. The key depends on an item-specific annotation absent from the model input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not clearly support any listed activity. B matches the database annotation, but the provided functional description points to a likely non-catalytic regulatory or scaffold role rather than endopeptidase activity."
  },
  "important_caveats": [
    "The annotation and historical record match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation is computational; the cited functional description does not directly establish endopeptidase catalysis."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0H3KA40 (LyrA/SpdC, Lysostaphin resistance protein A) carries the GO annotation GO:0004175 (endopeptidase activity) as evidenced in C6 and H5. However, this annotation is solely IEA:UniProtKB-ARBA (automatic rule-based inference), not experimentally validated. Critically, the experimental FUNCTION comment (C5, H4; ECO:0000269 PubMed:33593946) states the protein 'probably plays a non-catalytic role in the cleavage of nascent peptidoglycan' and acts 'as a scaffold protein.' The annotation exists and matches the expected answer, but its evidentiary basis is weak and partially contradicted by experimental data.

Citations as saved: [C6](#evidence-c6), [H5](#evidence-h5), [C5](#evidence-c5), [H4](#evidence-h4), [C8](#evidence-c8), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 419-aa sequence shows a hydrophobic N-terminal/transmembrane region, a large hydrophobic middle segment, and an acidic C-terminal tail. No recognizable catalytic triad, peptidase motif (e.g., Ser-His-Asp, Cys-His-Asn), kinase motif, DNA-binding domain (helix-turn-helix, zinc finger), or nuclease active site is identifiable from the sequence. All four options (dUMP kinase, endopeptidase, DNA binding, endonuclease) lack sequence-level support. The protein is in fact a membrane-associated scaffolding/regulatory protein with no intrinsic catalytic activity.


**Missing item-specific fact**

> The specific UniProt annotation assigning GO:0004175 (endopeptidase activity) to LyrA/SpdC via ARBA rule-based inference, which cannot be derived from sequence features alone since no peptidase catalytic motif is present.


**Reason**

> None of the four options can be distinguished from the amino acid sequence by general biological reasoning. The protein lacks any recognizable catalytic motif for peptidases, kinases, nucleases, or DNA-binding domains. Selection of answer B depends entirely on knowing the specific database annotation for this protein, which is itself an automatic inference contradicted by experimental evidence showing a non-catalytic scaffolding role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While none of the four options accurately describe the protein's true molecular function (scaffolding/regulatory protein in peptidoglycan processing), the annotation uniquely assigns GO:0004175. The other three options have zero supporting annotation or sequence evidence. However, the 'correct' answer itself is scientifically questionable given the experimental evidence of non-catalytic function.


### Important caveats

- The GO:0004175 annotation is IEA:UniProtKB-ARBA only (automatic rule-based inference), not experimentally verified.
- Experimental evidence (PubMed:33593946) explicitly describes a 'non-catalytic role' and 'scaffold protein' function, directly contradicting endopeptidase (catalytic) activity.
- The protein's true molecular function (scaffolding, protein binding, regulation of SagB) is not among the four options.
- The ARBA rule likely assigned endopeptidase activity based on the protein's involvement in peptidoglycan cleavage pathways, conflating pathway participation with intrinsic catalytic function.
- Sequence identity to UniProt A0A0H3KA40 is confirmed (SHA256 match), but the model receives no accession or name information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 419-aa sequence shows a hydrophobic N-terminal/transmembrane region, a large hydrophobic middle segment, and an acidic C-terminal tail. No recognizable catalytic triad, peptidase motif (e.g., Ser-His-Asp, Cys-His-Asn), kinase motif, DNA-binding domain (helix-turn-helix, zinc finger), or nuclease active site is identifiable from the sequence. All four options (dUMP kinase, endopeptidase, DNA binding, endonuclease) lack sequence-level support. The protein is in fact a membrane-associated scaffolding/regulatory protein with no intrinsic catalytic activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt annotation assigning GO:0004175 (endopeptidase activity) to LyrA/SpdC via ARBA rule-based inference, which cannot be derived from sequence features alone since no peptidase catalytic motif is present.",
    "reason": "None of the four options can be distinguished from the amino acid sequence by general biological reasoning. The protein lacks any recognizable catalytic motif for peptidases, kinases, nucleases, or DNA-binding domains. Selection of answer B depends entirely on knowing the specific database annotation for this protein, which is itself an automatic inference contradicted by experimental evidence showing a non-catalytic scaffolding role."
  },
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H5",
      "C5",
      "H4",
      "C8",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H3KA40 (LyrA/SpdC, Lysostaphin resistance protein A) carries the GO annotation GO:0004175 (endopeptidase activity) as evidenced in C6 and H5. However, this annotation is solely IEA:UniProtKB-ARBA (automatic rule-based inference), not experimentally validated. Critically, the experimental FUNCTION comment (C5, H4; ECO:0000269 PubMed:33593946) states the protein 'probably plays a non-catalytic role in the cleavage of nascent peptidoglycan' and acts 'as a scaffold protein.' The annotation exists and matches the expected answer, but its evidentiary basis is weak and partially contradicted by experimental data."
  },
  "important_caveats": [
    "The GO:0004175 annotation is IEA:UniProtKB-ARBA only (automatic rule-based inference), not experimentally verified.",
    "Experimental evidence (PubMed:33593946) explicitly describes a 'non-catalytic role' and 'scaffold protein' function, directly contradicting endopeptidase (catalytic) activity.",
    "The protein's true molecular function (scaffolding, protein binding, regulation of SagB) is not among the four options.",
    "The ARBA rule likely assigned endopeptidase activity based on the protein's involvement in peptidoglycan cleavage pathways, conflating pathway participation with intrinsic catalytic function.",
    "Sequence identity to UniProt A0A0H3KA40 is confirmed (SHA256 match), but the model receives no accession or name information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While none of the four options accurately describe the protein's true molecular function (scaffolding/regulatory protein in peptidoglycan processing), the annotation uniquely assigns GO:0004175. The other three options have zero supporting annotation or sequence evidence. However, the 'correct' answer itself is scientifically questionable given the experimental evidence of non-catalytic function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H3KA40 (LyrA/SpdC, Lysostaphin resistance protein A) carries the GO annotation GO:0004175 (endopeptidase activity) as evidenced in C6 and H5. However, this annotation is solely IEA:UniProtKB-ARBA (automatic rule-based inference), not experimentally validated. Critically, the experimental FUNCTION comment (C5, H4; ECO:0000269 PubMed:33593946) states the protein 'probably plays a non-catalytic role in the cleavage of nascent peptidoglycan' and acts 'as a scaffold protein.' The annotation exists and matches the expected answer, but its evidentiary basis is weak and partially contradicted by experimental data.",
    "evidence_ids": ["C6", "H5", "C5", "H4", "C8", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The 419-aa sequence shows a hydrophobic N-terminal/transmembrane region, a large hydrophobic middle segment, and an acidic C-terminal tail. No recognizable catalytic triad, peptidase motif (e.g., Ser-His-Asp, Cys-His-Asn), kinase motif, DNA-binding domain (helix-turn-helix, zinc finger), or nuclease active site is identifiable from the sequence. All four options (dUMP kinase, endopeptidase, DNA binding, endonuclease) lack sequence-level support. The protein is in fact a membrane-associated scaffolding/regulatory protein with no intrinsic catalytic activity.",
    "missing_item_specific_fact": "The specific UniProt annotation assigning GO:0004175 (endopeptidase activity) to LyrA/SpdC via ARBA rule-based inference, which cannot be derived from sequence features alone since no peptidase catalytic motif is present.",
    "reason": "None of the four options can be distinguished from the amino acid sequence by general biological reasoning. The protein lacks any recognizable catalytic motif for peptidases, kinases, nucleases, or DNA-binding domains. Selection of answer B depends entirely on knowing the specific database annotation for this protein, which is itself an automatic inference contradicted by experimental evidence showing a non-catalytic scaffolding role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While none of the four options accurately describe the protein's true molecular function (scaffolding/regulatory protein in peptidoglycan processing), the annotation uniquely assigns GO:0004175. The other three options have zero supporting annotation or sequence evidence. However, the 'correct' answer itself is scientifically questionable given the experimental evidence of non-catalytic function."
  },
  "important_caveats": [
    "The GO:0004175 annotation is IEA:UniProtKB-ARBA only (automatic rule-based inference), not experimentally verified.",
    "Experimental evidence (PubMed:33593946) explicitly describes a 'non-catalytic role' and 'scaffold protein' function, directly contradicting endopeptidase (catalytic) activity.",
    "The protein's true molecular function (scaffolding, protein binding, regulation of SagB) is not among the four options.",
    "The ARBA rule likely assigned endopeptidase activity based on the protein's involvement in peptidoglycan cleavage pathways, conflating pathway participation with intrinsic catalytic function.",
    "Sequence identity to UniProt A0A0H3KA40 is confirmed (SHA256 match), but the model receives no accession or name information."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: uncertain

> The matched record assigns endopeptidase activity by computational IEA:UniProtKB-ARBA (C6), but the cited functional description instead presents this protein as a likely non-catalytic regulator or scaffold for peptidoglycan processing (C5). That does not establish catalysis of peptide bonds, the activity defined by endopeptidase, nor definitively rule out another activity. Thus the annotation supports the key as a database prediction, but the supplied evidence does not settle the scientific claim.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and appears to contain many transmembrane segments, with a charged, low-complexity C-terminal region. This makes a conventional soluble kinase or DNA-binding/nuclease protein less plausible. But those features do not identify an endopeptidase, and the sequence does not show an obvious catalytic protease signature that would distinguish B from the other choices with confidence.


**Missing item-specific fact**

> The exact protein's recorded endopeptidase annotation, which is a computational ARBA assignment in the matched record.


**Reason**

> Transferable sequence and protein-family reasoning can make some distractors less plausible, but it does not meaningfully establish peptide-bond-cleaving activity for this multipass protein. Selecting B depends on the exact target's annotation rather than a convincing inference from the original inputs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence does not clearly support any offered function, and the evidence does not establish multiple competing options. This is a lack of a well-supported choice, not a case where two options are comparably defensible.


### Important caveats

- The matched record's endopeptidase annotation is computational, not experimental evidence of peptide-bond hydrolysis.
- The cited non-catalytic role concerns regulation of peptidoglycan processing; it does not by itself exclude every possible catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and appears to contain many transmembrane segments, with a charged, low-complexity C-terminal region. This makes a conventional soluble kinase or DNA-binding/nuclease protein less plausible. But those features do not identify an endopeptidase, and the sequence does not show an obvious catalytic protease signature that would distinguish B from the other choices with confidence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact protein's recorded endopeptidase annotation, which is a computational ARBA assignment in the matched record.",
    "reason": "Transferable sequence and protein-family reasoning can make some distractors less plausible, but it does not meaningfully establish peptide-bond-cleaving activity for this multipass protein. Selecting B depends on the exact target's annotation rather than a convincing inference from the original inputs."
  },
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "GO2"
    ],
    "judgment": "cannot_determine",
    "reason": "The matched record assigns endopeptidase activity by computational IEA:UniProtKB-ARBA (C6), but the cited functional description instead presents this protein as a likely non-catalytic regulator or scaffold for peptidoglycan processing (C5). That does not establish catalysis of peptide bonds, the activity defined by endopeptidase, nor definitively rule out another activity. Thus the annotation supports the key as a database prediction, but the supplied evidence does not settle the scientific claim."
  },
  "important_caveats": [
    "The matched record's endopeptidase annotation is computational, not experimental evidence of peptide-bond hydrolysis.",
    "The cited non-catalytic role concerns regulation of peptidoglycan processing; it does not by itself exclude every possible catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not clearly support any offered function, and the evidence does not establish multiple competing options. This is a lack of a well-supported choice, not a case where two options are comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The matched record assigns endopeptidase activity by computational IEA:UniProtKB-ARBA (C6), but the cited functional description instead presents this protein as a likely non-catalytic regulator or scaffold for peptidoglycan processing (C5). That does not establish catalysis of peptide bonds, the activity defined by endopeptidase, nor definitively rule out another activity. Thus the annotation supports the key as a database prediction, but the supplied evidence does not settle the scientific claim.",
    "evidence_ids": ["C5", "C6", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and appears to contain many transmembrane segments, with a charged, low-complexity C-terminal region. This makes a conventional soluble kinase or DNA-binding/nuclease protein less plausible. But those features do not identify an endopeptidase, and the sequence does not show an obvious catalytic protease signature that would distinguish B from the other choices with confidence.",
    "missing_item_specific_fact": "The exact protein's recorded endopeptidase annotation, which is a computational ARBA assignment in the matched record.",
    "reason": "Transferable sequence and protein-family reasoning can make some distractors less plausible, but it does not meaningfully establish peptide-bond-cleaving activity for this multipass protein. Selecting B depends on the exact target's annotation rather than a convincing inference from the original inputs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not clearly support any offered function, and the evidence does not establish multiple competing options. This is a lack of a well-supported choice, not a case where two options are comparably defensible."
  },
  "important_caveats": [
    "The matched record's endopeptidase annotation is computational, not experimental evidence of peptide-bond hydrolysis.",
    "The cited non-catalytic role concerns regulation of peptidoglycan processing; it does not by itself exclude every possible catalytic activity."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0H3KA40) carries GO:0004175 (endopeptidase activity) as a molecular function annotation (evidence C6, H5). However, the evidence code is IEA:UniProtKB-ARBA (purely computational/inferred by electronic annotation), not experimental. Critically, the experimental evidence (PubMed:33593946, PubMed:20923422; evidence C5, H4) explicitly states the protein 'probably plays a non-catalytic role' and 'perhaps acting as a scaffold protein' in peptidoglycan processing. The annotation is therefore a database record that is contradicted by the underlying experimental characterization. The key is supported in the narrow sense that the annotation exists, but it is a low-confidence computational inference that conflicts with the protein's experimentally determined non-catalytic, scaffold-like function.

Citations as saved: [C6](#evidence-c6), [C5](#evidence-c5), [H5](#evidence-h5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence shows a clear multi-transmembrane architecture: a hydrophobic N-terminal region (~residues 1–140) containing approximately 5–6 TM helix-length hydrophobic stretches, followed by a long hydrophilic, acidic C-terminal cytoplasmic tail (~residues 141–419). This is the hallmark topology of a membrane-embedded or membrane-associated protein. Among the four options, a knowledgeable model can apply the transferable principle that dUMP kinase (A) is a small (~200 aa) soluble cytoplasmic enzyme with a characteristic kinase fold; DNA binding (C) requires specific structural motifs (HTH, zinc finger, winged-helix) in soluble proteins; and endonuclease activity (D) is typically a soluble catalytic function. All three are strongly incompatible with a multi-TM membrane protein. Endopeptidase activity (B), by contrast, is a well-established class of membrane-embedded catalytic activity (rhomboid proteases, signal peptide peptidase, presenilin/gamma-secretase, site-2 protease). While this particular protein lacks obvious protease catalytic residues, the membrane architecture makes B the only option that is architecturally plausible for a multi-TM protein. This elimination-based inference from membrane protease biology meaningfully distinguishes B from A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-TM membrane topology visible in the sequence allows a model to eliminate the three soluble-enzyme options (kinase, DNA binding, endonuclease) and select the only membrane-compatible activity (endopeptidase) by analogy with known membrane protease families. This is a legitimate transferable inference, though it is probabilistic and does not confirm that this specific protein is actually catalytic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (dUMP kinase, DNA binding, endonuclease) are clearly incompatible with a multi-TM membrane protein of 419 residues, leaving B as the only architecturally plausible choice among the offered options. No genuine ambiguity among the four alternatives is identified.


### Important caveats

- The GO:0004175 annotation is IEA:UniProtKB-ARBA (automatic rule-based inference), not experimental. The experimental evidence (PubMed:33593946) describes the protein as playing a 'non-catalytic role' and acting 'perhaps as a scaffold protein,' which contradicts endopeptidase activity.
- The protein (LyrA/SpdC) is a membrane scaffold/regulatory protein in S. aureus involved in peptidoglycan processing and surface protein display, not a protease. The database annotation may be an incorrect automatic inference.
- The membrane-protease elimination argument is architecturally valid but does not confirm catalytic activity; many membrane proteins are non-catalytic scaffolds, transporters, or receptors.
- The sequence lacks canonical protease catalytic motifs (Ser-His-Asp, Cys-His, Asp-His-His, or the rhomboid GxSx motif), so the positive identification of endopeptidase activity rests solely on elimination of clearly incompatible options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows a clear multi-transmembrane architecture: a hydrophobic N-terminal region (~residues 1–140) containing approximately 5–6 TM helix-length hydrophobic stretches, followed by a long hydrophilic, acidic C-terminal cytoplasmic tail (~residues 141–419). This is the hallmark topology of a membrane-embedded or membrane-associated protein. Among the four options, a knowledgeable model can apply the transferable principle that dUMP kinase (A) is a small (~200 aa) soluble cytoplasmic enzyme with a characteristic kinase fold; DNA binding (C) requires specific structural motifs (HTH, zinc finger, winged-helix) in soluble proteins; and endonuclease activity (D) is typically a soluble catalytic function. All three are strongly incompatible with a multi-TM membrane protein. Endopeptidase activity (B), by contrast, is a well-established class of membrane-embedded catalytic activity (rhomboid proteases, signal peptide peptidase, presenilin/gamma-secretase, site-2 protease). While this particular protein lacks obvious protease catalytic residues, the membrane architecture makes B the only option that is architecturally plausible for a multi-TM protein. This elimination-based inference from membrane protease biology meaningfully distinguishes B from A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-TM membrane topology visible in the sequence allows a model to eliminate the three soluble-enzyme options (kinase, DNA binding, endonuclease) and select the only membrane-compatible activity (endopeptidase) by analogy with known membrane protease families. This is a legitimate transferable inference, though it is probabilistic and does not confirm that this specific protein is actually catalytic."
  },
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C5",
      "H5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0H3KA40) carries GO:0004175 (endopeptidase activity) as a molecular function annotation (evidence C6, H5). However, the evidence code is IEA:UniProtKB-ARBA (purely computational/inferred by electronic annotation), not experimental. Critically, the experimental evidence (PubMed:33593946, PubMed:20923422; evidence C5, H4) explicitly states the protein 'probably plays a non-catalytic role' and 'perhaps acting as a scaffold protein' in peptidoglycan processing. The annotation is therefore a database record that is contradicted by the underlying experimental characterization. The key is supported in the narrow sense that the annotation exists, but it is a low-confidence computational inference that conflicts with the protein's experimentally determined non-catalytic, scaffold-like function."
  },
  "important_caveats": [
    "The GO:0004175 annotation is IEA:UniProtKB-ARBA (automatic rule-based inference), not experimental. The experimental evidence (PubMed:33593946) describes the protein as playing a 'non-catalytic role' and acting 'perhaps as a scaffold protein,' which contradicts endopeptidase activity.",
    "The protein (LyrA/SpdC) is a membrane scaffold/regulatory protein in S. aureus involved in peptidoglycan processing and surface protein display, not a protease. The database annotation may be an incorrect automatic inference.",
    "The membrane-protease elimination argument is architecturally valid but does not confirm catalytic activity; many membrane proteins are non-catalytic scaffolds, transporters, or receptors.",
    "The sequence lacks canonical protease catalytic motifs (Ser-His-Asp, Cys-His, Asp-His-His, or the rhomboid GxSx motif), so the positive identification of endopeptidase activity rests solely on elimination of clearly incompatible options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (dUMP kinase, DNA binding, endonuclease) are clearly incompatible with a multi-TM membrane protein of 419 residues, leaving B as the only architecturally plausible choice among the offered options. No genuine ambiguity among the four alternatives is identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0H3KA40) carries GO:0004175 (endopeptidase activity) as a molecular function annotation (evidence C6, H5). However, the evidence code is IEA:UniProtKB-ARBA (purely computational/inferred by electronic annotation), not experimental. Critically, the experimental evidence (PubMed:33593946, PubMed:20923422; evidence C5, H4) explicitly states the protein 'probably plays a non-catalytic role' and 'perhaps acting as a scaffold protein' in peptidoglycan processing. The annotation is therefore a database record that is contradicted by the underlying experimental characterization. The key is supported in the narrow sense that the annotation exists, but it is a low-confidence computational inference that conflicts with the protein's experimentally determined non-catalytic, scaffold-like function.",
    "evidence_ids": ["C6", "C5", "H5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence shows a clear multi-transmembrane architecture: a hydrophobic N-terminal region (~residues 1–140) containing approximately 5–6 TM helix-length hydrophobic stretches, followed by a long hydrophilic, acidic C-terminal cytoplasmic tail (~residues 141–419). This is the hallmark topology of a membrane-embedded or membrane-associated protein. Among the four options, a knowledgeable model can apply the transferable principle that dUMP kinase (A) is a small (~200 aa) soluble cytoplasmic enzyme with a characteristic kinase fold; DNA binding (C) requires specific structural motifs (HTH, zinc finger, winged-helix) in soluble proteins; and endonuclease activity (D) is typically a soluble catalytic function. All three are strongly incompatible with a multi-TM membrane protein. Endopeptidase activity (B), by contrast, is a well-established class of membrane-embedded catalytic activity (rhomboid proteases, signal peptide peptidase, presenilin/gamma-secretase, site-2 protease). While this particular protein lacks obvious protease catalytic residues, the membrane architecture makes B the only option that is architecturally plausible for a multi-TM protein. This elimination-based inference from membrane protease biology meaningfully distinguishes B from A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The multi-TM membrane topology visible in the sequence allows a model to eliminate the three soluble-enzyme options (kinase, DNA binding, endonuclease) and select the only membrane-compatible activity (endopeptidase) by analogy with known membrane protease families. This is a legitimate transferable inference, though it is probabilistic and does not confirm that this specific protein is actually catalytic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (dUMP kinase, DNA binding, endonuclease) are clearly incompatible with a multi-TM membrane protein of 419 residues, leaving B as the only architecturally plausible choice among the offered options. No genuine ambiguity among the four alternatives is identified."
  },
  "important_caveats": [
    "The GO:0004175 annotation is IEA:UniProtKB-ARBA (automatic rule-based inference), not experimental. The experimental evidence (PubMed:33593946) describes the protein as playing a 'non-catalytic role' and acting 'perhaps as a scaffold protein,' which contradicts endopeptidase activity.",
    "The protein (LyrA/SpdC) is a membrane scaffold/regulatory protein in S. aureus involved in peptidoglycan processing and surface protein display, not a protease. The database annotation may be an incorrect automatic inference.",
    "The membrane-protease elimination argument is architecturally valid but does not confirm catalytic activity; many membrane proteins are non-catalytic scaffolds, transporters, or receptors.",
    "The sequence lacks canonical protease catalytic motifs (Ser-His-Asp, Cys-His, Asp-His-His, or the rhomboid GxSx motif), so the positive identification of endopeptidase activity rests solely on elimination of clearly incompatible options."
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
  "requested_accession": "A0A0H3KA40",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "bf64f9d9785229636b37dbec53661c2fc5d174ff9bc941655a421585f73e403f",
  "benchmark_sequence_length": 419,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 38,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "current_source_sequence_sha256": "bf64f9d9785229636b37dbec53661c2fc5d174ff9bc941655a421585f73e403f",
  "current_source_sequence_length": 419,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 36,
  "selected_historical_version": {
    "accession": "A0A0H3KA40",
    "database": "Swiss-Prot",
    "entryVersion": 36,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LYRA_STAAE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "selected_historical_source_sequence_sha256": "bf64f9d9785229636b37dbec53661c2fc5d174ff9bc941655a421585f73e403f",
  "selected_historical_source_sequence_length": 419,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 36,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A0H3KA40\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":38,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Staphylococcaceae\",\"Staphylococcus\"],\"scientificName\":\"Staphylococcus aureus (strain Newman)\",\"taxonId\":426430}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20923422\",\"source\":\"PubMed\"}],\"value\":\"Abortive infectivity domain-containing protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20923422\",\"source\":\"PubMed\"}],\"value\":\"Surface protein display C\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Lysostaphin resistance protein A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q2FVT1\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20923422\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33593946\",\"source\":\"PubMed\"}],\"value\":\"Involved in bacterial cell envelope homeostasis (PubMed:33593946). Regulates peptidoglycan processing by N-acetylglucosaminidase SagB, perhaps acting as a scaffold protein (PubMed:33593946). As part of a complex with SagB, probably plays a non-catalytic role in the cleavage of nascent peptidoglycan, preferentially yielding longer lipid-linked oligomers (By similarity). Pleiotropic regulator of gene expression, probably acting via interactions with multiple two-component systems (By similarity). Plays a role in the abundant deposition of the immunoglobulin G-binding protein A (spa) at the cross-wall, a subcellular structure that initially arises from cytokinesis (PubMed:20923422)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004175\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:endopeptidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Frankel M.B.\",\"Wojcik B.M.\",\"DeDent A.C.\",\"Missiakas D.M.\",\"Schneewind O.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20923422\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1365-2958.2010.07334.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"238\",\"id\":\"20923422\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"252\",\"publicationDate\":\"2010\",\"title\":\"ABI domain-containing proteins contribute to surface protein display and cell division in Staphylococcus aureus.\",\"volume\":\"78\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Willing S.\",\"Schneewind O.\",\"Missiakas D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33593946\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.00014-21\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"33593946\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"0\",\"publicationDate\":\"2021\",\"title\":\"Regulated cleavage of glycan strands by the murein hydrolase SagB in S. aureus involves a direct interaction with LyrA (SpdC).\",\"volume\":\"203\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH SAGB\",\"MUTAGENESIS OF GLU-135; ARG-139; ARG-196 AND HIS-210\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   LYRA_STAAE              Reviewed;         419 AA.\nAC   A0A0H3KA40;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 36.\nDE   RecName: Full=Lysostaphin resistance protein A;\nDE   AltName: Full=Abortive infectivity domain-containing protein {ECO:0000303|PubMed:20923422};\nDE   AltName: Full=Surface protein display C {ECO:0000303|PubMed:20923422};\nGN   Name=lyrA {ECO:0000250|UniProtKB:Q2FVT1};\nGN   Synonyms=spdC {ECO:0000303|PubMed:33593946};\nGN   OrderedLocusNames=NWMN_2236 {ECO:0000312|EMBL:BAF68508.1};\nOS   Staphylococcus aureus (strain Newman).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Staphylococcaceae;\nOC   Staphylococcus.\nOX   NCBI_TaxID=426430 {ECO:0000312|Proteomes:UP000006386};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "source_locator": "lines 25-31",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND SUBCELLULAR LOCATION.\nRX   PubMed=20923422; DOI=10.1111/j.1365-2958.2010.07334.x;\nRA   Frankel M.B., Wojcik B.M., DeDent A.C., Missiakas D.M., Schneewind O.;\nRT   \"ABI domain-containing proteins contribute to surface protein display and\nRT   cell division in Staphylococcus aureus.\";\nRL   Mol. Microbiol. 78:238-252(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "source_locator": "lines 32-39",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH SAGB, AND MUTAGENESIS OF GLU-135; ARG-139;\nRP   ARG-196 AND HIS-210.\nRX   PubMed=33593946; DOI=10.1128/jb.00014-21;\nRA   Willing S., Schneewind O., Missiakas D.;\nRT   \"Regulated cleavage of glycan strands by the murein hydrolase SagB in S.\nRT   aureus involves a direct interaction with LyrA (SpdC).\";\nRL   J. Bacteriol. 203:0-0(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "source_locator": "lines 40-52",
  "excerpt": "CC   -!- FUNCTION: Involved in bacterial cell envelope homeostasis\nCC       (PubMed:33593946). Regulates peptidoglycan processing by N-\nCC       acetylglucosaminidase SagB, perhaps acting as a scaffold protein\nCC       (PubMed:33593946). As part of a complex with SagB, probably plays a\nCC       non-catalytic role in the cleavage of nascent peptidoglycan,\nCC       preferentially yielding longer lipid-linked oligomers (By similarity).\nCC       Pleiotropic regulator of gene expression, probably acting via\nCC       interactions with multiple two-component systems (By similarity). Plays\nCC       a role in the abundant deposition of the immunoglobulin G-binding\nCC       protein A (spa) at the cross-wall, a subcellular structure that\nCC       initially arises from cytokinesis (PubMed:20923422).\nCC       {ECO:0000250|UniProtKB:Q2FVT1, ECO:0000269|PubMed:20923422,\nCC       ECO:0000269|PubMed:33593946}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "source_locator": "lines 86-86",
  "excerpt": "DR   GO; GO:0004175; F:endopeptidase activity; IEA:UniProtKB-ARBA.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 36,
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
  "source_locator": "lines 27794-27818",
  "excerpt": "[Term]\nid: GO:0003677\nname: DNA binding\nnamespace: molecular_function\nalt_id: GO:0043566\ndef: \"Any molecular function by which a gene product interacts selectively and non-covalently with DNA (deoxyribonucleic acid).\" [GOC:dph, GOC:jl, GOC:tb, GOC:vw]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"microtubule/chromatin interaction\" RELATED []\nsynonym: \"plasmid binding\" NARROW []\nsynonym: \"structure specific DNA binding\" RELATED []\nsynonym: \"structure-specific DNA binding\" RELATED []\nis_a: GO:0003676 ! nucleic acid binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0003677"
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
  "source_locator": "lines 36973-37083",
  "excerpt": "[Term]\nid: GO:0004175\nname: endopeptidase activity\nnamespace: molecular_function\nalt_id: GO:0016809\ndef: \"Catalysis of the hydrolysis of internal, alpha-peptide bonds in a polypeptide chain.\" [http://merops.sanger.ac.uk/about/glossary.htm#ENDOPEPTIDASE]\nsynonym: \"elastase activity\" RELATED [GOC:krc]\nsynonym: \"endoprotease activity\" NARROW []\nsynonym: \"proteasome endopeptidase activity\" NARROW []\nsynonym: \"proteinase\" NARROW []\nxref: EC:3.4.99.-\nxref: Reactome:R-HSA-1168640 \"Ubiquitinated IkB is degraded\"\nxref: Reactome:R-HSA-1234159 \"Proteasome proteolyzes ub-HIF-alpha\"\nxref: Reactome:R-HSA-1236935 \"Proteasomal cleavage of substrate (26S proteasome catalyst)\"\nxref: Reactome:R-HSA-1236970 \"Proteasomal clevage of exogenous antigen (26S proteasome catalyst)\"\nxref: Reactome:R-HSA-1251997 \"Cleavage of ERBB4m80 by gamma-scretase complex\"\nxref: Reactome:R-HSA-1433374 \"Processing of SCF isoform 1\"\nxref: Reactome:R-HSA-1504193 \"Ubiquitinated DVL is degraded by the proteasome\"\nxref: Reactome:R-HSA-174058 \"Degradation of multiubiquitinated Cdh1\"\nxref: Reactome:R-HSA-174105 \"Degradation of multiubiquitinated cell cycle proteins\"\nxref: Reactome:R-HSA-174202 \"Degradation of multiubiquitinated Securin\"\nxref: Reactome:R-HSA-174203 \"SCF-mediated degradation of Emi1\"\nxref: Reactome:R-HSA-174255 \"Degradation multiubiquitinated Cyclin A\"\nxref: Reactome:R-HSA-180573 \"Degradation of ubiquitinated CD4\"\nxref: Reactome:R-HSA-180603 \"Proteosome-mediated degradation of APOBEC3G\"\nxref: Reactome:R-HSA-187574 \"Degradation of ubiquitinated p27/p21 by the 26S proteasome\"\nxref: Reactome:R-HSA-188191 \"APC/C:Cdh1-mediated degradation of Skp2\"\nxref: Reactome:R-HSA-193682 \"gamma-secretase cleaves the p75NTR transmembrane domain\"\nxref: Reactome:R-HSA-209061 \"Ubiquitinated and phosphorylated IKBA binds to and is degraded by the proteasome complex\"\nxref: Reactome:R-HSA-211715 \"Proteasome mediated degradation of PAK-2p34\"\nxref: Reactome:R-HSA-2130282 \"Degradation of ubiquitinated beta catenin by the proteasome\"\nxref: Reactome:R-HSA-2213200 \"Release of endostatin-like peptides\"\nxref: Reactome:R-HSA-264458 \"Proteasome mediated degradation of COP1\"\nxref: Reactome:R-HSA-353125 \"26S proteosome degrades ODC holoenzyme complex\"\nxref: Reactome:R-HSA-3640874 \"Ub-RibC-AXIN is degraded by the proteasome\"\nxref: Reactome:R-HSA-3928656 \"gamma-secretase cleaves EPHB2\"\nxref: Reactome:R-HSA-450466 \"AUF1:mRNA complex is degraded\"\nxref: Reactome:R-HSA-4608855 \"PRICKLE1 is degraded by the proteasome\"\nxref: Reactome:R-HSA-4641256 \"Ubiquitinated AXIN is degraded by the proteasome\"\nxref: Reactome:R-HSA-4641260 \"Ubiquitinated DVL1 is degraded by the proteasome\"\nxref: Reactome:R-HSA-5358340 \"Autoproteolytic cleavage of Hh precursors\"\nxref: Reactome:R-HSA-5358460 \"HPE SHH variants don't undergo autoproteolytic cleavage\"\nxref: Reactome:R-HSA-5362448 \"Hh C-terminal fragments are degraded by the proteasome\"\nxref: Reactome:R-HSA-5387392 \"processing defective Hh variants are degraded by the proteasome\"\nxref: Reactome:R-HSA-5607724 \"26S proteasome processes K48PolyUb-K21,22-p-S32,36-IkBA:NF-kB complex to form NF-kB complex\"\nxref: Reactome:R-HSA-5607731 \"26S proteasome processes p-7S-p100:RELB to form p52:RELB\"\nxref: Reactome:R-HSA-5610754 \"GLI3 is partially degraded by the proteasome to yield the GLI3 repressor\"\nxref: Reactome:R-HSA-5610757 \"GLI2 is degraded by the proteasome\"\nxref: Reactome:R-HSA-5610758 \"GLI1 is degraded by the proteasome after ubiquitination by beta-TrCP\"\nxref: Reactome:R-HSA-5610760 \"GLI1 is degraded by the proteasome after ubiquitination by ITCH\"\nxref: Reactome:R-HSA-5635854 \"GLI2,3 are degraded by the proteasome\"\nxref: Reactome:R-HSA-5635868 \"ub-GLI is degraded by the proteasome\"\nxref: Reactome:R-HSA-5658430 \"NF1 is degraded by the proteasome\"\nxref: Reactome:R-HSA-5668481 \"Protesomal degradation of K48polyUb-TRAF3\"\nxref: Reactome:R-HSA-5668520 \"26Sproteasome degrades K48polyUb-NIK\"\nxref: Reactome:R-HSA-5687112 \"MAPK6 is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-5693081 \"FURIN cleaves 7K-BACE1 to 7K-BACE1(46-501)\"\nxref: Reactome:R-HSA-6784628 \"PCSK6,FURIN mediate dissociation of 2 x LPL from GPIHBP1:HSPG:LPL dimer\"\nxref: Reactome:R-HSA-6784676 \"PCSK5 mediates dissociation of 2 x LPL from GPIHBP1:HSPG:LPL dimer\"\nxref: Reactome:R-HSA-68825 \"Ubiquitinated geminin is degraded by the proteasome\"\nxref: Reactome:R-HSA-68948 \"Ubiquitinated Orc1 is degraded by the proteasome\"\nxref: Reactome:R-HSA-69016 \"Ubiquitinated Cdc6 is degraded by the proteasome\"\nxref: Reactome:R-HSA-69600 \"Proteolytic degradation of ubiquitinated-Cdc25A\"\nxref: Reactome:R-HSA-74730 \"Insulin degradation\"\nxref: Reactome:R-HSA-75825 \"Proteasome mediated degradation of Cyclin D1\"\nxref: Reactome:R-HSA-8849797 \"Membrane proteases cleave Profilaggrin producing Filaggrin\"\nxref: Reactome:R-HSA-8850992 \"Proteasome degrades polyubiquitinated PTEN\"\nxref: Reactome:R-HSA-8852354 \"GTSE1 facilitates proteasome-mediated degradation of TP53\"\nxref: Reactome:R-HSA-8854044 \"Proteasome degrades AURKA ubiquitinated by SCF-FBXL7\"\nxref: Reactome:R-HSA-8854071 \"Proteasome-mediated degradation of PolyUb-FBXL7\"\nxref: Reactome:R-HSA-8866553 \"misfolded CFTR is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-8866858 \"CFTR F508del is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-8932355 \"26S proteasome degrades Ub-NFE2L2\"\nxref: Reactome:R-HSA-8934819 \"Cytoplasmic proteases cleave Profilaggrin producing Filaggrin\"\nxref: Reactome:R-HSA-8939801 \"26S proteasome degrades PolyUb-RUNX2\"\nxref: Reactome:R-HSA-8952408 \"Polyubiquitinated RUNX3 is degraded by the proteasome\"\nxref: Reactome:R-HSA-8957265 \"26S proteasome degrades TP73 polyubiquitinated by ITCH\"\nxref: Reactome:R-HSA-9008110 \"Proteasome degrades polyubiquitinated RUNX2\"\nxref: Reactome:R-HSA-9009362 \"Proteasome degrades PolyUb-RUNX2\"\nxref: Reactome:R-HSA-9010096 \"Gamma-secretase cleaves APP(672-770) to APP(672-711) and APP(672-713)\"\nxref: Reactome:R-HSA-9011313 \"Proteasome degrades ubiquitinated ROBO3.1\"\nxref: Reactome:R-HSA-9604642 \"Proteasome degrades ubiquitinated NICD4\"\nxref: Reactome:R-HSA-9614271 \"Autocleavage of ADGRG6\"\nxref: Reactome:R-HSA-9755303 \"26S proteasome degrades HIFalpha\"\nxref: Reactome:R-HSA-9755306 \"ub UBXN7 is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-9760521 \"Unknown peptidase cleaves pro-STa\"\nxref: Reactome:R-HSA-9762096 \"Ub,pS335,S338,T NFE2L2 is degraded\"\nxref: Reactome:R-HSA-9766223 \"Proteasome-dependent degradation of ubiquitinated CDH1\"\nxref: Reactome:R-HSA-983150 \"Proteasomal cleavage of substrate\"\nxref: Reactome:R-HSA-983158 \"Trimming of peptides in ER\"\nxref: Reactome:R-HSA-9839376 \"TGFBR3(784-851) degradation\"\nxref: Reactome:R-HSA-9906017 \"Unknown peptidase cleaves UQCRFS1 subunit\"\nxref: Reactome:R-HSA-9908101 \"Maturation of the canonical 20S core particle\"\nxref: Reactome:R-HSA-9908105 \"Maturation of the 20S immunoproteasome core particle\"\nxref: Reactome:R-HSA-9908108 \"Maturation of the 20S thymoproteasome core particle\"\nxref: Reactome:R-HSA-9908780 \"Maturation of the preholospermatoproteasome\"\nxref: Reactome:R-HSA-9912636 \"Proteasomal cleavage of intracellular substrate (PA28-alpha-beta-20S proteasome catalyst)\"\nxref: Reactome:R-HSA-9912655 \"Proteasomal cleavage of intracellular substrate (immunoproteasome catalyst)\"\nxref: Reactome:R-HSA-9912747 \"Proteasomal clevage of exogenous antigen (immunoproteasome catalyst)\"\nxref: Reactome:R-HSA-9912751 \"Proteasomal cleavage of partially digested antigen (immunoproteasome catalyst)\"\nxref: Reactome:R-HSA-9929352 \"Ubiquitinated CD274 is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-9929486 \"SPOP-mediated degradation of CD274 by 26S Proteosome\"\nxref: Reactome:R-HSA-9931314 \"Proteasomal degradation of polyUb-p-S195-CD274\"\nxref: Reactome:R-HSA-9934884 \"Proteolysis of K48polyUb,p-S-CRY1,2\"\nxref: Reactome:R-HSA-9934887 \"Proteolysis of K48polyUb-K107,p-S-CRY1,K48polyUb-K126,p-S-CRY2\"\nxref: Reactome:R-HSA-9934893 \"Proteolysis of K48polyUb-K,p-S-PER1,2,3\"\nxref: Reactome:R-HSA-9949676 \"The proteasome degrades the alanine-tailed K48-polyUb nascent peptide bound to LTN1:NEMF:TCF25:VCP hexamer\"\nxref: Reactome:R-HSA-9954728 \"The proteasome degrades the K48-polyubiquitinated alanine-tailed nascent peptide\"\nis_a: GO:0008233 ! peptidase activity\nproperty_value: skos:narrowMatch EC:3.4.99.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004175"
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
  "source_locator": "lines 43848-43862",
  "excerpt": "[Term]\nid: GO:0004519\nname: endonuclease activity\nnamespace: molecular_function\ndef: \"Catalysis of the cleavage of ester linkages within nucleic acids by creating internal breaks.\" [GOC:mah, ISBN:0198547684]\nxref: Reactome:R-HSA-5358512 \"MLH1:PMS2 makes single strand incision near  insertion/deletion loop of 2 bases or more\"\nxref: Reactome:R-HSA-5358518 \"MLH1:PMS2 makes single strand incision near 1-2 base mismatch\"\nxref: Reactome:R-HSA-5690990 \"5'- incision of DNA by ERCC1:ERCC4 in GG-NER\"\nxref: Reactome:R-HSA-5693533 \"DCLRE1C (ARTEMIS) processes DNA DSB ends\"\nxref: Reactome:R-HSA-72180 \"Cleavage of mRNA at the 3'-end\"\nxref: Reactome:R-HSA-9970193 \"CPSF3 cleaves pre-mRNA at distal 3'UTR PAS\"\nxref: Reactome:R-HSA-9970282 \"U1 snRNP suppresses CPSF3-mediated pre-mRNA cleavage at intronic PAS\"\nxref: Reactome:R-HSA-9970294 \"CPSF3 cleaves pre-mRNA at proximal 3'UTR PAS\"\nis_a: GO:0004518 ! nuclease activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004519"
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
  "source_locator": "lines 433250-433261",
  "excerpt": "[Term]\nid: GO:0120136\nname: dUMP kinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: ATP + dUMP = ADP + dUDP.\" [PMID:3010881, RHEA:30655]\nsynonym: \"ATP:dUMP phosphotransferase activity\" EXACT []\nsynonym: \"deoxyuridine monophosphate kinase activity\" EXACT []\nsynonym: \"dUMP-kinase activity\" EXACT []\nxref: RHEA:30655\nis_a: GO:0047507 ! deoxynucleoside phosphate kinase activity, ATP as phosphate donor\nproperty_value: skos:exactMatch RHEA:30655\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0120136"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
