# GO_biological_process_0012

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — indole alkaloid biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATPQFSCLLPAFFLLVVFLFLLIKELRRYKSPKTTQKLPPGPPMLPIIGNLHQMASSLPHQNLKKLADKYGPLMHLKLGEISAVAVSSPRLAKEVLQTRGLAFADRPQSVVAKLMLHNCLGVTFSRYGDYWRQLRQIFAMELLSSKSVQSFSTIMEDELFAMVKSIESEAGRPIILADKLISYLYATLSRATLGRVCKGKETLIEVTGETLALSGAQSLEDIFPSVKIFAYLNPLRPKVRKLFNRIDGVLEDIINQQEKKLLSARVDNDQLQPEENDMLSVLLKLRNGKDSKVQVTNNDIKAIIFELFLAGTVGSSTTVEWAMSEMMKNPKVMEKAQHEVREVLKGKKRICQSDIQKLSYLKLVVKETLRLHPPAPLLFPRECRGQCEVDGYTIPAKAMVMVNCWALGRDPEHWIEADKFEPERFKNSSIDFIGNHFEYIPFGAGRRICPGISFGATNVELLLAALLYHFDWELAGGMHPKDLDMLELFGPGCTRKNPLSVIPSICIPSHDDN

[Multiple Choices]
A. nuclear pore complex assembly
B. regulation of establishment of protein localization
C. indole alkaloid biosynthetic process
D. negative regulation of RNA export from nucleus
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact sequence matches the Alstonia scholaris alstonine synthase entry. Its function is reported as converting tetrahydroalstonine to alstonine, and the entry assigns indole alkaloid biosynthesis with IDA evidence linked to a publication. This supports choice C, while preserving that the evidence is reported in the cited source rather than independently assessed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and P450-like sequence features may suggest a membrane-associated cytochrome P450, but they do not identify its particular substrate or biological pathway. Those broad features do not meaningfully distinguish indole alkaloid biosynthesis from the other listed processes.


**Missing item-specific fact**

> The protein-specific identification as alstonine synthase and its reported catalytic conversion of tetrahydroalstonine to alstonine are needed to select indole alkaloid biosynthesis.


**Reason**

> The decisive functional and pathway information is absent from the sequence and choices. Recognizing the exact sequence or retrieving its annotation would resolve the answer, but would constitute lookup or memorization rather than reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone does not establish which process applies, but the reviewer-only matched-sequence evidence supports C; no other listed option is supported by the supplied evidence.


### Important caveats

