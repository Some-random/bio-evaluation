# catalytic_activity_0040

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0040.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKEKGEEKMNDSRKITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRKIERIEKGDSYIPDVSSNVLKDLVQNKQLVVYTPHTGIEEFQNSEYVIVTVPTPINKQKEPDLSALIAASHYIKQNLQAGQTFIFESSTYPGTLEEVIIPIIAQSGKEVGKDYYIGYSPERIDPANQQYTVQTIPKVISGQTERCKQQVQKLYSTIFDTVVPVSSPKVAEMCKLFENIQRLVNISLVNELNILCEKLGIDFREALEAAATKPFGFTPYWPGPGIGGHCIPVDPLYFQWKARQLGQSSQLIEVAHMINEKMPQQIVTQVKELSAPPGTVFLIGIAYKKDVNDLRESPALPIIELLVNEGYKVQYHDPYISSAKIGDKIYDSIPLKKKTLEKADCILIVTDHSNIDWNICKGMKHVIDTRGVLKKVSA

[Multiple Choices]
A. deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+)
B. UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)
C. deacetylisoipecoside + S-adenosyl-L-methionine = 6-O-methyldeacetylisoipecoside + S-adenosyl-L-homocysteine + H(+)
D. L-homocysteine + glycine betaine = N,N-dimethylglycine + L-methionine
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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence is annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase, and the source records the reaction in choice B with experimental evidence cited (ECO:0000269, PubMed 20529859).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 423-aa sequence has a glycine-rich region consistent with dinucleotide binding and a cysteine-containing motif (WPGPGIGGHC), supporting an NAD-dependent sugar oxidoreductase family inference. Among the choices, B is the NAD-dependent oxidation of a UDP-linked sugar to a uronic acid; A is ATP-dependent amide formation, while C and D are methyl-transfer reactions. This supports B as a meaningful family-level inference, though the sequence alone does not prove the precise substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable enzyme-family and reaction-class knowledge gives a credible basis for distinguishing B from these alternatives without needing the target's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct reaction classes, and the sequence-based oxidoreductase inference points to B.


### Important caveats

