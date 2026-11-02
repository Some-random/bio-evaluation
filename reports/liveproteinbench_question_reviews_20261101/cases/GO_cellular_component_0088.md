# GO_cellular_component_0088

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — SAGA complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLTDRVLATKEALVVALGDNWERYRANMKNWFRSRWTKEEFDAESRKILTPDKLHLHNQFLLALLNKIDAFAPLENPPAVQTSSSSGNRSKRRKRSSRTFAERLNFELSDVLDFVAEDNMQIIRPPTTIGIPSDQQQQQLQSQRYCAQELFLPDAGFIMGRFLIGAWEIGLVSVDDNVAEYVAMAVQVLLKDLLSAIIKKRKHYKTSGEGNFYYDVGAPLRDPSLRNTVTRQKVDDTPLELDKELNTANFMRRQNDDVTFLSACEEVQPTERTVITLKDCQLALRDRNLIGSHAVYSINMERLNMMMH

[Multiple Choices]
A. microvillus membrane
B. transcription regulator complex
C. endoplasmic reticulum membrane
D. SAGA complex
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

> The exact sequence matches the Drosophila protein annotated to the SAGA complex. UniProt records a FlyBase IDA annotation for SAGA, and the cited study is described as identifying the protein as a SAGA subunit. This supports D as a cellular component, though the evidence is reviewer-only and the original source snapshot is unknown.

