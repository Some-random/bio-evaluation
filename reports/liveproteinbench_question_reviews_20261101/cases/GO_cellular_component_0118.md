# GO_cellular_component_0118

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — side of membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLLYLVALFVASICSVTAQTWTSCNPLTTTCPPDQALGINTTFTFNKTLDDTIWNVTNGVLSHTDEGTEFTITGENQSPTMQSNFYIFFGIVESHVKMAKGAGIISSIVLQSDDLDEIDWEWVGYNTSEVQSNYFGKGNNETFNRGGYHYVPNADTEFHNYTTYWTQEKLEWWIDGKLARTLTYEDSQGAGKYYPQTPCNIRYGIWPAGIKGNAQGTIEWAGGLVDYSKAPFTMVLQSVRVHDFHTGKEYNYTDHSGSWQSIDVIAGNSTIANAIQNPPKSLSEKWAELPTGAKAGVYIGAGCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN

[Multiple Choices]
A. host cell plasma membrane
B. endocytic vesicle
C. side of membrane
D. host cell nucleolus
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

> The sequence-matched UniProt record annotates this protein to the cell membrane with a GPI anchor and also lists GO:0098552, side of membrane. The location annotations are computational/inferred rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic signal-peptide-like region and C-terminal hydrophobic tail are consistent with a secreted protein carrying a GPI-anchor signal, supporting membrane association and distinguishing it from nucleolar or endocytic-vesicle localization. The broad side-of-membrane choice fits that inference.


**Missing item-specific fact**

> No additional protein-specific fact is essential to favor C among these choices, though confirming its exact cellular localization would require external evidence.


**Reason**

> The sequence provides recognizable secretion and likely GPI-anchor features. Choice A specifies a host-cell plasma membrane, which does not fit the inferred fungal protein context; the sequence features support the more general membrane-side option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence and annotations support membrane association; the other options name a host-cell compartment, an endocytic vesicle, or a nucleolar compartment. The record also lists secretion to the cell wall, but that is not an offered choice.


### Important caveats

- The reviewer-only UniProt annotation is sequence-matched, but the cellular-location evidence shown is computational or inferred, not a direct experimental localization result.
- The record gives both cell-membrane and cell-wall locations, so calling one the primary location is not fully resolved by the excerpts.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal-peptide-like region and C-terminal hydrophobic tail are consistent with a secreted protein carrying a GPI-anchor signal, supporting membrane association and distinguishing it from nucleolar or endocytic-vesicle localization. The broad side-of-membrane choice fits that inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional protein-specific fact is essential to favor C among these choices, though confirming its exact cellular localization would require external evidence.",
    "reason": "The sequence provides recognizable secretion and likely GPI-anchor features. Choice A specifies a host-cell plasma membrane, which does not fit the inferred fungal protein context; the sequence features support the more general membrane-side option."
  },
  "case_id": "GO_cellular_component_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to the cell membrane with a GPI anchor and also lists GO:0098552, side of membrane. The location annotations are computational/inferred rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation is sequence-matched, but the cellular-location evidence shown is computational or inferred, not a direct experimental localization result.",
    "The record gives both cell-membrane and cell-wall locations, so calling one the primary location is not fully resolved by the excerpts.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and annotations support membrane association; the other options name a host-cell compartment, an endocytic vesicle, or a nucleolar compartment. The record also lists secretion to the cell wall, but that is not an offered choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to the cell membrane with a GPI anchor and also lists GO:0098552, side of membrane. The location annotations are computational/inferred rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal-peptide-like region and C-terminal hydrophobic tail are consistent with a secreted protein carrying a GPI-anchor signal, supporting membrane association and distinguishing it from nucleolar or endocytic-vesicle localization. The broad side-of-membrane choice fits that inference.",
    "missing_item_specific_fact": "No additional protein-specific fact is essential to favor C among these choices, though confirming its exact cellular localization would require external evidence.",
    "reason": "The sequence provides recognizable secretion and likely GPI-anchor features. Choice A specifies a host-cell plasma membrane, which does not fit the inferred fungal protein context; the sequence features support the more general membrane-side option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and annotations support membrane association; the other options name a host-cell compartment, an endocytic vesicle, or a nucleolar compartment. The record also lists secretion to the cell wall, but that is not an offered choice."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation is sequence-matched, but the cellular-location evidence shown is computational or inferred, not a direct experimental localization result.",
    "The record gives both cell-membrane and cell-wall locations, so calling one the primary location is not fully resolved by the excerpts.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WXE6 (Crh-like protein 3, Aspergillus fumigatus) carries a direct GO annotation to GO:0098552 (side of membrane) via IEA:UniProtKB-KW (H5). The subcellular location comment states 'Cell membrane; Lipid-anchor, GPI-anchor' (C5/H3), which is biologically consistent with 'side of membrane' (defined as one leaflet of a membrane bilayer with anchored proteins, GO4). A GPI-anchored protein resides on one leaflet of the bilayer, matching the GO:0098552 definition. Note that GO:0005886 (plasma membrane) is also annotated (H4), but that term is not among the answer choices; option A is GO:0020002 (host cell plasma membrane), a goslim_virus term referring to a host cell's membrane in viral contexts, which does not apply to this fungal protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO4](#evidence-go4), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal hydrophobic stretch followed by a short polar tail in the sequence is consistent with a GPI-anchor signal, which places the protein on one leaflet of the membrane bilayer. This is compatible with 'side of membrane' (GO:0098552: one leaflet with anchored proteins). Additionally, the 'host cell' qualifier in options A and D is specific to viral/parasitic contexts (goslim_virus subset), which could be reasoned against for a non-viral protein. However, the database also annotates GO:0005886 (plasma membrane) as a valid location, and the designation of 'side of membrane' as the 'primary' component over 'plasma membrane' is a curation/annotation choice not derivable from sequence alone.


