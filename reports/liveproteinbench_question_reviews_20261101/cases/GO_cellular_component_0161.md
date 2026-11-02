# GO_cellular_component_0161

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — mitochondrion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLKFLSTKCKQFNSLNHIIKHKIYFPSKSNKSYFSSSVKDVEKKNKEPIIQLTNDAINKMKEINLKYKNSKALKVCVEAGGCSGFQYSFSLIDKNKIKDKEQIVYDKDCIVVIDKQVIDILKNSKIHYINNLISKKFTIENIQNISSKCSCGNSFDIDFV

[Multiple Choices]
A. checkpoint clamp complex
B. Dbf4-dependent protein kinase complex
C. plasma membrane
D. mitochondrion
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

> The exact sequence matches the annotated Plasmodium falciparum IscA1 protein. Its mitochondrial location is recorded with experimental evidence (ECO:0000269), supporting choice D.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus is Lys-rich and lacks acidic residues across its first several dozen residues, a pattern compatible with a mitochondrial targeting presequence. The sequence also lacks an obvious long hydrophobic transmembrane segment, making plasma membrane less plausible; the specific nuclear DNA-replication complexes are not suggested by an evident sequence feature.


**Missing item-specific fact**

> The protein-specific experimental localization is not supplied; the sequence pattern supports a prediction but does not establish mitochondrial localization.


**Reason**

> The sequence offers a meaningful, though not definitive, targeting-signal-based distinction in favor of mitochondrion over the listed alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative listed option has comparable sequence-based support for this protein's primary compartment.


### Important caveats

