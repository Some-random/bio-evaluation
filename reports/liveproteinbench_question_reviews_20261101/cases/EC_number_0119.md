# EC_number_0119

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 1.1.1.122

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAAVGRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRAVEQELLGTVFIPGDVTQEGDLQTLISETVSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEENLLGAYTLIKLALPHLRKSKGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRYGVRVNCISPGNIWTPLWQELAAATSDPRATILEGTLAQPLGRMGQPAEVGAAAVFLASEATFCTGLELFMTGGAELGYGRKASSSTLVEVPILPP

[Multiple Choices]
A. 1.1.1.336
B. 5.4.99.39
C. 1.1.1.122
D. 3.1.1.29
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

> The supplied sequence exactly matches the rat UniProt entry, whose EC 1.1.1.122 annotation is linked to experimental evidence (ECO:0000269) for oxidation of L-fucose and other sugars. This supports choice C, while preserving that the evidence is reported through a curated database entry citing a paper.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's cofactor-binding motif and enzyme-family features may suggest an NAD-dependent oxidoreductase, helping distinguish it from an isomerase or hydrolase, but they do not establish the precise substrate specificity needed to distinguish the dehydrogenase options.


**Missing item-specific fact**

> The protein's experimentally characterized substrate specificity and corresponding EC annotation are not supplied in the question.


**Reason**

> Choosing the exact four-part EC number depends on protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would resolve it, but is not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options designate distinct enzyme classifications, and the sequence-matched annotation with cited experimental evidence supports C. The sequence-only input does not itself resolve exact substrate specificity, but that is a lookup-dependence limitation rather than evidence that multiple options are correct.


### Important caveats

- The evidence is from a sequence-matched UniProt annotation citing a 2024 paper; the primary study was not independently reviewed here.
- The author’s exact data-construction snapshot is unknown, although the sequence-matched archived entry already records EC 1.1.1.122.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's cofactor-binding motif and enzyme-family features may suggest an NAD-dependent oxidoreductase, helping distinguish it from an isomerase or hydrolase, but they do not establish the precise substrate specificity needed to distinguish the dehydrogenase options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally characterized substrate specificity and corresponding EC annotation are not supplied in the question.",
    "reason": "Choosing the exact four-part EC number depends on protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would resolve it, but is not reasoning from the supplied information."
  },
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rat UniProt entry, whose EC 1.1.1.122 annotation is linked to experimental evidence (ECO:0000269) for oxidation of L-fucose and other sugars. This supports choice C, while preserving that the evidence is reported through a curated database entry citing a paper."
  },
  "important_caveats": [
    "The evidence is from a sequence-matched UniProt annotation citing a 2024 paper; the primary study was not independently reviewed here.",
    "The author’s exact data-construction snapshot is unknown, although the sequence-matched archived entry already records EC 1.1.1.122."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options designate distinct enzyme classifications, and the sequence-matched annotation with cited experimental evidence supports C. The sequence-only input does not itself resolve exact substrate specificity, but that is a lookup-dependence limitation rather than evidence that multiple options are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rat UniProt entry, whose EC 1.1.1.122 annotation is linked to experimental evidence (ECO:0000269) for oxidation of L-fucose and other sugars. This supports choice C, while preserving that the evidence is reported through a curated database entry citing a paper.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's cofactor-binding motif and enzyme-family features may suggest an NAD-dependent oxidoreductase, helping distinguish it from an isomerase or hydrolase, but they do not establish the precise substrate specificity needed to distinguish the dehydrogenase options.",
    "missing_item_specific_fact": "The protein's experimentally characterized substrate specificity and corresponding EC annotation are not supplied in the question.",
    "reason": "Choosing the exact four-part EC number depends on protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would resolve it, but is not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options designate distinct enzyme classifications, and the sequence-matched annotation with cited experimental evidence supports C. The sequence-only input does not itself resolve exact substrate specificity, but that is a lookup-dependence limitation rather than evidence that multiple options are correct."
  },
  "important_caveats": [
    "The evidence is from a sequence-matched UniProt annotation citing a 2024 paper; the primary study was not independently reviewed here.",
    "The author’s exact data-construction snapshot is unknown, although the sequence-matched archived entry already records EC 1.1.1.122."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A8I6GJ95 (rat HSD17B14, 270 aa, sequence SHA256 matched) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al.). The catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+) is confirmed experimentally. The expected answer C (1.1.1.122) is directly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal mitochondrial targeting signal and the Rossmann-fold NAD-binding motif (VVVTGGSRGIGAA) allow a model to infer this is an NAD-dependent dehydrogenase (EC 1.1.1.x), thereby eliminating the isomerase (B, EC 5.4.99.39) and hydrolase (D, EC 3.1.1.29). However, no general sequence feature distinguishes EC 1.1.1.122 (L-fucose dehydrogenase) from EC 1.1.1.336 (another EC 1.1.1.x dehydrogenase). The substrate-specificity residues that determine whether this enzyme acts on L-fucose versus the substrate of 1.1.1.336 are not identifiable from the raw sequence without prior knowledge of this particular protein's active-site architecture or its database annotation.


