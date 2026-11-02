# GO_cellular_component_0005

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — extracellular region

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTKLTLTVALVSALLASGASAQQPTGTGNGPDPRATTDLNRNQPTKSWTQWQPKATYAFSQLPDQYMGANRIESGEGGQPGGEPQSGYNTCARNTWNQDSKCQTAWINSLEDFCLWAPAEYGTVGEKERSGVAYCTTDRHGTRLIPDGTIQGAHFVRTRDYVQVTGVGDFTSILIPDGDDGGEFDPHGADDLGNPIGGIVYTTANPASNGEPFFVSEWTNFMSYNQFCLRACWGERAAAQCEHIYDVMGCRWNIPANYEPGVFETCDGDIGQLQGIYSGSTFRQGDPVTPPAHPAPSSSQCSSVSTIGHGLLARSASASTSSVETSSSSAASSAATDSSASTNSASSMTRVTNSAVSTNVGSGTGSGSGSGSGSGSGSGSGSSSGSSSSGSSSNTQGAASSASSLTISVGLAGLVAIGAAAFAL

[Multiple Choices]
A. acrosomal membrane
B. extracellular region
C. viral envelope
D. fungal-type cell wall
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

> The exact sequence matches the UniProt entry, which reports experimental evidence for secretion and an IDA annotation to extracellular region. The entry also reports cell-membrane localization, so extracellular region is supported but not exclusive.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secretion signal, and the C-terminal hydrophobic segment with membrane anchoring; these features favor an externally exposed protein over the acrosomal or viral-envelope choices.


**Missing item-specific fact**

> The sequence does not establish whether the protein is in the extracellular region or retained in the fungal cell wall. Distinguishing those choices requires protein-specific localization evidence or annotation.


**Reason**

> Sequence features support secretion and membrane association, but do not precisely resolve extracellular space versus fungal cell wall. The experimental localization annotation is item-specific information absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> A secreted fungal protein could be extracellular or associated with the fungal cell wall; the supplied sequence alone does not distinguish these locations.


### Important caveats

