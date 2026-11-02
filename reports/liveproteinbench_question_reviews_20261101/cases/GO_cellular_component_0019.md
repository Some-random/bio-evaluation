# GO_cellular_component_0019

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — mitochondrial membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MALSRAKPDELPRDAVVITEDQALKYQWKIITSWDKIGEVWSLRYTPGILSALAAGTGAYINNHYRTKLRLGGHGRLSTYLPIVAVPAIFTMLAHKFFIQRPILLNPLGECPVCIQMRSAAFQTSLGIVYPTILAPFAAFLFATRCYTYRIPSITENPREVFLLWRKFTRPIVPALGTLIGLQALLTMFLTGQEDKQNFKLMLRMREIEHQVEEEHLPQRMDF

[Multiple Choices]
A. host cell mitochondrion
B. trans-Golgi network membrane
C. spindle
D. mitochondrial membrane
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

> The sequence matches the annotated Drosophila protein. Its mitochondrial-membrane annotation is transferred by similarity, while the record also includes experimentally supported mitochondrial localization and complex I assembly-complex localization. These support choice D, though the membrane-specific annotation is not itself direct experimental evidence in the cited record.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence appears to encode a multipass membrane protein, which weighs against spindle and is consistent with a membrane location. Hydrophobic segments alone do not distinguish mitochondrial membrane from trans-Golgi network membrane, nor establish the protein-specific mitochondrial association.


**Missing item-specific fact**

> The protein-specific association with mitochondrial complex I biogenesis and mitochondrial localization.


**Reason**

> The exact distinction needed for D relies on protein-specific annotation or experimental knowledge not supplied with the sequence. Recognizing the sequence or naming a predictor would not provide an input-based biological argument for that location.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports the more specific choice, mitochondrial membrane. Although that is within a mitochondrion, option A is the distinct GO term “host cell mitochondrion,” not a general alternative for mitochondrial membrane.


### Important caveats

