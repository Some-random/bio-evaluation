# GO_cellular_component_0112

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — kinetoplast

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTFNGRFRATLRGINIRNASMTSLSLTGSHAQKQTVLGSTPGALGTIPTVALNGVNPLPRYRHNLLFGTLSFGDRWDRIQRRLAVLGRASTGNVVVPFSDSADAFRRMWESVDSASDSVLWQTYICKDDFVGQKTVKKLEEAHRRGCKTELLYDCGGNITGRRRLVGDLKKSGANVIEHRPMWEHFFPYFLRGMKWELSPGIRNHRKILIVDNKLGFCGGLNIGDEYCGTSEGGNGRFRDTHCVVMGPAVMHMREVYEDTKAPKPWKWSLARWRQIASATMNLRYLEGMNVKHDYLEPTTTFVRQGGGVYLRRQMERAERSTVRMMERMRWKRQRERLNRCLLTLAKNLREGQGLVFKAATGKGDDVATTDAGSKRNNEVSHGQWKLMKRRIDEYRQRAIKNAEESFFRRLRVVNPSMRLLEDTSPVAEAEAYGQAHAAVTQVLSCNPHSRDWSIPYAFWQVSKFVHQRLWVTTPYYMPHRKLMRALQLAARRGVDVRILAGSNRTTDPWFMWYASNYITGMLMASGVRVYEYKGGQVMHAKTVVADSIWTSIGSYNWDMMSNKNMEICVCHLDHNLALTMEKQFLDDMNVSEEVNYEEYQRRSLWLRFSSWFFYTALRIAEKFTFRTFWDPDLSSEID

[Multiple Choices]
A. plasma membrane
B. viral nucleocapsid
C. striated muscle dense body
D. kinetoplast
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

> The exact sequence matches a historical UniProt record annotated with GO:0020023 (kinetoplast), with evidence code IDA:GeneDB. The same record reports experimental localization to the mitochondrial inner membrane, consistent with a kinetoplast-associated mitochondrial protein.

