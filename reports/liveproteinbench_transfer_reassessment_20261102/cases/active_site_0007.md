# active_site_0007: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0007.txt)

**Task:** `active_site`  
**Author key, unchanged:** **D** — Position 52 (Proton acceptor; for glutaminase activity)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ

[Multiple Choices]
A. Position 413 (Proton donor)
B. Position 327 (Proton acceptor)
C. Position 372 (Charge relay system)
D. Position 52 (Proton acceptor; for glutaminase activity)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies residue 52 as the proton acceptor for glutaminase activity. This is a HAMAP computational annotation, not direct experimental evidence in the supplied record.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a defensible way to assign the specific proton-acceptor role to residue 52 rather than to the other listed positions.


**Missing item-specific fact**

> The protein-specific annotation that residue 52 is the proton acceptor for glutaminase activity.


**Reason**

> Choosing the keyed position and role requires a protein-specific functional annotation or equivalent external knowledge; general sequence reasoning does not establish that exact catalytic assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation specifically supports option D among the listed choices.


### Important caveats

- The supporting active-site annotation is attributed to HAMAP, so it should not be described as experimentally demonstrated by this evidence.
- The reviewer-only source records an exact sequence match, including for the historical entry; the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a defensible way to assign the specific proton-acceptor role to residue 52 rather than to the other listed positions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation that residue 52 is the proton acceptor for glutaminase activity.",
    "reason": "Choosing the keyed position and role requires a protein-specific functional annotation or equivalent external knowledge; general sequence reasoning does not establish that exact catalytic assignment."
  },
  "case_id": "active_site_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 52 as the proton acceptor for glutaminase activity. This is a HAMAP computational annotation, not direct experimental evidence in the supplied record."
  },
  "important_caveats": [
    "The supporting active-site annotation is attributed to HAMAP, so it should not be described as experimentally demonstrated by this evidence.",
    "The reviewer-only source records an exact sequence match, including for the historical entry; the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation specifically supports option D among the listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 52 as the proton acceptor for glutaminase activity. This is a HAMAP computational annotation, not direct experimental evidence in the supplied record.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a defensible way to assign the specific proton-acceptor role to residue 52 rather than to the other listed positions.",
    "missing_item_specific_fact": "The protein-specific annotation that residue 52 is the proton acceptor for glutaminase activity.",
    "reason": "Choosing the keyed position and role requires a protein-specific functional annotation or equivalent external knowledge; general sequence reasoning does not establish that exact catalytic assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation specifically supports option D among the listed choices."
  },
  "important_caveats": [
    "The supporting active-site annotation is attributed to HAMAP, so it should not be described as experimentally demonstrated by this evidence.",
    "The reviewer-only source records an exact sequence match, including for the historical entry; the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0H2X6L3 (NadE, Xanthomonas campestris pv. campestris 8004) annotates position 52 as 'Proton acceptor; for glutaminase activity' (Active site feature, evidence ECO:0000255|HAMAP-Rule:MF_02090). The sequence residue at position 52 is Glu (E), consistent with the known catalytic mechanism of glutamine amidotransferases where a conserved Glu activates a water nucleophile. The annotation is computational (HAMAP-Rule inference by family similarity), not direct experimental evidence for this specific protein, but it is consistent with the well-characterized NadE catalytic triad. The distractor positions (413, 327, 372) do not correspond to any annotated active site in this entry.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly reason that the N-terminal ~200 residues constitute a glutaminase domain (Ntn-hydrolase fold) and that a Glu proton acceptor would reside there, making options B (327), C (372), and A (413) less likely as they fall in the synthetase domain. However, distinguishing position 52 specifically from the many Glu residues in the N-terminal region, or confirming its exact role as 'proton acceptor for glutaminase activity,' requires knowledge of the conserved NadE catalytic triad positions or the specific UniProt annotation.


**Missing item-specific fact**

> The exact position (52) of the catalytic Glu proton acceptor in this particular NadE sequence, and the assignment of functional roles (proton acceptor vs. nucleophile vs. 'for glutaminase activity') to positions 52, 119, and 157 respectively, as annotated by HAMAP-Rule MF_02090. Without this annotation or memorized family alignment, selecting position 52 over other Glu residues in the glutaminase domain is not achievable by general reasoning alone.


**Reason**

> While domain architecture recognition (N-terminal glutaminase vs. C-terminal synthetase) provides a weak argument against the C-terminal distractors, pinpointing position 52 as the specific proton acceptor requires item-specific annotation knowledge or memorization of the NadE family catalytic residue positions. The question's precision (exact position + exact functional label) exceeds what general biological reasoning from sequence alone can resolve.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D corresponds to an actual UniProt-annotated active site (position 52). Positions 413, 327, and 372 are not annotated as active sites in this entry. The other annotated active sites (119, 157) are not offered as options. Thus D is uniquely correct among the four choices.


### Important caveats

- The active site annotation at position 52 carries evidence code ECO:0000255 (inferred by similarity to HAMAP-Rule MF_02090), meaning it is a computational/curatorial family inference, not direct experimental characterization of this specific X. campestris protein.
- The full catalytic center of NadE involves three active-site residues (52, 119, 157); the question and answer format presents only one, which is a simplification.
- The UniProt accession A0A0H2X6L3 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must identify the protein from sequence alone.
- The protein was integrated into Swiss-Prot on 2025-02-05; if the benchmark was constructed before this date, the annotation may not have been publicly available at construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly reason that the N-terminal ~200 residues constitute a glutaminase domain (Ntn-hydrolase fold) and that a Glu proton acceptor would reside there, making options B (327), C (372), and A (413) less likely as they fall in the synthetase domain. However, distinguishing position 52 specifically from the many Glu residues in the N-terminal region, or confirming its exact role as 'proton acceptor for glutaminase activity,' requires knowledge of the conserved NadE catalytic triad positions or the specific UniProt annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact position (52) of the catalytic Glu proton acceptor in this particular NadE sequence, and the assignment of functional roles (proton acceptor vs. nucleophile vs. 'for glutaminase activity') to positions 52, 119, and 157 respectively, as annotated by HAMAP-Rule MF_02090. Without this annotation or memorized family alignment, selecting position 52 over other Glu residues in the glutaminase domain is not achievable by general reasoning alone.",
    "reason": "While domain architecture recognition (N-terminal glutaminase vs. C-terminal synthetase) provides a weak argument against the C-terminal distractors, pinpointing position 52 as the specific proton acceptor requires item-specific annotation knowledge or memorization of the NadE family catalytic residue positions. The question's precision (exact position + exact functional label) exceeds what general biological reasoning from sequence alone can resolve."
  },
  "case_id": "active_site_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0H2X6L3 (NadE, Xanthomonas campestris pv. campestris 8004) annotates position 52 as 'Proton acceptor; for glutaminase activity' (Active site feature, evidence ECO:0000255|HAMAP-Rule:MF_02090). The sequence residue at position 52 is Glu (E), consistent with the known catalytic mechanism of glutamine amidotransferases where a conserved Glu activates a water nucleophile. The annotation is computational (HAMAP-Rule inference by family similarity), not direct experimental evidence for this specific protein, but it is consistent with the well-characterized NadE catalytic triad. The distractor positions (413, 327, 372) do not correspond to any annotated active site in this entry."
  },
  "important_caveats": [
    "The active site annotation at position 52 carries evidence code ECO:0000255 (inferred by similarity to HAMAP-Rule MF_02090), meaning it is a computational/curatorial family inference, not direct experimental characterization of this specific X. campestris protein.",
    "The full catalytic center of NadE involves three active-site residues (52, 119, 157); the question and answer format presents only one, which is a simplification.",
    "The UniProt accession A0A0H2X6L3 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must identify the protein from sequence alone.",
    "The protein was integrated into Swiss-Prot on 2025-02-05; if the benchmark was constructed before this date, the annotation may not have been publicly available at construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D corresponds to an actual UniProt-annotated active site (position 52). Positions 413, 327, and 372 are not annotated as active sites in this entry. The other annotated active sites (119, 157) are not offered as options. Thus D is uniquely correct among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0H2X6L3 (NadE, Xanthomonas campestris pv. campestris 8004) annotates position 52 as 'Proton acceptor; for glutaminase activity' (Active site feature, evidence ECO:0000255|HAMAP-Rule:MF_02090). The sequence residue at position 52 is Glu (E), consistent with the known catalytic mechanism of glutamine amidotransferases where a conserved Glu activates a water nucleophile. The annotation is computational (HAMAP-Rule inference by family similarity), not direct experimental evidence for this specific protein, but it is consistent with the well-characterized NadE catalytic triad. The distractor positions (413, 327, 372) do not correspond to any annotated active site in this entry.",
    "evidence_ids": ["C5", "H3", "C4", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly reason that the N-terminal ~200 residues constitute a glutaminase domain (Ntn-hydrolase fold) and that a Glu proton acceptor would reside there, making options B (327), C (372), and A (413) less likely as they fall in the synthetase domain. However, distinguishing position 52 specifically from the many Glu residues in the N-terminal region, or confirming its exact role as 'proton acceptor for glutaminase activity,' requires knowledge of the conserved NadE catalytic triad positions or the specific UniProt annotation.",
    "missing_item_specific_fact": "The exact position (52) of the catalytic Glu proton acceptor in this particular NadE sequence, and the assignment of functional roles (proton acceptor vs. nucleophile vs. 'for glutaminase activity') to positions 52, 119, and 157 respectively, as annotated by HAMAP-Rule MF_02090. Without this annotation or memorized family alignment, selecting position 52 over other Glu residues in the glutaminase domain is not achievable by general reasoning alone.",
    "reason": "While domain architecture recognition (N-terminal glutaminase vs. C-terminal synthetase) provides a weak argument against the C-terminal distractors, pinpointing position 52 as the specific proton acceptor requires item-specific annotation knowledge or memorization of the NadE family catalytic residue positions. The question's precision (exact position + exact functional label) exceeds what general biological reasoning from sequence alone can resolve."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D corresponds to an actual UniProt-annotated active site (position 52). Positions 413, 327, and 372 are not annotated as active sites in this entry. The other annotated active sites (119, 157) are not offered as options. Thus D is uniquely correct among the four choices."
  },
  "important_caveats": [
    "The active site annotation at position 52 carries evidence code ECO:0000255 (inferred by similarity to HAMAP-Rule MF_02090), meaning it is a computational/curatorial family inference, not direct experimental characterization of this specific X. campestris protein.",
    "The full catalytic center of NadE involves three active-site residues (52, 119, 157); the question and answer format presents only one, which is a simplification.",
    "The UniProt accession A0A0H2X6L3 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must identify the protein from sequence alone.",
    "The protein was integrated into Swiss-Prot on 2025-02-05; if the benchmark was constructed before this date, the annotation may not have been publicly available at construction time."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact input sequence matches the source sequence, and the annotation identifies residue 52 as the proton acceptor for glutaminase activity. This is a HAMAP computational annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a glutamine-dependent NAD synthetase, whose glutaminase domain uses conserved catalytic residues. Residue 52 is glutamate in the supplied sequence, consistent with the catalytic acid/base role in that domain; choice D uniquely links its proton-acceptor role to glutaminase activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level knowledge of glutamine-dependent NAD synthetases and their glutaminase domain provides a credible basis to favor D among these choices. Exact residue-role assignment is not certain from sequence alone, but the choices make the family-level distinction meaningful.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The glutaminase-specific description in D distinguishes it from the other offered residue-role descriptions.


### Important caveats

- The supporting residue annotation is attributed to a computational HAMAP rule; the excerpts do not independently establish experimental validation.
- The source sequence match establishes applicability of the annotation, but the source record was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a glutamine-dependent NAD synthetase, whose glutaminase domain uses conserved catalytic residues. Residue 52 is glutamate in the supplied sequence, consistent with the catalytic acid/base role in that domain; choice D uniquely links its proton-acceptor role to glutaminase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of glutamine-dependent NAD synthetases and their glutaminase domain provides a credible basis to favor D among these choices. Exact residue-role assignment is not certain from sequence alone, but the choices make the family-level distinction meaningful."
  },
  "case_id": "active_site_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact input sequence matches the source sequence, and the annotation identifies residue 52 as the proton acceptor for glutaminase activity. This is a HAMAP computational annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supporting residue annotation is attributed to a computational HAMAP rule; the excerpts do not independently establish experimental validation.",
    "The source sequence match establishes applicability of the annotation, but the source record was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The glutaminase-specific description in D distinguishes it from the other offered residue-role descriptions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact input sequence matches the source sequence, and the annotation identifies residue 52 as the proton acceptor for glutaminase activity. This is a HAMAP computational annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a glutamine-dependent NAD synthetase, whose glutaminase domain uses conserved catalytic residues. Residue 52 is glutamate in the supplied sequence, consistent with the catalytic acid/base role in that domain; choice D uniquely links its proton-acceptor role to glutaminase activity.",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of glutamine-dependent NAD synthetases and their glutaminase domain provides a credible basis to favor D among these choices. Exact residue-role assignment is not certain from sequence alone, but the choices make the family-level distinction meaningful."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The glutaminase-specific description in D distinguishes it from the other offered residue-role descriptions."
  },
  "important_caveats": [
    "The supporting residue annotation is attributed to a computational HAMAP rule; the excerpts do not independently establish experimental validation.",
    "The source sequence match establishes applicability of the annotation, but the source record was not part of the original model input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0H2X6L3 annotates position 52 as 'Proton acceptor; for glutaminase activity' (Active site), matching option D exactly. The residue at position 52 in the supplied sequence is E (Glutamate), consistent with the proton-acceptor role in the Class I glutamine amidotransferase catalytic triad (Glu-His-Cys). The annotation evidence code is ECO:0000255 (inferred by similarity to HAMAP-Rule MF_02090), i.e., computational transfer rather than direct experimental validation, but it is a well-supported family-level annotation for glutamine-dependent NAD+ synthetase (EC 6.3.5.1).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~200 residues of the supplied sequence contain a recognizable glutamine amidotransferase (GATase) domain, identifiable by its characteristic fold and the presence of a catalytic Cys (position 157) and Glu residues in the expected N-terminal region. Family knowledge of Class I GATase enzymes (shared across GMP synthase, carbamoyl phosphate synthetase, NAD synthetase, etc.) establishes the catalytic triad as Glu (proton acceptor) → His (proton donor) → Cys (nucleophile), with the proton-acceptor Glu located in the N-terminal ~60 residues. Option D places a proton acceptor at position 52 (E), squarely within the GATase domain and consistent with the conserved Glu position. The qualifier 'for glutaminase activity' specifically refers to the GATase sub-reaction, further anchoring the answer to the N-terminal domain. Options A (413), B (327), and C (372) all fall in the C-terminal synthetase domain, which catalyzes a different reaction (adenylylation/amidation of deamido-NAD) and does not host the glutaminase catalytic triad. Thus, recognizing the GATase domain and its conserved triad architecture from sequence features and family-level knowledge meaningfully distinguishes D from A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the GATase domain from the N-terminal sequence pattern, recall the conserved Glu-His-Cys triad architecture from multiple related enzymes, and use the 'for glutaminase activity' qualifier to restrict the answer to the N-terminal domain. Among the four offered choices, only D places a residue in the GATase domain with the correct residue type (Glu) and role (proton acceptor). This is a legitimate family-level inference, not mere memorization of this specific entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated by domain location: D is in the N-terminal GATase domain while A, B, C are in the C-terminal synthetase domain. The 'for glutaminase activity' qualifier in D uniquely matches the GATase catalytic mechanism. No other option is defensible as the glutaminase proton acceptor.


### Important caveats

- The UniProt annotation at position 52 is based on HAMAP-Rule transfer (ECO:0000255), not direct experimental mutagenesis or crystallographic catalytic-site mapping for this specific protein.
- The specific position 52 depends on the alignment within the GATase family; a model would need to identify the correct Glu among several Glu residues in the N-terminal region, though among the offered choices only D is in the correct domain.
- The protein identity (NAD+ synthetase) and organism (Xanthomonas campestris) were not provided in the original input; the model must rely on sequence-based family recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~200 residues of the supplied sequence contain a recognizable glutamine amidotransferase (GATase) domain, identifiable by its characteristic fold and the presence of a catalytic Cys (position 157) and Glu residues in the expected N-terminal region. Family knowledge of Class I GATase enzymes (shared across GMP synthase, carbamoyl phosphate synthetase, NAD synthetase, etc.) establishes the catalytic triad as Glu (proton acceptor) → His (proton donor) → Cys (nucleophile), with the proton-acceptor Glu located in the N-terminal ~60 residues. Option D places a proton acceptor at position 52 (E), squarely within the GATase domain and consistent with the conserved Glu position. The qualifier 'for glutaminase activity' specifically refers to the GATase sub-reaction, further anchoring the answer to the N-terminal domain. Options A (413), B (327), and C (372) all fall in the C-terminal synthetase domain, which catalyzes a different reaction (adenylylation/amidation of deamido-NAD) and does not host the glutaminase catalytic triad. Thus, recognizing the GATase domain and its conserved triad architecture from sequence features and family-level knowledge meaningfully distinguishes D from A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GATase domain from the N-terminal sequence pattern, recall the conserved Glu-His-Cys triad architecture from multiple related enzymes, and use the 'for glutaminase activity' qualifier to restrict the answer to the N-terminal domain. Among the four offered choices, only D places a residue in the GATase domain with the correct residue type (Glu) and role (proton acceptor). This is a legitimate family-level inference, not mere memorization of this specific entry."
  },
  "case_id": "active_site_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 annotates position 52 as 'Proton acceptor; for glutaminase activity' (Active site), matching option D exactly. The residue at position 52 in the supplied sequence is E (Glutamate), consistent with the proton-acceptor role in the Class I glutamine amidotransferase catalytic triad (Glu-His-Cys). The annotation evidence code is ECO:0000255 (inferred by similarity to HAMAP-Rule MF_02090), i.e., computational transfer rather than direct experimental validation, but it is a well-supported family-level annotation for glutamine-dependent NAD+ synthetase (EC 6.3.5.1)."
  },
  "important_caveats": [
    "The UniProt annotation at position 52 is based on HAMAP-Rule transfer (ECO:0000255), not direct experimental mutagenesis or crystallographic catalytic-site mapping for this specific protein.",
    "The specific position 52 depends on the alignment within the GATase family; a model would need to identify the correct Glu among several Glu residues in the N-terminal region, though among the offered choices only D is in the correct domain.",
    "The protein identity (NAD+ synthetase) and organism (Xanthomonas campestris) were not provided in the original input; the model must rely on sequence-based family recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by domain location: D is in the N-terminal GATase domain while A, B, C are in the C-terminal synthetase domain. The 'for glutaminase activity' qualifier in D uniquely matches the GATase catalytic mechanism. No other option is defensible as the glutaminase proton acceptor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 annotates position 52 as 'Proton acceptor; for glutaminase activity' (Active site), matching option D exactly. The residue at position 52 in the supplied sequence is E (Glutamate), consistent with the proton-acceptor role in the Class I glutamine amidotransferase catalytic triad (Glu-His-Cys). The annotation evidence code is ECO:0000255 (inferred by similarity to HAMAP-Rule MF_02090), i.e., computational transfer rather than direct experimental validation, but it is a well-supported family-level annotation for glutamine-dependent NAD+ synthetase (EC 6.3.5.1).",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~200 residues of the supplied sequence contain a recognizable glutamine amidotransferase (GATase) domain, identifiable by its characteristic fold and the presence of a catalytic Cys (position 157) and Glu residues in the expected N-terminal region. Family knowledge of Class I GATase enzymes (shared across GMP synthase, carbamoyl phosphate synthetase, NAD synthetase, etc.) establishes the catalytic triad as Glu (proton acceptor) → His (proton donor) → Cys (nucleophile), with the proton-acceptor Glu located in the N-terminal ~60 residues. Option D places a proton acceptor at position 52 (E), squarely within the GATase domain and consistent with the conserved Glu position. The qualifier 'for glutaminase activity' specifically refers to the GATase sub-reaction, further anchoring the answer to the N-terminal domain. Options A (413), B (327), and C (372) all fall in the C-terminal synthetase domain, which catalyzes a different reaction (adenylylation/amidation of deamido-NAD) and does not host the glutaminase catalytic triad. Thus, recognizing the GATase domain and its conserved triad architecture from sequence features and family-level knowledge meaningfully distinguishes D from A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GATase domain from the N-terminal sequence pattern, recall the conserved Glu-His-Cys triad architecture from multiple related enzymes, and use the 'for glutaminase activity' qualifier to restrict the answer to the N-terminal domain. Among the four offered choices, only D places a residue in the GATase domain with the correct residue type (Glu) and role (proton acceptor). This is a legitimate family-level inference, not mere memorization of this specific entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by domain location: D is in the N-terminal GATase domain while A, B, C are in the C-terminal synthetase domain. The 'for glutaminase activity' qualifier in D uniquely matches the GATase catalytic mechanism. No other option is defensible as the glutaminase proton acceptor."
  },
  "important_caveats": [
    "The UniProt annotation at position 52 is based on HAMAP-Rule transfer (ECO:0000255), not direct experimental mutagenesis or crystallographic catalytic-site mapping for this specific protein.",
    "The specific position 52 depends on the alignment within the GATase family; a model would need to identify the correct Glu among several Glu residues in the N-terminal region, though among the offered choices only D is in the correct domain.",
    "The protein identity (NAD+ synthetase) and organism (Xanthomonas campestris) were not provided in the original input; the model must rely on sequence-based family recognition."
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
  "requested_accession": "A0A0H2X6L3",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "3d11eda2e9e6481a31767f7fc550e14d13db9c3ed7ac21360bb4b2288341703d",
  "benchmark_sequence_length": 552,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 50,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "current_source_sequence_sha256": "3d11eda2e9e6481a31767f7fc550e14d13db9c3ed7ac21360bb4b2288341703d",
  "current_source_sequence_length": 552,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 49,
  "selected_historical_version": {
    "accession": "A0A0H2X6L3",
    "database": "Swiss-Prot",
    "entryVersion": 49,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NADE_XANC8",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "selected_historical_source_sequence_sha256": "3d11eda2e9e6481a31767f7fc550e14d13db9c3ed7ac21360bb4b2288341703d",
  "selected_historical_source_sequence_length": 552,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 49,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A0H2X6L3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":50,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Lysobacterales\",\"Lysobacteraceae\",\"Xanthomonas\"],\"scientificName\":\"Xanthomonas campestris pv. campestris (strain 8004)\",\"taxonId\":314565}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"NAD(+) synthase [glutamine-hydrolyzing]\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NAD(+) synthetase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NADS\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"6.3.5.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Glutamine-dependent NAD(+) synthetase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Proton acceptor; for glutaminase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":52},\"start\":{\"modifier\":\"EXACT\",\"value\":52}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"For glutaminase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":119},\"start\":{\"modifier\":\"EXACT\",\"value\":119}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Nucleophile; for glutaminase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":157},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58359\",\"name\":\"L-glutamine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":125},\"start\":{\"modifier\":\"EXACT\",\"value\":125}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58359\",\"name\":\"L-glutamine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":183},\"start\":{\"modifier\":\"EXACT\",\"value\":183}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58359\",\"name\":\"L-glutamine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":189},\"start\":{\"modifier\":\"EXACT\",\"value\":189}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":305},\"start\":{\"modifier\":\"EXACT\",\"value\":298}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58437\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58437\",\"name\":\"deamido-NAD(+)\",\"note\":\"ligand shared between two neighboring subunits\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":381},\"start\":{\"modifier\":\"EXACT\",\"value\":381}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":405},\"start\":{\"modifier\":\"EXACT\",\"value\":405}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58437\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58437\",\"name\":\"deamido-NAD(+)\",\"note\":\"ligand shared between two neighboring subunits\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":410},\"start\":{\"modifier\":\"EXACT\",\"value\":410}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58437\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58437\",\"name\":\"deamido-NAD(+)\",\"note\":\"ligand shared between two neighboring subunits\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":522},\"start\":{\"modifier\":\"EXACT\",\"value\":522}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Xu G.\",\"Ma J.\",\"Fang Q.\",\"Peng Q.\",\"Jiao X.\",\"Hu W.\",\"Zhao Q.\",\"Kong Y.\",\"Liu F.\",\"Shi X.\",\"Tang D.J.\",\"Tang J.L.\",\"Ming Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38429435\"},{\"database\":\"DOI\",\"id\":\"10.1038/s42003-024-05921-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"255\",\"id\":\"38429435\",\"journal\":\"Commun. Biol.\",\"lastPage\":\"255\",\"publicationDate\":\"2024\",\"title\":\"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.\",\"volume\":\"7\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"8004\"}],\"referenceNumber\":2,\"referencePositions\":[\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   NADE_XANC8              Reviewed;         552 AA.\nAC   A0A0H2X6L3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 49.\nDE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};\nDE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};\nDE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};\nDE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};\nDE            Short=NADS {ECO:0000303|PubMed:38429435};\nGN   Name=nadE {ECO:0000255|HAMAP-Rule:MF_02090};\nGN   OrderedLocusNames=XC_1067 {ECO:0000312|EMBL:AAY48137.1};\nOS   Xanthomonas campestris pv. campestris (strain 8004).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Lysobacterales; Lysobacteraceae; Xanthomonas.\nOX   NCBI_TaxID=314565;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 28-36",
  "excerpt": "RN   [2]\nRP   DISRUPTION PHENOTYPE.\nRC   STRAIN=8004;\nRX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;\nRA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,\nRA   Shi X., Tang D.J., Tang J.L., Ming Z.;\nRT   \"Structural insights into Xanthomonas campestris pv. campestris NAD+\nRT   biosynthesis via the NAM salvage pathway.\";\nRL   Commun. Biol. 7:255-255(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 108-110",
  "excerpt": "FT   ACT_SITE        52\nFT                   /note=\"Proton acceptor; for glutaminase activity\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 111-113",
  "excerpt": "FT   ACT_SITE        119\nFT                   /note=\"For glutaminase activity\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 114-116",
  "excerpt": "FT   ACT_SITE        157\nFT                   /note=\"Nucleophile; for glutaminase activity\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 117-120",
  "excerpt": "FT   BINDING         125\nFT                   /ligand=\"L-glutamine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58359\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 121-124",
  "excerpt": "FT   BINDING         183\nFT                   /ligand=\"L-glutamine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58359\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 125-128",
  "excerpt": "FT   BINDING         189\nFT                   /ligand=\"L-glutamine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58359\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 129-132",
  "excerpt": "FT   BINDING         298..305\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 133-138",
  "excerpt": "FT   BINDING         381\nFT                   /ligand=\"deamido-NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58437\"\nFT                   /ligand_note=\"ligand shared between two neighboring\nFT                   subunits\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 139-142",
  "excerpt": "FT   BINDING         405\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 143-148",
  "excerpt": "FT   BINDING         410\nFT                   /ligand=\"deamido-NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58437\"\nFT                   /ligand_note=\"ligand shared between two neighboring\nFT                   subunits\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "source_locator": "lines 149-154",
  "excerpt": "FT   BINDING         522\nFT                   /ligand=\"deamido-NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58437\"\nFT                   /ligand_note=\"ligand shared between two neighboring\nFT                   subunits\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_02090\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
