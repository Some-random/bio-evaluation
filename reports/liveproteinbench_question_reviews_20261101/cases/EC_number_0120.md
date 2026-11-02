# EC_number_0120

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.2.1.183

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSASGKEKPLKDVPGSYGVPVVGALKDRLDFYWFQGEVEFYKSRMEKNQSTVFRVNFPPGPPGFPEGHGIVLLDQVSYSVLLDNAKVDKRDTLIGSYMPDLAFTGGYRTLPYLDTAEEKHTTYKSLMFEILHESAQRFGPELSSAFDRTAQEWEAKIAKDGSVESLSTAGNMVIQFLYKTITHQDPMATMGDDPHSVYMAWTGVQFAGIAYTNLPHITEELLMHSFQLPFFPIKKKYEQIVEFFRSAGSGLLDLAVTKYGLDREEALHNLVFSFGINTRLGLLKMFPPILFFIARAGAEFQARLKQEIRGRMKKREDAASIQALGDLKLVKATVLEVFRLMPSIFVAFGRARQDLEVESHDARYKIKKGELLGTHQYFVMRDPVVFKDPHSFVPDRFMGSEGAALLPHIVWSNGRETDSPTPTNKQCPGKNQAELIAVQFIAEMFLRYDSWEVTQESSVSATKLDVHLCKLVKRS

[Multiple Choices]
A. 4.2.1.70
B. 5.3.1.16
C. 4.2.1.183
D. 3.6.1.5
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the recorded CYP74M1 sequence. The matched UniProt record assigns EC 4.2.1.183 and links that assignment to experimental evidence for the enzyme's catalytic reactions.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could suggest an enzyme family, but the input gives no organism, functional annotation, substrate, or reaction context that specifically distinguishes divinyl ether synthase activity from the listed alternatives.


**Missing item-specific fact**

> The protein-specific catalytic activity—divinyl ether synthase CYP74M1, supported by the reported substrate-to-product reactions—is needed to identify EC 4.2.1.183.


**Reason**

> Selecting the precise EC number depends on an item-specific functional annotation or experimental result not supplied in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's experimental activity supports choice C; the evidence provided does not support another listed EC number.


### Important caveats

