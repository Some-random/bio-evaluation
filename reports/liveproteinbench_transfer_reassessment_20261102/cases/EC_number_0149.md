# EC_number_0149: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0149.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 2.3.1.312

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MIETPYLLFLGDAPDMLAAKVAIGIRDWRPDHAVGQISLPGCGANLGLTEMTLEEAKAAGAKTLVIGVANRGGKISQEWKKVLVQALEEGFDLASGLHNLLRDEPDLAAVAEATGRTLHDVRVPSVQYPIADGVKRRGKRCLAVGTDCSVGKMYTALAMDAEMQARGIKSTFRATGQTGILITGDGVPLDAVIADFMAGSIEYLTPDNDDDHWDLIEGQGSLFHVSYSGVTMALVHGGQPDALILCHEPTRTHMRGLPDYDVPSLEELRDVALPLAQRANKDCKIVGISVNTQHLGEEEAVAYLKEVEGRMGLPAVDPYRHGAGRLVDALAAV

[Multiple Choices]
A. 2.3.1.322
B. 2.7.7.43
C. 2.3.1.312
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

> The supplied sequence exactly matches the UniProt entry annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312. The annotation links the catalytic activity to PubMed evidence code ECO:0000269; the cited reaction is D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+). This supports choice C, although the primary paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include different enzyme reaction classifications, but the sequence and options alone provide no sufficiently specific biological argument for identifying this protein's exact substrate and reaction. Broad sequence-based functional inference would not establish the complete EC number.


**Missing item-specific fact**

> The protein-specific functional assignment identifying the sequence as D-glutamate N-acetyltransferase, and its catalyzed reaction, is needed to select EC 2.3.1.312.


**Reason**

> The reviewer evidence supports the key, but that annotation and its cited experimental evidence were not provided to the evaluated model. Recognizing or retrieving the exact protein entry would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched annotation specifies EC 2.3.1.312; no supplied evidence supports another listed choice.


### Important caveats

