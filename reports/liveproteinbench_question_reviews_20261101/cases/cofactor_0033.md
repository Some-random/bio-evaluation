# cofactor_0033

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSVSPQSTMARIPERRVRTLDFAQFRHGEPSGSRGFCRELVDCLSSVGFVKIRNHGISGQEIENVFVMSQLFFSLPQAAKGKAAHPPEANPHRGYSYVGQEKLSRVKDYEKGKREITDVYDIKHYPIDRDARQESYDQGAAVDNLYPNRWPDEQDIPGFRVLMETFYERCHEVHQDILRAIAIGFDLSPSFLTDLCCQNTSELRLNHYPSVHPSSLRKGAKRISEHTDFGTVTLLFQDSVGGLEIEDQNTPGTYFPVLSERKSDIIVNIGDCIQRWTNDKIHSTSHRVVLPEDTDALTKDRYSVAYFGKPSRSQLVGSLREFVKEGEKPKYNDISAWQYNQEKLVLTY

[Multiple Choices]
A. tungstopterin
B. pantetheine 4'-phosphate
C. FAD
D. Fe(2+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the annotated protein. Its UniProt record identifies it as a 2-oxoglutarate–Fe(II)-type oxidoreductase and annotates one Fe(2+) ion per subunit. The cofactor annotation is based on a PROSITE rule, so it is computational annotation rather than direct experimental evidence of metal binding.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include a metal ion and several chemically distinct cofactors, but the input supplies no protein function, organism, pathway, or clearly diagnostic cofactor-binding feature that meaningfully establishes which one this particular protein requires.


**Missing item-specific fact**

> The needed protein-specific fact is that this sequence is ppzD, a 2-oxoglutarate–Fe(II)-type oxidoreductase annotated as binding Fe(2+). That identity and annotation are absent from the question input.


**Reason**

> Selecting Fe(2+) depends on knowing the function or cofactor annotation of this particular protein; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports Fe(2+) as the annotated cofactor, and no other listed option is comparably supported.


### Important caveats

- The sequence match is exact, but the author’s source snapshot is unknown.
- The cofactor statement is attributed to a PROSITE rule; the cited functional literature does not, in the excerpts provided, independently establish direct experimental measurement of iron binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include a metal ion and several chemically distinct cofactors, but the input supplies no protein function, organism, pathway, or clearly diagnostic cofactor-binding feature that meaningfully establishes which one this particular protein requires.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The needed protein-specific fact is that this sequence is ppzD, a 2-oxoglutarate–Fe(II)-type oxidoreductase annotated as binding Fe(2+). That identity and annotation are absent from the question input.",
    "reason": "Selecting Fe(2+) depends on knowing the function or cofactor annotation of this particular protein; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "case_id": "cofactor_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. Its UniProt record identifies it as a 2-oxoglutarate–Fe(II)-type oxidoreductase and annotates one Fe(2+) ion per subunit. The cofactor annotation is based on a PROSITE rule, so it is computational annotation rather than direct experimental evidence of metal binding."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s source snapshot is unknown.",
    "The cofactor statement is attributed to a PROSITE rule; the cited functional literature does not, in the excerpts provided, independently establish direct experimental measurement of iron binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports Fe(2+) as the annotated cofactor, and no other listed option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. Its UniProt record identifies it as a 2-oxoglutarate–Fe(II)-type oxidoreductase and annotates one Fe(2+) ion per subunit. The cofactor annotation is based on a PROSITE rule, so it is computational annotation rather than direct experimental evidence of metal binding.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include a metal ion and several chemically distinct cofactors, but the input supplies no protein function, organism, pathway, or clearly diagnostic cofactor-binding feature that meaningfully establishes which one this particular protein requires.",
    "missing_item_specific_fact": "The needed protein-specific fact is that this sequence is ppzD, a 2-oxoglutarate–Fe(II)-type oxidoreductase annotated as binding Fe(2+). That identity and annotation are absent from the question input.",
    "reason": "Selecting Fe(2+) depends on knowing the function or cofactor annotation of this particular protein; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports Fe(2+) as the annotated cofactor, and no other listed option is comparably supported."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s source snapshot is unknown.",
    "The cofactor statement is attributed to a PROSITE rule; the cited functional literature does not, in the excerpts provided, independently establish direct experimental measurement of iron binding."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A455ZMR3 (sequence SHA256 matched exactly) annotates this protein as '2-oxoglutarate-Fe(II) type oxidoreductase ppzD' with EC 1.14.11.-/1.14.11.57 and explicitly lists Fe(2+) as the cofactor (1 Fe(2+) ion per subunit, ECO:0000255|PROSITE-ProRule:PRU00805). The 2024 JACS paper (PubMed 38578094) experimentally characterized this enzyme as an Iron(II), alpha-Ketoglutarate-Dependent enzyme, providing experimental confirmation beyond the computational annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2-oxoglutarate/Fe(II)-dependent dioxygenase superfamily is characterized by a well-known HxD/E...H...H facial triad motif that coordinates Fe(II) in a distorted octahedral geometry. In the supplied 349-aa sequence, a HxD/E motif is visible in the C-terminal region (e.g., 'CHEVHQD'), followed by additional conserved histidines (~100-150 residues downstream: 'RLNH', 'PSVH', 'RISEH'). This triad pattern is a generalizable family signature directly implying Fe(II) coordination. The distractors correspond to entirely different enzyme classes: tungstopterin (Mo/W aldehyde oxidoreductases with large multi-domain architectures), pantetheine 4'-phosphate (CoA-dependent acyltransferases), and FAD (flavoproteins with Rossmann-fold GxGxxG motifs). None of these alternative cofactor classes match the observed sequence architecture.


**Missing item-specific fact**

> None critical. Identification of the HxD/E...H...H triad is a generalizable motif-recognition task within the 2OG oxygenase superfamily, not an item-specific database lookup.


**Reason**

> A knowledgeable bioinformatician can identify the 2OG/Fe(II) oxygenase facial triad from the sequence pattern and infer Fe(2+) as the cofactor without needing to recognize this exact protein. The motif is a well-established, generalizable structural signature across thousands of family members.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four cofactor choices correspond to mutually exclusive enzyme classes with distinct structural signatures. The HxD/E...H...H pattern in the sequence uniquely points to 2OG/Fe(II) oxygenases and Fe(2+). No other option is defensible given the observed sequence features.


### Important caveats

- The primary cofactor annotation carries ECO:0000255 (computational, PROSITE-ProRule), but the 2024 JACS publication (PubMed 38578094) provides direct experimental evidence of Iron(II) dependence, strengthening the annotation.
- The HxD/E...H...H motif identification requires specialized knowledge of enzyme superfamily signatures; while generalizable, it is not trivially obvious to a general biology audience.
- Sequence identity is exact (SHA256 match confirmed between benchmark and UniProt source).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2-oxoglutarate/Fe(II)-dependent dioxygenase superfamily is characterized by a well-known HxD/E...H...H facial triad motif that coordinates Fe(II) in a distorted octahedral geometry. In the supplied 349-aa sequence, a HxD/E motif is visible in the C-terminal region (e.g., 'CHEVHQD'), followed by additional conserved histidines (~100-150 residues downstream: 'RLNH', 'PSVH', 'RISEH'). This triad pattern is a generalizable family signature directly implying Fe(II) coordination. The distractors correspond to entirely different enzyme classes: tungstopterin (Mo/W aldehyde oxidoreductases with large multi-domain architectures), pantetheine 4'-phosphate (CoA-dependent acyltransferases), and FAD (flavoproteins with Rossmann-fold GxGxxG motifs). None of these alternative cofactor classes match the observed sequence architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Identification of the HxD/E...H...H triad is a generalizable motif-recognition task within the 2OG oxygenase superfamily, not an item-specific database lookup.",
    "reason": "A knowledgeable bioinformatician can identify the 2OG/Fe(II) oxygenase facial triad from the sequence pattern and infer Fe(2+) as the cofactor without needing to recognize this exact protein. The motif is a well-established, generalizable structural signature across thousands of family members."
  },
  "case_id": "cofactor_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A455ZMR3 (sequence SHA256 matched exactly) annotates this protein as '2-oxoglutarate-Fe(II) type oxidoreductase ppzD' with EC 1.14.11.-/1.14.11.57 and explicitly lists Fe(2+) as the cofactor (1 Fe(2+) ion per subunit, ECO:0000255|PROSITE-ProRule:PRU00805). The 2024 JACS paper (PubMed 38578094) experimentally characterized this enzyme as an Iron(II), alpha-Ketoglutarate-Dependent enzyme, providing experimental confirmation beyond the computational annotation."
  },
  "important_caveats": [
    "The primary cofactor annotation carries ECO:0000255 (computational, PROSITE-ProRule), but the 2024 JACS publication (PubMed 38578094) provides direct experimental evidence of Iron(II) dependence, strengthening the annotation.",
    "The HxD/E...H...H motif identification requires specialized knowledge of enzyme superfamily signatures; while generalizable, it is not trivially obvious to a general biology audience.",
    "Sequence identity is exact (SHA256 match confirmed between benchmark and UniProt source)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor choices correspond to mutually exclusive enzyme classes with distinct structural signatures. The HxD/E...H...H pattern in the sequence uniquely points to 2OG/Fe(II) oxygenases and Fe(2+). No other option is defensible given the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A455ZMR3 (sequence SHA256 matched exactly) annotates this protein as '2-oxoglutarate-Fe(II) type oxidoreductase ppzD' with EC 1.14.11.-/1.14.11.57 and explicitly lists Fe(2+) as the cofactor (1 Fe(2+) ion per subunit, ECO:0000255|PROSITE-ProRule:PRU00805). The 2024 JACS paper (PubMed 38578094) experimentally characterized this enzyme as an Iron(II), alpha-Ketoglutarate-Dependent enzyme, providing experimental confirmation beyond the computational annotation.",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2-oxoglutarate/Fe(II)-dependent dioxygenase superfamily is characterized by a well-known HxD/E...H...H facial triad motif that coordinates Fe(II) in a distorted octahedral geometry. In the supplied 349-aa sequence, a HxD/E motif is visible in the C-terminal region (e.g., 'CHEVHQD'), followed by additional conserved histidines (~100-150 residues downstream: 'RLNH', 'PSVH', 'RISEH'). This triad pattern is a generalizable family signature directly implying Fe(II) coordination. The distractors correspond to entirely different enzyme classes: tungstopterin (Mo/W aldehyde oxidoreductases with large multi-domain architectures), pantetheine 4'-phosphate (CoA-dependent acyltransferases), and FAD (flavoproteins with Rossmann-fold GxGxxG motifs). None of these alternative cofactor classes match the observed sequence architecture.",
    "missing_item_specific_fact": "None critical. Identification of the HxD/E...H...H triad is a generalizable motif-recognition task within the 2OG oxygenase superfamily, not an item-specific database lookup.",
    "reason": "A knowledgeable bioinformatician can identify the 2OG/Fe(II) oxygenase facial triad from the sequence pattern and infer Fe(2+) as the cofactor without needing to recognize this exact protein. The motif is a well-established, generalizable structural signature across thousands of family members."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor choices correspond to mutually exclusive enzyme classes with distinct structural signatures. The HxD/E...H...H pattern in the sequence uniquely points to 2OG/Fe(II) oxygenases and Fe(2+). No other option is defensible given the observed sequence features."
  },
  "important_caveats": [
    "The primary cofactor annotation carries ECO:0000255 (computational, PROSITE-ProRule), but the 2024 JACS publication (PubMed 38578094) provides direct experimental evidence of Iron(II) dependence, strengthening the annotation.",
    "The HxD/E...H...H motif identification requires specialized knowledge of enzyme superfamily signatures; while generalizable, it is not trivially obvious to a general biology audience.",
    "Sequence identity is exact (SHA256 match confirmed between benchmark and UniProt source)."
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

**Accession:** `A0A455ZMR3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 20. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:18.557115+00:00.  

```json
"A0A455ZMR3"
```

Source SHA-256: `598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:18.557115+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"Pyrrolopyrazine biosynthesis cluster protein D"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"value":"1.14.11.-"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"value":"1.14.11.57"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"2-oxoglutarate-Fe(II) type oxidoreductase ppzD"}}}
```

Source SHA-256: `598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:18.557115+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29033"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00805","source":"PROSITE-ProRule"}],"name":"Fe(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00805","source":"PROSITE-ProRule"}],"value":"Binds 1 Fe(2+) ion per subunit."}]}}
```

Source SHA-256: `598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:18.557115+00:00.  

