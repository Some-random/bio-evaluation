# EC_number_0064: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0064.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **D** — 1.2.1.11

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
MASYPKKKCGVLGATGSVGQRFILLLADHPFLELHAIGASNRSAGKKYKDAVRWKQTTAMSERLSNLVLRDCRADQFSDCDLVFSGLNSDVAGEIEMEFIKAEIPVFSNAKNYRKHPLVPLVVPTVNPQHLDLIPHQRKEFGLKKGFLVCNSNCAVIGVVIPFAALQAKFGPVEEVEVFTEQAVSGAGYPGVPSMDIMDNVIPYISGEEDKLENEAQKILGSLNADATAFDEQKGLTVGATCTRVGVTDGHMAFVSLRFKNRPGPSAEEVKQAMREYQSEAQKLGCPSAPREAIKVFDEPDRPQPRLDRDISKGYTVSVGRVREAAPGSYFDLRFAALSHNTVIGAAGSSILNAEVAVIKGYI

[Multiple Choices]
A. 1.2.1.46
B. 1.1.1.195
C. 2.7.1.39
D. 1.2.1.11
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry for an Aspergillus fumigatus aspartate-semialdehyde dehydrogenase. UniProt assigns EC 1.2.1.11 and cites experimental evidence for both the enzyme annotation and its catalytic reaction. This supports choice D, while the database evidence is reviewer-only and was not available to the evaluated model.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit enzyme-family inference, but the input provides no organism, pathway, substrate, or reaction context that establishes the specific catalytic activity and complete EC number.


**Missing item-specific fact**

> The protein-specific assignment to aspartate-semialdehyde dehydrogenase and its reaction corresponding to EC 1.2.1.11.


**Reason**

> Choosing among these complete EC numbers requires identifying the particular enzyme activity, a fact not stated in the input. Recognizing the sequence or using a predictor would rely on protein-specific identification rather than a biological argument supplied by the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited sequence-matched annotation supports D; the evidence provided does not support another listed option.


### Important caveats

- The annotation cites experimental evidence, but the primary papers were not independently retrieved or validated here.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may permit enzyme-family inference, but the input provides no organism, pathway, substrate, or reaction context that establishes the specific catalytic activity and complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment to aspartate-semialdehyde dehydrogenase and its reaction corresponding to EC 1.2.1.11.",
    "reason": "Choosing among these complete EC numbers requires identifying the particular enzyme activity, a fact not stated in the input. Recognizing the sequence or using a predictor would rely on protein-specific identification rather than a biological argument supplied by the question."
  },
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for an Aspergillus fumigatus aspartate-semialdehyde dehydrogenase. UniProt assigns EC 1.2.1.11 and cites experimental evidence for both the enzyme annotation and its catalytic reaction. This supports choice D, while the database evidence is reviewer-only and was not available to the evaluated model."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the primary papers were not independently retrieved or validated here.",
    "The exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited sequence-matched annotation supports D; the evidence provided does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for an Aspergillus fumigatus aspartate-semialdehyde dehydrogenase. UniProt assigns EC 1.2.1.11 and cites experimental evidence for both the enzyme annotation and its catalytic reaction. This supports choice D, while the database evidence is reviewer-only and was not available to the evaluated model.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit enzyme-family inference, but the input provides no organism, pathway, substrate, or reaction context that establishes the specific catalytic activity and complete EC number.",
    "missing_item_specific_fact": "The protein-specific assignment to aspartate-semialdehyde dehydrogenase and its reaction corresponding to EC 1.2.1.11.",
    "reason": "Choosing among these complete EC numbers requires identifying the particular enzyme activity, a fact not stated in the input. Recognizing the sequence or using a predictor would rely on protein-specific identification rather than a biological argument supplied by the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited sequence-matched annotation supports D; the evidence provided does not support another listed option."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the primary papers were not independently retrieved or validated here.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WWR8 (sequence exactly matched, 363 aa) is annotated as Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, with experimental evidence (ECO:0000269) from PubMed:28045392 (X-ray crystallography, PDB 5JW6) and PubMed:29608391 (enzymatic assay). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is experimentally confirmed. Both current and archived (entry v118) records agree.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three reasoning steps distinguish the answer: (1) The N-terminal Rossmann-fold motif 'GVLGATGSVGQ' (GxGxxG) identifies the protein as an NAD(P)-binding oxidoreductase, eliminating choice C (EC 2.7.1.39, a phosphotransferase). (2) The catalytic cysteine pair 'CNSNCA' (Cys-Asn-Ser-Asn-Cys) embedded in the sequence 'FLVCNSNCAVIG' is the hallmark catalytic dyad of aldehyde dehydrogenases, indicating an aldehyde/oxo-group substrate (EC 1.2.1.x), which eliminates choice B (EC 1.1.1.195, acting on CH-OH group). (3) The specific CNSNCA catalytic arrangement is a well-documented active-site signature unique to aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) within the EC 1.2.1.x class; other EC 1.2.1.x enzymes (e.g., EC 1.2.1.46) employ different catalytic residue arrangements. Together, these sequence features support choosing D over A.


