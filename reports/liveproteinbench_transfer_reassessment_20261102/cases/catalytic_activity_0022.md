# catalytic_activity_0022: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0022.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **A** — 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)

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
MGFAARPFHIVFSLFVLAGATQALIICPFDSIYQFGDSISDTGNYIRILPNGPAAAAANFPYGITFPGIPTGRFSDGRLIVDFIARVLGLPLLNPYLQQNASFKNGVNFAVGGATALNSSVLAAAGVQIPDIYLIPLSTQLNWFQTYLRSNCSSPTECSKKVQNSLFLIGNIGNNDVNYALPYRTIQEIEAYVPSIAKAVANATREIIRLGGRRIIVPGTFPFGCLPRNLYLFPNGDKDDLGCLRRLNDLSIYFNNLFQQALNSLRIEFPQAVIIYADYYNAFRFLLRNARALGFTSTLQSCCGIGGPYNFDLNRLCGFPGVPVCRNPREYIQWDGFHYTEAAHRHIVQYLIPDILKELKCS

[Multiple Choices]
A. 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)
B. a 5'-end (5'-triphosphoguanosine)-adenylyl-adenylyl-cytidylyl-adenosine in mRNA + 2 S-adenosyl-L-methionine = a 5'-end (N(7)-methyl 5'-triphosphoguanosine)-(2'-O-methyladenylyl)-adenylyl-cytidylyl-adenosine in mRNA + 2 S-adenosyl-L-homocysteine + H(+)
C. 2',2'-dihydroxy-2-oxospirilloxanthin = 2,2'-dioxospirilloxanthin + H2O
D. L-aspartate + ATP = 4-phospho-L-aspartate + ADP
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

> The supplied sequence exactly matches the annotated 362-aa protein, and both historical and current UniProt records assign it the reaction in A with ECO:0000269 evidence linked to PubMed 38212296. This supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices may suggest a hydrolase rather than an RNA methyltransferase or kinase, but they do not establish the enzyme’s specific substrate or distinguish hydrolysis of 17-O-acetylnorajmaline from other possible enzyme reactions.


**Missing item-specific fact**

> The protein-specific catalytic annotation or experimental finding that this enzyme hydrolyzes 17-O-acetylnorajmaline.


**Reason**

> Identifying the precise reaction requires a protein-specific substrate/function fact not supplied in the prompt; recognizing the exact sequence from an external record would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the matched annotation supports A; the input alone, however, does not establish that specific reaction.


### Important caveats

- The sequence match is exact, but the author’s precise source snapshot is unknown.
- The cited evidence code indicates experimental evidence in the database record; the underlying primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices may suggest a hydrolase rather than an RNA methyltransferase or kinase, but they do not establish the enzyme’s specific substrate or distinguish hydrolysis of 17-O-acetylnorajmaline from other possible enzyme reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental finding that this enzyme hydrolyzes 17-O-acetylnorajmaline.",
    "reason": "Identifying the precise reaction requires a protein-specific substrate/function fact not supplied in the prompt; recognizing the exact sequence from an external record would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 362-aa protein, and both historical and current UniProt records assign it the reaction in A with ECO:0000269 evidence linked to PubMed 38212296. This supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s precise source snapshot is unknown.",
    "The cited evidence code indicates experimental evidence in the database record; the underlying primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched annotation supports A; the input alone, however, does not establish that specific reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 362-aa protein, and both historical and current UniProt records assign it the reaction in A with ECO:0000269 evidence linked to PubMed 38212296. This supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices may suggest a hydrolase rather than an RNA methyltransferase or kinase, but they do not establish the enzyme’s specific substrate or distinguish hydrolysis of 17-O-acetylnorajmaline from other possible enzyme reactions.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental finding that this enzyme hydrolyzes 17-O-acetylnorajmaline.",
    "reason": "Identifying the precise reaction requires a protein-specific substrate/function fact not supplied in the prompt; recognizing the exact sequence from an external record would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched annotation supports A; the input alone, however, does not establish that specific reaction."
  },
  "important_caveats": [
    "The sequence match is exact, but the author’s precise source snapshot is unknown.",
    "The cited evidence code indicates experimental evidence in the database record; the underlying primary paper was not independently validated here."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ5 (sequence exactly matched, 362 AA) annotates EC 3.1.1.80 'Acetylajmalan esterase 2' (RsAAE2) from Rauvolfia serpentina. The catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' is supported by experimental evidence (ECO:0000269, PubMed:38212296, Guo et al. Nat. Commun. 2024). The expected answer matches the annotated reaction verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The four choices represent distinct enzyme classes (esterase, methyltransferase, oxidoreductase, kinase), so elimination based on absence of characteristic motifs (SAM-binding for B, FAD/NAD Rossmann fold for C, glycine-rich kinase loop for D) provides partial narrowing. However, the sequence lacks a canonical GxSxG serine hydrolase motif and does not contain an unambiguous, generalizable esterase signature that would allow confident positive identification of the enzyme class from sequence alone. The specific substrate '17-O-acetylnorajmaline' is a highly specific alkaloid biosynthetic intermediate known only from the 2024 Rauvolfia serpentina ajmaline pathway characterization.


**Missing item-specific fact**

> Recognition that this 362-aa sequence corresponds to Acetylajmalan esterase 2 (RsAAE2) in the Rauvolfia serpentina ajmaline biosynthetic pathway, and that its experimentally characterized substrate is 17-O-acetylnorajmaline (not 17-O-acetylajmaline), requires either exact sequence-to-database matching or memorization of the 2024 Nat. Commun. pathway paper. No generalizable sequence motif in the provided input unambiguously identifies this as a norajmaline-specific esterase.


**Reason**

> While the widely divergent enzyme classes among the four choices allow some elimination-based reasoning, confidently identifying the correct answer as a specific esterase acting on 17-O-acetylnorajmaline requires item-specific knowledge of the Rauvolfia serpentina alkaloid biosynthetic pathway or exact sequence lookup. The sequence itself does not present a textbook esterase motif (e.g., GxSxG) that would allow a model to reason from general biochemistry to this precise catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four entirely different enzyme classes (esterase/hydrolysis, methyltransferase, oxidoreductase/dehydrogenation, kinase/phosphorylation). Only one (A) is a hydrolytic esterase reaction. No other choice is biochemically plausible for this sequence, so there is no genuine ambiguity among the options.


### Important caveats

- The UniProt entry P0DXJ5 was first public in June 2025, and the supporting publication is from 2024. The sequence and annotation are very recent, making prior memorization by a model less likely but also meaning the sequence is unlikely to appear in older training corpora.
- The sequence lacks a canonical GxSxG serine hydrolase motif, making positive identification as an esterase from sequence alone non-trivial even for domain experts.
- A second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) to Q3MKY2, but this is not among the choices, so it does not create ambiguity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices represent distinct enzyme classes (esterase, methyltransferase, oxidoreductase, kinase), so elimination based on absence of characteristic motifs (SAM-binding for B, FAD/NAD Rossmann fold for C, glycine-rich kinase loop for D) provides partial narrowing. However, the sequence lacks a canonical GxSxG serine hydrolase motif and does not contain an unambiguous, generalizable esterase signature that would allow confident positive identification of the enzyme class from sequence alone. The specific substrate '17-O-acetylnorajmaline' is a highly specific alkaloid biosynthetic intermediate known only from the 2024 Rauvolfia serpentina ajmaline pathway characterization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this 362-aa sequence corresponds to Acetylajmalan esterase 2 (RsAAE2) in the Rauvolfia serpentina ajmaline biosynthetic pathway, and that its experimentally characterized substrate is 17-O-acetylnorajmaline (not 17-O-acetylajmaline), requires either exact sequence-to-database matching or memorization of the 2024 Nat. Commun. pathway paper. No generalizable sequence motif in the provided input unambiguously identifies this as a norajmaline-specific esterase.",
    "reason": "While the widely divergent enzyme classes among the four choices allow some elimination-based reasoning, confidently identifying the correct answer as a specific esterase acting on 17-O-acetylnorajmaline requires item-specific knowledge of the Rauvolfia serpentina alkaloid biosynthetic pathway or exact sequence lookup. The sequence itself does not present a textbook esterase motif (e.g., GxSxG) that would allow a model to reason from general biochemistry to this precise catalytic activity."
  },
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ5 (sequence exactly matched, 362 AA) annotates EC 3.1.1.80 'Acetylajmalan esterase 2' (RsAAE2) from Rauvolfia serpentina. The catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' is supported by experimental evidence (ECO:0000269, PubMed:38212296, Guo et al. Nat. Commun. 2024). The expected answer matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ5 was first public in June 2025, and the supporting publication is from 2024. The sequence and annotation are very recent, making prior memorization by a model less likely but also meaning the sequence is unlikely to appear in older training corpora.",
    "The sequence lacks a canonical GxSxG serine hydrolase motif, making positive identification as an esterase from sequence alone non-trivial even for domain experts.",
    "A second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) to Q3MKY2, but this is not among the choices, so it does not create ambiguity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four entirely different enzyme classes (esterase/hydrolysis, methyltransferase, oxidoreductase/dehydrogenation, kinase/phosphorylation). Only one (A) is a hydrolytic esterase reaction. No other choice is biochemically plausible for this sequence, so there is no genuine ambiguity among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ5 (sequence exactly matched, 362 AA) annotates EC 3.1.1.80 'Acetylajmalan esterase 2' (RsAAE2) from Rauvolfia serpentina. The catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' is supported by experimental evidence (ECO:0000269, PubMed:38212296, Guo et al. Nat. Commun. 2024). The expected answer matches the annotated reaction verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The four choices represent distinct enzyme classes (esterase, methyltransferase, oxidoreductase, kinase), so elimination based on absence of characteristic motifs (SAM-binding for B, FAD/NAD Rossmann fold for C, glycine-rich kinase loop for D) provides partial narrowing. However, the sequence lacks a canonical GxSxG serine hydrolase motif and does not contain an unambiguous, generalizable esterase signature that would allow confident positive identification of the enzyme class from sequence alone. The specific substrate '17-O-acetylnorajmaline' is a highly specific alkaloid biosynthetic intermediate known only from the 2024 Rauvolfia serpentina ajmaline pathway characterization.",
    "missing_item_specific_fact": "Recognition that this 362-aa sequence corresponds to Acetylajmalan esterase 2 (RsAAE2) in the Rauvolfia serpentina ajmaline biosynthetic pathway, and that its experimentally characterized substrate is 17-O-acetylnorajmaline (not 17-O-acetylajmaline), requires either exact sequence-to-database matching or memorization of the 2024 Nat. Commun. pathway paper. No generalizable sequence motif in the provided input unambiguously identifies this as a norajmaline-specific esterase.",
    "reason": "While the widely divergent enzyme classes among the four choices allow some elimination-based reasoning, confidently identifying the correct answer as a specific esterase acting on 17-O-acetylnorajmaline requires item-specific knowledge of the Rauvolfia serpentina alkaloid biosynthetic pathway or exact sequence lookup. The sequence itself does not present a textbook esterase motif (e.g., GxSxG) that would allow a model to reason from general biochemistry to this precise catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four entirely different enzyme classes (esterase/hydrolysis, methyltransferase, oxidoreductase/dehydrogenation, kinase/phosphorylation). Only one (A) is a hydrolytic esterase reaction. No other choice is biochemically plausible for this sequence, so there is no genuine ambiguity among the options."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ5 was first public in June 2025, and the supporting publication is from 2024. The sequence and annotation are very recent, making prior memorization by a model less likely but also meaning the sequence is unlikely to appear in older training corpora.",
    "The sequence lacks a canonical GxSxG serine hydrolase motif, making positive identification as an esterase from sequence alone non-trivial even for domain experts.",
    "A second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) to Q3MKY2, but this is not among the choices, so it does not create ambiguity."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry annotates the reaction in A as catalytic activity with ECO:0000269 evidence linked to a publication. The archived entry also contains this annotation, so support is not limited to the current snapshot. The cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic N-terminal segment consistent with a signal peptide, followed by a predominantly non-membrane protein. In the offered choices, A is ester hydrolysis, compatible with an esterase; B and D require characteristic SAM-dependent methyltransferase or ATP-dependent kinase functions, respectively, for which the sequence offers no obvious signature. C concerns a specialized carotenoid transformation and is less consistent with this apparent protein architecture. These are probabilistic class-level clues, not proof of the exact substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and enzyme-class knowledge gives a meaningful basis to favor A among these alternatives. The precise norajmaline substrate specificity is not established from those clues alone, but the alternatives are distinct enough that this limitation does not make the choice lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option has comparable support from the sequence-level class clues.


