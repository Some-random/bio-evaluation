# cofactor_0027

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — heme

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLLRPAKYQLPLPPGPRGLPIIGNLHQAPKEKAWEVYKQWSDRYGPIMSVNNGGMITIIVSSHEVVKNFLEKNNAVFSSRPQLLVLERALYGFTTPALPYGEKWLKHRALRGAVLKPAMAVRYRGLQDLESKQLLRDLLYSEDFTQCMRRQAASLFLGIAYGNRFPEETPEIIDIDQAVAQLGGISESMFQGTGMLREFFPVLKYFPGYDKFLKQLDDVGERLANIYVRRFRDGLSTPAWNWAKEYSKRPEAQGMGELELSFCIGSTYQASLTPYEILRIILLAAICHPEEKARLQKEIDLVVGKDNLPGWEHKDRIQFVQAFIYEALRWHAFSPLGAPRAVSRDIEYKGYFIPKGATLVLNQWAMDHDENVYDNPFTFRPQRWIDNPDLPHVIFGFGLRGCPGQHLARDHLFINTARLFWAFNFGNAYENGKKVELDLDELMQPRGGGSAFNQVPSFKASVIIRSSERRQIVENEWDAVEKDEQKILAEAMPLPE

[Multiple Choices]
A. tungstopterin
B. heme b
C. cob(II)alamin
D. heme
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

> The sequence is consistent with a cytochrome P450, including its conserved heme-binding cysteine motif, supporting a heme cofactor. The matched UniProt record also annotates heme, but that annotation is transferred by similarity rather than direct evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The P450-like sequence and conserved heme-binding motif support heme over tungstopterin or cob(II)alamin.


**Missing item-specific fact**

> To select the database’s exact label, rather than the chemically overlapping option, one would need the protein-specific annotation identifying the cofactor as “heme.”


**Reason**

> Sequence reasoning supports the heme class, but does not cleanly distinguish the keyed “heme” option from “heme b,” a specific form commonly meant by heme in this context. The exact keyed wording depends on annotation convention.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Cytochrome P450s use heme b; “heme” is a broader label that can refer to that same cofactor, so both choices are defensible without a definition that distinguishes the terms.


### Important caveats

