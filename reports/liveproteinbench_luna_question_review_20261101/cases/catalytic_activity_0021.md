# catalytic_activity_0021

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQLSSIADKIRESATMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATIRTGKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYISMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPTGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGNQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.
B. 4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+)
C. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
D. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

## Luna’s full visible review

### Expected-answer support: supported

> The exact sequence matches the Mumps orthorubulavirus hemagglutinin-neuraminidase entry, whose catalytic activity is the reaction in choice A. The annotation cites experimental evidence for EC 3.2.1.18, although the primary study was not independently assessed here.

Cited evidence: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a hydrophobic segment consistent with membrane anchoring and a large extracellular region, which may make a membrane-associated viral protein more plausible than the soluble enzymes in B–D. That broad inference does not establish sialidase activity or the specific linkages in A.

**Missing item-specific fact**

> The protein-specific identification as a hemagglutinin-neuraminidase with sialidase activity is absent from the input and is needed to select A confidently.

**Reason**

> The sequence and choices provide, at most, broad contextual clues. Distinguishing the specific catalytic reaction requires a protein-specific functional annotation or experimental knowledge, not merely general biological reasoning.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The supplied evidence supports A for the sequence-matched protein; the other choices describe distinct reactions without comparable support.

### Important caveats

- The source annotation reports experimental evidence associated with a 2024 publication and specifies strain 13V165E2; the primary paper was not comprehensively retrieved or independently validated.
- Reviewer-only accession and annotation evidence were not present in the evaluated model input.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Mumps orthorubulavirus hemagglutinin-neuraminidase entry, whose catalytic activity is the reaction in choice A. The annotation cites experimental evidence for EC 3.2.1.18, although the primary study was not independently assessed here.",
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a hydrophobic segment consistent with membrane anchoring and a large extracellular region, which may make a membrane-associated viral protein more plausible than the soluble enzymes in B–D. That broad inference does not establish sialidase activity or the specific linkages in A.",
    "missing_item_specific_fact": "The protein-specific identification as a hemagglutinin-neuraminidase with sialidase activity is absent from the input and is needed to select A confidently.",
    "reason": "The sequence and choices provide, at most, broad contextual clues. Distinguishing the specific catalytic reaction requires a protein-specific functional annotation or experimental knowledge, not merely general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A for the sequence-matched protein; the other choices describe distinct reactions without comparable support."
  },
  "important_caveats": [
    "The source annotation reports experimental evidence associated with a 2024 publication and specifies strain 13V165E2; the primary paper was not comprehensively retrieved or independently validated.",
    "Reviewer-only accession and annotation evidence were not present in the evaluated model input."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9WAF5`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 130. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
"Q9WAF5"
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis"],"scientificName":"Mumps orthorubulavirus","taxonId":2560602}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39088577","source":"PubMed"}],"value":"3.2.1.18"}],"fullName":{"value":"Hemagglutinin-neuraminidase"}}}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.18","evidences":[{"evidenceCode":"ECO:0000269","id":"39088577","source":"PubMed"}],"name":"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates."}}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"citation":{"authors":["Takahashi T.","Kurebayashi Y.","Otsubo T.","Ikeda K.","Konagaya K.","Suzuki S.","Yamazaki M.","Suzuki K.","Narimichi Y.","Minami A.","Takeuchi H."],"citationCrossReferences":[{"database":"PubMed","id":"39088577"},{"database":"DOI","id":"10.1093/glycob/cwae059"}],"citationType":"journal article","firstPage":"0","id":"39088577","journal":"Glycobiology","lastPage":"0","publicationDate":"2024","title":"Novel sialidase inhibitors suppress mumps virus replication and infection.","volume":"34"},"referenceComments":[{"type":"STRAIN","value":"13V165E2"}],"referenceNumber":6,"referencePositions":["CATALYTIC ACTIVITY"]}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)  
**Locator:** `lines 93-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-02T04:33:57.899829+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-
CC         (2->8)- glycosidic linkages of terminal sialic acid residues in
CC         oligosaccharides, glycoproteins, glycolipids, colominic acid and
CC         synthetic substrates.; EC=3.2.1.18;
CC         Evidence={ECO:0000269|PubMed:39088577};
```

Source SHA-256: `eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 21). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
