# active_site_0093: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0093.txt)

**Task:** `active_site`  
**Author key, unchanged:** **C** — Position 176 (Proton donor/acceptor)

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
MKPHNSEKYFVKNGQPHFLISGEVHYFRINPKLWRNHLQLLKQTGADTVSTYIPWDWHEIEEDDFDFEGKTHPARNLIRFIKLCKEENLDLIVKPGPYILAEYENQGLPSWLLKKLSKNAFALDENGNVISPDLVSYLSDEFLEYTFKWYDKVMPIISKHQKEHYGPITMMQLCNEIGVFQWLSGKSDYNPKVINLYKEFIIQRYKTIEKLNSVYSTNYNSFDDLKAPSGKIKLRSDYCAYFDFHLFFREYYNKYISILKNKIRSFGINIKLTHNIPGWIYGNASELPMLISTYSEIMKNHPDIIFGLDHIPEFVSFRNAHSDLACNKILEAMQPEAPVWAAEFQAGTREHHVKAYAKDLETFYIASLAHGIKGFNYYMFSQGINPEGKGFYGKTFYFQTALDAASNKLALYDSIKKVNRFIRKEQKDLLRTNVNSEICVGFYKPYFFTELISSQLLKEKKLNVEELGLYIDPRFLREEILFNGLLRGLQTLNYNYDVVDLENCDLKSLTAYKQLWITSAEFMDAETQNLLSEFVLNGGNLILYPAVPTLDNYLNRCEILKNNFGIEFITKDSSHKVSAFGIEDVFTAFSKKQIYNDTNSKPIAFTQENEICGIRKKIGKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQFVVRENNKSRYIFFLNYHNERKTFNYRKSSELKKKKSEEISIAPFSYKVIKENK

[Multiple Choices]
A. Position 359 (For beta-ketoacyl synthase activity)
B. Position 2056 (For beta-ketoacyl synthase 2 activity)
C. Position 176 (Proton donor/acceptor)
D. Position 662 (For acyltransferase activity of LM)
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