**Missing item-specific fact**

> None strictly missing. The CNSNCA motif recognition is specialized but constitutes well-established catalytic-mechanism biochemistry rather than an opaque database annotation.


**Reason**

> The sequence contains identifiable structural and catalytic motifs (Rossmann fold, catalytic Cys dyad CNSNCA) that allow a knowledgeable biochemist to narrow from four EC numbers to the correct one through general enzyme-mechanism reasoning, without needing to recall the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different EC top-level classes (1.1.1.x, 1.2.1.x, 2.7.1.x), and within EC 1.2.1.x the CNSNCA motif is specific to ASADH. No other option is defensible given the sequence features.


### Important caveats

- The CNSNCA catalytic-motif recognition is specialized biochemistry; a model without training on ASADH active-site architecture may struggle to distinguish D from A (both EC 1.2.1.x).
- The reviewer evidence is experimental (X-ray crystallography and enzymatic assays), strengthening the annotation, but this evidence was not available to the evaluated model.
- The exact identity of EC 1.2.1.46 (choice A) was not independently verified here; however, the CNSNCA motif is not a general feature of all EC 1.2.1.x enzymes, supporting the discrimination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three reasoning steps distinguish the answer: (1) The N-terminal Rossmann-fold motif 'GVLGATGSVGQ' (GxGxxG) identifies the protein as an NAD(P)-binding oxidoreductase, eliminating choice C (EC 2.7.1.39, a phosphotransferase). (2) The catalytic cysteine pair 'CNSNCA' (Cys-Asn-Ser-Asn-Cys) embedded in the sequence 'FLVCNSNCAVIG' is the hallmark catalytic dyad of aldehyde dehydrogenases, indicating an aldehyde/oxo-group substrate (EC 1.2.1.x), which eliminates choice B (EC 1.1.1.195, acting on CH-OH group). (3) The specific CNSNCA catalytic arrangement is a well-documented active-site signature unique to aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) within the EC 1.2.1.x class; other EC 1.2.1.x enzymes (e.g., EC 1.2.1.46) employ different catalytic residue arrangements. Together, these sequence features support choosing D over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly missing. The CNSNCA motif recognition is specialized but constitutes well-established catalytic-mechanism biochemistry rather than an opaque database annotation.",
    "reason": "The sequence contains identifiable structural and catalytic motifs (Rossmann fold, catalytic Cys dyad CNSNCA) that allow a knowledgeable biochemist to narrow from four EC numbers to the correct one through general enzyme-mechanism reasoning, without needing to recall the specific UniProt entry."
  },
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WWR8 (sequence exactly matched, 363 aa) is annotated as Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, with experimental evidence (ECO:0000269) from PubMed:28045392 (X-ray crystallography, PDB 5JW6) and PubMed:29608391 (enzymatic assay). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is experimentally confirmed. Both current and archived (entry v118) records agree."
  },
  "important_caveats": [
    "The CNSNCA catalytic-motif recognition is specialized biochemistry; a model without training on ASADH active-site architecture may struggle to distinguish D from A (both EC 1.2.1.x).",
    "The reviewer evidence is experimental (X-ray crystallography and enzymatic assays), strengthening the annotation, but this evidence was not available to the evaluated model.",
    "The exact identity of EC 1.2.1.46 (choice A) was not independently verified here; however, the CNSNCA motif is not a general feature of all EC 1.2.1.x enzymes, supporting the discrimination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC top-level classes (1.1.1.x, 1.2.1.x, 2.7.1.x), and within EC 1.2.1.x the CNSNCA motif is specific to ASADH. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WWR8 (sequence exactly matched, 363 aa) is annotated as Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, with experimental evidence (ECO:0000269) from PubMed:28045392 (X-ray crystallography, PDB 5JW6) and PubMed:29608391 (enzymatic assay). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is experimentally confirmed. Both current and archived (entry v118) records agree.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three reasoning steps distinguish the answer: (1) The N-terminal Rossmann-fold motif 'GVLGATGSVGQ' (GxGxxG) identifies the protein as an NAD(P)-binding oxidoreductase, eliminating choice C (EC 2.7.1.39, a phosphotransferase). (2) The catalytic cysteine pair 'CNSNCA' (Cys-Asn-Ser-Asn-Cys) embedded in the sequence 'FLVCNSNCAVIG' is the hallmark catalytic dyad of aldehyde dehydrogenases, indicating an aldehyde/oxo-group substrate (EC 1.2.1.x), which eliminates choice B (EC 1.1.1.195, acting on CH-OH group). (3) The specific CNSNCA catalytic arrangement is a well-documented active-site signature unique to aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) within the EC 1.2.1.x class; other EC 1.2.1.x enzymes (e.g., EC 1.2.1.46) employ different catalytic residue arrangements. Together, these sequence features support choosing D over A.",
    "missing_item_specific_fact": "None strictly missing. The CNSNCA motif recognition is specialized but constitutes well-established catalytic-mechanism biochemistry rather than an opaque database annotation.",
    "reason": "The sequence contains identifiable structural and catalytic motifs (Rossmann fold, catalytic Cys dyad CNSNCA) that allow a knowledgeable biochemist to narrow from four EC numbers to the correct one through general enzyme-mechanism reasoning, without needing to recall the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC top-level classes (1.1.1.x, 1.2.1.x, 2.7.1.x), and within EC 1.2.1.x the CNSNCA motif is specific to ASADH. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The CNSNCA catalytic-motif recognition is specialized biochemistry; a model without training on ASADH active-site architecture may struggle to distinguish D from A (both EC 1.2.1.x).",
    "The reviewer evidence is experimental (X-ray crystallography and enzymatic assays), strengthening the annotation, but this evidence was not available to the evaluated model.",
    "The exact identity of EC 1.2.1.46 (choice A) was not independently verified here; however, the CNSNCA motif is not a general feature of all EC 1.2.1.x enzymes, supporting the discrimination."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns EC 1.2.1.11 and gives the corresponding catalytic reaction, with both supported by experimental evidence codes. This supports choice D.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features consistent with the aspartate-semialdehyde dehydrogenase family, including a nucleotide-binding-like N-terminal motif and a conserved cysteine-containing region. Transferable family knowledge connects this enzyme to the phosphorylating oxidation of aspartate semialdehyde, distinguishing EC 1.2.1.11 (D) from the other offered enzyme classifications.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a meaningful basis for choosing among these options without needing the exact protein's database annotation. The inference is not experimental proof, but the offered alternatives make the family distinction relevant.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based family inference and the sequence-matched annotation support the same offered option.


### Important caveats

- The annotation excerpts cite experimental evidence, but the cited primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with the aspartate-semialdehyde dehydrogenase family, including a nucleotide-binding-like N-terminal motif and a conserved cysteine-containing region. Transferable family knowledge connects this enzyme to the phosphorylating oxidation of aspartate semialdehyde, distinguishing EC 1.2.1.11 (D) from the other offered enzyme classifications.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing among these options without needing the exact protein's database annotation. The inference is not experimental proof, but the offered alternatives make the family distinction relevant."
  },
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.2.1.11 and gives the corresponding catalytic reaction, with both supported by experimental evidence codes. This supports choice D."
  },
  "important_caveats": [
    "The annotation excerpts cite experimental evidence, but the cited primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference and the sequence-matched annotation support the same offered option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.2.1.11 and gives the corresponding catalytic reaction, with both supported by experimental evidence codes. This supports choice D.",
    "evidence_ids": ["C1", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features consistent with the aspartate-semialdehyde dehydrogenase family, including a nucleotide-binding-like N-terminal motif and a conserved cysteine-containing region. Transferable family knowledge connects this enzyme to the phosphorylating oxidation of aspartate semialdehyde, distinguishing EC 1.2.1.11 (D) from the other offered enzyme classifications.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing among these options without needing the exact protein's database annotation. The inference is not experimental proof, but the offered alternatives make the family distinction relevant."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference and the sequence-matched annotation support the same offered option."
  },
  "important_caveats": [
    "The annotation excerpts cite experimental evidence, but the cited primary studies were not independently reviewed here."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer-only UniProt evidence (C4, C5, H2, H5) confirms the protein is Aspartate-semialdehyde dehydrogenase (Q4WWR8) with EC 1.2.1.11, annotated with experimental evidence codes (ECO:0000269 from PubMed 28045392 and 29608391). A crystal structure (PDB 5JW6) and biochemical characterization support the catalytic activity: L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+). The sequence matches exactly (363 aa, same SHA256).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark features of the aspartate-semialdehyde dehydrogenase (ASADH) family, one of the most extensively characterized enzyme families across bacteria, fungi, and plants. (1) The N-terminal 'GVLGATGSVG' motif is a canonical Rossmann-fold NAD(P)-binding signature (GxGxxG), shared with hundreds of dehydrogenases but with the specific spacing and flanking context matching ASADH homologs. (2) The catalytic cysteine in the 'GFLVCNSNCAVIG' region is characteristic of aldehyde dehydrogenases (EC 1.2.1.x) that use a Cys-thioester intermediate mechanism, distinguishing them from alcohol dehydrogenases (EC 1.1.x.x) which use Ser/Zn catalysis. This eliminates option B (1.1.1.195). (3) The overall ~363 aa length and two-domain architecture (Rossmann NAD(P)-binding domain + catalytic domain) match the ASADH family size (~340-370 aa) and are inconsistent with multi-domain enzymes. (4) The transferase option C (2.7.1.39) is excluded by the clear oxidoreductase signature (Rossmann fold + catalytic Cys + NAD(P) binding). (5) Between the remaining EC 1.2.1.x options (A: 1.2.1.46 vs D: 1.2.1.11), the specific combination of N-terminal Rossmann fold sequence, catalytic Cys context, and overall fold architecture matches ASADH homologs studied in E. coli, Saccharomyces, and other fungi, where EC 1.2.1.11 is the established assignment. This is transferable family-level knowledge from ASADH characterization across many organisms.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use transferable ASADH family knowledge (Rossmann fold motif, catalytic Cys mechanism, ~360 aa size, two-domain architecture) learned from homologs in E. coli, yeast, plants, and other fungi to distinguish EC 1.2.1.11 from an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), and a different aldehyde dehydrogenase (EC 1.2.1.46). The sequence features are diagnostic at the family level without requiring recall of this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence features (Rossmann fold, catalytic Cys, ~363 aa length, two-domain architecture) clearly point to the ASADH family (EC 1.2.1.11) and are inconsistent with an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), or a structurally distinct aldehyde dehydrogenase. No other option is well-supported by the sequence evidence.