- The database annotations are reviewer-only evidence, not original model inputs.
- The cited experimental evidence supports the reaction annotation, but the underlying primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 423-aa sequence has a glycine-rich region consistent with dinucleotide binding and a cysteine-containing motif (WPGPGIGGHC), supporting an NAD-dependent sugar oxidoreductase family inference. Among the choices, B is the NAD-dependent oxidation of a UDP-linked sugar to a uronic acid; A is ATP-dependent amide formation, while C and D are methyl-transfer reactions. This supports B as a meaningful family-level inference, though the sequence alone does not prove the precise substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family and reaction-class knowledge gives a credible basis for distinguishing B from these alternatives without needing the target's database record."
  },
  "case_id": "catalytic_activity_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase, and the source records the reaction in choice B with experimental evidence cited (ECO:0000269, PubMed 20529859)."
  },
  "important_caveats": [
    "The database annotations are reviewer-only evidence, not original model inputs.",
    "The cited experimental evidence supports the reaction annotation, but the underlying primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes, and the sequence-based oxidoreductase inference points to B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase, and the source records the reaction in choice B with experimental evidence cited (ECO:0000269, PubMed 20529859).",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 423-aa sequence has a glycine-rich region consistent with dinucleotide binding and a cysteine-containing motif (WPGPGIGGHC), supporting an NAD-dependent sugar oxidoreductase family inference. Among the choices, B is the NAD-dependent oxidation of a UDP-linked sugar to a uronic acid; A is ATP-dependent amide formation, while C and D are methyl-transfer reactions. This supports B as a meaningful family-level inference, though the sequence alone does not prove the precise substrate.",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family and reaction-class knowledge gives a credible basis for distinguishing B from these alternatives without needing the target's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes, and the sequence-based oxidoreductase inference points to B."
  },
  "important_caveats": [
    "The database annotations are reviewer-only evidence, not original model inputs.",
    "The cited experimental evidence supports the reaction annotation, but the underlying primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A7GKX6 (sequence matched, 423 aa) annotates this protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136) with the exact reaction in choice B. The evidence code ECO:0000269 (inferred from direct assay) from PubMed:20529859 indicates experimental confirmation of catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region 'ITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRK' contains a classic Rossmann-fold NAD-binding motif (GxGxVG pattern: GLGYVG), which is the hallmark of NAD-dependent oxidoreductases/dehydrogenases. Among the four choices: (A) is a synthetase (EC 6.3.5.1) that would require glutaminase and ATP-binding domains rather than a dehydrogenase Rossmann fold; (C) and (D) are methyltransferases requiring SAM-binding motifs, not NAD-binding Rossmann folds; (B) is the only NAD-dependent dehydrogenase reaction. Recognizing the Rossmann fold as diagnostic of NAD-dependent oxidation/reduction chemistry, and knowing that UDP-sugar dehydrogenases (e.g., UDP-glucose 6-dehydrogenase, EC 1.1.1.22) share this architecture, allows a knowledgeable model to select B over the synthetase and methyltransferase alternatives. The ~423 aa length is also consistent with the UDP-sugar dehydrogenase family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold NAD-binding motif is one of the most widely recognized sequence features in biochemistry, transferable across all NAD-dependent dehydrogenases. It meaningfully eliminates the methyltransferase options (C, D) and the synthetase option (A), leaving B as the only NAD-dependent dehydrogenase among the choices. This is standard protein-family-level inference, not target-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Rossmann-fold NAD-binding motif clearly indicates an NAD-dependent dehydrogenase. Only choice B fits this category. Choices A (synthetase), C (O-methyltransferase), and D (methyltransferase) require entirely different cofactor architectures (ATP/glutamine, SAM, betaine) not suggested by the sequence motifs present.


### Important caveats

- The Rossmann fold motif narrows the answer to a dehydrogenase but does not by itself prove the specific UDP-GlcNAc substrate; however, among the offered choices, only B is a dehydrogenase, making the discrimination sufficient.
- The experimental evidence (ECO:0000269, PubMed:20529859) confirms the annotation, but the model is not expected to know this specific paper.
- The sequence is from Bacillus cytotoxicus; family-level homology to better-characterized UDP-sugar dehydrogenases (e.g., E. coli Ugd) supports the inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'ITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRK' contains a classic Rossmann-fold NAD-binding motif (GxGxVG pattern: GLGYVG), which is the hallmark of NAD-dependent oxidoreductases/dehydrogenases. Among the four choices: (A) is a synthetase (EC 6.3.5.1) that would require glutaminase and ATP-binding domains rather than a dehydrogenase Rossmann fold; (C) and (D) are methyltransferases requiring SAM-binding motifs, not NAD-binding Rossmann folds; (B) is the only NAD-dependent dehydrogenase reaction. Recognizing the Rossmann fold as diagnostic of NAD-dependent oxidation/reduction chemistry, and knowing that UDP-sugar dehydrogenases (e.g., UDP-glucose 6-dehydrogenase, EC 1.1.1.22) share this architecture, allows a knowledgeable model to select B over the synthetase and methyltransferase alternatives. The ~423 aa length is also consistent with the UDP-sugar dehydrogenase family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif is one of the most widely recognized sequence features in biochemistry, transferable across all NAD-dependent dehydrogenases. It meaningfully eliminates the methyltransferase options (C, D) and the synthetase option (A), leaving B as the only NAD-dependent dehydrogenase among the choices. This is standard protein-family-level inference, not target-specific lookup."
  },
  "case_id": "catalytic_activity_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A7GKX6 (sequence matched, 423 aa) annotates this protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136) with the exact reaction in choice B. The evidence code ECO:0000269 (inferred from direct assay) from PubMed:20529859 indicates experimental confirmation of catalytic activity."
  },
  "important_caveats": [
    "The Rossmann fold motif narrows the answer to a dehydrogenase but does not by itself prove the specific UDP-GlcNAc substrate; however, among the offered choices, only B is a dehydrogenase, making the discrimination sufficient.",
    "The experimental evidence (ECO:0000269, PubMed:20529859) confirms the annotation, but the model is not expected to know this specific paper.",
    "The sequence is from Bacillus cytotoxicus; family-level homology to better-characterized UDP-sugar dehydrogenases (e.g., E. coli Ugd) supports the inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold NAD-binding motif clearly indicates an NAD-dependent dehydrogenase. Only choice B fits this category. Choices A (synthetase), C (O-methyltransferase), and D (methyltransferase) require entirely different cofactor architectures (ATP/glutamine, SAM, betaine) not suggested by the sequence motifs present."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A7GKX6 (sequence matched, 423 aa) annotates this protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136) with the exact reaction in choice B. The evidence code ECO:0000269 (inferred from direct assay) from PubMed:20529859 indicates experimental confirmation of catalytic activity.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region 'ITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRK' contains a classic Rossmann-fold NAD-binding motif (GxGxVG pattern: GLGYVG), which is the hallmark of NAD-dependent oxidoreductases/dehydrogenases. Among the four choices: (A) is a synthetase (EC 6.3.5.1) that would require glutaminase and ATP-binding domains rather than a dehydrogenase Rossmann fold; (C) and (D) are methyltransferases requiring SAM-binding motifs, not NAD-binding Rossmann folds; (B) is the only NAD-dependent dehydrogenase reaction. Recognizing the Rossmann fold as diagnostic of NAD-dependent oxidation/reduction chemistry, and knowing that UDP-sugar dehydrogenases (e.g., UDP-glucose 6-dehydrogenase, EC 1.1.1.22) share this architecture, allows a knowledgeable model to select B over the synthetase and methyltransferase alternatives. The ~423 aa length is also consistent with the UDP-sugar dehydrogenase family.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif is one of the most widely recognized sequence features in biochemistry, transferable across all NAD-dependent dehydrogenases. It meaningfully eliminates the methyltransferase options (C, D) and the synthetase option (A), leaving B as the only NAD-dependent dehydrogenase among the choices. This is standard protein-family-level inference, not target-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold NAD-binding motif clearly indicates an NAD-dependent dehydrogenase. Only choice B fits this category. Choices A (synthetase), C (O-methyltransferase), and D (methyltransferase) require entirely different cofactor architectures (ATP/glutamine, SAM, betaine) not suggested by the sequence motifs present."
  },
  "important_caveats": [
    "The Rossmann fold motif narrows the answer to a dehydrogenase but does not by itself prove the specific UDP-GlcNAc substrate; however, among the offered choices, only B is a dehydrogenase, making the discrimination sufficient.",
    "The experimental evidence (ECO:0000269, PubMed:20529859) confirms the annotation, but the model is not expected to know this specific paper.",
    "The sequence is from Bacillus cytotoxicus; family-level homology to better-characterized UDP-sugar dehydrogenases (e.g., E. coli Ugd) supports the inference."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 423,
  "benchmark_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "current_entry_audit": {
    "entryVersion": 98,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-09-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 423,
  "current_source_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 96,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A7GKX6",
  "selected_historical_entry_version": 96,
  "selected_historical_record_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "selected_historical_source_sequence_length": 423,
  "selected_historical_source_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "selected_historical_version": {
    "accession": "A7GKX6",
    "database": "Swiss-Prot",
    "entryVersion": 96,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UGNAD_BACCN",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A7GKX6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":98,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-09-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\",\"Bacillus cereus group\"],\"scientificName\":\"Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98)\",\"taxonId\":315749}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.136\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-N-acetyl-D-glucosamine 6-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAc 6-dehydrogenase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13326\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.136\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13325\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65040\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Gu X.\",\"Glushka J.\",\"Lee S.G.\",\"Bar-Peled M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20529859\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m110.125872\"}],\"citationType\":\"journal article\",\"firstPage\":\"24825\",\"id\":\"20529859\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"24833\",\"publicationDate\":\"2010\",\"title\":\"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADE43879.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H1",
  "excerpt": "ID   UGNAD_BACCN             Reviewed;         423 AA.\nAC   A7GKX6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-SEP-2007, sequence version 1.\nDT   28-JAN-2026, entry version 96.\nDE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:20529859};\nGN   Name=UGlcNAcDH {ECO:0000303|PubMed:20529859};\nGN   OrderedLocusNames=Bcer98_0429 {ECO:0000312|EMBL:ABS20784.1};\nOS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;\nOC   Bacillus cereus group.\nOX   NCBI_TaxID=315749;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:ADE43879.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;\nRX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;\nRA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;\nRT   \"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the\nRT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\";\nRL   J. Biol. Chem. 285:24825-24833(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-\nCC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);\nCC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,\nCC         ChEBI:CHEBI:65040; EC=1.1.1.136;\nCC         Evidence={ECO:0000269|PubMed:20529859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;\nCC         Evidence={ECO:0000269|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 40. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
