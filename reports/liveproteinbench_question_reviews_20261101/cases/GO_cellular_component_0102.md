# GO_cellular_component_0102

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTALDTDTPTAGRSAPLISPGPVIPPPDFGPLDRAQGWAMTAIITALAAITRFLNLGSPTDAGTPIFDEKHYAPQAWQVLHNDGVEDNPGYGLVVHPPVGKQLIAIGEWLFGYNGLGWRFSGAVCGVIIVMLVTRIARRISRSTLVGAIAGLLIIADGVSFVSSRTALLDVFLVMFAVAAFACLMVDRDQVRERMYHAFLDGRIAETRWGTRLGVRWWRFGAGVLLGLACATKWSGLYFVLFFGVMTLVFDAIARKQYHVPHPWRGMLRRDLGPAAYVFGLIPFAVYLASYAPWFASETAVNRYEVGRSIGPDSILPIPDALRSLWHYTHAAYRFHSNLTNADGNHHPWESKPWTWPMSLRPVLYAIDNQDVPGCGAQSCVKAVMLVGTPAMWFIAVPVLGWALWRTVVRRDWRYGAVLVGYMAGFLPWFADIDRQMYFFYATVMAPFLVLAIALILGDILYKPNQNPERRTLGLLTVCFYVALVITNFAWMYPILTGLPISQTTWNLQIWLPSWR

[Multiple Choices]
A. site of double-strand break
B. plasma membrane
C. external side of plasma membrane
D. replisome
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

> The sequence matches a UniProt entry annotated to the cell membrane as a multi-pass membrane protein; its GO annotation is plasma membrane. The evidence is computational or transferred by similarity, not direct experimental localization evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains numerous long hydrophobic stretches consistent with a multi-pass integral membrane protein. That supports plasma membrane over the DNA-damage and replisome choices; the sequence does not suggest a protein located specifically on the membrane’s external side.


**Missing item-specific fact**

> No item-specific database annotation or experimental measurement is needed to distinguish the listed choices at this level.


**Reason**

> The prominent multi-pass membrane signature supplies a concrete biological basis for choosing B. The reviewer-only annotation corroborates the key but is not needed as input to the reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports an integral membrane protein, whereas option C specifies the external side of the membrane rather than the membrane itself.


### Important caveats