> The supplied sequence exactly matches the 716-residue UniProt entry for this glucosyltransferase, which annotates residue 176 as the proton donor/acceptor. This supports choice C. The UniProt feature is a curator inference citing a paper, not itself direct experimental evidence; the cited paper is identified as covering active-site analysis and mutagenesis of Glu-176 and Glu-343.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C26](#evidence-c26), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence length rules out position 2056, and the unrelated activity labels may help reject some distractors, but the input gives no enzyme identity or functional context that establishes the catalytic role of residue 176.


**Missing item-specific fact**

> The protein-specific annotation or experimental characterization assigning residue 176 as the proton donor/acceptor is needed to select C.


**Reason**

> Knowing which exact residue performs this catalytic role requires an item-specific active-site assignment; it is not meaningfully derivable from the bare sequence and choices by general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports C among the listed choices; no other option is supported as the proton donor/acceptor for this sequence.


### Important caveats

- The reviewer-only UniProt records match the input sequence, but the author's exact source snapshot is unknown.
- The database annotation cites a publication that includes structural work and mutagenesis, but the supplied evidence does not independently establish the paper's experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence length rules out position 2056, and the unrelated activity labels may help reject some distractors, but the input gives no enzyme identity or functional context that establishes the catalytic role of residue 176.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or experimental characterization assigning residue 176 as the proton donor/acceptor is needed to select C.",
    "reason": "Knowing which exact residue performs this catalytic role requires an item-specific active-site assignment; it is not meaningfully derivable from the bare sequence and choices by general biological reasoning."
  },
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C26",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 716-residue UniProt entry for this glucosyltransferase, which annotates residue 176 as the proton donor/acceptor. This supports choice C. The UniProt feature is a curator inference citing a paper, not itself direct experimental evidence; the cited paper is identified as covering active-site analysis and mutagenesis of Glu-176 and Glu-343."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the input sequence, but the author's exact source snapshot is unknown.",
    "The database annotation cites a publication that includes structural work and mutagenesis, but the supplied evidence does not independently establish the paper's experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C among the listed choices; no other option is supported as the proton donor/acceptor for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 716-residue UniProt entry for this glucosyltransferase, which annotates residue 176 as the proton donor/acceptor. This supports choice C. The UniProt feature is a curator inference citing a paper, not itself direct experimental evidence; the cited paper is identified as covering active-site analysis and mutagenesis of Glu-176 and Glu-343.",
    "evidence_ids": ["C1", "C4", "C5", "C26", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence length rules out position 2056, and the unrelated activity labels may help reject some distractors, but the input gives no enzyme identity or functional context that establishes the catalytic role of residue 176.",
    "missing_item_specific_fact": "The protein-specific annotation or experimental characterization assigning residue 176 as the proton donor/acceptor is needed to select C.",
    "reason": "Knowing which exact residue performs this catalytic role requires an item-specific active-site assignment; it is not meaningfully derivable from the bare sequence and choices by general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C among the listed choices; no other option is supported as the proton donor/acceptor for this sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the input sequence, but the author's exact source snapshot is unknown.",
    "The database annotation cites a publication that includes structural work and mutagenesis, but the supplied evidence does not independently establish the paper's experimental results."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry I0AIT9 (Beta-1,2-glucosyltransferase, EC 2.4.1.391, Ignavibacterium album) explicitly annotates an Active site at position 176 with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074, corroborated by X-ray crystallography and mutagenesis of Glu-176 and Glu-343 in PDB structures 7VKX/7VKY). The sequence matches the benchmark sequence exactly (716 residues, SHA-256 match). The distractors are clearly wrong: position 2056 exceeds the 716-residue sequence; 'beta-ketoacyl synthase' and 'acyltransferase of LM' describe entirely different enzyme classes irrelevant to this glycosyltransferase.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C26](#evidence-c26), [H3](#evidence-h3), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option B (position 2056) can be eliminated by simple arithmetic since the sequence is only 716 residues long. However, distinguishing C from A and D requires knowing that this protein is a glycosyltransferase (EC 2.4.1.391) rather than a beta-ketoacyl synthase or acyltransferase. Identifying the protein's function from a 716-residue sequence without database access is not feasible through general reasoning; recognizing GT-B fold motifs from sequence alone does not yield the specific catalytic residue at position 176. The precise assignment of Glu-176 as proton donor/acceptor was determined experimentally via X-ray crystallography and site-directed mutagenesis (PubMed 35065074).


**Missing item-specific fact**

> The identity of the protein as a beta-1,2-glucosyltransferase (EC 2.4.1.391) and the experimentally determined annotation that Glu-176 serves as the proton donor/acceptor in the catalytic mechanism. Without this item-specific knowledge, the functional descriptions in options A and D cannot be ruled out, and the specific position 176 cannot be identified from sequence alone.


**Reason**

> While B is eliminable by arithmetic (position exceeds sequence length), the discrimination among A, C, and D hinges on knowing the protein's actual enzymatic class and the experimentally determined active-site residue. This is a protein-specific annotation derived from a 2022 crystallographic/mutagenesis study, not derivable from general biological reasoning applied to the raw sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt entry annotates two active sites (position 176 as proton donor/acceptor and position 343 as nucleophile), but only position 176 appears among the options. The other three options reference entirely different enzyme classes or an impossible position, leaving no genuine ambiguity among the provided choices.


### Important caveats

- The UniProt annotation for position 176 carries evidence code ECO:0000305 (inferred from direct assay / published experiment), supported by X-ray crystallography (PDB 7VKX, 7VKY) and mutagenesis of Glu-176 and Glu-343. This is experimental evidence, not mere computational prediction.
- The entry was first publicly released 2025-04-09; the author's data-construction snapshot is unknown. Sequence match is confirmed across historical (entry v55) and current (v57) versions.
- The protein also has a second annotated active site (position 343, Nucleophile), which is not offered as a choice; the question's phrasing 'the enzyme's catalytic center' could in principle encompass both sites, but the answer options constrain the task to selecting among the four given choices.
- The identity of the protein (accession I0AIT9) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B (position 2056) can be eliminated by simple arithmetic since the sequence is only 716 residues long. However, distinguishing C from A and D requires knowing that this protein is a glycosyltransferase (EC 2.4.1.391) rather than a beta-ketoacyl synthase or acyltransferase. Identifying the protein's function from a 716-residue sequence without database access is not feasible through general reasoning; recognizing GT-B fold motifs from sequence alone does not yield the specific catalytic residue at position 176. The precise assignment of Glu-176 as proton donor/acceptor was determined experimentally via X-ray crystallography and site-directed mutagenesis (PubMed 35065074).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the protein as a beta-1,2-glucosyltransferase (EC 2.4.1.391) and the experimentally determined annotation that Glu-176 serves as the proton donor/acceptor in the catalytic mechanism. Without this item-specific knowledge, the functional descriptions in options A and D cannot be ruled out, and the specific position 176 cannot be identified from sequence alone.",
    "reason": "While B is eliminable by arithmetic (position exceeds sequence length), the discrimination among A, C, and D hinges on knowing the protein's actual enzymatic class and the experimentally determined active-site residue. This is a protein-specific annotation derived from a 2022 crystallographic/mutagenesis study, not derivable from general biological reasoning applied to the raw sequence."
  },
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C26",
      "H3",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry I0AIT9 (Beta-1,2-glucosyltransferase, EC 2.4.1.391, Ignavibacterium album) explicitly annotates an Active site at position 176 with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074, corroborated by X-ray crystallography and mutagenesis of Glu-176 and Glu-343 in PDB structures 7VKX/7VKY). The sequence matches the benchmark sequence exactly (716 residues, SHA-256 match). The distractors are clearly wrong: position 2056 exceeds the 716-residue sequence; 'beta-ketoacyl synthase' and 'acyltransferase of LM' describe entirely different enzyme classes irrelevant to this glycosyltransferase."
  },
  "important_caveats": [
    "The UniProt annotation for position 176 carries evidence code ECO:0000305 (inferred from direct assay / published experiment), supported by X-ray crystallography (PDB 7VKX, 7VKY) and mutagenesis of Glu-176 and Glu-343. This is experimental evidence, not mere computational prediction.",
    "The entry was first publicly released 2025-04-09; the author's data-construction snapshot is unknown. Sequence match is confirmed across historical (entry v55) and current (v57) versions.",
    "The protein also has a second annotated active site (position 343, Nucleophile), which is not offered as a choice; the question's phrasing 'the enzyme's catalytic center' could in principle encompass both sites, but the answer options constrain the task to selecting among the four given choices.",
    "The identity of the protein (accession I0AIT9) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry annotates two active sites (position 176 as proton donor/acceptor and position 343 as nucleophile), but only position 176 appears among the options. The other three options reference entirely different enzyme classes or an impossible position, leaving no genuine ambiguity among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry I0AIT9 (Beta-1,2-glucosyltransferase, EC 2.4.1.391, Ignavibacterium album) explicitly annotates an Active site at position 176 with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074, corroborated by X-ray crystallography and mutagenesis of Glu-176 and Glu-343 in PDB structures 7VKX/7VKY). The sequence matches the benchmark sequence exactly (716 residues, SHA-256 match). The distractors are clearly wrong: position 2056 exceeds the 716-residue sequence; 'beta-ketoacyl synthase' and 'acyltransferase of LM' describe entirely different enzyme classes irrelevant to this glycosyltransferase.",
    "evidence_ids": ["C5", "C6", "C26", "H3", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option B (position 2056) can be eliminated by simple arithmetic since the sequence is only 716 residues long. However, distinguishing C from A and D requires knowing that this protein is a glycosyltransferase (EC 2.4.1.391) rather than a beta-ketoacyl synthase or acyltransferase. Identifying the protein's function from a 716-residue sequence without database access is not feasible through general reasoning; recognizing GT-B fold motifs from sequence alone does not yield the specific catalytic residue at position 176. The precise assignment of Glu-176 as proton donor/acceptor was determined experimentally via X-ray crystallography and site-directed mutagenesis (PubMed 35065074).",
    "missing_item_specific_fact": "The identity of the protein as a beta-1,2-glucosyltransferase (EC 2.4.1.391) and the experimentally determined annotation that Glu-176 serves as the proton donor/acceptor in the catalytic mechanism. Without this item-specific knowledge, the functional descriptions in options A and D cannot be ruled out, and the specific position 176 cannot be identified from sequence alone.",
    "reason": "While B is eliminable by arithmetic (position exceeds sequence length), the discrimination among A, C, and D hinges on knowing the protein's actual enzymatic class and the experimentally determined active-site residue. This is a protein-specific annotation derived from a 2022 crystallographic/mutagenesis study, not derivable from general biological reasoning applied to the raw sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry annotates two active sites (position 176 as proton donor/acceptor and position 343 as nucleophile), but only position 176 appears among the options. The other three options reference entirely different enzyme classes or an impossible position, leaving no genuine ambiguity among the provided choices."
  },
  "important_caveats": [
    "The UniProt annotation for position 176 carries evidence code ECO:0000305 (inferred from direct assay / published experiment), supported by X-ray crystallography (PDB 7VKX, 7VKY) and mutagenesis of Glu-176 and Glu-343. This is experimental evidence, not mere computational prediction.",
    "The entry was first publicly released 2025-04-09; the author's data-construction snapshot is unknown. Sequence match is confirmed across historical (entry v55) and current (v57) versions.",
    "The protein also has a second annotated active site (position 343, Nucleophile), which is not offered as a choice; the question's phrasing 'the enzyme's catalytic center' could in principle encompass both sites, but the answer options constrain the task to selecting among the four given choices.",
    "The identity of the protein (accession I0AIT9) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies residue 176 as an active-site proton donor/acceptor. The cited paper also concerns active-site analysis and mutagenesis of Glu-176 and Glu-343. This supports C as a catalytic residue, though it does not mean residue 176 is the entire active site.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C26](#evidence-c26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The target-specific assignment of residue 176 as the proton donor/acceptor, established by its active-site annotation and supporting structural or mutagenesis work.


**Reason**

> The sequence reveals residues and their positions, but does not by itself establish which one performs proton transfer. A general expectation that acidic residues can act as acid/base catalysts does not distinguish position 176 from other acidic residues without a recognizable family-level feature or alignment that identifies this catalytic position. The alternative activity labels may look implausible, but that alone does not establish the exact target-specific assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports C among the offered choices. Other catalytic residues are annotated for this protein, but no other offered option is identified as a defensible alternative for the stated proton donor/acceptor role.


### Important caveats

- The active-site annotation is curator-attributed evidence linked to a paper; the excerpts do not independently reproduce the experimental results.
- The annotated active site includes another catalytic residue, so the keyed option should be understood as identifying one active-site residue, not a complete catalytic center.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The target-specific assignment of residue 176 as the proton donor/acceptor, established by its active-site annotation and supporting structural or mutagenesis work.",
    "reason": "The sequence reveals residues and their positions, but does not by itself establish which one performs proton transfer. A general expectation that acidic residues can act as acid/base catalysts does not distinguish position 176 from other acidic residues without a recognizable family-level feature or alignment that identifies this catalytic position. The alternative activity labels may look implausible, but that alone does not establish the exact target-specific assignment."
  },
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C26"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 176 as an active-site proton donor/acceptor. The cited paper also concerns active-site analysis and mutagenesis of Glu-176 and Glu-343. This supports C as a catalytic residue, though it does not mean residue 176 is the entire active site."
  },
  "important_caveats": [
    "The active-site annotation is curator-attributed evidence linked to a paper; the excerpts do not independently reproduce the experimental results.",
    "The annotated active site includes another catalytic residue, so the keyed option should be understood as identifying one active-site residue, not a complete catalytic center."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C among the offered choices. Other catalytic residues are annotated for this protein, but no other offered option is identified as a defensible alternative for the stated proton donor/acceptor role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 176 as an active-site proton donor/acceptor. The cited paper also concerns active-site analysis and mutagenesis of Glu-176 and Glu-343. This supports C as a catalytic residue, though it does not mean residue 176 is the entire active site.",
    "evidence_ids": ["C5", "H3", "C26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The target-specific assignment of residue 176 as the proton donor/acceptor, established by its active-site annotation and supporting structural or mutagenesis work.",
    "reason": "The sequence reveals residues and their positions, but does not by itself establish which one performs proton transfer. A general expectation that acidic residues can act as acid/base catalysts does not distinguish position 176 from other acidic residues without a recognizable family-level feature or alignment that identifies this catalytic position. The alternative activity labels may look implausible, but that alone does not establish the exact target-specific assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C among the offered choices. Other catalytic residues are annotated for this protein, but no other offered option is identified as a defensible alternative for the stated proton donor/acceptor role."
  },
  "important_caveats": [
    "The active-site annotation is curator-attributed evidence linked to a paper; the excerpts do not independently reproduce the experimental results.",
    "The annotated active site includes another catalytic residue, so the keyed option should be understood as identifying one active-site residue, not a complete catalytic center."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (I0AIT9, sequence matched) annotates position 176 as 'Active site' with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074). The reference (PubMed:35065074) explicitly includes 'MUTAGENESIS OF GLU-176 AND GLU-343' and X-ray crystallography data, confirming experimental support. The residue at position 176 in the supplied sequence is indeed Glutamic acid (E), consistent with the annotation.

Citations as saved: [C5](#evidence-c5), [C26](#evidence-c26), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three elimination arguments distinguish C from the other options using transferable knowledge: (1) Option B (position 2056) is immediately impossible because the supplied sequence is only 716 residues long—any model can count or estimate sequence length. (2) Option A ('For beta-ketoacyl synthase activity') and Option D ('For acyltransferase activity of LM') carry functional annotations belonging to entirely different enzyme families. Beta-ketoacyl synthase (FabZ/FasB) is a ~400-residue thiolase-fold enzyme with a conserved Cys-His-His catalytic triad; acyltransferases feature a GxSxG serine nucleophile motif. The 716-residue sequence here matches neither family's characteristic architecture or motifs. (3) Option C ('Proton donor/acceptor') describes a generic catalytic role (general acid/base) consistent with glycosyltransferase chemistry, where Glu/Asp residues serve as proton shuttlers. Position 176 is indeed a Glutamic acid in the sequence. By elimination of the three clearly incompatible options, C is the only viable answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of B is trivial (position exceeds sequence length). The elimination of A and D relies on recognizing that their functional descriptions belong to well-known but unrelated enzyme families (fatty acid synthase thiolase, serine acyltransferase), which is standard transferable biochemistry knowledge. The remaining option C has a generic catalytic description compatible with the protein's likely function. No protein-specific database lookup is strictly required to reach C by elimination among the four offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only C is positionally valid and functionally consistent with the protein. B is impossible by sequence length; A and D describe activities of incompatible enzyme families. No ambiguity exists among the offered alternatives.


### Important caveats

- The UniProt entry also annotates position 343 (Glu, 'Nucleophile') as a second active site, but this is not offered as a choice, so it does not create ambiguity among the provided options.
- The elimination of A and D depends on the model recognizing that 'beta-ketoacyl synthase' and 'acyltransferase of LM' are specific annotations from other protein contexts rather than plausible descriptions for this sequence. A model unfamiliar with these enzyme families might struggle with this elimination step.
- The reviewer-only evidence confirms the protein is a Beta-1,2-glucosyltransferase (EC 2.4.1.391) from Ignavibacterium album, but this identity was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three elimination arguments distinguish C from the other options using transferable knowledge: (1) Option B (position 2056) is immediately impossible because the supplied sequence is only 716 residues long—any model can count or estimate sequence length. (2) Option A ('For beta-ketoacyl synthase activity') and Option D ('For acyltransferase activity of LM') carry functional annotations belonging to entirely different enzyme families. Beta-ketoacyl synthase (FabZ/FasB) is a ~400-residue thiolase-fold enzyme with a conserved Cys-His-His catalytic triad; acyltransferases feature a GxSxG serine nucleophile motif. The 716-residue sequence here matches neither family's characteristic architecture or motifs. (3) Option C ('Proton donor/acceptor') describes a generic catalytic role (general acid/base) consistent with glycosyltransferase chemistry, where Glu/Asp residues serve as proton shuttlers. Position 176 is indeed a Glutamic acid in the sequence. By elimination of the three clearly incompatible options, C is the only viable answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B is trivial (position exceeds sequence length). The elimination of A and D relies on recognizing that their functional descriptions belong to well-known but unrelated enzyme families (fatty acid synthase thiolase, serine acyltransferase), which is standard transferable biochemistry knowledge. The remaining option C has a generic catalytic description compatible with the protein's likely function. No protein-specific database lookup is strictly required to reach C by elimination among the four offered choices."
  },
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C26",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (I0AIT9, sequence matched) annotates position 176 as 'Active site' with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074). The reference (PubMed:35065074) explicitly includes 'MUTAGENESIS OF GLU-176 AND GLU-343' and X-ray crystallography data, confirming experimental support. The residue at position 176 in the supplied sequence is indeed Glutamic acid (E), consistent with the annotation."
  },
  "important_caveats": [
    "The UniProt entry also annotates position 343 (Glu, 'Nucleophile') as a second active site, but this is not offered as a choice, so it does not create ambiguity among the provided options.",
    "The elimination of A and D depends on the model recognizing that 'beta-ketoacyl synthase' and 'acyltransferase of LM' are specific annotations from other protein contexts rather than plausible descriptions for this sequence. A model unfamiliar with these enzyme families might struggle with this elimination step.",
    "The reviewer-only evidence confirms the protein is a Beta-1,2-glucosyltransferase (EC 2.4.1.391) from Ignavibacterium album, but this identity was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only C is positionally valid and functionally consistent with the protein. B is impossible by sequence length; A and D describe activities of incompatible enzyme families. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (I0AIT9, sequence matched) annotates position 176 as 'Active site' with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074). The reference (PubMed:35065074) explicitly includes 'MUTAGENESIS OF GLU-176 AND GLU-343' and X-ray crystallography data, confirming experimental support. The residue at position 176 in the supplied sequence is indeed Glutamic acid (E), consistent with the annotation.",
    "evidence_ids": ["C5", "C26", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three elimination arguments distinguish C from the other options using transferable knowledge: (1) Option B (position 2056) is immediately impossible because the supplied sequence is only 716 residues long—any model can count or estimate sequence length. (2) Option A ('For beta-ketoacyl synthase activity') and Option D ('For acyltransferase activity of LM') carry functional annotations belonging to entirely different enzyme families. Beta-ketoacyl synthase (FabZ/FasB) is a ~400-residue thiolase-fold enzyme with a conserved Cys-His-His catalytic triad; acyltransferases feature a GxSxG serine nucleophile motif. The 716-residue sequence here matches neither family's characteristic architecture or motifs. (3) Option C ('Proton donor/acceptor') describes a generic catalytic role (general acid/base) consistent with glycosyltransferase chemistry, where Glu/Asp residues serve as proton shuttlers. Position 176 is indeed a Glutamic acid in the sequence. By elimination of the three clearly incompatible options, C is the only viable answer.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B is trivial (position exceeds sequence length). The elimination of A and D relies on recognizing that their functional descriptions belong to well-known but unrelated enzyme families (fatty acid synthase thiolase, serine acyltransferase), which is standard transferable biochemistry knowledge. The remaining option C has a generic catalytic description compatible with the protein's likely function. No protein-specific database lookup is strictly required to reach C by elimination among the four offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only C is positionally valid and functionally consistent with the protein. B is impossible by sequence length; A and D describe activities of incompatible enzyme families. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The UniProt entry also annotates position 343 (Glu, 'Nucleophile') as a second active site, but this is not offered as a choice, so it does not create ambiguity among the provided options.",
    "The elimination of A and D depends on the model recognizing that 'beta-ketoacyl synthase' and 'acyltransferase of LM' are specific annotations from other protein contexts rather than plausible descriptions for this sequence. A model unfamiliar with these enzyme families might struggle with this elimination step.",
    "The reviewer-only evidence confirms the protein is a Beta-1,2-glucosyltransferase (EC 2.4.1.391) from Ignavibacterium album, but this identity was not provided to the evaluated model."
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
  "requested_accession": "I0AIT9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "benchmark_sequence_length": 716,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 57,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-06-13",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "current_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "current_source_sequence_length": 716,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 55,
  "selected_historical_version": {
    "accession": "I0AIT9",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "B12GT_IGNAJ",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "selected_historical_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "selected_historical_source_sequence_length": 716,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"I0AIT9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":57,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-06-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Ignavibacteriota\",\"Ignavibacteria\",\"Ignavibacteriales\",\"Ignavibacteriaceae\",\"Ignavibacterium\"],\"scientificName\":\"Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16)\",\"taxonId\":945713}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"IaSGT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.391\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Proton donor/acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":176},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":343},\"start\":{\"modifier\":\"EXACT\",\"value\":343}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":52},\"start\":{\"modifier\":\"EXACT\",\"value\":52}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":99},\"start\":{\"modifier\":\"EXACT\",\"value\":99}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":101},\"start\":{\"modifier\":\"EXACT\",\"value\":101}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":102},\"start\":{\"modifier\":\"EXACT\",\"value\":102}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":175},\"start\":{\"modifier\":\"EXACT\",\"value\":175}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"1\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":176},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":176},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"1\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":278},\"start\":{\"modifier\":\"EXACT\",\"value\":278}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":278},\"start\":{\"modifier\":\"EXACT\",\"value\":278}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"1\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":279},\"start\":{\"modifier\":\"EXACT\",\"value\":279}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":279},\"start\":{\"modifier\":\"EXACT\",\"value\":279}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":343},\"start\":{\"modifier\":\"EXACT\",\"value\":343}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"1\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":349},\"start\":{\"modifier\":\"EXACT\",\"value\":349}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":349},\"start\":{\"modifier\":\"EXACT\",\"value\":349}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C21",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"2\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":358},\"start\":{\"modifier\":\"EXACT\",\"value\":358}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C22",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/18",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"2\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":361},\"start\":{\"modifier\":\"EXACT\",\"value\":361}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C23",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/19",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:1230\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:1230\",\"name\":\"sophorose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":378},\"start\":{\"modifier\":\"EXACT\",\"value\":378}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C24",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/20",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"2\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":708},\"start\":{\"modifier\":\"EXACT\",\"value\":708}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C25",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/features/21",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:15903\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:15903\",\"label\":\"2\",\"name\":\"beta-D-glucose\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":709},\"start\":{\"modifier\":\"EXACT\",\"value\":709}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C26",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Kobayashi K.\",\"Shimizu H.\",\"Tanaka N.\",\"Kuramochi K.\",\"Nakai H.\",\"Nakajima M.\",\"Taguchi H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35065074\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2022.101606\"}],\"citationType\":\"journal article\",\"firstPage\":\"101606\",\"id\":\"35065074\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"101606\",\"publicationDate\":\"2022\",\"title\":\"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.\",\"volume\":\"298\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKW\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL0\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL1\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL3\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL4\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL6\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF GLU-176 AND GLU-343\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   B12GT_IGNAJ             Reviewed;         716 AA.\nAC   I0AIT9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-JUN-2012, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};\nDE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};\nGN   OrderedLocusNames=IALB_1185 {ECO:0000312|EMBL:AFH48896.1};\nOS   Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 /\nOS   Mat9-16).\nOC   Bacteria; Pseudomonadati; Ignavibacteriota; Ignavibacteria;\nOC   Ignavibacteriales; Ignavibacteriaceae; Ignavibacterium.\nOX   NCBI_TaxID=945713;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 25-36",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7VKW, ECO:0007744|PDB:7VKX, ECO:0007744|PDB:7VKY, ECO:0007744|PDB:7VKZ, ECO:0007744|PDB:7VL0, ECO:0007744|PDB:7VL1, ECO:0007744|PDB:7VL2, ECO:0007744|PDB:7VL3, ECO:0007744|PDB:7VL4, ECO:0007744|PDB:7VL5, ECO:0007744|PDB:7VL6}\nRP   X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE;\nRP   SOPHOROSE AND ALTERNATIVE SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF\nRP   GLU-176 AND GLU-343.\nRC   STRAIN=DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16;\nRX   PubMed=35065074; DOI=10.1016/j.jbc.2022.101606;\nRA   Kobayashi K., Shimizu H., Tanaka N., Kuramochi K., Nakai H., Nakajima M.,\nRA   Taguchi H.;\nRT   \"Characterization and structural analyses of a novel glycosyltransferase\nRT   acting on the beta-1,2-glucosidic linkages.\";\nRL   J. Biol. Chem. 298:101606-101606(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 159-161",
  "excerpt": "FT   ACT_SITE        176\nFT                   /note=\"Proton donor/acceptor\"\nFT                   /evidence=\"ECO:0000305|PubMed:35065074\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 162-164",
  "excerpt": "FT   ACT_SITE        343\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000305|PubMed:35065074\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 165-169",
  "excerpt": "FT   BINDING         52\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 170-174",
  "excerpt": "FT   BINDING         99\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 175-179",
  "excerpt": "FT   BINDING         101\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 180-184",
  "excerpt": "FT   BINDING         102\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 185-189",
  "excerpt": "FT   BINDING         175\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 190-195",
  "excerpt": "FT   BINDING         176\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 196-200",
  "excerpt": "FT   BINDING         176\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 201-206",
  "excerpt": "FT   BINDING         278\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 207-211",
  "excerpt": "FT   BINDING         278\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 212-217",
  "excerpt": "FT   BINDING         279\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 218-222",
  "excerpt": "FT   BINDING         279\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 223-227",
  "excerpt": "FT   BINDING         343\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 228-233",
  "excerpt": "FT   BINDING         349\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 234-238",
  "excerpt": "FT   BINDING         349\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H19",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 239-244",
  "excerpt": "FT   BINDING         358\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H20",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 245-250",
  "excerpt": "FT   BINDING         361\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H21",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 251-255",
  "excerpt": "FT   BINDING         378\nFT                   /ligand=\"sophorose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:1230\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKY\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H22",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 256-261",
  "excerpt": "FT   BINDING         708\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "evidence_id": "H23",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "source_locator": "lines 262-267",
  "excerpt": "FT   BINDING         709\nFT                   /ligand=\"beta-D-glucose\"\nFT                   /ligand_id=\"ChEBI:CHEBI:15903\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000269|PubMed:35065074,\nFT                   ECO:0007744|PDB:7VKX\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
