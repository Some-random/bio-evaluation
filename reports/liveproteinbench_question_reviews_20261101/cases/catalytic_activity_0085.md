# catalytic_activity_0085

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGETTQLDLSVKAVGWGAADASGTLQPIKFYRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVIEVGSKVQKFKVGDKVGVGCMVGSCGKCFNCQNGMENYCPEPNMADGSVYREQQGEPSFGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGIVVYSPMKYMGLDKPGKHIGVIGLGGLGSIAVKFIKAFGGKATVISTSKRKEKEAIEEHGADAFVVNTDTEKLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGVVLLVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQETLDFAAQHNIVCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYED

[Multiple Choices]
A. a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)
B. acetaldehyde + NAD(+) + H2O = acetate + NADH + 2 H(+)
C. NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+)
D. (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH
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

> The supplied sequence exactly matches the UniProt entry annotated as geissoschizine synthase, and that entry lists choice D as its catalytic reaction. However, the reaction annotation is transferred by similarity from UniProtKB:W8JWW7 (ECO:0000250), so it supports the key as a database annotation rather than establishing direct experimental verification for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone may suggest an enzyme with oxidoreductase-related features, but it does not provide a defensible way to identify geissoschizine or the specific 4,21-dehydrogenation among the choices.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental substrate/reaction information identifying this sequence as geissoschizine synthase.


**Reason**

> Selecting D requires an item-specific functional association absent from the input. General sequence reasoning does not distinguish this specialized alkaloid reaction from other possible enzyme activities.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the matched database annotation supports D; the limitation concerns whether that reaction can be inferred from the input, not ambiguity between the listed reactions.


### Important caveats

- The reviewer-only evidence identifies a sequence-matched database record, but that identity and annotation were not supplied to the evaluated model.
- The catalytic reaction evidence is transferred by similarity from another UniProt entry; it is not presented here as a direct experimental measurement for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone may suggest an enzyme with oxidoreductase-related features, but it does not provide a defensible way to identify geissoschizine or the specific 4,21-dehydrogenation among the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate/reaction information identifying this sequence as geissoschizine synthase.",
    "reason": "Selecting D requires an item-specific functional association absent from the input. General sequence reasoning does not distinguish this specialized alkaloid reaction from other possible enzyme activities."
  },
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as geissoschizine synthase, and that entry lists choice D as its catalytic reaction. However, the reaction annotation is transferred by similarity from UniProtKB:W8JWW7 (ECO:0000250), so it supports the key as a database annotation rather than establishing direct experimental verification for this exact protein."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched database record, but that identity and annotation were not supplied to the evaluated model.",
    "The catalytic reaction evidence is transferred by similarity from another UniProt entry; it is not presented here as a direct experimental measurement for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched database annotation supports D; the limitation concerns whether that reaction can be inferred from the input, not ambiguity between the listed reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as geissoschizine synthase, and that entry lists choice D as its catalytic reaction. However, the reaction annotation is transferred by similarity from UniProtKB:W8JWW7 (ECO:0000250), so it supports the key as a database annotation rather than establishing direct experimental verification for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone may suggest an enzyme with oxidoreductase-related features, but it does not provide a defensible way to identify geissoschizine or the specific 4,21-dehydrogenation among the choices.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate/reaction information identifying this sequence as geissoschizine synthase.",
    "reason": "Selecting D requires an item-specific functional association absent from the input. General sequence reasoning does not distinguish this specialized alkaloid reaction from other possible enzyme activities."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched database annotation supports D; the limitation concerns whether that reaction can be inferred from the input, not ambiguity between the listed reactions."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched database record, but that identity and annotation were not supplied to the evaluated model.",
    "The catalytic reaction evidence is transferred by similarity from another UniProt entry; it is not presented here as a direct experimental measurement for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence (365 aa, SHA-256 matched) corresponds exactly to UniProt P0DXJ1 (GS_RAUSE, Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina. The annotated catalytic activity (C5, H4) is verbatim: '(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH', matching choice D. The EC number carries evidence code ECO:0000250 (inferred by similarity to W8JWW7), while the protein name and functional context are supported by PubMed 38212296 (Nat. Commun. 2024, Guo et al.) with evidence code ECO:0000312 (experimental). The physiological direction is noted as right-to-left (RHEA:11378), but the canonical reaction equation as written in choice D matches RHEA:11376 as annotated. The answer is supported by the database annotation and the underlying experimental publication.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains Rossmann-fold-like motifs (e.g., 'GGLGS' near residue ~170, 'GAPETL' near ~230) consistent with NAD(P)-dependent oxidoreductase activity, which could plausibly help eliminate choice A (tRNA acetyltransferase using acetyl-CoA/ATP, no Rossmann fold) and choice C (NADase, entirely different mechanism and fold). However, distinguishing choice B (acetaldehyde dehydrogenase, NAD+-dependent) from choice D (geissoschizine synthase, NADP+-dependent alkaloid dehydrogenase) requires knowing the specific substrate identity (geissoschizine, a monoterpenoid indole alkaloid) and the specific dehydrogenation positions (4,21). No general sequence motif uniquely encodes 'this is a Rauvolfia alkaloid dehydrogenase acting on geissoschizine.'