- Reviewer-only sequence identity and annotations were not supplied to the evaluated model.
- The historical entry and current entry both match the sequence, but the author's exact source snapshot is unknown.
- The functional annotation is linked to a publication and carries IDA evidence; the primary study was not independently retrieved and validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and P450-like sequence features may suggest a membrane-associated cytochrome P450, but they do not identify its particular substrate or biological pathway. Those broad features do not meaningfully distinguish indole alkaloid biosynthesis from the other listed processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as alstonine synthase and its reported catalytic conversion of tetrahydroalstonine to alstonine are needed to select indole alkaloid biosynthesis.",
    "reason": "The decisive functional and pathway information is absent from the sequence and choices. Recognizing the exact sequence or retrieving its annotation would resolve the answer, but would constitute lookup or memorization rather than reasoning from supplied context."
  },
  "case_id": "GO_biological_process_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Alstonia scholaris alstonine synthase entry. Its function is reported as converting tetrahydroalstonine to alstonine, and the entry assigns indole alkaloid biosynthesis with IDA evidence linked to a publication. This supports choice C, while preserving that the evidence is reported in the cited source rather than independently assessed here."
  },
  "important_caveats": [
    "Reviewer-only sequence identity and annotations were not supplied to the evaluated model.",
    "The historical entry and current entry both match the sequence, but the author's exact source snapshot is unknown.",
    "The functional annotation is linked to a publication and carries IDA evidence; the primary study was not independently retrieved and validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not establish which process applies, but the reviewer-only matched-sequence evidence supports C; no other listed option is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Alstonia scholaris alstonine synthase entry. Its function is reported as converting tetrahydroalstonine to alstonine, and the entry assigns indole alkaloid biosynthesis with IDA evidence linked to a publication. This supports choice C, while preserving that the evidence is reported in the cited source rather than independently assessed here.",
    "evidence_ids": ["C1", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and P450-like sequence features may suggest a membrane-associated cytochrome P450, but they do not identify its particular substrate or biological pathway. Those broad features do not meaningfully distinguish indole alkaloid biosynthesis from the other listed processes.",
    "missing_item_specific_fact": "The protein-specific identification as alstonine synthase and its reported catalytic conversion of tetrahydroalstonine to alstonine are needed to select indole alkaloid biosynthesis.",
    "reason": "The decisive functional and pathway information is absent from the sequence and choices. Recognizing the exact sequence or retrieving its annotation would resolve the answer, but would constitute lookup or memorization rather than reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not establish which process applies, but the reviewer-only matched-sequence evidence supports C; no other listed option is supported by the supplied evidence."
  },
  "important_caveats": [
    "Reviewer-only sequence identity and annotations were not supplied to the evaluated model.",
    "The historical entry and current entry both match the sequence, but the author's exact source snapshot is unknown.",
    "The functional annotation is linked to a publication and carries IDA evidence; the primary study was not independently retrieved and validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB entry A0A9E7LUJ4 (Alstonine synthase, EC 1.14.19.-) from Alstonia scholaris is directly annotated with GO:0035835 (indole alkaloid biosynthetic process) with evidence code IDA:UniProtKB, supported by experimental data from PubMed:36349266. The FUNCTION comment confirms it catalyzes the conversion of tetrahydroalstonine to alstonine (a pentacyclic indole alkaloid), and the PATHWAY comment states 'Alkaloid biosynthesis.' The sequence matches the benchmark input exactly (SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif (FxxGxRxCxG: visible as 'FIGNHFEYIPFGAGRRICPGISFG' with the conserved heme-coordinating Cys in 'RRICPG'), identifying the protein as a P450 monooxygenase — a metabolic/biosynthetic enzyme. Among the four options, only C (indole alkaloid biosynthetic process) describes a metabolic/biosynthetic pathway. Options A (nuclear pore complex assembly), B (regulation of establishment of protein localization), and D (negative regulation of RNA export from nucleus) all describe nucleocytoplasmic transport/localization processes, which are mechanistically incompatible with the catalytic function of a P450 enzyme. A model recognizing the P450 motif can eliminate A, B, and D on the basis that P450s are metabolic oxidases, not structural or regulatory components of nuclear transport machinery.


**Missing item-specific fact**

> None strictly required. While the specific 'indole alkaloid' label (as opposed to, e.g., terpenoid or fatty-acid metabolism) cannot be positively identified from the sequence alone without organism/substrate context, the three distractors are all non-metabolic processes that are categorically incompatible with a P450, making C the only viable option by elimination.


**Reason**

> The P450 heme-binding motif is a well-known, identifiable sequence feature. Recognizing it as a metabolic enzyme and contrasting that with the three nuclear-transport-related distractors constitutes a concrete biological argument grounded in general enzymology and cell biology, not item-specific memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe nucleocytoplasmic transport or localization processes that are mechanistically incompatible with a cytochrome P450 monooxygenase. Only C describes a biosynthetic/metabolic process consistent with P450 enzymatic activity. No other option is defensible for this protein class.


### Important caveats

- The specific 'indole alkaloid' qualifier in option C is not derivable from the sequence alone; it is selected by elimination of clearly incompatible non-metabolic distractors rather than by positive identification of the alkaloid class.
- The UniProt annotation uses evidence code IDA (Inferred from Direct Assay), indicating experimental support from PubMed:36349266, not purely computational inference.
- The entry was first publicly released 2025-06-18 (entry version 14); the historical archived version 13 (released 28-Jan-2026) also carries the same GO annotation. The benchmark author's source snapshot date is unknown, but the sequence has been stable since 2023-05-03.
- The reviewer-only evidence confirms sequence identity (SHA256 match) between the benchmark input and the UniProt entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FxxGxRxCxG: visible as 'FIGNHFEYIPFGAGRRICPGISFG' with the conserved heme-coordinating Cys in 'RRICPG'), identifying the protein as a P450 monooxygenase — a metabolic/biosynthetic enzyme. Among the four options, only C (indole alkaloid biosynthetic process) describes a metabolic/biosynthetic pathway. Options A (nuclear pore complex assembly), B (regulation of establishment of protein localization), and D (negative regulation of RNA export from nucleus) all describe nucleocytoplasmic transport/localization processes, which are mechanistically incompatible with the catalytic function of a P450 enzyme. A model recognizing the P450 motif can eliminate A, B, and D on the basis that P450s are metabolic oxidases, not structural or regulatory components of nuclear transport machinery.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. While the specific 'indole alkaloid' label (as opposed to, e.g., terpenoid or fatty-acid metabolism) cannot be positively identified from the sequence alone without organism/substrate context, the three distractors are all non-metabolic processes that are categorically incompatible with a P450, making C the only viable option by elimination.",
    "reason": "The P450 heme-binding motif is a well-known, identifiable sequence feature. Recognizing it as a metabolic enzyme and contrasting that with the three nuclear-transport-related distractors constitutes a concrete biological argument grounded in general enzymology and cell biology, not item-specific memorization."
  },
  "case_id": "GO_biological_process_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB entry A0A9E7LUJ4 (Alstonine synthase, EC 1.14.19.-) from Alstonia scholaris is directly annotated with GO:0035835 (indole alkaloid biosynthetic process) with evidence code IDA:UniProtKB, supported by experimental data from PubMed:36349266. The FUNCTION comment confirms it catalyzes the conversion of tetrahydroalstonine to alstonine (a pentacyclic indole alkaloid), and the PATHWAY comment states 'Alkaloid biosynthesis.' The sequence matches the benchmark input exactly (SHA256 confirmed)."
  },
  "important_caveats": [
    "The specific 'indole alkaloid' qualifier in option C is not derivable from the sequence alone; it is selected by elimination of clearly incompatible non-metabolic distractors rather than by positive identification of the alkaloid class.",
    "The UniProt annotation uses evidence code IDA (Inferred from Direct Assay), indicating experimental support from PubMed:36349266, not purely computational inference.",
    "The entry was first publicly released 2025-06-18 (entry version 14); the historical archived version 13 (released 28-Jan-2026) also carries the same GO annotation. The benchmark author's source snapshot date is unknown, but the sequence has been stable since 2023-05-03.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) between the benchmark input and the UniProt entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe nucleocytoplasmic transport or localization processes that are mechanistically incompatible with a cytochrome P450 monooxygenase. Only C describes a biosynthetic/metabolic process consistent with P450 enzymatic activity. No other option is defensible for this protein class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB entry A0A9E7LUJ4 (Alstonine synthase, EC 1.14.19.-) from Alstonia scholaris is directly annotated with GO:0035835 (indole alkaloid biosynthetic process) with evidence code IDA:UniProtKB, supported by experimental data from PubMed:36349266. The FUNCTION comment confirms it catalyzes the conversion of tetrahydroalstonine to alstonine (a pentacyclic indole alkaloid), and the PATHWAY comment states 'Alkaloid biosynthesis.' The sequence matches the benchmark input exactly (SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FxxGxRxCxG: visible as 'FIGNHFEYIPFGAGRRICPGISFG' with the conserved heme-coordinating Cys in 'RRICPG'), identifying the protein as a P450 monooxygenase — a metabolic/biosynthetic enzyme. Among the four options, only C (indole alkaloid biosynthetic process) describes a metabolic/biosynthetic pathway. Options A (nuclear pore complex assembly), B (regulation of establishment of protein localization), and D (negative regulation of RNA export from nucleus) all describe nucleocytoplasmic transport/localization processes, which are mechanistically incompatible with the catalytic function of a P450 enzyme. A model recognizing the P450 motif can eliminate A, B, and D on the basis that P450s are metabolic oxidases, not structural or regulatory components of nuclear transport machinery.",
    "missing_item_specific_fact": "None strictly required. While the specific 'indole alkaloid' label (as opposed to, e.g., terpenoid or fatty-acid metabolism) cannot be positively identified from the sequence alone without organism/substrate context, the three distractors are all non-metabolic processes that are categorically incompatible with a P450, making C the only viable option by elimination.",
    "reason": "The P450 heme-binding motif is a well-known, identifiable sequence feature. Recognizing it as a metabolic enzyme and contrasting that with the three nuclear-transport-related distractors constitutes a concrete biological argument grounded in general enzymology and cell biology, not item-specific memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe nucleocytoplasmic transport or localization processes that are mechanistically incompatible with a cytochrome P450 monooxygenase. Only C describes a biosynthetic/metabolic process consistent with P450 enzymatic activity. No other option is defensible for this protein class."
  },
  "important_caveats": [
    "The specific 'indole alkaloid' qualifier in option C is not derivable from the sequence alone; it is selected by elimination of clearly incompatible non-metabolic distractors rather than by positive identification of the alkaloid class.",
    "The UniProt annotation uses evidence code IDA (Inferred from Direct Assay), indicating experimental support from PubMed:36349266, not purely computational inference.",
    "The entry was first publicly released 2025-06-18 (entry version 14); the historical archived version 13 (released 28-Jan-2026) also carries the same GO annotation. The benchmark author's source snapshot date is unknown, but the sequence has been stable since 2023-05-03.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) between the benchmark input and the UniProt entry."
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

**Accession:** `A0A9E7LUJ4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
"A0A9E7LUJ4"
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Cytochrome P450 AS"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.14.19.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Alstonine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsAS"}]}}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"A cytochrome P450 monooxygenase involved in the biosynthesis of pentacyclic alkaloids natural products such as alstonine, putative antipsychotic compounds (PubMed:36349266). Catalyzes the conversion of tetrahydroalstonine to alstonine (PubMed:36349266). No oxidative activity towards ajmalicine (PubMed:36349266)"}]}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"36349266","source":"PubMed"}],"id":"GO:0035835","properties":[{"key":"GoTerm","value":"P:indole alkaloid biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)  
**Locator:** `lines 24-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.040905+00:00.  

```text
CC   -!- FUNCTION: A cytochrome P450 monooxygenase involved in the biosynthesis
CC       of pentacyclic alkaloids natural products such as alstonine, putative
CC       antipsychotic compounds (PubMed:36349266). Catalyzes the conversion of
CC       tetrahydroalstonine to alstonine (PubMed:36349266). No oxidative
CC       activity towards ajmalicine (PubMed:36349266).
CC       {ECO:0000269|PubMed:36349266}.
```

Source SHA-256: `cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)  
**Locator:** `lines 44-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.040905+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:36349266}.
```

Source SHA-256: `cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)  
**Locator:** `lines 58-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.040905+00:00.  

```text
DR   GO; GO:0035835; P:indole alkaloid biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 221717-221728`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0035835
name: indole alkaloid biosynthetic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the formation of an indole alkaloid, an alkaloid containing an indole skeleton." [GOC:yaf]
synonym: "indole alkaloid anabolism" EXACT [GOC:bf]
synonym: "indole alkaloid biosynthesis" EXACT [GOC:bf]
synonym: "indole alkaloid formation" EXACT [GOC:bf]
synonym: "indole alkaloid synthesis" EXACT [GOC:bf]
is_a: GO:0009821 ! alkaloid biosynthetic process
is_a: GO:0035834 ! indole alkaloid metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
