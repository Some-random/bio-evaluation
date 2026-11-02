# GO_cellular_component_0006

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | uncertain | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key differ; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKSLIGTLGLYCLFILTNNVVSSYGDDLYPLTIMHTNDFHARFEETNVKGNPCKSGEKCIGGLARVLHTIKKIIKEQEKKNIESLYINAGDNFQGTIWYNIGRWNVTSELMNIQPPDVMVLGNHEFDHGIDGLLPFLNNMDKTEIVVANMDARDEPQVAKKIKPFTIIKKKYRNIGVIGVVVEEVPDLANTGKLKFRNESEAILEAARNLKKEDPSVNIIIVVSHVGFDVDKIIAERTGSEVDIIVGGHSHTVLYTGTPPGPEKPEDNYPYVYNHPSGNKVLVVQAVCHAKYVGNLTVFFDKKGKVVTYEGAPIYMDTKVEQDKDVLEAMKPWRKLIDEKTKLVVGRTNVDLPRDICRSEECALGNLYTDSMIYAFGGKENCKSGSTWTTAPIAFVHAGAMRSSLHQGDILYSDALLLSPFTNMVVAYDLPGAQLKAALEFSAAPKNEDEKRRFLQMSGLKVTYNMSRAANNRIVDLKVRTNVCPYDQYENLDEKKTYRVVSPSFLQGGGDGFKMLRDYAKNIQNQKIDLDALVDYLKKFSPLAPKAEGRITIIH

[Multiple Choices]
A. aggresome
B. cytoplasmic vesicle
C. host cell plasma membrane
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

### Expected-answer support: uncertain

> The sequence-matched record assigns plasma membrane by computational IEA:TreeGrafter, which supports D as an annotation, but the record also reports secretion and extracellular localization with experimental evidence. That evidence does not establish plasma membrane as the protein's primary location, nor does it definitively rule out some plasma-membrane association.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secretion signal, while the sequence does not show an obvious retained transmembrane anchor. This suggests secretion rather than residence at the plasma membrane, but does not distinguish the offered compartments in favor of D.


**Missing item-specific fact**

> Choosing D depends on the protein-specific GO plasma-membrane annotation, which is an IEA:TreeGrafter inference; resolving its actual primary localization also requires the protein-specific experimental evidence for secretion/extracellular localization.


**Reason**

> The supplied sequence offers no defensible general biological argument for selecting plasma membrane over the other listed options. The relevant evidence is protein-specific annotation and localization data absent from the original question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed options omit secretion and extracellular space, the locations supported by the experimental evidence. D has a computational GO annotation, but the supplied evidence does not establish it as the primary location; no second listed option is clearly supported.


### Important caveats