- The localization evidence is reported for the sequence-matched protein and includes both secreted and cell-membrane locations.
- The reviewer-only annotations support the key but were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, and the C-terminal hydrophobic segment with membrane anchoring; these features favor an externally exposed protein over the acrosomal or viral-envelope choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence does not establish whether the protein is in the extracellular region or retained in the fungal cell wall. Distinguishing those choices requires protein-specific localization evidence or annotation.",
    "reason": "Sequence features support secretion and membrane association, but do not precisely resolve extracellular space versus fungal cell wall. The experimental localization annotation is item-specific information absent from the question."
  },
  "case_id": "GO_cellular_component_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which reports experimental evidence for secretion and an IDA annotation to extracellular region. The entry also reports cell-membrane localization, so extracellular region is supported but not exclusive."
  },
  "important_caveats": [
    "The localization evidence is reported for the sequence-matched protein and includes both secreted and cell-membrane locations.",
    "The reviewer-only annotations support the key but were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "A secreted fungal protein could be extracellular or associated with the fungal cell wall; the supplied sequence alone does not distinguish these locations."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which reports experimental evidence for secretion and an IDA annotation to extracellular region. The entry also reports cell-membrane localization, so extracellular region is supported but not exclusive.",
    "evidence_ids": ["C1", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, and the C-terminal hydrophobic segment with membrane anchoring; these features favor an externally exposed protein over the acrosomal or viral-envelope choices.",
    "missing_item_specific_fact": "The sequence does not establish whether the protein is in the extracellular region or retained in the fungal cell wall. Distinguishing those choices requires protein-specific localization evidence or annotation.",
    "reason": "Sequence features support secretion and membrane association, but do not precisely resolve extracellular space versus fungal cell wall. The experimental localization annotation is item-specific information absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "A secreted fungal protein could be extracellular or associated with the fungal cell wall; the supplied sequence alone does not distinguish these locations."
  },
  "important_caveats": [
    "The localization evidence is reported for the sequence-matched protein and includes both secreted and cell-membrane locations.",
    "The reviewer-only annotations support the key but were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0D1E921, ROW1_MYCMD) explicitly annotates GO:0005576 (extracellular region) with IDA:UniProtKB evidence from PubMed:38742361 (C6, H4). The subcellular location comment (C5, H3) states the protein is a single-pass membrane protein that is also 'Secreted,' consistent with extracellular localization. The primary literature (Pejenaute-Ochoa et al., 2024, New Phytol.) experimentally determined this localization. The plasma membrane annotation (C7/H5) is also present, but among the four offered choices, extracellular region is the best-supported answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays a clear N-terminal signal peptide (MTKLTLTVALVSALLASGASA, ~20 hydrophobic residues) directing entry into the secretory pathway, followed by a large glycosylated extracellular domain (multiple N-glycosylation sequons: NRT, NAT, NGS), and a C-terminal transmembrane helix (SVGLAGLVAIGAAAFAL). This architecture—a signal peptide, large soluble domain, and single-pass TM anchor—is characteristic of a membrane-anchored secreted protein whose bulk resides in the extracellular space. This rules out D (fungal-type cell wall) because cell wall structural proteins are typically GPI-anchored or fully secreted without transmembrane domains; a TM domain anchors the protein to the membrane, not into the wall matrix. A (acrosomal membrane) is eliminated because acrosomes are sperm-specific organelles with no relevance to a protein bearing fungal-type N-glycosylation and this architecture. C (viral envelope) is eliminated because the protein is clearly a eukaryotic secreted/membrane protein, not a viral structural protein.


**Missing item-specific fact**

> None critically required. One cannot determine the organism is a fungus from sequence alone, but the sequence features (signal peptide + TM domain + N-glycosylation) are sufficient to eliminate A and C, and the TM domain argues against D. The specific experimental finding that ROW1 localizes to the appressorium is supplementary but not needed to choose among the four options.


**Reason**

> The sequence contains identifiable signal peptide and transmembrane domain features that, combined with general knowledge of cell wall protein architecture (GPI-anchored or fully secreted, no TM domain) and the irrelevance of acrosomal/viral compartments to a eukaryotic secreted protein, allow a reasoning-based elimination of A, C, and D in favor of B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only B is consistent with the signal-peptide + TM-domain architecture of a secreted membrane protein. The plasma membrane is also annotated in UniProt but is not offered as a choice. D might superficially seem plausible given the fungal origin and the protein name 'Remodeling of fungal cell wall 1,' but the TM domain and membrane anchoring argue against the protein being a cell wall component itself. The GO definition note (that extracellular region is for products not attached to the cell surface) introduces minor terminological tension with the TM anchor, but UniProt's IDA annotation resolves this in favor of B.


### Important caveats

- The UniProt entry also annotates GO:0005886 (plasma membrane) with IDA evidence; the question's phrasing 'primary Cellular Component' and the available choices make B the best answer, but the protein is genuinely both membrane-anchored and extracellular.
- The GO:0005576 definition notes it is intended for gene products NOT attached to the cell surface; a single-pass membrane protein's extracellular domain could arguably be annotated to GO:0009897 (external side of plasma membrane) instead. UniProt nonetheless assigns GO:0005576 with IDA evidence.
- The organism (Mycosarcoma maydis / Ustilago maydis) cannot be determined from sequence alone; the reasoning relies on general eukaryotic secretory pathway biology rather than species identification.
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays a clear N-terminal signal peptide (MTKLTLTVALVSALLASGASA, ~20 hydrophobic residues) directing entry into the secretory pathway, followed by a large glycosylated extracellular domain (multiple N-glycosylation sequons: NRT, NAT, NGS), and a C-terminal transmembrane helix (SVGLAGLVAIGAAAFAL). This architecture—a signal peptide, large soluble domain, and single-pass TM anchor—is characteristic of a membrane-anchored secreted protein whose bulk resides in the extracellular space. This rules out D (fungal-type cell wall) because cell wall structural proteins are typically GPI-anchored or fully secreted without transmembrane domains; a TM domain anchors the protein to the membrane, not into the wall matrix. A (acrosomal membrane) is eliminated because acrosomes are sperm-specific organelles with no relevance to a protein bearing fungal-type N-glycosylation and this architecture. C (viral envelope) is eliminated because the protein is clearly a eukaryotic secreted/membrane protein, not a viral structural protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critically required. One cannot determine the organism is a fungus from sequence alone, but the sequence features (signal peptide + TM domain + N-glycosylation) are sufficient to eliminate A and C, and the TM domain argues against D. The specific experimental finding that ROW1 localizes to the appressorium is supplementary but not needed to choose among the four options.",
    "reason": "The sequence contains identifiable signal peptide and transmembrane domain features that, combined with general knowledge of cell wall protein architecture (GPI-anchored or fully secreted, no TM domain) and the irrelevance of acrosomal/viral compartments to a eukaryotic secreted protein, allow a reasoning-based elimination of A, C, and D in favor of B."
  },
  "case_id": "GO_cellular_component_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0D1E921, ROW1_MYCMD) explicitly annotates GO:0005576 (extracellular region) with IDA:UniProtKB evidence from PubMed:38742361 (C6, H4). The subcellular location comment (C5, H3) states the protein is a single-pass membrane protein that is also 'Secreted,' consistent with extracellular localization. The primary literature (Pejenaute-Ochoa et al., 2024, New Phytol.) experimentally determined this localization. The plasma membrane annotation (C7/H5) is also present, but among the four offered choices, extracellular region is the best-supported answer."
  },
  "important_caveats": [
    "The UniProt entry also annotates GO:0005886 (plasma membrane) with IDA evidence; the question's phrasing 'primary Cellular Component' and the available choices make B the best answer, but the protein is genuinely both membrane-anchored and extracellular.",
    "The GO:0005576 definition notes it is intended for gene products NOT attached to the cell surface; a single-pass membrane protein's extracellular domain could arguably be annotated to GO:0009897 (external side of plasma membrane) instead. UniProt nonetheless assigns GO:0005576 with IDA evidence.",
    "The organism (Mycosarcoma maydis / Ustilago maydis) cannot be determined from sequence alone; the reasoning relies on general eukaryotic secretory pathway biology rather than species identification.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only B is consistent with the signal-peptide + TM-domain architecture of a secreted membrane protein. The plasma membrane is also annotated in UniProt but is not offered as a choice. D might superficially seem plausible given the fungal origin and the protein name 'Remodeling of fungal cell wall 1,' but the TM domain and membrane anchoring argue against the protein being a cell wall component itself. The GO definition note (that extracellular region is for products not attached to the cell surface) introduces minor terminological tension with the TM anchor, but UniProt's IDA annotation resolves this in favor of B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0D1E921, ROW1_MYCMD) explicitly annotates GO:0005576 (extracellular region) with IDA:UniProtKB evidence from PubMed:38742361 (C6, H4). The subcellular location comment (C5, H3) states the protein is a single-pass membrane protein that is also 'Secreted,' consistent with extracellular localization. The primary literature (Pejenaute-Ochoa et al., 2024, New Phytol.) experimentally determined this localization. The plasma membrane annotation (C7/H5) is also present, but among the four offered choices, extracellular region is the best-supported answer.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays a clear N-terminal signal peptide (MTKLTLTVALVSALLASGASA, ~20 hydrophobic residues) directing entry into the secretory pathway, followed by a large glycosylated extracellular domain (multiple N-glycosylation sequons: NRT, NAT, NGS), and a C-terminal transmembrane helix (SVGLAGLVAIGAAAFAL). This architecture—a signal peptide, large soluble domain, and single-pass TM anchor—is characteristic of a membrane-anchored secreted protein whose bulk resides in the extracellular space. This rules out D (fungal-type cell wall) because cell wall structural proteins are typically GPI-anchored or fully secreted without transmembrane domains; a TM domain anchors the protein to the membrane, not into the wall matrix. A (acrosomal membrane) is eliminated because acrosomes are sperm-specific organelles with no relevance to a protein bearing fungal-type N-glycosylation and this architecture. C (viral envelope) is eliminated because the protein is clearly a eukaryotic secreted/membrane protein, not a viral structural protein.",
    "missing_item_specific_fact": "None critically required. One cannot determine the organism is a fungus from sequence alone, but the sequence features (signal peptide + TM domain + N-glycosylation) are sufficient to eliminate A and C, and the TM domain argues against D. The specific experimental finding that ROW1 localizes to the appressorium is supplementary but not needed to choose among the four options.",
    "reason": "The sequence contains identifiable signal peptide and transmembrane domain features that, combined with general knowledge of cell wall protein architecture (GPI-anchored or fully secreted, no TM domain) and the irrelevance of acrosomal/viral compartments to a eukaryotic secreted protein, allow a reasoning-based elimination of A, C, and D in favor of B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only B is consistent with the signal-peptide + TM-domain architecture of a secreted membrane protein. The plasma membrane is also annotated in UniProt but is not offered as a choice. D might superficially seem plausible given the fungal origin and the protein name 'Remodeling of fungal cell wall 1,' but the TM domain and membrane anchoring argue against the protein being a cell wall component itself. The GO definition note (that extracellular region is for products not attached to the cell surface) introduces minor terminological tension with the TM anchor, but UniProt's IDA annotation resolves this in favor of B."
  },
  "important_caveats": [
    "The UniProt entry also annotates GO:0005886 (plasma membrane) with IDA evidence; the question's phrasing 'primary Cellular Component' and the available choices make B the best answer, but the protein is genuinely both membrane-anchored and extracellular.",
    "The GO:0005576 definition notes it is intended for gene products NOT attached to the cell surface; a single-pass membrane protein's extracellular domain could arguably be annotated to GO:0009897 (external side of plasma membrane) instead. UniProt nonetheless assigns GO:0005576 with IDA evidence.",
    "The organism (Mycosarcoma maydis / Ustilago maydis) cannot be determined from sequence alone; the reasoning relies on general eukaryotic secretory pathway biology rather than species identification.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model."
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

**Accession:** `A0A0D1E921` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 33. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.233517+00:00.  

```json
"A0A0D1E921"
```

Source SHA-256: `572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.233517+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38742361","source":"PubMed"}],"value":"Localizes to the appressorium"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38742361","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9904","value":"Single-pass membrane protein"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38742361","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}}]}
```

Source SHA-256: `572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.233517+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38742361","source":"PubMed"}],"id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.233517+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38742361","source":"PubMed"}],"id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0D1E921.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.233517+00:00.  

```json
{"citation":{"authors":["Pejenaute-Ochoa M.D.","Tomas-Gallardo L.","Ibeas J.I.","Barrales R.R."],"citationCrossReferences":[{"database":"PubMed","id":"38742361"},{"database":"DOI","id":"10.1111/nph.19798"}],"citationType":"journal article","firstPage":"1101","id":"38742361","journal":"New Phytol.","lastPage":"1122","publicationDate":"2024","title":"Row1, a member of a new family of conserved fungal proteins involved in infection, is required for appressoria functionality in Ustilago maydis.","volume":"243"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `572fa870d5f0441e3cf49fdb3360dda67fa47be83ec478dd1439ce1b78c9f919`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33)  
**Locator:** `lines 54-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-01T06:27:17.968792+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:38742361};
CC       Single-pass membrane protein {ECO:0000255}. Secreted
CC       {ECO:0000269|PubMed:38742361}. Note=Localizes to the appressorium.
CC       {ECO:0000269|PubMed:38742361}.
```

Source SHA-256: `8114ff9e42268e7b756dc319780d9d2caebbb1204516dbaf81ce46718216e5f8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33)  
**Locator:** `lines 83-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-01T06:27:17.968792+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IDA:UniProtKB.
```

Source SHA-256: `8114ff9e42268e7b756dc319780d9d2caebbb1204516dbaf81ce46718216e5f8`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0D1E921?format=txt&versions=33)  
**Locator:** `lines 84-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-01T06:27:17.968792+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.
```

Source SHA-256: `8114ff9e42268e7b756dc319780d9d2caebbb1204516dbaf81ce46718216e5f8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
