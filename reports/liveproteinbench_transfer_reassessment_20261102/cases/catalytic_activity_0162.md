# catalytic_activity_0162: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0162.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **C** — an aliphatic sulfonate + 4 oxidized &#91;4Fe-4S&#93;-&#91;ferredoxin&#93; + 2 H2O = 4 reduced &#91;4Fe-4S&#93;-&#91;ferredoxin&#93; + a carboxylate + sulfite + 6 H(+)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

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
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence has a UniProt catalytic-activity annotation for exactly the reaction in option C, with experimental evidence codes citing two publications. The record also lists other catalytic activities, but none of those are among the other offered options.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence is consistent with a large tungsten-containing oxidoreductase of the WOR-like family, rather than the lipid enzyme in A, the CMP-sialic-acid synthetase in B, or the radical-SAM enzyme in D. Transferable knowledge that tungsten/iron-sulfur oxidoreductases catalyze redox transformations meaningfully favors C among these choices, which describes an iron-sulfur-ferredoxin-coupled oxidation.


**Missing item-specific fact**

> The precise substrate range and exact aliphatic-sulfonate reaction are not established by that family-level inference alone.


**Reason**

> The alternatives differ substantially in enzyme class and reaction chemistry, so family-level recognition can distinguish C without recalling this exact protein's annotation. It does not independently establish every detail of C; the exact substrate specificity remains a limitation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the source record describes additional activities, no other offered option matches those activities.


### Important caveats

- The reviewer-only source evidence was not part of the original input and supports the key, not the transferability judgment.
- The sequence and family-level cues support a probabilistic choice; they do not by themselves prove the exact sulfonate substrate reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with a large tungsten-containing oxidoreductase of the WOR-like family, rather than the lipid enzyme in A, the CMP-sialic-acid synthetase in B, or the radical-SAM enzyme in D. Transferable knowledge that tungsten/iron-sulfur oxidoreductases catalyze redox transformations meaningfully favors C among these choices, which describes an iron-sulfur-ferredoxin-coupled oxidation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise substrate range and exact aliphatic-sulfonate reaction are not established by that family-level inference alone.",
    "reason": "The alternatives differ substantially in enzyme class and reaction chemistry, so family-level recognition can distinguish C without recalling this exact protein's annotation. It does not independently establish every detail of C; the exact substrate specificity remains a limitation."
  },
  "case_id": "catalytic_activity_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt catalytic-activity annotation for exactly the reaction in option C, with experimental evidence codes citing two publications. The record also lists other catalytic activities, but none of those are among the other offered options."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not part of the original input and supports the key, not the transferability judgment.",
    "The sequence and family-level cues support a probabilistic choice; they do not by themselves prove the exact sulfonate substrate reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the source record describes additional activities, no other offered option matches those activities."
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
    "reason": "The matched sequence has a UniProt catalytic-activity annotation for exactly the reaction in option C, with experimental evidence codes citing two publications. The record also lists other catalytic activities, but none of those are among the other offered options.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence is consistent with a large tungsten-containing oxidoreductase of the WOR-like family, rather than the lipid enzyme in A, the CMP-sialic-acid synthetase in B, or the radical-SAM enzyme in D. Transferable knowledge that tungsten/iron-sulfur oxidoreductases catalyze redox transformations meaningfully favors C among these choices, which describes an iron-sulfur-ferredoxin-coupled oxidation.",
    "missing_item_specific_fact": "The precise substrate range and exact aliphatic-sulfonate reaction are not established by that family-level inference alone.",
    "reason": "The alternatives differ substantially in enzyme class and reaction chemistry, so family-level recognition can distinguish C without recalling this exact protein's annotation. It does not independently establish every detail of C; the exact substrate specificity remains a limitation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the source record describes additional activities, no other offered option matches those activities."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not part of the original input and supports the key, not the transferability judgment.",
    "The sequence and family-level cues support a probabilistic choice; they do not by themselves prove the exact sulfonate substrate reaction."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E7FHH1 annotates this protein with EC 1.97.1.13 and the exact catalytic reaction in option C, supported by direct experimental evidence (ECO:0000269) from two publications (PubMed:16199576 and PubMed:36269456). The reaction text matches option C verbatim.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of the aldehyde/tungsten-containing aldehyde oxidoreductase (AOR/WOR) family within the DMSO reductase superfamily: (1) the 'HND' motif (~residue 130: 'IHNDTVEIRD') diagnostic of the AOR/WOR family active site; (2) the 'GAGGYS' tungsten-cofactor-binding motif (~residue 280: 'TGAGGYSVGHDRSSEPIRNW'); (3) multiple 'GKG' motifs (e.g., 'IYIGKGGEN', 'AAGYGGYGAVMGSKNLKAVIAKGSGP') indicating 4Fe-4S cluster coordination. These features unambiguously identify a tungsten-containing oxidoreductase with 4Fe-4S ferredoxin as electron acceptor. Among the four options, only C involves a tungsten/molybdenum oxidoreductase coupled to 4Fe-4S ferredoxin. Option A (cardiolipin synthase) is a phospholipase with no resemblance. Option B (CMP-sialic acid synthetase) is a nucleotidyltransferase with no resemblance. Option D (radical SAM enzyme) requires a CX3CX2C motif absent from this sequence. Thus family-level sequence features (HND + GAGGYS + GKG) distinguish C from all other choices without needing to know the specific sulfonate substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The tungsten cofactor motif (GAGGYS), the HND active-site motif, and 4Fe-4S cluster-binding GKG motifs are well-known family signatures transferable from other AOR/WOR/DMSO-reductase-family proteins. These features uniquely match option C's description of a tungsten oxidoreductase with 4Fe-4S ferredoxin, while excluding A (phospholipase), B (nucleotidyltransferase), and D (radical SAM, no CX3CX2C motif). The specific sulfonate substrate need not be predicted from sequence; the enzyme class alone discriminates the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option C is consistent with the tungsten-containing oxidoreductase family features present in the sequence. The other three options represent entirely different enzyme classes with no sequence-level support.


