# EC_number_0088: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0088.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 6.3.5.1

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
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ

[Multiple Choices]
A. 5.6.2.4
B. 2.3.1.193
C. 6.3.5.1
D. 1.14.19.80
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

> The exact sequence matches a UniProt entry annotated as glutamine-dependent NAD(+) synthetase, EC 6.3.5.1, with the catalytic activity and EC assignment attributed to the HAMAP rule. This supports the key as a database-based functional annotation, but does not establish direct experimental validation of the reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support recognition of an enzyme with glutamine-processing and ATP-dependent ligase features, favoring a ligase over the other broad EC classes. Those features alone do not establish the specific NAD-synthetase reaction required for EC 6.3.5.1.


**Missing item-specific fact**

> The protein-specific identification as glutamine-dependent NAD(+) synthetase, or equivalent family/domain evidence establishing its substrate and reaction, is not supplied in the question.


**Reason**

> Choosing the complete EC number depends on identifying this particular enzyme and its reaction; the sequence and unlabeled EC choices do not state that reaction. Recognizing the sequence through an external annotation would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only annotation supports C, and the listed EC numbers are distinct classifications. No competing option is comparably supported by the supplied information.


### Important caveats

- The sequence match is exact in both current and historical UniProt records, but the author's precise source snapshot is unknown.
- The EC and catalytic-activity annotation is attributed to a computational HAMAP rule; the cited paper excerpt concerns a disruption phenotype and does not itself establish direct enzymatic measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support recognition of an enzyme with glutamine-processing and ATP-dependent ligase features, favoring a ligase over the other broad EC classes. Those features alone do not establish the specific NAD-synthetase reaction required for EC 6.3.5.1.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as glutamine-dependent NAD(+) synthetase, or equivalent family/domain evidence establishing its substrate and reaction, is not supplied in the question.",
    "reason": "Choosing the complete EC number depends on identifying this particular enzyme and its reaction; the sequence and unlabeled EC choices do not state that reaction. Recognizing the sequence through an external annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as glutamine-dependent NAD(+) synthetase, EC 6.3.5.1, with the catalytic activity and EC assignment attributed to the HAMAP rule. This supports the key as a database-based functional annotation, but does not establish direct experimental validation of the reaction."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's precise source snapshot is unknown.",
    "The EC and catalytic-activity annotation is attributed to a computational HAMAP rule; the cited paper excerpt concerns a disruption phenotype and does not itself establish direct enzymatic measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports C, and the listed EC numbers are distinct classifications. No competing option is comparably supported by the supplied information."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as glutamine-dependent NAD(+) synthetase, EC 6.3.5.1, with the catalytic activity and EC assignment attributed to the HAMAP rule. This supports the key as a database-based functional annotation, but does not establish direct experimental validation of the reaction.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support recognition of an enzyme with glutamine-processing and ATP-dependent ligase features, favoring a ligase over the other broad EC classes. Those features alone do not establish the specific NAD-synthetase reaction required for EC 6.3.5.1.",
    "missing_item_specific_fact": "The protein-specific identification as glutamine-dependent NAD(+) synthetase, or equivalent family/domain evidence establishing its substrate and reaction, is not supplied in the question.",
    "reason": "Choosing the complete EC number depends on identifying this particular enzyme and its reaction; the sequence and unlabeled EC choices do not state that reaction. Recognizing the sequence through an external annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports C, and the listed EC numbers are distinct classifications. No competing option is comparably supported by the supplied information."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's precise source snapshot is unknown.",
    "The EC and catalytic-activity annotation is attributed to a computational HAMAP rule; the cited paper excerpt concerns a disruption phenotype and does not itself establish direct enzymatic measurement."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0H2X6L3 (NADE_XANC8) matches the benchmark sequence exactly (552 AA, SHA256 match). The entry is annotated as Glutamine-dependent NAD(+) synthetase with EC=6.3.5.1, assigned via HAMAP-Rule MF_02090 (computational/curatorial evidence code ECO:0000255). The gene name is nadE. A 2024 PubMed reference (38429435) provides DISRUPTION PHENOTYPE evidence related to NAD+ biosynthesis in Xanthomonas campestris. The catalytic reaction (deamido-NAD(+) + L-glutamine + ATP + H2O → L-glutamate + AMP + diphosphate + NAD(+) + H(+)) is consistent with EC 6.3.5.1. The annotation is primarily curatorial (HAMAP rule) rather than direct experimental, but the gene name, organism context, and disruption phenotype support the assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options span four different top-level EC classes (1=oxidoreductase, 2=transferase, 5=isomerase, 6=ligase). The sequence (~552 aa) exhibits a two-domain architecture characteristic of NadE: an N-terminal glutamine amidotransferase domain (containing a conserved Cys-His-Glu catalytic triad, e.g., the 'DGDNCVVTVKGVQVGVVICEDLWFAE' region with catalytic Cys) and a C-terminal nucleotide synthetase domain (containing the 'GDMCGGY' nucleotidyltransferase motif). The combination of a glutamine amidotransferase domain coupled to an ATP-dependent nucleotide synthetase domain is the hallmark of glutamine-dependent NAD(+) synthetase (NadE, EC 6.3.5.1), a ligase (EC 6) forming a C–N bond using glutamine as the nitrogen donor. This two-domain architecture is not consistent with an ABC transporter (EC 5.6.2.4), an acyltransferase (EC 2.3.1.193), or a cytochrome P450 oxidoreductase (EC 1.14.19.80).


