# EC_number_0131: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0131.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 4.1.1.128

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MKKRCLITGGAGFIGSHLAEELVKRGHPVTIVDNFYKGKSKYHEELTGNIPIIPISILDKNSMHELVNQHDVVFHLAAILGVKTTMEKSIELIETNFDGTRNILQAALKGKKKVIFASTSEVYGKGTPPFSEDDDRLYGATSKIRWSYAICKTLEETLCLGYALQGLPVTIVRYFNIYGPRAKDGPYAGVIPRFIRAALQGDDLLVYGDGKQTRCFTYVSDAVEATIAAMDEKVNGEIINIGSEDEKSIQEVAQDIHQLTHSSSKIVHVPFEKVYPHGFEEIPNRKPDVTKLKEMCQFHPNVSWEQGLKETIQWFREIEND

[Multiple Choices]
A. 4.1.1.36
B. 5.6.1.1
C. 4.1.1.128
D. 1.14.14.154
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

> The supplied 321-aa sequence exactly matches the UniProt sequence for A7GKX7. UniProt assigns it EC 4.1.1.128 and links the catalytic-activity annotation to PubMed 20529859 with experimental evidence code ECO:0000269. The reported reaction is decarboxylation of UDP-2-acetamido-2-deoxy-alpha-D-glucuronate to UDP-N-acetyl-alpha-D-xylosamine and CO2, supporting choice C.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently specific substrate or reaction context to distinguish this exact decarboxylase EC number from the other enzyme classes listed.


**Missing item-specific fact**

> The protein-specific functional identification and catalytic reaction—UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase activity—are needed to select EC 4.1.1.128.


**Reason**

> The EC number specifies a particular catalyzed reaction. Recognizing the sequence or relying on general sequence heuristics would not establish that exact activity without protein-specific functional information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence has a supported annotation for choice C; the evidence provided does not support another listed choice.


### Important caveats

