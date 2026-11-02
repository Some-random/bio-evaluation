# catalytic_activity_0162

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — an aliphatic sulfonate + 4 oxidized &#91;4Fe-4S&#93;-&#91;ferredoxin&#93; + 2 H2O = 4 reduced &#91;4Fe-4S&#93;-&#91;ferredoxin&#93; + a carboxylate + sulfite + 6 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MYAYNGKLLDVDLTREKVKEVELSEDVLKKFYGGRGLGTYILWKELGEKWEKVDPLGEENLLLILTGPLTGYYPGMKTSIVSKSPESNGVVGSVLSSELGLELKAAGYDGIIIRGKAKSPVYLFIHNDTVEIRDATKYWGMGGIELYKTLLKEVHEEIRKKEKLKGVPKEPAMIYIGKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPEVYDKEKMKVLLREFWKELFSMTTFREWGTGAGGYSVGHDRSSEPIRNWQEEYHDNEEISVVNFENRTWIKKYWADYGCPVNCMKISYLRYGPYKGSISDAPDYELQAYMGTNLGIFEPEKIVYLSYLVDELGLDGINTGNILGFAAELYQRGILTKEDLGFELNWGDEKAFAKLLHLIVEKEGIGKILAEGTYRAALKISEIKGIDVTKYAVHVKGIAVGAHGIRSELDYTKDISYAVSVQGGDHTSTAALPAKGYTGELVEAFYDSAVICNFVTKPGFEKIIEFGNALSGFNITPEQWLNEIGLRIIHLQRILLLLGGPDVYWDPRKDDDNPPRFYEPLPSGPVKGKAPNREDIKAKVKQYYEEIGYDEHGIPKEEVLEELGIGEAKREVKRIKKRLNL

[Multiple Choices]
A. 2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol
B. N-acetylneuraminate + CTP = CMP-N-acetyl-beta-neuraminate + diphosphate
C. an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6 H(+)
D. AH2 + 2 S-adenosyl-L-methionine = 2 5'-deoxyadenosin-5'-yl radical + 2 L-methionine + A + 2 H(+)
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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the 624-aa UniProt entry annotated as aliphatic sulfonate oxidoreductase. That entry gives choice C as a catalytic activity, with experimental evidence codes citing two publications. This supports the key for this sequence, while not independently validating the primary experiments.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe unrelated reaction types, but the sequence alone provides no clear, general biological argument that identifies this particular enzyme's aliphatic-sulfonate oxidoreductase activity.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental knowledge that this sequence corresponds to an aliphatic sulfonate oxidoreductase catalyzing the reaction in C.


**Reason**

> Choosing C requires connecting the sequence to its specific enzyme function, a fact not supplied in the prompt. Recognizing the sequence or using a predictor would not make that fact available through general reasoning from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, C is the one supported for the matched protein. The entry reports other catalytic activities as well, but none corresponds to A, B, or D.


### Important caveats