**Missing item-specific fact**

> Precise recognition of the NadE family requires specialized knowledge of the glutamine amidotransferase + NAD synthetase two-domain fold. Without familiarity with this specific domain combination, distinguishing EC 6.3.5.1 from other EC 6 ligases that also use glutamine would be difficult. However, the four distractors are from entirely different EC classes, reducing the specificity needed.


**Reason**

> The sequence contains identifiable domain features (glutaminase catalytic Cys, nucleotidyltransferase motif) that support the ligase/glutamine-amidotransferase classification. The four options being from four different EC top-level classes means that recognizing the two-domain glutaminase+synthetase architecture is sufficient to select EC 6 over EC 1, 2, or 5. This constitutes a concrete biological argument from the sequence, though it requires specialized domain-recognition knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options belong to four distinct EC top-level classes (1, 2, 5, 6), and the sequence's two-domain glutaminase+synthetase architecture is most consistent with EC 6. No other option plausibly matches the observed domain organization.


### Important caveats

- The EC 6.3.5.1 annotation is assigned via HAMAP-Rule (ECO:0000255), a computational/curatorial rule, not direct in vitro enzymatic assay evidence. The 2024 PubMed paper provides disruption phenotype and structural data but the entry does not cite direct kinetic characterization.
- The entry was first public on 2025-02-05 (entry version 50 current, version 49 at historical cutoff). The author's source snapshot date is unknown, but sequence match is confirmed across versions.
- Domain recognition from raw sequence without structural data or database lookup requires specialized knowledge of the NadE/glutamine amidotransferase superfamily architecture.
- The identity of the protein (NadE from Xanthomonas campestris) was inferred by the reviewer from dataset metadata; this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options span four different top-level EC classes (1=oxidoreductase, 2=transferase, 5=isomerase, 6=ligase). The sequence (~552 aa) exhibits a two-domain architecture characteristic of NadE: an N-terminal glutamine amidotransferase domain (containing a conserved Cys-His-Glu catalytic triad, e.g., the 'DGDNCVVTVKGVQVGVVICEDLWFAE' region with catalytic Cys) and a C-terminal nucleotide synthetase domain (containing the 'GDMCGGY' nucleotidyltransferase motif). The combination of a glutamine amidotransferase domain coupled to an ATP-dependent nucleotide synthetase domain is the hallmark of glutamine-dependent NAD(+) synthetase (NadE, EC 6.3.5.1), a ligase (EC 6) forming a C–N bond using glutamine as the nitrogen donor. This two-domain architecture is not consistent with an ABC transporter (EC 5.6.2.4), an acyltransferase (EC 2.3.1.193), or a cytochrome P450 oxidoreductase (EC 1.14.19.80).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of the NadE family requires specialized knowledge of the glutamine amidotransferase + NAD synthetase two-domain fold. Without familiarity with this specific domain combination, distinguishing EC 6.3.5.1 from other EC 6 ligases that also use glutamine would be difficult. However, the four distractors are from entirely different EC classes, reducing the specificity needed.",
    "reason": "The sequence contains identifiable domain features (glutaminase catalytic Cys, nucleotidyltransferase motif) that support the ligase/glutamine-amidotransferase classification. The four options being from four different EC top-level classes means that recognizing the two-domain glutaminase+synthetase architecture is sufficient to select EC 6 over EC 1, 2, or 5. This constitutes a concrete biological argument from the sequence, though it requires specialized domain-recognition knowledge."
  },
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 (NADE_XANC8) matches the benchmark sequence exactly (552 AA, SHA256 match). The entry is annotated as Glutamine-dependent NAD(+) synthetase with EC=6.3.5.1, assigned via HAMAP-Rule MF_02090 (computational/curatorial evidence code ECO:0000255). The gene name is nadE. A 2024 PubMed reference (38429435) provides DISRUPTION PHENOTYPE evidence related to NAD+ biosynthesis in Xanthomonas campestris. The catalytic reaction (deamido-NAD(+) + L-glutamine + ATP + H2O → L-glutamate + AMP + diphosphate + NAD(+) + H(+)) is consistent with EC 6.3.5.1. The annotation is primarily curatorial (HAMAP rule) rather than direct experimental, but the gene name, organism context, and disruption phenotype support the assignment."
  },
  "important_caveats": [
    "The EC 6.3.5.1 annotation is assigned via HAMAP-Rule (ECO:0000255), a computational/curatorial rule, not direct in vitro enzymatic assay evidence. The 2024 PubMed paper provides disruption phenotype and structural data but the entry does not cite direct kinetic characterization.",
    "The entry was first public on 2025-02-05 (entry version 50 current, version 49 at historical cutoff). The author's source snapshot date is unknown, but sequence match is confirmed across versions.",
    "Domain recognition from raw sequence without structural data or database lookup requires specialized knowledge of the NadE/glutamine amidotransferase superfamily architecture.",
    "The identity of the protein (NadE from Xanthomonas campestris) was inferred by the reviewer from dataset metadata; this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four distinct EC top-level classes (1, 2, 5, 6), and the sequence's two-domain glutaminase+synthetase architecture is most consistent with EC 6. No other option plausibly matches the observed domain organization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 (NADE_XANC8) matches the benchmark sequence exactly (552 AA, SHA256 match). The entry is annotated as Glutamine-dependent NAD(+) synthetase with EC=6.3.5.1, assigned via HAMAP-Rule MF_02090 (computational/curatorial evidence code ECO:0000255). The gene name is nadE. A 2024 PubMed reference (38429435) provides DISRUPTION PHENOTYPE evidence related to NAD+ biosynthesis in Xanthomonas campestris. The catalytic reaction (deamido-NAD(+) + L-glutamine + ATP + H2O → L-glutamate + AMP + diphosphate + NAD(+) + H(+)) is consistent with EC 6.3.5.1. The annotation is primarily curatorial (HAMAP rule) rather than direct experimental, but the gene name, organism context, and disruption phenotype support the assignment.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options span four different top-level EC classes (1=oxidoreductase, 2=transferase, 5=isomerase, 6=ligase). The sequence (~552 aa) exhibits a two-domain architecture characteristic of NadE: an N-terminal glutamine amidotransferase domain (containing a conserved Cys-His-Glu catalytic triad, e.g., the 'DGDNCVVTVKGVQVGVVICEDLWFAE' region with catalytic Cys) and a C-terminal nucleotide synthetase domain (containing the 'GDMCGGY' nucleotidyltransferase motif). The combination of a glutamine amidotransferase domain coupled to an ATP-dependent nucleotide synthetase domain is the hallmark of glutamine-dependent NAD(+) synthetase (NadE, EC 6.3.5.1), a ligase (EC 6) forming a C–N bond using glutamine as the nitrogen donor. This two-domain architecture is not consistent with an ABC transporter (EC 5.6.2.4), an acyltransferase (EC 2.3.1.193), or a cytochrome P450 oxidoreductase (EC 1.14.19.80).",
    "missing_item_specific_fact": "Precise recognition of the NadE family requires specialized knowledge of the glutamine amidotransferase + NAD synthetase two-domain fold. Without familiarity with this specific domain combination, distinguishing EC 6.3.5.1 from other EC 6 ligases that also use glutamine would be difficult. However, the four distractors are from entirely different EC classes, reducing the specificity needed.",
    "reason": "The sequence contains identifiable domain features (glutaminase catalytic Cys, nucleotidyltransferase motif) that support the ligase/glutamine-amidotransferase classification. The four options being from four different EC top-level classes means that recognizing the two-domain glutaminase+synthetase architecture is sufficient to select EC 6 over EC 1, 2, or 5. This constitutes a concrete biological argument from the sequence, though it requires specialized domain-recognition knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four distinct EC top-level classes (1, 2, 5, 6), and the sequence's two-domain glutaminase+synthetase architecture is most consistent with EC 6. No other option plausibly matches the observed domain organization."
  },
  "important_caveats": [
    "The EC 6.3.5.1 annotation is assigned via HAMAP-Rule (ECO:0000255), a computational/curatorial rule, not direct in vitro enzymatic assay evidence. The 2024 PubMed paper provides disruption phenotype and structural data but the entry does not cite direct kinetic characterization.",
    "The entry was first public on 2025-02-05 (entry version 50 current, version 49 at historical cutoff). The author's source snapshot date is unknown, but sequence match is confirmed across versions.",
    "Domain recognition from raw sequence without structural data or database lookup requires specialized knowledge of the NadE/glutamine amidotransferase superfamily architecture.",
    "The identity of the protein (NadE from Xanthomonas campestris) was inferred by the reviewer from dataset metadata; this accession was not provided to the evaluated model."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact supplied sequence matches the UniProt sequence annotated as glutamine-dependent NAD(+) synthetase, EC 6.3.5.1. This support is computational: the annotation cites a HAMAP rule, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the two-part architecture of glutamine-dependent NAD synthetases: an N-terminal glutamine-amidotransferase region, including a catalytic cysteine-containing motif, and a C-terminal ATP-dependent synthetase region. Transferable knowledge of this enzyme family makes EC 6.3.5.1 a meaningful choice over the alternatives, which describe unrelated reaction classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence and domain inference can distinguish the NAD synthetase option without knowing this protein's database record. The inference is not experimental proof, but the alternatives do not require finer discrimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered EC number is comparably supported by the sequence and family-level inference.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but its EC assignment is computationally attributed to HAMAP; the excerpts do not establish direct experimental confirmation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the two-part architecture of glutamine-dependent NAD synthetases: an N-terminal glutamine-amidotransferase region, including a catalytic cysteine-containing motif, and a C-terminal ATP-dependent synthetase region. Transferable knowledge of this enzyme family makes EC 6.3.5.1 a meaningful choice over the alternatives, which describe unrelated reaction classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and domain inference can distinguish the NAD synthetase option without knowing this protein's database record. The inference is not experimental proof, but the alternatives do not require finer discrimination."
  },
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt sequence annotated as glutamine-dependent NAD(+) synthetase, EC 6.3.5.1. This support is computational: the annotation cites a HAMAP rule, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its EC assignment is computationally attributed to HAMAP; the excerpts do not establish direct experimental confirmation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered EC number is comparably supported by the sequence and family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt sequence annotated as glutamine-dependent NAD(+) synthetase, EC 6.3.5.1. This support is computational: the annotation cites a HAMAP rule, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the two-part architecture of glutamine-dependent NAD synthetases: an N-terminal glutamine-amidotransferase region, including a catalytic cysteine-containing motif, and a C-terminal ATP-dependent synthetase region. Transferable knowledge of this enzyme family makes EC 6.3.5.1 a meaningful choice over the alternatives, which describe unrelated reaction classes.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and domain inference can distinguish the NAD synthetase option without knowing this protein's database record. The inference is not experimental proof, but the alternatives do not require finer discrimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered EC number is comparably supported by the sequence and family-level inference."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its EC assignment is computationally attributed to HAMAP; the excerpts do not establish direct experimental confirmation."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0H2X6L3 (NADE_XANC8) annotates this 552-aa protein as Glutamine-dependent NAD(+) synthetase with EC 6.3.5.1. The EC number is assigned via HAMAP-Rule MF_02090 (ECO:0000255, computational/profiling evidence), and the entry also cites PubMed:38429435 (structural and disruption-phenotype study in Xanthomonas campestris) providing experimental context. The catalytic reaction (deamido-NAD+ + L-glutamine + ATP + H2O → L-glutamate + AMP + diphosphate + NAD+ + H+) matches EC 6.3.5.1. Sequence match is confirmed (SHA-256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 552-aa sequence displays the hallmark two-domain architecture of NadE (glutamine-dependent NAD+ synthetase): an N-terminal glutamine amidotransferase (GAT) domain with a catalytic Cys (visible in the 'AHCEQ' region around residue ~75) and a C-terminal synthetase domain containing conserved motifs for ATP/NAD+ binding. This architecture is shared across NadE homologs in bacteria and plants. Against the offered distractors: (A) EC 5.6.2.4 is an ABC-transporter translocase requiring Walker A (GxxGxGKS/T), Walker B, and ABC signature (LSGGQ) motifs — none are present; (B) EC 2.3.1.193 is a small (~200–300 aa) acyltransferase with a HxxxD or DIL motif — the protein is far too large and lacks such motifs; (D) EC 1.14.19.80 is a cytochrome P450 requiring the conserved heme-binding FxxGxxxCxG motif — absent here. The GAT+synthetase fold, the ~550-aa length, and the absence of motifs diagnostic of the other three enzyme classes collectively point to EC 6.3.5.1, a family-level inference transferable from well-characterized NadE proteins (e.g., E. coli, B. subtilis, plant homologs).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with the NadE protein family can recognize the two-domain GAT/synthetase architecture, the characteristic length, and conserved motifs, and can exclude the three distractors by the absence of their defining motifs (Walker A/B for ABC transporters, HxxxD for acyltransferases, FxxGxxxCxG for P450s). The sequence is in fact >95% identical to E. coli NadE (P0A6E2), making family recognition straightforward. The inference relies on transferable family knowledge and structural principles, not on recalling this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span four distinct EC classes (translocase, transferase, ligase, oxidoreductase). The sequence lacks any motif characteristic of ABC transporters (A), acyltransferases (B), or cytochrome P450s (D), while clearly matching the NadE fold. Only C is defensible.