### Important caveats

- The specific sulfonate substrate (as opposed to aldehyde) was discovered in 2022 (PubMed:36269456); the 2005 paper described it as a tungsten-containing aldehyde oxidoreductase. However, the enzyme class (W-oxidoreductase + 4Fe-4S ferredoxin) is sufficient to select C among the given options.
- The UniProt annotation carries ECO:0000269 (direct assay evidence), indicating experimental rather than purely computational assignment.
- The sequence matches the current UniProt entry E7FHH1 (Pyrococcus furiosus WOR5 large subunit) exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the aldehyde/tungsten-containing aldehyde oxidoreductase (AOR/WOR) family within the DMSO reductase superfamily: (1) the 'HND' motif (~residue 130: 'IHNDTVEIRD') diagnostic of the AOR/WOR family active site; (2) the 'GAGGYS' tungsten-cofactor-binding motif (~residue 280: 'TGAGGYSVGHDRSSEPIRNW'); (3) multiple 'GKG' motifs (e.g., 'IYIGKGGEN', 'AAGYGGYGAVMGSKNLKAVIAKGSGP') indicating 4Fe-4S cluster coordination. These features unambiguously identify a tungsten-containing oxidoreductase with 4Fe-4S ferredoxin as electron acceptor. Among the four options, only C involves a tungsten/molybdenum oxidoreductase coupled to 4Fe-4S ferredoxin. Option A (cardiolipin synthase) is a phospholipase with no resemblance. Option B (CMP-sialic acid synthetase) is a nucleotidyltransferase with no resemblance. Option D (radical SAM enzyme) requires a CX3CX2C motif absent from this sequence. Thus family-level sequence features (HND + GAGGYS + GKG) distinguish C from all other choices without needing to know the specific sulfonate substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The tungsten cofactor motif (GAGGYS), the HND active-site motif, and 4Fe-4S cluster-binding GKG motifs are well-known family signatures transferable from other AOR/WOR/DMSO-reductase-family proteins. These features uniquely match option C's description of a tungsten oxidoreductase with 4Fe-4S ferredoxin, while excluding A (phospholipase), B (nucleotidyltransferase), and D (radical SAM, no CX3CX2C motif). The specific sulfonate substrate need not be predicted from sequence; the enzyme class alone discriminates the answer."
  },
  "case_id": "catalytic_activity_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E7FHH1 annotates this protein with EC 1.97.1.13 and the exact catalytic reaction in option C, supported by direct experimental evidence (ECO:0000269) from two publications (PubMed:16199576 and PubMed:36269456). The reaction text matches option C verbatim."
  },
  "important_caveats": [
    "The specific sulfonate substrate (as opposed to aldehyde) was discovered in 2022 (PubMed:36269456); the 2005 paper described it as a tungsten-containing aldehyde oxidoreductase. However, the enzyme class (W-oxidoreductase + 4Fe-4S ferredoxin) is sufficient to select C among the given options.",
    "The UniProt annotation carries ECO:0000269 (direct assay evidence), indicating experimental rather than purely computational assignment.",
    "The sequence matches the current UniProt entry E7FHH1 (Pyrococcus furiosus WOR5 large subunit) exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C is consistent with the tungsten-containing oxidoreductase family features present in the sequence. The other three options represent entirely different enzyme classes with no sequence-level support."
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
    "reason": "The UniProt entry E7FHH1 annotates this protein with EC 1.97.1.13 and the exact catalytic reaction in option C, supported by direct experimental evidence (ECO:0000269) from two publications (PubMed:16199576 and PubMed:36269456). The reaction text matches option C verbatim.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the aldehyde/tungsten-containing aldehyde oxidoreductase (AOR/WOR) family within the DMSO reductase superfamily: (1) the 'HND' motif (~residue 130: 'IHNDTVEIRD') diagnostic of the AOR/WOR family active site; (2) the 'GAGGYS' tungsten-cofactor-binding motif (~residue 280: 'TGAGGYSVGHDRSSEPIRNW'); (3) multiple 'GKG' motifs (e.g., 'IYIGKGGEN', 'AAGYGGYGAVMGSKNLKAVIAKGSGP') indicating 4Fe-4S cluster coordination. These features unambiguously identify a tungsten-containing oxidoreductase with 4Fe-4S ferredoxin as electron acceptor. Among the four options, only C involves a tungsten/molybdenum oxidoreductase coupled to 4Fe-4S ferredoxin. Option A (cardiolipin synthase) is a phospholipase with no resemblance. Option B (CMP-sialic acid synthetase) is a nucleotidyltransferase with no resemblance. Option D (radical SAM enzyme) requires a CX3CX2C motif absent from this sequence. Thus family-level sequence features (HND + GAGGYS + GKG) distinguish C from all other choices without needing to know the specific sulfonate substrate.",
    "missing_item_specific_fact": "",
    "reason": "The tungsten cofactor motif (GAGGYS), the HND active-site motif, and 4Fe-4S cluster-binding GKG motifs are well-known family signatures transferable from other AOR/WOR/DMSO-reductase-family proteins. These features uniquely match option C's description of a tungsten oxidoreductase with 4Fe-4S ferredoxin, while excluding A (phospholipase), B (nucleotidyltransferase), and D (radical SAM, no CX3CX2C motif). The specific sulfonate substrate need not be predicted from sequence; the enzyme class alone discriminates the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C is consistent with the tungsten-containing oxidoreductase family features present in the sequence. The other three options represent entirely different enzyme classes with no sequence-level support."
  },
  "important_caveats": [
    "The specific sulfonate substrate (as opposed to aldehyde) was discovered in 2022 (PubMed:36269456); the 2005 paper described it as a tungsten-containing aldehyde oxidoreductase. However, the enzyme class (W-oxidoreductase + 4Fe-4S ferredoxin) is sufficient to select C among the given options.",
    "The UniProt annotation carries ECO:0000269 (direct assay evidence), indicating experimental rather than purely computational assignment.",
    "The sequence matches the current UniProt entry E7FHH1 (Pyrococcus furiosus WOR5 large subunit) exactly."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "E7FHH1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "benchmark_sequence_length": 624,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 61,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "current_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "current_source_sequence_length": 624,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 59,
  "selected_historical_version": {
    "accession": "E7FHH1",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASOR_PYRFU",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "selected_historical_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "selected_historical_source_sequence_length": 624,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"E7FHH1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":61,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Pyrococcus\"],\"scientificName\":\"Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1)\",\"taxonId\":186497}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"Aliphatic sulfonate ferredoxin oxidoreductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"ASOR\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"Tungsten-containing aldehyde oxidoreductase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"WOR5\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5 large subunit\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5-L\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.13\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aliphatic sulfonate oxidoreductase, WOR-like subunit\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.97.1.13\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80643\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29067\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231625\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"an aliphatic sulfonate + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + an aldehyde + sulfite + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80647\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17478\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231625\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"2 oxidized [4Fe-4S]-[ferredoxin] + an aldehyde + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80651\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17478\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29067\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80087\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57305\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:507393\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"2 oxidized [4Fe-4S]-[ferredoxin] + taurine + H2O = aminoacetaldehyde + 2 reduced [4Fe-4S]-[ferredoxin] + sulfite + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80635\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58213\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:507393\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"aminoacetaldehyde + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + glycine + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80639\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57305\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58213\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Bevers L.E.\",\"Bol E.\",\"Hagedoorn P.L.\",\"Hagen W.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16199576\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.187.20.7056-7061.2005\"}],\"citationType\":\"journal article\",\"firstPage\":\"7056\",\"id\":\"16199576\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"7061\",\"publicationDate\":\"2005\",\"title\":\"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus furiosus with a broad substrate specificity.\",\"volume\":\"187\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 43587 / DSM 3638 / JCM 8422 / Vc1\"}],\"referenceNumber\":3,\"referencePositions\":[\"PROTEIN SEQUENCE OF 1-21\",\"FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Mathew L.G.\",\"Haja D.K.\",\"Pritchett C.\",\"McCormick W.\",\"Zeineddine R.\",\"Fontenot L.S.\",\"Rivera M.E.\",\"Glushka J.\",\"Adams M.W.W.\",\"Lanzilotta W.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36269456\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00775-022-01965-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"747\",\"id\":\"36269456\",\"journal\":\"J. Biol. Inorg. Chem.\",\"lastPage\":\"758\",\"publicationDate\":\"2022\",\"title\":\"An unprecedented function for a tungsten-containing oxidoreductase.\",\"volume\":\"27\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X1O\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X6U\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"COM1\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR (4FE-4S) CLUSTER AND TUNGSTOPTERIN\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 1-20",
  "excerpt": "ID   ASOR_PYRFU              Reviewed;         624 AA.\nAC   E7FHH1; A0A5C0XQU4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};\nDE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nDE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};\nDE            Short=ASOR {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-L {ECO:0000303|PubMed:36269456};\nGN   Name=wor5 {ECO:0000303|PubMed:16199576};\nGN   OrderedLocusNames=PF1480 {ECO:0000312|EMBL:AAL81604.1};\nGN   ORFNames=PFDSM3638_07420 {ECO:0000312|EMBL:QEK79109.1};\nOS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Pyrococcus.\nOX   NCBI_TaxID=186497;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 6-13",
  "excerpt": "DE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};\nDE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nDE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};\nDE            Short=ASOR {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-L {ECO:0000303|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 37-45",
  "excerpt": "RN   [3]\nRP   PROTEIN SEQUENCE OF 1-21, FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE, COFACTOR,\nRP   AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=ATCC 43587 / DSM 3638 / JCM 8422 / Vc1;\nRX   PubMed=16199576; DOI=10.1128/jb.187.20.7056-7061.2005;\nRA   Bevers L.E., Bol E., Hagedoorn P.L., Hagen W.R.;\nRT   \"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus\nRT   furiosus with a broad substrate specificity.\";\nRL   J. Bacteriol. 187:7056-7061(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 46-55",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6X1O, ECO:0007744|PDB:6X6U}\nRP   X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR\nRP   (4FE-4S) CLUSTER AND TUNGSTOPTERIN, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND SUBCELLULAR LOCATION.\nRC   STRAIN=COM1;\nRX   PubMed=36269456; DOI=10.1007/s00775-022-01965-0;\nRA   Mathew L.G., Haja D.K., Pritchett C., McCormick W., Zeineddine R.,\nRA   Fontenot L.S., Rivera M.E., Glushka J., Adams M.W.W., Lanzilotta W.N.;\nRT   \"An unprecedented function for a tungsten-containing oxidoreductase.\";\nRL   J. Biol. Inorg. Chem. 27:747-758(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 69-76",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2\nCC         H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6\nCC         H(+); Xref=Rhea:RHEA:80643, Rhea:RHEA-COMP:18797, Rhea:RHEA-\nCC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:29067, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723,\nCC         ChEBI:CHEBI:231625; EC=1.97.1.13;\nCC         Evidence={ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 77-83",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an aliphatic sulfonate + 2 oxidized [4Fe-4S]-[ferredoxin] +\nCC         H2O = 2 reduced [4Fe-4S]-[ferredoxin] + an aldehyde + sulfite + 3\nCC         H(+); Xref=Rhea:RHEA:80647, Rhea:RHEA-COMP:18797, Rhea:RHEA-\nCC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:17478, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723,\nCC         ChEBI:CHEBI:231625; Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 84-90",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 oxidized [4Fe-4S]-[ferredoxin] + an aldehyde + H2O = 2\nCC         reduced [4Fe-4S]-[ferredoxin] + a carboxylate + 3 H(+);\nCC         Xref=Rhea:RHEA:80651, Rhea:RHEA-COMP:18797, Rhea:RHEA-COMP:18798,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17478,\nCC         ChEBI:CHEBI:29067, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723;\nCC         Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 91-97",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced\nCC         [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+);\nCC         Xref=Rhea:RHEA:80087, Rhea:RHEA-COMP:18797, Rhea:RHEA-COMP:18798,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:33722, ChEBI:CHEBI:33723, ChEBI:CHEBI:57305,\nCC         ChEBI:CHEBI:507393; Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 98-104",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 oxidized [4Fe-4S]-[ferredoxin] + taurine + H2O =\nCC         aminoacetaldehyde + 2 reduced [4Fe-4S]-[ferredoxin] + sulfite + 3\nCC         H(+); Xref=Rhea:RHEA:80635, Rhea:RHEA-COMP:18797, Rhea:RHEA-\nCC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:33722, ChEBI:CHEBI:33723, ChEBI:CHEBI:58213,\nCC         ChEBI:CHEBI:507393; Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 105-111",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=aminoacetaldehyde + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2\nCC         reduced [4Fe-4S]-[ferredoxin] + glycine + 3 H(+);\nCC         Xref=Rhea:RHEA:80639, Rhea:RHEA-COMP:18797, Rhea:RHEA-COMP:18798,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:33722,\nCC         ChEBI:CHEBI:33723, ChEBI:CHEBI:57305, ChEBI:CHEBI:58213;\nCC         Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 162. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