- The cited localization annotation is based on similarity to another UniProt entry, and the multi-pass topology annotation is computational.
- The GO term plasma membrane is used for bacterial cell membrane; the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic stretches consistent with a multi-pass integral membrane protein. That supports plasma membrane over the DNA-damage and replisome choices; the sequence does not suggest a protein located specifically on the membrane’s external side.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific database annotation or experimental measurement is needed to distinguish the listed choices at this level.",
    "reason": "The prominent multi-pass membrane signature supplies a concrete biological basis for choosing B. The reviewer-only annotation corroborates the key but is not needed as input to the reasoning."
  },
  "case_id": "GO_cellular_component_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches a UniProt entry annotated to the cell membrane as a multi-pass membrane protein; its GO annotation is plasma membrane. The evidence is computational or transferred by similarity, not direct experimental localization evidence."
  },
  "important_caveats": [
    "The cited localization annotation is based on similarity to another UniProt entry, and the multi-pass topology annotation is computational.",
    "The GO term plasma membrane is used for bacterial cell membrane; the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports an integral membrane protein, whereas option C specifies the external side of the membrane rather than the membrane itself."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches a UniProt entry annotated to the cell membrane as a multi-pass membrane protein; its GO annotation is plasma membrane. The evidence is computational or transferred by similarity, not direct experimental localization evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic stretches consistent with a multi-pass integral membrane protein. That supports plasma membrane over the DNA-damage and replisome choices; the sequence does not suggest a protein located specifically on the membrane’s external side.",
    "missing_item_specific_fact": "No item-specific database annotation or experimental measurement is needed to distinguish the listed choices at this level.",
    "reason": "The prominent multi-pass membrane signature supplies a concrete biological basis for choosing B. The reviewer-only annotation corroborates the key but is not needed as input to the reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports an integral membrane protein, whereas option C specifies the external side of the membrane rather than the membrane itself."
  },
  "important_caveats": [
    "The cited localization annotation is based on similarity to another UniProt entry, and the multi-pass topology annotation is computational.",
    "The GO term plasma membrane is used for bacterial cell membrane; the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0R3E8 (PMT_MYCS2) annotates the protein as 'Cell membrane; Multi-pass membrane protein' (evidence code ECO:0000250, inferred from similarity to P9WN05). The GO cross-reference explicitly assigns GO:0005886 (plasma membrane) with ISS/IEA evidence. GO:0005886 lists 'cell membrane' as an EXACT synonym (GO1). The annotation is computational (sequence-similarity-based) rather than direct experimental, but it is a valid and consistent database annotation. The sequence itself contains numerous hydrophobic stretches consistent with multi-pass membrane topology.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 516-aa sequence contains multiple long hydrophobic segments (e.g., AIITALAAITRFLNLGS, IIVMLVTRIARRISRSTLVGAIAGLLIIADGVSFVSSRTALLDVFLVMFAVAAFACLMV, VLLGLACATKWSGLYFVLFFGVMTLVFDAIARK, and several others) indicative of a multi-pass transmembrane protein. Multi-pass topology means the protein spans the lipid bilayer, making 'plasma membrane' (the whole membrane) the correct compartment rather than 'external side of plasma membrane' (a single leaflet). The enzymatic function (polyprenol-phosphate-mannose transferase) requires a membrane-embedded lipid carrier, further supporting membrane localization. Bacterial origin (Mycolicibacterium smegmatis) and absence of DNA-binding, helicase, or replication machinery motifs exclude replisome (D) and site of double-strand break (A).


**Missing item-specific fact**

> None critical. The multi-pass hydrophobic topology is directly observable in the sequence, and the distinction between 'plasma membrane' and 'external side' follows from the multi-pass (spanning) topology rather than peripheral/external-leaflet-only association.


**Reason**

> A model with general knowledge of transmembrane protein topology, bacterial cell biology, and GO cellular component definitions can reason from the hydrophobic segment count and the transferase function to select plasma membrane over the other options. The B-vs-C distinction is resolved by recognizing that a multi-pass protein is embedded across the bilayer (plasma membrane) rather than restricted to one leaflet (external side).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A (site of double-strand break) and D (replisome) are clearly incompatible with a multi-pass membrane protein lacking any DNA-interaction motifs. C (external side of plasma membrane) is a sub-compartment of B; a multi-pass protein spanning the bilayer is best described by B. The annotation and sequence features unambiguously favor B over C.


### Important caveats

- The UniProt subcellular-location annotation carries evidence code ECO:0000250 (similarity to P9WN05), i.e., it is computational inference, not direct experimental localization.
- The GO assignment is ISS/IEA (inferred from sequence similarity / UniProtKB-SubCell), not an experimentally curated GO annotation.
- The GO ontology definition of 'external side of plasma membrane' (GO2) includes 'any protein embedded in, attached to, or peripherally associated with' the external leaflet, which could in principle encompass a multi-pass protein's external domains; however, the primary and most specific location for a multi-pass protein is the plasma membrane itself.
- The protein is from a bacterium; 'plasma membrane' and 'cell membrane' are synonymous in prokaryotic context (GO1 lists 'cell membrane' as EXACT synonym).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 516-aa sequence contains multiple long hydrophobic segments (e.g., AIITALAAITRFLNLGS, IIVMLVTRIARRISRSTLVGAIAGLLIIADGVSFVSSRTALLDVFLVMFAVAAFACLMV, VLLGLACATKWSGLYFVLFFGVMTLVFDAIARK, and several others) indicative of a multi-pass transmembrane protein. Multi-pass topology means the protein spans the lipid bilayer, making 'plasma membrane' (the whole membrane) the correct compartment rather than 'external side of plasma membrane' (a single leaflet). The enzymatic function (polyprenol-phosphate-mannose transferase) requires a membrane-embedded lipid carrier, further supporting membrane localization. Bacterial origin (Mycolicibacterium smegmatis) and absence of DNA-binding, helicase, or replication machinery motifs exclude replisome (D) and site of double-strand break (A).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The multi-pass hydrophobic topology is directly observable in the sequence, and the distinction between 'plasma membrane' and 'external side' follows from the multi-pass (spanning) topology rather than peripheral/external-leaflet-only association.",
    "reason": "A model with general knowledge of transmembrane protein topology, bacterial cell biology, and GO cellular component definitions can reason from the hydrophobic segment count and the transferase function to select plasma membrane over the other options. The B-vs-C distinction is resolved by recognizing that a multi-pass protein is embedded across the bilayer (plasma membrane) rather than restricted to one leaflet (external side)."
  },
  "case_id": "GO_cellular_component_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0R3E8 (PMT_MYCS2) annotates the protein as 'Cell membrane; Multi-pass membrane protein' (evidence code ECO:0000250, inferred from similarity to P9WN05). The GO cross-reference explicitly assigns GO:0005886 (plasma membrane) with ISS/IEA evidence. GO:0005886 lists 'cell membrane' as an EXACT synonym (GO1). The annotation is computational (sequence-similarity-based) rather than direct experimental, but it is a valid and consistent database annotation. The sequence itself contains numerous hydrophobic stretches consistent with multi-pass membrane topology."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation carries evidence code ECO:0000250 (similarity to P9WN05), i.e., it is computational inference, not direct experimental localization.",
    "The GO assignment is ISS/IEA (inferred from sequence similarity / UniProtKB-SubCell), not an experimentally curated GO annotation.",
    "The GO ontology definition of 'external side of plasma membrane' (GO2) includes 'any protein embedded in, attached to, or peripherally associated with' the external leaflet, which could in principle encompass a multi-pass protein's external domains; however, the primary and most specific location for a multi-pass protein is the plasma membrane itself.",
    "The protein is from a bacterium; 'plasma membrane' and 'cell membrane' are synonymous in prokaryotic context (GO1 lists 'cell membrane' as EXACT synonym)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A (site of double-strand break) and D (replisome) are clearly incompatible with a multi-pass membrane protein lacking any DNA-interaction motifs. C (external side of plasma membrane) is a sub-compartment of B; a multi-pass protein spanning the bilayer is best described by B. The annotation and sequence features unambiguously favor B over C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0R3E8 (PMT_MYCS2) annotates the protein as 'Cell membrane; Multi-pass membrane protein' (evidence code ECO:0000250, inferred from similarity to P9WN05). The GO cross-reference explicitly assigns GO:0005886 (plasma membrane) with ISS/IEA evidence. GO:0005886 lists 'cell membrane' as an EXACT synonym (GO1). The annotation is computational (sequence-similarity-based) rather than direct experimental, but it is a valid and consistent database annotation. The sequence itself contains numerous hydrophobic stretches consistent with multi-pass membrane topology.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 516-aa sequence contains multiple long hydrophobic segments (e.g., AIITALAAITRFLNLGS, IIVMLVTRIARRISRSTLVGAIAGLLIIADGVSFVSSRTALLDVFLVMFAVAAFACLMV, VLLGLACATKWSGLYFVLFFGVMTLVFDAIARK, and several others) indicative of a multi-pass transmembrane protein. Multi-pass topology means the protein spans the lipid bilayer, making 'plasma membrane' (the whole membrane) the correct compartment rather than 'external side of plasma membrane' (a single leaflet). The enzymatic function (polyprenol-phosphate-mannose transferase) requires a membrane-embedded lipid carrier, further supporting membrane localization. Bacterial origin (Mycolicibacterium smegmatis) and absence of DNA-binding, helicase, or replication machinery motifs exclude replisome (D) and site of double-strand break (A).",
    "missing_item_specific_fact": "None critical. The multi-pass hydrophobic topology is directly observable in the sequence, and the distinction between 'plasma membrane' and 'external side' follows from the multi-pass (spanning) topology rather than peripheral/external-leaflet-only association.",
    "reason": "A model with general knowledge of transmembrane protein topology, bacterial cell biology, and GO cellular component definitions can reason from the hydrophobic segment count and the transferase function to select plasma membrane over the other options. The B-vs-C distinction is resolved by recognizing that a multi-pass protein is embedded across the bilayer (plasma membrane) rather than restricted to one leaflet (external side)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A (site of double-strand break) and D (replisome) are clearly incompatible with a multi-pass membrane protein lacking any DNA-interaction motifs. C (external side of plasma membrane) is a sub-compartment of B; a multi-pass protein spanning the bilayer is best described by B. The annotation and sequence features unambiguously favor B over C."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation carries evidence code ECO:0000250 (similarity to P9WN05), i.e., it is computational inference, not direct experimental localization.",
    "The GO assignment is ISS/IEA (inferred from sequence similarity / UniProtKB-SubCell), not an experimentally curated GO annotation.",
    "The GO ontology definition of 'external side of plasma membrane' (GO2) includes 'any protein embedded in, attached to, or peripherally associated with' the external leaflet, which could in principle encompass a multi-pass protein's external domains; however, the primary and most specific location for a multi-pass protein is the plasma membrane itself.",
    "The protein is from a bacterium; 'plasma membrane' and 'cell membrane' are synonymous in prokaryotic context (GO1 lists 'cell membrane' as EXACT synonym)."
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

**Accession:** `A0R3E8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P9WN05","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:45.822179+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 56-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P9WN05};
CC       Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)  
**Locator:** `lines 91-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:26:48.840229+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7`.

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

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 100773-100784`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009897
name: external side of plasma membrane
namespace: cellular_component
def: "The leaflet of the plasma membrane that faces the extracellular side of the cell, including any protein embedded in, attached to, or peripherally associated with it." [GOC:dos, GOC:tb]
synonym: "external leaflet of plasma membrane" EXACT [GOC:ab]
synonym: "juxtamembrane" BROAD []
synonym: "outer surface of cytoplasmic membrane" EXACT []
is_a: GO:0098552 ! side of membrane
relationship: part_of GO:0005886 ! plasma membrane
relationship: part_of GO:0009986 ! cell surface

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 102. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