- The annotation and sequence-match evidence are reviewer-only and were not supplied to the evaluated model.
- The EC assignment is linked in UniProt to experimental evidence from PubMed 20529859, but the primary paper was not independently retrieved and validated here.
- The historical UniProt sequence matches exactly; the author's actual source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific substrate or reaction context to distinguish this exact decarboxylase EC number from the other enzyme classes listed.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification and catalytic reaction—UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase activity—are needed to select EC 4.1.1.128.",
    "reason": "The EC number specifies a particular catalyzed reaction. Recognizing the sequence or relying on general sequence heuristics would not establish that exact activity without protein-specific functional information."
  },
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 321-aa sequence exactly matches the UniProt sequence for A7GKX7. UniProt assigns it EC 4.1.1.128 and links the catalytic-activity annotation to PubMed 20529859 with experimental evidence code ECO:0000269. The reported reaction is decarboxylation of UDP-2-acetamido-2-deoxy-alpha-D-glucuronate to UDP-N-acetyl-alpha-D-xylosamine and CO2, supporting choice C."
  },
  "important_caveats": [
    "The annotation and sequence-match evidence are reviewer-only and were not supplied to the evaluated model.",
    "The EC assignment is linked in UniProt to experimental evidence from PubMed 20529859, but the primary paper was not independently retrieved and validated here.",
    "The historical UniProt sequence matches exactly; the author's actual source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has a supported annotation for choice C; the evidence provided does not support another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 321-aa sequence exactly matches the UniProt sequence for A7GKX7. UniProt assigns it EC 4.1.1.128 and links the catalytic-activity annotation to PubMed 20529859 with experimental evidence code ECO:0000269. The reported reaction is decarboxylation of UDP-2-acetamido-2-deoxy-alpha-D-glucuronate to UDP-N-acetyl-alpha-D-xylosamine and CO2, supporting choice C.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific substrate or reaction context to distinguish this exact decarboxylase EC number from the other enzyme classes listed.",
    "missing_item_specific_fact": "The protein-specific functional identification and catalytic reaction—UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase activity—are needed to select EC 4.1.1.128.",
    "reason": "The EC number specifies a particular catalyzed reaction. Recognizing the sequence or relying on general sequence heuristics would not establish that exact activity without protein-specific functional information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has a supported annotation for choice C; the evidence provided does not support another listed choice."
  },
  "important_caveats": [
    "The annotation and sequence-match evidence are reviewer-only and were not supplied to the evaluated model.",
    "The EC assignment is linked in UniProt to experimental evidence from PubMed 20529859, but the primary paper was not independently retrieved and validated here.",
    "The historical UniProt sequence matches exactly; the author's actual source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 321-aa sequence matches UniProt entry A7GKX7 (UXNAS_BACCN) exactly (SHA256 confirmed). The entry annotates this protein as EC 4.1.1.128 (UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase) with evidence code ECO:0000269 (experimental evidence) from PubMed:20529859 (Gu et al., J. Biol. Chem. 2010). The catalytic reaction (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ → UDP-N-acetyl-alpha-D-xylosamine + CO2) is experimentally characterized. The sequence is 321 aa, matching the benchmark sequence length.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal region contains a Rossmann-like nucleotide-binding motif (GGAGFIGSHL…VTIVDNFYKG) and a GDGKQ motif characteristic of UDP-sugar-binding proteins, which could help a knowledgeable reader narrow the class toward nucleotide-sugar enzymes and away from a generic monooxygenase (D: 1.14.14.154) or isomerase (B: 5.6.1.1). However, both A (4.1.1.36) and C (4.1.1.128) are carboxy-lyases (decarboxylases) acting on UDP-sugar substrates. Distinguishing these two specific 4-digit EC numbers requires knowing the exact substrate (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate for 128 vs. whatever 4.1.1.36 acts on), which is not encoded in any generalizable sequence motif visible in the input.


**Missing item-specific fact**

> The specific substrate identity and reaction chemistry that differentiate EC 4.1.1.36 from EC 4.1.1.128, which must be looked up or memorized from the UniProt/database entry or the primary literature (PubMed:20529859). No sequence-derived feature in the provided 321-aa chain uniquely identifies the glucuronate→xylosamine decarboxylation over another 4.1.1.x decarboxylation.


**Reason**

> While sequence features (UDP-binding motifs, overall fold) may plausibly eliminate B and D, the critical discrimination between A and C—both 4.1.1.x decarboxylases—cannot be achieved through general biological reasoning from the sequence alone. It requires the item-specific fact of which particular UDP-sugar decarboxylation this enzyme catalyzes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (4.1.1.36) and C (4.1.1.128) belong to the same EC 4.1.1.x subclass (carboxy-lyases/decarboxylases). Without the specific substrate information, a model relying on sequence-level reasoning cannot confidently prefer one over the other. B (isomerase) and D (monooxygenase) are more readily eliminated by the UDP-binding motifs and overall architecture.


### Important caveats

- The UniProt annotation for EC 4.1.1.128 carries experimental evidence (ECO:0000269, PubMed:20529859), not merely computational inference.
- The identity of EC 4.1.1.36 (the distractor) was not independently verified in the supplied evidence; its exact reaction is not provided in the reviewer excerpts.
- The sequence was first released in 2007 but the Swiss-Prot entry was only created in 2025-02-05; the benchmark author's source snapshot is unknown.
- The Rossmann-like N-terminal motif could superficially mislead toward oxidoreductase assignments, adding noise to any sequence-based reasoning path.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a Rossmann-like nucleotide-binding motif (GGAGFIGSHL…VTIVDNFYKG) and a GDGKQ motif characteristic of UDP-sugar-binding proteins, which could help a knowledgeable reader narrow the class toward nucleotide-sugar enzymes and away from a generic monooxygenase (D: 1.14.14.154) or isomerase (B: 5.6.1.1). However, both A (4.1.1.36) and C (4.1.1.128) are carboxy-lyases (decarboxylases) acting on UDP-sugar substrates. Distinguishing these two specific 4-digit EC numbers requires knowing the exact substrate (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate for 128 vs. whatever 4.1.1.36 acts on), which is not encoded in any generalizable sequence motif visible in the input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity and reaction chemistry that differentiate EC 4.1.1.36 from EC 4.1.1.128, which must be looked up or memorized from the UniProt/database entry or the primary literature (PubMed:20529859). No sequence-derived feature in the provided 321-aa chain uniquely identifies the glucuronate→xylosamine decarboxylation over another 4.1.1.x decarboxylation.",
    "reason": "While sequence features (UDP-binding motifs, overall fold) may plausibly eliminate B and D, the critical discrimination between A and C—both 4.1.1.x decarboxylases—cannot be achieved through general biological reasoning from the sequence alone. It requires the item-specific fact of which particular UDP-sugar decarboxylation this enzyme catalyzes."
  },
  "case_id": "EC_number_0131",
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
    "reason": "The supplied 321-aa sequence matches UniProt entry A7GKX7 (UXNAS_BACCN) exactly (SHA256 confirmed). The entry annotates this protein as EC 4.1.1.128 (UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase) with evidence code ECO:0000269 (experimental evidence) from PubMed:20529859 (Gu et al., J. Biol. Chem. 2010). The catalytic reaction (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ → UDP-N-acetyl-alpha-D-xylosamine + CO2) is experimentally characterized. The sequence is 321 aa, matching the benchmark sequence length."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.1.1.128 carries experimental evidence (ECO:0000269, PubMed:20529859), not merely computational inference.",
    "The identity of EC 4.1.1.36 (the distractor) was not independently verified in the supplied evidence; its exact reaction is not provided in the reviewer excerpts.",
    "The sequence was first released in 2007 but the Swiss-Prot entry was only created in 2025-02-05; the benchmark author's source snapshot is unknown.",
    "The Rossmann-like N-terminal motif could superficially mislead toward oxidoreductase assignments, adding noise to any sequence-based reasoning path."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (4.1.1.36) and C (4.1.1.128) belong to the same EC 4.1.1.x subclass (carboxy-lyases/decarboxylases). Without the specific substrate information, a model relying on sequence-level reasoning cannot confidently prefer one over the other. B (isomerase) and D (monooxygenase) are more readily eliminated by the UDP-binding motifs and overall architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 321-aa sequence matches UniProt entry A7GKX7 (UXNAS_BACCN) exactly (SHA256 confirmed). The entry annotates this protein as EC 4.1.1.128 (UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase) with evidence code ECO:0000269 (experimental evidence) from PubMed:20529859 (Gu et al., J. Biol. Chem. 2010). The catalytic reaction (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ → UDP-N-acetyl-alpha-D-xylosamine + CO2) is experimentally characterized. The sequence is 321 aa, matching the benchmark sequence length.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal region contains a Rossmann-like nucleotide-binding motif (GGAGFIGSHL…VTIVDNFYKG) and a GDGKQ motif characteristic of UDP-sugar-binding proteins, which could help a knowledgeable reader narrow the class toward nucleotide-sugar enzymes and away from a generic monooxygenase (D: 1.14.14.154) or isomerase (B: 5.6.1.1). However, both A (4.1.1.36) and C (4.1.1.128) are carboxy-lyases (decarboxylases) acting on UDP-sugar substrates. Distinguishing these two specific 4-digit EC numbers requires knowing the exact substrate (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate for 128 vs. whatever 4.1.1.36 acts on), which is not encoded in any generalizable sequence motif visible in the input.",
    "missing_item_specific_fact": "The specific substrate identity and reaction chemistry that differentiate EC 4.1.1.36 from EC 4.1.1.128, which must be looked up or memorized from the UniProt/database entry or the primary literature (PubMed:20529859). No sequence-derived feature in the provided 321-aa chain uniquely identifies the glucuronate→xylosamine decarboxylation over another 4.1.1.x decarboxylation.",
    "reason": "While sequence features (UDP-binding motifs, overall fold) may plausibly eliminate B and D, the critical discrimination between A and C—both 4.1.1.x decarboxylases—cannot be achieved through general biological reasoning from the sequence alone. It requires the item-specific fact of which particular UDP-sugar decarboxylation this enzyme catalyzes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (4.1.1.36) and C (4.1.1.128) belong to the same EC 4.1.1.x subclass (carboxy-lyases/decarboxylases). Without the specific substrate information, a model relying on sequence-level reasoning cannot confidently prefer one over the other. B (isomerase) and D (monooxygenase) are more readily eliminated by the UDP-binding motifs and overall architecture."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.1.1.128 carries experimental evidence (ECO:0000269, PubMed:20529859), not merely computational inference.",
    "The identity of EC 4.1.1.36 (the distractor) was not independently verified in the supplied evidence; its exact reaction is not provided in the reviewer excerpts.",
    "The sequence was first released in 2007 but the Swiss-Prot entry was only created in 2025-02-05; the benchmark author's source snapshot is unknown.",
    "The Rossmann-like N-terminal motif could superficially mislead toward oxidoreductase assignments, adding noise to any sequence-based reasoning path."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches the cited UniProt entry, whose EC 4.1.1.128 annotation and catalytic reaction are supported there by experimental-evidence codes citing PubMed 20529859. This supports the key for the supplied sequence, though the paper itself was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a glycine-rich dinucleotide-binding motif (ITGGAGF...), consistent with an NAD-dependent nucleotide-sugar enzyme. Transferable knowledge of this enzyme family supports a nucleotide-sugar decarboxylase over the isomerase and monooxygenase choices, and makes the offered UDP-sugar decarboxylase EC 4.1.1.128 a credible best match. This is a family-level inference, not a definitive sequence-only proof of substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable cofactor-binding feature and the associated nucleotide-sugar enzyme family provide a meaningful basis for choosing among the offered reaction classes without relying on the target's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based family inference favors C among the supplied options; no second option is comparably supported.