- The matched database cofactor annotation is supported by transferred evidence, not direct experimental evidence shown here.
- The reviewer-only accession and annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The P450-like sequence and conserved heme-binding motif support heme over tungstopterin or cob(II)alamin.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "To select the database’s exact label, rather than the chemically overlapping option, one would need the protein-specific annotation identifying the cofactor as “heme.”",
    "reason": "Sequence reasoning supports the heme class, but does not cleanly distinguish the keyed “heme” option from “heme b,” a specific form commonly meant by heme in this context. The exact keyed wording depends on annotation convention."
  },
  "case_id": "cofactor_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence is consistent with a cytochrome P450, including its conserved heme-binding cysteine motif, supporting a heme cofactor. The matched UniProt record also annotates heme, but that annotation is transferred by similarity rather than direct evidence for this exact protein."
  },
  "important_caveats": [
    "The matched database cofactor annotation is supported by transferred evidence, not direct experimental evidence shown here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Cytochrome P450s use heme b; “heme” is a broader label that can refer to that same cofactor, so both choices are defensible without a definition that distinguishes the terms."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence is consistent with a cytochrome P450, including its conserved heme-binding cysteine motif, supporting a heme cofactor. The matched UniProt record also annotates heme, but that annotation is transferred by similarity rather than direct evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The P450-like sequence and conserved heme-binding motif support heme over tungstopterin or cob(II)alamin.",
    "missing_item_specific_fact": "To select the database’s exact label, rather than the chemically overlapping option, one would need the protein-specific annotation identifying the cofactor as “heme.”",
    "reason": "Sequence reasoning supports the heme class, but does not cleanly distinguish the keyed “heme” option from “heme b,” a specific form commonly meant by heme in this context. The exact keyed wording depends on annotation convention."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Cytochrome P450s use heme b; “heme” is a broader label that can refer to that same cofactor, so both choices are defensible without a definition that distinguishes the terms."
  },
  "important_caveats": [
    "The matched database cofactor annotation is supported by transferred evidence, not direct experimental evidence shown here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A2Z5U6I9 (529 aa, SHA-256 confirmed), annotated as 'Cytochrome P450 monooxygenase okaD' (EC 1.14.99.-) from Penicillium ochrochloron. The UniProt COFACTOR comment explicitly lists 'heme' (ChEBI:30413), evidenced by similarity to P04798 (ECO:0000250). All cytochrome P450 enzymes are heme-dependent monooxygenases; heme is a defining cofactor of the P450 superfamily. The annotation is by similarity rather than direct experimental cofactor measurement for this specific protein, but the protein is explicitly classified as a P450 monooxygenase with EC 1.14.99.-, making heme a near-definitional cofactor. The expected answer 'heme' (D) is well-supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits recognizable P450 family hallmarks: (1) a 529-residue length typical of fungal microsomal P450s; (2) an N-terminal hydrophobic transmembrane/signal region (MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLL) characteristic of membrane-associated P450s; (3) a conserved heme-binding motif region containing the critical proximal Cys ligand (visible in the segment '…GCPGQHLARDHLFINTARLFWAFNFGNAYENGK…' where the Cys coordinates the heme iron). Recognizing these features identifies the protein as a cytochrome P450 monooxygenase, and P450 enzymes are by definition heme-dependent. Tungstopterin (A) is associated with formylmethanofuran dehydrogenase in methanogenic archaea; cob(II)alamin (C) is associated with B12-dependent enzymes such as certain methyltransferases and mutases. Neither is plausible for a eukaryotic fungal P450.


**Missing item-specific fact**

> The precise distinction between 'heme' (D) and 'heme b' (B) is not fully resolvable from sequence features alone. P450s specifically use heme b (protoporphyrin IX–Fe), which is a subtype of heme. The UniProt annotation uses the general term 'heme' (ChEBI:30413) rather than 'heme b' (ChEBI:30414). Choosing D over B requires knowing the annotation convention or accepting that 'heme' is the standard general term for P450 cofactors.


**Reason**

> Identifying the protein as a P450 from sequence features (N-terminal TM region, conserved Cys heme-ligand motif, family-typical length) and concluding heme is the cofactor constitutes a concrete biological reasoning chain. Distractors A and C are eliminated by general knowledge of cofactor–enzyme class associations. The residual B-vs-D ambiguity is a granularity issue (general vs. specific heme subtype) rather than a lookup of an item-specific fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> P450 enzymes specifically bind heme b (protoporphyrin IX with Fe²⁺), making 'heme b' (B) biochemically precise. 'Heme' (D) is the general class term and is what UniProt annotates (ChEBI:30413). Both are defensible descriptions of the P450 cofactor. The question wording ('the specific cofactor') could arguably favor the more specific 'heme b,' but the author key and UniProt annotation use the general term 'heme.' This is a granularity ambiguity rather than a factual error, but it means a knowledgeable respondent could reasonably select B.


### Important caveats

- The UniProt heme annotation carries evidence code ECO:0000250 (inferred by similarity to P04798), not direct experimental cofactor measurement for okaD specifically. However, the protein is explicitly named a cytochrome P450 monooxygenase with EC 1.14.99.-, for which heme is definitional.
- The distinction between 'heme' (D) and 'heme b' (B) is a granularity issue; both are correct descriptions of the P450 cofactor. The key follows the UniProt annotation convention.
- The reviewer-only UniProt accession and metadata were absent from the evaluated model input; the model must rely on sequence features and general biological knowledge.
- The historical UniProt entry (version 23, first released 2026-01) and current entry (version 24) both carry the same heme cofactor annotation and sequence match.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits recognizable P450 family hallmarks: (1) a 529-residue length typical of fungal microsomal P450s; (2) an N-terminal hydrophobic transmembrane/signal region (MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLL) characteristic of membrane-associated P450s; (3) a conserved heme-binding motif region containing the critical proximal Cys ligand (visible in the segment '…GCPGQHLARDHLFINTARLFWAFNFGNAYENGK…' where the Cys coordinates the heme iron). Recognizing these features identifies the protein as a cytochrome P450 monooxygenase, and P450 enzymes are by definition heme-dependent. Tungstopterin (A) is associated with formylmethanofuran dehydrogenase in methanogenic archaea; cob(II)alamin (C) is associated with B12-dependent enzymes such as certain methyltransferases and mutases. Neither is plausible for a eukaryotic fungal P450.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise distinction between 'heme' (D) and 'heme b' (B) is not fully resolvable from sequence features alone. P450s specifically use heme b (protoporphyrin IX–Fe), which is a subtype of heme. The UniProt annotation uses the general term 'heme' (ChEBI:30413) rather than 'heme b' (ChEBI:30414). Choosing D over B requires knowing the annotation convention or accepting that 'heme' is the standard general term for P450 cofactors.",
    "reason": "Identifying the protein as a P450 from sequence features (N-terminal TM region, conserved Cys heme-ligand motif, family-typical length) and concluding heme is the cofactor constitutes a concrete biological reasoning chain. Distractors A and C are eliminated by general knowledge of cofactor–enzyme class associations. The residual B-vs-D ambiguity is a granularity issue (general vs. specific heme subtype) rather than a lookup of an item-specific fact."
  },
  "case_id": "cofactor_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A2Z5U6I9 (529 aa, SHA-256 confirmed), annotated as 'Cytochrome P450 monooxygenase okaD' (EC 1.14.99.-) from Penicillium ochrochloron. The UniProt COFACTOR comment explicitly lists 'heme' (ChEBI:30413), evidenced by similarity to P04798 (ECO:0000250). All cytochrome P450 enzymes are heme-dependent monooxygenases; heme is a defining cofactor of the P450 superfamily. The annotation is by similarity rather than direct experimental cofactor measurement for this specific protein, but the protein is explicitly classified as a P450 monooxygenase with EC 1.14.99.-, making heme a near-definitional cofactor. The expected answer 'heme' (D) is well-supported."
  },
  "important_caveats": [
    "The UniProt heme annotation carries evidence code ECO:0000250 (inferred by similarity to P04798), not direct experimental cofactor measurement for okaD specifically. However, the protein is explicitly named a cytochrome P450 monooxygenase with EC 1.14.99.-, for which heme is definitional.",
    "The distinction between 'heme' (D) and 'heme b' (B) is a granularity issue; both are correct descriptions of the P450 cofactor. The key follows the UniProt annotation convention.",
    "The reviewer-only UniProt accession and metadata were absent from the evaluated model input; the model must rely on sequence features and general biological knowledge.",
    "The historical UniProt entry (version 23, first released 2026-01) and current entry (version 24) both carry the same heme cofactor annotation and sequence match."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "P450 enzymes specifically bind heme b (protoporphyrin IX with Fe²⁺), making 'heme b' (B) biochemically precise. 'Heme' (D) is the general class term and is what UniProt annotates (ChEBI:30413). Both are defensible descriptions of the P450 cofactor. The question wording ('the specific cofactor') could arguably favor the more specific 'heme b,' but the author key and UniProt annotation use the general term 'heme.' This is a granularity ambiguity rather than a factual error, but it means a knowledgeable respondent could reasonably select B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A2Z5U6I9 (529 aa, SHA-256 confirmed), annotated as 'Cytochrome P450 monooxygenase okaD' (EC 1.14.99.-) from Penicillium ochrochloron. The UniProt COFACTOR comment explicitly lists 'heme' (ChEBI:30413), evidenced by similarity to P04798 (ECO:0000250). All cytochrome P450 enzymes are heme-dependent monooxygenases; heme is a defining cofactor of the P450 superfamily. The annotation is by similarity rather than direct experimental cofactor measurement for this specific protein, but the protein is explicitly classified as a P450 monooxygenase with EC 1.14.99.-, making heme a near-definitional cofactor. The expected answer 'heme' (D) is well-supported.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits recognizable P450 family hallmarks: (1) a 529-residue length typical of fungal microsomal P450s; (2) an N-terminal hydrophobic transmembrane/signal region (MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLL) characteristic of membrane-associated P450s; (3) a conserved heme-binding motif region containing the critical proximal Cys ligand (visible in the segment '…GCPGQHLARDHLFINTARLFWAFNFGNAYENGK…' where the Cys coordinates the heme iron). Recognizing these features identifies the protein as a cytochrome P450 monooxygenase, and P450 enzymes are by definition heme-dependent. Tungstopterin (A) is associated with formylmethanofuran dehydrogenase in methanogenic archaea; cob(II)alamin (C) is associated with B12-dependent enzymes such as certain methyltransferases and mutases. Neither is plausible for a eukaryotic fungal P450.",
    "missing_item_specific_fact": "The precise distinction between 'heme' (D) and 'heme b' (B) is not fully resolvable from sequence features alone. P450s specifically use heme b (protoporphyrin IX–Fe), which is a subtype of heme. The UniProt annotation uses the general term 'heme' (ChEBI:30413) rather than 'heme b' (ChEBI:30414). Choosing D over B requires knowing the annotation convention or accepting that 'heme' is the standard general term for P450 cofactors.",
    "reason": "Identifying the protein as a P450 from sequence features (N-terminal TM region, conserved Cys heme-ligand motif, family-typical length) and concluding heme is the cofactor constitutes a concrete biological reasoning chain. Distractors A and C are eliminated by general knowledge of cofactor–enzyme class associations. The residual B-vs-D ambiguity is a granularity issue (general vs. specific heme subtype) rather than a lookup of an item-specific fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "P450 enzymes specifically bind heme b (protoporphyrin IX with Fe²⁺), making 'heme b' (B) biochemically precise. 'Heme' (D) is the general class term and is what UniProt annotates (ChEBI:30413). Both are defensible descriptions of the P450 cofactor. The question wording ('the specific cofactor') could arguably favor the more specific 'heme b,' but the author key and UniProt annotation use the general term 'heme.' This is a granularity ambiguity rather than a factual error, but it means a knowledgeable respondent could reasonably select B."
  },
  "important_caveats": [
    "The UniProt heme annotation carries evidence code ECO:0000250 (inferred by similarity to P04798), not direct experimental cofactor measurement for okaD specifically. However, the protein is explicitly named a cytochrome P450 monooxygenase with EC 1.14.99.-, for which heme is definitional.",
    "The distinction between 'heme' (D) and 'heme b' (B) is a granularity issue; both are correct descriptions of the P450 cofactor. The key follows the UniProt annotation convention.",
    "The reviewer-only UniProt accession and metadata were absent from the evaluated model input; the model must rely on sequence features and general biological knowledge.",
    "The historical UniProt entry (version 23, first released 2026-01) and current entry (version 24) both carry the same heme cofactor annotation and sequence match."
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

**Accession:** `A0A2Z5U6I9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 23. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:54.111891+00:00.  

```json
"A0A2Z5U6I9"
```

Source SHA-256: `40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:54.111891+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Okaramines biosynthesis cluster protein D"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"value":"1.14.99.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase okaD"}}}
```

Source SHA-256: `40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:54.111891+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:30413"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P04798","source":"UniProtKB"}],"name":"heme"}],"commentType":"COFACTOR"}
```

Source SHA-256: `40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:54.111891+00:00.  