### Important caveats

- The EC annotation in UniProt is assigned by HAMAP-Rule (ECO:0000255), a computational/profiling method, not direct experimental kinetics. The PubMed reference (38429435) provides structural and genetic (disruption phenotype) evidence but not purified-enzyme kinetics.
- The query sequence is nearly identical to E. coli NadE (P0A6E2) apart from a short N-terminal 'MME' extension, which makes family recognition easier than for a more divergent NadE homolog.
- The reviewer-only evidence was not available to the evaluated model; the reasoning above relies solely on sequence features and transferable NadE-family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 552-aa sequence displays the hallmark two-domain architecture of NadE (glutamine-dependent NAD+ synthetase): an N-terminal glutamine amidotransferase (GAT) domain with a catalytic Cys (visible in the 'AHCEQ' region around residue ~75) and a C-terminal synthetase domain containing conserved motifs for ATP/NAD+ binding. This architecture is shared across NadE homologs in bacteria and plants. Against the offered distractors: (A) EC 5.6.2.4 is an ABC-transporter translocase requiring Walker A (GxxGxGKS/T), Walker B, and ABC signature (LSGGQ) motifs — none are present; (B) EC 2.3.1.193 is a small (~200–300 aa) acyltransferase with a HxxxD or DIL motif — the protein is far too large and lacks such motifs; (D) EC 1.14.19.80 is a cytochrome P450 requiring the conserved heme-binding FxxGxxxCxG motif — absent here. The GAT+synthetase fold, the ~550-aa length, and the absence of motifs diagnostic of the other three enzyme classes collectively point to EC 6.3.5.1, a family-level inference transferable from well-characterized NadE proteins (e.g., E. coli, B. subtilis, plant homologs).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the NadE protein family can recognize the two-domain GAT/synthetase architecture, the characteristic length, and conserved motifs, and can exclude the three distractors by the absence of their defining motifs (Walker A/B for ABC transporters, HxxxD for acyltransferases, FxxGxxxCxG for P450s). The sequence is in fact >95% identical to E. coli NadE (P0A6E2), making family recognition straightforward. The inference relies on transferable family knowledge and structural principles, not on recalling this exact protein's database record."
  },
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 (NADE_XANC8) annotates this 552-aa protein as Glutamine-dependent NAD(+) synthetase with EC 6.3.5.1. The EC number is assigned via HAMAP-Rule MF_02090 (ECO:0000255, computational/profiling evidence), and the entry also cites PubMed:38429435 (structural and disruption-phenotype study in Xanthomonas campestris) providing experimental context. The catalytic reaction (deamido-NAD+ + L-glutamine + ATP + H2O → L-glutamate + AMP + diphosphate + NAD+ + H+) matches EC 6.3.5.1. Sequence match is confirmed (SHA-256 identical)."
  },
  "important_caveats": [
    "The EC annotation in UniProt is assigned by HAMAP-Rule (ECO:0000255), a computational/profiling method, not direct experimental kinetics. The PubMed reference (38429435) provides structural and genetic (disruption phenotype) evidence but not purified-enzyme kinetics.",
    "The query sequence is nearly identical to E. coli NadE (P0A6E2) apart from a short N-terminal 'MME' extension, which makes family recognition easier than for a more divergent NadE homolog.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning above relies solely on sequence features and transferable NadE-family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct EC classes (translocase, transferase, ligase, oxidoreductase). The sequence lacks any motif characteristic of ABC transporters (A), acyltransferases (B), or cytochrome P450s (D), while clearly matching the NadE fold. Only C is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 (NADE_XANC8) annotates this 552-aa protein as Glutamine-dependent NAD(+) synthetase with EC 6.3.5.1. The EC number is assigned via HAMAP-Rule MF_02090 (ECO:0000255, computational/profiling evidence), and the entry also cites PubMed:38429435 (structural and disruption-phenotype study in Xanthomonas campestris) providing experimental context. The catalytic reaction (deamido-NAD+ + L-glutamine + ATP + H2O → L-glutamate + AMP + diphosphate + NAD+ + H+) matches EC 6.3.5.1. Sequence match is confirmed (SHA-256 identical).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 552-aa sequence displays the hallmark two-domain architecture of NadE (glutamine-dependent NAD+ synthetase): an N-terminal glutamine amidotransferase (GAT) domain with a catalytic Cys (visible in the 'AHCEQ' region around residue ~75) and a C-terminal synthetase domain containing conserved motifs for ATP/NAD+ binding. This architecture is shared across NadE homologs in bacteria and plants. Against the offered distractors: (A) EC 5.6.2.4 is an ABC-transporter translocase requiring Walker A (GxxGxGKS/T), Walker B, and ABC signature (LSGGQ) motifs — none are present; (B) EC 2.3.1.193 is a small (~200–300 aa) acyltransferase with a HxxxD or DIL motif — the protein is far too large and lacks such motifs; (D) EC 1.14.19.80 is a cytochrome P450 requiring the conserved heme-binding FxxGxxxCxG motif — absent here. The GAT+synthetase fold, the ~550-aa length, and the absence of motifs diagnostic of the other three enzyme classes collectively point to EC 6.3.5.1, a family-level inference transferable from well-characterized NadE proteins (e.g., E. coli, B. subtilis, plant homologs).",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the NadE protein family can recognize the two-domain GAT/synthetase architecture, the characteristic length, and conserved motifs, and can exclude the three distractors by the absence of their defining motifs (Walker A/B for ABC transporters, HxxxD for acyltransferases, FxxGxxxCxG for P450s). The sequence is in fact >95% identical to E. coli NadE (P0A6E2), making family recognition straightforward. The inference relies on transferable family knowledge and structural principles, not on recalling this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct EC classes (translocase, transferase, ligase, oxidoreductase). The sequence lacks any motif characteristic of ABC transporters (A), acyltransferases (B), or cytochrome P450s (D), while clearly matching the NadE fold. Only C is defensible."
  },
  "important_caveats": [
    "The EC annotation in UniProt is assigned by HAMAP-Rule (ECO:0000255), a computational/profiling method, not direct experimental kinetics. The PubMed reference (38429435) provides structural and genetic (disruption phenotype) evidence but not purified-enzyme kinetics.",
    "The query sequence is nearly identical to E. coli NadE (P0A6E2) apart from a short N-terminal 'MME' extension, which makes family recognition easier than for a more divergent NadE homolog.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning above relies solely on sequence features and transferable NadE-family knowledge."
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
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"6.3.5.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"name\":\"deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24384\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29985\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58437\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
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
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};\nDE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};\nDE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};\nDE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};\nDE            Short=NADS {ECO:0000303|PubMed:38429435};\n",
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
  "source_locator": "lines 28-36",
  "excerpt": "RN   [2]\nRP   DISRUPTION PHENOTYPE.\nRC   STRAIN=8004;\nRX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;\nRA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,\nRA   Shi X., Tang D.J., Tang J.L., Ming Z.;\nRT   \"Structural insights into Xanthomonas campestris pv. campestris NAD+\nRT   biosynthesis via the NAM salvage pathway.\";\nRL   Commun. Biol. 7:255-255(2024).\n",
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
  "source_locator": "lines 40-46",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP +\nCC         diphosphate + NAD(+) + H(+); Xref=Rhea:RHEA:24384, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29985, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:33019, ChEBI:CHEBI:57540, ChEBI:CHEBI:58359,\nCC         ChEBI:CHEBI:58437, ChEBI:CHEBI:456215; EC=6.3.5.1;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_02090};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 49,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 88. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
