# EC_number_0147: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0147.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **A** — 3.2.2.5

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
MVKVDLESKRYGEKLKEVFLMLDNNVVECIKEITESSRNGKLVFFVGAGVSTLSDYPQWWRLVDKYHEELYGSPKKGNYSSDEYLRIPQIFYNVKGEMAFDGILKDFFQVDKPTNPIHDKILAMNPAHVITTNYDNLIDTACWKRGKYFSVISAEEDVANATSSRYLLKVHGDFRKGFKGENVVLKEDDYLNYDQNYPLISNLMKTIIATHTIVFIGYGLGDYNINMLLNWVRKLQKDSFHKPFFIRTDPSPIENETLIYYENKGLRIIDAASLIDSNEYDYLERYSAVMDLLIESQENKFITKDDEVIDYIYGKISPLFALQYIRKIDLKHVFEYDYHFEVNGTVVRHKNKGFGYMERFFELKESCDERSKLSKKQYERFNALFNFFEKNGVICMAKDAGTLNTSIEINSLAYHGKYDVMKKFIEEQSVSIEDDYKKAFFLACLGRWEESYDLYSNIILNSIDESNGCVYYLSQINRYRIYQSITQAVTQFNGLGLLTFGRHYKPFTDEFLARIEREMTNFNIDDLFNGMPFEFQKKYKILEFLSDNQFLYDDTVKLFELTNKVRSEMSEGSYSFGMSSDIVVLLRLYDNLRFLYENCLWSVSFHEFHQYIRNSMSLLIEKAEYERTRDIDELGFSFFGKKSGFFMEYYDFVNISRHFKIDDIKNLERSCSIDKIRFGEQEKIEEYLVGIAEEITKQFSANGMNVVFYTQFISEAKAALYFAKYVKLSEEGLGKIVKALLFYFPERDLDIGKRYVWLERLTKCNELPKSIISIIDDFLVLQAEKHIDQNYSEVSSNGLYSRDYGALIKHFEKNFISKRLSEITLCLTQDKQKQIDFLFKLLPLLSTNAKSHLLSFKSVENINDLMNGIRIGLIDEFTPEHEELIIEYLETRKVNYIVEKEKGIQTFSSNDYMSTFGIWYFLEEINNSKMEEFIGMDDQYDFFVDPENFDYKKFIPSWLKNYNDKLLGKIAGNKHMKHHVIEVLKERVKNSNDKRYLEILMNYFI

[Multiple Choices]
A. 3.2.2.5
B. 3.2.2.27
C. 1.11.1.24
D. 5.4.99.14
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

> The supplied sequence exactly matches the 1005-aa UniProtKB P0DXN8 sequence. Its historical UniProt entry assigns EC 3.2.2.5 and gives the reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+), with ECO:0000269 evidence linked to publications. This supports choice A for the matched protein, while the cited evidence has not been independently checked here.