```json
{"citation":{"authors":["Lai C.Y.","Lo I.W.","Hewage R.T.","Chen Y.C.","Chen C.T.","Lee C.F.","Lin S.","Tang M.C.","Lin H.C."],"citationCrossReferences":[{"database":"PubMed","id":"28631282"},{"database":"DOI","id":"10.1002/anie.201705501"}],"citationType":"journal article","firstPage":"9478","id":"28631282","journal":"Angew. Chem. Int. Ed.","lastPage":"9482","publicationDate":"2017","title":"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.","volume":"56"},"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:57.209412+00:00.  

```text
ID   OKAD_PENOH              Reviewed;         529 AA.
AC   A0A2Z5U6I9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-OCT-2018, sequence version 1.
DT   28-JAN-2026, entry version 23.
DE   RecName: Full=Cytochrome P450 monooxygenase okaD {ECO:0000303|PubMed:28631282};
DE            EC=1.14.99.- {ECO:0000269|PubMed:28631282};
DE   AltName: Full=Okaramines biosynthesis cluster protein D {ECO:0000303|PubMed:28631282};
GN   Name=okaD {ECO:0000303|PubMed:28631282};
OS   Penicillium ochrochloron.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=69780;
```

Source SHA-256: `325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:57.209412+00:00.  

```text
DE   RecName: Full=Cytochrome P450 monooxygenase okaD {ECO:0000303|PubMed:28631282};
DE            EC=1.14.99.- {ECO:0000269|PubMed:28631282};
DE   AltName: Full=Okaramines biosynthesis cluster protein D {ECO:0000303|PubMed:28631282};
```

Source SHA-256: `325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)  
**Locator:** `lines 67-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:57.209412+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=heme; Xref=ChEBI:CHEBI:30413;
CC         Evidence={ECO:0000250|UniProtKB:P04798};
```

Source SHA-256: `325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
