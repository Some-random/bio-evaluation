# cofactor_0170: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0170.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **A** — Zn(2+)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | no saved label | no saved label | output error (invalid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MISKSIILRFSELSMRKKATLVGLPLLAVAAISSSLNSPTRQQRIELSLPESPLVQFSSAEHTVEVVKVGHPDYEYEIKPGDNLSTIFNQLGFAYTELMKVMETDLNYLALDTLRPGNVLRFWKGSDNTLAKMELEFSLVDRAVYTRLNDGSYEFEERKIPGTWKVEPLIGEVDGSFSLSANRAGLGAADVDQIVTLLKDKINFGRDLRRGDRFEVVLSRQLVGEKLTGNSEIQAIKIFNRGKEITAYLHQDGQYYDKNGDSLQRAFQRYPVDSKWRISSNFDPRRLHPVTKRVAPHNGTDFAMPIGTPVYTSGDGVVVMTRNHPYAGNYVVIQHGNTYMTRYLHLSKILVKKGQKVSRGQRIGLSGNTGRVTGPHLHYELIVRGRPVNAMKANIPMASSVPKKEMAQFIAKRKELDQMLARQESMLAAQ

[Multiple Choices]
A. Zn(2+)
B. pantetheine 4'-phosphate
C. FAD
D. Mo-bis(molybdopterin guanine dinucleotide)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

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
```

</details>

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the annotated ShyA protein. UniProt records Zn(2+) as its cofactor, one ion per subunit, with experimental evidence attribution; the cited structural study reports a crystal structure in complex with Zn(2+).

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has several histidine- and acidic-residue-containing regions, which could be consistent with metal binding, but the supplied input does not establish the protein's function or identify a specific metal-binding active site well enough to determine the required cofactor.


**Missing item-specific fact**

> That this sequence is ShyA, a zinc-dependent peptidoglycan endopeptidase; the reported one-Zn-per-subunit cofactor assignment is an item-specific annotation supported by cited experimental evidence.


**Reason**

> Selecting Zn depends on protein-specific functional or cofactor information absent from the question. Generic sequence heuristics do not distinguish a required Zn cofactor from the listed alternatives with adequate support.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation explicitly assigns Zn(2+); no supplied evidence supports another listed cofactor.


### Important caveats

- The cofactor annotation and cited structural evidence are reviewer-only and were not supplied to the evaluated model.
- The current and checked historical UniProt records match the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several histidine- and acidic-residue-containing regions, which could be consistent with metal binding, but the supplied input does not establish the protein's function or identify a specific metal-binding active site well enough to determine the required cofactor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence is ShyA, a zinc-dependent peptidoglycan endopeptidase; the reported one-Zn-per-subunit cofactor assignment is an item-specific annotation supported by cited experimental evidence.",
    "reason": "Selecting Zn depends on protein-specific functional or cofactor information absent from the question. Generic sequence heuristics do not distinguish a required Zn cofactor from the listed alternatives with adequate support."
  },
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated ShyA protein. UniProt records Zn(2+) as its cofactor, one ion per subunit, with experimental evidence attribution; the cited structural study reports a crystal structure in complex with Zn(2+)."
  },
  "important_caveats": [
    "The cofactor annotation and cited structural evidence are reviewer-only and were not supplied to the evaluated model.",
    "The current and checked historical UniProt records match the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation explicitly assigns Zn(2+); no supplied evidence supports another listed cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated ShyA protein. UniProt records Zn(2+) as its cofactor, one ion per subunit, with experimental evidence attribution; the cited structural study reports a crystal structure in complex with Zn(2+).",
    "evidence_ids": ["C5", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has several histidine- and acidic-residue-containing regions, which could be consistent with metal binding, but the supplied input does not establish the protein's function or identify a specific metal-binding active site well enough to determine the required cofactor.",
    "missing_item_specific_fact": "That this sequence is ShyA, a zinc-dependent peptidoglycan endopeptidase; the reported one-Zn-per-subunit cofactor assignment is an item-specific annotation supported by cited experimental evidence.",
    "reason": "Selecting Zn depends on protein-specific functional or cofactor information absent from the question. Generic sequence heuristics do not distinguish a required Zn cofactor from the listed alternatives with adequate support."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation explicitly assigns Zn(2+); no supplied evidence supports another listed cofactor."
  },
  "important_caveats": [
    "The cofactor annotation and cited structural evidence are reviewer-only and were not supplied to the evaluated model.",
    "The current and checked historical UniProt records match the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9KN86 (ShyA, Vibrio cholerae) explicitly annotates Zn(2+) as the cofactor (ECO:0000269|PubMed:32393643, 'Binds 1 zinc ion per subunit'). The alternative name 'Zn-metalloprotease' and EC 3.4.24.- (metalloprotease class) confirm this. X-ray crystallography at 2.08 Å (PDB 6U2A, 6UE4) shows the protein in complex with Zn(2+). The sequence matches the benchmark input exactly (SHA-256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple H-x-H motifs (e.g., 'HPYAGNYVVIQHGNTY', 'HLHYELIVRGRPVNAMKANIPMASSVPKKEMAQFIAKRKELDQMLARQESMLAAQ') consistent with zinc-coordinating metalloprotease active sites. The protein has a signal peptide indicating a periplasmic/extracellular peptidase. Critically, the three distractors are organic cofactors tied to entirely different enzyme classes: FAD requires Rossmann-fold motifs (GxGxxG, absent here), Mo-bis(molybdopterin guanine dinucleotide) requires molybdenum enzyme motifs (absent), and pantetheine 4'-phosphate is for acyl-carrier/acyltransferase systems (no such motifs present). By elimination of organic-cofactor enzyme classes and positive identification of His-rich metal-binding patterns, Zn(2+) is the only biochemically consistent choice for a peptidoglycan-degrading endopeptidase.


**Missing item-specific fact**

> Precise recognition of the M23 peptidase family fold would strengthen the argument, but is not strictly required given the strong elimination of all three organic-cofactor options and the visible His-rich coordination motifs.


**Reason**

> A model with general biological knowledge can (a) note the absence of any flavin, molybdopterin, or acyl-carrier binding motifs, eliminating B, C, and D; (b) observe HxxH-type patterns suggestive of a zinc metalloprotease active site; and (c) infer that a peptidoglycan-degrading endopeptidase (EC 3.4.24.-) uses Zn(2+). This constitutes a concrete biological argument rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three non-metal distractors are associated with mechanistically distinct enzyme classes (oxidoreductases, molybdoenzymes, acyltransferases) that are clearly inconsistent with the sequence architecture and His-rich motifs. Only Zn(2+) is compatible with a metalloprotease.


### Important caveats

- The M23 peptidase family assignment from raw sequence is non-trivial; a model relying solely on motif scanning might struggle to positively identify the family, though elimination of the three organic-cofactor choices is straightforward.
- The UniProt COFACTOR annotation carries evidence code ECO:0000269 (experimental, from PubMed:32393643 / PDB structures), so the key is experimentally grounded, not merely computational.
- The entry was first publicly released in April 2025; depending on the benchmark construction date, the annotation may or may not have been available to the author at question-creation time, though the sequence itself has been in databases since 2000.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple H-x-H motifs (e.g., 'HPYAGNYVVIQHGNTY', 'HLHYELIVRGRPVNAMKANIPMASSVPKKEMAQFIAKRKELDQMLARQESMLAAQ') consistent with zinc-coordinating metalloprotease active sites. The protein has a signal peptide indicating a periplasmic/extracellular peptidase. Critically, the three distractors are organic cofactors tied to entirely different enzyme classes: FAD requires Rossmann-fold motifs (GxGxxG, absent here), Mo-bis(molybdopterin guanine dinucleotide) requires molybdenum enzyme motifs (absent), and pantetheine 4'-phosphate is for acyl-carrier/acyltransferase systems (no such motifs present). By elimination of organic-cofactor enzyme classes and positive identification of His-rich metal-binding patterns, Zn(2+) is the only biochemically consistent choice for a peptidoglycan-degrading endopeptidase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of the M23 peptidase family fold would strengthen the argument, but is not strictly required given the strong elimination of all three organic-cofactor options and the visible His-rich coordination motifs.",
    "reason": "A model with general biological knowledge can (a) note the absence of any flavin, molybdopterin, or acyl-carrier binding motifs, eliminating B, C, and D; (b) observe HxxH-type patterns suggestive of a zinc metalloprotease active site; and (c) infer that a peptidoglycan-degrading endopeptidase (EC 3.4.24.-) uses Zn(2+). This constitutes a concrete biological argument rather than pure lookup."
  },
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9KN86 (ShyA, Vibrio cholerae) explicitly annotates Zn(2+) as the cofactor (ECO:0000269|PubMed:32393643, 'Binds 1 zinc ion per subunit'). The alternative name 'Zn-metalloprotease' and EC 3.4.24.- (metalloprotease class) confirm this. X-ray crystallography at 2.08 Å (PDB 6U2A, 6UE4) shows the protein in complex with Zn(2+). The sequence matches the benchmark input exactly (SHA-256 identical)."
  },
  "important_caveats": [
    "The M23 peptidase family assignment from raw sequence is non-trivial; a model relying solely on motif scanning might struggle to positively identify the family, though elimination of the three organic-cofactor choices is straightforward.",
    "The UniProt COFACTOR annotation carries evidence code ECO:0000269 (experimental, from PubMed:32393643 / PDB structures), so the key is experimentally grounded, not merely computational.",
    "The entry was first publicly released in April 2025; depending on the benchmark construction date, the annotation may or may not have been available to the author at question-creation time, though the sequence itself has been in databases since 2000."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three non-metal distractors are associated with mechanistically distinct enzyme classes (oxidoreductases, molybdoenzymes, acyltransferases) that are clearly inconsistent with the sequence architecture and His-rich motifs. Only Zn(2+) is compatible with a metalloprotease."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9KN86 (ShyA, Vibrio cholerae) explicitly annotates Zn(2+) as the cofactor (ECO:0000269|PubMed:32393643, 'Binds 1 zinc ion per subunit'). The alternative name 'Zn-metalloprotease' and EC 3.4.24.- (metalloprotease class) confirm this. X-ray crystallography at 2.08 Å (PDB 6U2A, 6UE4) shows the protein in complex with Zn(2+). The sequence matches the benchmark input exactly (SHA-256 identical).",
    "evidence_ids": ["C4", "C5", "C8", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple H-x-H motifs (e.g., 'HPYAGNYVVIQHGNTY', 'HLHYELIVRGRPVNAMKANIPMASSVPKKEMAQFIAKRKELDQMLARQESMLAAQ') consistent with zinc-coordinating metalloprotease active sites. The protein has a signal peptide indicating a periplasmic/extracellular peptidase. Critically, the three distractors are organic cofactors tied to entirely different enzyme classes: FAD requires Rossmann-fold motifs (GxGxxG, absent here), Mo-bis(molybdopterin guanine dinucleotide) requires molybdenum enzyme motifs (absent), and pantetheine 4'-phosphate is for acyl-carrier/acyltransferase systems (no such motifs present). By elimination of organic-cofactor enzyme classes and positive identification of His-rich metal-binding patterns, Zn(2+) is the only biochemically consistent choice for a peptidoglycan-degrading endopeptidase.",
    "missing_item_specific_fact": "Precise recognition of the M23 peptidase family fold would strengthen the argument, but is not strictly required given the strong elimination of all three organic-cofactor options and the visible His-rich coordination motifs.",
    "reason": "A model with general biological knowledge can (a) note the absence of any flavin, molybdopterin, or acyl-carrier binding motifs, eliminating B, C, and D; (b) observe HxxH-type patterns suggestive of a zinc metalloprotease active site; and (c) infer that a peptidoglycan-degrading endopeptidase (EC 3.4.24.-) uses Zn(2+). This constitutes a concrete biological argument rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three non-metal distractors are associated with mechanistically distinct enzyme classes (oxidoreductases, molybdoenzymes, acyltransferases) that are clearly inconsistent with the sequence architecture and His-rich motifs. Only Zn(2+) is compatible with a metalloprotease."
  },
  "important_caveats": [
    "The M23 peptidase family assignment from raw sequence is non-trivial; a model relying solely on motif scanning might struggle to positively identify the family, though elimination of the three organic-cofactor choices is straightforward.",
    "The UniProt COFACTOR annotation carries evidence code ECO:0000269 (experimental, from PubMed:32393643 / PDB structures), so the key is experimentally grounded, not merely computational.",
    "The entry was first publicly released in April 2025; depending on the benchmark construction date, the annotation may or may not have been available to the author at question-creation time, though the sequence itself has been in databases since 2000."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1140)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates Zn(2+) as a cofactor and says that each subunit binds one zinc ion, with experimental evidence code ECO:0000269. This supports the keyed choice.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal export signal and an enzyme-like region with histidine/aspartate-rich motifs, a pattern consistent with an exported metallopeptidase. Transferable knowledge of zinc-dependent peptidases makes Zn(2+) a credible choice; the alternatives are less consistent with this sequence, which lacks an obvious flavoprotein or molybdenum-enzyme signature.",
    "missing_item_specific_fact": "",
    "reason": "A family-level metallopeptidase inference from the sequence can meaningfully distinguish zinc from the other offered cofactors, even without knowing the exact protein's annotation. The inference is probabilistic, not a direct demonstration of metal binding from sequence alone.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered cofactor is comparably supported by the sequence-level metallopeptidase inference."
  },
  "important_caveats": [
    "The source annotation reports zinc binding; binding alone is not a complete demonstration that zinc is essential for catalysis. The experimental cofactor annotation supports the key, but the underlying study was not independently reviewed here."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q9KN86) annotates this protein as Peptidoglycan DD-endopeptidase ShyA (EC 3.4.24.-), a metalloendopeptidase. The cofactor is explicitly annotated as Zn(2+) with experimental evidence (ECO:0000269|PubMed:32393643), confirmed by X-ray crystallography (PDB 6U2A, 6UE4) showing the protein in complex with Zn(2+). The entry also lists 'Zn-metalloprotease' as an alternative name. The answer A (Zn(2+)) is directly supported by structural and biochemical evidence.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish Zn(2+) from the other three options through multiple transferable lines of reasoning: (1) The sequence contains a hydrophobic N-terminal signal peptide (GLPLLAVAAISSS) indicating periplasmic/extracellular localization, and the overall domain architecture with clustered histidines in the C-terminal region (e.g., HPYAG...QHG...PHLHY) is consistent with a metalloprotease active site. (2) Peptidases/proteases overwhelmingly use metal-ion cofactors, most commonly Zn(2+), whereas FAD is a cofactor for oxidoreductases, Mo-bis-MGD is specific to certain anaerobic oxidoreductases (nitrate reductase, DMSO reductase), and pantetheine 4'-phosphate is a prosthetic group for acyl carrier proteins or phosphopantetheinyl transferases. None of these three alternative cofactors are ever used by peptidases. (3) The sequence lacks Rossmann-fold motifs (GxGxxG) for FAD binding, lacks the distinctive molybdopterin-binding fold, and lacks the ACP-like short helical bundle for pantetheine attachment. (4) The presence of multiple histidines in spatial proximity in the C-terminal catalytic domain is a hallmark of zinc coordination in metalloproteases (M23, M48, and related families). Together, these features allow a model to confidently select Zn(2+) while eliminating the other three options as belonging to entirely different enzyme classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The four answer choices belong to four distinct enzyme classes (metalloprotease, acyl-transfer, flavoprotein oxidoreductase, molybdoenzyme). Recognizing the sequence as a peptidase/protease and noting the absence of FAD-binding, molybdopterin-binding, or pantetheine-attachment motifs allows elimination of B, C, and D. The clustered histidines further support zinc coordination. This is standard family-level and class-level biological reasoning transferable from knowledge of other metalloproteases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options correspond to four mutually exclusive enzyme classes. A peptidase sequence cannot plausibly use FAD, Mo-bis-MGD, or pantetheine 4'-phosphate as its catalytic cofactor. No ambiguity exists among the choices.


### Important caveats

- The reviewer evidence confirms the protein is ShyA (Q9KN86) from Vibrio cholerae, but this identity was not provided to the evaluated model. The reasoning relies solely on sequence features and general enzyme-class knowledge.
- The EC 3.4.24.- designation (metalloendopeptidase) is assigned in the UniProt entry with experimental evidence, but the model must infer the protease class from sequence features rather than from a provided annotation.
- The exact zinc-binding residues (His-376, His-378) were confirmed by mutagenesis and crystallography; a model identifying histidine clusters in the C-terminal region is making a reasonable structural inference consistent with known metalloprotease families.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish Zn(2+) from the other three options through multiple transferable lines of reasoning: (1) The sequence contains a hydrophobic N-terminal signal peptide (GLPLLAVAAISSS) indicating periplasmic/extracellular localization, and the overall domain architecture with clustered histidines in the C-terminal region (e.g., HPYAG...QHG...PHLHY) is consistent with a metalloprotease active site. (2) Peptidases/proteases overwhelmingly use metal-ion cofactors, most commonly Zn(2+), whereas FAD is a cofactor for oxidoreductases, Mo-bis-MGD is specific to certain anaerobic oxidoreductases (nitrate reductase, DMSO reductase), and pantetheine 4'-phosphate is a prosthetic group for acyl carrier proteins or phosphopantetheinyl transferases. None of these three alternative cofactors are ever used by peptidases. (3) The sequence lacks Rossmann-fold motifs (GxGxxG) for FAD binding, lacks the distinctive molybdopterin-binding fold, and lacks the ACP-like short helical bundle for pantetheine attachment. (4) The presence of multiple histidines in spatial proximity in the C-terminal catalytic domain is a hallmark of zinc coordination in metalloproteases (M23, M48, and related families). Together, these features allow a model to confidently select Zn(2+) while eliminating the other three options as belonging to entirely different enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The four answer choices belong to four distinct enzyme classes (metalloprotease, acyl-transfer, flavoprotein oxidoreductase, molybdoenzyme). Recognizing the sequence as a peptidase/protease and noting the absence of FAD-binding, molybdopterin-binding, or pantetheine-attachment motifs allows elimination of B, C, and D. The clustered histidines further support zinc coordination. This is standard family-level and class-level biological reasoning transferable from knowledge of other metalloproteases."
  },
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q9KN86) annotates this protein as Peptidoglycan DD-endopeptidase ShyA (EC 3.4.24.-), a metalloendopeptidase. The cofactor is explicitly annotated as Zn(2+) with experimental evidence (ECO:0000269|PubMed:32393643), confirmed by X-ray crystallography (PDB 6U2A, 6UE4) showing the protein in complex with Zn(2+). The entry also lists 'Zn-metalloprotease' as an alternative name. The answer A (Zn(2+)) is directly supported by structural and biochemical evidence."
  },
  "important_caveats": [
    "The reviewer evidence confirms the protein is ShyA (Q9KN86) from Vibrio cholerae, but this identity was not provided to the evaluated model. The reasoning relies solely on sequence features and general enzyme-class knowledge.",
    "The EC 3.4.24.- designation (metalloendopeptidase) is assigned in the UniProt entry with experimental evidence, but the model must infer the protease class from sequence features rather than from a provided annotation.",
    "The exact zinc-binding residues (His-376, His-378) were confirmed by mutagenesis and crystallography; a model identifying histidine clusters in the C-terminal region is making a reasonable structural inference consistent with known metalloprotease families."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options correspond to four mutually exclusive enzyme classes. A peptidase sequence cannot plausibly use FAD, Mo-bis-MGD, or pantetheine 4'-phosphate as its catalytic cofactor. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q9KN86) annotates this protein as Peptidoglycan DD-endopeptidase ShyA (EC 3.4.24.-), a metalloendopeptidase. The cofactor is explicitly annotated as Zn(2+) with experimental evidence (ECO:0000269|PubMed:32393643), confirmed by X-ray crystallography (PDB 6U2A, 6UE4) showing the protein in complex with Zn(2+). The entry also lists 'Zn-metalloprotease' as an alternative name. The answer A (Zn(2+)) is directly supported by structural and biochemical evidence.",
    "evidence_ids": ["C5", "C8", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish Zn(2+) from the other three options through multiple transferable lines of reasoning: (1) The sequence contains a hydrophobic N-terminal signal peptide (GLPLLAVAAISSS) indicating periplasmic/extracellular localization, and the overall domain architecture with clustered histidines in the C-terminal region (e.g., HPYAG...QHG...PHLHY) is consistent with a metalloprotease active site. (2) Peptidases/proteases overwhelmingly use metal-ion cofactors, most commonly Zn(2+), whereas FAD is a cofactor for oxidoreductases, Mo-bis-MGD is specific to certain anaerobic oxidoreductases (nitrate reductase, DMSO reductase), and pantetheine 4'-phosphate is a prosthetic group for acyl carrier proteins or phosphopantetheinyl transferases. None of these three alternative cofactors are ever used by peptidases. (3) The sequence lacks Rossmann-fold motifs (GxGxxG) for FAD binding, lacks the distinctive molybdopterin-binding fold, and lacks the ACP-like short helical bundle for pantetheine attachment. (4) The presence of multiple histidines in spatial proximity in the C-terminal catalytic domain is a hallmark of zinc coordination in metalloproteases (M23, M48, and related families). Together, these features allow a model to confidently select Zn(2+) while eliminating the other three options as belonging to entirely different enzyme classes.",
    "missing_item_specific_fact": "",
    "reason": "The four answer choices belong to four distinct enzyme classes (metalloprotease, acyl-transfer, flavoprotein oxidoreductase, molybdoenzyme). Recognizing the sequence as a peptidase/protease and noting the absence of FAD-binding, molybdopterin-binding, or pantetheine-attachment motifs allows elimination of B, C, and D. The clustered histidines further support zinc coordination. This is standard family-level and class-level biological reasoning transferable from knowledge of other metalloproteases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options correspond to four mutually exclusive enzyme classes. A peptidase sequence cannot plausibly use FAD, Mo-bis-MGD, or pantetheine 4'-phosphate as its catalytic cofactor. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The reviewer evidence confirms the protein is ShyA (Q9KN86) from Vibrio cholerae, but this identity was not provided to the evaluated model. The reasoning relies solely on sequence features and general enzyme-class knowledge.",
    "The EC 3.4.24.- designation (metalloendopeptidase) is assigned in the UniProt entry with experimental evidence, but the model must infer the protease class from sequence features rather than from a provided annotation.",
    "The exact zinc-binding residues (His-376, His-378) were confirmed by mutagenesis and crystallography; a model identifying histidine clusters in the C-terminal region is making a reasonable structural inference consistent with known metalloprotease families."
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
  "requested_accession": "Q9KN86",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "0520ed638d8cdb09bee8796cafa9092296b04e973c78b3a4073bed6df5a3e163",
  "benchmark_sequence_length": 430,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 112,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "current_source_sequence_sha256": "0520ed638d8cdb09bee8796cafa9092296b04e973c78b3a4073bed6df5a3e163",
  "current_source_sequence_length": 430,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 110,
  "selected_historical_version": {
    "accession": "Q9KN86",
    "database": "Swiss-Prot",
    "entryVersion": 110,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SHYA_VIBCH",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "selected_historical_source_sequence_sha256": "0520ed638d8cdb09bee8796cafa9092296b04e973c78b3a4073bed6df5a3e163",
  "selected_historical_source_sequence_length": 430,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 110,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9KN86\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":112,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF95993.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000584\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Vibrionales\",\"Vibrionaceae\",\"Vibrio\"],\"scientificName\":\"Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961)\",\"taxonId\":243277}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"Autolysin ShyA\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"Major peptidoglycan endopeptidase ShyA\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"Major PG EP ShyA\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"value\":\"Sidewall hydrolase A\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"value\":\"Zn-metalloprotease\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23834664\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30782657\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Peptidoglycan DD-endopeptidase ShyA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 zinc ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Doerr T.\",\"Cava F.\",\"Lam H.\",\"Davis B.M.\",\"Waldor M.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23834664\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.12323\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"23834664\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"962\",\"publicationDate\":\"2013\",\"title\":\"Substrate specificity of an elongation-specific peptidoglycan endopeptidase and its implications for cell wall architecture and growth of Vibrio cholerae.\",\"volume\":\"89\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-378\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Murphy S.G.\",\"Alvarez L.\",\"Adams M.C.\",\"Liu S.\",\"Chappie J.S.\",\"Cava F.\",\"Doerr T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30782657\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.02620-18\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30782657\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc Starvation Response.\",\"volume\":\"10\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Shin J.H.\",\"Sulpizio A.G.\",\"Kelley A.\",\"Alvarez L.\",\"Murphy S.G.\",\"Fan L.\",\"Cava F.\",\"Mao Y.\",\"Saper M.A.\",\"Dorr T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32393643\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.2001661117\"}],\"citationType\":\"journal article\",\"firstPage\":\"11692\",\"id\":\"32393643\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"11702\",\"publicationDate\":\"2020\",\"title\":\"Structural basis of peptidoglycan endopeptidase regulation.\",\"volume\":\"117\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6U2A\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6UE4\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.08 ANGSTROMS) OF 36-430 IN COMPLEX WITH ZN(2+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"SUBCELLULAR LOCATION\",\"DOMAIN\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF 1-MET--ARG-265; 1-MET--ILE-160; 1-MET--VAL-66; GLU-103; LEU-109; ASP-112; ARG-286; HIS-297; ASP-301; LEU-344; HIS-345; HIS-376; HIS-378 AND 427-LEU--GLN-430\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "source_locator": "lines 1-20",
  "excerpt": "ID   SHYA_VIBCH              Reviewed;         430 AA.\nAC   Q9KN86;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 110.\nDE   RecName: Full=Peptidoglycan DD-endopeptidase ShyA {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:23834664, ECO:0000269|PubMed:30782657, ECO:0000269|PubMed:32393643};\nDE   AltName: Full=Autolysin ShyA {ECO:0000303|PubMed:32393643};\nDE   AltName: Full=Major peptidoglycan endopeptidase ShyA {ECO:0000303|PubMed:32393643};\nDE            Short=Major PG EP ShyA {ECO:0000303|PubMed:32393643};\nDE   AltName: Full=Sidewall hydrolase A {ECO:0000303|PubMed:23834664};\nDE   AltName: Full=Zn-metalloprotease {ECO:0000303|PubMed:23834664};\nDE   Flags: Precursor;\nGN   Name=shyA {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nGN   OrderedLocusNames=VC_A0079 {ECO:0000303|PubMed:23834664,\nGN   ECO:0000312|EMBL:AAF95993.1};\nOS   Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Vibrionales;\nOC   Vibrionaceae; Vibrio.\nOX   NCBI_TaxID=243277 {ECO:0000312|EMBL:AAF95993.1, ECO:0000312|Proteomes:UP000000584};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "source_locator": "lines 6-13",
  "excerpt": "DE   RecName: Full=Peptidoglycan DD-endopeptidase ShyA {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:23834664, ECO:0000269|PubMed:30782657, ECO:0000269|PubMed:32393643};\nDE   AltName: Full=Autolysin ShyA {ECO:0000303|PubMed:32393643};\nDE   AltName: Full=Major peptidoglycan endopeptidase ShyA {ECO:0000303|PubMed:32393643};\nDE            Short=Major PG EP ShyA {ECO:0000303|PubMed:32393643};\nDE   AltName: Full=Sidewall hydrolase A {ECO:0000303|PubMed:23834664};\nDE   AltName: Full=Zn-metalloprotease {ECO:0000303|PubMed:23834664};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "source_locator": "lines 35-45",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBCELLULAR LOCATION, DISRUPTION\nRP   PHENOTYPE, AND MUTAGENESIS OF HIS-378.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:23834664};\nRX   PubMed=23834664; DOI=10.1111/mmi.12323;\nRA   Doerr T., Cava F., Lam H., Davis B.M., Waldor M.K.;\nRT   \"Substrate specificity of an elongation-specific peptidoglycan\nRT   endopeptidase and its implications for cell wall architecture and growth of\nRT   Vibrio cholerae.\";\nRL   Mol. Microbiol. 89:949-962(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "source_locator": "lines 46-55",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:30782657};\nRX   PubMed=30782657; DOI=10.1128/mbio.02620-18;\nRA   Murphy S.G., Alvarez L., Adams M.C., Liu S., Chappie J.S., Cava F.,\nRA   Doerr T.;\nRT   \"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc\nRT   Starvation Response.\";\nRL   MBio 10:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "source_locator": "lines 56-68",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6U2A, ECO:0007744|PDB:6UE4}\nRP   X-RAY CRYSTALLOGRAPHY (2.08 ANGSTROMS) OF 36-430 IN COMPLEX WITH ZN(2+),\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, PATHWAY,\nRP   SUBCELLULAR LOCATION, DOMAIN, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF\nRP   1-MET--ARG-265; 1-MET--ILE-160; 1-MET--VAL-66; GLU-103; LEU-109; ASP-112;\nRP   ARG-286; HIS-297; ASP-301; LEU-344; HIS-345; HIS-376; HIS-378 AND\nRP   427-LEU--GLN-430.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:32393643};\nRX   PubMed=32393643; DOI=10.1073/pnas.2001661117;\nRA   Shin J.H., Sulpizio A.G., Kelley A., Alvarez L., Murphy S.G., Fan L.,\nRA   Cava F., Mao Y., Saper M.A., Dorr T.;\nRT   \"Structural basis of peptidoglycan endopeptidase regulation.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 117:11692-11702(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "source_locator": "lines 87-90",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000269|PubMed:32393643};\nCC       Note=Binds 1 zinc ion per subunit. {ECO:0000269|PubMed:32393643};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