**Missing item-specific fact**

> The identity of the specific natural-product substrate (geissoschizine) and the regiochemistry of dehydrogenation (4,21-dehydro) are item-specific facts that cannot be deduced from the amino acid sequence by general biological reasoning. The protein's association with Rauvolfia serpentina alkaloid biosynthesis (from PubMed 38212296) and the precise EC 1.3.1.36 assignment are database/experimental annotations absent from the model input.


**Reason**

> While Rossmann-fold motifs narrow the class to NAD(P)-dependent oxidoreductases (eliminating A and C with moderate confidence), the choice between a generic aldehyde dehydrogenase (B) and a highly specific plant alkaloid dehydrogenase (D) cannot be resolved by sequence reasoning alone. Identifying geissoschizine synthase requires recognizing this particular protein or its database annotation, making the question lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the annotation evidence, only D matches the catalytic activity of P0DXJ1. Choices A, B, and C describe mechanistically distinct reactions (acetyltransferase, aldehyde dehydrogenase, NADase) inconsistent with the observed Rossmann-fold oxidoreductase architecture and the specific EC 1.3.1.36 annotation. No ambiguity in the correct answer exists from the evidence standpoint, though from the model's reasoning standpoint B is a closer distractor than A or C.


### Important caveats

- The EC number assignment carries ECO:0000250 (inferred by similarity to W8JWW7), meaning the reaction annotation is transferred rather than directly measured on P0DXJ1 itself. The PubMed 38212296 reference (Guo et al., Nat. Commun. 2024) provides experimental context for the ajmaline biosynthesis pathway including this step.
- The physiological direction is annotated as right-to-left (RHEA:11378), meaning in vivo the enzyme likely catalyzes 4,21-dehydrogeissoschizine + NADPH → (19E)-geissoschizine + NADP+. The multiple-choice option D presents the reaction in the canonical (left-to-right) direction per RHEA:11376, which is standard practice in EC annotations.
- The UniProt entry was first public on 2025-06-18; the historical record (entry version 2) was released 2026-01-28. The sequence match is confirmed across both current and historical snapshots.
- The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 365-aa sequence and the four reaction choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains Rossmann-fold-like motifs (e.g., 'GGLGS' near residue ~170, 'GAPETL' near ~230) consistent with NAD(P)-dependent oxidoreductase activity, which could plausibly help eliminate choice A (tRNA acetyltransferase using acetyl-CoA/ATP, no Rossmann fold) and choice C (NADase, entirely different mechanism and fold). However, distinguishing choice B (acetaldehyde dehydrogenase, NAD+-dependent) from choice D (geissoschizine synthase, NADP+-dependent alkaloid dehydrogenase) requires knowing the specific substrate identity (geissoschizine, a monoterpenoid indole alkaloid) and the specific dehydrogenation positions (4,21). No general sequence motif uniquely encodes 'this is a Rauvolfia alkaloid dehydrogenase acting on geissoschizine.'",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the specific natural-product substrate (geissoschizine) and the regiochemistry of dehydrogenation (4,21-dehydro) are item-specific facts that cannot be deduced from the amino acid sequence by general biological reasoning. The protein's association with Rauvolfia serpentina alkaloid biosynthesis (from PubMed 38212296) and the precise EC 1.3.1.36 assignment are database/experimental annotations absent from the model input.",
    "reason": "While Rossmann-fold motifs narrow the class to NAD(P)-dependent oxidoreductases (eliminating A and C with moderate confidence), the choice between a generic aldehyde dehydrogenase (B) and a highly specific plant alkaloid dehydrogenase (D) cannot be resolved by sequence reasoning alone. Identifying geissoschizine synthase requires recognizing this particular protein or its database annotation, making the question lookup-dependent."
  },
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence (365 aa, SHA-256 matched) corresponds exactly to UniProt P0DXJ1 (GS_RAUSE, Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina. The annotated catalytic activity (C5, H4) is verbatim: '(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH', matching choice D. The EC number carries evidence code ECO:0000250 (inferred by similarity to W8JWW7), while the protein name and functional context are supported by PubMed 38212296 (Nat. Commun. 2024, Guo et al.) with evidence code ECO:0000312 (experimental). The physiological direction is noted as right-to-left (RHEA:11378), but the canonical reaction equation as written in choice D matches RHEA:11376 as annotated. The answer is supported by the database annotation and the underlying experimental publication."
  },
  "important_caveats": [
    "The EC number assignment carries ECO:0000250 (inferred by similarity to W8JWW7), meaning the reaction annotation is transferred rather than directly measured on P0DXJ1 itself. The PubMed 38212296 reference (Guo et al., Nat. Commun. 2024) provides experimental context for the ajmaline biosynthesis pathway including this step.",
    "The physiological direction is annotated as right-to-left (RHEA:11378), meaning in vivo the enzyme likely catalyzes 4,21-dehydrogeissoschizine + NADPH → (19E)-geissoschizine + NADP+. The multiple-choice option D presents the reaction in the canonical (left-to-right) direction per RHEA:11376, which is standard practice in EC annotations.",
    "The UniProt entry was first public on 2025-06-18; the historical record (entry version 2) was released 2026-01-28. The sequence match is confirmed across both current and historical snapshots.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 365-aa sequence and the four reaction choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the annotation evidence, only D matches the catalytic activity of P0DXJ1. Choices A, B, and C describe mechanistically distinct reactions (acetyltransferase, aldehyde dehydrogenase, NADase) inconsistent with the observed Rossmann-fold oxidoreductase architecture and the specific EC 1.3.1.36 annotation. No ambiguity in the correct answer exists from the evidence standpoint, though from the model's reasoning standpoint B is a closer distractor than A or C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence (365 aa, SHA-256 matched) corresponds exactly to UniProt P0DXJ1 (GS_RAUSE, Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina. The annotated catalytic activity (C5, H4) is verbatim: '(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH', matching choice D. The EC number carries evidence code ECO:0000250 (inferred by similarity to W8JWW7), while the protein name and functional context are supported by PubMed 38212296 (Nat. Commun. 2024, Guo et al.) with evidence code ECO:0000312 (experimental). The physiological direction is noted as right-to-left (RHEA:11378), but the canonical reaction equation as written in choice D matches RHEA:11376 as annotated. The answer is supported by the database annotation and the underlying experimental publication.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains Rossmann-fold-like motifs (e.g., 'GGLGS' near residue ~170, 'GAPETL' near ~230) consistent with NAD(P)-dependent oxidoreductase activity, which could plausibly help eliminate choice A (tRNA acetyltransferase using acetyl-CoA/ATP, no Rossmann fold) and choice C (NADase, entirely different mechanism and fold). However, distinguishing choice B (acetaldehyde dehydrogenase, NAD+-dependent) from choice D (geissoschizine synthase, NADP+-dependent alkaloid dehydrogenase) requires knowing the specific substrate identity (geissoschizine, a monoterpenoid indole alkaloid) and the specific dehydrogenation positions (4,21). No general sequence motif uniquely encodes 'this is a Rauvolfia alkaloid dehydrogenase acting on geissoschizine.'",
    "missing_item_specific_fact": "The identity of the specific natural-product substrate (geissoschizine) and the regiochemistry of dehydrogenation (4,21-dehydro) are item-specific facts that cannot be deduced from the amino acid sequence by general biological reasoning. The protein's association with Rauvolfia serpentina alkaloid biosynthesis (from PubMed 38212296) and the precise EC 1.3.1.36 assignment are database/experimental annotations absent from the model input.",
    "reason": "While Rossmann-fold motifs narrow the class to NAD(P)-dependent oxidoreductases (eliminating A and C with moderate confidence), the choice between a generic aldehyde dehydrogenase (B) and a highly specific plant alkaloid dehydrogenase (D) cannot be resolved by sequence reasoning alone. Identifying geissoschizine synthase requires recognizing this particular protein or its database annotation, making the question lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the annotation evidence, only D matches the catalytic activity of P0DXJ1. Choices A, B, and C describe mechanistically distinct reactions (acetyltransferase, aldehyde dehydrogenase, NADase) inconsistent with the observed Rossmann-fold oxidoreductase architecture and the specific EC 1.3.1.36 annotation. No ambiguity in the correct answer exists from the evidence standpoint, though from the model's reasoning standpoint B is a closer distractor than A or C."
  },
  "important_caveats": [
    "The EC number assignment carries ECO:0000250 (inferred by similarity to W8JWW7), meaning the reaction annotation is transferred rather than directly measured on P0DXJ1 itself. The PubMed 38212296 reference (Guo et al., Nat. Commun. 2024) provides experimental context for the ajmaline biosynthesis pathway including this step.",
    "The physiological direction is annotated as right-to-left (RHEA:11378), meaning in vivo the enzyme likely catalyzes 4,21-dehydrogeissoschizine + NADPH → (19E)-geissoschizine + NADP+. The multiple-choice option D presents the reaction in the canonical (left-to-right) direction per RHEA:11376, which is standard practice in EC annotations.",
    "The UniProt entry was first public on 2025-06-18; the historical record (entry version 2) was released 2026-01-28. The sequence match is confirmed across both current and historical snapshots.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 365-aa sequence and the four reaction choices."
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

**Accession:** `P0DXJ1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
"P0DXJ1"
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"W8JWW7","source":"UniProtKB"}],"value":"1.3.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Geissoschizine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsGS"}]}}
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000250","id":"W8JWW7","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:11378"}}],"reaction":{"ecNumber":"1.3.1.36","evidences":[{"evidenceCode":"ECO:0000250","id":"W8JWW7","source":"UniProtKB"}],"name":"(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:11376"},{"database":"ChEBI","id":"CHEBI:17037"},{"database":"ChEBI","id":"CHEBI:17294"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:32.265438+00:00.  

```text
DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};
DE            Short=RsGS {ECO:0000303|PubMed:38212296};
DE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};
```

Source SHA-256: `7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)  
**Locator:** `lines 16-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:32.265438+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:WKU61919.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, BIOTECHNOLOGY, TISSUE SPECIFICITY,
RP   AND PATHWAY.
RX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;
RA   Guo J., Gao D., Lian J., Qu Y.;
RT   "De novo biosynthesis of antiarrhythmic alkaloid ajmaline.";
RL   Nat. Commun. 15:457-457(2024).
```

Source SHA-256: `7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:32.265438+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine +
CC         NADPH; Xref=Rhea:RHEA:11376, ChEBI:CHEBI:17037, ChEBI:CHEBI:17294,
CC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.3.1.36;
CC         Evidence={ECO:0000250|UniProtKB:W8JWW7};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:11378;
CC         Evidence={ECO:0000250|UniProtKB:W8JWW7};
```

Source SHA-256: `7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
