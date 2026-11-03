# EC_number_0133: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0133.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 1.3.1.36

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MAGETTQLDLSVKAVGWGAADASGTLQPIKFYRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVIEVGSKVQKFKVGDKVGVGCMVGSCGKCFNCQNGMENYCPEPNMADGSVYREQQGEPSFGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGIVVYSPMKYMGLDKPGKHIGVIGLGGLGSIAVKFIKAFGGKATVISTSKRKEKEAIEEHGADAFVVNTDTEKLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGVVLLVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQETLDFAAQHNIVCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYED

[Multiple Choices]
A. 1.3.1.73
B. 1.14.14.126
C. 1.3.1.36
D. 3.6.1.5
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact supplied sequence matches the UniProt entry annotated as geissoschizine synthase, EC 1.3.1.36, with a corresponding catalytic reaction. The annotation is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but no supplied context or general sequence feature uniquely establishes the geissoschizine reaction or distinguishes this precise EC number from the alternatives.


**Missing item-specific fact**

> The protein-specific functional annotation identifying this sequence as geissoschizine synthase and associating it with EC 1.3.1.36.


**Reason**

> Selecting the precise EC classification depends on protein-specific functional knowledge absent from the prompt; recognizing the sequence or consulting an annotation would supply that missing information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed choices specify distinct EC classifications, and the matched sequence annotation supports C.


### Important caveats

