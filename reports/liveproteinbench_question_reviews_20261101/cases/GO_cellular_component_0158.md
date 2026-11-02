# GO_cellular_component_0158

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQTEHWGSLPAEDDGGQLTPDKYVPTAAKKLKLDEIRQRGDPQPQEKHHKLELRSALVTQTIEVMKQTEVLQSLIETYSNKNGSSNYLLNPCLMIPEVDFPPENAAELVGSQKFQKPIWFTPTVDTAYSRGDPEAYPEIPSSACRQAMRKVMCGMLRLAGFTDCSESAVQLLTDATEEFLRSFIGEYRGYYDSQPRLQNSTVLQLVPLERAHFAQTGTSLTQVHNYYKHKVLARNRAEIAEFNSVLQEYDKLMKESQSSMQKQHNEFNGHDFLNILDNSATGSSQSIGGMAMGDMLQDLGGSTGSSGTVSSQQMLYGLLDGQISSNTSNMTGTSGNGSTGGNGNGNGATISNFHATFET

[Multiple Choices]
A. lysosomal membrane
B. membrane
C. nucleus
D. cell tip
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

> The supplied sequence exactly matches the reviewed Drosophila Spt7 record, which annotates the protein to the nucleus. The subcellular-location annotation cites experimental evidence, and the GO nucleus annotation is marked IDA.