Citations as saved: [H1](#evidence-h1), [H9](#evidence-h9), [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support recognizing a large protein with a sirtuin-like NAD-related enzyme domain, which makes the hydrolase-class option more plausible than the oxidoreductase or isomerase options. But that does not establish the precise EC subclass or this protein's NADase reaction.


**Missing item-specific fact**

> The protein-specific catalytic activity—hydrolysis of NAD(+) to ADP-D-ribose and nicotinamide, assigned EC 3.2.2.5—is not supplied in the question and is needed to distinguish the exact answer.


**Reason**

> The reviewer-only records support the key, but the evaluated input contains only sequence and choices. Inferring the complete EC number requires protein-specific functional knowledge or external annotation; recognizing the sequence or asserting a predictor could identify it would be lookup dependence, not reasoning support.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein's cited catalytic-activity annotation supports A; the other choices describe different EC classes or subclasses and are not supported by the supplied sequence alone.


### Important caveats

- The source accession and annotations are reviewer-only and were absent from the evaluated model input.
- The historical sequence match establishes source applicability, but the author's exact data-source snapshot is unknown.
- The annotation cites experimental evidence codes and publications; those primary studies were not independently retrieved or validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support recognizing a large protein with a sirtuin-like NAD-related enzyme domain, which makes the hydrolase-class option more plausible than the oxidoreductase or isomerase options. But that does not establish the precise EC subclass or this protein's NADase reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—hydrolysis of NAD(+) to ADP-D-ribose and nicotinamide, assigned EC 3.2.2.5—is not supplied in the question and is needed to distinguish the exact answer.",
    "reason": "The reviewer-only records support the key, but the evaluated input contains only sequence and choices. Inferring the complete EC number requires protein-specific functional knowledge or external annotation; recognizing the sequence or asserting a predictor could identify it would be lookup dependence, not reasoning support."
  },
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H9",
      "C1",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1005-aa UniProtKB P0DXN8 sequence. Its historical UniProt entry assigns EC 3.2.2.5 and gives the reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+), with ECO:0000269 evidence linked to publications. This supports choice A for the matched protein, while the cited evidence has not been independently checked here."
  },
  "important_caveats": [
    "The source accession and annotations are reviewer-only and were absent from the evaluated model input.",
    "The historical sequence match establishes source applicability, but the author's exact data-source snapshot is unknown.",
    "The annotation cites experimental evidence codes and publications; those primary studies were not independently retrieved or validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's cited catalytic-activity annotation supports A; the other choices describe different EC classes or subclasses and are not supported by the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1005-aa UniProtKB P0DXN8 sequence. Its historical UniProt entry assigns EC 3.2.2.5 and gives the reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+), with ECO:0000269 evidence linked to publications. This supports choice A for the matched protein, while the cited evidence has not been independently checked here.",
    "evidence_ids": ["H1", "H9", "C1", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support recognizing a large protein with a sirtuin-like NAD-related enzyme domain, which makes the hydrolase-class option more plausible than the oxidoreductase or isomerase options. But that does not establish the precise EC subclass or this protein's NADase reaction.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—hydrolysis of NAD(+) to ADP-D-ribose and nicotinamide, assigned EC 3.2.2.5—is not supplied in the question and is needed to distinguish the exact answer.",
    "reason": "The reviewer-only records support the key, but the evaluated input contains only sequence and choices. Inferring the complete EC number requires protein-specific functional knowledge or external annotation; recognizing the sequence or asserting a predictor could identify it would be lookup dependence, not reasoning support."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's cited catalytic-activity annotation supports A; the other choices describe different EC classes or subclasses and are not supported by the supplied sequence alone."
  },
  "important_caveats": [
    "The source accession and annotations are reviewer-only and were absent from the evaluated model input.",
    "The historical sequence match establishes source applicability, but the author's exact data-source snapshot is unknown.",
    "The annotation cites experimental evidence codes and publications; those primary studies were not independently retrieved or validated here."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt P0DXN8 (DSR2, Defense-associated sirtuin 2 from Bacillus subtilis) is annotated with EC 3.2.2.5 (NAD(+) glycohydrolase) backed by experimental evidence (ECO:0000269) from six independent PubMed publications (36192536, 38538592, 38555355, 38729958, 39039073, 39059542). The catalytic reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+) is confirmed. The sequence matches the benchmark input exactly (1005 AA, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~1005 AA) contains sirtuin-like catalytic domain features (conserved motifs associated with NAD+ binding and the sirtuin fold). Sirtuins are well-established NAD+-dependent enzymes. Among the four options, EC 1.11.1.24 (oxidoreductase/peroxidase) and EC 5.4.99.14 (isomerase/translocase) belong to entirely different enzyme classes and are incompatible with a sirtuin-like hydrolase. EC 3.2.2.27 does not correspond to a recognized NAD+-related glycosylase. EC 3.2.2.5 (NAD+ glycohydrolase) is the canonical EC number for NAD+ cleavage, the hallmark reaction of sirtuin-family enzymes. A model recognizing sirtuin-like sequence features can eliminate C and D by enzyme class and select A over B by associating the sirtuin fold with NAD+ glycohydrolase activity.


**Missing item-specific fact**

> The specific discovery that DSR2 functions as an NADase (rather than a protein deacetylase) is a 2022 experimental finding. However, since no deacetylase EC number (e.g., EC 3.5.1.-) appears among the options, this distinction does not impede selection of the correct answer from the given choices.


**Reason**

> The reasoning path—recognize sirtuin-like sequence → NAD+-dependent hydrolase → NAD+ glycohydrolase (EC 3.2.2.5)—relies on general knowledge of sirtuin biochemistry and EC classification logic. The distractors C and D are in wholly different enzyme classes, and B is not a recognized NAD+-cleaving glycosylase. This provides meaningful grounds to distinguish the answer without memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> EC 1.11.1.24 (oxidoreductase) and EC 5.4.99.14 (isomerase) are in incompatible enzyme classes for a sirtuin-like protein. EC 3.2.2.27 is not a recognized NAD+-related glycosylase. Only EC 3.2.2.5 aligns with both the sirtuin fold and NAD+ cleavage chemistry.


### Important caveats

- The annotation of DSR2 as EC 3.2.2.5 was established experimentally starting in 2022 (Garb et al., Nat. Microbiol.), so the entry is relatively recent. A model trained on older data might not have this specific association, but the sirtuin→NAD+→EC 3.2.2.5 reasoning path remains valid.
- The distinction between sirtuin NADase activity and sirtuin deacetylase activity is mechanistically specific; however, no deacetylase EC number is offered as a distractor, so this does not create ambiguity in the answer set.
- Sequence-match is confirmed (SHA256 identical), so the evidence applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~1005 AA) contains sirtuin-like catalytic domain features (conserved motifs associated with NAD+ binding and the sirtuin fold). Sirtuins are well-established NAD+-dependent enzymes. Among the four options, EC 1.11.1.24 (oxidoreductase/peroxidase) and EC 5.4.99.14 (isomerase/translocase) belong to entirely different enzyme classes and are incompatible with a sirtuin-like hydrolase. EC 3.2.2.27 does not correspond to a recognized NAD+-related glycosylase. EC 3.2.2.5 (NAD+ glycohydrolase) is the canonical EC number for NAD+ cleavage, the hallmark reaction of sirtuin-family enzymes. A model recognizing sirtuin-like sequence features can eliminate C and D by enzyme class and select A over B by associating the sirtuin fold with NAD+ glycohydrolase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific discovery that DSR2 functions as an NADase (rather than a protein deacetylase) is a 2022 experimental finding. However, since no deacetylase EC number (e.g., EC 3.5.1.-) appears among the options, this distinction does not impede selection of the correct answer from the given choices.",
    "reason": "The reasoning path—recognize sirtuin-like sequence → NAD+-dependent hydrolase → NAD+ glycohydrolase (EC 3.2.2.5)—relies on general knowledge of sirtuin biochemistry and EC classification logic. The distractors C and D are in wholly different enzyme classes, and B is not a recognized NAD+-cleaving glycosylase. This provides meaningful grounds to distinguish the answer without memorizing this specific protein's database entry."
  },
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H9"
    ],
    "judgment": "supported",
    "reason": "UniProt P0DXN8 (DSR2, Defense-associated sirtuin 2 from Bacillus subtilis) is annotated with EC 3.2.2.5 (NAD(+) glycohydrolase) backed by experimental evidence (ECO:0000269) from six independent PubMed publications (36192536, 38538592, 38555355, 38729958, 39039073, 39059542). The catalytic reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+) is confirmed. The sequence matches the benchmark input exactly (1005 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The annotation of DSR2 as EC 3.2.2.5 was established experimentally starting in 2022 (Garb et al., Nat. Microbiol.), so the entry is relatively recent. A model trained on older data might not have this specific association, but the sirtuin→NAD+→EC 3.2.2.5 reasoning path remains valid.",
    "The distinction between sirtuin NADase activity and sirtuin deacetylase activity is mechanistically specific; however, no deacetylase EC number is offered as a distractor, so this does not create ambiguity in the answer set.",
    "Sequence-match is confirmed (SHA256 identical), so the evidence applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 1.11.1.24 (oxidoreductase) and EC 5.4.99.14 (isomerase) are in incompatible enzyme classes for a sirtuin-like protein. EC 3.2.2.27 is not a recognized NAD+-related glycosylase. Only EC 3.2.2.5 aligns with both the sirtuin fold and NAD+ cleavage chemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt P0DXN8 (DSR2, Defense-associated sirtuin 2 from Bacillus subtilis) is annotated with EC 3.2.2.5 (NAD(+) glycohydrolase) backed by experimental evidence (ECO:0000269) from six independent PubMed publications (36192536, 38538592, 38555355, 38729958, 39039073, 39059542). The catalytic reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+) is confirmed. The sequence matches the benchmark input exactly (1005 AA, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "H2", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~1005 AA) contains sirtuin-like catalytic domain features (conserved motifs associated with NAD+ binding and the sirtuin fold). Sirtuins are well-established NAD+-dependent enzymes. Among the four options, EC 1.11.1.24 (oxidoreductase/peroxidase) and EC 5.4.99.14 (isomerase/translocase) belong to entirely different enzyme classes and are incompatible with a sirtuin-like hydrolase. EC 3.2.2.27 does not correspond to a recognized NAD+-related glycosylase. EC 3.2.2.5 (NAD+ glycohydrolase) is the canonical EC number for NAD+ cleavage, the hallmark reaction of sirtuin-family enzymes. A model recognizing sirtuin-like sequence features can eliminate C and D by enzyme class and select A over B by associating the sirtuin fold with NAD+ glycohydrolase activity.",
    "missing_item_specific_fact": "The specific discovery that DSR2 functions as an NADase (rather than a protein deacetylase) is a 2022 experimental finding. However, since no deacetylase EC number (e.g., EC 3.5.1.-) appears among the options, this distinction does not impede selection of the correct answer from the given choices.",
    "reason": "The reasoning path—recognize sirtuin-like sequence → NAD+-dependent hydrolase → NAD+ glycohydrolase (EC 3.2.2.5)—relies on general knowledge of sirtuin biochemistry and EC classification logic. The distractors C and D are in wholly different enzyme classes, and B is not a recognized NAD+-cleaving glycosylase. This provides meaningful grounds to distinguish the answer without memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 1.11.1.24 (oxidoreductase) and EC 5.4.99.14 (isomerase) are in incompatible enzyme classes for a sirtuin-like protein. EC 3.2.2.27 is not a recognized NAD+-related glycosylase. Only EC 3.2.2.5 aligns with both the sirtuin fold and NAD+ cleavage chemistry."
  },
  "important_caveats": [
    "The annotation of DSR2 as EC 3.2.2.5 was established experimentally starting in 2022 (Garb et al., Nat. Microbiol.), so the entry is relatively recent. A model trained on older data might not have this specific association, but the sirtuin→NAD+→EC 3.2.2.5 reasoning path remains valid.",
    "The distinction between sirtuin NADase activity and sirtuin deacetylase activity is mechanistically specific; however, no deacetylase EC number is offered as a distractor, so this does not create ambiguity in the answer set.",
    "Sequence-match is confirmed (SHA256 identical), so the evidence applies directly to the supplied sequence."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns EC 3.2.2.5 and reports the corresponding NAD+ hydrolysis reaction with experimental evidence codes (ECO:0000269). This supports the key beyond a computational or similarity-based annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a large defense-associated sirtuin containing an NAD-dependent catalytic module. Sirtuin-family knowledge provides a meaningful route to NAD-consuming activity, including NAD glycohydrolase activity, supporting A (3.2.2.5) over the offered oxidoreductase, isomerase, and alternative hydrolase choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence and functional patterns can distinguish the NAD-hydrolyzing sirtuin option among these alternatives without recalling this exact protein's database entry. The sequence alone may not establish the precise reaction experimentally, but the offered choices make the family inference meaningful.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the sirtuin-associated NAD glycohydrolase classification is the defensible match; the alternatives describe distinct enzyme activities.


### Important caveats

- The reviewer-only records match the supplied sequence and cite experimental evidence, but those records were not part of the original model input.
- The sequence-based family inference is probabilistic; exact EC assignment ultimately depends on the enzyme's catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large defense-associated sirtuin containing an NAD-dependent catalytic module. Sirtuin-family knowledge provides a meaningful route to NAD-consuming activity, including NAD glycohydrolase activity, supporting A (3.2.2.5) over the offered oxidoreductase, isomerase, and alternative hydrolase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and functional patterns can distinguish the NAD-hydrolyzing sirtuin option among these alternatives without recalling this exact protein's database entry. The sequence alone may not establish the precise reaction experimentally, but the offered choices make the family inference meaningful."
  },
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.2.5 and reports the corresponding NAD+ hydrolysis reaction with experimental evidence codes (ECO:0000269). This supports the key beyond a computational or similarity-based annotation."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence and cite experimental evidence, but those records were not part of the original model input.",
    "The sequence-based family inference is probabilistic; exact EC assignment ultimately depends on the enzyme's catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sirtuin-associated NAD glycohydrolase classification is the defensible match; the alternatives describe distinct enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.2.5 and reports the corresponding NAD+ hydrolysis reaction with experimental evidence codes (ECO:0000269). This supports the key beyond a computational or similarity-based annotation.",
    "evidence_ids": ["C4", "C5", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a large defense-associated sirtuin containing an NAD-dependent catalytic module. Sirtuin-family knowledge provides a meaningful route to NAD-consuming activity, including NAD glycohydrolase activity, supporting A (3.2.2.5) over the offered oxidoreductase, isomerase, and alternative hydrolase choices.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and functional patterns can distinguish the NAD-hydrolyzing sirtuin option among these alternatives without recalling this exact protein's database entry. The sequence alone may not establish the precise reaction experimentally, but the offered choices make the family inference meaningful."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sirtuin-associated NAD glycohydrolase classification is the defensible match; the alternatives describe distinct enzyme activities."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence and cite experimental evidence, but those records were not part of the original model input.",
    "The sequence-based family inference is probabilistic; exact EC assignment ultimately depends on the enzyme's catalytic activity."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXN8 (DSR2_BACIU, 1005 AA, Bacillus subtilis) is annotated with EC 3.2.2.5 (NAD(+) glycohydrolase) supported by multiple experimental evidence codes (ECO:0000269) from six independent publications (2022–2024). The catalytic reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+) is confirmed by structural (cryo-EM) and biochemical studies. The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable sirtuin catalytic domain, identifiable by the conserved GAG NAD+-binding motif ('VFFVGAGVSTLSDY') and the overall Rossmann-fold architecture typical of the Sir2/sirtuin superfamily. Sirtuins are NAD+-dependent enzymes. Among the four options, C (1.11.1.24, peroxidase) and D (5.4.99.14, transglutaminase) are unrelated enzyme classes with no sirtuin-like features. The real discrimination is between A (3.2.2.5, NAD(+) glycohydrolase producing ADP-ribose + nicotinamide) and B (3.2.2.27, ADP-ribosyl cyclase producing cyclic ADP-ribose). From family-level knowledge: sirtuin-domain proteins (Sir2, bacterial sirtuins, DSR family) classically hydrolyze NAD+ to linear ADP-ribose + nicotinamide (EC 3.2.2.5), whereas ADP-ribosyl cyclase activity (3.2.2.27) is characteristic of the CD38/cADPR synthase family, which has a distinct structural fold. The sirtuin GAG motif and overall domain architecture are hallmarks of the NADase (3.2.2.5) reaction, not the cyclase reaction. This family-level inference meaningfully distinguishes A from B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the sirtuin domain from the GAG motif and Rossmann-fold architecture, recognize that sirtuins are NAD+-hydrolyzing enzymes, and use family-level knowledge to distinguish the sirtuin-associated NADase product (ADP-ribose + nicotinamide, EC 3.2.2.5) from the CD38-type cyclase product (cyclic ADP-ribose, EC 3.2.2.27). Options C and D are eliminated as unrelated enzyme classes. This is a defensible transferable inference from sirtuin-family biochemistry, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly unrelated enzyme classes (peroxidase, transglutaminase) with no sirtuin features. Between A and B, the sirtuin-domain identification and the well-established biochemical distinction between sirtuin NADase (linear ADP-ribose product) and CD38-type ADP-ribosyl cyclase (cyclic ADP-ribose product) provide a clear discriminator. No genuine ambiguity remains among the offered choices.