### Important caveats

- The sequence clues support a probabilistic choice of reaction class, not independent confirmation of the exact substrate and products.
- The reviewer-only annotation is sequence-matched; its cited experimental evidence was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with a signal peptide, followed by a predominantly non-membrane protein. In the offered choices, A is ester hydrolysis, compatible with an esterase; B and D require characteristic SAM-dependent methyltransferase or ATP-dependent kinase functions, respectively, for which the sequence offers no obvious signature. C concerns a specialized carotenoid transformation and is less consistent with this apparent protein architecture. These are probabilistic class-level clues, not proof of the exact substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-class knowledge gives a meaningful basis to favor A among these alternatives. The precise norajmaline substrate specificity is not established from those clues alone, but the alternatives are distinct enough that this limitation does not make the choice lookup-dependent."
  },
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the reaction in A as catalytic activity with ECO:0000269 evidence linked to a publication. The archived entry also contains this annotation, so support is not limited to the current snapshot. The cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence clues support a probabilistic choice of reaction class, not independent confirmation of the exact substrate and products.",
    "The reviewer-only annotation is sequence-matched; its cited experimental evidence was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparable support from the sequence-level class clues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the reaction in A as catalytic activity with ECO:0000269 evidence linked to a publication. The archived entry also contains this annotation, so support is not limited to the current snapshot. The cited paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with a signal peptide, followed by a predominantly non-membrane protein. In the offered choices, A is ester hydrolysis, compatible with an esterase; B and D require characteristic SAM-dependent methyltransferase or ATP-dependent kinase functions, respectively, for which the sequence offers no obvious signature. C concerns a specialized carotenoid transformation and is less consistent with this apparent protein architecture. These are probabilistic class-level clues, not proof of the exact substrate.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-class knowledge gives a meaningful basis to favor A among these alternatives. The precise norajmaline substrate specificity is not established from those clues alone, but the alternatives are distinct enough that this limitation does not make the choice lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparable support from the sequence-level class clues."
  },
  "important_caveats": [
    "The sequence clues support a probabilistic choice of reaction class, not independent confirmation of the exact substrate and products.",
    "The reviewer-only annotation is sequence-matched; its cited experimental evidence was not independently validated here."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ5 (Acetylajmalan esterase 2, RsAAE2) from Rauvolfia serpentina is annotated with EC 3.1.1.80 and the exact catalytic reaction '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' with experimental evidence (ECO:0000269, PubMed:38212296). The sequence in the benchmark matches the source entry exactly (SHA-256 confirmed). The expected answer A is directly supported by experimentally verified annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains the highly conserved 'GDSISDTG' motif (approximately residues 45-52), which is the signature GDSL catalytic motif of the GDSL lipase/esterase superfamily. GDSL esterases are a large, well-characterized family of plant secretory hydrolases that cleave ester bonds. The N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC...) is consistent with plant secretory esterases. Among the four choices, only option A represents an esterase (EC 3.1.1.x) reaction: hydrolysis of an acetate ester to release acetate. Option B is a methyltransferase (cap methylation), option C is a dehydratase (carotenoid dehydration), and option D is a kinase (aspartate phosphorylation). None of these enzyme classes would contain a GDSL motif. A knowledgeable model recognizing the GDSL motif from other plant GDSL esterases can confidently assign esterase activity, which uniquely matches choice A among the offered alternatives. The specific substrate identity (norajmaline vs ajmaline) is irrelevant here since only one esterase option is presented.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GDSL motif is a well-established family-level sequence signature shared across hundreds of characterized plant esterases and lipases. Recognizing this motif and mapping it to esterase activity is legitimate transfer knowledge from other proteins. Among the four offered choices, only A is an esterase reaction, making the family-level inference sufficient to select the correct answer without needing the exact substrate annotation of this specific protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four distinct enzyme classes (esterase, methyltransferase, dehydratase, kinase). The GDSL motif unambiguously identifies the protein as an esterase, eliminating B, C, and D. No ambiguity exists among the offered alternatives.