- The UniProt evidence links the functional assignment to a cited publication, but that publication was not independently assessed.
- The exact source snapshot used by the benchmark author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include different enzyme reaction classifications, but the sequence and options alone provide no sufficiently specific biological argument for identifying this protein's exact substrate and reaction. Broad sequence-based functional inference would not establish the complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment identifying the sequence as D-glutamate N-acetyltransferase, and its catalyzed reaction, is needed to select EC 2.3.1.312.",
    "reason": "The reviewer evidence supports the key, but that annotation and its cited experimental evidence were not provided to the evaluated model. Recognizing or retrieving the exact protein entry would be lookup, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312. The annotation links the catalytic activity to PubMed evidence code ECO:0000269; the cited reaction is D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+). This supports choice C, although the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt evidence links the functional assignment to a cited publication, but that publication was not independently assessed.",
    "The exact source snapshot used by the benchmark author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation specifies EC 2.3.1.312; no supplied evidence supports another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312. The annotation links the catalytic activity to PubMed evidence code ECO:0000269; the cited reaction is D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+). This supports choice C, although the primary paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include different enzyme reaction classifications, but the sequence and options alone provide no sufficiently specific biological argument for identifying this protein's exact substrate and reaction. Broad sequence-based functional inference would not establish the complete EC number.",
    "missing_item_specific_fact": "The protein-specific functional assignment identifying the sequence as D-glutamate N-acetyltransferase, and its catalyzed reaction, is needed to select EC 2.3.1.312.",
    "reason": "The reviewer evidence supports the key, but that annotation and its cited experimental evidence were not provided to the evaluated model. Recognizing or retrieving the exact protein entry would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation specifies EC 2.3.1.312; no supplied evidence supports another listed choice."
  },
  "important_caveats": [
    "The UniProt evidence links the functional assignment to a cited publication, but that publication was not independently assessed.",
    "The exact source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A2T1AE85 (sequence match confirmed, 333 AA, same SHA256) is annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269 from PubMed:36690779). X-ray crystallography at 2.20 Å (PDB:7XRJ) confirmed catalytic activity and mutagenesis of key residues (HIS-119, ARG-122, SER-125, GLN-177, ASP-185, ASP-190). The reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally established. This is a Swiss-Prot reviewed entry.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) fold motifs (e.g., 'GKISQEWKK', 'GTDCSVGK', 'GDGVPLDA'), which supports classification as an acyltransferase (EC 2.3.1.x), thereby eliminating option B (2.7.7.43, nucleotidyltransferase) and D (5.4.99.14, isomerase). However, this fold-level argument cannot distinguish between EC 2.3.1.322 (option A) and EC 2.3.1.312 (option C), both of which are acetyltransferases in the same subclass.


**Missing item-specific fact**

> The specific substrate identity (D-glutamate for 2.3.1.312 vs. the substrate of 2.3.1.322) required to distinguish the two remaining acyltransferase options. This enzyme was characterized in a 2023 paper (Yu et al., ISME J.) describing a novel D-glutamate catabolic pathway, making it a recently discovered enzyme whose substrate specificity cannot be inferred from general biological knowledge of the GNAT fold alone.


**Reason**

> While the GNAT fold narrows the answer to the 2.3.1.x subclass, the final distinction between two closely related acetyltransferase EC numbers (2.3.1.322 vs. 2.3.1.312) requires knowledge of the specific substrate or a database lookup. No sequence motif in the provided 333-residue protein uniquely encodes 'D-glutamate' as the substrate without external annotation or memorization of this specific enzyme's characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both options A (2.3.1.322) and C (2.3.1.312) are acetyltransferases in the same EC subclass. Without specific substrate knowledge or database access, a model identifying the GNAT fold could reasonably select either option. The distractors B (nucleotidyltransferase) and D (isomerase) are eliminable by fold recognition, but A vs. C requires item-specific knowledge.


### Important caveats

- The expected answer is experimentally validated (X-ray crystallography, mutagenesis, PubMed:36690779), so the key is scientifically correct.
- This is a novel enzyme described in 2023, making it unlikely to appear in pre-2023 training data, further increasing reliance on database lookup.
- The GNAT fold identification provides partial reasoning support (eliminates B and D) but is insufficient for the final A-vs-C discrimination.
- The identity of the protein was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) fold motifs (e.g., 'GKISQEWKK', 'GTDCSVGK', 'GDGVPLDA'), which supports classification as an acyltransferase (EC 2.3.1.x), thereby eliminating option B (2.7.7.43, nucleotidyltransferase) and D (5.4.99.14, isomerase). However, this fold-level argument cannot distinguish between EC 2.3.1.322 (option A) and EC 2.3.1.312 (option C), both of which are acetyltransferases in the same subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (D-glutamate for 2.3.1.312 vs. the substrate of 2.3.1.322) required to distinguish the two remaining acyltransferase options. This enzyme was characterized in a 2023 paper (Yu et al., ISME J.) describing a novel D-glutamate catabolic pathway, making it a recently discovered enzyme whose substrate specificity cannot be inferred from general biological knowledge of the GNAT fold alone.",
    "reason": "While the GNAT fold narrows the answer to the 2.3.1.x subclass, the final distinction between two closely related acetyltransferase EC numbers (2.3.1.322 vs. 2.3.1.312) requires knowledge of the specific substrate or a database lookup. No sequence motif in the provided 333-residue protein uniquely encodes 'D-glutamate' as the substrate without external annotation or memorization of this specific enzyme's characterization."
  },
  "case_id": "EC_number_0149",
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
    "reason": "UniProt entry A0A2T1AE85 (sequence match confirmed, 333 AA, same SHA256) is annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269 from PubMed:36690779). X-ray crystallography at 2.20 Å (PDB:7XRJ) confirmed catalytic activity and mutagenesis of key residues (HIS-119, ARG-122, SER-125, GLN-177, ASP-185, ASP-190). The reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally established. This is a Swiss-Prot reviewed entry."
  },
  "important_caveats": [
    "The expected answer is experimentally validated (X-ray crystallography, mutagenesis, PubMed:36690779), so the key is scientifically correct.",
    "This is a novel enzyme described in 2023, making it unlikely to appear in pre-2023 training data, further increasing reliance on database lookup.",
    "The GNAT fold identification provides partial reasoning support (eliminates B and D) but is insufficient for the final A-vs-C discrimination.",
    "The identity of the protein was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both options A (2.3.1.322) and C (2.3.1.312) are acetyltransferases in the same EC subclass. Without specific substrate knowledge or database access, a model identifying the GNAT fold could reasonably select either option. The distractors B (nucleotidyltransferase) and D (isomerase) are eliminable by fold recognition, but A vs. C requires item-specific knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A2T1AE85 (sequence match confirmed, 333 AA, same SHA256) is annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269 from PubMed:36690779). X-ray crystallography at 2.20 Å (PDB:7XRJ) confirmed catalytic activity and mutagenesis of key residues (HIS-119, ARG-122, SER-125, GLN-177, ASP-185, ASP-190). The reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally established. This is a Swiss-Prot reviewed entry.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) fold motifs (e.g., 'GKISQEWKK', 'GTDCSVGK', 'GDGVPLDA'), which supports classification as an acyltransferase (EC 2.3.1.x), thereby eliminating option B (2.7.7.43, nucleotidyltransferase) and D (5.4.99.14, isomerase). However, this fold-level argument cannot distinguish between EC 2.3.1.322 (option A) and EC 2.3.1.312 (option C), both of which are acetyltransferases in the same subclass.",
    "missing_item_specific_fact": "The specific substrate identity (D-glutamate for 2.3.1.312 vs. the substrate of 2.3.1.322) required to distinguish the two remaining acyltransferase options. This enzyme was characterized in a 2023 paper (Yu et al., ISME J.) describing a novel D-glutamate catabolic pathway, making it a recently discovered enzyme whose substrate specificity cannot be inferred from general biological knowledge of the GNAT fold alone.",
    "reason": "While the GNAT fold narrows the answer to the 2.3.1.x subclass, the final distinction between two closely related acetyltransferase EC numbers (2.3.1.322 vs. 2.3.1.312) requires knowledge of the specific substrate or a database lookup. No sequence motif in the provided 333-residue protein uniquely encodes 'D-glutamate' as the substrate without external annotation or memorization of this specific enzyme's characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both options A (2.3.1.322) and C (2.3.1.312) are acetyltransferases in the same EC subclass. Without specific substrate knowledge or database access, a model identifying the GNAT fold could reasonably select either option. The distractors B (nucleotidyltransferase) and D (isomerase) are eliminable by fold recognition, but A vs. C requires item-specific knowledge."
  },
  "important_caveats": [
    "The expected answer is experimentally validated (X-ray crystallography, mutagenesis, PubMed:36690779), so the key is scientifically correct.",
    "This is a novel enzyme described in 2023, making it unlikely to appear in pre-2023 training data, further increasing reliance on database lookup.",
    "The GNAT fold identification provides partial reasoning support (eliminates B and D) but is insufficient for the final A-vs-C discrimination.",
    "The identity of the protein was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns EC 2.3.1.312 and reports the specific reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA, with experimental evidence (ECO:0000269). This supports choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad enzyme-class inference, but choices A and C are both EC 2.3.1 acyltransferases. The provided sequence has no evident feature that meaningfully distinguishes their substrate-specific reactions.


**Missing item-specific fact**

> Which substrate-specific reaction this protein catalyzes, or a functionally characterized close homolog that establishes that reaction.


**Reason**

> General transferase or cofactor-binding knowledge could help distinguish some alternatives, but it does not meaningfully resolve the key distinction between A and C. Choosing C requires protein-specific functional information or a sufficiently close, characterized homolog.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports C, and no evidence establishes another offered EC number as a valid annotation for this protein. The sequence-based distinction is underdetermined, but that alone does not show that multiple options are biochemically correct.


### Important caveats

- The reviewer-only source reports an experimentally supported reaction for a sequence-matched entry; the primary paper was not independently reviewed here.
- The source identity and annotation were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad enzyme-class inference, but choices A and C are both EC 2.3.1 acyltransferases. The provided sequence has no evident feature that meaningfully distinguishes their substrate-specific reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Which substrate-specific reaction this protein catalyzes, or a functionally characterized close homolog that establishes that reaction.",
    "reason": "General transferase or cofactor-binding knowledge could help distinguish some alternatives, but it does not meaningfully resolve the key distinction between A and C. Choosing C requires protein-specific functional information or a sufficiently close, characterized homolog."
  },
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.1.312 and reports the specific reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA, with experimental evidence (ECO:0000269). This supports choice C."
  },
  "important_caveats": [
    "The reviewer-only source reports an experimentally supported reaction for a sequence-matched entry; the primary paper was not independently reviewed here.",
    "The source identity and annotation were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C, and no evidence establishes another offered EC number as a valid annotation for this protein. The sequence-based distinction is underdetermined, but that alone does not show that multiple options are biochemically correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.1.312 and reports the specific reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA, with experimental evidence (ECO:0000269). This supports choice C.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad enzyme-class inference, but choices A and C are both EC 2.3.1 acyltransferases. The provided sequence has no evident feature that meaningfully distinguishes their substrate-specific reactions.",
    "missing_item_specific_fact": "Which substrate-specific reaction this protein catalyzes, or a functionally characterized close homolog that establishes that reaction.",
    "reason": "General transferase or cofactor-binding knowledge could help distinguish some alternatives, but it does not meaningfully resolve the key distinction between A and C. Choosing C requires protein-specific functional information or a sufficiently close, characterized homolog."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C, and no evidence establishes another offered EC number as a valid annotation for this protein. The sequence-based distinction is underdetermined, but that alone does not show that multiple options are biochemically correct."
  },
  "important_caveats": [
    "The reviewer-only source reports an experimentally supported reaction for a sequence-matched entry; the primary paper was not independently reviewed here.",
    "The source identity and annotation were not part of the original model input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2T1AE85 (Swiss-Prot, reviewed) annotates this 333-aa protein as D-glutamate N-acetyltransferase with EC 2.3.1.312, supported by experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023) and X-ray crystallography (PDB:7XRJ, 2.20 Å). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H⁺ is confirmed by Rhea (RHEA:76495). The benchmark sequence SHA256 matches the source sequence exactly. The EC number assignment is experimentally validated, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable GNAT (GCN5-related N-acetyltransferase) fold signature, notably the 'VANRGGKISQ' motif (RGG pattern characteristic of the CoA-binding loop in GNAT enzymes) and the overall ~333-aa architecture with a central β-sheet core flanked by α-helices. This family-level recognition legitimately eliminates option B (EC 2.7.7.43, a nucleotidyltransferase with an entirely different fold and catalytic mechanism involving a nucleotidyl group transfer) and option D (EC 5.4.99.14, an isomerase catalyzing intramolecular rearrangements, not an intermolecular acyl transfer). However, both remaining options A (EC 2.3.1.322) and C (EC 2.3.1.312) are acyltransferases within the 2.3.1.x sub-subclass, which encompasses hundreds of GNAT-fold enzymes with diverse substrates (histones, polyamines, amino acids, aromatic amines, etc.). The specific substrate identity—D-glutamate for 2.3.1.312 versus whatever substrate 2.3.1.322 acts upon—is determined by a small set of active-site residues whose arrangement cannot be reliably predicted from general GNAT family knowledge. No conserved motif within the GNAT superfamily encodes D-glutamate specificity in a way that a model trained on other acetyltransferases could use to discriminate 312 from 322.


**Missing item-specific fact**

> The specific substrate identity of EC 2.3.1.322 and the precise active-site residue configuration that confers D-glutamate (as opposed to another substrate) specificity in this particular GNAT-fold enzyme. This enzyme was characterized experimentally only in 2023 (PubMed:36690779), so no well-established family-level substrate-specificity pattern exists that would allow transfer from other proteins.


**Reason**

> While the GNAT fold recognition is a valid transferable inference that narrows the four choices to two (eliminating the nucleotidyltransferase and isomerase options), the final distinction between EC 2.3.1.312 and EC 2.3.1.322 requires knowing the exact substrate specificity of this particular enzyme. Both are acyltransferases sharing the same broad fold. The substrate-determining residues in GNAT enzymes are highly variable and not predictable from general family-level knowledge, especially for a novel enzyme first characterized in 2023. This constitutes a fact about this exact protein that is not derivable from transferable knowledge of other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (2.3.1.322) and C (2.3.1.312) are acyltransferases in the 2.3.1.x sub-subclass. Without specific knowledge of the substrate of 2.3.1.322 and the active-site determinants of D-glutamate specificity, a knowledgeable model using only sequence and general family knowledge cannot confidently choose between them. The GNAT fold is shared by both.


### Important caveats

- The EC 2.3.1.312 assignment is experimentally validated (X-ray crystallography at 2.20 Å, mutagenesis of six active-site residues, enzymatic assay), making the key highly reliable.
- The GNAT fold recognition legitimately eliminates options B and D, so the question is not purely a four-way guess; it reduces to a two-way choice between closely related acyltransferase EC numbers.
- The enzyme and its EC number were first reported in 2023, meaning there is limited accumulated family-level knowledge from other proteins that could inform substrate-specificity predictions for this particular subfamily.
- The reviewer-only evidence confirms exact sequence match (SHA256) between the benchmark input and UniProt A0A2T1AE85, so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable GNAT (GCN5-related N-acetyltransferase) fold signature, notably the 'VANRGGKISQ' motif (RGG pattern characteristic of the CoA-binding loop in GNAT enzymes) and the overall ~333-aa architecture with a central β-sheet core flanked by α-helices. This family-level recognition legitimately eliminates option B (EC 2.7.7.43, a nucleotidyltransferase with an entirely different fold and catalytic mechanism involving a nucleotidyl group transfer) and option D (EC 5.4.99.14, an isomerase catalyzing intramolecular rearrangements, not an intermolecular acyl transfer). However, both remaining options A (EC 2.3.1.322) and C (EC 2.3.1.312) are acyltransferases within the 2.3.1.x sub-subclass, which encompasses hundreds of GNAT-fold enzymes with diverse substrates (histones, polyamines, amino acids, aromatic amines, etc.). The specific substrate identity—D-glutamate for 2.3.1.312 versus whatever substrate 2.3.1.322 acts upon—is determined by a small set of active-site residues whose arrangement cannot be reliably predicted from general GNAT family knowledge. No conserved motif within the GNAT superfamily encodes D-glutamate specificity in a way that a model trained on other acetyltransferases could use to discriminate 312 from 322.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of EC 2.3.1.322 and the precise active-site residue configuration that confers D-glutamate (as opposed to another substrate) specificity in this particular GNAT-fold enzyme. This enzyme was characterized experimentally only in 2023 (PubMed:36690779), so no well-established family-level substrate-specificity pattern exists that would allow transfer from other proteins.",
    "reason": "While the GNAT fold recognition is a valid transferable inference that narrows the four choices to two (eliminating the nucleotidyltransferase and isomerase options), the final distinction between EC 2.3.1.312 and EC 2.3.1.322 requires knowing the exact substrate specificity of this particular enzyme. Both are acyltransferases sharing the same broad fold. The substrate-determining residues in GNAT enzymes are highly variable and not predictable from general family-level knowledge, especially for a novel enzyme first characterized in 2023. This constitutes a fact about this exact protein that is not derivable from transferable knowledge of other proteins."
  },
  "case_id": "EC_number_0149",
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
    "reason": "The UniProt entry A0A2T1AE85 (Swiss-Prot, reviewed) annotates this 333-aa protein as D-glutamate N-acetyltransferase with EC 2.3.1.312, supported by experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023) and X-ray crystallography (PDB:7XRJ, 2.20 Å). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H⁺ is confirmed by Rhea (RHEA:76495). The benchmark sequence SHA256 matches the source sequence exactly. The EC number assignment is experimentally validated, not merely computational."
  },
  "important_caveats": [
    "The EC 2.3.1.312 assignment is experimentally validated (X-ray crystallography at 2.20 Å, mutagenesis of six active-site residues, enzymatic assay), making the key highly reliable.",
    "The GNAT fold recognition legitimately eliminates options B and D, so the question is not purely a four-way guess; it reduces to a two-way choice between closely related acyltransferase EC numbers.",
    "The enzyme and its EC number were first reported in 2023, meaning there is limited accumulated family-level knowledge from other proteins that could inform substrate-specificity predictions for this particular subfamily.",
    "The reviewer-only evidence confirms exact sequence match (SHA256) between the benchmark input and UniProt A0A2T1AE85, so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (2.3.1.322) and C (2.3.1.312) are acyltransferases in the 2.3.1.x sub-subclass. Without specific knowledge of the substrate of 2.3.1.322 and the active-site determinants of D-glutamate specificity, a knowledgeable model using only sequence and general family knowledge cannot confidently choose between them. The GNAT fold is shared by both."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2T1AE85 (Swiss-Prot, reviewed) annotates this 333-aa protein as D-glutamate N-acetyltransferase with EC 2.3.1.312, supported by experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023) and X-ray crystallography (PDB:7XRJ, 2.20 Å). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H⁺ is confirmed by Rhea (RHEA:76495). The benchmark sequence SHA256 matches the source sequence exactly. The EC number assignment is experimentally validated, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable GNAT (GCN5-related N-acetyltransferase) fold signature, notably the 'VANRGGKISQ' motif (RGG pattern characteristic of the CoA-binding loop in GNAT enzymes) and the overall ~333-aa architecture with a central β-sheet core flanked by α-helices. This family-level recognition legitimately eliminates option B (EC 2.7.7.43, a nucleotidyltransferase with an entirely different fold and catalytic mechanism involving a nucleotidyl group transfer) and option D (EC 5.4.99.14, an isomerase catalyzing intramolecular rearrangements, not an intermolecular acyl transfer). However, both remaining options A (EC 2.3.1.322) and C (EC 2.3.1.312) are acyltransferases within the 2.3.1.x sub-subclass, which encompasses hundreds of GNAT-fold enzymes with diverse substrates (histones, polyamines, amino acids, aromatic amines, etc.). The specific substrate identity—D-glutamate for 2.3.1.312 versus whatever substrate 2.3.1.322 acts upon—is determined by a small set of active-site residues whose arrangement cannot be reliably predicted from general GNAT family knowledge. No conserved motif within the GNAT superfamily encodes D-glutamate specificity in a way that a model trained on other acetyltransferases could use to discriminate 312 from 322.",
    "missing_item_specific_fact": "The specific substrate identity of EC 2.3.1.322 and the precise active-site residue configuration that confers D-glutamate (as opposed to another substrate) specificity in this particular GNAT-fold enzyme. This enzyme was characterized experimentally only in 2023 (PubMed:36690779), so no well-established family-level substrate-specificity pattern exists that would allow transfer from other proteins.",
    "reason": "While the GNAT fold recognition is a valid transferable inference that narrows the four choices to two (eliminating the nucleotidyltransferase and isomerase options), the final distinction between EC 2.3.1.312 and EC 2.3.1.322 requires knowing the exact substrate specificity of this particular enzyme. Both are acyltransferases sharing the same broad fold. The substrate-determining residues in GNAT enzymes are highly variable and not predictable from general family-level knowledge, especially for a novel enzyme first characterized in 2023. This constitutes a fact about this exact protein that is not derivable from transferable knowledge of other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (2.3.1.322) and C (2.3.1.312) are acyltransferases in the 2.3.1.x sub-subclass. Without specific knowledge of the substrate of 2.3.1.322 and the active-site determinants of D-glutamate specificity, a knowledgeable model using only sequence and general family knowledge cannot confidently choose between them. The GNAT fold is shared by both."
  },
  "important_caveats": [
    "The EC 2.3.1.312 assignment is experimentally validated (X-ray crystallography at 2.20 Å, mutagenesis of six active-site residues, enzymatic assay), making the key highly reliable.",
    "The GNAT fold recognition legitimately eliminates options B and D, so the question is not purely a four-way guess; it reduces to a two-way choice between closely related acyltransferase EC numbers.",
    "The enzyme and its EC number were first reported in 2023, meaning there is limited accumulated family-level knowledge from other proteins that could inform substrate-specificity predictions for this particular subfamily.",
    "The reviewer-only evidence confirms exact sequence match (SHA256) between the benchmark input and UniProt A0A2T1AE85, so the annotation applies directly to the supplied sequence."
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
  "requested_accession": "A0A2T1AE85",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "c0d9f366f41666bbc0ced1375f251e0666f921019f749a5a93a254b4c941f9e7",
  "benchmark_sequence_length": 333,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-07-18",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "current_source_sequence_sha256": "c0d9f366f41666bbc0ced1375f251e0666f921019f749a5a93a254b4c941f9e7",
  "current_source_sequence_length": 333,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 17,
  "selected_historical_version": {
    "accession": "A0A2T1AE85",
    "database": "Swiss-Prot",
    "entryVersion": 17,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DGCN_TRISK",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "selected_historical_source_sequence_sha256": "c0d9f366f41666bbc0ced1375f251e0666f921019f749a5a93a254b4c941f9e7",
  "selected_historical_source_sequence_length": 333,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 17,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A2T1AE85\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-07-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Epibacterium scottomollicae\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Alphaproteobacteria\",\"Rhodobacterales\",\"Paracoccaceae\",\"Tritonibacter\"],\"scientificName\":\"Tritonibacter scottomollicae\",\"taxonId\":483013}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.312\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"D-glutamate N-acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:76496\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76495\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29986\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:195260\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json",
  "source_sha256": "09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159",
  "retrieved_utc": "2026-11-02T04:24:51.195751+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Yu Y.\",\"Wang P.\",\"Cao H.Y.\",\"Teng Z.J.\",\"Zhu Y.\",\"Wang M.\",\"McMinn A.\",\"Chen Y.\",\"Xiang H.\",\"Zhang Y.Z.\",\"Chen X.L.\",\"Zhang Y.Q.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36690779\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41396-023-01364-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"36690779\",\"journal\":\"ISME J.\",\"lastPage\":\"548\",\"publicationDate\":\"2023\",\"title\":\"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.\",\"volume\":\"17\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7XRJ\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 25328 / CCUG 55858 / LMG 24367 / R-28751\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   DGCN_TRISK              Reviewed;         333 AA.\nAC   A0A2T1AE85;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUL-2018, sequence version 1.\nDT   28-JAN-2026, entry version 17.\nDE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\nGN   Name=dgcN {ECO:0000303|PubMed:36690779};\nGN   ORFNames=CLV89_10851 {ECO:0000312|EMBL:PRZ46905.1};\nOS   Tritonibacter scottomollicae (Epibacterium scottomollicae).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;\nOC   Rhodobacterales; Paracoccaceae; Tritonibacter.\nOX   NCBI_TaxID=483013;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 17,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "source_locator": "lines 6-7",
  "excerpt": "DE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 17,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "source_locator": "lines 21-30",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7XRJ}\nRP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY, AND\nRP   MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190.\nRC   STRAIN=DSM 25328 / CCUG 55858 / LMG 24367 / R-28751;\nRX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;\nRA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,\nRA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;\nRT   \"Novel D-glutamate catabolic pathway in marine Proteobacteria and\nRT   halophilic archaea.\";\nRL   ISME J. 17:537-548(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 17,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17",
  "source_sha256": "4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6",
  "retrieved_utc": "2026-11-02T04:24:54.258050+00:00",
  "source_locator": "lines 36-42",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+);\nCC         Xref=Rhea:RHEA:76495, ChEBI:CHEBI:15378, ChEBI:CHEBI:29986,\nCC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195260;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76496;\nCC         Evidence={ECO:0000305|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 17,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