- The supporting UniProt EC and catalytic-activity annotations are similarity-transferred from a homolog, not shown here as direct experimental confirmation for the supplied protein.
- The sequence match applies to the cited database record; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but no supplied context or general sequence feature uniquely establishes the geissoschizine reaction or distinguishes this precise EC number from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation identifying this sequence as geissoschizine synthase and associating it with EC 1.3.1.36.",
    "reason": "Selecting the precise EC classification depends on protein-specific functional knowledge absent from the prompt; recognizing the sequence or consulting an annotation would supply that missing information."
  },
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as geissoschizine synthase, EC 1.3.1.36, with a corresponding catalytic reaction. The annotation is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The supporting UniProt EC and catalytic-activity annotations are similarity-transferred from a homolog, not shown here as direct experimental confirmation for the supplied protein.",
    "The sequence match applies to the cited database record; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed choices specify distinct EC classifications, and the matched sequence annotation supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as geissoschizine synthase, EC 1.3.1.36, with a corresponding catalytic reaction. The annotation is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but no supplied context or general sequence feature uniquely establishes the geissoschizine reaction or distinguishes this precise EC number from the alternatives.",
    "missing_item_specific_fact": "The protein-specific functional annotation identifying this sequence as geissoschizine synthase and associating it with EC 1.3.1.36.",
    "reason": "Selecting the precise EC classification depends on protein-specific functional knowledge absent from the prompt; recognizing the sequence or consulting an annotation would supply that missing information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed choices specify distinct EC classifications, and the matched sequence annotation supports C."
  },
  "important_caveats": [
    "The supporting UniProt EC and catalytic-activity annotations are similarity-transferred from a homolog, not shown here as direct experimental confirmation for the supplied protein.",
    "The sequence match applies to the cited database record; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ1 (sequence SHA256 matched) annotates this protein as Geissoschizine synthase with EC 1.3.1.36. The catalytic reaction is (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH. However, the EC annotation carries evidence code ECO:0000250 (similarity to UniProtKB:W8JWW7), meaning it is a computational inference by homology rather than direct experimental characterization of this specific protein's substrate specificity. The protein name and pathway context derive from PubMed 38212296 (Nat. Commun. 2024), which characterized the ajmaline biosynthesis pathway in Rauvolfia serpentina. The key is supported by current database annotation but rests on transferred similarity evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable Rossmann-fold NAD(P)-binding motifs (e.g., GCMVGSCGKCFNC, GGLGSIAVKFIK) consistent with an oxidoreductase, which rules out D (3.6.1.5, a hydrolase/GTPase) and B (1.14.14.126, a cytochrome P450 requiring heme-binding motifs like FxxGxxxCxG). However, both remaining options A (1.3.1.73) and C (1.3.1.36) belong to the same EC subclass 1.3.1 (oxidoreductases acting on CH-CH group with NAD+/NADP+ as acceptor). Distinguishing between these two requires knowing the specific substrate (geissoschizine vs. the substrate of 1.3.1.73), which cannot be reliably inferred from general sequence features alone.


**Missing item-specific fact**

> The specific substrate identity of this enzyme (geissoschizine) and the distinction between the substrates of EC 1.3.1.73 and EC 1.3.1.36. Additionally, knowledge that Rauvolfia serpentina alkaloid biosynthesis involves geissoschizine synthase at this pathway step is item-specific pathway knowledge, not general biological reasoning derivable from the sequence.


**Reason**

> While the sequence supports broad classification as an NAD(P)-dependent dehydrogenase (eliminating D and B), the critical distinction between the two 1.3.1.x options requires knowing which specific small-molecule substrate the enzyme acts upon. No general sequence heuristic reliably distinguishes between two dehydrogenases in the same EC subclass by substrate identity. Selection of C over A depends on memorizing this protein's annotation or knowing Rauvolfia serpentina's alkaloid biosynthetic pathway in detail.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (1.3.1.73) and C (1.3.1.36) fall within EC subclass 1.3.1 and describe NAD(P)-dependent dehydrogenases acting on CH-CH bonds. From the sequence alone, a model can identify the enzyme as an NAD(P)-binding oxidoreductase but cannot confidently distinguish which specific substrate (and thus which final EC digit) applies. Without memorized pathway knowledge of Rauvolfia serpentina alkaloid biosynthesis, both A and C are plausible choices for a sequence-based predictor.


### Important caveats

- The EC annotation for P0DXJ1 is based on ECO:0000250 (similarity to W8JWW7), not direct experimental assay of this protein's substrate specificity. The annotation is a computational transfer.
- The protein was identified in the context of the ajmaline biosynthesis pathway (PubMed 38212296, 2024), but the specific EC assignment for this enzyme relies on homology rather than in vitro substrate characterization of P0DXJ1 itself.
- The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation may not have been available when the benchmark was constructed.
- The sequence match is confirmed (SHA256 identical between benchmark and UniProt P0DXJ1, 365 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable Rossmann-fold NAD(P)-binding motifs (e.g., GCMVGSCGKCFNC, GGLGSIAVKFIK) consistent with an oxidoreductase, which rules out D (3.6.1.5, a hydrolase/GTPase) and B (1.14.14.126, a cytochrome P450 requiring heme-binding motifs like FxxGxxxCxG). However, both remaining options A (1.3.1.73) and C (1.3.1.36) belong to the same EC subclass 1.3.1 (oxidoreductases acting on CH-CH group with NAD+/NADP+ as acceptor). Distinguishing between these two requires knowing the specific substrate (geissoschizine vs. the substrate of 1.3.1.73), which cannot be reliably inferred from general sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (geissoschizine) and the distinction between the substrates of EC 1.3.1.73 and EC 1.3.1.36. Additionally, knowledge that Rauvolfia serpentina alkaloid biosynthesis involves geissoschizine synthase at this pathway step is item-specific pathway knowledge, not general biological reasoning derivable from the sequence.",
    "reason": "While the sequence supports broad classification as an NAD(P)-dependent dehydrogenase (eliminating D and B), the critical distinction between the two 1.3.1.x options requires knowing which specific small-molecule substrate the enzyme acts upon. No general sequence heuristic reliably distinguishes between two dehydrogenases in the same EC subclass by substrate identity. Selection of C over A depends on memorizing this protein's annotation or knowing Rauvolfia serpentina's alkaloid biosynthetic pathway in detail."
  },
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (sequence SHA256 matched) annotates this protein as Geissoschizine synthase with EC 1.3.1.36. The catalytic reaction is (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH. However, the EC annotation carries evidence code ECO:0000250 (similarity to UniProtKB:W8JWW7), meaning it is a computational inference by homology rather than direct experimental characterization of this specific protein's substrate specificity. The protein name and pathway context derive from PubMed 38212296 (Nat. Commun. 2024), which characterized the ajmaline biosynthesis pathway in Rauvolfia serpentina. The key is supported by current database annotation but rests on transferred similarity evidence."
  },
  "important_caveats": [
    "The EC annotation for P0DXJ1 is based on ECO:0000250 (similarity to W8JWW7), not direct experimental assay of this protein's substrate specificity. The annotation is a computational transfer.",
    "The protein was identified in the context of the ajmaline biosynthesis pathway (PubMed 38212296, 2024), but the specific EC assignment for this enzyme relies on homology rather than in vitro substrate characterization of P0DXJ1 itself.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation may not have been available when the benchmark was constructed.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt P0DXJ1, 365 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (1.3.1.73) and C (1.3.1.36) fall within EC subclass 1.3.1 and describe NAD(P)-dependent dehydrogenases acting on CH-CH bonds. From the sequence alone, a model can identify the enzyme as an NAD(P)-binding oxidoreductase but cannot confidently distinguish which specific substrate (and thus which final EC digit) applies. Without memorized pathway knowledge of Rauvolfia serpentina alkaloid biosynthesis, both A and C are plausible choices for a sequence-based predictor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (sequence SHA256 matched) annotates this protein as Geissoschizine synthase with EC 1.3.1.36. The catalytic reaction is (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH. However, the EC annotation carries evidence code ECO:0000250 (similarity to UniProtKB:W8JWW7), meaning it is a computational inference by homology rather than direct experimental characterization of this specific protein's substrate specificity. The protein name and pathway context derive from PubMed 38212296 (Nat. Commun. 2024), which characterized the ajmaline biosynthesis pathway in Rauvolfia serpentina. The key is supported by current database annotation but rests on transferred similarity evidence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable Rossmann-fold NAD(P)-binding motifs (e.g., GCMVGSCGKCFNC, GGLGSIAVKFIK) consistent with an oxidoreductase, which rules out D (3.6.1.5, a hydrolase/GTPase) and B (1.14.14.126, a cytochrome P450 requiring heme-binding motifs like FxxGxxxCxG). However, both remaining options A (1.3.1.73) and C (1.3.1.36) belong to the same EC subclass 1.3.1 (oxidoreductases acting on CH-CH group with NAD+/NADP+ as acceptor). Distinguishing between these two requires knowing the specific substrate (geissoschizine vs. the substrate of 1.3.1.73), which cannot be reliably inferred from general sequence features alone.",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (geissoschizine) and the distinction between the substrates of EC 1.3.1.73 and EC 1.3.1.36. Additionally, knowledge that Rauvolfia serpentina alkaloid biosynthesis involves geissoschizine synthase at this pathway step is item-specific pathway knowledge, not general biological reasoning derivable from the sequence.",
    "reason": "While the sequence supports broad classification as an NAD(P)-dependent dehydrogenase (eliminating D and B), the critical distinction between the two 1.3.1.x options requires knowing which specific small-molecule substrate the enzyme acts upon. No general sequence heuristic reliably distinguishes between two dehydrogenases in the same EC subclass by substrate identity. Selection of C over A depends on memorizing this protein's annotation or knowing Rauvolfia serpentina's alkaloid biosynthetic pathway in detail."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (1.3.1.73) and C (1.3.1.36) fall within EC subclass 1.3.1 and describe NAD(P)-dependent dehydrogenases acting on CH-CH bonds. From the sequence alone, a model can identify the enzyme as an NAD(P)-binding oxidoreductase but cannot confidently distinguish which specific substrate (and thus which final EC digit) applies. Without memorized pathway knowledge of Rauvolfia serpentina alkaloid biosynthesis, both A and C are plausible choices for a sequence-based predictor."
  },
  "important_caveats": [
    "The EC annotation for P0DXJ1 is based on ECO:0000250 (similarity to W8JWW7), not direct experimental assay of this protein's substrate specificity. The annotation is a computational transfer.",
    "The protein was identified in the context of the ajmaline biosynthesis pathway (PubMed 38212296, 2024), but the specific EC assignment for this enzyme relies on homology rather than in vitro substrate characterization of P0DXJ1 itself.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation may not have been available when the benchmark was constructed.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt P0DXJ1, 365 aa)."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns EC 1.3.1.36 and gives the corresponding catalytic reaction. The assignment is supported by similarity-based evidence (ECO:0000250), so it is a database annotation transferred from a homolog rather than direct experimental evidence shown here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may support a soluble oxidoreductase hypothesis and thereby make the P450 and ATPase alternatives less plausible. But A and C are both EC 1.3.1 enzymes; generic cofactor-binding or redox-family features do not establish which substrate-specific activity applies.


**Missing item-specific fact**

> The protein's catalytic substrate/reaction, or a sufficiently specific homolog relationship establishing that activity, is needed to distinguish EC 1.3.1.36 from EC 1.3.1.73.


**Reason**

> The supplied sequence alone does not provide a concrete transferable basis for the substrate-level distinction between A and C. Choosing C requires the relevant activity annotation or sufficiently specific functional homology, neither of which is supplied as context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported EC assignment identifies C; the difficulty of inferring it from the sequence does not make another listed EC a defensible annotation for this protein.


### Important caveats

- The source annotation is sequence-matched, but its cited evidence is similarity-based; the supplied evidence does not independently establish experimental validation of the exact protein's reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may support a soluble oxidoreductase hypothesis and thereby make the P450 and ATPase alternatives less plausible. But A and C are both EC 1.3.1 enzymes; generic cofactor-binding or redox-family features do not establish which substrate-specific activity applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's catalytic substrate/reaction, or a sufficiently specific homolog relationship establishing that activity, is needed to distinguish EC 1.3.1.36 from EC 1.3.1.73.",
    "reason": "The supplied sequence alone does not provide a concrete transferable basis for the substrate-level distinction between A and C. Choosing C requires the relevant activity annotation or sufficiently specific functional homology, neither of which is supplied as context."
  },
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.3.1.36 and gives the corresponding catalytic reaction. The assignment is supported by similarity-based evidence (ECO:0000250), so it is a database annotation transferred from a homolog rather than direct experimental evidence shown here."
  },
  "important_caveats": [
    "The source annotation is sequence-matched, but its cited evidence is similarity-based; the supplied evidence does not independently establish experimental validation of the exact protein's reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported EC assignment identifies C; the difficulty of inferring it from the sequence does not make another listed EC a defensible annotation for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.3.1.36 and gives the corresponding catalytic reaction. The assignment is supported by similarity-based evidence (ECO:0000250), so it is a database annotation transferred from a homolog rather than direct experimental evidence shown here.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may support a soluble oxidoreductase hypothesis and thereby make the P450 and ATPase alternatives less plausible. But A and C are both EC 1.3.1 enzymes; generic cofactor-binding or redox-family features do not establish which substrate-specific activity applies.",
    "missing_item_specific_fact": "The protein's catalytic substrate/reaction, or a sufficiently specific homolog relationship establishing that activity, is needed to distinguish EC 1.3.1.36 from EC 1.3.1.73.",
    "reason": "The supplied sequence alone does not provide a concrete transferable basis for the substrate-level distinction between A and C. Choosing C requires the relevant activity annotation or sufficiently specific functional homology, neither of which is supplied as context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported EC assignment identifies C; the difficulty of inferring it from the sequence does not make another listed EC a defensible annotation for this protein."
  },
  "important_caveats": [
    "The source annotation is sequence-matched, but its cited evidence is similarity-based; the supplied evidence does not independently establish experimental validation of the exact protein's reaction."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ1 (GS_RAUSE) annotates this 365-aa protein as Geissoschizine synthase with EC 1.3.1.36, catalyzing (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH. The sequence in the question matches the database entry exactly (SHA-256 match confirmed). However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity to W8JWW7), so it is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein. The functional characterization is supported by PubMed 38212296 (Nat. Commun. 2024) which reports the ajmaline biosynthetic pathway including this enzyme.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD(P)-binding motif ('GLGSIAVKFIKAFGGK' with the GxGxxG pattern) and a second nucleotide-binding region ('GAPETLFELPVQPLILGRRKIIGSSTGGLKEYQET'), confirming an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). Crucially, the sequence lacks the conserved P450 heme-binding motif (FxxGxxxCxG), ruling out EC 1.14.14.126 (option B), and lacks Walker A/P-loop motifs (GxxxxGK&#91;ST&#93;) typical of NTPases, ruling out EC 3.6.1.5 (option D). This narrows the answer to the 1.3.1.x class (CH-CH dehydrogenases). Between the two remaining 1.3.1.x options (1.3.1.73 vs 1.3.1.36), the overall sequence architecture—small (~365 aa), plant-type oxidoreductase with the specific arrangement of NAD(P)-binding and catalytic motifs—is consistent with the geissoschizine synthase family within monoterpenoid indole alkaloid (MIA) biosynthesis. A model with knowledge of plant specialized metabolism and MIA biosynthetic enzyme families could recognize this as a geissoschizine synthase (EC 1.3.1.36) rather than the more obscure EC 1.3.1.73. The inference is probabilistic and family-level rather than a first-principles derivation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence features (NAD(P)-binding Rossmann fold, absence of P450 heme motif, absence of ATPase Walker motifs) eliminate options B and D with high confidence. The remaining distinction between 1.3.1.73 and 1.3.1.36 relies on recognizing the enzyme as a member of the geissoschizine synthase / MIA biosynthetic oxidoreductase family, which is transferable knowledge from other characterized plant alkaloid biosynthetic enzymes. This is a defensible family-level inference, though the distinction between the two 1.3.1.x options is less sharp than the elimination of B and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (1.3.1.73) and C (1.3.1.36) are CH-CH group dehydrogenases (EC 1.3.1.x). The sequence features confirm the 1.3.1.x class but do not, on their own, provide a sharply distinguishing feature between these two specific EC numbers without invoking family-level recognition of the geissoschizine synthase lineage. A model that correctly identifies the enzyme class but lacks specific knowledge of the geissoschizine synthase family could plausibly select either A or C. The distinction ultimately rests on recognizing this as a geissoschizine synthase family member rather than a different 1.3.1.x enzyme.


### Important caveats

- The EC 1.3.1.36 annotation in UniProt is based on similarity (ECO:0000250) to W8JWW7, not direct experimental characterization of P0DXJ1 itself, though the 2024 Nat. Commun. paper functionally characterizes the enzyme in the ajmaline pathway.
- The specific identity and substrate of EC 1.3.1.73 could not be independently confirmed from the provided evidence; if it is an extremely obscure or poorly characterized EC number, it may serve as a weak distractor, reducing the effective discrimination burden.
- The sequence-level distinction between the two 1.3.1.x options is less definitive than the elimination of options B and D; the family-level inference supporting C is probabilistic rather than a strict sequence-motif argument.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif ('GLGSIAVKFIKAFGGK' with the GxGxxG pattern) and a second nucleotide-binding region ('GAPETLFELPVQPLILGRRKIIGSSTGGLKEYQET'), confirming an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). Crucially, the sequence lacks the conserved P450 heme-binding motif (FxxGxxxCxG), ruling out EC 1.14.14.126 (option B), and lacks Walker A/P-loop motifs (GxxxxGK[ST]) typical of NTPases, ruling out EC 3.6.1.5 (option D). This narrows the answer to the 1.3.1.x class (CH-CH dehydrogenases). Between the two remaining 1.3.1.x options (1.3.1.73 vs 1.3.1.36), the overall sequence architecture—small (~365 aa), plant-type oxidoreductase with the specific arrangement of NAD(P)-binding and catalytic motifs—is consistent with the geissoschizine synthase family within monoterpenoid indole alkaloid (MIA) biosynthesis. A model with knowledge of plant specialized metabolism and MIA biosynthetic enzyme families could recognize this as a geissoschizine synthase (EC 1.3.1.36) rather than the more obscure EC 1.3.1.73. The inference is probabilistic and family-level rather than a first-principles derivation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence features (NAD(P)-binding Rossmann fold, absence of P450 heme motif, absence of ATPase Walker motifs) eliminate options B and D with high confidence. The remaining distinction between 1.3.1.73 and 1.3.1.36 relies on recognizing the enzyme as a member of the geissoschizine synthase / MIA biosynthetic oxidoreductase family, which is transferable knowledge from other characterized plant alkaloid biosynthetic enzymes. This is a defensible family-level inference, though the distinction between the two 1.3.1.x options is less sharp than the elimination of B and D."
  },
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (GS_RAUSE) annotates this 365-aa protein as Geissoschizine synthase with EC 1.3.1.36, catalyzing (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH. The sequence in the question matches the database entry exactly (SHA-256 match confirmed). However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity to W8JWW7), so it is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein. The functional characterization is supported by PubMed 38212296 (Nat. Commun. 2024) which reports the ajmaline biosynthetic pathway including this enzyme."
  },
  "important_caveats": [
    "The EC 1.3.1.36 annotation in UniProt is based on similarity (ECO:0000250) to W8JWW7, not direct experimental characterization of P0DXJ1 itself, though the 2024 Nat. Commun. paper functionally characterizes the enzyme in the ajmaline pathway.",
    "The specific identity and substrate of EC 1.3.1.73 could not be independently confirmed from the provided evidence; if it is an extremely obscure or poorly characterized EC number, it may serve as a weak distractor, reducing the effective discrimination burden.",
    "The sequence-level distinction between the two 1.3.1.x options is less definitive than the elimination of options B and D; the family-level inference supporting C is probabilistic rather than a strict sequence-motif argument."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (1.3.1.73) and C (1.3.1.36) are CH-CH group dehydrogenases (EC 1.3.1.x). The sequence features confirm the 1.3.1.x class but do not, on their own, provide a sharply distinguishing feature between these two specific EC numbers without invoking family-level recognition of the geissoschizine synthase lineage. A model that correctly identifies the enzyme class but lacks specific knowledge of the geissoschizine synthase family could plausibly select either A or C. The distinction ultimately rests on recognizing this as a geissoschizine synthase family member rather than a different 1.3.1.x enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (GS_RAUSE) annotates this 365-aa protein as Geissoschizine synthase with EC 1.3.1.36, catalyzing (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH. The sequence in the question matches the database entry exactly (SHA-256 match confirmed). However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity to W8JWW7), so it is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein. The functional characterization is supported by PubMed 38212296 (Nat. Commun. 2024) which reports the ajmaline biosynthetic pathway including this enzyme.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif ('GLGSIAVKFIKAFGGK' with the GxGxxG pattern) and a second nucleotide-binding region ('GAPETLFELPVQPLILGRRKIIGSSTGGLKEYQET'), confirming an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). Crucially, the sequence lacks the conserved P450 heme-binding motif (FxxGxxxCxG), ruling out EC 1.14.14.126 (option B), and lacks Walker A/P-loop motifs (GxxxxGK[ST]) typical of NTPases, ruling out EC 3.6.1.5 (option D). This narrows the answer to the 1.3.1.x class (CH-CH dehydrogenases). Between the two remaining 1.3.1.x options (1.3.1.73 vs 1.3.1.36), the overall sequence architecture—small (~365 aa), plant-type oxidoreductase with the specific arrangement of NAD(P)-binding and catalytic motifs—is consistent with the geissoschizine synthase family within monoterpenoid indole alkaloid (MIA) biosynthesis. A model with knowledge of plant specialized metabolism and MIA biosynthetic enzyme families could recognize this as a geissoschizine synthase (EC 1.3.1.36) rather than the more obscure EC 1.3.1.73. The inference is probabilistic and family-level rather than a first-principles derivation.",
    "missing_item_specific_fact": "",
    "reason": "The sequence features (NAD(P)-binding Rossmann fold, absence of P450 heme motif, absence of ATPase Walker motifs) eliminate options B and D with high confidence. The remaining distinction between 1.3.1.73 and 1.3.1.36 relies on recognizing the enzyme as a member of the geissoschizine synthase / MIA biosynthetic oxidoreductase family, which is transferable knowledge from other characterized plant alkaloid biosynthetic enzymes. This is a defensible family-level inference, though the distinction between the two 1.3.1.x options is less sharp than the elimination of B and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (1.3.1.73) and C (1.3.1.36) are CH-CH group dehydrogenases (EC 1.3.1.x). The sequence features confirm the 1.3.1.x class but do not, on their own, provide a sharply distinguishing feature between these two specific EC numbers without invoking family-level recognition of the geissoschizine synthase lineage. A model that correctly identifies the enzyme class but lacks specific knowledge of the geissoschizine synthase family could plausibly select either A or C. The distinction ultimately rests on recognizing this as a geissoschizine synthase family member rather than a different 1.3.1.x enzyme."
  },
  "important_caveats": [
    "The EC 1.3.1.36 annotation in UniProt is based on similarity (ECO:0000250) to W8JWW7, not direct experimental characterization of P0DXJ1 itself, though the 2024 Nat. Commun. paper functionally characterizes the enzyme in the ajmaline pathway.",
    "The specific identity and substrate of EC 1.3.1.73 could not be independently confirmed from the provided evidence; if it is an extremely obscure or poorly characterized EC number, it may serve as a weak distractor, reducing the effective discrimination burden.",
    "The sequence-level distinction between the two 1.3.1.x options is less definitive than the elimination of options B and D; the family-level inference supporting C is probabilistic rather than a strict sequence-motif argument."
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
  "requested_accession": "P0DXJ1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "benchmark_sequence_length": 365,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "current_source_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "current_source_sequence_length": 365,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 2,
  "selected_historical_version": {
    "accession": "P0DXJ1",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GS_RAUSE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "selected_historical_source_sequence_sha256": "be11b71809d30f0c5458041f2312ead6b14de7b52ebdd4b914b15674410bd94d",
  "selected_historical_source_sequence_length": 365,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P0DXJ1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"W8JWW7\",\"source\":\"UniProtKB\"}],\"value\":\"1.3.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Geissoschizine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsGS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"W8JWW7\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:11378\"}}],\"reaction\":{\"ecNumber\":\"1.3.1.36\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"W8JWW7\",\"source\":\"UniProtKB\"}],\"name\":\"(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:11376\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17037\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17294\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ1.json",
  "source_sha256": "6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5",
  "retrieved_utc": "2026-11-02T04:29:29.884516+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61919.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"BIOTECHNOLOGY\",\"TISSUE SPECIFICITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   GS_RAUSE                Reviewed;         365 AA.\nAC   P0DXJ1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};\nDE            Short=RsGS {ECO:0000303|PubMed:38212296};\nDE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};\nGN   Name=GS {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};\nDE            Short=RsGS {ECO:0000303|PubMed:38212296};\nDE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "source_locator": "lines 16-22",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WKU61919.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, BIOTECHNOLOGY, TISSUE SPECIFICITY,\nRP   AND PATHWAY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2",
  "source_sha256": "7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7",
  "retrieved_utc": "2026-11-02T04:29:32.265438+00:00",
  "source_locator": "lines 31-37",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine +\nCC         NADPH; Xref=Rhea:RHEA:11376, ChEBI:CHEBI:17037, ChEBI:CHEBI:17294,\nCC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.3.1.36;\nCC         Evidence={ECO:0000250|UniProtKB:W8JWW7};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:11378;\nCC         Evidence={ECO:0000250|UniProtKB:W8JWW7};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