**Missing item-specific fact**

> The specific annotation decision that designates 'side of membrane' (GO:0098552) as the primary cellular component for this particular protein, rather than 'plasma membrane' (GO:0005886), which is also annotated. Both are IEA annotations; the 'primary' label is a database curation artifact.


**Reason**

> While GPI-anchor recognition from the sequence provides a partial biological argument for membrane-leaflet localization, the actual choice between 'side of membrane' and 'plasma membrane' as the 'primary' location is an annotation-level decision. The model must know or look up that this protein's primary GO CC annotation is GO:0098552 rather than GO:0005886. The elimination of options A and D via 'host cell' reasoning is possible but somewhat indirect; the core discrimination between the remaining plausible membrane-associated terms depends on the specific database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> Among the four options, only C (side of membrane) matches an actual annotation on this protein. Option A (host cell plasma membrane, GO:0020002) is a goslim_virus term inappropriate for a fungal protein. Options B (endocytic vesicle) and D (host cell nucleolus) have no annotation support. The true ambiguity is between 'plasma membrane' (GO:0005886, also annotated) and 'side of membrane' (GO:0098552), but 'plasma membrane' is not offered as an option, so C is the only defensible choice among the given alternatives.


### Important caveats

- Both GO:0005886 (plasma membrane) and GO:0098552 (side of membrane) are IEA (Inferred from Electronic Annotation) annotations; neither is experimentally validated for this protein.
- The subcellular location comment 'Cell membrane; Lipid-anchor, GPI-anchor' is annotated with ECO:0000255 (inferred by similarity/prorule), not direct experimental evidence.
- The 'host cell plasma membrane' option (GO:0020002) is a goslim_virus term and is a different ontology branch from 'plasma membrane' (GO:0005886); its inclusion as a distractor tests whether the model recognizes the 'host cell' qualifier as virus-specific.
- The protein is also annotated as 'Secreted, cell wall' (ECO:0000305), suggesting it may also be found extracellularly, but this is not among the answer options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal hydrophobic stretch followed by a short polar tail in the sequence is consistent with a GPI-anchor signal, which places the protein on one leaflet of the membrane bilayer. This is compatible with 'side of membrane' (GO:0098552: one leaflet with anchored proteins). Additionally, the 'host cell' qualifier in options A and D is specific to viral/parasitic contexts (goslim_virus subset), which could be reasoned against for a non-viral protein. However, the database also annotates GO:0005886 (plasma membrane) as a valid location, and the designation of 'side of membrane' as the 'primary' component over 'plasma membrane' is a curation/annotation choice not derivable from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation decision that designates 'side of membrane' (GO:0098552) as the primary cellular component for this particular protein, rather than 'plasma membrane' (GO:0005886), which is also annotated. Both are IEA annotations; the 'primary' label is a database curation artifact.",
    "reason": "While GPI-anchor recognition from the sequence provides a partial biological argument for membrane-leaflet localization, the actual choice between 'side of membrane' and 'plasma membrane' as the 'primary' location is an annotation-level decision. The model must know or look up that this protein's primary GO CC annotation is GO:0098552 rather than GO:0005886. The elimination of options A and D via 'host cell' reasoning is possible but somewhat indirect; the core discrimination between the remaining plausible membrane-associated terms depends on the specific database annotation."
  },
  "case_id": "GO_cellular_component_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H4",
      "H5",
      "GO4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXE6 (Crh-like protein 3, Aspergillus fumigatus) carries a direct GO annotation to GO:0098552 (side of membrane) via IEA:UniProtKB-KW (H5). The subcellular location comment states 'Cell membrane; Lipid-anchor, GPI-anchor' (C5/H3), which is biologically consistent with 'side of membrane' (defined as one leaflet of a membrane bilayer with anchored proteins, GO4). A GPI-anchored protein resides on one leaflet of the bilayer, matching the GO:0098552 definition. Note that GO:0005886 (plasma membrane) is also annotated (H4), but that term is not among the answer choices; option A is GO:0020002 (host cell plasma membrane), a goslim_virus term referring to a host cell's membrane in viral contexts, which does not apply to this fungal protein."
  },
  "important_caveats": [
    "Both GO:0005886 (plasma membrane) and GO:0098552 (side of membrane) are IEA (Inferred from Electronic Annotation) annotations; neither is experimentally validated for this protein.",
    "The subcellular location comment 'Cell membrane; Lipid-anchor, GPI-anchor' is annotated with ECO:0000255 (inferred by similarity/prorule), not direct experimental evidence.",
    "The 'host cell plasma membrane' option (GO:0020002) is a goslim_virus term and is a different ontology branch from 'plasma membrane' (GO:0005886); its inclusion as a distractor tests whether the model recognizes the 'host cell' qualifier as virus-specific.",
    "The protein is also annotated as 'Secreted, cell wall' (ECO:0000305), suggesting it may also be found extracellularly, but this is not among the answer options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "Among the four options, only C (side of membrane) matches an actual annotation on this protein. Option A (host cell plasma membrane, GO:0020002) is a goslim_virus term inappropriate for a fungal protein. Options B (endocytic vesicle) and D (host cell nucleolus) have no annotation support. The true ambiguity is between 'plasma membrane' (GO:0005886, also annotated) and 'side of membrane' (GO:0098552), but 'plasma membrane' is not offered as an option, so C is the only defensible choice among the given alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXE6 (Crh-like protein 3, Aspergillus fumigatus) carries a direct GO annotation to GO:0098552 (side of membrane) via IEA:UniProtKB-KW (H5). The subcellular location comment states 'Cell membrane; Lipid-anchor, GPI-anchor' (C5/H3), which is biologically consistent with 'side of membrane' (defined as one leaflet of a membrane bilayer with anchored proteins, GO4). A GPI-anchored protein resides on one leaflet of the bilayer, matching the GO:0098552 definition. Note that GO:0005886 (plasma membrane) is also annotated (H4), but that term is not among the answer choices; option A is GO:0020002 (host cell plasma membrane), a goslim_virus term referring to a host cell's membrane in viral contexts, which does not apply to this fungal protein.",
    "evidence_ids": ["C5", "H3", "H4", "H5", "GO4", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal hydrophobic stretch followed by a short polar tail in the sequence is consistent with a GPI-anchor signal, which places the protein on one leaflet of the membrane bilayer. This is compatible with 'side of membrane' (GO:0098552: one leaflet with anchored proteins). Additionally, the 'host cell' qualifier in options A and D is specific to viral/parasitic contexts (goslim_virus subset), which could be reasoned against for a non-viral protein. However, the database also annotates GO:0005886 (plasma membrane) as a valid location, and the designation of 'side of membrane' as the 'primary' component over 'plasma membrane' is a curation/annotation choice not derivable from sequence alone.",
    "missing_item_specific_fact": "The specific annotation decision that designates 'side of membrane' (GO:0098552) as the primary cellular component for this particular protein, rather than 'plasma membrane' (GO:0005886), which is also annotated. Both are IEA annotations; the 'primary' label is a database curation artifact.",
    "reason": "While GPI-anchor recognition from the sequence provides a partial biological argument for membrane-leaflet localization, the actual choice between 'side of membrane' and 'plasma membrane' as the 'primary' location is an annotation-level decision. The model must know or look up that this protein's primary GO CC annotation is GO:0098552 rather than GO:0005886. The elimination of options A and D via 'host cell' reasoning is possible but somewhat indirect; the core discrimination between the remaining plausible membrane-associated terms depends on the specific database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C"],
    "reason": "Among the four options, only C (side of membrane) matches an actual annotation on this protein. Option A (host cell plasma membrane, GO:0020002) is a goslim_virus term inappropriate for a fungal protein. Options B (endocytic vesicle) and D (host cell nucleolus) have no annotation support. The true ambiguity is between 'plasma membrane' (GO:0005886, also annotated) and 'side of membrane' (GO:0098552), but 'plasma membrane' is not offered as an option, so C is the only defensible choice among the given alternatives."
  },
  "important_caveats": [
    "Both GO:0005886 (plasma membrane) and GO:0098552 (side of membrane) are IEA (Inferred from Electronic Annotation) annotations; neither is experimentally validated for this protein.",
    "The subcellular location comment 'Cell membrane; Lipid-anchor, GPI-anchor' is annotated with ECO:0000255 (inferred by similarity/prorule), not direct experimental evidence.",
    "The 'host cell plasma membrane' option (GO:0020002) is a goslim_virus term and is a different ontology branch from 'plasma membrane' (GO:0005886); its inclusion as a distractor tests whether the model recognizes the 'host cell' qualifier as virus-specific.",
    "The protein is also annotated as 'Secreted, cell wall' (ECO:0000305), suggesting it may also be found extracellularly, but this is not among the answer options."
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

**Accession:** `Q4WXE6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 98. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.355475+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9902","value":"Lipid-anchor, GPI-anchor"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0041","value":"Secreted, cell wall"}}]}
```

Source SHA-256: `e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)  
**Locator:** `lines 65-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 2.  
**Retrieved:** 2026-11-02T04:31:00.140024+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000255}; Lipid-anchor, GPI-
CC       anchor {ECO:0000255}. Secreted, cell wall {ECO:0000305}.
```

Source SHA-256: `af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)  
**Locator:** `lines 92-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 2.  
**Retrieved:** 2026-11-02T04:31:00.140024+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)  
**Locator:** `lines 93-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 2.  
**Retrieved:** 2026-11-02T04:31:00.140024+00:00.  

```text
DR   GO; GO:0098552; C:side of membrane; IEA:UniProtKB-KW.
```

Source SHA-256: `af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 155120-155127`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0020002
name: host cell plasma membrane
namespace: cellular_component
def: "The plasma membrane surrounding a host cell." [GOC:mb]
subset: goslim_virus
is_a: GO:0033644 ! host cell membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 408943-408950`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0098552
name: side of membrane
namespace: cellular_component
def: "A cellular component consisting of one leaflet of a membrane bilayer and any protein embedded or anchored in it or attached to its surface." [GOC:dos]
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0016020 ! membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
