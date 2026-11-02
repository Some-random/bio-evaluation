# GO_biological_process_0049

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — indole alkaloid biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVIGHLHKLGGPNPIYRNLAEWSDKYGPVMTLKLGMQNAVVVSDREAIKECFTTNDKALADRPPSSIGLHLGFNYAAIGAAPYGPYWRDMRKLVLLEVLSSRRLEMLRNVRISEIGTSIKELYSNIIRSSGGSGPAKVVISHWIEQLTLNYILRTIAGRRFSDDSSKDAQYVKGVINDFMYFAGQFVVSDVIPIPLLRWLDPQGHLKGMKRVAKEVDTMCEAWIQEHVQRRMREKPGPGQEQDFIDVLLNNRDVMRKAQEEIDNHVGKERWVDETDLKHLVYLQAIVKEGLRLYPPGPLGAPHRAIEDCQVGGYFIPKGTQLLVNVWKLHRDPRVWSEPEKFMPERFLTRQAEVDVFGHHFELLPFGSGRRACPGITFAVQVMHLTVARLLQGFDMTTPSNLPVDMTEGPGVTMPKAHPVEVLMMPRLPSALYEP

[Multiple Choices]
A. neuropeptide signaling pathway
B. regulation of meristem structural organization
C. hair follicle development
D. indole alkaloid biosynthetic process
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

> The exact sequence matches a UniProt entry annotated with indole alkaloid biosynthesis. The entry describes experimental evidence for a role in ajmaline-type monoterpenoid indole alkaloid biosynthesis, and its GO annotation is supported by IDA evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a membrane-associated cytochrome P450 enzyme, which may suggest enzymatic metabolism, but that general clue does not identify the specific indole alkaloid pathway rather than another process.


**Missing item-specific fact**

> The protein-specific functional assignment that this enzyme catalyzes a step in indole alkaloid biosynthesis.


**Reason**

> Choosing D requires knowing the particular substrate, product, or pathway role of this protein. That information is not supplied by the sequence or choices alone; recognizing the sequence or retrieving its annotation would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Reviewer evidence supports D for this sequence; the other listed options are not comparably supported by the supplied evidence.


### Important caveats