- The mitochondrial assignment is supported by a sequence-matched database annotation with experimental evidence, but the underlying experiment was not independently reviewed here.
- A plausible mitochondrial presequence is predictive evidence, not proof of localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus is Lys-rich and lacks acidic residues across its first several dozen residues, a pattern compatible with a mitochondrial targeting presequence. The sequence also lacks an obvious long hydrophobic transmembrane segment, making plasma membrane less plausible; the specific nuclear DNA-replication complexes are not suggested by an evident sequence feature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The protein-specific experimental localization is not supplied; the sequence pattern supports a prediction but does not establish mitochondrial localization.",
    "reason": "The sequence offers a meaningful, though not definitive, targeting-signal-based distinction in favor of mitochondrion over the listed alternatives."
  },
  "case_id": "GO_cellular_component_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Plasmodium falciparum IscA1 protein. Its mitochondrial location is recorded with experimental evidence (ECO:0000269), supporting choice D."
  },
  "important_caveats": [
    "The mitochondrial assignment is supported by a sequence-matched database annotation with experimental evidence, but the underlying experiment was not independently reviewed here.",
    "A plausible mitochondrial presequence is predictive evidence, not proof of localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative listed option has comparable sequence-based support for this protein's primary compartment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Plasmodium falciparum IscA1 protein. Its mitochondrial location is recorded with experimental evidence (ECO:0000269), supporting choice D.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus is Lys-rich and lacks acidic residues across its first several dozen residues, a pattern compatible with a mitochondrial targeting presequence. The sequence also lacks an obvious long hydrophobic transmembrane segment, making plasma membrane less plausible; the specific nuclear DNA-replication complexes are not suggested by an evident sequence feature.",
    "missing_item_specific_fact": "The protein-specific experimental localization is not supplied; the sequence pattern supports a prediction but does not establish mitochondrial localization.",
    "reason": "The sequence offers a meaningful, though not definitive, targeting-signal-based distinction in favor of mitochondrion over the listed alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative listed option has comparable sequence-based support for this protein's primary compartment."
  },
  "important_caveats": [
    "The mitochondrial assignment is supported by a sequence-matched database annotation with experimental evidence, but the underlying experiment was not independently reviewed here.",
    "A plausible mitochondrial presequence is predictive evidence, not proof of localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt O96161 (PfIscA1, Iron-sulfur assembly protein IscA1 from Plasmodium falciparum 3D7, 160 aa, SHA256 confirmed). UniProt subcellular location is 'Mitochondrion' with experimental evidence code ECO:0000269 from PubMed:34032321 (Sadik et al. 2021, Mol. Microbiol. 116:606-623, titled '&#91;Fe-S&#93; biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion'). GO:0005739 (mitochondrion) is annotated via ISS:GeneDB, and GO:0120510 (mitochondrial &#91;4Fe-4S&#93; assembly complex) via IEA. The expected answer D is directly supported by experimental subcellular localization data.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 160-aa protein contains multiple cysteine residues (CKQ, KVC, CSF, DCIV, KCSCG) suggestive of iron-sulfur cluster coordination. The eukaryotic ISC (iron-sulfur cluster) assembly machinery is canonically mitochondrial. The sequence lacks long hydrophobic transmembrane segments (ruling out plasma membrane, option C), lacks kinase catalytic motifs (ruling out Dbf4-dependent kinase complex, option B), and lacks DNA-binding or PCNA-like clamp structural features (ruling out checkpoint clamp complex, option A). The small size and cysteine content are consistent with an ISC scaffold/assembly protein, whose compartment is the mitochondrion.


**Missing item-specific fact**

> Precise recognition of this sequence as PfIscA1 and confirmation that Plasmodium's ISC machinery is specifically mitochondrial (rather than cytoplasmic as in some prokaryotes or mitosomes as in some anaerobic eukaryotes) adds specificity beyond general reasoning, but the general principle that eukaryotic ISC proteins are mitochondrial is well-established textbook knowledge.


**Reason**

> A knowledgeable model can eliminate options A, B, and C by noting the absence of kinase domains, DNA-binding motifs, and transmembrane helices, and can positively support D by recognizing cysteine-rich small proteins as Fe-S cluster assembly factors whose eukaryotic compartment is the mitochondrion. The reasoning path is concrete and does not require memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (nuclear DNA-damage clamp) and B (nuclear replication kinase) are excluded by the absence of DNA-binding or kinase structural features. Option C (plasma membrane) is excluded by the absence of transmembrane segments. Only D (mitochondrion) is consistent with the cysteine-rich, small, soluble protein profile characteristic of ISC machinery.


### Important caveats

- The subcellular localization evidence (ECO:0000269) is experimental (PubMed:34032321), not merely computational transfer.
- The GO:0005739 annotation carries ISS:GeneDB (inferred by sequence similarity), while the primary experimental evidence is from the 2021 Sadik et al. paper.
- Plasmodium falciparum mitochondrial targeting signals are atypical; the N-terminal region here does not show a canonical cleavable presequence, which could make mitochondrial targeting less obvious to a purely sequence-based heuristic model.
- The identity of the protein (IscA1) was inferred by the reviewer from dataset metadata absent from the model input; the model must rely on sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 160-aa protein contains multiple cysteine residues (CKQ, KVC, CSF, DCIV, KCSCG) suggestive of iron-sulfur cluster coordination. The eukaryotic ISC (iron-sulfur cluster) assembly machinery is canonically mitochondrial. The sequence lacks long hydrophobic transmembrane segments (ruling out plasma membrane, option C), lacks kinase catalytic motifs (ruling out Dbf4-dependent kinase complex, option B), and lacks DNA-binding or PCNA-like clamp structural features (ruling out checkpoint clamp complex, option A). The small size and cysteine content are consistent with an ISC scaffold/assembly protein, whose compartment is the mitochondrion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of this sequence as PfIscA1 and confirmation that Plasmodium's ISC machinery is specifically mitochondrial (rather than cytoplasmic as in some prokaryotes or mitosomes as in some anaerobic eukaryotes) adds specificity beyond general reasoning, but the general principle that eukaryotic ISC proteins are mitochondrial is well-established textbook knowledge.",
    "reason": "A knowledgeable model can eliminate options A, B, and C by noting the absence of kinase domains, DNA-binding motifs, and transmembrane helices, and can positively support D by recognizing cysteine-rich small proteins as Fe-S cluster assembly factors whose eukaryotic compartment is the mitochondrion. The reasoning path is concrete and does not require memorizing this specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "C8",
      "H3",
      "H5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt O96161 (PfIscA1, Iron-sulfur assembly protein IscA1 from Plasmodium falciparum 3D7, 160 aa, SHA256 confirmed). UniProt subcellular location is 'Mitochondrion' with experimental evidence code ECO:0000269 from PubMed:34032321 (Sadik et al. 2021, Mol. Microbiol. 116:606-623, titled '[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion'). GO:0005739 (mitochondrion) is annotated via ISS:GeneDB, and GO:0120510 (mitochondrial [4Fe-4S] assembly complex) via IEA. The expected answer D is directly supported by experimental subcellular localization data."
  },
  "important_caveats": [
    "The subcellular localization evidence (ECO:0000269) is experimental (PubMed:34032321), not merely computational transfer.",
    "The GO:0005739 annotation carries ISS:GeneDB (inferred by sequence similarity), while the primary experimental evidence is from the 2021 Sadik et al. paper.",
    "Plasmodium falciparum mitochondrial targeting signals are atypical; the N-terminal region here does not show a canonical cleavable presequence, which could make mitochondrial targeting less obvious to a purely sequence-based heuristic model.",
    "The identity of the protein (IscA1) was inferred by the reviewer from dataset metadata absent from the model input; the model must rely on sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (nuclear DNA-damage clamp) and B (nuclear replication kinase) are excluded by the absence of DNA-binding or kinase structural features. Option C (plasma membrane) is excluded by the absence of transmembrane segments. Only D (mitochondrion) is consistent with the cysteine-rich, small, soluble protein profile characteristic of ISC machinery."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt O96161 (PfIscA1, Iron-sulfur assembly protein IscA1 from Plasmodium falciparum 3D7, 160 aa, SHA256 confirmed). UniProt subcellular location is 'Mitochondrion' with experimental evidence code ECO:0000269 from PubMed:34032321 (Sadik et al. 2021, Mol. Microbiol. 116:606-623, titled '[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion'). GO:0005739 (mitochondrion) is annotated via ISS:GeneDB, and GO:0120510 (mitochondrial [4Fe-4S] assembly complex) via IEA. The expected answer D is directly supported by experimental subcellular localization data.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "C8", "H3", "H5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 160-aa protein contains multiple cysteine residues (CKQ, KVC, CSF, DCIV, KCSCG) suggestive of iron-sulfur cluster coordination. The eukaryotic ISC (iron-sulfur cluster) assembly machinery is canonically mitochondrial. The sequence lacks long hydrophobic transmembrane segments (ruling out plasma membrane, option C), lacks kinase catalytic motifs (ruling out Dbf4-dependent kinase complex, option B), and lacks DNA-binding or PCNA-like clamp structural features (ruling out checkpoint clamp complex, option A). The small size and cysteine content are consistent with an ISC scaffold/assembly protein, whose compartment is the mitochondrion.",
    "missing_item_specific_fact": "Precise recognition of this sequence as PfIscA1 and confirmation that Plasmodium's ISC machinery is specifically mitochondrial (rather than cytoplasmic as in some prokaryotes or mitosomes as in some anaerobic eukaryotes) adds specificity beyond general reasoning, but the general principle that eukaryotic ISC proteins are mitochondrial is well-established textbook knowledge.",
    "reason": "A knowledgeable model can eliminate options A, B, and C by noting the absence of kinase domains, DNA-binding motifs, and transmembrane helices, and can positively support D by recognizing cysteine-rich small proteins as Fe-S cluster assembly factors whose eukaryotic compartment is the mitochondrion. The reasoning path is concrete and does not require memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (nuclear DNA-damage clamp) and B (nuclear replication kinase) are excluded by the absence of DNA-binding or kinase structural features. Option C (plasma membrane) is excluded by the absence of transmembrane segments. Only D (mitochondrion) is consistent with the cysteine-rich, small, soluble protein profile characteristic of ISC machinery."
  },
  "important_caveats": [
    "The subcellular localization evidence (ECO:0000269) is experimental (PubMed:34032321), not merely computational transfer.",
    "The GO:0005739 annotation carries ISS:GeneDB (inferred by sequence similarity), while the primary experimental evidence is from the 2021 Sadik et al. paper.",
    "Plasmodium falciparum mitochondrial targeting signals are atypical; the N-terminal region here does not show a canonical cleavable presequence, which could make mitochondrial targeting less obvious to a purely sequence-based heuristic model.",
    "The identity of the protein (IscA1) was inferred by the reviewer from dataset metadata absent from the model input; the model must rely on sequence features alone."
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

**Accession:** `O96161` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 132. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96161.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:18.609210+00:00.  

```json
"O96161"
```

Source SHA-256: `2347597d553a6fb134b39a6fcbd1feba2232026810eb8b53e71970d3380e7753`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96161.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:18.609210+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Iron-sulfur assembly protein IscA1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34032321","source":"PubMed"}],"value":"PfIscA1"}]}}
```

Source SHA-256: `2347597d553a6fb134b39a6fcbd1feba2232026810eb8b53e71970d3380e7753`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96161.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:18.609210+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"id":"SL-0173","value":"Mitochondrion"}}]}
```

Source SHA-256: `2347597d553a6fb134b39a6fcbd1feba2232026810eb8b53e71970d3380e7753`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96161.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:18.609210+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000250","id":"12368867","source":"PubMed"}],"id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"ISS:GeneDB"}]}
```

Source SHA-256: `2347597d553a6fb134b39a6fcbd1feba2232026810eb8b53e71970d3380e7753`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96161.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:18.609210+00:00.  

```json
{"citation":{"authors":["Sadik M.","Afsar M.","Ramachandran R.","Habib S."],"citationCrossReferences":[{"database":"PubMed","id":"34032321"},{"database":"DOI","id":"10.1111/mmi.14735"}],"citationType":"journal article","firstPage":"606","id":"34032321","journal":"Mol. Microbiol.","lastPage":"623","publicationDate":"2021","title":"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.","volume":"116"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","SUBUNIT","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `2347597d553a6fb134b39a6fcbd1feba2232026810eb8b53e71970d3380e7753`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96161?format=txt&versions=132)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-02T04:29:25.824429+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, SUBUNIT, AND SUBCELLULAR LOCATION.
RX   PubMed=34032321; DOI=10.1111/mmi.14735;
RA   Sadik M., Afsar M., Ramachandran R., Habib S.;
RT   "[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the
RT   Plasmodium falciparum mitochondrion.";
RL   Mol. Microbiol. 116:606-623(2021).
```

Source SHA-256: `a3906d1a18bf93241fbf44e7d3ffad8e37e539926c16e0a7d9f01db318dbf10e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96161?format=txt&versions=132)  
**Locator:** `lines 55-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-02T04:29:25.824429+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:34032321}.
```

Source SHA-256: `a3906d1a18bf93241fbf44e7d3ffad8e37e539926c16e0a7d9f01db318dbf10e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96161?format=txt&versions=132)  
**Locator:** `lines 80-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-02T04:29:25.824429+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; ISS:GeneDB.
```

Source SHA-256: `a3906d1a18bf93241fbf44e7d3ffad8e37e539926c16e0a7d9f01db318dbf10e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 161. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