### Important caveats

- The specific substrate (norajmaline vs. ajmaline) is not derivable from sequence alone, but this distinction is irrelevant because only one esterase option (A) is offered among the choices.
- The protein was characterized experimentally in 2024 (PubMed:38212296) and deposited in UniProt in June 2025, making it relatively recent knowledge.
- The GDSL motif identification is a family-level inference from other plant esterases; it does not require memorization of this specific protein's record.
- The UniProt entry also lists a second catalytic activity (17-O-acetylajmaline → ajmaline) inferred by similarity (ECO:0000250), but this is not among the choices and does not affect the answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains the highly conserved 'GDSISDTG' motif (approximately residues 45-52), which is the signature GDSL catalytic motif of the GDSL lipase/esterase superfamily. GDSL esterases are a large, well-characterized family of plant secretory hydrolases that cleave ester bonds. The N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC...) is consistent with plant secretory esterases. Among the four choices, only option A represents an esterase (EC 3.1.1.x) reaction: hydrolysis of an acetate ester to release acetate. Option B is a methyltransferase (cap methylation), option C is a dehydratase (carotenoid dehydration), and option D is a kinase (aspartate phosphorylation). None of these enzyme classes would contain a GDSL motif. A knowledgeable model recognizing the GDSL motif from other plant GDSL esterases can confidently assign esterase activity, which uniquely matches choice A among the offered alternatives. The specific substrate identity (norajmaline vs ajmaline) is irrelevant here since only one esterase option is presented.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GDSL motif is a well-established family-level sequence signature shared across hundreds of characterized plant esterases and lipases. Recognizing this motif and mapping it to esterase activity is legitimate transfer knowledge from other proteins. Among the four offered choices, only A is an esterase reaction, making the family-level inference sufficient to select the correct answer without needing the exact substrate annotation of this specific protein."
  },
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ5 (Acetylajmalan esterase 2, RsAAE2) from Rauvolfia serpentina is annotated with EC 3.1.1.80 and the exact catalytic reaction '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' with experimental evidence (ECO:0000269, PubMed:38212296). The sequence in the benchmark matches the source entry exactly (SHA-256 confirmed). The expected answer A is directly supported by experimentally verified annotation."
  },
  "important_caveats": [
    "The specific substrate (norajmaline vs. ajmaline) is not derivable from sequence alone, but this distinction is irrelevant because only one esterase option (A) is offered among the choices.",
    "The protein was characterized experimentally in 2024 (PubMed:38212296) and deposited in UniProt in June 2025, making it relatively recent knowledge.",
    "The GDSL motif identification is a family-level inference from other plant esterases; it does not require memorization of this specific protein's record.",
    "The UniProt entry also lists a second catalytic activity (17-O-acetylajmaline → ajmaline) inferred by similarity (ECO:0000250), but this is not among the choices and does not affect the answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (esterase, methyltransferase, dehydratase, kinase). The GDSL motif unambiguously identifies the protein as an esterase, eliminating B, C, and D. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ5 (Acetylajmalan esterase 2, RsAAE2) from Rauvolfia serpentina is annotated with EC 3.1.1.80 and the exact catalytic reaction '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' with experimental evidence (ECO:0000269, PubMed:38212296). The sequence in the benchmark matches the source entry exactly (SHA-256 confirmed). The expected answer A is directly supported by experimentally verified annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains the highly conserved 'GDSISDTG' motif (approximately residues 45-52), which is the signature GDSL catalytic motif of the GDSL lipase/esterase superfamily. GDSL esterases are a large, well-characterized family of plant secretory hydrolases that cleave ester bonds. The N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC...) is consistent with plant secretory esterases. Among the four choices, only option A represents an esterase (EC 3.1.1.x) reaction: hydrolysis of an acetate ester to release acetate. Option B is a methyltransferase (cap methylation), option C is a dehydratase (carotenoid dehydration), and option D is a kinase (aspartate phosphorylation). None of these enzyme classes would contain a GDSL motif. A knowledgeable model recognizing the GDSL motif from other plant GDSL esterases can confidently assign esterase activity, which uniquely matches choice A among the offered alternatives. The specific substrate identity (norajmaline vs ajmaline) is irrelevant here since only one esterase option is presented.",
    "missing_item_specific_fact": "",
    "reason": "The GDSL motif is a well-established family-level sequence signature shared across hundreds of characterized plant esterases and lipases. Recognizing this motif and mapping it to esterase activity is legitimate transfer knowledge from other proteins. Among the four offered choices, only A is an esterase reaction, making the family-level inference sufficient to select the correct answer without needing the exact substrate annotation of this specific protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (esterase, methyltransferase, dehydratase, kinase). The GDSL motif unambiguously identifies the protein as an esterase, eliminating B, C, and D. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The specific substrate (norajmaline vs. ajmaline) is not derivable from sequence alone, but this distinction is irrelevant because only one esterase option (A) is offered among the choices.",
    "The protein was characterized experimentally in 2024 (PubMed:38212296) and deposited in UniProt in June 2025, making it relatively recent knowledge.",
    "The GDSL motif identification is a family-level inference from other plant esterases; it does not require memorization of this specific protein's record.",
    "The UniProt entry also lists a second catalytic activity (17-O-acetylajmaline → ajmaline) inferred by similarity (ECO:0000250), but this is not among the choices and does not affect the answer."
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
  "requested_accession": "P0DXJ5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "benchmark_sequence_length": 362,
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
  "current_record_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "current_source_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "current_source_sequence_length": 362,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 2,
  "selected_historical_version": {
    "accession": "P0DXJ5",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AAE2_RAUSE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "selected_historical_source_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "selected_historical_source_sequence_length": 362,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P0DXJ5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"3.1.1.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Acetylajmalan esterase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsAAE2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23797\"}}],\"reaction\":{\"ecNumber\":\"3.1.1.80\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"name\":\"17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23796\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77725\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3MKY2\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:22125\"}}],\"reaction\":{\"ecNumber\":\"3.1.1.80\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3MKY2\",\"source\":\"UniProtKB\"}],\"name\":\"17-O-acetylajmaline + H2O = ajmaline + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:22124\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58567\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58679\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   AAE2_RAUSE              Reviewed;         362 AA.\nAC   P0DXJ5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\nGN   Name=AAE2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 17-23",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE\nRP   SPECIFICITY, AND BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 31-37",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+);\nCC         Xref=Rhea:RHEA:23796, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30089, ChEBI:CHEBI:77618, ChEBI:CHEBI:77725; EC=3.1.1.80;\nCC         Evidence={ECO:0000269|PubMed:38212296};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23797;\nCC         Evidence={ECO:0000269|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 38-44",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylajmaline + H2O = ajmaline + acetate + H(+);\nCC         Xref=Rhea:RHEA:22124, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30089, ChEBI:CHEBI:58567, ChEBI:CHEBI:58679; EC=3.1.1.80;\nCC         Evidence={ECO:0000250|UniProtKB:Q3MKY2};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:22125;\nCC         Evidence={ECO:0000250|UniProtKB:Q3MKY2};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