- The sequence match is exact, and a historical UniProt record available by the stated cutoff also carries the GO annotation.
- The author's precise source snapshot is unknown; the reviewer-only annotation establishes support for the key but was absent from the evaluated input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450 enzyme, which may suggest enzymatic metabolism, but that general clue does not identify the specific indole alkaloid pathway rather than another process.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that this enzyme catalyzes a step in indole alkaloid biosynthesis.",
    "reason": "Choosing D requires knowing the particular substrate, product, or pathway role of this protein. That information is not supplied by the sequence or choices alone; recognizing the sequence or retrieving its annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "GO_biological_process_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with indole alkaloid biosynthesis. The entry describes experimental evidence for a role in ajmaline-type monoterpenoid indole alkaloid biosynthesis, and its GO annotation is supported by IDA evidence."
  },
  "important_caveats": [
    "The sequence match is exact, and a historical UniProt record available by the stated cutoff also carries the GO annotation.",
    "The author's precise source snapshot is unknown; the reviewer-only annotation establishes support for the key but was absent from the evaluated input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer evidence supports D for this sequence; the other listed options are not comparably supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with indole alkaloid biosynthesis. The entry describes experimental evidence for a role in ajmaline-type monoterpenoid indole alkaloid biosynthesis, and its GO annotation is supported by IDA evidence.",
    "evidence_ids": ["C1", "C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450 enzyme, which may suggest enzymatic metabolism, but that general clue does not identify the specific indole alkaloid pathway rather than another process.",
    "missing_item_specific_fact": "The protein-specific functional assignment that this enzyme catalyzes a step in indole alkaloid biosynthesis.",
    "reason": "Choosing D requires knowing the particular substrate, product, or pathway role of this protein. That information is not supplied by the sequence or choices alone; recognizing the sequence or retrieving its annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer evidence supports D for this sequence; the other listed options are not comparably supported by the supplied evidence."
  },
  "important_caveats": [
    "The sequence match is exact, and a historical UniProt record available by the stated cutoff also carries the GO annotation.",
    "The author's precise source snapshot is unknown; the reviewer-only annotation establishes support for the key but was absent from the evaluated input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A218NGS0 (Vinorine hydroxylase, CYP5437/CYP82S18 from Rauvolfia serpentina) carries a direct GO annotation GO:0035835 'indole alkaloid biosynthetic process' with evidence code IDA (Inferred from Direct Assay, PubMed:28654178). The FUNCTION comment confirms it catalyzes hydroxylation of vinorine to vomilenine, an intermediate in ajmaline (a monoterpenoid indole alkaloid) biosynthesis. The PATHWAY comment states 'Alkaloid biosynthesis; ajmaline biosynthesis.' The sequence matches exactly (SHA-256 confirmed). Ajmaline is a well-characterized indole alkaloid, so the GO term assignment is experimentally supported.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif (FGSGRRACPG, matching FxxGxRxCxG), identifying it as a P450 monooxygenase. P450s are catalytic biosynthetic enzymes, not neuropeptides or GPCR ligands, which eliminates option A (neuropeptide signaling pathway). The sequence lacks animal-specific features and the overall composition is consistent with a plant protein, eliminating option C (hair follicle development, an animal-specific process). Between the remaining plant options B and D: P450s catalyze chemical transformations (hydroxylations, oxidations) in biosynthetic pathways rather than directly regulating developmental architecture. 'Regulation of meristem structural organization' (B) describes a developmental regulatory process, not a catalytic biosynthetic step. A P450 in plant secondary metabolism is annotated to its biosynthetic pathway, not to a developmental regulation term. This reasoning chain (P450 → biosynthetic enzyme → plant secondary metabolism → biosynthetic process) meaningfully distinguishes D from the other options.


**Missing item-specific fact**

> The specific 'indole' qualifier in 'indole alkaloid biosynthetic process' cannot be deduced from the P450 heme motif alone; it requires knowledge that this particular CYP82-family enzyme acts on monoterpenoid indole alkaloid intermediates (vinorine/vomilenine). However, among the four given options, only D is a biosynthetic process, so the broader reasoning still selects D uniquely.


**Reason**

> The P450 heme-binding motif is identifiable from the sequence. The elimination of animal-specific options (A, C) and the developmental-regulation option (B) follows from general biological knowledge about P450 function and organism context. The specific 'indole' designation requires domain knowledge of the CYP82 family's role in alkaloid biosynthesis, but within the constrained four-option set, the reasoning chain is sufficient to select D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are animal-specific processes incompatible with a plant P450. Option B describes developmental regulation rather than enzymatic biosynthesis. Option D is the only biosynthetic process among the choices, consistent with the catalytic nature of a P450. No two options are equally defensible given the sequence evidence.


### Important caveats

- The specific 'indole alkaloid' designation requires knowledge of the CYP82 family's substrate specificity in plant secondary metabolism; the P450 motif alone identifies the enzyme class but not the substrate class.
- The GO annotation evidence code is IDA (direct experimental assay from PubMed:28654178), providing strong experimental support for the annotation.
- The sequence is 480 amino acids from Rauvolfia serpentina, a well-known source of monoterpenoid indole alkaloids (reserpine, ajmaline, etc.), which provides contextual support for the alkaloid biosynthesis annotation.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what could be inferred from the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FGSGRRACPG, matching FxxGxRxCxG), identifying it as a P450 monooxygenase. P450s are catalytic biosynthetic enzymes, not neuropeptides or GPCR ligands, which eliminates option A (neuropeptide signaling pathway). The sequence lacks animal-specific features and the overall composition is consistent with a plant protein, eliminating option C (hair follicle development, an animal-specific process). Between the remaining plant options B and D: P450s catalyze chemical transformations (hydroxylations, oxidations) in biosynthetic pathways rather than directly regulating developmental architecture. 'Regulation of meristem structural organization' (B) describes a developmental regulatory process, not a catalytic biosynthetic step. A P450 in plant secondary metabolism is annotated to its biosynthetic pathway, not to a developmental regulation term. This reasoning chain (P450 → biosynthetic enzyme → plant secondary metabolism → biosynthetic process) meaningfully distinguishes D from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific 'indole' qualifier in 'indole alkaloid biosynthetic process' cannot be deduced from the P450 heme motif alone; it requires knowledge that this particular CYP82-family enzyme acts on monoterpenoid indole alkaloid intermediates (vinorine/vomilenine). However, among the four given options, only D is a biosynthetic process, so the broader reasoning still selects D uniquely.",
    "reason": "The P450 heme-binding motif is identifiable from the sequence. The elimination of animal-specific options (A, C) and the developmental-regulation option (B) follows from general biological knowledge about P450 function and organism context. The specific 'indole' designation requires domain knowledge of the CYP82 family's role in alkaloid biosynthesis, but within the constrained four-option set, the reasoning chain is sufficient to select D."
  },
  "case_id": "GO_biological_process_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H4",
      "H5",
      "H6",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A218NGS0 (Vinorine hydroxylase, CYP5437/CYP82S18 from Rauvolfia serpentina) carries a direct GO annotation GO:0035835 'indole alkaloid biosynthetic process' with evidence code IDA (Inferred from Direct Assay, PubMed:28654178). The FUNCTION comment confirms it catalyzes hydroxylation of vinorine to vomilenine, an intermediate in ajmaline (a monoterpenoid indole alkaloid) biosynthesis. The PATHWAY comment states 'Alkaloid biosynthesis; ajmaline biosynthesis.' The sequence matches exactly (SHA-256 confirmed). Ajmaline is a well-characterized indole alkaloid, so the GO term assignment is experimentally supported."
  },
  "important_caveats": [
    "The specific 'indole alkaloid' designation requires knowledge of the CYP82 family's substrate specificity in plant secondary metabolism; the P450 motif alone identifies the enzyme class but not the substrate class.",
    "The GO annotation evidence code is IDA (direct experimental assay from PubMed:28654178), providing strong experimental support for the annotation.",
    "The sequence is 480 amino acids from Rauvolfia serpentina, a well-known source of monoterpenoid indole alkaloids (reserpine, ajmaline, etc.), which provides contextual support for the alkaloid biosynthesis annotation.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what could be inferred from the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are animal-specific processes incompatible with a plant P450. Option B describes developmental regulation rather than enzymatic biosynthesis. Option D is the only biosynthetic process among the choices, consistent with the catalytic nature of a P450. No two options are equally defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A218NGS0 (Vinorine hydroxylase, CYP5437/CYP82S18 from Rauvolfia serpentina) carries a direct GO annotation GO:0035835 'indole alkaloid biosynthetic process' with evidence code IDA (Inferred from Direct Assay, PubMed:28654178). The FUNCTION comment confirms it catalyzes hydroxylation of vinorine to vomilenine, an intermediate in ajmaline (a monoterpenoid indole alkaloid) biosynthesis. The PATHWAY comment states 'Alkaloid biosynthesis; ajmaline biosynthesis.' The sequence matches exactly (SHA-256 confirmed). Ajmaline is a well-characterized indole alkaloid, so the GO term assignment is experimentally supported.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "C7", "H1", "H4", "H5", "H6", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FGSGRRACPG, matching FxxGxRxCxG), identifying it as a P450 monooxygenase. P450s are catalytic biosynthetic enzymes, not neuropeptides or GPCR ligands, which eliminates option A (neuropeptide signaling pathway). The sequence lacks animal-specific features and the overall composition is consistent with a plant protein, eliminating option C (hair follicle development, an animal-specific process). Between the remaining plant options B and D: P450s catalyze chemical transformations (hydroxylations, oxidations) in biosynthetic pathways rather than directly regulating developmental architecture. 'Regulation of meristem structural organization' (B) describes a developmental regulatory process, not a catalytic biosynthetic step. A P450 in plant secondary metabolism is annotated to its biosynthetic pathway, not to a developmental regulation term. This reasoning chain (P450 → biosynthetic enzyme → plant secondary metabolism → biosynthetic process) meaningfully distinguishes D from the other options.",
    "missing_item_specific_fact": "The specific 'indole' qualifier in 'indole alkaloid biosynthetic process' cannot be deduced from the P450 heme motif alone; it requires knowledge that this particular CYP82-family enzyme acts on monoterpenoid indole alkaloid intermediates (vinorine/vomilenine). However, among the four given options, only D is a biosynthetic process, so the broader reasoning still selects D uniquely.",
    "reason": "The P450 heme-binding motif is identifiable from the sequence. The elimination of animal-specific options (A, C) and the developmental-regulation option (B) follows from general biological knowledge about P450 function and organism context. The specific 'indole' designation requires domain knowledge of the CYP82 family's role in alkaloid biosynthesis, but within the constrained four-option set, the reasoning chain is sufficient to select D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are animal-specific processes incompatible with a plant P450. Option B describes developmental regulation rather than enzymatic biosynthesis. Option D is the only biosynthetic process among the choices, consistent with the catalytic nature of a P450. No two options are equally defensible given the sequence evidence."
  },
  "important_caveats": [
    "The specific 'indole alkaloid' designation requires knowledge of the CYP82 family's substrate specificity in plant secondary metabolism; the P450 motif alone identifies the enzyme class but not the substrate class.",
    "The GO annotation evidence code is IDA (direct experimental assay from PubMed:28654178), providing strong experimental support for the annotation.",
    "The sequence is 480 amino acids from Rauvolfia serpentina, a well-known source of monoterpenoid indole alkaloids (reserpine, ajmaline, etc.), which provides contextual support for the alkaloid biosynthesis annotation.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what could be inferred from the sequence and general biological knowledge."
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

**Accession:** `A0A218NGS0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
"A0A218NGS0"
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"commonName":"Serpentine wood","lineage":["Eukaryota","Viridiplantae","Streptophyta","Embryophyta","Tracheophyta","Spermatophyta","Magnoliopsida","eudicotyledons","Gunneridae","Pentapetalae","asterids","lamiids","Gentianales","Apocynaceae","Rauvolfioideae","Vinceae","Rauvolfiinae","Rauvolfia"],"scientificName":"Rauvolfia serpentina","synonyms":["Ophioxylon serpentinum"],"taxonId":4060}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"ASG81458.1","source":"EMBL"}],"value":"Cytochrome P450 5437"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"ASG81458.1","source":"EMBL"}],"value":"RsCYP5437"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"}],"value":"Cytochrome P450 82S18"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"}],"value":"Perakine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"}],"value":"Vomilenine isomerase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28654178","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.14.14.104"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Vinorine hydroxylase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsVH"}]}}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28654178","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"A cytochrome P450 monooxygenase involved in the biosynthesis of ajmaline-type monoterpenoid indole alkaloids (MIAs) natural products, important plant-derived pharmaceuticals used in the therapy of heart disorders (PubMed:28654178, PubMed:38212296). Catalyzes the hydroxylation of vinorine to vomilenine, an intermediate chemical in the biosynthesis of ajmaline (PubMed:28654178, PubMed:38212296). Supports also vomilenine isomerization to perakine (PubMed:28654178)"}]}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28654178","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"28654178","source":"PubMed"}],"id":"GO:0035835","properties":[{"key":"GoTerm","value":"P:indole alkaloid biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 1-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
ID   VINHY_RAUSE             Reviewed;         480 AA.
AC   A0A218NGS0;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-SEP-2017, sequence version 1.
DT   28-JAN-2026, entry version 26.
DE   RecName: Full=Vinorine hydroxylase {ECO:0000303|PubMed:28654178, ECO:0000303|PubMed:38212296};
DE            Short=RsVH {ECO:0000303|PubMed:38212296};
DE            EC=1.14.14.104 {ECO:0000269|PubMed:28654178, ECO:0000269|PubMed:38212296};
DE   AltName: Full=Cytochrome P450 5437 {ECO:0000312|EMBL:ASG81458.1};
DE            Short=RsCYP5437 {ECO:0000312|EMBL:ASG81458.1};
DE   AltName: Full=Cytochrome P450 82S18 {ECO:0000303|PubMed:28654178};
DE   AltName: Full=Perakine synthase {ECO:0000303|PubMed:28654178};
DE            Short=Vomilenine isomerase {ECO:0000303|PubMed:28654178};
GN   Name=VH {ECO:0000303|PubMed:28654178, ECO:0000303|PubMed:38212296};
GN   Synonyms=CYP5437 {ECO:0000312|EMBL:ASG81458.1},
GN   CYP82S18 {ECO:0000303|PubMed:28654178};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 38-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
CC   -!- FUNCTION: A cytochrome P450 monooxygenase involved in the biosynthesis
CC       of ajmaline-type monoterpenoid indole alkaloids (MIAs) natural
CC       products, important plant-derived pharmaceuticals used in the therapy
CC       of heart disorders (PubMed:28654178, PubMed:38212296). Catalyzes the
CC       hydroxylation of vinorine to vomilenine, an intermediate chemical in
CC       the biosynthesis of ajmaline (PubMed:28654178, PubMed:38212296).
CC       Supports also vomilenine isomerization to perakine (PubMed:28654178).
CC       {ECO:0000269|PubMed:28654178, ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 78-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:28654178, ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 112-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
DR   GO; GO:0035835; P:indole alkaloid biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

### Evidence GO4

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