Citations as saved: [H4](#evidence-h4), [H3](#evidence-h3), [C1](#evidence-c1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a membrane-associated protein, but it does not provide a reliable basis for distinguishing a kinetoplast from other cellular membranes or compartments.


**Missing item-specific fact**

> The protein-specific kinetoplast localization annotation or equivalent experimental localization evidence is absent from the prompt.


**Reason**

> Selecting D depends on an item-specific localization fact. A general sequence heuristic or recognition of a membrane-associated protein does not establish localization to this particular mitochondrial substructure.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence specifically supports the kinetoplast annotation; the other options are not comparably supported.


### Important caveats

- The supporting UniProt record matches the sequence, but the author's exact source snapshot is unknown.
- The archived GO annotation is IDA:GeneDB; the separate mitochondrial inner-membrane localization is attributed to experimental evidence. These annotations support the key but are not independent validation here of the primary paper.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a membrane-associated protein, but it does not provide a reliable basis for distinguishing a kinetoplast from other cellular membranes or compartments.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific kinetoplast localization annotation or equivalent experimental localization evidence is absent from the prompt.",
    "reason": "Selecting D depends on an item-specific localization fact. A general sequence heuristic or recognition of a membrane-associated protein does not establish localization to this particular mitochondrial substructure."
  },
  "case_id": "GO_cellular_component_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H3",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a historical UniProt record annotated with GO:0020023 (kinetoplast), with evidence code IDA:GeneDB. The same record reports experimental localization to the mitochondrial inner membrane, consistent with a kinetoplast-associated mitochondrial protein."
  },
  "important_caveats": [
    "The supporting UniProt record matches the sequence, but the author's exact source snapshot is unknown.",
    "The archived GO annotation is IDA:GeneDB; the separate mitochondrial inner-membrane localization is attributed to experimental evidence. These annotations support the key but are not independent validation here of the primary paper."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence specifically supports the kinetoplast annotation; the other options are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a historical UniProt record annotated with GO:0020023 (kinetoplast), with evidence code IDA:GeneDB. The same record reports experimental localization to the mitochondrial inner membrane, consistent with a kinetoplast-associated mitochondrial protein.",
    "evidence_ids": ["H4", "H3", "C1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a membrane-associated protein, but it does not provide a reliable basis for distinguishing a kinetoplast from other cellular membranes or compartments.",
    "missing_item_specific_fact": "The protein-specific kinetoplast localization annotation or equivalent experimental localization evidence is absent from the prompt.",
    "reason": "Selecting D depends on an item-specific localization fact. A general sequence heuristic or recognition of a membrane-associated protein does not establish localization to this particular mitochondrial substructure."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence specifically supports the kinetoplast annotation; the other options are not comparably supported."
  },
  "important_caveats": [
    "The supporting UniProt record matches the sequence, but the author's exact source snapshot is unknown.",
    "The archived GO annotation is IDA:GeneDB; the separate mitochondrial inner-membrane localization is attributed to experimental evidence. These annotations support the key but are not independent validation here of the primary paper."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q584D1 (Cardiolipin synthetase, Trypanosoma brucei). The UniProt entry carries GO:0020023 (kinetoplast) with IDA:GeneDB evidence (C6/H4). The primary experimental evidence (PubMed:22451910) places the protein at the 'Mitochondrion inner membrane' (C5/H3), and the kinetoplast is defined as a sub-structure within the mitochondrion of kinetoplastid parasites (GO3). Among the four choices, kinetoplast is the only mitochondrion-related option, and the GO annotation explicitly assigns this term. The answer is supported by database annotation, though the more precise experimental localization is 'mitochondrial inner membrane' rather than specifically the kinetoplast sub-region.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If one could identify the organism as a kinetoplastid (e.g., Trypanosoma), then knowing that (i) cardiolipin synthetase is a mitochondrial inner-membrane enzyme and (ii) the kinetoplast is a mitochondrial sub-structure unique to kinetoplastids, one could reason to D over A. The distractors B (viral nucleocapsid) and C (striated muscle dense body) are trivially eliminable for any eukaryotic enzyme.


**Missing item-specific fact**

> Identifying the sequence as originating from a kinetoplastid organism (Trypanosoma brucei) from the amino-acid sequence alone requires either memorization of kinetoplastid sequence signatures or a database lookup. Without this organism identification, the presence of 'kinetoplast' as an option is unmotivated, and the protein could be a generic mitochondrial membrane protein of any eukaryote.


**Reason**

> The biological reasoning chain (mitochondrial enzyme → kinetoplast sub-compartment) is valid but is gated on first recognizing the organism as a kinetoplastid. Sequence composition alone (e.g., unusual residue frequencies in Trypanosoma) is not a reliable, general-knowledge signal for most solvers. The decisive step—linking this particular sequence to a kinetoplastid organism and hence to the kinetoplast compartment—depends on item-specific identification rather than generalizable biological inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (viral nucleocapsid) and C (striated muscle dense body) are clearly irrelevant for a eukaryotic mitochondrial enzyme. Option A (plasma membrane) is eliminable once the protein is recognized as mitochondrial. Among the given choices, D is the only defensible answer, though 'mitochondrial inner membrane' (the primary experimental annotation) would have been more precise and is not offered.


### Important caveats

- The primary experimental evidence (PubMed:22451910, ECO:0000269) specifies 'Mitochondrion inner membrane,' not specifically the kinetoplast sub-region. The kinetoplast GO annotation (GO:0020023) carries IDA:GeneDB evidence, which is experimental but from a different source.
- The kinetoplast is a sub-compartment of the mitochondrion in kinetoplastids; not every mitochondrial inner-membrane protein in Trypanosoma is necessarily at the kinetoplast. The GeneDB annotation assigns this protein there, but the primary paper's localization statement is broader.
- The organism identification (Trypanosoma brucei, kinetoplastid) is not stated in the model input and must be inferred from the sequence or retrieved from a database.
- The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot is unknown but the sequence has been stable since 2005-05-10.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If one could identify the organism as a kinetoplastid (e.g., Trypanosoma), then knowing that (i) cardiolipin synthetase is a mitochondrial inner-membrane enzyme and (ii) the kinetoplast is a mitochondrial sub-structure unique to kinetoplastids, one could reason to D over A. The distractors B (viral nucleocapsid) and C (striated muscle dense body) are trivially eliminable for any eukaryotic enzyme.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying the sequence as originating from a kinetoplastid organism (Trypanosoma brucei) from the amino-acid sequence alone requires either memorization of kinetoplastid sequence signatures or a database lookup. Without this organism identification, the presence of 'kinetoplast' as an option is unmotivated, and the protein could be a generic mitochondrial membrane protein of any eukaryote.",
    "reason": "The biological reasoning chain (mitochondrial enzyme → kinetoplast sub-compartment) is valid but is gated on first recognizing the organism as a kinetoplastid. Sequence composition alone (e.g., unusual residue frequencies in Trypanosoma) is not a reliable, general-knowledge signal for most solvers. The decisive step—linking this particular sequence to a kinetoplastid organism and hence to the kinetoplast compartment—depends on item-specific identification rather than generalizable biological inference."
  },
  "case_id": "GO_cellular_component_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q584D1 (Cardiolipin synthetase, Trypanosoma brucei). The UniProt entry carries GO:0020023 (kinetoplast) with IDA:GeneDB evidence (C6/H4). The primary experimental evidence (PubMed:22451910) places the protein at the 'Mitochondrion inner membrane' (C5/H3), and the kinetoplast is defined as a sub-structure within the mitochondrion of kinetoplastid parasites (GO3). Among the four choices, kinetoplast is the only mitochondrion-related option, and the GO annotation explicitly assigns this term. The answer is supported by database annotation, though the more precise experimental localization is 'mitochondrial inner membrane' rather than specifically the kinetoplast sub-region."
  },
  "important_caveats": [
    "The primary experimental evidence (PubMed:22451910, ECO:0000269) specifies 'Mitochondrion inner membrane,' not specifically the kinetoplast sub-region. The kinetoplast GO annotation (GO:0020023) carries IDA:GeneDB evidence, which is experimental but from a different source.",
    "The kinetoplast is a sub-compartment of the mitochondrion in kinetoplastids; not every mitochondrial inner-membrane protein in Trypanosoma is necessarily at the kinetoplast. The GeneDB annotation assigns this protein there, but the primary paper's localization statement is broader.",
    "The organism identification (Trypanosoma brucei, kinetoplastid) is not stated in the model input and must be inferred from the sequence or retrieved from a database.",
    "The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot is unknown but the sequence has been stable since 2005-05-10."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (viral nucleocapsid) and C (striated muscle dense body) are clearly irrelevant for a eukaryotic mitochondrial enzyme. Option A (plasma membrane) is eliminable once the protein is recognized as mitochondrial. Among the given choices, D is the only defensible answer, though 'mitochondrial inner membrane' (the primary experimental annotation) would have been more precise and is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q584D1 (Cardiolipin synthetase, Trypanosoma brucei). The UniProt entry carries GO:0020023 (kinetoplast) with IDA:GeneDB evidence (C6/H4). The primary experimental evidence (PubMed:22451910) places the protein at the 'Mitochondrion inner membrane' (C5/H3), and the kinetoplast is defined as a sub-structure within the mitochondrion of kinetoplastid parasites (GO3). Among the four choices, kinetoplast is the only mitochondrion-related option, and the GO annotation explicitly assigns this term. The answer is supported by database annotation, though the more precise experimental localization is 'mitochondrial inner membrane' rather than specifically the kinetoplast sub-region.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H3", "H4", "H5", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If one could identify the organism as a kinetoplastid (e.g., Trypanosoma), then knowing that (i) cardiolipin synthetase is a mitochondrial inner-membrane enzyme and (ii) the kinetoplast is a mitochondrial sub-structure unique to kinetoplastids, one could reason to D over A. The distractors B (viral nucleocapsid) and C (striated muscle dense body) are trivially eliminable for any eukaryotic enzyme.",
    "missing_item_specific_fact": "Identifying the sequence as originating from a kinetoplastid organism (Trypanosoma brucei) from the amino-acid sequence alone requires either memorization of kinetoplastid sequence signatures or a database lookup. Without this organism identification, the presence of 'kinetoplast' as an option is unmotivated, and the protein could be a generic mitochondrial membrane protein of any eukaryote.",
    "reason": "The biological reasoning chain (mitochondrial enzyme → kinetoplast sub-compartment) is valid but is gated on first recognizing the organism as a kinetoplastid. Sequence composition alone (e.g., unusual residue frequencies in Trypanosoma) is not a reliable, general-knowledge signal for most solvers. The decisive step—linking this particular sequence to a kinetoplastid organism and hence to the kinetoplast compartment—depends on item-specific identification rather than generalizable biological inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (viral nucleocapsid) and C (striated muscle dense body) are clearly irrelevant for a eukaryotic mitochondrial enzyme. Option A (plasma membrane) is eliminable once the protein is recognized as mitochondrial. Among the given choices, D is the only defensible answer, though 'mitochondrial inner membrane' (the primary experimental annotation) would have been more precise and is not offered."
  },
  "important_caveats": [
    "The primary experimental evidence (PubMed:22451910, ECO:0000269) specifies 'Mitochondrion inner membrane,' not specifically the kinetoplast sub-region. The kinetoplast GO annotation (GO:0020023) carries IDA:GeneDB evidence, which is experimental but from a different source.",
    "The kinetoplast is a sub-compartment of the mitochondrion in kinetoplastids; not every mitochondrial inner-membrane protein in Trypanosoma is necessarily at the kinetoplast. The GeneDB annotation assigns this protein there, but the primary paper's localization statement is broader.",
    "The organism identification (Trypanosoma brucei, kinetoplastid) is not stated in the model input and must be inferred from the sequence or retrieved from a database.",
    "The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot is unknown but the sequence has been stable since 2005-05-10."
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

**Accession:** `Q584D1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 102. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
"Q584D1"
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"22451910","source":"PubMed"}],"id":"SL-0168","value":"Mitochondrion inner membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9904","value":"Single-pass membrane protein"}}]}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"database":"GO","id":"GO:0020023","properties":[{"key":"GoTerm","value":"C:kinetoplast"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"22451910","source":"PubMed"}],"id":"GO:0005743","properties":[{"key":"GoTerm","value":"C:mitochondrial inner membrane"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"22451910","source":"PubMed"}],"id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 95-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion inner membrane
CC       {ECO:0000269|PubMed:22451910}; Single-pass membrane protein
CC       {ECO:0000255}.
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 126-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
DR   GO; GO:0020023; C:kinetoplast; IDA:GeneDB.
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 127-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
DR   GO; GO:0005743; C:mitochondrial inner membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 128-128`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IDA:GeneDB.
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 155291-155299`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0020023
name: kinetoplast
namespace: cellular_component
def: "A sub-structure within the large single mitochondrion of kinetoplastid parasites and which is closely associated with the flagellar pocket and basal body of the flagellum." [GOC:mb]
xref: Wikipedia:Kinetoplast
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0005739 ! mitochondrion

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