Citations as saved: [H5](#evidence-h5), [H6](#evidence-h6), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence appears to encode a soluble protein rather than a typical membrane protein, which weakens the membrane choices. But that does not specifically distinguish nuclear residence from cell-tip residence.


**Missing item-specific fact**

> The identity or function of this protein as a SAGA complex subunit, or direct protein-specific localization evidence, is needed to establish nuclear localization.


**Reason**

> The input provides no clear localization signal that resolves nucleus versus cell tip. Knowing the protein-specific SAGA association or its experimental localization requires an external fact; recognizing the exact sequence would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports nucleus, and the sequence alone does not establish a competing listed localization.


### Important caveats

- The supporting annotation is sequence-matched and cites experimental evidence, but the underlying primary studies were not independently validated here.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence appears to encode a soluble protein rather than a typical membrane protein, which weakens the membrane choices. But that does not specifically distinguish nuclear residence from cell-tip residence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity or function of this protein as a SAGA complex subunit, or direct protein-specific localization evidence, is needed to establish nuclear localization.",
    "reason": "The input provides no clear localization signal that resolves nucleus versus cell tip. Knowing the protein-specific SAGA association or its experimental localization requires an external fact; recognizing the exact sequence would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "GO_cellular_component_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H6",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Drosophila Spt7 record, which annotates the protein to the nucleus. The subcellular-location annotation cites experimental evidence, and the GO nucleus annotation is marked IDA."
  },
  "important_caveats": [
    "The supporting annotation is sequence-matched and cites experimental evidence, but the underlying primary studies were not independently validated here.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports nucleus, and the sequence alone does not establish a competing listed localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Drosophila Spt7 record, which annotates the protein to the nucleus. The subcellular-location annotation cites experimental evidence, and the GO nucleus annotation is marked IDA.",
    "evidence_ids": ["H5", "H6", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence appears to encode a soluble protein rather than a typical membrane protein, which weakens the membrane choices. But that does not specifically distinguish nuclear residence from cell-tip residence.",
    "missing_item_specific_fact": "The identity or function of this protein as a SAGA complex subunit, or direct protein-specific localization evidence, is needed to establish nuclear localization.",
    "reason": "The input provides no clear localization signal that resolves nucleus versus cell tip. Knowing the protein-specific SAGA association or its experimental localization requires an external fact; recognizing the exact sequence would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports nucleus, and the sequence alone does not establish a competing listed localization."
  },
  "important_caveats": [
    "The supporting annotation is sequence-matched and cites experimental evidence, but the underlying primary studies were not independently validated here.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9VX12 (SAGA complex subunit Spt7, Drosophila melanogaster) annotates subcellular location as Nucleus with experimental evidence (ECO:0000269 from PubMed:20008933 and PubMed:24493646). The GO annotation GO:0005634 (nucleus) is supported by IDA:FlyBase evidence from multiple independent studies. The protein is a subunit of the SAGA transcriptional coactivator complex, which functions in the nucleus. Sequence match is confirmed (SHA256 identical).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (359 aa) lacks any transmembrane domain (no stretch of ≥18 hydrophobic residues), lacks an N-terminal signal peptide, and lacks mitochondrial targeting or peroxisomal targeting signals. This eliminates membrane (B) and lysosomal membrane (A) as the protein is clearly soluble. 'Cell tip' (D) is a highly specialized localization seen in yeast polarity proteins (e.g., Cdc42 effectors, exocyst components) and is implausible for a small, soluble, non-polarity protein. By elimination among the four options, nucleus (C) is the most defensible answer. Additionally, the protein's composition (moderate charge, no hydrophobic clusters, small size) is consistent with a soluble nuclear regulatory protein rather than a membrane or structural protein.


**Missing item-specific fact**

> Positive identification of nucleus (vs. cytoplasm, which is not an option) is weak without recognizing the protein as a SAGA complex subunit. The sequence lacks a canonical bipartite NLS. However, since cytoplasm is not among the choices, elimination of A, B, and D suffices to select C.


**Reason**

> A model can reason from the absence of transmembrane segments, signal peptides, and organelle-targeting sequences to eliminate membrane-associated options (A, B). Cell tip (D) is a specialized fungal/yeast polarity localization implausible for this protein type. This leaves nucleus as the only viable option. The reasoning is primarily eliminative but uses concrete sequence features and general cell biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the four options and the sequence lacking membrane-targeting features, only nucleus is defensible. Cytoplasm is not offered as a distractor, which simplifies the question. Cell tip is implausible for a small soluble protein without polarity-domain architecture.


### Important caveats

- The positive identification of nucleus relies on elimination rather than a recognizable NLS or transcription-factor domain in the sequence itself.
- Without cytoplasm as a distractor, the question is easier than it would be in a full GO Cellular Component prediction task.
- The sequence is from Drosophila melanogaster, but the organism is not stated in the question; 'cell tip' is primarily a yeast/fungal term, making option D even less plausible for a metazoan protein.
- The UniProt entry was first publicly released in 2025-06-18; the benchmark construction date relative to this release is uncertain.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (359 aa) lacks any transmembrane domain (no stretch of ≥18 hydrophobic residues), lacks an N-terminal signal peptide, and lacks mitochondrial targeting or peroxisomal targeting signals. This eliminates membrane (B) and lysosomal membrane (A) as the protein is clearly soluble. 'Cell tip' (D) is a highly specialized localization seen in yeast polarity proteins (e.g., Cdc42 effectors, exocyst components) and is implausible for a small, soluble, non-polarity protein. By elimination among the four options, nucleus (C) is the most defensible answer. Additionally, the protein's composition (moderate charge, no hydrophobic clusters, small size) is consistent with a soluble nuclear regulatory protein rather than a membrane or structural protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of nucleus (vs. cytoplasm, which is not an option) is weak without recognizing the protein as a SAGA complex subunit. The sequence lacks a canonical bipartite NLS. However, since cytoplasm is not among the choices, elimination of A, B, and D suffices to select C.",
    "reason": "A model can reason from the absence of transmembrane segments, signal peptides, and organelle-targeting sequences to eliminate membrane-associated options (A, B). Cell tip (D) is a specialized fungal/yeast polarity localization implausible for this protein type. This leaves nucleus as the only viable option. The reasoning is primarily eliminative but uses concrete sequence features and general cell biology."
  },
  "case_id": "GO_cellular_component_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9VX12 (SAGA complex subunit Spt7, Drosophila melanogaster) annotates subcellular location as Nucleus with experimental evidence (ECO:0000269 from PubMed:20008933 and PubMed:24493646). The GO annotation GO:0005634 (nucleus) is supported by IDA:FlyBase evidence from multiple independent studies. The protein is a subunit of the SAGA transcriptional coactivator complex, which functions in the nucleus. Sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "The positive identification of nucleus relies on elimination rather than a recognizable NLS or transcription-factor domain in the sequence itself.",
    "Without cytoplasm as a distractor, the question is easier than it would be in a full GO Cellular Component prediction task.",
    "The sequence is from Drosophila melanogaster, but the organism is not stated in the question; 'cell tip' is primarily a yeast/fungal term, making option D even less plausible for a metazoan protein.",
    "The UniProt entry was first publicly released in 2025-06-18; the benchmark construction date relative to this release is uncertain."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four options and the sequence lacking membrane-targeting features, only nucleus is defensible. Cytoplasm is not offered as a distractor, which simplifies the question. Cell tip is implausible for a small soluble protein without polarity-domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9VX12 (SAGA complex subunit Spt7, Drosophila melanogaster) annotates subcellular location as Nucleus with experimental evidence (ECO:0000269 from PubMed:20008933 and PubMed:24493646). The GO annotation GO:0005634 (nucleus) is supported by IDA:FlyBase evidence from multiple independent studies. The protein is a subunit of the SAGA transcriptional coactivator complex, which functions in the nucleus. Sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C5", "C6", "H5", "H6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (359 aa) lacks any transmembrane domain (no stretch of ≥18 hydrophobic residues), lacks an N-terminal signal peptide, and lacks mitochondrial targeting or peroxisomal targeting signals. This eliminates membrane (B) and lysosomal membrane (A) as the protein is clearly soluble. 'Cell tip' (D) is a highly specialized localization seen in yeast polarity proteins (e.g., Cdc42 effectors, exocyst components) and is implausible for a small, soluble, non-polarity protein. By elimination among the four options, nucleus (C) is the most defensible answer. Additionally, the protein's composition (moderate charge, no hydrophobic clusters, small size) is consistent with a soluble nuclear regulatory protein rather than a membrane or structural protein.",
    "missing_item_specific_fact": "Positive identification of nucleus (vs. cytoplasm, which is not an option) is weak without recognizing the protein as a SAGA complex subunit. The sequence lacks a canonical bipartite NLS. However, since cytoplasm is not among the choices, elimination of A, B, and D suffices to select C.",
    "reason": "A model can reason from the absence of transmembrane segments, signal peptides, and organelle-targeting sequences to eliminate membrane-associated options (A, B). Cell tip (D) is a specialized fungal/yeast polarity localization implausible for this protein type. This leaves nucleus as the only viable option. The reasoning is primarily eliminative but uses concrete sequence features and general cell biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four options and the sequence lacking membrane-targeting features, only nucleus is defensible. Cytoplasm is not offered as a distractor, which simplifies the question. Cell tip is implausible for a small soluble protein without polarity-domain architecture."
  },
  "important_caveats": [
    "The positive identification of nucleus relies on elimination rather than a recognizable NLS or transcription-factor domain in the sequence itself.",
    "Without cytoplasm as a distractor, the question is easier than it would be in a full GO Cellular Component prediction task.",
    "The sequence is from Drosophila melanogaster, but the organism is not stated in the question; 'cell tip' is primarily a yeast/fungal term, making option D even less plausible for a metazoan protein.",
    "The UniProt entry was first publicly released in 2025-06-18; the benchmark construction date relative to this release is uncertain."
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

**Accession:** `Q9VX12` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 167. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:45.135468+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"20008933","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24493646","source":"PubMed"}],"id":"SL-0191","value":"Nucleus"}}]}
```

Source SHA-256: `ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VX12.json)  
**Locator:** `/uniProtKBCrossReferences/27`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:45.135468+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"16980620","source":"PubMed"},{"evidenceCode":"ECO:0000314","id":"21764853","source":"PubMed"}],"id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `ae7512cc6937670c745d0ef7f02a0b1125a8c84ebd9426ae75d0ae1ec689e89f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)  
**Locator:** `lines 86-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 167 / 3.  
**Retrieved:** 2026-11-02T04:33:49.946751+00:00.  

```text
RN   [5] {ECO:0000305}
RP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, SUBCELLULAR LOCATION, AND
RP   IDENTIFICATION BY MASS SPECTROMETRY.
RX   PubMed=20008933; DOI=10.1101/gad.1846409;
RA   Weake V.M., Swanson S.K., Mushegian A., Florens L., Washburn M.P.,
RA   Abmayr S.M., Workman J.L.;
RT   "A novel histone fold domain-containing protein that replaces TAF6 in
RT   Drosophila SAGA is required for SAGA-dependent gene expression.";
RL   Genes Dev. 23:2818-2823(2009).
```

Source SHA-256: `13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)  
**Locator:** `lines 104-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 167 / 3.  
**Retrieved:** 2026-11-02T04:33:49.946751+00:00.  

```text
RN   [7] {ECO:0000305}
RP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, SUBCELLULAR LOCATION, AND
RP   IDENTIFICATION BY MASS SPECTROMETRY.
RX   PubMed=24493646; DOI=10.1101/gad.225151.113;
RA   Mohan R.D., Dialynas G., Weake V.M., Liu J., Martin-Brown S., Florens L.,
RA   Washburn M.P., Workman J.L., Abmayr S.M.;
RT   "Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination
RT   and leads to neural and retinal degeneration.";
RL   Genes Dev. 28:259-272(2014).
```

Source SHA-256: `13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)  
**Locator:** `lines 141-142`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 167 / 3.  
**Retrieved:** 2026-11-02T04:33:49.946751+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:20008933,
CC       ECO:0000269|PubMed:24493646}.
```

Source SHA-256: `13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VX12?format=txt&versions=167)  
**Locator:** `lines 172-172`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 167 / 3.  
**Retrieved:** 2026-11-02T04:33:49.946751+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; IDA:FlyBase.
```

Source SHA-256: `13cc86526c2299139df11f6bcecf17865c802aee49360b817aee509eb152a071`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58002-58025`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005634
name: nucleus
namespace: cellular_component
def: "A membrane-bounded organelle of eukaryotic cells in which chromosomes are housed and replicated. In most cells, the nucleus contains all of the cell's chromosomes except the organellar chromosomes, and is the site of RNA synthesis and processing. In some species, or in specialized cell types, RNA metabolism or DNA replication may be absent." [GOC:curators]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "cell nucleus" EXACT []
synonym: "horsetail nucleus" NARROW [GOC:al, GOC:mah, GOC:vw, PMID:15030757]
xref: NIF_Subcellular:sao1702920020
xref: Wikipedia:Cell_nucleus
is_a: GO:0043231 ! intracellular membrane-bounded organelle

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 158. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