### Important caveats

- DSR2 was only functionally characterized in 2022–2024; the specific NADase assignment to DSR2 required experimental work. However, the general principle that sirtuin-domain proteins catalyze NAD+ hydrolysis (EC 3.2.2.5) rather than cyclic ADP-ribose formation (EC 3.2.2.27) is well-established family knowledge predating DSR2's characterization.
- The sequence is 1005 residues long, consistent with the full-length DSR2 protein including N-terminal and C-terminal regulatory domains beyond the sirtuin catalytic core.
- The GAG motif identification is a heuristic; not every sirtuin has a perfect GAG motif, but the overall domain architecture and length support sirtuin family membership.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable sirtuin catalytic domain, identifiable by the conserved GAG NAD+-binding motif ('VFFVGAGVSTLSDY') and the overall Rossmann-fold architecture typical of the Sir2/sirtuin superfamily. Sirtuins are NAD+-dependent enzymes. Among the four options, C (1.11.1.24, peroxidase) and D (5.4.99.14, transglutaminase) are unrelated enzyme classes with no sirtuin-like features. The real discrimination is between A (3.2.2.5, NAD(+) glycohydrolase producing ADP-ribose + nicotinamide) and B (3.2.2.27, ADP-ribosyl cyclase producing cyclic ADP-ribose). From family-level knowledge: sirtuin-domain proteins (Sir2, bacterial sirtuins, DSR family) classically hydrolyze NAD+ to linear ADP-ribose + nicotinamide (EC 3.2.2.5), whereas ADP-ribosyl cyclase activity (3.2.2.27) is characteristic of the CD38/cADPR synthase family, which has a distinct structural fold. The sirtuin GAG motif and overall domain architecture are hallmarks of the NADase (3.2.2.5) reaction, not the cyclase reaction. This family-level inference meaningfully distinguishes A from B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the sirtuin domain from the GAG motif and Rossmann-fold architecture, recognize that sirtuins are NAD+-hydrolyzing enzymes, and use family-level knowledge to distinguish the sirtuin-associated NADase product (ADP-ribose + nicotinamide, EC 3.2.2.5) from the CD38-type cyclase product (cyclic ADP-ribose, EC 3.2.2.27). Options C and D are eliminated as unrelated enzyme classes. This is a defensible transferable inference from sirtuin-family biochemistry, not a lookup of this specific protein's annotation."
  },
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXN8 (DSR2_BACIU, 1005 AA, Bacillus subtilis) is annotated with EC 3.2.2.5 (NAD(+) glycohydrolase) supported by multiple experimental evidence codes (ECO:0000269) from six independent publications (2022–2024). The catalytic reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+) is confirmed by structural (cryo-EM) and biochemical studies. The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "DSR2 was only functionally characterized in 2022–2024; the specific NADase assignment to DSR2 required experimental work. However, the general principle that sirtuin-domain proteins catalyze NAD+ hydrolysis (EC 3.2.2.5) rather than cyclic ADP-ribose formation (EC 3.2.2.27) is well-established family knowledge predating DSR2's characterization.",
    "The sequence is 1005 residues long, consistent with the full-length DSR2 protein including N-terminal and C-terminal regulatory domains beyond the sirtuin catalytic core.",
    "The GAG motif identification is a heuristic; not every sirtuin has a perfect GAG motif, but the overall domain architecture and length support sirtuin family membership."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly unrelated enzyme classes (peroxidase, transglutaminase) with no sirtuin features. Between A and B, the sirtuin-domain identification and the well-established biochemical distinction between sirtuin NADase (linear ADP-ribose product) and CD38-type ADP-ribosyl cyclase (cyclic ADP-ribose product) provide a clear discriminator. No genuine ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXN8 (DSR2_BACIU, 1005 AA, Bacillus subtilis) is annotated with EC 3.2.2.5 (NAD(+) glycohydrolase) supported by multiple experimental evidence codes (ECO:0000269) from six independent publications (2022–2024). The catalytic reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+) is confirmed by structural (cryo-EM) and biochemical studies. The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "H1", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable sirtuin catalytic domain, identifiable by the conserved GAG NAD+-binding motif ('VFFVGAGVSTLSDY') and the overall Rossmann-fold architecture typical of the Sir2/sirtuin superfamily. Sirtuins are NAD+-dependent enzymes. Among the four options, C (1.11.1.24, peroxidase) and D (5.4.99.14, transglutaminase) are unrelated enzyme classes with no sirtuin-like features. The real discrimination is between A (3.2.2.5, NAD(+) glycohydrolase producing ADP-ribose + nicotinamide) and B (3.2.2.27, ADP-ribosyl cyclase producing cyclic ADP-ribose). From family-level knowledge: sirtuin-domain proteins (Sir2, bacterial sirtuins, DSR family) classically hydrolyze NAD+ to linear ADP-ribose + nicotinamide (EC 3.2.2.5), whereas ADP-ribosyl cyclase activity (3.2.2.27) is characteristic of the CD38/cADPR synthase family, which has a distinct structural fold. The sirtuin GAG motif and overall domain architecture are hallmarks of the NADase (3.2.2.5) reaction, not the cyclase reaction. This family-level inference meaningfully distinguishes A from B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the sirtuin domain from the GAG motif and Rossmann-fold architecture, recognize that sirtuins are NAD+-hydrolyzing enzymes, and use family-level knowledge to distinguish the sirtuin-associated NADase product (ADP-ribose + nicotinamide, EC 3.2.2.5) from the CD38-type cyclase product (cyclic ADP-ribose, EC 3.2.2.27). Options C and D are eliminated as unrelated enzyme classes. This is a defensible transferable inference from sirtuin-family biochemistry, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly unrelated enzyme classes (peroxidase, transglutaminase) with no sirtuin features. Between A and B, the sirtuin-domain identification and the well-established biochemical distinction between sirtuin NADase (linear ADP-ribose product) and CD38-type ADP-ribosyl cyclase (cyclic ADP-ribose product) provide a clear discriminator. No genuine ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "DSR2 was only functionally characterized in 2022–2024; the specific NADase assignment to DSR2 required experimental work. However, the general principle that sirtuin-domain proteins catalyze NAD+ hydrolysis (EC 3.2.2.5) rather than cyclic ADP-ribose formation (EC 3.2.2.27) is well-established family knowledge predating DSR2's characterization.",
    "The sequence is 1005 residues long, consistent with the full-length DSR2 protein including N-terminal and C-terminal regulatory domains beyond the sirtuin catalytic core.",
    "The GAG motif identification is a heuristic; not every sirtuin has a perfect GAG motif, but the overall domain architecture and length support sirtuin family membership."
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
  "requested_accession": "P0DXN8",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "a332c6e633f60b28e85281a737e0528d5b23210a87c285627c304ff5d2412161",
  "benchmark_sequence_length": 1005,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "current_source_sequence_sha256": "a332c6e633f60b28e85281a737e0528d5b23210a87c285627c304ff5d2412161",
  "current_source_sequence_length": 1005,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 4,
  "selected_historical_version": {
    "accession": "P0DXN8",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DSR2_BACIU",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "selected_historical_source_sequence_sha256": "a332c6e633f60b28e85281a737e0528d5b23210a87c285627c304ff5d2412161",
  "selected_historical_source_sequence_length": 1005,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P0DXN8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\"],\"scientificName\":\"Bacillus subtilis\",\"taxonId\":1423}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36192536\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38538592\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38555355\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38729958\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39039073\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39059542\",\"source\":\"PubMed\"}],\"value\":\"3.2.2.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36192536\",\"source\":\"PubMed\"}],\"value\":\"Defense-associated sirtuin 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36192536\",\"source\":\"PubMed\"}],\"value\":\"DSR2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36192536\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38538592\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38555355\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38729958\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39039073\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39059542\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:16302\"}}],\"reaction\":{\"ecNumber\":\"3.2.2.5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36192536\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38538592\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38555355\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38729958\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39039073\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39059542\",\"source\":\"PubMed\"}],\"name\":\"NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:16301\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17154\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57967\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Garb J.\",\"Lopatina A.\",\"Bernheim A.\",\"Zaremba M.\",\"Siksnys V.\",\"Melamed S.\",\"Leavitt A.\",\"Millman A.\",\"Amitai G.\",\"Sorek R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36192536\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41564-022-01207-8\"}],\"citationType\":\"journal article\",\"firstPage\":\"1849\",\"id\":\"36192536\",\"journal\":\"Nat. Microbiol.\",\"lastPage\":\"1856\",\"publicationDate\":\"2022\",\"title\":\"Multiple phage resistance systems inhibit infection via SIR2-dependent NAD+ depletion.\",\"volume\":\"7\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DOMAIN\",\"MUTAGENESIS OF ASN-133 AND HIS-171\",\"INTERACTION WITH PHAGE SPR TAIL TUBE PROTEIN (MICROBIAL INFECTION)\",\"ACTIVITY REGULATION (MICROBIAL INFECTION)\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang R.\",\"Xu Q.\",\"Wu Z.\",\"Li J.\",\"Guo H.\",\"Liao T.\",\"Shi Y.\",\"Yuan L.\",\"Gao H.\",\"Yang R.\",\"Shi Z.\",\"Li F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39039073\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-50410-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"6185\",\"id\":\"39039073\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"6185\",\"publicationDate\":\"2024\",\"title\":\"The structural basis of the activation and inhibition of DSR2 NADase by phage proteins.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y13\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y34\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y3M\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y3W\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Y3Y\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZC9\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":3,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.11 ANGSTROMS) OF MUTANT HIS-171\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.14 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN AND NAD\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.25 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"FUNCTION\",\"SUBUNIT\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"MUTAGENESIS OF TYR-260\",\"NAD-BINDING\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"ACTIVE SITE\",\"MUTAGENESIS OF TYR-134; ASP-135 AND HIS-171\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang J.T.\",\"Liu X.Y.\",\"Li Z.\",\"Wei X.Y.\",\"Song X.Y.\",\"Cui N.\",\"Zhong J.\",\"Li H.\",\"Jia N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38555355\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-47177-9\"}],\"citationType\":\"journal article\",\"firstPage\":\"2797\",\"id\":\"38555355\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2797\",\"publicationDate\":\"2024\",\"title\":\"Structural basis for phage-mediated activation and repression of bacterial DSR2 anti-phage defense system.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYA\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYB\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYC\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYD\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WYF\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":4,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.37 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN AND NAD\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.62 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (2.56 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"STRUCTURE BY ELECTRON MICROSCOPY (2.85 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1 AND NAD\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"DOMAIN\",\"SUBUNIT\",\"MUTAGENESIS OF TRP-59; TYR-71; ASN-133; ASP-135; ASP-188 AND TYR-282\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"ACTIVITY REGULATION (MICROBIAL INFECTION)\",\"CATALYTIC ACTIVITY\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Huang J.\",\"Zhu K.\",\"Gao Y.\",\"Ye F.\",\"Li Z.\",\"Ge Y.\",\"Liu S.\",\"Yang J.\",\"Gao A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38729958\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-48291-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"3954\",\"id\":\"38729958\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"3954\",\"publicationDate\":\"2024\",\"title\":\"Molecular basis of bacterial DSR2 anti-phage defense and viral immune evasion.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKS\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKT\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKX\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":5,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (4.15 ANGSTROMS)\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.58 ANGSTROMS) OF 2-1005 IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.86 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"MUTAGENESIS OF 259-ILE-TYR-260\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"ACTIVITY REGULATION (MICROBIAL INFECTION)\",\"CATALYTIC ACTIVITY\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/references/5",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin H.\",\"Li X.\",\"Wang X.\",\"Zhang C.\",\"Gao J.\",\"Yu G.\",\"He Q.\",\"Yang J.\",\"Liu X.\",\"Wei Y.\",\"Li Z.\",\"Zhang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38538592\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-47030-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"2692\",\"id\":\"38538592\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2692\",\"publicationDate\":\"2024\",\"title\":\"Insights into the modulation of bacterial NADase activity by phage proteins.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8K98\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8K9A\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8W56\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WFN\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8WKN\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS)\",\"STRUCTURE BY ELECTRON MICROSCOPY (2.90 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"SUBUNIT\",\"DOMAIN\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"ACTIVITY REGULATION (MICROBIAL INFECTION)\",\"CATALYTIC ACTIVITY\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXN8.json",
  "source_sha256": "3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf",
  "retrieved_utc": "2026-11-02T04:29:34.653615+00:00",
  "json_pointer": "/references/6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.\",\"Wang Y.\",\"Zheng J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39059542\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2024.134145\"}],\"citationType\":\"journal article\",\"firstPage\":\"134145\",\"id\":\"39059542\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"134145\",\"publicationDate\":\"2024\",\"title\":\"Structural insights into autoinhibition and activation of defense-associated sirtuin protein.\",\"volume\":\"277\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8YKF\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8YL5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8YLN\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8YLT\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8Z18\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8ZTR\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"29R7-12 / 29R\"}],\"referenceNumber\":7,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.53 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.09 ANGSTROMS) IN COMPLEX WITH NAD\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.26 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN N-TERMINUS DOMAIN\",\"STRUCTURE BY ELECTRON MICROSCOPY (3.35 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1\",\"FUNCTION\",\"ACTIVITY REGULATION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION)\",\"INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION)\",\"ACTIVE SITE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   DSR2_BACIU              Reviewed;        1005 AA.\nAC   P0DXN8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Defense-associated sirtuin 2 {ECO:0000303|PubMed:36192536};\nDE            Short=DSR2 {ECO:0000303|PubMed:36192536};\nDE            EC=3.2.2.5 {ECO:0000269|PubMed:36192536, ECO:0000269|PubMed:38538592, ECO:0000269|PubMed:38555355, ECO:0000269|PubMed:38729958, ECO:0000269|PubMed:39039073, ECO:0000269|PubMed:39059542};\nGN   ORFNames=BKP58_08510;\nOS   Bacillus subtilis.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus.\nOX   NCBI_TaxID=1423;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=Defense-associated sirtuin 2 {ECO:0000303|PubMed:36192536};\nDE            Short=DSR2 {ECO:0000303|PubMed:36192536};\nDE            EC=3.2.2.5 {ECO:0000269|PubMed:36192536, ECO:0000269|PubMed:38538592, ECO:0000269|PubMed:38555355, ECO:0000269|PubMed:38729958, ECO:0000269|PubMed:39039073, ECO:0000269|PubMed:39059542};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "source_locator": "lines 22-32",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, DOMAIN, MUTAGENESIS OF ASN-133 AND HIS-171,\nRP   INTERACTION WITH PHAGE SPR TAIL TUBE PROTEIN (MICROBIAL INFECTION), AND\nRP   ACTIVITY REGULATION (MICROBIAL INFECTION).\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=36192536; DOI=10.1038/s41564-022-01207-8;\nRA   Garb J., Lopatina A., Bernheim A., Zaremba M., Siksnys V., Melamed S.,\nRA   Leavitt A., Millman A., Amitai G., Sorek R.;\nRT   \"Multiple phage resistance systems inhibit infection via SIR2-dependent\nRT   NAD+ depletion.\";\nRL   Nat. Microbiol. 7:1849-1856(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "source_locator": "lines 33-48",
  "excerpt": "RN   [3] {ECO:0007744|PDB:8Y13, ECO:0007744|PDB:8Y34, ECO:0007744|PDB:8Y3M, ECO:0007744|PDB:8Y3W, ECO:0007744|PDB:8Y3Y, ECO:0007744|PDB:8ZC9}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.11 ANGSTROMS) OF MUTANT HIS-171,\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.14 ANGSTROMS) IN COMPLEX WITH PHAGE SPR\nRP   TAIL TUBE PROTEIN AND NAD, STRUCTURE BY ELECTRON MICROSCOPY (3.25\nRP   ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1, FUNCTION, SUBUNIT, CATALYTIC\nRP   ACTIVITY, ACTIVITY REGULATION, MUTAGENESIS OF TYR-260, NAD-BINDING,\nRP   INTERACTION WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION), INTERACTION\nRP   WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION), ACTIVE SITE, AND MUTAGENESIS\nRP   OF TYR-134; ASP-135 AND HIS-171.\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=39039073; DOI=10.1038/s41467-024-50410-0;\nRA   Wang R., Xu Q., Wu Z., Li J., Guo H., Liao T., Shi Y., Yuan L., Gao H.,\nRA   Yang R., Shi Z., Li F.;\nRT   \"The structural basis of the activation and inhibition of DSR2 NADase by\nRT   phage proteins.\";\nRL   Nat. Commun. 15:6185-6185(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "source_locator": "lines 49-66",
  "excerpt": "RN   [4] {ECO:0007744|PDB:8WYA, ECO:0007744|PDB:8WYB, ECO:0007744|PDB:8WYC, ECO:0007744|PDB:8WYD, ECO:0007744|PDB:8WYE, ECO:0007744|PDB:8WYF}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.37 ANGSTROMS) IN COMPLEX WITH PHAGE SPR\nRP   TAIL TUBE PROTEIN AND NAD, STRUCTURE BY ELECTRON MICROSCOPY (3.62\nRP   ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN, STRUCTURE BY\nRP   ELECTRON MICROSCOPY (2.56 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1,\nRP   STRUCTURE BY ELECTRON MICROSCOPY (2.85 ANGSTROMS) IN COMPLEX WITH PHAGE\nRP   SPBETA DSAD1 AND NAD, INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL\nRP   INFECTION), DOMAIN, SUBUNIT, MUTAGENESIS OF TRP-59; TYR-71; ASN-133;\nRP   ASP-135; ASP-188 AND TYR-282, INTERACTION WITH PHAGE SPR TAIL TUBE\nRP   (MICROBIAL INFECTION), ACTIVITY REGULATION (MICROBIAL INFECTION), CATALYTIC\nRP   ACTIVITY, AND FUNCTION.\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=38555355; DOI=10.1038/s41467-024-47177-9;\nRA   Zhang J.T., Liu X.Y., Li Z., Wei X.Y., Song X.Y., Cui N., Zhong J., Li H.,\nRA   Jia N.;\nRT   \"Structural basis for phage-mediated activation and repression of bacterial\nRT   DSR2 anti-phage defense system.\";\nRL   Nat. Commun. 15:2797-2797(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "source_locator": "lines 67-80",
  "excerpt": "RN   [5] {ECO:0007744|PDB:8WKS, ECO:0007744|PDB:8WKT, ECO:0007744|PDB:8WKX}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (4.15 ANGSTROMS), STRUCTURE BY ELECTRON\nRP   MICROSCOPY (3.58 ANGSTROMS) OF 2-1005 IN COMPLEX WITH PHAGE SPR TAIL TUBE\nRP   PROTEIN, STRUCTURE BY ELECTRON MICROSCOPY (3.86 ANGSTROMS) IN COMPLEX WITH\nRP   PHAGE SPBETA DSAD1, MUTAGENESIS OF 259-ILE-TYR-260, INTERACTION WITH PHAGE\nRP   SPR TAIL TUBE (MICROBIAL INFECTION), ACTIVITY REGULATION (MICROBIAL\nRP   INFECTION), CATALYTIC ACTIVITY, INTERACTION WITH PHAGE SPBETA DSAD1\nRP   (MICROBIAL INFECTION), AND FUNCTION.\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=38729958; DOI=10.1038/s41467-024-48291-4;\nRA   Huang J., Zhu K., Gao Y., Ye F., Li Z., Ge Y., Liu S., Yang J., Gao A.;\nRT   \"Molecular basis of bacterial DSR2 anti-phage defense and viral immune\nRT   evasion.\";\nRL   Nat. Commun. 15:3954-3954(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "source_locator": "lines 81-94",
  "excerpt": "RN   [6] {ECO:0007744|PDB:8K98, ECO:0007744|PDB:8K9A, ECO:0007744|PDB:8W56, ECO:0007744|PDB:8WFN, ECO:0007744|PDB:8WKN}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS), STRUCTURE BY ELECTRON\nRP   MICROSCOPY (2.90 ANGSTROMS) IN COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN,\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS) IN COMPLEX WITH PHAGE\nRP   SPBETA DSAD1, SUBUNIT, DOMAIN, INTERACTION WITH PHAGE SPR TAIL TUBE\nRP   (MICROBIAL INFECTION), ACTIVITY REGULATION (MICROBIAL INFECTION), CATALYTIC\nRP   ACTIVITY, INTERACTION WITH PHAGE SPBETA DSAD1 (MICROBIAL INFECTION), AND\nRP   FUNCTION.\nRX   PubMed=38538592; DOI=10.1038/s41467-024-47030-z;\nRA   Yin H., Li X., Wang X., Zhang C., Gao J., Yu G., He Q., Yang J., Liu X.,\nRA   Wei Y., Li Z., Zhang H.;\nRT   \"Insights into the modulation of bacterial NADase activity by phage\nRT   proteins.\";\nRL   Nat. Commun. 15:2692-2692(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "source_locator": "lines 95-109",
  "excerpt": "RN   [7] {ECO:0007744|PDB:8YKF, ECO:0007744|PDB:8YL5, ECO:0007744|PDB:8YLN, ECO:0007744|PDB:8YLT, ECO:0007744|PDB:8Z18, ECO:0007744|PDB:8ZTR}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.53 ANGSTROMS) IN COMPLEX WITH PHAGE SPR\nRP   TAIL TUBE PROTEIN, STRUCTURE BY ELECTRON MICROSCOPY (3.09 ANGSTROMS) IN\nRP   COMPLEX WITH NAD, STRUCTURE BY ELECTRON MICROSCOPY (3.26 ANGSTROMS) IN\nRP   COMPLEX WITH PHAGE SPR TAIL TUBE PROTEIN N-TERMINUS DOMAIN, STRUCTURE BY\nRP   ELECTRON MICROSCOPY (3.35 ANGSTROMS) IN COMPLEX WITH PHAGE SPBETA DSAD1,\nRP   FUNCTION, ACTIVITY REGULATION, CATALYTIC ACTIVITY, SUBUNIT, INTERACTION\nRP   WITH PHAGE SPR TAIL TUBE (MICROBIAL INFECTION), INTERACTION WITH PHAGE\nRP   SPBETA DSAD1 (MICROBIAL INFECTION), AND ACTIVE SITE.\nRC   STRAIN=29R7-12 / 29R;\nRX   PubMed=39059542; DOI=10.1016/j.ijbiomac.2024.134145;\nRA   Yang X., Wang Y., Zheng J.;\nRT   \"Structural insights into autoinhibition and activation of defense-\nRT   associated sirtuin protein.\";\nRL   Int. J. Biol. Macromol. 277:134145-134145(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4",
  "source_sha256": "10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e",
  "retrieved_utc": "2026-11-02T04:29:41.291631+00:00",
  "source_locator": "lines 119-129",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+);\nCC         Xref=Rhea:RHEA:16301, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:17154, ChEBI:CHEBI:57540, ChEBI:CHEBI:57967; EC=3.2.2.5;\nCC         Evidence={ECO:0000269|PubMed:36192536, ECO:0000269|PubMed:38538592,\nCC         ECO:0000269|PubMed:38555355, ECO:0000269|PubMed:38729958,\nCC         ECO:0000269|PubMed:39039073, ECO:0000269|PubMed:39059542};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16302;\nCC         Evidence={ECO:0000269|PubMed:36192536, ECO:0000269|PubMed:38538592,\nCC         ECO:0000269|PubMed:38555355, ECO:0000269|PubMed:38729958,\nCC         ECO:0000269|PubMed:39039073, ECO:0000269|PubMed:39059542};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