```json
{"citation":{"authors":["Rothchild K.W.","Hagar M.","Berry D.","Ryan K.S."],"citationCrossReferences":[{"database":"PubMed","id":"38578094"},{"database":"DOI","id":"10.1021/jacs.4c01419"}],"citationType":"journal article","firstPage":"10263","id":"38578094","journal":"J. Am. Chem. Soc.","lastPage":"10267","publicationDate":"2024","title":"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.","volume":"146"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:22.046089+00:00.  

```text
ID   PPZD_METMF              Reviewed;         349 AA.
AC   A0A455ZMR3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUN-2019, sequence version 1.
DT   28-JAN-2026, entry version 20.
DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzD {ECO:0000303|PubMed:30452111};
DE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};
DE            EC=1.14.11.57 {ECO:0000269|PubMed:38578094};
DE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein D {ECO:0000303|PubMed:30452111};
GN   Name=ppzD;
OS   Metarhizium majus (strain ARSEF 297).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;
OC   Metarhizium majus.
OX   NCBI_TaxID=1276143;
```

Source SHA-256: `1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:22.046089+00:00.  

```text
DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzD {ECO:0000303|PubMed:30452111};
DE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};
DE            EC=1.14.11.57 {ECO:0000269|PubMed:38578094};
DE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein D {ECO:0000303|PubMed:30452111};
```

Source SHA-256: `1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)  
**Locator:** `lines 25-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:22.046089+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=38578094; DOI=10.1021/jacs.4c01419;
RA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;
RT   "Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ
RT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.";
RL   J. Am. Chem. Soc. 146:10263-10267(2024).
```

Source SHA-256: `1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)  
**Locator:** `lines 77-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:22.046089+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00805};
CC       Note=Binds 1 Fe(2+) ion per subunit. {ECO:0000255|PROSITE-
CC       ProRule:PRU00805};
```

Source SHA-256: `1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