**Missing item-specific fact**

> The specific substrate-binding and catalytic-site residues that confer L-fucose specificity in HSD17B14, or alternatively the protein's identity as HSD17B14/L-fucose dehydrogenase (a function only experimentally established in 2024, PubMed:38944119), are required to distinguish EC 1.1.1.122 from EC 1.1.1.336.


**Reason**

> While the Rossmann fold provides a valid general argument for EC class 1.1.1.x (oxidoreductase, CH-OH, NAD+), selecting the fourth digit (122 vs 336) requires protein-specific knowledge. The function was only confirmed experimentally in 2024; before that, HSD17B14 had no well-established EC assignment. No general biological reasoning from the 270-aa sequence alone can distinguish these two EC 1.1.1.x options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (1.1.1.336) and C (1.1.1.122) are EC 1.1.1.x oxidoreductases consistent with the Rossmann-fold NAD-binding motif visible in the sequence. Without protein-specific knowledge, a model cannot definitively choose between them. Options B (isomerase) and D (hydrolase) are clearly incompatible with the dehydrogenase fold and can be eliminated by reasoning.


### Important caveats

- The EC 1.1.1.122 assignment for HSD17B14 is very recent (2024, PubMed:38944119). Before this publication, HSD17B14 was primarily associated with mitochondrial RNA processing and lacked a confirmed EC number. A model trained on older data would not associate this sequence with EC 1.1.1.122.
- The protein's alternative name 'Hydroxysteroid 17-beta dehydrogenase 14' could mislead a model toward steroid-dehydrogenase EC numbers, which are not among the choices, adding to the lookup dependency.
- All UniProt evidence is reviewer-only and was not available to the evaluated model. The sequence-match is confirmed (SHA256 identical, 270 aa).
- The identity of EC 1.1.1.336 as a specific enzyme was not independently verified in this audit; it is treated as a plausible distractor within the same EC subclass.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal mitochondrial targeting signal and the Rossmann-fold NAD-binding motif (VVVTGGSRGIGAA) allow a model to infer this is an NAD-dependent dehydrogenase (EC 1.1.1.x), thereby eliminating the isomerase (B, EC 5.4.99.39) and hydrolase (D, EC 3.1.1.29). However, no general sequence feature distinguishes EC 1.1.1.122 (L-fucose dehydrogenase) from EC 1.1.1.336 (another EC 1.1.1.x dehydrogenase). The substrate-specificity residues that determine whether this enzyme acts on L-fucose versus the substrate of 1.1.1.336 are not identifiable from the raw sequence without prior knowledge of this particular protein's active-site architecture or its database annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate-binding and catalytic-site residues that confer L-fucose specificity in HSD17B14, or alternatively the protein's identity as HSD17B14/L-fucose dehydrogenase (a function only experimentally established in 2024, PubMed:38944119), are required to distinguish EC 1.1.1.122 from EC 1.1.1.336.",
    "reason": "While the Rossmann fold provides a valid general argument for EC class 1.1.1.x (oxidoreductase, CH-OH, NAD+), selecting the fourth digit (122 vs 336) requires protein-specific knowledge. The function was only confirmed experimentally in 2024; before that, HSD17B14 had no well-established EC assignment. No general biological reasoning from the 270-aa sequence alone can distinguish these two EC 1.1.1.x options."
  },
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A8I6GJ95 (rat HSD17B14, 270 aa, sequence SHA256 matched) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al.). The catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+) is confirmed experimentally. The expected answer C (1.1.1.122) is directly supported."
  },
  "important_caveats": [
    "The EC 1.1.1.122 assignment for HSD17B14 is very recent (2024, PubMed:38944119). Before this publication, HSD17B14 was primarily associated with mitochondrial RNA processing and lacked a confirmed EC number. A model trained on older data would not associate this sequence with EC 1.1.1.122.",
    "The protein's alternative name 'Hydroxysteroid 17-beta dehydrogenase 14' could mislead a model toward steroid-dehydrogenase EC numbers, which are not among the choices, adding to the lookup dependency.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model. The sequence-match is confirmed (SHA256 identical, 270 aa).",
    "The identity of EC 1.1.1.336 as a specific enzyme was not independently verified in this audit; it is treated as a plausible distractor within the same EC subclass."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (1.1.1.336) and C (1.1.1.122) are EC 1.1.1.x oxidoreductases consistent with the Rossmann-fold NAD-binding motif visible in the sequence. Without protein-specific knowledge, a model cannot definitively choose between them. Options B (isomerase) and D (hydrolase) are clearly incompatible with the dehydrogenase fold and can be eliminated by reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A8I6GJ95 (rat HSD17B14, 270 aa, sequence SHA256 matched) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, 2024 JBC paper by Witecka et al.). The catalytic activity L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+) is confirmed experimentally. The expected answer C (1.1.1.122) is directly supported.",
    "evidence_ids": ["C4", "C5", "C8", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal mitochondrial targeting signal and the Rossmann-fold NAD-binding motif (VVVTGGSRGIGAA) allow a model to infer this is an NAD-dependent dehydrogenase (EC 1.1.1.x), thereby eliminating the isomerase (B, EC 5.4.99.39) and hydrolase (D, EC 3.1.1.29). However, no general sequence feature distinguishes EC 1.1.1.122 (L-fucose dehydrogenase) from EC 1.1.1.336 (another EC 1.1.1.x dehydrogenase). The substrate-specificity residues that determine whether this enzyme acts on L-fucose versus the substrate of 1.1.1.336 are not identifiable from the raw sequence without prior knowledge of this particular protein's active-site architecture or its database annotation.",
    "missing_item_specific_fact": "The specific substrate-binding and catalytic-site residues that confer L-fucose specificity in HSD17B14, or alternatively the protein's identity as HSD17B14/L-fucose dehydrogenase (a function only experimentally established in 2024, PubMed:38944119), are required to distinguish EC 1.1.1.122 from EC 1.1.1.336.",
    "reason": "While the Rossmann fold provides a valid general argument for EC class 1.1.1.x (oxidoreductase, CH-OH, NAD+), selecting the fourth digit (122 vs 336) requires protein-specific knowledge. The function was only confirmed experimentally in 2024; before that, HSD17B14 had no well-established EC assignment. No general biological reasoning from the 270-aa sequence alone can distinguish these two EC 1.1.1.x options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (1.1.1.336) and C (1.1.1.122) are EC 1.1.1.x oxidoreductases consistent with the Rossmann-fold NAD-binding motif visible in the sequence. Without protein-specific knowledge, a model cannot definitively choose between them. Options B (isomerase) and D (hydrolase) are clearly incompatible with the dehydrogenase fold and can be eliminated by reasoning."
  },
  "important_caveats": [
    "The EC 1.1.1.122 assignment for HSD17B14 is very recent (2024, PubMed:38944119). Before this publication, HSD17B14 was primarily associated with mitochondrial RNA processing and lacked a confirmed EC number. A model trained on older data would not associate this sequence with EC 1.1.1.122.",
    "The protein's alternative name 'Hydroxysteroid 17-beta dehydrogenase 14' could mislead a model toward steroid-dehydrogenase EC numbers, which are not among the choices, adding to the lookup dependency.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model. The sequence-match is confirmed (SHA256 identical, 270 aa).",
    "The identity of EC 1.1.1.336 as a specific enzyme was not independently verified in this audit; it is treated as a plausible distractor within the same EC subclass."
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

**Accession:** `A0A8I6GJ95` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.152365+00:00.  

```json
"A0A8I6GJ95"
```

Source SHA-256: `b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.152365+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Hydroxysteroid 17-beta dehydrogenase 14"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"value":"1.1.1.122"}],"fullName":{"value":"L-fucose dehydrogenase"}}}
```

Source SHA-256: `b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.152365+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"38944119","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81516"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"name":"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81515"},{"database":"ChEBI","id":"CHEBI:2181"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:81457"}]}}
```

Source SHA-256: `b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.152365+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"38944119","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81520"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"name":"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81519"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:46994"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:194242"}]}}
```

Source SHA-256: `b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.152365+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"38944119","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81524"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"name":"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81523"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:37619"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:182410"}]}}
```

Source SHA-256: `b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.152365+00:00.  

```json
{"citation":{"authors":["Witecka A.","Kazak V.","Kwiatkowski S.","Kiersztan A.","Jagielski A.K.","Kozminski W.","Augustyniak R.","Drozak J."],"citationCrossReferences":[{"database":"PubMed","id":"38944119"},{"database":"DOI","id":"10.1016/j.jbc.2024.107501"}],"citationType":"journal article","firstPage":"107501","id":"38944119","journal":"J. Biol. Chem.","lastPage":"107501","publicationDate":"2024","title":"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.","volume":"300"},"referenceNumber":2,"referencePositions":["CATALYTIC ACTIVITY","FUNCTION","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:42:06.511227+00:00.  

```text
DE   RecName: Full=L-fucose dehydrogenase;
DE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};
DE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;
```

Source SHA-256: `254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)  
**Locator:** `lines 62-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:42:06.511227+00:00.  

```text
RN   [2]
RP   CATALYTIC ACTIVITY, FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;
RA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,
RA   Kozminski W., Augustyniak R., Drozak J.;
RT   "Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose
RT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.";
RL   J. Biol. Chem. 300:107501-107501(2024).
```

Source SHA-256: `254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)  
**Locator:** `lines 77-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:42:06.511227+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);
CC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;
CC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;
CC         Evidence={ECO:0000305|PubMed:38944119};
```

Source SHA-256: `254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
