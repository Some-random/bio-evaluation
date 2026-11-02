# GO_cellular_component_0050

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — plasma membrane

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
A. NF-kappaB p50/p65 complex
B. primosome complex
C. myelin sheath
D. plasma membrane
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence match has a UniProt cell-membrane annotation and a GO plasma-membrane annotation. These are inferential/transferred annotations, not direct experimental localization evidence, but they support choice D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long hydrophobic segments consistent with a seven-transmembrane receptor. That architecture supports a membrane protein and, among these choices, makes plasma membrane much more plausible than the listed protein complexes or myelin sheath.


**Missing item-specific fact**

> Direct experimental localization would establish the protein's native distribution more firmly; it is not necessary to distinguish these choices from the sequence's receptor-like membrane architecture.


**Reason**

> The supplied sequence provides a concrete biological basis for selecting D without needing to recognize the exact protein or retrieve its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are sufficiently distinct for the sequence's multi-pass receptor architecture to favor plasma membrane.


### Important caveats

- The reviewer-only UniProt cell-membrane annotation is transferred, and the GO plasma-membrane annotation is inferred; neither excerpt establishes direct experimental localization.
- Sequence architecture supports membrane association but does not by itself prove the precise native compartment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic segments consistent with a seven-transmembrane receptor. That architecture supports a membrane protein and, among these choices, makes plasma membrane much more plausible than the listed protein complexes or myelin sheath.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Direct experimental localization would establish the protein's native distribution more firmly; it is not necessary to distinguish these choices from the sequence's receptor-like membrane architecture.",
    "reason": "The supplied sequence provides a concrete biological basis for selecting D without needing to recognize the exact protein or retrieve its database entry."
  },
  "case_id": "GO_cellular_component_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt cell-membrane annotation and a GO plasma-membrane annotation. These are inferential/transferred annotations, not direct experimental localization evidence, but they support choice D."
  },
  "important_caveats": [
    "The reviewer-only UniProt cell-membrane annotation is transferred, and the GO plasma-membrane annotation is inferred; neither excerpt establishes direct experimental localization.",
    "Sequence architecture supports membrane association but does not by itself prove the precise native compartment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are sufficiently distinct for the sequence's multi-pass receptor architecture to favor plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt cell-membrane annotation and a GO plasma-membrane annotation. These are inferential/transferred annotations, not direct experimental localization evidence, but they support choice D.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic segments consistent with a seven-transmembrane receptor. That architecture supports a membrane protein and, among these choices, makes plasma membrane much more plausible than the listed protein complexes or myelin sheath.",
    "missing_item_specific_fact": "Direct experimental localization would establish the protein's native distribution more firmly; it is not necessary to distinguish these choices from the sequence's receptor-like membrane architecture.",
    "reason": "The supplied sequence provides a concrete biological basis for selecting D without needing to recognize the exact protein or retrieve its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are sufficiently distinct for the sequence's multi-pass receptor architecture to favor plasma membrane."
  },
  "important_caveats": [
    "The reviewer-only UniProt cell-membrane annotation is transferred, and the GO plasma-membrane annotation is inferred; neither excerpt establishes direct experimental localization.",
    "Sequence architecture supports membrane association but does not by itself prove the precise native compartment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E7FEL0 (GPR4_DANRE, zebrafish G protein-coupled receptor 4) annotates the protein as 'Cell membrane; Multi-pass membrane protein' (ECO:0000250|UniProtKB:P46093, ECO:0000255) and assigns GO:0005886 (plasma membrane) via ISS/IBA evidence. A 2025 Cryo-EM structure (PDB 8ZFZ, 9J31) of GPR4-Gs complex further confirms membrane localization. The sequence (373 aa) matches the benchmark exactly. The annotation is primarily by sequence similarity to human GPR4 (P46093) rather than direct experimental localization of the zebrafish protein, but the GPCR architecture and structural evidence strongly support plasma membrane localization.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains approximately 7 long hydrophobic stretches (~20-25 residues each) arranged in the canonical 7-transmembrane GPCR topology, including recognizable conserved motifs (a DRY-like motif at the TM3/ICL2 boundary, an NPxxY-like motif 'NPCDC' in TM7). This multi-pass membrane architecture is incompatible with a nuclear transcription factor complex (NF-kB), a DNA replication complex (primosome), or a myelin sheath component. GPCRs are plasma membrane receptors that signal via heterotrimeric G proteins at the cell surface. The absence of nuclear localization signals, DNA-binding domains, helicase/primase motifs, and myelin-specific features (e.g., PLP's highly charged C-terminus, MBP's lysine-rich structure) eliminates all three distractors through general knowledge of protein domain architecture and membrane protein topology.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 7-TM GPCR architecture is recognizable from the sequence itself through hydrophobicity analysis and conserved motif identification. This is standard general biological knowledge about membrane protein topology. The distractors (nuclear complex, replication complex, myelin) are eliminated by the absence of their defining structural features. No item-specific database lookup is required to reach the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different cellular compartments (nuclear complex, replication machinery, extracellular glial structure, plasma membrane). The sequence's clear multi-pass membrane topology with GPCR-like architecture unambiguously points to plasma membrane. No other option is defensible given the sequence features.


### Important caveats

- The GO annotation for this zebrafish protein is primarily by sequence similarity (ISS/IBA) to human GPR4, not direct experimental localization of the zebrafish ortholog. However, the 2025 Cryo-EM structure of the zebrafish GPR4-Gs complex provides strong structural confirmation of membrane localization.
- The sequence similarity-based annotation means the 'plasma membrane' assignment inherits the evidence level of the parent annotation, though GPCR plasma membrane localization is extremely well-established across the superfamily.
- The distractors are notably easy: NF-kB (nuclear), primosome (nuclear/replication), and myelin sheath (extracellular glial) are all incompatible with a 7-TM membrane receptor, making this a relatively straightforward reasoning task.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains approximately 7 long hydrophobic stretches (~20-25 residues each) arranged in the canonical 7-transmembrane GPCR topology, including recognizable conserved motifs (a DRY-like motif at the TM3/ICL2 boundary, an NPxxY-like motif 'NPCDC' in TM7). This multi-pass membrane architecture is incompatible with a nuclear transcription factor complex (NF-kB), a DNA replication complex (primosome), or a myelin sheath component. GPCRs are plasma membrane receptors that signal via heterotrimeric G proteins at the cell surface. The absence of nuclear localization signals, DNA-binding domains, helicase/primase motifs, and myelin-specific features (e.g., PLP's highly charged C-terminus, MBP's lysine-rich structure) eliminates all three distractors through general knowledge of protein domain architecture and membrane protein topology.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM GPCR architecture is recognizable from the sequence itself through hydrophobicity analysis and conserved motif identification. This is standard general biological knowledge about membrane protein topology. The distractors (nuclear complex, replication complex, myelin) are eliminated by the absence of their defining structural features. No item-specific database lookup is required to reach the answer."
  },
  "case_id": "GO_cellular_component_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E7FEL0 (GPR4_DANRE, zebrafish G protein-coupled receptor 4) annotates the protein as 'Cell membrane; Multi-pass membrane protein' (ECO:0000250|UniProtKB:P46093, ECO:0000255) and assigns GO:0005886 (plasma membrane) via ISS/IBA evidence. A 2025 Cryo-EM structure (PDB 8ZFZ, 9J31) of GPR4-Gs complex further confirms membrane localization. The sequence (373 aa) matches the benchmark exactly. The annotation is primarily by sequence similarity to human GPR4 (P46093) rather than direct experimental localization of the zebrafish protein, but the GPCR architecture and structural evidence strongly support plasma membrane localization."
  },
  "important_caveats": [
    "The GO annotation for this zebrafish protein is primarily by sequence similarity (ISS/IBA) to human GPR4, not direct experimental localization of the zebrafish ortholog. However, the 2025 Cryo-EM structure of the zebrafish GPR4-Gs complex provides strong structural confirmation of membrane localization.",
    "The sequence similarity-based annotation means the 'plasma membrane' assignment inherits the evidence level of the parent annotation, though GPCR plasma membrane localization is extremely well-established across the superfamily.",
    "The distractors are notably easy: NF-kB (nuclear), primosome (nuclear/replication), and myelin sheath (extracellular glial) are all incompatible with a 7-TM membrane receptor, making this a relatively straightforward reasoning task."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different cellular compartments (nuclear complex, replication machinery, extracellular glial structure, plasma membrane). The sequence's clear multi-pass membrane topology with GPCR-like architecture unambiguously points to plasma membrane. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E7FEL0 (GPR4_DANRE, zebrafish G protein-coupled receptor 4) annotates the protein as 'Cell membrane; Multi-pass membrane protein' (ECO:0000250|UniProtKB:P46093, ECO:0000255) and assigns GO:0005886 (plasma membrane) via ISS/IBA evidence. A 2025 Cryo-EM structure (PDB 8ZFZ, 9J31) of GPR4-Gs complex further confirms membrane localization. The sequence (373 aa) matches the benchmark exactly. The annotation is primarily by sequence similarity to human GPR4 (P46093) rather than direct experimental localization of the zebrafish protein, but the GPCR architecture and structural evidence strongly support plasma membrane localization.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains approximately 7 long hydrophobic stretches (~20-25 residues each) arranged in the canonical 7-transmembrane GPCR topology, including recognizable conserved motifs (a DRY-like motif at the TM3/ICL2 boundary, an NPxxY-like motif 'NPCDC' in TM7). This multi-pass membrane architecture is incompatible with a nuclear transcription factor complex (NF-kB), a DNA replication complex (primosome), or a myelin sheath component. GPCRs are plasma membrane receptors that signal via heterotrimeric G proteins at the cell surface. The absence of nuclear localization signals, DNA-binding domains, helicase/primase motifs, and myelin-specific features (e.g., PLP's highly charged C-terminus, MBP's lysine-rich structure) eliminates all three distractors through general knowledge of protein domain architecture and membrane protein topology.",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM GPCR architecture is recognizable from the sequence itself through hydrophobicity analysis and conserved motif identification. This is standard general biological knowledge about membrane protein topology. The distractors (nuclear complex, replication complex, myelin) are eliminated by the absence of their defining structural features. No item-specific database lookup is required to reach the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different cellular compartments (nuclear complex, replication machinery, extracellular glial structure, plasma membrane). The sequence's clear multi-pass membrane topology with GPCR-like architecture unambiguously points to plasma membrane. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO annotation for this zebrafish protein is primarily by sequence similarity (ISS/IBA) to human GPR4, not direct experimental localization of the zebrafish ortholog. However, the 2025 Cryo-EM structure of the zebrafish GPR4-Gs complex provides strong structural confirmation of membrane localization.",
    "The sequence similarity-based annotation means the 'plasma membrane' assignment inherits the evidence level of the parent annotation, though GPCR plasma membrane localization is extremely well-established across the superfamily.",
    "The distractors are notably easy: NF-kB (nuclear), primosome (nuclear/replication), and myelin sheath (extracellular glial) are all incompatible with a 7-TM membrane receptor, making this a relatively straightforward reasoning task."
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
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P46093","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/uniProtKBCrossReferences/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"citation":{"authors":["Ma Y.","Wang Y.","Tang M.","Weng Y.","Chen Y.","Xu Y.","An S.","Wu Y.","Zhao S.","Xu H.","Li D.","Liu M.","Lu W.","Ru H.","Song G."],"citationCrossReferences":[{"database":"PubMed","id":"39799123"},{"database":"DOI","id":"10.1038/s41467-025-55901-2"}],"citationType":"journal article","firstPage":"605","id":"39799123","journal":"Nat. Commun.","lastPage":"605","publicationDate":"2025","title":"Cryo-EM structure of an activated GPR4-Gs signaling complex.","volume":"16"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"referenceNumber":2,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (3.05 ANGSTROMS) OF 2-360 IN COMPLEX WITH GNAS","FUNCTION","MUTAGENESIS OF GLN-53; ASN-58; GLU-59; ASP-71; HIS-87; ASP-89; TYR-106; TYR-110; ARG-123; ARG-137; 164-ASP-GLU-165; HIS-173; GLU-178; ASN-219; GLU-226; TYR-248; TYR-276; HIS-277; ASP-290 AND GLU-299"]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 78-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P46093};
CC       Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 117-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IBA:GO_Central.
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