- The reviewer-only sequence match and annotations were not supplied to the evaluated model.
- The cited experimental evidence supports the database annotation; the primary studies were not independently reviewed here.
- The actual author data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe unrelated reaction types, but the sequence alone provides no clear, general biological argument that identifies this particular enzyme's aliphatic-sulfonate oxidoreductase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental knowledge that this sequence corresponds to an aliphatic sulfonate oxidoreductase catalyzing the reaction in C.",
    "reason": "Choosing C requires connecting the sequence to its specific enzyme function, a fact not supplied in the prompt. Recognizing the sequence or using a predictor would not make that fact available through general reasoning from the input."
  },
  "case_id": "catalytic_activity_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 624-aa UniProt entry annotated as aliphatic sulfonate oxidoreductase. That entry gives choice C as a catalytic activity, with experimental evidence codes citing two publications. This supports the key for this sequence, while not independently validating the primary experiments."
  },
  "important_caveats": [
    "The reviewer-only sequence match and annotations were not supplied to the evaluated model.",
    "The cited experimental evidence supports the database annotation; the primary studies were not independently reviewed here.",
    "The actual author data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, C is the one supported for the matched protein. The entry reports other catalytic activities as well, but none corresponds to A, B, or D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 624-aa UniProt entry annotated as aliphatic sulfonate oxidoreductase. That entry gives choice C as a catalytic activity, with experimental evidence codes citing two publications. This supports the key for this sequence, while not independently validating the primary experiments.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe unrelated reaction types, but the sequence alone provides no clear, general biological argument that identifies this particular enzyme's aliphatic-sulfonate oxidoreductase activity.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental knowledge that this sequence corresponds to an aliphatic sulfonate oxidoreductase catalyzing the reaction in C.",
    "reason": "Choosing C requires connecting the sequence to its specific enzyme function, a fact not supplied in the prompt. Recognizing the sequence or using a predictor would not make that fact available through general reasoning from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, C is the one supported for the matched protein. The entry reports other catalytic activities as well, but none corresponds to A, B, or D."
  },
  "important_caveats": [
    "The reviewer-only sequence match and annotations were not supplied to the evaluated model.",
    "The cited experimental evidence supports the database annotation; the primary studies were not independently reviewed here.",
    "The actual author data-source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt E7FHH1 (ASOR_PYRFU) exactly. The primary EC 1.97.1.13 catalytic activity annotation reads verbatim: 'an aliphatic sulfonate + 4 oxidized &#91;4Fe-4S&#93;-&#91;ferredoxin&#93; + 2 H2O = 4 reduced &#91;4Fe-4S&#93;-&#91;ferredoxin&#93; + a carboxylate + sulfite + 6 H(+)', backed by ECO:0000269 (direct assay) from PubMed:16199576 and PubMed:36269456. Choice C reproduces this reaction exactly.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the GFGGYSV motif (~residues 250-256), a hallmark of the tungsten-bispterin (W-bisPGP) binding domain in the DMSO-reductase/tungstoenzyme family, along with multiple cysteine-rich stretches consistent with &#91;4Fe-4S&#93; cluster coordination. It lacks the CX3CX2C radical-SAM motif (ruling out D), the HKD phospholipase-D triad (ruling out A), and nucleotidyltransferase motifs (ruling out B). Among the four choices, only C describes a tungsten-containing oxidoreductase using &#91;4Fe-4S&#93; ferredoxin as electron acceptor, matching the identified enzyme family.


**Missing item-specific fact**

> None strictly required; however, confidently recognizing the GFGGYSV tungsten-bispterin motif and distinguishing it from molybdenum analogues requires specialized knowledge of tungstoenzyme sequence signatures.


**Reason**

> A knowledgeable reader can identify the tungsten-bispterin oxidoreductase family from the GFGGYSV motif and Fe-S cluster cysteine patterns, then eliminate the other three choices (radical SAM, phospholipase D, nucleotidyltransferase) by absence of their diagnostic motifs. Only C is consistent with a tungsten oxidoreductase coupled to &#91;4Fe-4S&#93; ferredoxin.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only C involves a tungsten-containing oxidoreductase with &#91;4Fe-4S&#93; ferredoxin. The other three (cardiolipin synthase, nucleotidyltransferase, radical SAM) are mechanistically and structurally incompatible with the sequence features. Although UniProt also lists a 2-electron aldehyde-producing variant and taurine-specific reactions, none of those appear as alternative choices, so no ambiguity exists among the given options.


### Important caveats

- The enzyme was originally characterized in 2005 as a tungsten-containing aldehyde oxidoreductase (WOR5); the aliphatic sulfonate oxidoreductase function was established in 2022 (PubMed:36269456). The EC 1.97.1.13 assignment and the 4-electron sulfonate-to-carboxylate reaction are the current primary annotation.
- The GFGGYSV motif recognition, while a genuine sequence feature, requires specialized tungstoenzyme knowledge; a model without this knowledge would struggle to distinguish C from D or A purely by sequence.
- Reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning path described relies on general (if specialized) enzymology knowledge applied to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the GFGGYSV motif (~residues 250-256), a hallmark of the tungsten-bispterin (W-bisPGP) binding domain in the DMSO-reductase/tungstoenzyme family, along with multiple cysteine-rich stretches consistent with [4Fe-4S] cluster coordination. It lacks the CX3CX2C radical-SAM motif (ruling out D), the HKD phospholipase-D triad (ruling out A), and nucleotidyltransferase motifs (ruling out B). Among the four choices, only C describes a tungsten-containing oxidoreductase using [4Fe-4S] ferredoxin as electron acceptor, matching the identified enzyme family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, confidently recognizing the GFGGYSV tungsten-bispterin motif and distinguishing it from molybdenum analogues requires specialized knowledge of tungstoenzyme sequence signatures.",
    "reason": "A knowledgeable reader can identify the tungsten-bispterin oxidoreductase family from the GFGGYSV motif and Fe-S cluster cysteine patterns, then eliminate the other three choices (radical SAM, phospholipase D, nucleotidyltransferase) by absence of their diagnostic motifs. Only C is consistent with a tungsten oxidoreductase coupled to [4Fe-4S] ferredoxin."
  },
  "case_id": "catalytic_activity_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt E7FHH1 (ASOR_PYRFU) exactly. The primary EC 1.97.1.13 catalytic activity annotation reads verbatim: 'an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6 H(+)', backed by ECO:0000269 (direct assay) from PubMed:16199576 and PubMed:36269456. Choice C reproduces this reaction exactly."
  },
  "important_caveats": [
    "The enzyme was originally characterized in 2005 as a tungsten-containing aldehyde oxidoreductase (WOR5); the aliphatic sulfonate oxidoreductase function was established in 2022 (PubMed:36269456). The EC 1.97.1.13 assignment and the 4-electron sulfonate-to-carboxylate reaction are the current primary annotation.",
    "The GFGGYSV motif recognition, while a genuine sequence feature, requires specialized tungstoenzyme knowledge; a model without this knowledge would struggle to distinguish C from D or A purely by sequence.",
    "Reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning path described relies on general (if specialized) enzymology knowledge applied to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only C involves a tungsten-containing oxidoreductase with [4Fe-4S] ferredoxin. The other three (cardiolipin synthase, nucleotidyltransferase, radical SAM) are mechanistically and structurally incompatible with the sequence features. Although UniProt also lists a 2-electron aldehyde-producing variant and taurine-specific reactions, none of those appear as alternative choices, so no ambiguity exists among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt E7FHH1 (ASOR_PYRFU) exactly. The primary EC 1.97.1.13 catalytic activity annotation reads verbatim: 'an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6 H(+)', backed by ECO:0000269 (direct assay) from PubMed:16199576 and PubMed:36269456. Choice C reproduces this reaction exactly.",
    "evidence_ids": ["C5", "H5", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the GFGGYSV motif (~residues 250-256), a hallmark of the tungsten-bispterin (W-bisPGP) binding domain in the DMSO-reductase/tungstoenzyme family, along with multiple cysteine-rich stretches consistent with [4Fe-4S] cluster coordination. It lacks the CX3CX2C radical-SAM motif (ruling out D), the HKD phospholipase-D triad (ruling out A), and nucleotidyltransferase motifs (ruling out B). Among the four choices, only C describes a tungsten-containing oxidoreductase using [4Fe-4S] ferredoxin as electron acceptor, matching the identified enzyme family.",
    "missing_item_specific_fact": "None strictly required; however, confidently recognizing the GFGGYSV tungsten-bispterin motif and distinguishing it from molybdenum analogues requires specialized knowledge of tungstoenzyme sequence signatures.",
    "reason": "A knowledgeable reader can identify the tungsten-bispterin oxidoreductase family from the GFGGYSV motif and Fe-S cluster cysteine patterns, then eliminate the other three choices (radical SAM, phospholipase D, nucleotidyltransferase) by absence of their diagnostic motifs. Only C is consistent with a tungsten oxidoreductase coupled to [4Fe-4S] ferredoxin."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only C involves a tungsten-containing oxidoreductase with [4Fe-4S] ferredoxin. The other three (cardiolipin synthase, nucleotidyltransferase, radical SAM) are mechanistically and structurally incompatible with the sequence features. Although UniProt also lists a 2-electron aldehyde-producing variant and taurine-specific reactions, none of those appear as alternative choices, so no ambiguity exists among the given options."
  },
  "important_caveats": [
    "The enzyme was originally characterized in 2005 as a tungsten-containing aldehyde oxidoreductase (WOR5); the aliphatic sulfonate oxidoreductase function was established in 2022 (PubMed:36269456). The EC 1.97.1.13 assignment and the 4-electron sulfonate-to-carboxylate reaction are the current primary annotation.",
    "The GFGGYSV motif recognition, while a genuine sequence feature, requires specialized tungstoenzyme knowledge; a model without this knowledge would struggle to distinguish C from D or A purely by sequence.",
    "Reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning path described relies on general (if specialized) enzymology knowledge applied to the supplied sequence."
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

**Accession:** `E7FHH1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 59. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
"E7FHH1"
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"Aliphatic sulfonate ferredoxin oxidoreductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"ASOR"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16199576","source":"PubMed"}],"value":"Tungsten-containing aldehyde oxidoreductase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16199576","source":"PubMed"}],"value":"WOR5"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"WOR5 large subunit"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"WOR5-L"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"value":"1.97.1.13"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aliphatic sulfonate oxidoreductase, WOR-like subunit"}}}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.97.1.13","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"name":"an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80643"},{"database":"Rhea","id":"RHEA-COMP:18797"},{"database":"Rhea","id":"RHEA-COMP:18798"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17359"},{"database":"ChEBI","id":"CHEBI:29067"},{"database":"ChEBI","id":"CHEBI:33722"},{"database":"ChEBI","id":"CHEBI:33723"},{"database":"ChEBI","id":"CHEBI:231625"}]}}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 6-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
DE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};
DE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};
DE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};
DE            Short=ASOR {ECO:0000303|PubMed:36269456};
DE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};
DE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};
DE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};
DE            Short=WOR5-L {ECO:0000303|PubMed:36269456};
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 69-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2
CC         H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6
CC         H(+); Xref=Rhea:RHEA:80643, Rhea:RHEA-COMP:18797, Rhea:RHEA-
CC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,
CC         ChEBI:CHEBI:29067, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723,
CC         ChEBI:CHEBI:231625; EC=1.97.1.13;
CC         Evidence={ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 162. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