Citations as saved: [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's basic regions are compatible with nuclear localization, and it lacks an obvious long transmembrane segment, which weighs against the membrane options. But those clues do not establish membership in SAGA rather than another transcription-associated complex.


**Missing item-specific fact**

> The protein-specific fact that this Drosophila protein is a SAGA subunit, established by annotation and cited experimental work.


**Reason**

> Distinguishing the specific SAGA complex from the broader transcription regulator complex requires knowledge of this protein's complex membership; the sequence and choices alone do not provide a reliable discriminator.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> D is the specific supported complex. B is also plausibly defensible as a broader category because SAGA regulates transcription; the question does not specify that only the most specific GO term should be selected.


### Important caveats

- The sequence match and cited annotations support the key, but the reviewer-only accession and annotations were not supplied to the evaluated model.
- The protein is also annotated to the nucleus, which is not among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's basic regions are compatible with nuclear localization, and it lacks an obvious long transmembrane segment, which weighs against the membrane options. But those clues do not establish membership in SAGA rather than another transcription-associated complex.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this Drosophila protein is a SAGA subunit, established by annotation and cited experimental work.",
    "reason": "Distinguishing the specific SAGA complex from the broader transcription regulator complex requires knowledge of this protein's complex membership; the sequence and choices alone do not provide a reliable discriminator."
  },
  "case_id": "GO_cellular_component_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C8",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila protein annotated to the SAGA complex. UniProt records a FlyBase IDA annotation for SAGA, and the cited study is described as identifying the protein as a SAGA subunit. This supports D as a cellular component, though the evidence is reviewer-only and the original source snapshot is unknown."
  },
  "important_caveats": [
    "The sequence match and cited annotations support the key, but the reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The protein is also annotated to the nucleus, which is not among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "D is the specific supported complex. B is also plausibly defensible as a broader category because SAGA regulates transcription; the question does not specify that only the most specific GO term should be selected."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila protein annotated to the SAGA complex. UniProt records a FlyBase IDA annotation for SAGA, and the cited study is described as identifying the protein as a SAGA subunit. This supports D as a cellular component, though the evidence is reviewer-only and the original source snapshot is unknown.",
    "evidence_ids": ["C7", "C8", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's basic regions are compatible with nuclear localization, and it lacks an obvious long transmembrane segment, which weighs against the membrane options. But those clues do not establish membership in SAGA rather than another transcription-associated complex.",
    "missing_item_specific_fact": "The protein-specific fact that this Drosophila protein is a SAGA subunit, established by annotation and cited experimental work.",
    "reason": "Distinguishing the specific SAGA complex from the broader transcription regulator complex requires knowledge of this protein's complex membership; the sequence and choices alone do not provide a reliable discriminator."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "D is the specific supported complex. B is also plausibly defensible as a broader category because SAGA regulates transcription; the question does not specify that only the most specific GO term should be selected."
  },
  "important_caveats": [
    "The sequence match and cited annotations support the key, but the reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The protein is also annotated to the nucleus, which is not among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q8IPA1 (TAD12_DROME, Transcriptional adapter 1-2, Drosophila melanogaster). GO:0000124 (C:SAGA complex) is annotated with IDA:FlyBase evidence, supported by experimental identification in the SAGA complex via mass spectrometry in three independent studies (PubMed:16980620, 21764853, 24493646). The UniProt SUBCELLULAR LOCATION comment also notes 'Nucleus' (GO:0005634), but among the provided options, SAGA complex is the most specific and directly experimentally supported annotation.

Citations as saved: [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H6](#evidence-h6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence lacks transmembrane domains, which helps rule out options A (microvillus membrane) and C (endoplasmic reticulum membrane) via general biophysical reasoning. However, the critical distinction between B (transcription regulator complex) and D (SAGA complex) cannot be made from sequence features alone. Both are nuclear transcription-associated complexes. The sequence contains no motifs that specifically indicate SAGA complex membership (e.g., specific protein-protein interaction domains unique to SAGA subunits) versus general transcription regulation. Distinguishing B from D requires knowing that this specific protein is Ada1-2, a well-characterized SAGA complex subunit identified experimentally by mass spectrometry.


**Missing item-specific fact**

> The specific experimental identification of this protein (Ada1-2/Q8IPA1) as a SAGA complex subunit via mass spectrometry co-purification. Without recognizing the protein identity and recalling its complex membership, the sequence provides no basis to prefer 'SAGA complex' over 'transcription regulator complex.'


**Reason**

> While general reasoning can eliminate membrane-localized options (A, C), the choice between the two nuclear transcription-related complexes (B vs D) depends entirely on protein-specific experimental annotation. The sequence does not encode distinguishing features between a generic transcription regulator and a specific SAGA subunit. Recognizing the exact sequence as Ada1-2 and recalling its SAGA membership constitutes memorization of a database entry, not reasoning from sequence properties.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The SAGA complex is a transcription-regulating coactivator complex. A model reasoning that this is a transcription-related nuclear protein could plausibly select B (transcription regulator complex, GO:0005667) as a general description. In the provided GO ontology, GO:0000124 (SAGA complex) is not listed as a subclass of GO:0005667 (transcription regulator complex), so they are technically separate terms, but biologically the SAGA complex does regulate transcription. Without the specific annotation, B is a reasonable general answer. However, the direct IDA annotation to GO:0000124 makes D the most precise and evidence-supported choice.


### Important caveats

- The UniProt annotation for SAGA complex membership (GO:0000124) carries IDA:FlyBase evidence codes, indicating experimental (mass spectrometry) support rather than computational inference.
- The protein is also annotated to GO:0005634 (nucleus), which is not among the options; the question asks for the 'primary Cellular Component' but the options do not include 'nucleus' itself.
- The GO ontology excerpt shows SAGA complex (GO:0000124) is_a GO:0070461 (SAGA-type complex) and is_a GO:1905368 (peptidase complex), but does not show it as a subclass of transcription regulator complex (GO:0005667), making B and D formally distinct terms.
- The protein name 'Transcriptional adapter 1-2' hints at transcription function but does not specify SAGA membership without prior knowledge of the Ada1 protein family.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks transmembrane domains, which helps rule out options A (microvillus membrane) and C (endoplasmic reticulum membrane) via general biophysical reasoning. However, the critical distinction between B (transcription regulator complex) and D (SAGA complex) cannot be made from sequence features alone. Both are nuclear transcription-associated complexes. The sequence contains no motifs that specifically indicate SAGA complex membership (e.g., specific protein-protein interaction domains unique to SAGA subunits) versus general transcription regulation. Distinguishing B from D requires knowing that this specific protein is Ada1-2, a well-characterized SAGA complex subunit identified experimentally by mass spectrometry.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental identification of this protein (Ada1-2/Q8IPA1) as a SAGA complex subunit via mass spectrometry co-purification. Without recognizing the protein identity and recalling its complex membership, the sequence provides no basis to prefer 'SAGA complex' over 'transcription regulator complex.'",
    "reason": "While general reasoning can eliminate membrane-localized options (A, C), the choice between the two nuclear transcription-related complexes (B vs D) depends entirely on protein-specific experimental annotation. The sequence does not encode distinguishing features between a generic transcription regulator and a specific SAGA subunit. Recognizing the exact sequence as Ada1-2 and recalling its SAGA membership constitutes memorization of a database entry, not reasoning from sequence properties."
  },
  "case_id": "GO_cellular_component_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C8",
      "C9",
      "C10",
      "H6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q8IPA1 (TAD12_DROME, Transcriptional adapter 1-2, Drosophila melanogaster). GO:0000124 (C:SAGA complex) is annotated with IDA:FlyBase evidence, supported by experimental identification in the SAGA complex via mass spectrometry in three independent studies (PubMed:16980620, 21764853, 24493646). The UniProt SUBCELLULAR LOCATION comment also notes 'Nucleus' (GO:0005634), but among the provided options, SAGA complex is the most specific and directly experimentally supported annotation."
  },
  "important_caveats": [
    "The UniProt annotation for SAGA complex membership (GO:0000124) carries IDA:FlyBase evidence codes, indicating experimental (mass spectrometry) support rather than computational inference.",
    "The protein is also annotated to GO:0005634 (nucleus), which is not among the options; the question asks for the 'primary Cellular Component' but the options do not include 'nucleus' itself.",
    "The GO ontology excerpt shows SAGA complex (GO:0000124) is_a GO:0070461 (SAGA-type complex) and is_a GO:1905368 (peptidase complex), but does not show it as a subclass of transcription regulator complex (GO:0005667), making B and D formally distinct terms.",
    "The protein name 'Transcriptional adapter 1-2' hints at transcription function but does not specify SAGA membership without prior knowledge of the Ada1 protein family."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The SAGA complex is a transcription-regulating coactivator complex. A model reasoning that this is a transcription-related nuclear protein could plausibly select B (transcription regulator complex, GO:0005667) as a general description. In the provided GO ontology, GO:0000124 (SAGA complex) is not listed as a subclass of GO:0005667 (transcription regulator complex), so they are technically separate terms, but biologically the SAGA complex does regulate transcription. Without the specific annotation, B is a reasonable general answer. However, the direct IDA annotation to GO:0000124 makes D the most precise and evidence-supported choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q8IPA1 (TAD12_DROME, Transcriptional adapter 1-2, Drosophila melanogaster). GO:0000124 (C:SAGA complex) is annotated with IDA:FlyBase evidence, supported by experimental identification in the SAGA complex via mass spectrometry in three independent studies (PubMed:16980620, 21764853, 24493646). The UniProt SUBCELLULAR LOCATION comment also notes 'Nucleus' (GO:0005634), but among the provided options, SAGA complex is the most specific and directly experimentally supported annotation.",
    "evidence_ids": ["C7", "C8", "C9", "C10", "H6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence lacks transmembrane domains, which helps rule out options A (microvillus membrane) and C (endoplasmic reticulum membrane) via general biophysical reasoning. However, the critical distinction between B (transcription regulator complex) and D (SAGA complex) cannot be made from sequence features alone. Both are nuclear transcription-associated complexes. The sequence contains no motifs that specifically indicate SAGA complex membership (e.g., specific protein-protein interaction domains unique to SAGA subunits) versus general transcription regulation. Distinguishing B from D requires knowing that this specific protein is Ada1-2, a well-characterized SAGA complex subunit identified experimentally by mass spectrometry.",
    "missing_item_specific_fact": "The specific experimental identification of this protein (Ada1-2/Q8IPA1) as a SAGA complex subunit via mass spectrometry co-purification. Without recognizing the protein identity and recalling its complex membership, the sequence provides no basis to prefer 'SAGA complex' over 'transcription regulator complex.'",
    "reason": "While general reasoning can eliminate membrane-localized options (A, C), the choice between the two nuclear transcription-related complexes (B vs D) depends entirely on protein-specific experimental annotation. The sequence does not encode distinguishing features between a generic transcription regulator and a specific SAGA subunit. Recognizing the exact sequence as Ada1-2 and recalling its SAGA membership constitutes memorization of a database entry, not reasoning from sequence properties."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The SAGA complex is a transcription-regulating coactivator complex. A model reasoning that this is a transcription-related nuclear protein could plausibly select B (transcription regulator complex, GO:0005667) as a general description. In the provided GO ontology, GO:0000124 (SAGA complex) is not listed as a subclass of GO:0005667 (transcription regulator complex), so they are technically separate terms, but biologically the SAGA complex does regulate transcription. Without the specific annotation, B is a reasonable general answer. However, the direct IDA annotation to GO:0000124 makes D the most precise and evidence-supported choice."
  },
  "important_caveats": [
    "The UniProt annotation for SAGA complex membership (GO:0000124) carries IDA:FlyBase evidence codes, indicating experimental (mass spectrometry) support rather than computational inference.",
    "The protein is also annotated to GO:0005634 (nucleus), which is not among the options; the question asks for the 'primary Cellular Component' but the options do not include 'nucleus' itself.",
    "The GO ontology excerpt shows SAGA complex (GO:0000124) is_a GO:0070461 (SAGA-type complex) and is_a GO:1905368 (peptidase complex), but does not show it as a subclass of transcription regulator complex (GO:0005667), making B and D formally distinct terms.",
    "The protein name 'Transcriptional adapter 1-2' hints at transcription function but does not specify SAGA membership without prior knowledge of the Ada1 protein family."
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

**Accession:** `Q8IPA1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 169. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)  
**Locator:** `/uniProtKBCrossReferences/28`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:17.256572+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"16980620","source":"PubMed"},{"evidenceCode":"ECO:0000314","id":"21764853","source":"PubMed"}],"id":"GO:0000124","properties":[{"key":"GoTerm","value":"C:SAGA complex"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:17.256572+00:00.  

```json
{"citation":{"authors":["Guelman S.","Suganuma T.","Florens L.","Weake V.","Swanson S.K.","Washburn M.P.","Abmayr S.M.","Workman J.L."],"citationCrossReferences":[{"database":"PubMed","id":"16980620"},{"database":"DOI","id":"10.1128/mcb.00130-06"}],"citationType":"journal article","firstPage":"7178","id":"16980620","journal":"Mol. Cell. Biol.","lastPage":"7189","publicationDate":"2006","title":"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA required for histone H3 acetylation.","volume":"26"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","IDENTIFICATION IN SAGA COMPLEX","INTERACTION WITH GCN5; SPT3 AND ADA2B","IDENTIFICATION BY MASS SPECTROMETRY"]}
```

Source SHA-256: `40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:17.256572+00:00.  

```json
{"citation":{"authors":["Weake V.M.","Dyer J.O.","Seidel C.","Box A.","Swanson S.K.","Peak A.","Florens L.","Washburn M.P.","Abmayr S.M.","Workman J.L."],"citationCrossReferences":[{"database":"PubMed","id":"21764853"},{"database":"DOI","id":"10.1101/gad.2046211"}],"citationType":"journal article","firstPage":"1499","id":"21764853","journal":"Genes Dev.","lastPage":"1509","publicationDate":"2011","title":"Post-transcription initiation function of the ubiquitous SAGA complex in tissue-specific gene activation.","volume":"25"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","IDENTIFICATION IN SAGA COMPLEX","DEVELOPMENTAL STAGE","IDENTIFICATION BY MASS SPECTROMETRY"]}
```

Source SHA-256: `40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPA1.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:17.256572+00:00.  

```json
{"citation":{"authors":["Mohan R.D.","Dialynas G.","Weake V.M.","Liu J.","Martin-Brown S.","Florens L.","Washburn M.P.","Workman J.L.","Abmayr S.M."],"citationCrossReferences":[{"database":"PubMed","id":"24493646"},{"database":"DOI","id":"10.1101/gad.225151.113"}],"citationType":"journal article","firstPage":"259","id":"24493646","journal":"Genes Dev.","lastPage":"272","publicationDate":"2014","title":"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination and leads to neural and retinal degeneration.","volume":"28"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":6,"referencePositions":["FUNCTION","IDENTIFICATION IN THE SAGA COMPLEX","SUBCELLULAR LOCATION","IDENTIFICATION BY MASS SPECTROMETRY"]}
```

Source SHA-256: `40c1a185721f3b79fef0b945c4adb9dba009ce28a7482b261b9fcc948ecfb70c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)  
**Locator:** `lines 75-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 169 / 1.  
**Retrieved:** 2026-11-02T04:32:22.664157+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, INTERACTION WITH GCN5; SPT3 AND
RP   ADA2B, AND IDENTIFICATION BY MASS SPECTROMETRY.
RX   PubMed=16980620; DOI=10.1128/mcb.00130-06;
RA   Guelman S., Suganuma T., Florens L., Weake V., Swanson S.K., Washburn M.P.,
RA   Abmayr S.M., Workman J.L.;
RT   "The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA
RT   required for histone H3 acetylation.";
RL   Mol. Cell. Biol. 26:7178-7189(2006).
```

Source SHA-256: `87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)  
**Locator:** `lines 93-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 169 / 1.  
**Retrieved:** 2026-11-02T04:32:22.664157+00:00.  

```text
RN   [6] {ECO:0000305}
RP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, SUBCELLULAR LOCATION, AND
RP   IDENTIFICATION BY MASS SPECTROMETRY.
RX   PubMed=24493646; DOI=10.1101/gad.225151.113;
RA   Mohan R.D., Dialynas G., Weake V.M., Liu J., Martin-Brown S., Florens L.,
RA   Washburn M.P., Workman J.L., Abmayr S.M.;
RT   "Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination
RT   and leads to neural and retinal degeneration.";
RL   Genes Dev. 28:259-272(2014).
```

Source SHA-256: `87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPA1?format=txt&versions=169)  
**Locator:** `lines 167-167`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 169 / 1.  
**Retrieved:** 2026-11-02T04:32:22.664157+00:00.  

```text
DR   GO; GO:0000124; C:SAGA complex; IDA:FlyBase.
```

Source SHA-256: `87b4f639978e8cd9a90e850c629bd1d8f14c1311dd821d2e2a5b2077e408431a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 88. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
