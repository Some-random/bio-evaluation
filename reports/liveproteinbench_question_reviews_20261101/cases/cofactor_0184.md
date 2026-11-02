# cofactor_0184

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — pyridoxal 5&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI

[Multiple Choices]
A. Mn(2+)
B. pyridoxal 5'-phosphate
C. Na(+)
D. FMN
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

> The supplied sequence exactly matches the annotated tobacco chloroplastic cystathionine gamma-synthase. Its cofactor annotation states that it binds one pyridoxal 5'-phosphate per subunit, and the cited crystal-structure records report a complex with pyridoxal phosphate. This supports choice B.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Once identified as cystathionine gamma-synthase, its PLP-dependent catalytic role distinguishes B. But the prompt gives only the sequence, not that identity or a clear, independently interpretable family assignment.


**Missing item-specific fact**

> The protein's identity or family and its experimentally established PLP requirement; the sequence-to-annotation link is not supplied.


**Reason**

> The key is supported by reviewer-only, sequence-matched annotation and experimental literature references. Those facts were absent from the evaluated input; recognizing the exact sequence or recalling its database entry would be lookup or memorization, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched cofactor annotation supports PLP, and the options specify distinct candidate cofactors.


### Important caveats

- The evidence includes an annotation citing experimental studies and records of crystal structures in complex with PLP; the primary papers were not independently reviewed here.
- The current and archived entries match the supplied sequence, but the author's exact data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Once identified as cystathionine gamma-synthase, its PLP-dependent catalytic role distinguishes B. But the prompt gives only the sequence, not that identity or a clear, independently interpretable family assignment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity or family and its experimentally established PLP requirement; the sequence-to-annotation link is not supplied.",
    "reason": "The key is supported by reviewer-only, sequence-matched annotation and experimental literature references. Those facts were absent from the evaluated input; recognizing the exact sequence or recalling its database entry would be lookup or memorization, not reasoning from supplied context."
  },
  "case_id": "cofactor_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated tobacco chloroplastic cystathionine gamma-synthase. Its cofactor annotation states that it binds one pyridoxal 5'-phosphate per subunit, and the cited crystal-structure records report a complex with pyridoxal phosphate. This supports choice B."
  },
  "important_caveats": [
    "The evidence includes an annotation citing experimental studies and records of crystal structures in complex with PLP; the primary papers were not independently reviewed here.",
    "The current and archived entries match the supplied sequence, but the author's exact data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched cofactor annotation supports PLP, and the options specify distinct candidate cofactors."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated tobacco chloroplastic cystathionine gamma-synthase. Its cofactor annotation states that it binds one pyridoxal 5'-phosphate per subunit, and the cited crystal-structure records report a complex with pyridoxal phosphate. This supports choice B.",
    "evidence_ids": ["C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Once identified as cystathionine gamma-synthase, its PLP-dependent catalytic role distinguishes B. But the prompt gives only the sequence, not that identity or a clear, independently interpretable family assignment.",
    "missing_item_specific_fact": "The protein's identity or family and its experimentally established PLP requirement; the sequence-to-annotation link is not supplied.",
    "reason": "The key is supported by reviewer-only, sequence-matched annotation and experimental literature references. Those facts were absent from the evaluated input; recognizing the exact sequence or recalling its database entry would be lookup or memorization, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched cofactor annotation supports PLP, and the options specify distinct candidate cofactors."
  },
  "important_caveats": [
    "The evidence includes an annotation citing experimental studies and records of crystal structures in complex with PLP; the primary papers were not independently reviewed here.",
    "The current and archived entries match the supplied sequence, but the author's exact data-source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9ZPL5 (CGS1_TOBAC, cystathionine gamma-synthase 1, chloroplastic, EC 2.5.1.160) explicitly annotates pyridoxal 5'-phosphate as the cofactor with experimental evidence (ECO:0000269, direct assay) from two independent X-ray crystallography studies (PubMed 10438597, 11518531) showing PLP bound at LYS-356. The sequence matches exactly (SHA-256 confirmed). The annotation is backed by structural data, not mere computational inference.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If one could identify the protein as a transsulfuration enzyme (cystathionine gamma-synthase, EC 2.5.1.160), general biochemical knowledge would apply: transsulfuration enzymes that cleave/form C-S bonds in amino acid substrates universally require PLP to form a Schiff base with the substrate's amino group. Mn(2+) is associated with hydrolytic/oxidative enzymes, Na(+) is not a typical catalytic cofactor, and FMN is for oxidoreductases. This reasoning path is valid but entirely contingent on first identifying the enzyme family from the sequence.


**Missing item-specific fact**

> The critical step is recognizing from the 540-aa sequence that this protein belongs to the PLP-dependent transsulfuration enzyme family (cystathionine gamma-synthase / cystathionine beta-synthase / cystathionine gamma-lyase superfamily). The sequence provides no obvious functional annotation, no EC number, and no active-site context beyond the raw amino acid string. Identifying the conserved PLP-binding lysine (Lys-356) and the fold-type I PLP architecture from primary sequence alone, without structural information or family assignment, is not achievable through general reasoning. The identification requires either exact sequence recognition (database lookup) or prior memorization of this specific enzyme family.


**Reason**

> The general principle that amino acid C-S bond metabolizing transferases use PLP is well-known, but applying it requires first determining the enzyme's function from the sequence. No sequence motif, domain annotation, or contextual clue is provided that would allow a model to infer 'this is a transsulfuration enzyme' through reasoning alone. The question thus depends on recognizing the protein or its family, which is a lookup/memorization step.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the enzyme is correctly identified as a transsulfuration enzyme, only PLP is defensible. Mn(2+), Na(+), and FMN are not cofactors for gamma-synthase transsulfuration chemistry. The distractors are clearly wrong for this enzyme class. No ambiguity exists among the choices given the correct enzyme identification.


### Important caveats

- The sequence was first publicly released in UniProt on 2025-06-18 (entry version 110+), so this is a relatively recent annotation; the author's source snapshot is unknown.
- The PLP cofactor assignment is backed by two independent X-ray crystallography structures at 2.90 Å and 3.10 Å showing PLP covalently bound at Lys-356, providing strong experimental support.
- The reviewer-only evidence (accession, annotation excerpts) was not available to the evaluated model; the model had only the raw sequence and four choices.
- The entry was integrated into Swiss-Prot as recently as January 2026, meaning the protein was previously unreviewed or absent from curated databases, potentially affecting training-data availability for models.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If one could identify the protein as a transsulfuration enzyme (cystathionine gamma-synthase, EC 2.5.1.160), general biochemical knowledge would apply: transsulfuration enzymes that cleave/form C-S bonds in amino acid substrates universally require PLP to form a Schiff base with the substrate's amino group. Mn(2+) is associated with hydrolytic/oxidative enzymes, Na(+) is not a typical catalytic cofactor, and FMN is for oxidoreductases. This reasoning path is valid but entirely contingent on first identifying the enzyme family from the sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The critical step is recognizing from the 540-aa sequence that this protein belongs to the PLP-dependent transsulfuration enzyme family (cystathionine gamma-synthase / cystathionine beta-synthase / cystathionine gamma-lyase superfamily). The sequence provides no obvious functional annotation, no EC number, and no active-site context beyond the raw amino acid string. Identifying the conserved PLP-binding lysine (Lys-356) and the fold-type I PLP architecture from primary sequence alone, without structural information or family assignment, is not achievable through general reasoning. The identification requires either exact sequence recognition (database lookup) or prior memorization of this specific enzyme family.",
    "reason": "The general principle that amino acid C-S bond metabolizing transferases use PLP is well-known, but applying it requires first determining the enzyme's function from the sequence. No sequence motif, domain annotation, or contextual clue is provided that would allow a model to infer 'this is a transsulfuration enzyme' through reasoning alone. The question thus depends on recognizing the protein or its family, which is a lookup/memorization step."
  },
  "case_id": "cofactor_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9ZPL5 (CGS1_TOBAC, cystathionine gamma-synthase 1, chloroplastic, EC 2.5.1.160) explicitly annotates pyridoxal 5'-phosphate as the cofactor with experimental evidence (ECO:0000269, direct assay) from two independent X-ray crystallography studies (PubMed 10438597, 11518531) showing PLP bound at LYS-356. The sequence matches exactly (SHA-256 confirmed). The annotation is backed by structural data, not mere computational inference."
  },
  "important_caveats": [
    "The sequence was first publicly released in UniProt on 2025-06-18 (entry version 110+), so this is a relatively recent annotation; the author's source snapshot is unknown.",
    "The PLP cofactor assignment is backed by two independent X-ray crystallography structures at 2.90 Å and 3.10 Å showing PLP covalently bound at Lys-356, providing strong experimental support.",
    "The reviewer-only evidence (accession, annotation excerpts) was not available to the evaluated model; the model had only the raw sequence and four choices.",
    "The entry was integrated into Swiss-Prot as recently as January 2026, meaning the protein was previously unreviewed or absent from curated databases, potentially affecting training-data availability for models."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the enzyme is correctly identified as a transsulfuration enzyme, only PLP is defensible. Mn(2+), Na(+), and FMN are not cofactors for gamma-synthase transsulfuration chemistry. The distractors are clearly wrong for this enzyme class. No ambiguity exists among the choices given the correct enzyme identification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9ZPL5 (CGS1_TOBAC, cystathionine gamma-synthase 1, chloroplastic, EC 2.5.1.160) explicitly annotates pyridoxal 5'-phosphate as the cofactor with experimental evidence (ECO:0000269, direct assay) from two independent X-ray crystallography studies (PubMed 10438597, 11518531) showing PLP bound at LYS-356. The sequence matches exactly (SHA-256 confirmed). The annotation is backed by structural data, not mere computational inference.",
    "evidence_ids": ["C5", "C7", "C8", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If one could identify the protein as a transsulfuration enzyme (cystathionine gamma-synthase, EC 2.5.1.160), general biochemical knowledge would apply: transsulfuration enzymes that cleave/form C-S bonds in amino acid substrates universally require PLP to form a Schiff base with the substrate's amino group. Mn(2+) is associated with hydrolytic/oxidative enzymes, Na(+) is not a typical catalytic cofactor, and FMN is for oxidoreductases. This reasoning path is valid but entirely contingent on first identifying the enzyme family from the sequence.",
    "missing_item_specific_fact": "The critical step is recognizing from the 540-aa sequence that this protein belongs to the PLP-dependent transsulfuration enzyme family (cystathionine gamma-synthase / cystathionine beta-synthase / cystathionine gamma-lyase superfamily). The sequence provides no obvious functional annotation, no EC number, and no active-site context beyond the raw amino acid string. Identifying the conserved PLP-binding lysine (Lys-356) and the fold-type I PLP architecture from primary sequence alone, without structural information or family assignment, is not achievable through general reasoning. The identification requires either exact sequence recognition (database lookup) or prior memorization of this specific enzyme family.",
    "reason": "The general principle that amino acid C-S bond metabolizing transferases use PLP is well-known, but applying it requires first determining the enzyme's function from the sequence. No sequence motif, domain annotation, or contextual clue is provided that would allow a model to infer 'this is a transsulfuration enzyme' through reasoning alone. The question thus depends on recognizing the protein or its family, which is a lookup/memorization step."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the enzyme is correctly identified as a transsulfuration enzyme, only PLP is defensible. Mn(2+), Na(+), and FMN are not cofactors for gamma-synthase transsulfuration chemistry. The distractors are clearly wrong for this enzyme class. No ambiguity exists among the choices given the correct enzyme identification."
  },
  "important_caveats": [
    "The sequence was first publicly released in UniProt on 2025-06-18 (entry version 110+), so this is a relatively recent annotation; the author's source snapshot is unknown.",
    "The PLP cofactor assignment is backed by two independent X-ray crystallography structures at 2.90 Å and 3.10 Å showing PLP covalently bound at Lys-356, providing strong experimental support.",
    "The reviewer-only evidence (accession, annotation excerpts) was not available to the evaluated model; the model had only the raw sequence and four choices.",
    "The entry was integrated into Swiss-Prot as recently as January 2026, meaning the protein was previously unreviewed or absent from curated databases, potentially affecting training-data availability for models."
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

**Accession:** `Q9ZPL5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 110. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:597326"},"evidences":[{"evidenceCode":"ECO:0000269","id":"10438597","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"11518531","source":"PubMed"}],"name":"pyridoxal 5'-phosphate"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10438597","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"11518531","source":"PubMed"}],"value":"Binds 1 pyridoxal 5'-phosphate per subunit."}]}}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"citation":{"authors":["Steegborn C.","Messerschmidt A.","Laber B.","Streber W.","Huber R.","Clausen T."],"citationCrossReferences":[{"database":"PubMed","id":"10438597"},{"database":"DOI","id":"10.1006/jmbi.1999.2935"}],"citationType":"journal article","firstPage":"983","id":"10438597","journal":"J. Mol. Biol.","lastPage":"996","publicationDate":"1999","title":"The crystal structure of cystathionine gamma-synthase from Nicotiana tabacum reveals its substrate and reaction specificity.","volume":"290"},"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.90 ANGSTROMS) IN COMPLEX WITH PYRIDOXAL PHOSPHATE AT LYS-356","COFACTOR","SUBUNIT"]}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"citation":{"authors":["Steegborn C.","Laber B.","Messerschmidt A.","Huber R.","Clausen T."],"citationCrossReferences":[{"database":"PubMed","id":"11518531"},{"database":"DOI","id":"10.1006/jmbi.2001.4880"}],"citationType":"journal article","firstPage":"789","id":"11518531","journal":"J. Mol. Biol.","lastPage":"801","publicationDate":"2001","title":"Crystal structures of cystathionine gamma-synthase inhibitor complexes rationalize the increased affinity of a novel inhibitor.","volume":"311"},"referenceNumber":5,"referencePositions":["X-RAY CRYSTALLOGRAPHY (3.10 ANGSTROMS) IN COMPLEX WITH PYRIDOXAL PHOSPHATE AT LYS-356","COFACTOR","SUBUNIT"]}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 38-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
RN   [4]
RP   X-RAY CRYSTALLOGRAPHY (2.90 ANGSTROMS) IN COMPLEX WITH PYRIDOXAL PHOSPHATE
RP   AT LYS-356, COFACTOR, AND SUBUNIT.
RX   PubMed=10438597; DOI=10.1006/jmbi.1999.2935;
RA   Steegborn C., Messerschmidt A., Laber B., Streber W., Huber R., Clausen T.;
RT   "The crystal structure of cystathionine gamma-synthase from Nicotiana
RT   tabacum reveals its substrate and reaction specificity.";
RL   J. Mol. Biol. 290:983-996(1999).
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 46-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
RN   [5]
RP   X-RAY CRYSTALLOGRAPHY (3.10 ANGSTROMS) IN COMPLEX WITH PYRIDOXAL PHOSPHATE
RP   AT LYS-356, COFACTOR, AND SUBUNIT.
RX   PubMed=11518531; DOI=10.1006/jmbi.2001.4880;
RA   Steegborn C., Laber B., Messerschmidt A., Huber R., Clausen T.;
RT   "Crystal structures of cystathionine gamma-synthase inhibitor complexes
RT   rationalize the increased affinity of a novel inhibitor.";
RL   J. Mol. Biol. 311:789-801(2001).
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 68-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;
CC         Evidence={ECO:0000269|PubMed:10438597, ECO:0000269|PubMed:11518531};
CC       Note=Binds 1 pyridoxal 5'-phosphate per subunit.
CC       {ECO:0000269|PubMed:10438597, ECO:0000269|PubMed:11518531};
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
