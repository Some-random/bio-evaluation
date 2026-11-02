# pathway_0127

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFSSLFVAACAAVTAFALPSELEKRAITTSQQGTSNGYFYSFWTNGGGSVSYNNGASGEYSVSWSNCGSFTSGKGWATGSSRNINFSGSFKPSGNAYLAVYGWTTSPLVEYYIMENYGDYNPGRSMTFKGTVTSDGSVYDIYTHQQVNQPSISGTATFEQYWSIRRTKRSSGTVTTANHFKAWASHGMYLGSHNYQIVSTEGYQSSGSSDITVS

[Multiple Choices]
A. L-methionine biosynthesis via de novo pathway. .
B. LPS O-antigen biosynthesis. .
C. Glycan degradation
D. Pyrimidine metabolism
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches a UniProt record annotated as an ethylene-inducing xylanase, EC 3.2.1.8, with a pathway annotation of glycan degradation via xylan degradation. The pathway assignment is attributed to a PROSITE-ProRule computational annotation, not established by the supplied excerpts as an experimental pathway measurement.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus has a hydrophobic signal-peptide-like segment, consistent with a secreted protein. That makes an extracellular carbohydrate-degrading enzyme a plausible fit, whereas methionine and pyrimidine biosynthesis are typically intracellular and LPS O-antigen biosynthesis is associated with bacterial cell envelopes. Among these choices, glycan degradation is meaningfully favored.


**Missing item-specific fact**

> The exact xylanase identity and catalytic activity are not stated in the input; those would be needed to establish the specific xylan-degradation assignment rather than infer the best fit among the choices.


**Reason**

> The sequence and choices provide a concrete, though not conclusive, biological basis for preferring glycan degradation. The exact enzyme annotation is reviewer-only evidence supporting the key, not information supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the listed alternatives, glycan degradation is the best-supported choice; the sequence does not directly prove its precise enzymatic activity, but the other options are less consistent with a likely secreted protein.


### Important caveats

- The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.
- The pathway annotation is computationally attributed to PROSITE-ProRule; the excerpts do not independently establish experimental validation of the pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus has a hydrophobic signal-peptide-like segment, consistent with a secreted protein. That makes an extracellular carbohydrate-degrading enzyme a plausible fit, whereas methionine and pyrimidine biosynthesis are typically intracellular and LPS O-antigen biosynthesis is associated with bacterial cell envelopes. Among these choices, glycan degradation is meaningfully favored.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact xylanase identity and catalytic activity are not stated in the input; those would be needed to establish the specific xylan-degradation assignment rather than infer the best fit among the choices.",
    "reason": "The sequence and choices provide a concrete, though not conclusive, biological basis for preferring glycan degradation. The exact enzyme annotation is reviewer-only evidence supporting the key, not information supplied to the evaluated model."
  },
  "case_id": "pathway_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches a UniProt record annotated as an ethylene-inducing xylanase, EC 3.2.1.8, with a pathway annotation of glycan degradation via xylan degradation. The pathway assignment is attributed to a PROSITE-ProRule computational annotation, not established by the supplied excerpts as an experimental pathway measurement."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway annotation is computationally attributed to PROSITE-ProRule; the excerpts do not independently establish experimental validation of the pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the listed alternatives, glycan degradation is the best-supported choice; the sequence does not directly prove its precise enzymatic activity, but the other options are less consistent with a likely secreted protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches a UniProt record annotated as an ethylene-inducing xylanase, EC 3.2.1.8, with a pathway annotation of glycan degradation via xylan degradation. The pathway assignment is attributed to a PROSITE-ProRule computational annotation, not established by the supplied excerpts as an experimental pathway measurement.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a hydrophobic signal-peptide-like segment, consistent with a secreted protein. That makes an extracellular carbohydrate-degrading enzyme a plausible fit, whereas methionine and pyrimidine biosynthesis are typically intracellular and LPS O-antigen biosynthesis is associated with bacterial cell envelopes. Among these choices, glycan degradation is meaningfully favored.",
    "missing_item_specific_fact": "The exact xylanase identity and catalytic activity are not stated in the input; those would be needed to establish the specific xylan-degradation assignment rather than infer the best fit among the choices.",
    "reason": "The sequence and choices provide a concrete, though not conclusive, biological basis for preferring glycan degradation. The exact enzyme annotation is reviewer-only evidence supporting the key, not information supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the listed alternatives, glycan degradation is the best-supported choice; the sequence does not directly prove its precise enzymatic activity, but the other options are less consistent with a likely secreted protein."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway annotation is computationally attributed to PROSITE-ProRule; the excerpts do not independently establish experimental validation of the pathway assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry K9GHZ3 (sequence matched, 216 AA) annotates the protein as Ethylene-inducing xylanase (EC 3.2.1.8, Endo-1,4-beta-xylanase) with PATHWAY: 'Glycan degradation; xylan degradation' (ECO:0000255|PROSITE-ProRule:PRU01097). The author key 'Glycan degradation' directly matches the UniProt pathway annotation. The EC 3.2.1.8 assignment (glycoside hydrolase acting on xylan, a polysaccharide/glycan) is consistent with the glycan degradation pathway. Note the evidence code is PROSITE-ProRule (computational inference), not direct experimental pathway reconstitution, but the xylanase activity and its classification as a glycan-degrading enzyme are well-established.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch (MVSFSSLFVAACAAVTAFALPSE...) is a canonical signal peptide indicating a secreted protein. Among the four options, L-methionine biosynthesis (A) and pyrimidine metabolism (D) are intracellular metabolic pathways whose enzymes do not require signal peptides. LPS O-antigen biosynthesis (B) is a bacterial pathway and is inapplicable to a fungal-derived protein. A secreted, relatively small (~216 aa) protein with composition consistent with a glycoside hydrolase fold most plausibly functions as an extracellular degradative enzyme, i.e., glycan degradation (C). This elimination-based reasoning uses general cell biology (signal peptide → secretion) and taxonomy (fungal vs. bacterial pathways) without requiring memorization of this specific protein's database entry.