- The sequence match identifies the same protein record, but reviewer-only accession and database evidence were not available to the evaluated model.
- The plasma-membrane annotation is computationally inferred; the secretion and extracellular annotations cite experimental evidence.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, while the sequence does not show an obvious retained transmembrane anchor. This suggests secretion rather than residence at the plasma membrane, but does not distinguish the offered compartments in favor of D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Choosing D depends on the protein-specific GO plasma-membrane annotation, which is an IEA:TreeGrafter inference; resolving its actual primary localization also requires the protein-specific experimental evidence for secretion/extracellular localization.",
    "reason": "The supplied sequence offers no defensible general biological argument for selecting plasma membrane over the other listed options. The relevant evidence is protein-specific annotation and localization data absent from the original question."
  },
  "case_id": "GO_cellular_component_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "cannot_determine",
    "reason": "The sequence-matched record assigns plasma membrane by computational IEA:TreeGrafter, which supports D as an annotation, but the record also reports secretion and extracellular localization with experimental evidence. That evidence does not establish plasma membrane as the protein's primary location, nor does it definitively rule out some plasma-membrane association."
  },
  "important_caveats": [
    "The sequence match identifies the same protein record, but reviewer-only accession and database evidence were not available to the evaluated model.",
    "The plasma-membrane annotation is computationally inferred; the secretion and extracellular annotations cite experimental evidence.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed options omit secretion and extracellular space, the locations supported by the experimental evidence. D has a computational GO annotation, but the supplied evidence does not establish it as the primary location; no second listed option is clearly supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0006",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The sequence-matched record assigns plasma membrane by computational IEA:TreeGrafter, which supports D as an annotation, but the record also reports secretion and extracellular localization with experimental evidence. That evidence does not establish plasma membrane as the protein's primary location, nor does it definitively rule out some plasma-membrane association.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, while the sequence does not show an obvious retained transmembrane anchor. This suggests secretion rather than residence at the plasma membrane, but does not distinguish the offered compartments in favor of D.",
    "missing_item_specific_fact": "Choosing D depends on the protein-specific GO plasma-membrane annotation, which is an IEA:TreeGrafter inference; resolving its actual primary localization also requires the protein-specific experimental evidence for secretion/extracellular localization.",
    "reason": "The supplied sequence offers no defensible general biological argument for selecting plasma membrane over the other listed options. The relevant evidence is protein-specific annotation and localization data absent from the original question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed options omit secretion and extracellular space, the locations supported by the experimental evidence. D has a computational GO annotation, but the supplied evidence does not establish it as the primary location; no second listed option is clearly supported."
  },
  "important_caveats": [
    "The sequence match identifies the same protein record, but reviewer-only accession and database evidence were not available to the evaluated model.",
    "The plasma-membrane annotation is computationally inferred; the secretion and extracellular annotations cite experimental evidence.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The experimentally determined subcellular location of Q95P65 (5'-nucleotidase-related protein from Glossina morsitans morsitans) is 'Secreted' with direct assay evidence (ECO:0000269, PubMed:20351782). The corresponding GO annotations are GO:0005576 (extracellular region) and GO:0005615 (extracellular space), both IDA:UniProtKB (Inferred by Direct Assay). The 'plasma membrane' annotation (GO:0005886) is supported ONLY by IEA:TreeGrafter, a purely automated computational inference from sequence similarity, which is the lowest-confidence annotation type and directly conflicts with the experimental secretion evidence. The protein is a soluble salivary enzyme (EC 3.6.1.5) with a signal peptide, not a membrane-embedded protein. The expected answer 'plasma membrane' is contradicted by the primary experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal sequence 'MKSLIGTLGLYCLFILTNN' resembles a signal peptide, which could suggest secretion or membrane targeting. However, a signal peptide alone does not distinguish 'plasma membrane' from 'cytoplasmic vesicle' or 'secreted/extracellular.' The protein lacks obvious transmembrane helices. A model reasoning from sequence would most naturally infer secretion (extracellular), which is not among the options. Choosing 'plasma membrane' over 'cytoplasmic vesicle' for a signal-peptide-containing nucleotidase requires knowing the specific annotation or recognizing this exact protein.


**Missing item-specific fact**

> The specific UniProt annotation (Secreted/extracellular, IDA) versus the TreeGrafter computational annotation (plasma membrane, IEA) for this exact protein. Additionally, the fact that the experimentally correct location (secreted/extracellular) is absent from the answer choices, forcing selection of the weakest computational annotation as 'correct,' is an item-specific database fact not derivable from sequence reasoning.


**Reason**

> The sequence provides a signal peptide hint but cannot distinguish plasma membrane from cytoplasmic vesicle or secreted/extracellular localization. The correct experimental answer (secreted) is not offered. Selection of 'plasma membrane' depends entirely on knowing the TreeGrafter annotation for this specific protein, which is a lookup task.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "D"
]
```

> The experimentally supported location (secreted/extracellular region/space) is not among the four options. Among the given choices, 'plasma membrane' (D) is the expected answer but is supported only by a low-confidence computational annotation (IEA:TreeGrafter) that contradicts the experimental evidence. 'Cytoplasmic vesicle' (B) could be argued as a transit compartment for a secreted protein. 'Host cell plasma membrane' (C) is a GO term for viral/pathogen contexts and is clearly inapplicable. 'Aggresome' (A) is clearly wrong. The question is fundamentally flawed because the true experimental answer is absent from the options.


### Important caveats

- The expected answer 'plasma membrane' is supported only by an IEA:TreeGrafter automated annotation, which is a computational similarity-based inference, not experimental evidence.
- The direct experimental evidence (ECO:0000269, IDA) places this protein in the secreted/extracellular compartment, contradicting the plasma membrane annotation.
- The correct experimental localization (secreted, extracellular region, extracellular space) is not offered as an answer choice, making the question structurally problematic.
- The protein is a soluble salivary enzyme (5'-nucleotidase, EC 3.6.1.5) from tsetse fly saliva with anti-platelet-aggregation activity, consistent with secretion rather than membrane residence.
- TreeGrafter annotations propagate GO terms by sequence similarity and are known to produce spurious membrane annotations for secreted homologs of membrane-bound enzymes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MKSLIGTLGLYCLFILTNN' resembles a signal peptide, which could suggest secretion or membrane targeting. However, a signal peptide alone does not distinguish 'plasma membrane' from 'cytoplasmic vesicle' or 'secreted/extracellular.' The protein lacks obvious transmembrane helices. A model reasoning from sequence would most naturally infer secretion (extracellular), which is not among the options. Choosing 'plasma membrane' over 'cytoplasmic vesicle' for a signal-peptide-containing nucleotidase requires knowing the specific annotation or recognizing this exact protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt annotation (Secreted/extracellular, IDA) versus the TreeGrafter computational annotation (plasma membrane, IEA) for this exact protein. Additionally, the fact that the experimentally correct location (secreted/extracellular) is absent from the answer choices, forcing selection of the weakest computational annotation as 'correct,' is an item-specific database fact not derivable from sequence reasoning.",
    "reason": "The sequence provides a signal peptide hint but cannot distinguish plasma membrane from cytoplasmic vesicle or secreted/extracellular localization. The correct experimental answer (secreted) is not offered. Selection of 'plasma membrane' depends entirely on knowing the TreeGrafter annotation for this specific protein, which is a lookup task."
  },
  "case_id": "GO_cellular_component_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "H2"
    ],
    "judgment": "contradicted",
    "reason": "The experimentally determined subcellular location of Q95P65 (5'-nucleotidase-related protein from Glossina morsitans morsitans) is 'Secreted' with direct assay evidence (ECO:0000269, PubMed:20351782). The corresponding GO annotations are GO:0005576 (extracellular region) and GO:0005615 (extracellular space), both IDA:UniProtKB (Inferred by Direct Assay). The 'plasma membrane' annotation (GO:0005886) is supported ONLY by IEA:TreeGrafter, a purely automated computational inference from sequence similarity, which is the lowest-confidence annotation type and directly conflicts with the experimental secretion evidence. The protein is a soluble salivary enzyme (EC 3.6.1.5) with a signal peptide, not a membrane-embedded protein. The expected answer 'plasma membrane' is contradicted by the primary experimental evidence."
  },
  "important_caveats": [
    "The expected answer 'plasma membrane' is supported only by an IEA:TreeGrafter automated annotation, which is a computational similarity-based inference, not experimental evidence.",
    "The direct experimental evidence (ECO:0000269, IDA) places this protein in the secreted/extracellular compartment, contradicting the plasma membrane annotation.",
    "The correct experimental localization (secreted, extracellular region, extracellular space) is not offered as an answer choice, making the question structurally problematic.",
    "The protein is a soluble salivary enzyme (5'-nucleotidase, EC 3.6.1.5) from tsetse fly saliva with anti-platelet-aggregation activity, consistent with secretion rather than membrane residence.",
    "TreeGrafter annotations propagate GO terms by sequence similarity and are known to produce spurious membrane annotations for secreted homologs of membrane-bound enzymes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "D"
    ],
    "reason": "The experimentally supported location (secreted/extracellular region/space) is not among the four options. Among the given choices, 'plasma membrane' (D) is the expected answer but is supported only by a low-confidence computational annotation (IEA:TreeGrafter) that contradicts the experimental evidence. 'Cytoplasmic vesicle' (B) could be argued as a transit compartment for a secreted protein. 'Host cell plasma membrane' (C) is a GO term for viral/pathogen contexts and is clearly inapplicable. 'Aggresome' (A) is clearly wrong. The question is fundamentally flawed because the true experimental answer is absent from the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0006",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The experimentally determined subcellular location of Q95P65 (5'-nucleotidase-related protein from Glossina morsitans morsitans) is 'Secreted' with direct assay evidence (ECO:0000269, PubMed:20351782). The corresponding GO annotations are GO:0005576 (extracellular region) and GO:0005615 (extracellular space), both IDA:UniProtKB (Inferred by Direct Assay). The 'plasma membrane' annotation (GO:0005886) is supported ONLY by IEA:TreeGrafter, a purely automated computational inference from sequence similarity, which is the lowest-confidence annotation type and directly conflicts with the experimental secretion evidence. The protein is a soluble salivary enzyme (EC 3.6.1.5) with a signal peptide, not a membrane-embedded protein. The expected answer 'plasma membrane' is contradicted by the primary experimental evidence.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal sequence 'MKSLIGTLGLYCLFILTNN' resembles a signal peptide, which could suggest secretion or membrane targeting. However, a signal peptide alone does not distinguish 'plasma membrane' from 'cytoplasmic vesicle' or 'secreted/extracellular.' The protein lacks obvious transmembrane helices. A model reasoning from sequence would most naturally infer secretion (extracellular), which is not among the options. Choosing 'plasma membrane' over 'cytoplasmic vesicle' for a signal-peptide-containing nucleotidase requires knowing the specific annotation or recognizing this exact protein.",
    "missing_item_specific_fact": "The specific UniProt annotation (Secreted/extracellular, IDA) versus the TreeGrafter computational annotation (plasma membrane, IEA) for this exact protein. Additionally, the fact that the experimentally correct location (secreted/extracellular) is absent from the answer choices, forcing selection of the weakest computational annotation as 'correct,' is an item-specific database fact not derivable from sequence reasoning.",
    "reason": "The sequence provides a signal peptide hint but cannot distinguish plasma membrane from cytoplasmic vesicle or secreted/extracellular localization. The correct experimental answer (secreted) is not offered. Selection of 'plasma membrane' depends entirely on knowing the TreeGrafter annotation for this specific protein, which is a lookup task."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["D"],
    "reason": "The experimentally supported location (secreted/extracellular region/space) is not among the four options. Among the given choices, 'plasma membrane' (D) is the expected answer but is supported only by a low-confidence computational annotation (IEA:TreeGrafter) that contradicts the experimental evidence. 'Cytoplasmic vesicle' (B) could be argued as a transit compartment for a secreted protein. 'Host cell plasma membrane' (C) is a GO term for viral/pathogen contexts and is clearly inapplicable. 'Aggresome' (A) is clearly wrong. The question is fundamentally flawed because the true experimental answer is absent from the options."
  },
  "important_caveats": [
    "The expected answer 'plasma membrane' is supported only by an IEA:TreeGrafter automated annotation, which is a computational similarity-based inference, not experimental evidence.",
    "The direct experimental evidence (ECO:0000269, IDA) places this protein in the secreted/extracellular compartment, contradicting the plasma membrane annotation.",
    "The correct experimental localization (secreted, extracellular region, extracellular space) is not offered as an answer choice, making the question structurally problematic.",
    "The protein is a soluble salivary enzyme (5'-nucleotidase, EC 3.6.1.5) from tsetse fly saliva with anti-platelet-aggregation activity, consistent with secretion rather than membrane residence.",
    "TreeGrafter annotations propagate GO terms by sequence similarity and are known to produce spurious membrane annotations for secreted homologs of membrane-bound enzymes."
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

**Accession:** `Q95P65` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 83. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.918010+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"20351782","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}}]}
```

Source SHA-256: `b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.918010+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"20351782","source":"PubMed"}],"id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.918010+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:28:44.138990+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, TISSUE SPECIFICITY,
RP   AND DISRUPTION PHENOTYPE.
RX   PubMed=20351782; DOI=10.1371/journal.pone.0009671;
RA   Caljon G., De Ridder K., De Baetselier P., Coosemans M.,
RA   Van Den Abbeele J.;
RT   "Identification of a tsetse fly salivary protein with dual inhibitory
RT   action on human platelet aggregation.";
RL   PLoS ONE 5:e9671-e9671(2010).
```

Source SHA-256: `8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:28:44.138990+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:20351782}.
```

Source SHA-256: `8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)  
**Locator:** `lines 98-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:28:44.138990+00:00.  

```text
DR   GO; GO:0005615; C:extracellular space; IDA:UniProtKB.
```

Source SHA-256: `8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)  
**Locator:** `lines 99-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:28:44.138990+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.
```

Source SHA-256: `8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
