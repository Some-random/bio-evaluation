# GO_biological_process_0105

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — G protein-coupled receptor signaling pathway

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASLRGSETMCNITTSCNVDSNIDQFFQPTLYIIVIVLGFPTNCMALWAAYMQVKQKNELGIYLMNLSIADLLYITTLPLWIDYFVHHDNWIHGQVSCKLFGFIFYTNIYVSIAFLCCISVDRYLAVAHPLKFAKVRRVKTALLVSAIVWLTEIVANSAPLFHDELFQDRFNHTFCFEKYPMEPWVAGMNLYRTFLGFLAPWGIMLAAYRGILRAVRGNVSTERQEKAKIKRLALSLILIVLLCFAPYHVLLLWRSVLFLINPCDCGGEENLFGAYHVTLALTSLNCVADPILYCFVNEGARHDVGRALATLLGLFQRGKSPETLMGASITVETPLAVKKPDFYSEVKTNAYKNDIEVLKDECLQMTILSVKK

[Multiple Choices]
A. G protein-coupled receptor signaling pathway
B. response to parathyroid hormone
C. regulation of DNA replication
D. negative regulation of apoptotic process in bone marrow cell
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

> The matched sequence is annotated as a GPCR, and the record describes G-protein signaling and experimentally supported GPCR-pathway annotations. A is the broader pathway term; the more specific adenylate-cyclase-activating pathway is also a subtype of it.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the characteristic multiple-transmembrane-helix architecture of a GPCR. Among the choices, GPCR signaling is the biologically direct match; the other options describe DNA replication regulation, a specific hormone response, or apoptosis regulation in bone marrow.


**Missing item-specific fact**

> The receptor's exact identity, ligand, and experimentally established signaling behavior are not provided; those would be needed to establish its specific function independently, but are not necessary to distinguish the broad GPCR option from these distractors.


**Reason**

> The sequence architecture gives a meaningful family-level inference relevant to choice A, rather than requiring recognition of the exact sequence or lookup of its annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is the clear match among the listed choices. The sequence and evidence support a more specific GPCR signaling process as well, but that process falls under option A.


### Important caveats