**Missing item-specific fact**

> None critical. Positive identification as specifically a xylanase (GH10 family) would require recognizing conserved catalytic motifs, but the question only asks for the pathway category, which is reachable by eliminating intracellular and bacterial options via the signal peptide and organismal context.


**Reason**

> The signal peptide is a concrete, observable sequence feature that supports the secreted-protein inference. Combined with the inapplicability of bacterial LPS biosynthesis to a fungal protein and the intracellular nature of methionine/pyrimidine pathways, the answer C is distinguishable through general biological reasoning without memorizing this protein's UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated: two are intracellular metabolic pathways (A, D), one is a bacterial pathway (B), and one is an extracellular degradative pathway (C). The signal peptide and fungal context cleanly eliminate A, B, and D, leaving C as the sole defensible choice.


### Important caveats

- The UniProt pathway annotation is based on PROSITE-ProRule (ECO:0000255), a computational/inference evidence code, not direct experimental pathway reconstitution. However, EC 3.2.1.8 (xylanase) is a well-established glycoside hydrolase activity.
- The reviewer-only evidence confirms the sequence matches K9GHZ3 exactly (SHA256 verified), but this accession was not provided to the evaluated model.
- The reasoning argument relies on recognizing the signal peptide and applying general biology (secretion, fungal vs. bacterial metabolism). A model unable to parse signal peptides from raw sequence would struggle, but this is a standard feature of the task format.
- The protein also functions as a pathogen-associated molecular pattern (PAMP) inducing ethylene in plants (PubMed:39718348), but its enzymatic/pathway classification remains glycan degradation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MVSFSSLFVAACAAVTAFALPSE...) is a canonical signal peptide indicating a secreted protein. Among the four options, L-methionine biosynthesis (A) and pyrimidine metabolism (D) are intracellular metabolic pathways whose enzymes do not require signal peptides. LPS O-antigen biosynthesis (B) is a bacterial pathway and is inapplicable to a fungal-derived protein. A secreted, relatively small (~216 aa) protein with composition consistent with a glycoside hydrolase fold most plausibly functions as an extracellular degradative enzyme, i.e., glycan degradation (C). This elimination-based reasoning uses general cell biology (signal peptide → secretion) and taxonomy (fungal vs. bacterial pathways) without requiring memorization of this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Positive identification as specifically a xylanase (GH10 family) would require recognizing conserved catalytic motifs, but the question only asks for the pathway category, which is reachable by eliminating intracellular and bacterial options via the signal peptide and organismal context.",
    "reason": "The signal peptide is a concrete, observable sequence feature that supports the secreted-protein inference. Combined with the inapplicability of bacterial LPS biosynthesis to a fungal protein and the intracellular nature of methionine/pyrimidine pathways, the answer C is distinguishable through general biological reasoning without memorizing this protein's UniProt annotation."
  },
  "case_id": "pathway_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry K9GHZ3 (sequence matched, 216 AA) annotates the protein as Ethylene-inducing xylanase (EC 3.2.1.8, Endo-1,4-beta-xylanase) with PATHWAY: 'Glycan degradation; xylan degradation' (ECO:0000255|PROSITE-ProRule:PRU01097). The author key 'Glycan degradation' directly matches the UniProt pathway annotation. The EC 3.2.1.8 assignment (glycoside hydrolase acting on xylan, a polysaccharide/glycan) is consistent with the glycan degradation pathway. Note the evidence code is PROSITE-ProRule (computational inference), not direct experimental pathway reconstitution, but the xylanase activity and its classification as a glycan-degrading enzyme are well-established."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on PROSITE-ProRule (ECO:0000255), a computational/inference evidence code, not direct experimental pathway reconstitution. However, EC 3.2.1.8 (xylanase) is a well-established glycoside hydrolase activity.",
    "The reviewer-only evidence confirms the sequence matches K9GHZ3 exactly (SHA256 verified), but this accession was not provided to the evaluated model.",
    "The reasoning argument relies on recognizing the signal peptide and applying general biology (secretion, fungal vs. bacterial metabolism). A model unable to parse signal peptides from raw sequence would struggle, but this is a standard feature of the task format.",
    "The protein also functions as a pathogen-associated molecular pattern (PAMP) inducing ethylene in plants (PubMed:39718348), but its enzymatic/pathway classification remains glycan degradation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: two are intracellular metabolic pathways (A, D), one is a bacterial pathway (B), and one is an extracellular degradative pathway (C). The signal peptide and fungal context cleanly eliminate A, B, and D, leaving C as the sole defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry K9GHZ3 (sequence matched, 216 AA) annotates the protein as Ethylene-inducing xylanase (EC 3.2.1.8, Endo-1,4-beta-xylanase) with PATHWAY: 'Glycan degradation; xylan degradation' (ECO:0000255|PROSITE-ProRule:PRU01097). The author key 'Glycan degradation' directly matches the UniProt pathway annotation. The EC 3.2.1.8 assignment (glycoside hydrolase acting on xylan, a polysaccharide/glycan) is consistent with the glycan degradation pathway. Note the evidence code is PROSITE-ProRule (computational inference), not direct experimental pathway reconstitution, but the xylanase activity and its classification as a glycan-degrading enzyme are well-established.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MVSFSSLFVAACAAVTAFALPSE...) is a canonical signal peptide indicating a secreted protein. Among the four options, L-methionine biosynthesis (A) and pyrimidine metabolism (D) are intracellular metabolic pathways whose enzymes do not require signal peptides. LPS O-antigen biosynthesis (B) is a bacterial pathway and is inapplicable to a fungal-derived protein. A secreted, relatively small (~216 aa) protein with composition consistent with a glycoside hydrolase fold most plausibly functions as an extracellular degradative enzyme, i.e., glycan degradation (C). This elimination-based reasoning uses general cell biology (signal peptide → secretion) and taxonomy (fungal vs. bacterial pathways) without requiring memorization of this specific protein's database entry.",
    "missing_item_specific_fact": "None critical. Positive identification as specifically a xylanase (GH10 family) would require recognizing conserved catalytic motifs, but the question only asks for the pathway category, which is reachable by eliminating intracellular and bacterial options via the signal peptide and organismal context.",
    "reason": "The signal peptide is a concrete, observable sequence feature that supports the secreted-protein inference. Combined with the inapplicability of bacterial LPS biosynthesis to a fungal protein and the intracellular nature of methionine/pyrimidine pathways, the answer C is distinguishable through general biological reasoning without memorizing this protein's UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: two are intracellular metabolic pathways (A, D), one is a bacterial pathway (B), and one is an extracellular degradative pathway (C). The signal peptide and fungal context cleanly eliminate A, B, and D, leaving C as the sole defensible choice."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on PROSITE-ProRule (ECO:0000255), a computational/inference evidence code, not direct experimental pathway reconstitution. However, EC 3.2.1.8 (xylanase) is a well-established glycoside hydrolase activity.",
    "The reviewer-only evidence confirms the sequence matches K9GHZ3 exactly (SHA256 verified), but this accession was not provided to the evaluated model.",
    "The reasoning argument relies on recognizing the signal peptide and applying general biology (secretion, fungal vs. bacterial metabolism). A model unable to parse signal peptides from raw sequence would struggle, but this is a standard feature of the task format.",
    "The protein also functions as a pathogen-associated molecular pattern (PAMP) inducing ethylene in plants (PubMed:39718348), but its enzymatic/pathway classification remains glycan degradation."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `K9GHZ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
"K9GHZ3"
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"Ethylene-inducing xylanase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"EIX"}]}}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
ID   EIX_PEND1               Reviewed;         216 AA.
AC   K9GHZ3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   06-FEB-2013, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:39718348};
DE            Short=EIX {ECO:0000303|PubMed:39718348};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:39718348};
DE   Flags: Precursor;
GN   Name=EIX {ECO:0000303|PubMed:39718348}; ORFNames=PDIP_02920;
OS   Penicillium digitatum (strain Pd1 / CECT 20795) (Green mold).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=1170230;
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 44-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-
CC       ProRule:PRU01097}.
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