- The annotation is linked to experimental evidence (ECO:0000269) and a cited publication, but the primary paper was not independently reviewed here.
- The sequence matches both the current record and a historical record; the author's exact data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could suggest an enzyme family, but the input gives no organism, functional annotation, substrate, or reaction context that specifically distinguishes divinyl ether synthase activity from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—divinyl ether synthase CYP74M1, supported by the reported substrate-to-product reactions—is needed to identify EC 4.2.1.183.",
    "reason": "Selecting the precise EC number depends on an item-specific functional annotation or experimental result not supplied in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "EC_number_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the recorded CYP74M1 sequence. The matched UniProt record assigns EC 4.2.1.183 and links that assignment to experimental evidence for the enzyme's catalytic reactions."
  },
  "important_caveats": [
    "The annotation is linked to experimental evidence (ECO:0000269) and a cited publication, but the primary paper was not independently reviewed here.",
    "The sequence matches both the current record and a historical record; the author's exact data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's experimental activity supports choice C; the evidence provided does not support another listed EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the recorded CYP74M1 sequence. The matched UniProt record assigns EC 4.2.1.183 and links that assignment to experimental evidence for the enzyme's catalytic reactions.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could suggest an enzyme family, but the input gives no organism, functional annotation, substrate, or reaction context that specifically distinguishes divinyl ether synthase activity from the listed alternatives.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—divinyl ether synthase CYP74M1, supported by the reported substrate-to-product reactions—is needed to identify EC 4.2.1.183.",
    "reason": "Selecting the precise EC number depends on an item-specific functional annotation or experimental result not supplied in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's experimental activity supports choice C; the evidence provided does not support another listed EC number."
  },
  "important_caveats": [
    "The annotation is linked to experimental evidence (ECO:0000269) and a cited publication, but the primary paper was not independently reviewed here.",
    "The sequence matches both the current record and a historical record; the author's exact data-source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt D8S724 (C74M1_SELML) exactly (475 aa, SHA-256 match). The entry is annotated as 'Divinyl ether synthase CYP74M1' with EC 4.2.1.183, supported by experimental evidence (ECO:0000269|PubMed:26776054, Gorina et al. 2016). Two catalytic reactions are documented: (13S)-hydroperoxy-(9Z,11E)-octadecadienoate → etheroleate + H2O and (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate → etherolenate + H2O, both assigned EC 4.2.1.183. The evidence code ECO:0000269 indicates direct experimental evidence from the cited publication.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The protein sequence exhibits hallmarks of a cytochrome P450 (length ~475 aa, conserved P450 motifs including a heme-binding region with FxxGxRxCxG-like pattern, overall composition). Recognizing the P450 fold eliminates EC 3.6.1.5 (hydrolase, option D) and EC 5.3.1.16 (isomerase, option B) since P450s are not hydrolases or isomerases. CYP74-family P450s acting on fatty acid hydroperoxides are classified as hydro-lyases (EC 4.2.1.x), which is consistent with both options A and C. However, distinguishing 4.2.1.70 from 4.2.1.183 requires knowing the specific reaction catalyzed and the EC assignment for this particular CYP74M subfamily.


**Missing item-specific fact**

> The specific identity of EC 4.2.1.70 (whether it is a P450 enzyme or an unrelated hydro-lyase) and the knowledge that EC 4.2.1.183 was specifically assigned to CYP74M divinyl ether synthases in 2016 (PubMed:26776054). Without knowing what reaction EC 4.2.1.70 catalyzes and whether it involves a P450 scaffold, a model cannot definitively eliminate option A through sequence reasoning alone.


**Reason**

> While P450 recognition provides a strong reasoning path to eliminate options B and D, the final distinction between A (4.2.1.70) and C (4.2.1.183) depends on knowing the specific EC number assignments within the CYP74 subfamily and what enzyme 4.2.1.70 represents. EC 4.2.1.183 is a recently assigned number (2016) specific to divinyl ether synthase activity of CYP74M enzymes. This is an item-specific annotation fact not derivable from general sequence features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> If 4.2.1.70 is confirmed to be a non-P450 hydro-lyase (which is likely given the diversity of enzymes in the 4.2.1.x class), then P450 recognition would eliminate A as well, leaving C as the only defensible answer. However, without confirming the identity of 4.2.1.70, a model might hesitate between A and C. The evidence strongly supports C as correct.


### Important caveats

- The EC number 4.2.1.183 was assigned in 2016 (PubMed:26776054) and is relatively recent; models trained on older data may not have encountered it.
- The P450 heme-binding motif in this CYP74 sequence appears in a somewhat degenerate form (FGRARQ region), which may make P450 recognition less straightforward than in canonical P450s.
- The identity of EC 4.2.1.70 was not independently verified in the reviewer evidence; if it happens to also be a P450 enzyme, the A vs C distinction becomes more challenging.
- The UniProt entry was first publicly released in June 2025, meaning the annotation may not have been available in training data used to construct this benchmark.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence exhibits hallmarks of a cytochrome P450 (length ~475 aa, conserved P450 motifs including a heme-binding region with FxxGxRxCxG-like pattern, overall composition). Recognizing the P450 fold eliminates EC 3.6.1.5 (hydrolase, option D) and EC 5.3.1.16 (isomerase, option B) since P450s are not hydrolases or isomerases. CYP74-family P450s acting on fatty acid hydroperoxides are classified as hydro-lyases (EC 4.2.1.x), which is consistent with both options A and C. However, distinguishing 4.2.1.70 from 4.2.1.183 requires knowing the specific reaction catalyzed and the EC assignment for this particular CYP74M subfamily.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of EC 4.2.1.70 (whether it is a P450 enzyme or an unrelated hydro-lyase) and the knowledge that EC 4.2.1.183 was specifically assigned to CYP74M divinyl ether synthases in 2016 (PubMed:26776054). Without knowing what reaction EC 4.2.1.70 catalyzes and whether it involves a P450 scaffold, a model cannot definitively eliminate option A through sequence reasoning alone.",
    "reason": "While P450 recognition provides a strong reasoning path to eliminate options B and D, the final distinction between A (4.2.1.70) and C (4.2.1.183) depends on knowing the specific EC number assignments within the CYP74 subfamily and what enzyme 4.2.1.70 represents. EC 4.2.1.183 is a recently assigned number (2016) specific to divinyl ether synthase activity of CYP74M enzymes. This is an item-specific annotation fact not derivable from general sequence features alone."
  },
  "case_id": "EC_number_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt D8S724 (C74M1_SELML) exactly (475 aa, SHA-256 match). The entry is annotated as 'Divinyl ether synthase CYP74M1' with EC 4.2.1.183, supported by experimental evidence (ECO:0000269|PubMed:26776054, Gorina et al. 2016). Two catalytic reactions are documented: (13S)-hydroperoxy-(9Z,11E)-octadecadienoate → etheroleate + H2O and (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate → etherolenate + H2O, both assigned EC 4.2.1.183. The evidence code ECO:0000269 indicates direct experimental evidence from the cited publication."
  },
  "important_caveats": [
    "The EC number 4.2.1.183 was assigned in 2016 (PubMed:26776054) and is relatively recent; models trained on older data may not have encountered it.",
    "The P450 heme-binding motif in this CYP74 sequence appears in a somewhat degenerate form (FGRARQ region), which may make P450 recognition less straightforward than in canonical P450s.",
    "The identity of EC 4.2.1.70 was not independently verified in the reviewer evidence; if it happens to also be a P450 enzyme, the A vs C distinction becomes more challenging.",
    "The UniProt entry was first publicly released in June 2025, meaning the annotation may not have been available in training data used to construct this benchmark."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "If 4.2.1.70 is confirmed to be a non-P450 hydro-lyase (which is likely given the diversity of enzymes in the 4.2.1.x class), then P450 recognition would eliminate A as well, leaving C as the only defensible answer. However, without confirming the identity of 4.2.1.70, a model might hesitate between A and C. The evidence strongly supports C as correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt D8S724 (C74M1_SELML) exactly (475 aa, SHA-256 match). The entry is annotated as 'Divinyl ether synthase CYP74M1' with EC 4.2.1.183, supported by experimental evidence (ECO:0000269|PubMed:26776054, Gorina et al. 2016). Two catalytic reactions are documented: (13S)-hydroperoxy-(9Z,11E)-octadecadienoate → etheroleate + H2O and (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate → etherolenate + H2O, both assigned EC 4.2.1.183. The evidence code ECO:0000269 indicates direct experimental evidence from the cited publication.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The protein sequence exhibits hallmarks of a cytochrome P450 (length ~475 aa, conserved P450 motifs including a heme-binding region with FxxGxRxCxG-like pattern, overall composition). Recognizing the P450 fold eliminates EC 3.6.1.5 (hydrolase, option D) and EC 5.3.1.16 (isomerase, option B) since P450s are not hydrolases or isomerases. CYP74-family P450s acting on fatty acid hydroperoxides are classified as hydro-lyases (EC 4.2.1.x), which is consistent with both options A and C. However, distinguishing 4.2.1.70 from 4.2.1.183 requires knowing the specific reaction catalyzed and the EC assignment for this particular CYP74M subfamily.",
    "missing_item_specific_fact": "The specific identity of EC 4.2.1.70 (whether it is a P450 enzyme or an unrelated hydro-lyase) and the knowledge that EC 4.2.1.183 was specifically assigned to CYP74M divinyl ether synthases in 2016 (PubMed:26776054). Without knowing what reaction EC 4.2.1.70 catalyzes and whether it involves a P450 scaffold, a model cannot definitively eliminate option A through sequence reasoning alone.",
    "reason": "While P450 recognition provides a strong reasoning path to eliminate options B and D, the final distinction between A (4.2.1.70) and C (4.2.1.183) depends on knowing the specific EC number assignments within the CYP74 subfamily and what enzyme 4.2.1.70 represents. EC 4.2.1.183 is a recently assigned number (2016) specific to divinyl ether synthase activity of CYP74M enzymes. This is an item-specific annotation fact not derivable from general sequence features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "If 4.2.1.70 is confirmed to be a non-P450 hydro-lyase (which is likely given the diversity of enzymes in the 4.2.1.x class), then P450 recognition would eliminate A as well, leaving C as the only defensible answer. However, without confirming the identity of 4.2.1.70, a model might hesitate between A and C. The evidence strongly supports C as correct."
  },
  "important_caveats": [
    "The EC number 4.2.1.183 was assigned in 2016 (PubMed:26776054) and is relatively recent; models trained on older data may not have encountered it.",
    "The P450 heme-binding motif in this CYP74 sequence appears in a somewhat degenerate form (FGRARQ region), which may make P450 recognition less straightforward than in canonical P450s.",
    "The identity of EC 4.2.1.70 was not independently verified in the reviewer evidence; if it happens to also be a P450 enzyme, the A vs C distinction becomes more challenging.",
    "The UniProt entry was first publicly released in June 2025, meaning the annotation may not have been available in training data used to construct this benchmark."
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

**Accession:** `D8S724` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 64. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:52.483973+00:00.  

```json
"D8S724"
```

Source SHA-256: `ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:52.483973+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"value":"4.2.1.183"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"26776054","source":"PubMed"}],"value":"Etheroleic acid synthase CYP74M1"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26776054","source":"PubMed"}],"value":"Divinyl ether synthase CYP74M1"}}}
```

Source SHA-256: `ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:52.483973+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"26776054","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79276"}}],"reaction":{"ecNumber":"4.2.1.183","evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"name":"(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79275"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:57466"},{"database":"ChEBI","id":"CHEBI:229759"}]}}
```

Source SHA-256: `ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:52.483973+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"26776054","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79272"}}],"reaction":{"ecNumber":"4.2.1.183","evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"name":"(13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79271"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:58757"},{"database":"ChEBI","id":"CHEBI:229758"}]}}
```

Source SHA-256: `ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:52.483973+00:00.  

```json
{"citation":{"authors":["Gorina S.S.","Toporkova Y.Y.","Mukhtarova L.S.","Smirnova E.O.","Chechetkin I.R.","Khairutdinov B.I.","Gogolev Y.V.","Grechkin A.N."],"citationCrossReferences":[{"database":"PubMed","id":"26776054"},{"database":"DOI","id":"10.1016/j.bbalip.2016.01.001"}],"citationType":"journal article","firstPage":"301","id":"26776054","journal":"Biochim. Biophys. Acta","lastPage":"309","publicationDate":"2016","title":"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular cloning and identification of divinyl ether synthases CYP74M1 and CYP74M3.","volume":"1861"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:54.936001+00:00.  

```text
ID   C74M1_SELML             Reviewed;         475 AA.
AC   D8S724;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-OCT-2010, sequence version 1.
DT   28-JAN-2026, entry version 64.
DE   RecName: Full=Divinyl ether synthase CYP74M1 {ECO:0000303|PubMed:26776054};
DE   AltName: Full=Etheroleic acid synthase CYP74M1 {ECO:0000305|PubMed:26776054};
DE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};
GN   Name=CYP74M1 {ECO:0000303|PubMed:26776054};
GN   Synonyms=DES1 {ECO:0000303|PubMed:26776054};
GN   ORFNames=SELMODRAFT_177485 {ECO:0000312|EMBL:EFJ19674.1};
OS   Selaginella moellendorffii (Spikemoss).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Lycopodiopsida; Selaginellales; Selaginellaceae; Selaginella.
OX   NCBI_TaxID=88036;
```

Source SHA-256: `1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:54.936001+00:00.  

```text
DE   RecName: Full=Divinyl ether synthase CYP74M1 {ECO:0000303|PubMed:26776054};
DE   AltName: Full=Etheroleic acid synthase CYP74M1 {ECO:0000305|PubMed:26776054};
DE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};
```

Source SHA-256: `1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)  
**Locator:** `lines 56-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:54.936001+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate +
CC         H2O; Xref=Rhea:RHEA:79275, ChEBI:CHEBI:15377, ChEBI:CHEBI:57466,
CC         ChEBI:CHEBI:229759; EC=4.2.1.183;
CC         Evidence={ECO:0000269|PubMed:26776054};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79276;
CC         Evidence={ECO:0000305|PubMed:26776054};
```

Source SHA-256: `1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)  
**Locator:** `lines 63-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:54.936001+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate =
CC         etherolenate + H2O; Xref=Rhea:RHEA:79271, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:58757, ChEBI:CHEBI:229758; EC=4.2.1.183;
CC         Evidence={ECO:0000269|PubMed:26776054};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79272;
CC         Evidence={ECO:0000305|PubMed:26776054};
```

Source SHA-256: `1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 120. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
