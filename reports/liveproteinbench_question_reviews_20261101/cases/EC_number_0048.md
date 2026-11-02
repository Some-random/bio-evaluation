# EC_number_0048

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.5.1.38

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSYGESHGKAIGCVIDGFLSNIEINFDLIQKQLDRRRPNQSKLTSNRNEKDKLVILSGFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQVSKELENKNPPSRDLVDSYGTVRYNEKEKIFMDCFNRIYDMNASMLKTDEYNKNTLTIPSIDNTYINVKTNECNINQVDNNHNNYINDKDNTFNNSEKSDEWIYLQTRCPHPYTAVQICSYILKLKNKGDSVGGIATCIIQNPPIGIGEPIFDKLEAELAKMILSIPAVKGIEFGSGFNGTYMFGSMHNDIFIPVENMSTKKESDLLYDDKGECKNMSYHSTIQNNEDQILNSTKGFMPPKNDKNFNNIDDYNVTFNNNEEKLLITKTNNCGGILAGISTGNNIVFRSAIKPVSSIQIEKETSDFYGNMCNLKVQGRHDSCILPRLPPIIEASSSMVIGDLILRQISKYGDKKLPTLFRNM

[Multiple Choices]
A. 1.5.1.32
B. 1.5.1.38
C. 5.6.2.4
D. 3.2.2.5
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

> The exact sequence matches the Plasmodium falciparum UniProt entry, which annotates EC 1.5.1.38 and cites experimental evidence for that activity. The historical entry available by the stated cutoff also includes this annotation. The evidence supports B, though it does not establish that this is the protein’s only EC activity.

Citations as saved: [C1](#evidence-c1), [C6](#evidence-c6), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a defensible way to distinguish the specific FMN-reductase activity represented by 1.5.1.38 from the other precise EC choices.


**Missing item-specific fact**

> The protein-specific experimentally characterized reaction—FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)—or an equivalent annotation is needed to justify EC 1.5.1.38.


**Reason**

> Inferring a broad enzyme family from sequence would not establish this specific catalytic activity or its complete EC number; doing so depends on an item-specific annotation or experimental fact absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the evidence supports B. However, the protein is also annotated with EC 4.2.3.5, which is not offered, so the single-answer format does not capture all annotated catalytic activities.


### Important caveats