- The mitochondrial-membrane subcellular-location annotation is transferred by similarity; the cited experimental GO annotations support mitochondrial and complex I assembly-complex localization.
- The author’s exact source snapshot is unknown, but the supplied sequence matches both current and historical records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence appears to encode a multipass membrane protein, which weighs against spindle and is consistent with a membrane location. Hydrophobic segments alone do not distinguish mitochondrial membrane from trans-Golgi network membrane, nor establish the protein-specific mitochondrial association.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific association with mitochondrial complex I biogenesis and mitochondrial localization.",
    "reason": "The exact distinction needed for D relies on protein-specific annotation or experimental knowledge not supplied with the sequence. Recognizing the sequence or naming a predictor would not provide an input-based biological argument for that location."
  },
  "case_id": "GO_cellular_component_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C8",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated Drosophila protein. Its mitochondrial-membrane annotation is transferred by similarity, while the record also includes experimentally supported mitochondrial localization and complex I assembly-complex localization. These support choice D, though the membrane-specific annotation is not itself direct experimental evidence in the cited record."
  },
  "important_caveats": [
    "The mitochondrial-membrane subcellular-location annotation is transferred by similarity; the cited experimental GO annotations support mitochondrial and complex I assembly-complex localization.",
    "The author’s exact source snapshot is unknown, but the supplied sequence matches both current and historical records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the more specific choice, mitochondrial membrane. Although that is within a mitochondrion, option A is the distinct GO term “host cell mitochondrion,” not a general alternative for mitochondrial membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated Drosophila protein. Its mitochondrial-membrane annotation is transferred by similarity, while the record also includes experimentally supported mitochondrial localization and complex I assembly-complex localization. These support choice D, though the membrane-specific annotation is not itself direct experimental evidence in the cited record.",
    "evidence_ids": ["C1", "C5", "C6", "C8", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence appears to encode a multipass membrane protein, which weighs against spindle and is consistent with a membrane location. Hydrophobic segments alone do not distinguish mitochondrial membrane from trans-Golgi network membrane, nor establish the protein-specific mitochondrial association.",
    "missing_item_specific_fact": "The protein-specific association with mitochondrial complex I biogenesis and mitochondrial localization.",
    "reason": "The exact distinction needed for D relies on protein-specific annotation or experimental knowledge not supplied with the sequence. Recognizing the sequence or naming a predictor would not provide an input-based biological argument for that location."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the more specific choice, mitochondrial membrane. Although that is within a mitochondrion, option A is the distinct GO term “host cell mitochondrion,” not a general alternative for mitochondrial membrane."
  },
  "important_caveats": [
    "The mitochondrial-membrane subcellular-location annotation is transferred by similarity; the cited experimental GO annotations support mitochondrial and complex I assembly-complex localization.",
    "The author’s exact source snapshot is unknown, but the supplied sequence matches both current and historical records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VLM7 (TMEM126B/dTMEM126B) is annotated with SUBCELLULAR LOCATION: Mitochondrion membrane (multi-pass membrane protein). GO:0031966 (mitochondrial membrane) is directly annotated (ISS). Additionally, the experimentally supported (IDA:FlyBase) annotation GO:0160295 (mitochondrial complex I intermediate assembly complex) is part_of GO:0005743 (mitochondrial inner membrane), which is_a GO:0031966 (mitochondrial membrane). The 2021 PubMed paper (34386730) confirms involvement in mitochondrial complex I biogenesis. Option D is well-supported by both direct annotation and the ontology hierarchy connecting the MCIA complex to mitochondrial membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3), [GO7](#evidence-go7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Some general reasoning can eliminate C (spindle is a microtubule structure, incompatible with a multi-pass membrane protein) and A (host cell mitochondrion is a GO term reserved for pathogen-host symbiosis contexts, not applicable to a Drosophila protein in its own cell). The absence of a cleavable signal peptide at the N-terminus weakly argues against secretory-pathway compartments like the trans-Golgi network. However, the sequence lacks a canonical N-terminal mitochondrial targeting sequence (positively charged amphipathic helix), and the multi-pass TM topology alone does not distinguish mitochondrial membrane from Golgi membrane. The definitive identification of this protein as TMEM126B / a component of the MCIA complex (mitochondrial complex I intermediate assembly complex) requires protein-specific knowledge not derivable from the bare sequence.


**Missing item-specific fact**

> The identity of this 223-aa protein as Drosophila TMEM126B, a known subunit of the mitochondrial complex I intermediate assembly (MCIA) complex localized to the inner mitochondrial membrane. Without this identification, the multi-pass membrane topology and lack of obvious targeting signals do not conclusively distinguish mitochondrial membrane (D) from trans-Golgi network membrane (B).


**Reason**

> While general reasoning can eliminate spindle (C) and host cell mitochondrion (A) through GO ontology logic and basic biology, the critical D-vs-B distinction for a short multi-pass membrane protein without a canonical mitochondrial presequence or ER signal peptide depends on recognizing the protein's specific identity and its role in complex I assembly. The UniProt 'mitochondrion membrane' annotation itself is ISS (inferred from similarity to human Q8IUX1), underscoring that this localization is not trivially predictable from the Drosophila sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Option A ('host cell mitochondrion', GO:0033650) is technically a mitochondrion term and a model unfamiliar with the GO term's pathogen-specific context might select it over D. However, the GO definition explicitly restricts it to symbiotic/host contexts, making D the correct and more specific answer. Option B (trans-Golgi network membrane) is the most challenging distractor because the sequence provides no definitive targeting signal to exclude it without protein identity knowledge.


### Important caveats

- The direct 'mitochondrion membrane' annotation (C5/H3) carries evidence code ECO:0000250 (similarity to human Q8IUX1), not direct experimental evidence for this Drosophila protein. The IDA experimental evidence (C6, C8) supports 'mitochondrion' and 'MCIA complex' but the membrane specificity comes through the ontology hierarchy (MCIA is part_of inner mitochondrial membrane is_a mitochondrial membrane).
- The UniProt entry was first public on 2025-02-05; the historical snapshot (entry v168, Jan 2026) already contains the mitochondrial membrane annotation, so the key was available at the time of benchmark construction.
- The sequence-match is confirmed (SHA256 match across current and historical records), so the annotation applies to the exact 223-aa sequence provided.
- The absence of a canonical N-terminal mitochondrial targeting presequence in the sequence is notable; TMEM126B is a multi-pass membrane protein whose mitochondrial targeting mechanism differs from the classic N-terminal presequence pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Some general reasoning can eliminate C (spindle is a microtubule structure, incompatible with a multi-pass membrane protein) and A (host cell mitochondrion is a GO term reserved for pathogen-host symbiosis contexts, not applicable to a Drosophila protein in its own cell). The absence of a cleavable signal peptide at the N-terminus weakly argues against secretory-pathway compartments like the trans-Golgi network. However, the sequence lacks a canonical N-terminal mitochondrial targeting sequence (positively charged amphipathic helix), and the multi-pass TM topology alone does not distinguish mitochondrial membrane from Golgi membrane. The definitive identification of this protein as TMEM126B / a component of the MCIA complex (mitochondrial complex I intermediate assembly complex) requires protein-specific knowledge not derivable from the bare sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of this 223-aa protein as Drosophila TMEM126B, a known subunit of the mitochondrial complex I intermediate assembly (MCIA) complex localized to the inner mitochondrial membrane. Without this identification, the multi-pass membrane topology and lack of obvious targeting signals do not conclusively distinguish mitochondrial membrane (D) from trans-Golgi network membrane (B).",
    "reason": "While general reasoning can eliminate spindle (C) and host cell mitochondrion (A) through GO ontology logic and basic biology, the critical D-vs-B distinction for a short multi-pass membrane protein without a canonical mitochondrial presequence or ER signal peptide depends on recognizing the protein's specific identity and its role in complex I assembly. The UniProt 'mitochondrion membrane' annotation itself is ISS (inferred from similarity to human Q8IUX1), underscoring that this localization is not trivially predictable from the Drosophila sequence alone."
  },
  "case_id": "GO_cellular_component_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "GO3",
      "GO7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VLM7 (TMEM126B/dTMEM126B) is annotated with SUBCELLULAR LOCATION: Mitochondrion membrane (multi-pass membrane protein). GO:0031966 (mitochondrial membrane) is directly annotated (ISS). Additionally, the experimentally supported (IDA:FlyBase) annotation GO:0160295 (mitochondrial complex I intermediate assembly complex) is part_of GO:0005743 (mitochondrial inner membrane), which is_a GO:0031966 (mitochondrial membrane). The 2021 PubMed paper (34386730) confirms involvement in mitochondrial complex I biogenesis. Option D is well-supported by both direct annotation and the ontology hierarchy connecting the MCIA complex to mitochondrial membrane."
  },
  "important_caveats": [
    "The direct 'mitochondrion membrane' annotation (C5/H3) carries evidence code ECO:0000250 (similarity to human Q8IUX1), not direct experimental evidence for this Drosophila protein. The IDA experimental evidence (C6, C8) supports 'mitochondrion' and 'MCIA complex' but the membrane specificity comes through the ontology hierarchy (MCIA is part_of inner mitochondrial membrane is_a mitochondrial membrane).",
    "The UniProt entry was first public on 2025-02-05; the historical snapshot (entry v168, Jan 2026) already contains the mitochondrial membrane annotation, so the key was available at the time of benchmark construction.",
    "The sequence-match is confirmed (SHA256 match across current and historical records), so the annotation applies to the exact 223-aa sequence provided.",
    "The absence of a canonical N-terminal mitochondrial targeting presequence in the sequence is notable; TMEM126B is a multi-pass membrane protein whose mitochondrial targeting mechanism differs from the classic N-terminal presequence pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Option A ('host cell mitochondrion', GO:0033650) is technically a mitochondrion term and a model unfamiliar with the GO term's pathogen-specific context might select it over D. However, the GO definition explicitly restricts it to symbiotic/host contexts, making D the correct and more specific answer. Option B (trans-Golgi network membrane) is the most challenging distractor because the sequence provides no definitive targeting signal to exclude it without protein identity knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VLM7 (TMEM126B/dTMEM126B) is annotated with SUBCELLULAR LOCATION: Mitochondrion membrane (multi-pass membrane protein). GO:0031966 (mitochondrial membrane) is directly annotated (ISS). Additionally, the experimentally supported (IDA:FlyBase) annotation GO:0160295 (mitochondrial complex I intermediate assembly complex) is part_of GO:0005743 (mitochondrial inner membrane), which is_a GO:0031966 (mitochondrial membrane). The 2021 PubMed paper (34386730) confirms involvement in mitochondrial complex I biogenesis. Option D is well-supported by both direct annotation and the ontology hierarchy connecting the MCIA complex to mitochondrial membrane.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "GO3", "GO7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Some general reasoning can eliminate C (spindle is a microtubule structure, incompatible with a multi-pass membrane protein) and A (host cell mitochondrion is a GO term reserved for pathogen-host symbiosis contexts, not applicable to a Drosophila protein in its own cell). The absence of a cleavable signal peptide at the N-terminus weakly argues against secretory-pathway compartments like the trans-Golgi network. However, the sequence lacks a canonical N-terminal mitochondrial targeting sequence (positively charged amphipathic helix), and the multi-pass TM topology alone does not distinguish mitochondrial membrane from Golgi membrane. The definitive identification of this protein as TMEM126B / a component of the MCIA complex (mitochondrial complex I intermediate assembly complex) requires protein-specific knowledge not derivable from the bare sequence.",
    "missing_item_specific_fact": "The identity of this 223-aa protein as Drosophila TMEM126B, a known subunit of the mitochondrial complex I intermediate assembly (MCIA) complex localized to the inner mitochondrial membrane. Without this identification, the multi-pass membrane topology and lack of obvious targeting signals do not conclusively distinguish mitochondrial membrane (D) from trans-Golgi network membrane (B).",
    "reason": "While general reasoning can eliminate spindle (C) and host cell mitochondrion (A) through GO ontology logic and basic biology, the critical D-vs-B distinction for a short multi-pass membrane protein without a canonical mitochondrial presequence or ER signal peptide depends on recognizing the protein's specific identity and its role in complex I assembly. The UniProt 'mitochondrion membrane' annotation itself is ISS (inferred from similarity to human Q8IUX1), underscoring that this localization is not trivially predictable from the Drosophila sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Option A ('host cell mitochondrion', GO:0033650) is technically a mitochondrion term and a model unfamiliar with the GO term's pathogen-specific context might select it over D. However, the GO definition explicitly restricts it to symbiotic/host contexts, making D the correct and more specific answer. Option B (trans-Golgi network membrane) is the most challenging distractor because the sequence provides no definitive targeting signal to exclude it without protein identity knowledge."
  },
  "important_caveats": [
    "The direct 'mitochondrion membrane' annotation (C5/H3) carries evidence code ECO:0000250 (similarity to human Q8IUX1), not direct experimental evidence for this Drosophila protein. The IDA experimental evidence (C6, C8) supports 'mitochondrion' and 'MCIA complex' but the membrane specificity comes through the ontology hierarchy (MCIA is part_of inner mitochondrial membrane is_a mitochondrial membrane).",
    "The UniProt entry was first public on 2025-02-05; the historical snapshot (entry v168, Jan 2026) already contains the mitochondrial membrane annotation, so the key was available at the time of benchmark construction.",
    "The sequence-match is confirmed (SHA256 match across current and historical records), so the annotation applies to the exact 223-aa sequence provided.",
    "The absence of a canonical N-terminal mitochondrial targeting presequence in the sequence is notable; TMEM126B is a multi-pass membrane protein whose mitochondrial targeting mechanism differs from the classic N-terminal presequence pathway."
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

**Accession:** `Q9VLM7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 168. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:25.958156+00:00.  

```json
"Q9VLM7"
```

Source SHA-256: `1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:25.958156+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IUX1","source":"UniProtKB"}],"id":"SL-0171","value":"Mitochondrion membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)  
**Locator:** `/uniProtKBCrossReferences/32`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:25.958156+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"34386730","source":"PubMed"}],"id":"GO:0160295","properties":[{"key":"GoTerm","value":"C:mitochondrial complex I intermediate assembly complex"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)  
**Locator:** `/uniProtKBCrossReferences/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:25.958156+00:00.  

```json
{"database":"GO","id":"GO:0031966","properties":[{"key":"GoTerm","value":"C:mitochondrial membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)  
**Locator:** `/uniProtKBCrossReferences/34`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:25.958156+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"34386730","source":"PubMed"}],"id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VLM7.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:25.958156+00:00.  

```json
{"citation":{"authors":["Murari A.","Rhooms S.K.","Garcia C.","Liu T.","Li H.","Mishra B.","Deshong C.","Owusu-Ansah E."],"citationCrossReferences":[{"database":"PubMed","id":"34386730"},{"database":"DOI","id":"10.1016/j.isci.2021.102869"}],"citationType":"journal article","firstPage":"102869","id":"34386730","journal":"IScience","lastPage":"102869","publicationDate":"2021","title":"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in mitochondrial complex I biogenesis.","volume":"24"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","INTERACTION WITH COMPLEX 1"]}
```

Source SHA-256: `1bcd7111d7277e25bf4c25f893d24cbc495d89cdc4770cf6a66f205e3d829c07`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 168 / 1.  
**Retrieved:** 2026-11-02T04:33:30.846128+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion membrane
CC       {ECO:0000250|UniProtKB:Q8IUX1}; Multi-pass membrane protein
CC       {ECO:0000255}.
```

Source SHA-256: `aa6b59d19cc42e8140fd34df1a8b1e15291088b9b8268a8d83178bcf68a1764a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168)  
**Locator:** `lines 125-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 168 / 1.  
**Retrieved:** 2026-11-02T04:33:30.846128+00:00.  

```text
DR   GO; GO:0031966; C:mitochondrial membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `aa6b59d19cc42e8140fd34df1a8b1e15291088b9b8268a8d83178bcf68a1764a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VLM7?format=txt&versions=168)  
**Locator:** `lines 126-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 168 / 1.  
**Retrieved:** 2026-11-02T04:33:30.846128+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IDA:FlyBase.
```

Source SHA-256: `aa6b59d19cc42e8140fd34df1a8b1e15291088b9b8268a8d83178bcf68a1764a`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 181484-181492`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031966
name: mitochondrial membrane
namespace: cellular_component
def: "Either of the lipid bilayers that surround the mitochondrion and form the mitochondrial envelope." [GOC:mah, NIF_Subcellular:sao1045389829]
xref: NIF_Subcellular:sao1045389829
is_a: GO:0031090 ! organelle membrane
relationship: part_of GO:0005740 ! mitochondrial envelope

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 451477-451485`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0160295
name: mitochondrial complex I intermediate assembly complex
namespace: cellular_component
def: "A protein complex involved in mitochondrial respiratory chain complex I (MCI) assembly. The mitochondrial complex I intermediate assembly (MCIA) complex is an inner mitochondrial membrane complex required for the aggregation, arrangement and bonding together of the subunits of the ND2-module of MCI. In humans, the MCIA complex is formed from NDUFAF1, ACAD9, ECSIT, TMEM126B, TMEM186 and COA1." [PMID:32320651]
synonym: "MCIA complex" EXACT []
synonym: "mitochondrial CI assembly complex" EXACT []
is_a: GO:0098800 ! inner mitochondrial membrane protein complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