### Important caveats

- The Rossmann-like motif supports an enzyme-family inference but does not alone establish the exact substrate or EC number.
- Reviewer-only source evidence supports the key but was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a glycine-rich dinucleotide-binding motif (ITGGAGF...), consistent with an NAD-dependent nucleotide-sugar enzyme. Transferable knowledge of this enzyme family supports a nucleotide-sugar decarboxylase over the isomerase and monooxygenase choices, and makes the offered UDP-sugar decarboxylase EC 4.1.1.128 a credible best match. This is a family-level inference, not a definitive sequence-only proof of substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable cofactor-binding feature and the associated nucleotide-sugar enzyme family provide a meaningful basis for choosing among the offered reaction classes without relying on the target's recorded annotation."
  },
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, whose EC 4.1.1.128 annotation and catalytic reaction are supported there by experimental-evidence codes citing PubMed 20529859. This supports the key for the supplied sequence, though the paper itself was not independently reviewed here."
  },
  "important_caveats": [
    "The Rossmann-like motif supports an enzyme-family inference but does not alone establish the exact substrate or EC number.",
    "Reviewer-only source evidence supports the key but was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors C among the supplied options; no second option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, whose EC 4.1.1.128 annotation and catalytic reaction are supported there by experimental-evidence codes citing PubMed 20529859. This supports the key for the supplied sequence, though the paper itself was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a glycine-rich dinucleotide-binding motif (ITGGAGF...), consistent with an NAD-dependent nucleotide-sugar enzyme. Transferable knowledge of this enzyme family supports a nucleotide-sugar decarboxylase over the isomerase and monooxygenase choices, and makes the offered UDP-sugar decarboxylase EC 4.1.1.128 a credible best match. This is a family-level inference, not a definitive sequence-only proof of substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable cofactor-binding feature and the associated nucleotide-sugar enzyme family provide a meaningful basis for choosing among the offered reaction classes without relying on the target's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors C among the supplied options; no second option is comparably supported."
  },
  "important_caveats": [
    "The Rossmann-like motif supports an enzyme-family inference but does not alone establish the exact substrate or EC number.",
    "Reviewer-only source evidence supports the key but was not part of the original model input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms UniProt entry A7GKX7 (UXNAS_BACCN) with sequence match (321 aa, SHA256 matched). The EC number 4.1.1.128 is annotated with experimental evidence (ECO:0000269, PubMed:20529859, Gu et al. 2010 JBC). The catalytic reaction is UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ = UDP-N-acetyl-alpha-D-xylosamine + CO2, confirmed by Rhea cross-reference. The sequence comparison is 'matched' for both current and historical records.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The Rossmann-fold motif 'GGAGFIGS' at the N-terminus indicates a nucleotide-binding fold, which reasonably eliminates option D (1.14.14.154, a cytochrome P450 monooxygenase with a completely different heme-binding fold) and option B (5.6.1.1, an isomerase category not associated with Rossmann folds). This narrows the choice to A (4.1.1.36, UDP-glucuronate decarboxylase) or C (4.1.1.128, UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase). Both are carboxy-lyases (EC 4.1.1.x) acting on UDP-sugar acids, potentially sharing similar overall folds and UDP-binding motifs. The critical distinction—whether the enzyme accommodates an N-acetyl group on C2 of the sugar (4.1.1.128) or acts on unsubstituted UDP-glucuronate (4.1.1.36)—is a subtle active-site specificity difference not discernible from the sequence alone. No obvious sequence motif in the provided 321-aa sequence specifically encodes N-acetyl recognition versus its absence.


**Missing item-specific fact**

> The specific substrate-binding active-site residues that distinguish UDP-glucuronate decarboxylase (4.1.1.36) from UDP-N-acetyl-glucosaminuronate decarboxylase (4.1.1.128), or the taxonomic/family context (Bacillus cytotoxicus, characterized in 2010) that identifies this particular enzyme as the N-acetyl-accepting variant rather than the classical UDP-glucuronate decarboxylase.


**Reason**

> While the Rossmann fold and decarboxylase character allow elimination of B and D, the remaining choice between A and C requires knowledge of the precise substrate specificity of these two closely related UDP-sugar acid decarboxylases. Both catalyze decarboxylation of UDP-linked sugar acids, likely share structural folds, and differ only in the presence/absence of an N-acetyl substituent on the substrate. No transferable family-level sequence feature in the provided input meaningfully distinguishes the N-acetyl-accepting variant (C) from the non-acetylated substrate variant (A) without recalling the specific annotation or experimental characterization of this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (4.1.1.36) and C (4.1.1.128) are UDP-sugar acid decarboxylases (EC 4.1.1.x) that could plausibly share a Rossmann-like nucleotide-binding fold. From the sequence alone, without specific knowledge of the N-acetyl substrate recognition, both remain viable. The distinction is subtle and not resolvable by general family-level inference.


### Important caveats

- The EC 4.1.1.128 annotation is based on experimental evidence (ECO:0000269, PubMed:20529859), not computational prediction.
- EC 4.1.1.128 was established relatively recently (2010 characterization), making it less likely to be encoded in a model's training data compared to the more established 4.1.1.36.
- The Rossmann fold 'GGAGFIGS' in a decarboxylase context is somewhat unusual and could in principle be used to argue against a classical dehydrogenase-like 4.1.1.36 if one knew that plant UGDs lack this specific fold variant, but this is very specific knowledge.
- Option B (5.6.1.1) appears to be an unusual or possibly non-standard EC number, serving as an easy distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The Rossmann-fold motif 'GGAGFIGS' at the N-terminus indicates a nucleotide-binding fold, which reasonably eliminates option D (1.14.14.154, a cytochrome P450 monooxygenase with a completely different heme-binding fold) and option B (5.6.1.1, an isomerase category not associated with Rossmann folds). This narrows the choice to A (4.1.1.36, UDP-glucuronate decarboxylase) or C (4.1.1.128, UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase). Both are carboxy-lyases (EC 4.1.1.x) acting on UDP-sugar acids, potentially sharing similar overall folds and UDP-binding motifs. The critical distinction—whether the enzyme accommodates an N-acetyl group on C2 of the sugar (4.1.1.128) or acts on unsubstituted UDP-glucuronate (4.1.1.36)—is a subtle active-site specificity difference not discernible from the sequence alone. No obvious sequence motif in the provided 321-aa sequence specifically encodes N-acetyl recognition versus its absence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate-binding active-site residues that distinguish UDP-glucuronate decarboxylase (4.1.1.36) from UDP-N-acetyl-glucosaminuronate decarboxylase (4.1.1.128), or the taxonomic/family context (Bacillus cytotoxicus, characterized in 2010) that identifies this particular enzyme as the N-acetyl-accepting variant rather than the classical UDP-glucuronate decarboxylase.",
    "reason": "While the Rossmann fold and decarboxylase character allow elimination of B and D, the remaining choice between A and C requires knowledge of the precise substrate specificity of these two closely related UDP-sugar acid decarboxylases. Both catalyze decarboxylation of UDP-linked sugar acids, likely share structural folds, and differ only in the presence/absence of an N-acetyl substituent on the substrate. No transferable family-level sequence feature in the provided input meaningfully distinguishes the N-acetyl-accepting variant (C) from the non-acetylated substrate variant (A) without recalling the specific annotation or experimental characterization of this protein."
  },
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms UniProt entry A7GKX7 (UXNAS_BACCN) with sequence match (321 aa, SHA256 matched). The EC number 4.1.1.128 is annotated with experimental evidence (ECO:0000269, PubMed:20529859, Gu et al. 2010 JBC). The catalytic reaction is UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ = UDP-N-acetyl-alpha-D-xylosamine + CO2, confirmed by Rhea cross-reference. The sequence comparison is 'matched' for both current and historical records."
  },
  "important_caveats": [
    "The EC 4.1.1.128 annotation is based on experimental evidence (ECO:0000269, PubMed:20529859), not computational prediction.",
    "EC 4.1.1.128 was established relatively recently (2010 characterization), making it less likely to be encoded in a model's training data compared to the more established 4.1.1.36.",
    "The Rossmann fold 'GGAGFIGS' in a decarboxylase context is somewhat unusual and could in principle be used to argue against a classical dehydrogenase-like 4.1.1.36 if one knew that plant UGDs lack this specific fold variant, but this is very specific knowledge.",
    "Option B (5.6.1.1) appears to be an unusual or possibly non-standard EC number, serving as an easy distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (4.1.1.36) and C (4.1.1.128) are UDP-sugar acid decarboxylases (EC 4.1.1.x) that could plausibly share a Rossmann-like nucleotide-binding fold. From the sequence alone, without specific knowledge of the N-acetyl substrate recognition, both remain viable. The distinction is subtle and not resolvable by general family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms UniProt entry A7GKX7 (UXNAS_BACCN) with sequence match (321 aa, SHA256 matched). The EC number 4.1.1.128 is annotated with experimental evidence (ECO:0000269, PubMed:20529859, Gu et al. 2010 JBC). The catalytic reaction is UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ = UDP-N-acetyl-alpha-D-xylosamine + CO2, confirmed by Rhea cross-reference. The sequence comparison is 'matched' for both current and historical records.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The Rossmann-fold motif 'GGAGFIGS' at the N-terminus indicates a nucleotide-binding fold, which reasonably eliminates option D (1.14.14.154, a cytochrome P450 monooxygenase with a completely different heme-binding fold) and option B (5.6.1.1, an isomerase category not associated with Rossmann folds). This narrows the choice to A (4.1.1.36, UDP-glucuronate decarboxylase) or C (4.1.1.128, UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase). Both are carboxy-lyases (EC 4.1.1.x) acting on UDP-sugar acids, potentially sharing similar overall folds and UDP-binding motifs. The critical distinction—whether the enzyme accommodates an N-acetyl group on C2 of the sugar (4.1.1.128) or acts on unsubstituted UDP-glucuronate (4.1.1.36)—is a subtle active-site specificity difference not discernible from the sequence alone. No obvious sequence motif in the provided 321-aa sequence specifically encodes N-acetyl recognition versus its absence.",
    "missing_item_specific_fact": "The specific substrate-binding active-site residues that distinguish UDP-glucuronate decarboxylase (4.1.1.36) from UDP-N-acetyl-glucosaminuronate decarboxylase (4.1.1.128), or the taxonomic/family context (Bacillus cytotoxicus, characterized in 2010) that identifies this particular enzyme as the N-acetyl-accepting variant rather than the classical UDP-glucuronate decarboxylase.",
    "reason": "While the Rossmann fold and decarboxylase character allow elimination of B and D, the remaining choice between A and C requires knowledge of the precise substrate specificity of these two closely related UDP-sugar acid decarboxylases. Both catalyze decarboxylation of UDP-linked sugar acids, likely share structural folds, and differ only in the presence/absence of an N-acetyl substituent on the substrate. No transferable family-level sequence feature in the provided input meaningfully distinguishes the N-acetyl-accepting variant (C) from the non-acetylated substrate variant (A) without recalling the specific annotation or experimental characterization of this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (4.1.1.36) and C (4.1.1.128) are UDP-sugar acid decarboxylases (EC 4.1.1.x) that could plausibly share a Rossmann-like nucleotide-binding fold. From the sequence alone, without specific knowledge of the N-acetyl substrate recognition, both remain viable. The distinction is subtle and not resolvable by general family-level inference."
  },
  "important_caveats": [
    "The EC 4.1.1.128 annotation is based on experimental evidence (ECO:0000269, PubMed:20529859), not computational prediction.",
    "EC 4.1.1.128 was established relatively recently (2010 characterization), making it less likely to be encoded in a model's training data compared to the more established 4.1.1.36.",
    "The Rossmann fold 'GGAGFIGS' in a decarboxylase context is somewhat unusual and could in principle be used to argue against a classical dehydrogenase-like 4.1.1.36 if one knew that plant UGDs lack this specific fold variant, but this is very specific knowledge.",
    "Option B (5.6.1.1) appears to be an unusual or possibly non-standard EC number, serving as an easy distractor."
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
  "requested_accession": "A7GKX7",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "benchmark_sequence_length": 321,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 96,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-09-11",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "current_source_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "current_source_sequence_length": 321,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 94,
  "selected_historical_version": {
    "accession": "A7GKX7",
    "database": "Swiss-Prot",
    "entryVersion": 94,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UXNAS_BACCN",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "selected_historical_source_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "selected_historical_source_sequence_length": 321,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 94,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A7GKX7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":96,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-09-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\",\"Bacillus cereus group\"],\"scientificName\":\"Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98)\",\"taxonId\":315749}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-XylNAc synthase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.128\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAcA decarboxylase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81488\"}}],\"reaction\":{\"ecNumber\":\"4.1.1.128\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"name\":\"UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81487\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65040\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231888\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Gu X.\",\"Glushka J.\",\"Lee S.G.\",\"Bar-Peled M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20529859\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m110.125872\"}],\"citationType\":\"journal article\",\"firstPage\":\"24825\",\"id\":\"20529859\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"24833\",\"publicationDate\":\"2010\",\"title\":\"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADE43880.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   UXNAS_BACCN             Reviewed;         321 AA.\nAC   A7GKX7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-SEP-2007, sequence version 1.\nDT   28-JAN-2026, entry version 94.\nDE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};\nDE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};\nDE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};\nDE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};\nGN   Name=UXNAcS {ECO:0000303|PubMed:20529859};\nGN   OrderedLocusNames=Bcer98_0430 {ECO:0000312|EMBL:ABS20785.1};\nOS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;\nOC   Bacillus cereus group.\nOX   NCBI_TaxID=315749;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 94,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};\nDE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};\nDE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};\nDE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 94,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "source_locator": "lines 27-35",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:ADE43880.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;\nRX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;\nRA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;\nRT   \"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the\nRT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\";\nRL   J. Biol. Chem. 285:24825-24833(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 94,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "source_locator": "lines 42-49",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-\nCC         acetyl-alpha-D-xylosamine + CO2; Xref=Rhea:RHEA:81487,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:65040,\nCC         ChEBI:CHEBI:231888; EC=4.1.1.128;\nCC         Evidence={ECO:0000269|PubMed:20529859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81488;\nCC         Evidence={ECO:0000269|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 94,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