- The UniProt record is for Plasmodium falciparum isolate 3D7, and the supplied sequence matches its sequence.
- The cited UniProt evidence for EC 1.5.1.38 is experimental evidence, but the primary paper was not independently reviewed here.
- The author’s exact source snapshot is unknown; a historical matched entry available by the stated cutoff also supports the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a defensible way to distinguish the specific FMN-reductase activity represented by 1.5.1.38 from the other precise EC choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimentally characterized reaction—FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)—or an equivalent annotation is needed to justify EC 1.5.1.38.",
    "reason": "Inferring a broad enzyme family from sequence would not establish this specific catalytic activity or its complete EC number; doing so depends on an item-specific annotation or experimental fact absent from the question."
  },
  "case_id": "EC_number_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C6",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium falciparum UniProt entry, which annotates EC 1.5.1.38 and cites experimental evidence for that activity. The historical entry available by the stated cutoff also includes this annotation. The evidence supports B, though it does not establish that this is the protein’s only EC activity."
  },
  "important_caveats": [
    "The UniProt record is for Plasmodium falciparum isolate 3D7, and the supplied sequence matches its sequence.",
    "The cited UniProt evidence for EC 1.5.1.38 is experimental evidence, but the primary paper was not independently reviewed here.",
    "The author’s exact source snapshot is unknown; a historical matched entry available by the stated cutoff also supports the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the evidence supports B. However, the protein is also annotated with EC 4.2.3.5, which is not offered, so the single-answer format does not capture all annotated catalytic activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium falciparum UniProt entry, which annotates EC 1.5.1.38 and cites experimental evidence for that activity. The historical entry available by the stated cutoff also includes this annotation. The evidence supports B, though it does not establish that this is the protein’s only EC activity.",
    "evidence_ids": ["C1", "C6", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a defensible way to distinguish the specific FMN-reductase activity represented by 1.5.1.38 from the other precise EC choices.",
    "missing_item_specific_fact": "The protein-specific experimentally characterized reaction—FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)—or an equivalent annotation is needed to justify EC 1.5.1.38.",
    "reason": "Inferring a broad enzyme family from sequence would not establish this specific catalytic activity or its complete EC number; doing so depends on an item-specific annotation or experimental fact absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the evidence supports B. However, the protein is also annotated with EC 4.2.3.5, which is not offered, so the single-answer format does not capture all annotated catalytic activities."
  },
  "important_caveats": [
    "The UniProt record is for Plasmodium falciparum isolate 3D7, and the supplied sequence matches its sequence.",
    "The cited UniProt evidence for EC 1.5.1.38 is experimental evidence, but the primary paper was not independently reviewed here.",
    "The author’s exact source snapshot is unknown; a historical matched entry available by the stated cutoff also supports the key."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry C6KT66 (AROC_PLAF7, chorismate synthase from P. falciparum) is annotated with EC 1.5.1.38 (FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)) with direct experimental evidence (ECO:0000269, PubMed:31381947, Khera et al. 2019 'Chorismate synthase from malaria parasites is bifunctional enzyme'). The sequence matches exactly (SHA256 confirmed). Among the four options, only 1.5.1.38 is annotated for this protein; 4.2.3.5 (the primary chorismate synthase activity) is absent from the choices, making B the only supported answer.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model recognizing the sequence as chorismate synthase (a well-known shikimate-pathway enzyme) would predict EC 4.2.3.5 as the primary activity, which is NOT among the options. Identifying the secondary FMN reductase activity (EC 1.5.1.38) requires knowing the specific 2019 experimental finding that P. falciparum chorismate synthase is bifunctional. While chorismate synthase uses FMN as a cofactor, this does not logically imply it catalyzes FMNH2 + NADP(+) → FMN + NADPH; that is a distinct oxidoreductase reaction demonstrated experimentally for this particular protein.


**Missing item-specific fact**

> The specific experimental demonstration (PubMed:31381947, 2019) that P. falciparum chorismate synthase possesses a secondary FMN reductase (NADPH) activity corresponding to EC 1.5.1.38. This bifunctional property is not inferable from sequence motifs, general chorismate synthase biochemistry, or standard EC classification logic.


**Reason**

> The sequence provides no distinguishing motif that would lead a model to select EC 1.5.1.38 over the other three options through general biological reasoning. The bifunctional nature is an item-specific experimental fact about this particular protein, discovered only in 2019. A model must either memorize this annotation or recognize the exact sequence and recall its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is bifunctional with primary EC 4.2.3.5 and secondary EC 1.5.1.38, only 1.5.1.38 appears among the options. The other three (1.5.1.32, 5.6.2.4, 3.2.2.5) are unrelated enzyme classes with no annotation connection to this protein. Thus B is the uniquely defensible choice despite the question's singular phrasing ('the EC number') for a bifunctional enzyme.


### Important caveats

- The protein's primary and namesake EC number is 4.2.3.5 (chorismate synthase), confirmed by direct assay (ECO:0000269). The question's omission of this from the options effectively forces selection of the secondary activity.
- EC 1.5.1.38 annotation carries evidence code ECO:0000269 (direct assay) from a single publication (PubMed:31381947, 2019), making it relatively recent and specific.
- The bifunctional characterization is specific to Plasmodium falciparum chorismate synthase and is not a general property of chorismate synthases across organisms.
- The question asks for 'the complete 4-digit EC number' (singular) for a protein with two experimentally supported EC numbers, creating a minor framing inconsistency.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model recognizing the sequence as chorismate synthase (a well-known shikimate-pathway enzyme) would predict EC 4.2.3.5 as the primary activity, which is NOT among the options. Identifying the secondary FMN reductase activity (EC 1.5.1.38) requires knowing the specific 2019 experimental finding that P. falciparum chorismate synthase is bifunctional. While chorismate synthase uses FMN as a cofactor, this does not logically imply it catalyzes FMNH2 + NADP(+) → FMN + NADPH; that is a distinct oxidoreductase reaction demonstrated experimentally for this particular protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental demonstration (PubMed:31381947, 2019) that P. falciparum chorismate synthase possesses a secondary FMN reductase (NADPH) activity corresponding to EC 1.5.1.38. This bifunctional property is not inferable from sequence motifs, general chorismate synthase biochemistry, or standard EC classification logic.",
    "reason": "The sequence provides no distinguishing motif that would lead a model to select EC 1.5.1.38 over the other three options through general biological reasoning. The bifunctional nature is an item-specific experimental fact about this particular protein, discovered only in 2019. A model must either memorize this annotation or recognize the exact sequence and recall its database entry."
  },
  "case_id": "EC_number_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "C8",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry C6KT66 (AROC_PLAF7, chorismate synthase from P. falciparum) is annotated with EC 1.5.1.38 (FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)) with direct experimental evidence (ECO:0000269, PubMed:31381947, Khera et al. 2019 'Chorismate synthase from malaria parasites is bifunctional enzyme'). The sequence matches exactly (SHA256 confirmed). Among the four options, only 1.5.1.38 is annotated for this protein; 4.2.3.5 (the primary chorismate synthase activity) is absent from the choices, making B the only supported answer."
  },
  "important_caveats": [
    "The protein's primary and namesake EC number is 4.2.3.5 (chorismate synthase), confirmed by direct assay (ECO:0000269). The question's omission of this from the options effectively forces selection of the secondary activity.",
    "EC 1.5.1.38 annotation carries evidence code ECO:0000269 (direct assay) from a single publication (PubMed:31381947, 2019), making it relatively recent and specific.",
    "The bifunctional characterization is specific to Plasmodium falciparum chorismate synthase and is not a general property of chorismate synthases across organisms.",
    "The question asks for 'the complete 4-digit EC number' (singular) for a protein with two experimentally supported EC numbers, creating a minor framing inconsistency."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional with primary EC 4.2.3.5 and secondary EC 1.5.1.38, only 1.5.1.38 appears among the options. The other three (1.5.1.32, 5.6.2.4, 3.2.2.5) are unrelated enzyme classes with no annotation connection to this protein. Thus B is the uniquely defensible choice despite the question's singular phrasing ('the EC number') for a bifunctional enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry C6KT66 (AROC_PLAF7, chorismate synthase from P. falciparum) is annotated with EC 1.5.1.38 (FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)) with direct experimental evidence (ECO:0000269, PubMed:31381947, Khera et al. 2019 'Chorismate synthase from malaria parasites is bifunctional enzyme'). The sequence matches exactly (SHA256 confirmed). Among the four options, only 1.5.1.38 is annotated for this protein; 4.2.3.5 (the primary chorismate synthase activity) is absent from the choices, making B the only supported answer.",
    "evidence_ids": ["C4", "C6", "C8", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model recognizing the sequence as chorismate synthase (a well-known shikimate-pathway enzyme) would predict EC 4.2.3.5 as the primary activity, which is NOT among the options. Identifying the secondary FMN reductase activity (EC 1.5.1.38) requires knowing the specific 2019 experimental finding that P. falciparum chorismate synthase is bifunctional. While chorismate synthase uses FMN as a cofactor, this does not logically imply it catalyzes FMNH2 + NADP(+) → FMN + NADPH; that is a distinct oxidoreductase reaction demonstrated experimentally for this particular protein.",
    "missing_item_specific_fact": "The specific experimental demonstration (PubMed:31381947, 2019) that P. falciparum chorismate synthase possesses a secondary FMN reductase (NADPH) activity corresponding to EC 1.5.1.38. This bifunctional property is not inferable from sequence motifs, general chorismate synthase biochemistry, or standard EC classification logic.",
    "reason": "The sequence provides no distinguishing motif that would lead a model to select EC 1.5.1.38 over the other three options through general biological reasoning. The bifunctional nature is an item-specific experimental fact about this particular protein, discovered only in 2019. A model must either memorize this annotation or recognize the exact sequence and recall its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional with primary EC 4.2.3.5 and secondary EC 1.5.1.38, only 1.5.1.38 appears among the options. The other three (1.5.1.32, 5.6.2.4, 3.2.2.5) are unrelated enzyme classes with no annotation connection to this protein. Thus B is the uniquely defensible choice despite the question's singular phrasing ('the EC number') for a bifunctional enzyme."
  },
  "important_caveats": [
    "The protein's primary and namesake EC number is 4.2.3.5 (chorismate synthase), confirmed by direct assay (ECO:0000269). The question's omission of this from the options effectively forces selection of the secondary activity.",
    "EC 1.5.1.38 annotation carries evidence code ECO:0000269 (direct assay) from a single publication (PubMed:31381947, 2019), making it relatively recent and specific.",
    "The bifunctional characterization is specific to Plasmodium falciparum chorismate synthase and is not a general property of chorismate synthases across organisms.",
    "The question asks for 'the complete 4-digit EC number' (singular) for a protein with two experimentally supported EC numbers, creating a minor framing inconsistency."
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

**Accession:** `C6KT66` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 89. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
"C6KT66"
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"31381947","source":"PubMed"}],"value":"1.5.1.38"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"value":"4.2.3.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"31381947","source":"PubMed"}],"value":"Chorismate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"}],"value":"PfCS"}]}}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:21626"}}],"reaction":{"ecNumber":"1.5.1.38","evidences":[{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"name":"FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:21624"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"citation":{"authors":["Khera H.K.","Singh S.K.","Singh S."],"citationCrossReferences":[{"database":"PubMed","id":"31381947"},{"database":"DOI","id":"10.1016/j.molbiopara.2019.111202"}],"citationType":"journal article","firstPage":"111202","id":"31381947","journal":"Mol. Biochem. Parasitol.","lastPage":"111202","publicationDate":"2019","title":"Chorismate synthase from malaria parasites is bifunctional enzyme.","volume":"233"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
DE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};
DE            Short=PfCS {ECO:0000303|PubMed:11298276};
DE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};
DE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 79-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=FMNH2 + NADP(+) = FMN + NADPH + 2 H(+); Xref=Rhea:RHEA:21624,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57618, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58210, ChEBI:CHEBI:58349; EC=1.5.1.38;
CC         Evidence={ECO:0000269|PubMed:31381947};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:21626;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