- A seven-transmembrane architecture supports GPCR-family identification but does not by itself establish a particular ligand or all in vivo biological roles.
- Reviewer-only annotations support the key but were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristic multiple-transmembrane-helix architecture of a GPCR. Among the choices, GPCR signaling is the biologically direct match; the other options describe DNA replication regulation, a specific hormone response, or apoptosis regulation in bone marrow.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The receptor's exact identity, ligand, and experimentally established signaling behavior are not provided; those would be needed to establish its specific function independently, but are not necessary to distinguish the broad GPCR option from these distractors.",
    "reason": "The sequence architecture gives a meaningful family-level inference relevant to choice A, rather than requiring recognition of the exact sequence or lookup of its annotation."
  },
  "case_id": "GO_biological_process_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C8",
      "H3",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a GPCR, and the record describes G-protein signaling and experimentally supported GPCR-pathway annotations. A is the broader pathway term; the more specific adenylate-cyclase-activating pathway is also a subtype of it."
  },
  "important_caveats": [
    "A seven-transmembrane architecture supports GPCR-family identification but does not by itself establish a particular ligand or all in vivo biological roles.",
    "Reviewer-only annotations support the key but were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the clear match among the listed choices. The sequence and evidence support a more specific GPCR signaling process as well, but that process falls under option A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a GPCR, and the record describes G-protein signaling and experimentally supported GPCR-pathway annotations. A is the broader pathway term; the more specific adenylate-cyclase-activating pathway is also a subtype of it.",
    "evidence_ids": ["C1", "C5", "C8", "H3", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the characteristic multiple-transmembrane-helix architecture of a GPCR. Among the choices, GPCR signaling is the biologically direct match; the other options describe DNA replication regulation, a specific hormone response, or apoptosis regulation in bone marrow.",
    "missing_item_specific_fact": "The receptor's exact identity, ligand, and experimentally established signaling behavior are not provided; those would be needed to establish its specific function independently, but are not necessary to distinguish the broad GPCR option from these distractors.",
    "reason": "The sequence architecture gives a meaningful family-level inference relevant to choice A, rather than requiring recognition of the exact sequence or lookup of its annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the clear match among the listed choices. The sequence and evidence support a more specific GPCR signaling process as well, but that process falls under option A."
  },
  "important_caveats": [
    "A seven-transmembrane architecture supports GPCR-family identification but does not by itself establish a particular ligand or all in vivo biological roles.",
    "Reviewer-only annotations support the key but were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence is an exact match to UniProt E7FEL0 (GPR4_DANRE), annotated as 'G protein-coupled receptor 4' with experimental (IDA) evidence for GO:0007186 'G protein-coupled receptor signaling pathway' (PubMed:25576873, PubMed:28270026) and GO:0007189 'adenylate cyclase-activating G protein-coupled receptor signaling pathway' (PubMed:39799123). The FUNCTION comment explicitly states it is a 'Proton-sensing G protein-coupled receptor' that 'triggers signaling via guanine nucleotide-binding proteins (G proteins).' Option A (GO:0007186) is the parent term of GO:0007189 and is directly annotated with IDA evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 373-aa sequence contains multiple hydrophobic stretches (~20-25 residues) consistent with seven transmembrane helices, and critically contains the 'DRY' motif (ISVDRYLAVAHPLK) in the putative third intracellular loop, a well-known hallmark of class A (rhodopsin-like) GPCRs. This architecture is incompatible with options C (DNA replication, a nuclear process) and D (bone marrow apoptosis regulation), which involve soluble/nuclear proteins. Option B (response to parathyroid hormone) is a specific ligand-dependent annotation requiring knowledge of the PTH receptor (a class B GPCR with distinct sequence features), whereas option A is the general pathway encompassing all GPCRs. From sequence architecture alone, one can identify a 7-TM/DRY-motif protein and assign it to the general GPCR signaling pathway.


**Missing item-specific fact**

> None strictly required. The 7-TM topology and DRY motif are recognizable from the sequence through general structural biology knowledge, and the distractors C and D are clearly eliminable for a membrane receptor. Distinguishing A from B does not require knowing the exact ligand; A is the general pathway for any GPCR, while B is a specific hormonal response not inferable from sequence alone.


**Reason**

> The sequence provides identifiable structural hallmarks (7 hydrophobic TM segments, DRY motif, extracellular cysteines) that are standard textbook features of class A GPCRs. General biological knowledge allows assignment to the GPCR signaling pathway and elimination of DNA replication and bone-marrow apoptosis options. The parathyroid hormone option requires specific ligand knowledge not derivable from the sequence, making A the uniquely defensible general answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A (GO:0007186) is the general GPCR pathway and is the parent of the more specific annotation GO:0007189. Options C and D are incompatible with a 7-TM membrane receptor. Option B (parathyroid hormone response) would require the PTH receptor (class B GPCR, PTHR1), which has a distinctly different sequence architecture (larger extracellular N-terminal domain, different TM topology). No other option is defensible.


### Important caveats

- The UniProt entry was first publicly released on 2025-06-18 (entry version 99 at historical cutoff), meaning the detailed functional annotation (PubMed:39799123, cryo-EM structure) postdates the likely benchmark construction. However, the protein name 'G protein-coupled receptor 4' and basic GPCR identity were available from the 2011 sequence deposition.
- The GO:0007186 annotation has IDA evidence from PubMed:25576873 and PubMed:28270026 (ZFIN), which predate the benchmark cutoff, confirming the GPCR pathway assignment was established before the 2025 cryo-EM paper.
- The sequence-to-GPCR identification relies on pattern recognition of 7-TM architecture and the DRY motif, which is standard knowledge but requires careful inspection of a raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 373-aa sequence contains multiple hydrophobic stretches (~20-25 residues) consistent with seven transmembrane helices, and critically contains the 'DRY' motif (ISVDRYLAVAHPLK) in the putative third intracellular loop, a well-known hallmark of class A (rhodopsin-like) GPCRs. This architecture is incompatible with options C (DNA replication, a nuclear process) and D (bone marrow apoptosis regulation), which involve soluble/nuclear proteins. Option B (response to parathyroid hormone) is a specific ligand-dependent annotation requiring knowledge of the PTH receptor (a class B GPCR with distinct sequence features), whereas option A is the general pathway encompassing all GPCRs. From sequence architecture alone, one can identify a 7-TM/DRY-motif protein and assign it to the general GPCR signaling pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The 7-TM topology and DRY motif are recognizable from the sequence through general structural biology knowledge, and the distractors C and D are clearly eliminable for a membrane receptor. Distinguishing A from B does not require knowing the exact ligand; A is the general pathway for any GPCR, while B is a specific hormonal response not inferable from sequence alone.",
    "reason": "The sequence provides identifiable structural hallmarks (7 hydrophobic TM segments, DRY motif, extracellular cysteines) that are standard textbook features of class A GPCRs. General biological knowledge allows assignment to the GPCR signaling pathway and elimination of DNA replication and bone-marrow apoptosis options. The parathyroid hormone option requires specific ligand knowledge not derivable from the sequence, making A the uniquely defensible general answer."
  },
  "case_id": "GO_biological_process_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence is an exact match to UniProt E7FEL0 (GPR4_DANRE), annotated as 'G protein-coupled receptor 4' with experimental (IDA) evidence for GO:0007186 'G protein-coupled receptor signaling pathway' (PubMed:25576873, PubMed:28270026) and GO:0007189 'adenylate cyclase-activating G protein-coupled receptor signaling pathway' (PubMed:39799123). The FUNCTION comment explicitly states it is a 'Proton-sensing G protein-coupled receptor' that 'triggers signaling via guanine nucleotide-binding proteins (G proteins).' Option A (GO:0007186) is the parent term of GO:0007189 and is directly annotated with IDA evidence."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-06-18 (entry version 99 at historical cutoff), meaning the detailed functional annotation (PubMed:39799123, cryo-EM structure) postdates the likely benchmark construction. However, the protein name 'G protein-coupled receptor 4' and basic GPCR identity were available from the 2011 sequence deposition.",
    "The GO:0007186 annotation has IDA evidence from PubMed:25576873 and PubMed:28270026 (ZFIN), which predate the benchmark cutoff, confirming the GPCR pathway assignment was established before the 2025 cryo-EM paper.",
    "The sequence-to-GPCR identification relies on pattern recognition of 7-TM architecture and the DRY motif, which is standard knowledge but requires careful inspection of a raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (GO:0007186) is the general GPCR pathway and is the parent of the more specific annotation GO:0007189. Options C and D are incompatible with a 7-TM membrane receptor. Option B (parathyroid hormone response) would require the PTH receptor (class B GPCR, PTHR1), which has a distinctly different sequence architecture (larger extracellular N-terminal domain, different TM topology). No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence is an exact match to UniProt E7FEL0 (GPR4_DANRE), annotated as 'G protein-coupled receptor 4' with experimental (IDA) evidence for GO:0007186 'G protein-coupled receptor signaling pathway' (PubMed:25576873, PubMed:28270026) and GO:0007189 'adenylate cyclase-activating G protein-coupled receptor signaling pathway' (PubMed:39799123). The FUNCTION comment explicitly states it is a 'Proton-sensing G protein-coupled receptor' that 'triggers signaling via guanine nucleotide-binding proteins (G proteins).' Option A (GO:0007186) is the parent term of GO:0007189 and is directly annotated with IDA evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 373-aa sequence contains multiple hydrophobic stretches (~20-25 residues) consistent with seven transmembrane helices, and critically contains the 'DRY' motif (ISVDRYLAVAHPLK) in the putative third intracellular loop, a well-known hallmark of class A (rhodopsin-like) GPCRs. This architecture is incompatible with options C (DNA replication, a nuclear process) and D (bone marrow apoptosis regulation), which involve soluble/nuclear proteins. Option B (response to parathyroid hormone) is a specific ligand-dependent annotation requiring knowledge of the PTH receptor (a class B GPCR with distinct sequence features), whereas option A is the general pathway encompassing all GPCRs. From sequence architecture alone, one can identify a 7-TM/DRY-motif protein and assign it to the general GPCR signaling pathway.",
    "missing_item_specific_fact": "None strictly required. The 7-TM topology and DRY motif are recognizable from the sequence through general structural biology knowledge, and the distractors C and D are clearly eliminable for a membrane receptor. Distinguishing A from B does not require knowing the exact ligand; A is the general pathway for any GPCR, while B is a specific hormonal response not inferable from sequence alone.",
    "reason": "The sequence provides identifiable structural hallmarks (7 hydrophobic TM segments, DRY motif, extracellular cysteines) that are standard textbook features of class A GPCRs. General biological knowledge allows assignment to the GPCR signaling pathway and elimination of DNA replication and bone-marrow apoptosis options. The parathyroid hormone option requires specific ligand knowledge not derivable from the sequence, making A the uniquely defensible general answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (GO:0007186) is the general GPCR pathway and is the parent of the more specific annotation GO:0007189. Options C and D are incompatible with a 7-TM membrane receptor. Option B (parathyroid hormone response) would require the PTH receptor (class B GPCR, PTHR1), which has a distinctly different sequence architecture (larger extracellular N-terminal domain, different TM topology). No other option is defensible."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-06-18 (entry version 99 at historical cutoff), meaning the detailed functional annotation (PubMed:39799123, cryo-EM structure) postdates the likely benchmark construction. However, the protein name 'G protein-coupled receptor 4' and basic GPCR identity were available from the 2011 sequence deposition.",
    "The GO:0007186 annotation has IDA evidence from PubMed:25576873 and PubMed:28270026 (ZFIN), which predate the benchmark cutoff, confirming the GPCR pathway assignment was established before the 2025 cryo-EM paper.",
    "The sequence-to-GPCR identification relies on pattern recognition of 7-TM architecture and the DRY motif, which is standard knowledge but requires careful inspection of a raw sequence."
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

**Accession:** `E7FEL0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 99. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
"E7FEL0"
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39799123","source":"PubMed"}],"value":"G protein-coupled receptor 4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39799123","source":"PubMed"}],"value":"zGPR4"}]}}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39799123","source":"PubMed"}],"value":"Proton-sensing G protein-coupled receptor activated by extracellular pH, which is required to monitor pH changes and generate adaptive reactions (PubMed:39799123). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase (PubMed:39799123). GPR4 is mainly coupled to G(s) G proteins and mediates activation of adenylate cyclase activity (PubMed:39799123)"}]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/uniProtKBCrossReferences/35`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39799123","source":"PubMed"}],"id":"GO:0007189","properties":[{"key":"GoTerm","value":"P:adenylate cyclase-activating G protein-coupled receptor signaling pathway"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/uniProtKBCrossReferences/37`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"25576873","source":"PubMed"},{"evidenceCode":"ECO:0000314","id":"28270026","source":"PubMed"}],"id":"GO:0007186","properties":[{"key":"GoTerm","value":"P:G protein-coupled receptor signaling pathway"},{"key":"GoEvidenceType","value":"IDA:ZFIN"}]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 62-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
CC   -!- FUNCTION: Proton-sensing G-protein coupled receptor activated by
CC       extracellular pH, which is required to monitor pH changes and generate
CC       adaptive reactions (PubMed:39799123). Ligand binding causes a
CC       conformation change that triggers signaling via guanine nucleotide-
CC       binding proteins (G proteins) and modulates the activity of downstream
CC       effectors, such as adenylate cyclase (PubMed:39799123). GPR4 is mainly
CC       coupled to G(s) G proteins and mediates activation of adenylate cyclase
CC       activity (PubMed:39799123). {ECO:0000269|PubMed:39799123}.
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 119-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
DR   GO; GO:0007189; P:adenylate cyclase-activating G protein-coupled receptor signaling pathway; IDA:UniProtKB.
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 121-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
DR   GO; GO:0007186; P:G protein-coupled receptor signaling pathway; IDA:ZFIN.
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 74132-74153`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0007186
name: G protein-coupled receptor signaling pathway
namespace: biological_process
alt_id: GO:0038042
def: "The series of molecular signals initiated by a ligand binding to its receptor, in which the activated receptor promotes the exchange of GDP for GTP on the alpha-subunit of an associated heterotrimeric G-protein complex. The GTP-bound activated alpha-G-protein then dissociates from the beta- and gamma-subunits to further transmit the signal within the cell. The pathway begins with receptor-ligand interaction, and ends with regulation of a downstream cellular process. The pathway can start from the plasma membrane, Golgi or nuclear membrane." [GOC:bf, GOC:mah, PMID:16902576, PMID:24568158, Wikipedia:G_protein-coupled_receptor]
subset: goslim_drosophila
synonym: "dimeric G-protein coupled receptor signaling pathway" NARROW []
synonym: "dimeric G-protein coupled receptor signalling pathway" NARROW [GOC:mah]
synonym: "G protein coupled receptor protein signaling pathway" EXACT []
synonym: "G protein coupled receptor protein signalling pathway" EXACT []
synonym: "G-protein coupled receptor protein signal transduction" EXACT []
synonym: "G-protein coupled receptor protein signaling pathway" EXACT [GOC:bf]
synonym: "G-protein coupled receptor signaling pathway via GPCR dimer" NARROW [GOC:bf]
synonym: "G-protein coupled receptor signalling pathway" EXACT []
synonym: "G-protein-coupled receptor protein signalling pathway" EXACT []
synonym: "GPCR signaling pathway" EXACT []
synonym: "GPCR signalling pathway" EXACT []
xref: Reactome:R-HSA-373076 "Class A/1 (Rhodopsin-like receptors)"
xref: Reactome:R-HSA-388396 "GPCR downstream signalling"
is_a: GO:0007165 ! signal transduction

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 105. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