### Important caveats

- The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269) with a crystal structure, not merely computational prediction.
- The exact identity of EC 1.2.1.46 (option A) was not independently verified from the provided materials; the argument for excluding it relies on the sequence matching ASADH family features rather than on knowing the specific properties of 1.2.1.46.
- The UniProt entry was first public in 2025-02-05; the author's source snapshot is unknown, though the sequence has been stable since 2005.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark features of the aspartate-semialdehyde dehydrogenase (ASADH) family, one of the most extensively characterized enzyme families across bacteria, fungi, and plants. (1) The N-terminal 'GVLGATGSVG' motif is a canonical Rossmann-fold NAD(P)-binding signature (GxGxxG), shared with hundreds of dehydrogenases but with the specific spacing and flanking context matching ASADH homologs. (2) The catalytic cysteine in the 'GFLVCNSNCAVIG' region is characteristic of aldehyde dehydrogenases (EC 1.2.1.x) that use a Cys-thioester intermediate mechanism, distinguishing them from alcohol dehydrogenases (EC 1.1.x.x) which use Ser/Zn catalysis. This eliminates option B (1.1.1.195). (3) The overall ~363 aa length and two-domain architecture (Rossmann NAD(P)-binding domain + catalytic domain) match the ASADH family size (~340-370 aa) and are inconsistent with multi-domain enzymes. (4) The transferase option C (2.7.1.39) is excluded by the clear oxidoreductase signature (Rossmann fold + catalytic Cys + NAD(P) binding). (5) Between the remaining EC 1.2.1.x options (A: 1.2.1.46 vs D: 1.2.1.11), the specific combination of N-terminal Rossmann fold sequence, catalytic Cys context, and overall fold architecture matches ASADH homologs studied in E. coli, Saccharomyces, and other fungi, where EC 1.2.1.11 is the established assignment. This is transferable family-level knowledge from ASADH characterization across many organisms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable ASADH family knowledge (Rossmann fold motif, catalytic Cys mechanism, ~360 aa size, two-domain architecture) learned from homologs in E. coli, yeast, plants, and other fungi to distinguish EC 1.2.1.11 from an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), and a different aldehyde dehydrogenase (EC 1.2.1.46). The sequence features are diagnostic at the family level without requiring recall of this specific UniProt entry."
  },
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only UniProt evidence (C4, C5, H2, H5) confirms the protein is Aspartate-semialdehyde dehydrogenase (Q4WWR8) with EC 1.2.1.11, annotated with experimental evidence codes (ECO:0000269 from PubMed 28045392 and 29608391). A crystal structure (PDB 5JW6) and biochemical characterization support the catalytic activity: L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+). The sequence matches exactly (363 aa, same SHA256)."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269) with a crystal structure, not merely computational prediction.",
    "The exact identity of EC 1.2.1.46 (option A) was not independently verified from the provided materials; the argument for excluding it relies on the sequence matching ASADH family features rather than on knowing the specific properties of 1.2.1.46.",
    "The UniProt entry was first public in 2025-02-05; the author's source snapshot is unknown, though the sequence has been stable since 2005."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features (Rossmann fold, catalytic Cys, ~363 aa length, two-domain architecture) clearly point to the ASADH family (EC 1.2.1.11) and are inconsistent with an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), or a structurally distinct aldehyde dehydrogenase. No other option is well-supported by the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only UniProt evidence (C4, C5, H2, H5) confirms the protein is Aspartate-semialdehyde dehydrogenase (Q4WWR8) with EC 1.2.1.11, annotated with experimental evidence codes (ECO:0000269 from PubMed 28045392 and 29608391). A crystal structure (PDB 5JW6) and biochemical characterization support the catalytic activity: L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+). The sequence matches exactly (363 aa, same SHA256).",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark features of the aspartate-semialdehyde dehydrogenase (ASADH) family, one of the most extensively characterized enzyme families across bacteria, fungi, and plants. (1) The N-terminal 'GVLGATGSVG' motif is a canonical Rossmann-fold NAD(P)-binding signature (GxGxxG), shared with hundreds of dehydrogenases but with the specific spacing and flanking context matching ASADH homologs. (2) The catalytic cysteine in the 'GFLVCNSNCAVIG' region is characteristic of aldehyde dehydrogenases (EC 1.2.1.x) that use a Cys-thioester intermediate mechanism, distinguishing them from alcohol dehydrogenases (EC 1.1.x.x) which use Ser/Zn catalysis. This eliminates option B (1.1.1.195). (3) The overall ~363 aa length and two-domain architecture (Rossmann NAD(P)-binding domain + catalytic domain) match the ASADH family size (~340-370 aa) and are inconsistent with multi-domain enzymes. (4) The transferase option C (2.7.1.39) is excluded by the clear oxidoreductase signature (Rossmann fold + catalytic Cys + NAD(P) binding). (5) Between the remaining EC 1.2.1.x options (A: 1.2.1.46 vs D: 1.2.1.11), the specific combination of N-terminal Rossmann fold sequence, catalytic Cys context, and overall fold architecture matches ASADH homologs studied in E. coli, Saccharomyces, and other fungi, where EC 1.2.1.11 is the established assignment. This is transferable family-level knowledge from ASADH characterization across many organisms.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable ASADH family knowledge (Rossmann fold motif, catalytic Cys mechanism, ~360 aa size, two-domain architecture) learned from homologs in E. coli, yeast, plants, and other fungi to distinguish EC 1.2.1.11 from an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), and a different aldehyde dehydrogenase (EC 1.2.1.46). The sequence features are diagnostic at the family level without requiring recall of this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features (Rossmann fold, catalytic Cys, ~363 aa length, two-domain architecture) clearly point to the ASADH family (EC 1.2.1.11) and are inconsistent with an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), or a structurally distinct aldehyde dehydrogenase. No other option is well-supported by the sequence evidence."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269) with a crystal structure, not merely computational prediction.",
    "The exact identity of EC 1.2.1.46 (option A) was not independently verified from the provided materials; the argument for excluding it relies on the sequence matching ASADH family features rather than on knowing the specific properties of 1.2.1.46.",
    "The UniProt entry was first public in 2025-02-05; the author's source snapshot is unknown, though the sequence has been stable since 2005."
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
  "requested_accession": "Q4WWR8",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "benchmark_sequence_length": 363,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "current_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "current_source_sequence_length": 363,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 118,
  "selected_historical_version": {
    "accession": "Q4WWR8",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_ASPFU",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "selected_historical_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "selected_historical_source_sequence_length": 363,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 118,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q4WWR8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002530\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28045392\",\"source\":\"PubMed\"}],\"value\":\"AfASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24286\"}}],\"reaction\":{\"ecNumber\":\"1.2.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"name\":\"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24284\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:537519\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28045392\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2053230x16020070\"}],\"citationType\":\"journal article\",\"firstPage\":\"36\",\"id\":\"28045392\",\"journal\":\"Acta Crystallogr. F\",\"lastPage\":\"44\",\"publicationDate\":\"2017\",\"title\":\"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from Aspergillus fumigatus.\",\"volume\":\"73\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5JW6\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   DHAS_ASPFU              Reviewed;         363 AA.\nAC   Q4WWR8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\nDE   AltName: Full=AfASADH {ECO:0000303|PubMed:28045392};\nGN   Name=hom2 {ECO:0000305};\nGN   ORFNames=AFUA_3G06830 {ECO:0000312|EMBL:EAL92885.1};\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879 {ECO:0000312|Proteomes:UP000002530};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\nDE   AltName: Full=AfASADH {ECO:0000303|PubMed:28045392};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 50-56",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 57-64",
  "excerpt": "RN   [4] {ECO:0007744|PDB:5JW6}\nRP   X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=28045392; DOI=10.1107/s2053230x16020070;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from\nRT   Aspergillus fumigatus.\";\nRL   Acta Crystallogr. F 73:36-44(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 72-79",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-\nCC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;\nCC         Evidence={ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;\nCC         Evidence={ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
