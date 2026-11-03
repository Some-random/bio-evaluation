# cofactor_0146: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0146.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **B** — Zn(2+)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | no saved label | no saved label | output error (invalid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEGTERVRPQRVEQKLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGSAREVQFFTDEDGERNLVALEKKGGIWRRSASDADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLLYDSLYFHGQQVAAGDILAAEVVKGGTTHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. pantetheine 4'-phosphate
B. Zn(2+)
C. Mo-bis(molybdopterin guanine dinucleotide)
D. Na(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact sequence matches the annotated Neisseria gonorrhoeae Mpg protein. UniProt annotates Zn(2+) as its cofactor and says it binds one zinc ion per subunit; the cofactor evidence is transferred by similarity (ECO:0000250), not a direct measurement established here for this exact protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C4](#evidence-c4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A zinc metalloprotease would use Zn(2+), but identifying this sequence as that particular metalloprotease requires recognizing its protein family or obtaining its annotation; the input supplies no function or organism context.


**Missing item-specific fact**

> The protein-specific identity/function and its zinc-cofactor annotation are absent from the question.


**Reason**

> The sequence alone does not provide an unambiguous, readily interpretable basis for identifying the enzyme family and its cofactor. Remembering or retrieving the exact sequence's annotation would distinguish the options, but that is lookup or memorization rather than reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports Zn(2+); the other listed options are not supported by the supplied reviewer evidence.


### Important caveats

- The cofactor annotation is similarity-transferred; the evidence excerpts do not establish a direct zinc-binding experiment on this exact protein.
- The reviewer-only accession and annotations were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A zinc metalloprotease would use Zn(2+), but identifying this sequence as that particular metalloprotease requires recognizing its protein family or obtaining its annotation; the input supplies no function or organism context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity/function and its zinc-cofactor annotation are absent from the question.",
    "reason": "The sequence alone does not provide an unambiguous, readily interpretable basis for identifying the enzyme family and its cofactor. Remembering or retrieving the exact sequence's annotation would distinguish the options, but that is lookup or memorization rather than reasoning from supplied context."
  },
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Neisseria gonorrhoeae Mpg protein. UniProt annotates Zn(2+) as its cofactor and says it binds one zinc ion per subunit; the cofactor evidence is transferred by similarity (ECO:0000250), not a direct measurement established here for this exact protein."
  },
  "important_caveats": [
    "The cofactor annotation is similarity-transferred; the evidence excerpts do not establish a direct zinc-binding experiment on this exact protein.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports Zn(2+); the other listed options are not supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Neisseria gonorrhoeae Mpg protein. UniProt annotates Zn(2+) as its cofactor and says it binds one zinc ion per subunit; the cofactor evidence is transferred by similarity (ECO:0000250), not a direct measurement established here for this exact protein.",
    "evidence_ids": ["C1", "C5", "C4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A zinc metalloprotease would use Zn(2+), but identifying this sequence as that particular metalloprotease requires recognizing its protein family or obtaining its annotation; the input supplies no function or organism context.",
    "missing_item_specific_fact": "The protein-specific identity/function and its zinc-cofactor annotation are absent from the question.",
    "reason": "The sequence alone does not provide an unambiguous, readily interpretable basis for identifying the enzyme family and its cofactor. Remembering or retrieving the exact sequence's annotation would distinguish the options, but that is lookup or memorization rather than reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports Zn(2+); the other listed options are not supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The cofactor annotation is similarity-transferred; the evidence excerpts do not establish a direct zinc-binding experiment on this exact protein.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5F676 explicitly annotates Zn(2+) as the cofactor (CHEBI:29105, 'Binds 1 zinc ion per subunit'). The protein is named 'Zinc metallopeptidase'/'Zinc metalloprotease' with EC 3.4.24.- (metalloendopeptidase). The M23B family designation (PubMed:22334697) and mutagenesis of His-295, Asp-299, His-373, His-375 confirm zinc coordination. The cofactor annotation itself uses ECO:0000250 (similarity to E0N688), but the referenced experimental work on the M23B family and the His/Asp/H/H mutagenesis data provide strong indirect experimental support. The His-rich motif (HANGVETLYAHLSAF...GPHLHYEARING) visible in the sequence is consistent with the M23 zinc-binding architecture.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains a conserved His-Asp-His-His cluster (HANGVETLYAHLSAF...GPHLHYEARING) characteristic of the M23-family zinc-binding site. A model with general metalloenzyme knowledge can recognize this His cluster as a metal-coordination motif. Additionally, the N-terminal hydrophobic signal peptide suggests a secreted/exported protein, and many exported peptidases (especially those acting on peptidoglycan) are zinc-dependent. The other three options are cofactors for entirely different enzyme classes: pantetheine 4'-phosphate for acyl-transfer reactions, Mo-bis-MGD for molybdenum oxidoreductases, and Na+ is not a recognized catalytic cofactor for peptidases. Eliminating these leaves Zn(2+) as the only chemically plausible cofactor for a peptidase.


**Missing item-specific fact**

> None strictly required. Identifying the exact M23B family assignment would benefit from database lookup, but the His/Asp zinc-binding motif is visible in the sequence and general knowledge of metallopeptidase cofactor requirements suffices to select Zn(2+) over the other options.


**Reason**

> The zinc-binding His cluster is present in the supplied sequence and recognizable through pattern recognition. The elimination of pantetheine, Mo-bis-MGD, and Na+ relies on general knowledge of which enzyme classes use those cofactors. A model need not know the specific protein name to reason that a peptidase-like domain with a His/Asp cluster requires zinc.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (pantetheine 4'-phosphate, Mo-bis-MGD, Na+) are cofactors for acyltransferases, molybdenum oxidoreductases, and non-enzymatic/transport roles respectively—none are associated with peptidase catalysis. Zn(2+) is the only cofactor consistent with a metallopeptidase. No ambiguity exists.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to E0N688), not direct experimental determination on this protein. However, the M23B family is well-established as zinc-dependent, and the mutagenesis data on the His/Asp residues (PubMed:22334697) provide strong experimental corroboration.
- The protein was only integrated into Swiss-Prot in February 2025; at the time of benchmark construction, the author may have relied on TrEMBL annotation or literature rather than a curated Swiss-Prot entry.
- The sequence-match between the benchmark input and UniProt Q5F676 is confirmed (430 aa, SHA-256 match).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a conserved His-Asp-His-His cluster (HANGVETLYAHLSAF...GPHLHYEARING) characteristic of the M23-family zinc-binding site. A model with general metalloenzyme knowledge can recognize this His cluster as a metal-coordination motif. Additionally, the N-terminal hydrophobic signal peptide suggests a secreted/exported protein, and many exported peptidases (especially those acting on peptidoglycan) are zinc-dependent. The other three options are cofactors for entirely different enzyme classes: pantetheine 4'-phosphate for acyl-transfer reactions, Mo-bis-MGD for molybdenum oxidoreductases, and Na+ is not a recognized catalytic cofactor for peptidases. Eliminating these leaves Zn(2+) as the only chemically plausible cofactor for a peptidase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Identifying the exact M23B family assignment would benefit from database lookup, but the His/Asp zinc-binding motif is visible in the sequence and general knowledge of metallopeptidase cofactor requirements suffices to select Zn(2+) over the other options.",
    "reason": "The zinc-binding His cluster is present in the supplied sequence and recognizable through pattern recognition. The elimination of pantetheine, Mo-bis-MGD, and Na+ relies on general knowledge of which enzyme classes use those cofactors. A model need not know the specific protein name to reason that a peptidase-like domain with a His/Asp cluster requires zinc."
  },
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5F676 explicitly annotates Zn(2+) as the cofactor (CHEBI:29105, 'Binds 1 zinc ion per subunit'). The protein is named 'Zinc metallopeptidase'/'Zinc metalloprotease' with EC 3.4.24.- (metalloendopeptidase). The M23B family designation (PubMed:22334697) and mutagenesis of His-295, Asp-299, His-373, His-375 confirm zinc coordination. The cofactor annotation itself uses ECO:0000250 (similarity to E0N688), but the referenced experimental work on the M23B family and the His/Asp/H/H mutagenesis data provide strong indirect experimental support. The His-rich motif (HANGVETLYAHLSAF...GPHLHYEARING) visible in the sequence is consistent with the M23 zinc-binding architecture."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to E0N688), not direct experimental determination on this protein. However, the M23B family is well-established as zinc-dependent, and the mutagenesis data on the His/Asp residues (PubMed:22334697) provide strong experimental corroboration.",
    "The protein was only integrated into Swiss-Prot in February 2025; at the time of benchmark construction, the author may have relied on TrEMBL annotation or literature rather than a curated Swiss-Prot entry.",
    "The sequence-match between the benchmark input and UniProt Q5F676 is confirmed (430 aa, SHA-256 match)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (pantetheine 4'-phosphate, Mo-bis-MGD, Na+) are cofactors for acyltransferases, molybdenum oxidoreductases, and non-enzymatic/transport roles respectively—none are associated with peptidase catalysis. Zn(2+) is the only cofactor consistent with a metallopeptidase. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5F676 explicitly annotates Zn(2+) as the cofactor (CHEBI:29105, 'Binds 1 zinc ion per subunit'). The protein is named 'Zinc metallopeptidase'/'Zinc metalloprotease' with EC 3.4.24.- (metalloendopeptidase). The M23B family designation (PubMed:22334697) and mutagenesis of His-295, Asp-299, His-373, His-375 confirm zinc coordination. The cofactor annotation itself uses ECO:0000250 (similarity to E0N688), but the referenced experimental work on the M23B family and the His/Asp/H/H mutagenesis data provide strong indirect experimental support. The His-rich motif (HANGVETLYAHLSAF...GPHLHYEARING) visible in the sequence is consistent with the M23 zinc-binding architecture.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a conserved His-Asp-His-His cluster (HANGVETLYAHLSAF...GPHLHYEARING) characteristic of the M23-family zinc-binding site. A model with general metalloenzyme knowledge can recognize this His cluster as a metal-coordination motif. Additionally, the N-terminal hydrophobic signal peptide suggests a secreted/exported protein, and many exported peptidases (especially those acting on peptidoglycan) are zinc-dependent. The other three options are cofactors for entirely different enzyme classes: pantetheine 4'-phosphate for acyl-transfer reactions, Mo-bis-MGD for molybdenum oxidoreductases, and Na+ is not a recognized catalytic cofactor for peptidases. Eliminating these leaves Zn(2+) as the only chemically plausible cofactor for a peptidase.",
    "missing_item_specific_fact": "None strictly required. Identifying the exact M23B family assignment would benefit from database lookup, but the His/Asp zinc-binding motif is visible in the sequence and general knowledge of metallopeptidase cofactor requirements suffices to select Zn(2+) over the other options.",
    "reason": "The zinc-binding His cluster is present in the supplied sequence and recognizable through pattern recognition. The elimination of pantetheine, Mo-bis-MGD, and Na+ relies on general knowledge of which enzyme classes use those cofactors. A model need not know the specific protein name to reason that a peptidase-like domain with a His/Asp cluster requires zinc."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (pantetheine 4'-phosphate, Mo-bis-MGD, Na+) are cofactors for acyltransferases, molybdenum oxidoreductases, and non-enzymatic/transport roles respectively—none are associated with peptidase catalysis. Zn(2+) is the only cofactor consistent with a metallopeptidase. No ambiguity exists."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to E0N688), not direct experimental determination on this protein. However, the M23B family is well-established as zinc-dependent, and the mutagenesis data on the His/Asp residues (PubMed:22334697) provide strong experimental corroboration.",
    "The protein was only integrated into Swiss-Prot in February 2025; at the time of benchmark construction, the author may have relied on TrEMBL annotation or literature rather than a curated Swiss-Prot entry.",
    "The sequence-match between the benchmark input and UniProt Q5F676 is confirmed (430 aa, SHA-256 match)."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1127)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates one Zn(2+) ion per subunit as the cofactor. This annotation is transferred from a related UniProt protein, rather than direct experimental evidence for this exact sequence, but it supports the keyed answer.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is compatible with a zinc-dependent metallopeptidase family: such enzymes use conserved histidine/aspartate-containing catalytic features to coordinate Zn(2+). That family-level pattern distinguishes zinc from pantetheine 4'-phosphate, a molybdopterin cofactor, and sodium.",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from metallopeptidase sequence patterns and family knowledge meaningfully favors Zn(2+) among these choices; recalling this exact protein's annotation is not necessary. The sequence alone may not establish the precise metal-binding details experimentally.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives are distinct, and the zinc-metallopeptidase inference favors only Zn(2+)."
  },
  "important_caveats": [
    "The supplied cofactor annotation is similarity-transferred; it does not itself document direct measurement of zinc binding for this exact protein."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q5F676) explicitly annotates this protein as a zinc metallopeptidase (M23B family) with Zn(2+) as cofactor. The COFACTOR comment states Zn(2+) with evidence ECO:0000250 (similarity-based from E0N688). However, the mutagenesis data (PubMed 22334697) experimentally confirmed the roles of His-295, Asp-299, His-373, and His-375 — a classic zinc-coordinating tetrad in metalloproteases — providing strong experimental support for zinc coordination. The protein is also assigned EC 3.4.24.- (metalloendopeptidase class) and named 'Zinc metallopeptidase'/'Zinc metalloprotease' in the entry.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C7](#evidence-c7), [H6](#evidence-h6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple histidine-rich clusters in patterns characteristic of zinc-binding sites in metalloproteases: 'HANGVETLYAH' and 'PHLHYEARING' provide the H...H spacing typical of zinc coordination in the M23B/NlpC/P60 peptidase family. The overall architecture — an N-terminal signal peptide (hydrophobic stretch MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEG), a peptidase-like beta-sheet-rich domain with conserved 'GGDGSARE' glycine-rich loop, and the C-terminal His/Asp clusters — is consistent with a secreted/outer-membrane metalloprotease. Transferable knowledge of the M23B family (NlpC/P60 domain, found in many bacterial peptidoglycan hydrolases) establishes that these enzymes are zinc-dependent. The other options are readily excluded: pantetheine 4'-phosphate requires acyltransferase/ACP-binding architecture absent here; Mo-bis(molybdopterin) requires the highly conserved Mo-S cluster cysteine motifs of molybdoenzymes, which are absent; Na(+) is not a recognized enzymatic cofactor for peptidases. Thus the zinc-binding histidine/asp pattern and peptidase fold meaningfully distinguish option B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the H-H and H-D-H spacing patterns, the peptidase-like fold, and the M23B/NlpC/P60 family architecture can infer Zn(2+) from transferable knowledge of metalloprotease families. The distractors (pantetheine, molybdopterin, Na+) lack any supporting sequence features, making B the clearly best-supported choice among the four.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The zinc-binding histidine patterns and peptidase fold uniquely support Zn(2+) among the four choices. No other option has any sequence-level support.


### Important caveats

- The direct cofactor annotation in UniProt uses ECO:0000250 (similarity-based inference from E0N688), not a direct experimental cofactor-binding assay. However, site-directed mutagenesis of the four zinc-coordinating residues (His-295, Asp-299, His-373, His-375) with loss of activity provides strong indirect experimental evidence for zinc dependence.
- The protein was first characterized in 2005 (oxidative stress response) and its peptidase activity and zinc dependence were experimentally demonstrated in 2012 (PubMed 22334697). The benchmark question was constructed from a dataset whose exact snapshot date is unknown, but the sequence has been unchanged since 2005.
- The cofactor annotation is transferred by similarity from E0N688 (a related M23B protein), which is a standard and well-accepted practice for conserved metal-binding sites in peptidase families.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple histidine-rich clusters in patterns characteristic of zinc-binding sites in metalloproteases: 'HANGVETLYAH' and 'PHLHYEARING' provide the H...H spacing typical of zinc coordination in the M23B/NlpC/P60 peptidase family. The overall architecture — an N-terminal signal peptide (hydrophobic stretch MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEG), a peptidase-like beta-sheet-rich domain with conserved 'GGDGSARE' glycine-rich loop, and the C-terminal His/Asp clusters — is consistent with a secreted/outer-membrane metalloprotease. Transferable knowledge of the M23B family (NlpC/P60 domain, found in many bacterial peptidoglycan hydrolases) establishes that these enzymes are zinc-dependent. The other options are readily excluded: pantetheine 4'-phosphate requires acyltransferase/ACP-binding architecture absent here; Mo-bis(molybdopterin) requires the highly conserved Mo-S cluster cysteine motifs of molybdoenzymes, which are absent; Na(+) is not a recognized enzymatic cofactor for peptidases. Thus the zinc-binding histidine/asp pattern and peptidase fold meaningfully distinguish option B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the H-H and H-D-H spacing patterns, the peptidase-like fold, and the M23B/NlpC/P60 family architecture can infer Zn(2+) from transferable knowledge of metalloprotease families. The distractors (pantetheine, molybdopterin, Na+) lack any supporting sequence features, making B the clearly best-supported choice among the four."
  },
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C7",
      "H6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q5F676) explicitly annotates this protein as a zinc metallopeptidase (M23B family) with Zn(2+) as cofactor. The COFACTOR comment states Zn(2+) with evidence ECO:0000250 (similarity-based from E0N688). However, the mutagenesis data (PubMed 22334697) experimentally confirmed the roles of His-295, Asp-299, His-373, and His-375 — a classic zinc-coordinating tetrad in metalloproteases — providing strong experimental support for zinc coordination. The protein is also assigned EC 3.4.24.- (metalloendopeptidase class) and named 'Zinc metallopeptidase'/'Zinc metalloprotease' in the entry."
  },
  "important_caveats": [
    "The direct cofactor annotation in UniProt uses ECO:0000250 (similarity-based inference from E0N688), not a direct experimental cofactor-binding assay. However, site-directed mutagenesis of the four zinc-coordinating residues (His-295, Asp-299, His-373, His-375) with loss of activity provides strong indirect experimental evidence for zinc dependence.",
    "The protein was first characterized in 2005 (oxidative stress response) and its peptidase activity and zinc dependence were experimentally demonstrated in 2012 (PubMed 22334697). The benchmark question was constructed from a dataset whose exact snapshot date is unknown, but the sequence has been unchanged since 2005.",
    "The cofactor annotation is transferred by similarity from E0N688 (a related M23B protein), which is a standard and well-accepted practice for conserved metal-binding sites in peptidase families."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The zinc-binding histidine patterns and peptidase fold uniquely support Zn(2+) among the four choices. No other option has any sequence-level support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q5F676) explicitly annotates this protein as a zinc metallopeptidase (M23B family) with Zn(2+) as cofactor. The COFACTOR comment states Zn(2+) with evidence ECO:0000250 (similarity-based from E0N688). However, the mutagenesis data (PubMed 22334697) experimentally confirmed the roles of His-295, Asp-299, His-373, and His-375 — a classic zinc-coordinating tetrad in metalloproteases — providing strong experimental support for zinc coordination. The protein is also assigned EC 3.4.24.- (metalloendopeptidase class) and named 'Zinc metallopeptidase'/'Zinc metalloprotease' in the entry.",
    "evidence_ids": ["C5", "C4", "C7", "H6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple histidine-rich clusters in patterns characteristic of zinc-binding sites in metalloproteases: 'HANGVETLYAH' and 'PHLHYEARING' provide the H...H spacing typical of zinc coordination in the M23B/NlpC/P60 peptidase family. The overall architecture — an N-terminal signal peptide (hydrophobic stretch MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEG), a peptidase-like beta-sheet-rich domain with conserved 'GGDGSARE' glycine-rich loop, and the C-terminal His/Asp clusters — is consistent with a secreted/outer-membrane metalloprotease. Transferable knowledge of the M23B family (NlpC/P60 domain, found in many bacterial peptidoglycan hydrolases) establishes that these enzymes are zinc-dependent. The other options are readily excluded: pantetheine 4'-phosphate requires acyltransferase/ACP-binding architecture absent here; Mo-bis(molybdopterin) requires the highly conserved Mo-S cluster cysteine motifs of molybdoenzymes, which are absent; Na(+) is not a recognized enzymatic cofactor for peptidases. Thus the zinc-binding histidine/asp pattern and peptidase fold meaningfully distinguish option B.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the H-H and H-D-H spacing patterns, the peptidase-like fold, and the M23B/NlpC/P60 family architecture can infer Zn(2+) from transferable knowledge of metalloprotease families. The distractors (pantetheine, molybdopterin, Na+) lack any supporting sequence features, making B the clearly best-supported choice among the four."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The zinc-binding histidine patterns and peptidase fold uniquely support Zn(2+) among the four choices. No other option has any sequence-level support."
  },
  "important_caveats": [
    "The direct cofactor annotation in UniProt uses ECO:0000250 (similarity-based inference from E0N688), not a direct experimental cofactor-binding assay. However, site-directed mutagenesis of the four zinc-coordinating residues (His-295, Asp-299, His-373, His-375) with loss of activity provides strong indirect experimental evidence for zinc dependence.",
    "The protein was first characterized in 2005 (oxidative stress response) and its peptidase activity and zinc dependence were experimentally demonstrated in 2012 (PubMed 22334697). The benchmark question was constructed from a dataset whose exact snapshot date is unknown, but the sequence has been unchanged since 2005.",
    "The cofactor annotation is transferred by similarity from E0N688 (a related M23B protein), which is a standard and well-accepted practice for conserved metal-binding sites in peptidase families."
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
  "requested_accession": "Q5F676",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "69e7a45357ac9f20734736f0f30bb74890972c0311fb90e7d268f0a51f998813",
  "benchmark_sequence_length": 430,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 90,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-03-15",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "current_source_sequence_sha256": "69e7a45357ac9f20734736f0f30bb74890972c0311fb90e7d268f0a51f998813",
  "current_source_sequence_length": 430,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 88,
  "selected_historical_version": {
    "accession": "Q5F676",
    "database": "Swiss-Prot",
    "entryVersion": 88,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MPG_NEIG1",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "selected_historical_source_sequence_sha256": "69e7a45357ac9f20734736f0f30bb74890972c0311fb90e7d268f0a51f998813",
  "selected_historical_source_sequence_length": 430,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 88,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q5F676\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":90,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-03-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAW90311.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000535\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Neisseriales\",\"Neisseriaceae\",\"Neisseria\"],\"scientificName\":\"Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090)\",\"taxonId\":242231}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23839218\",\"source\":\"PubMed\"}],\"value\":\"Metalloprotease NGO1686\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23839218\",\"source\":\"PubMed\"}],\"value\":\"Metalloprotease active against peptidoglycan\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Outer membrane protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"OMP\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22334697\",\"source\":\"PubMed\"}],\"value\":\"Virulence factor NG1686\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22334697\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23839218\",\"source\":\"PubMed\"}],\"value\":\"Zinc metallopeptidase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16194237\",\"source\":\"PubMed\"}],\"value\":\"Zinc metalloprotease\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc-dependent metallopeptidase\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22334697\",\"source\":\"PubMed\"}],\"value\":\"3.4.17.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22334697\",\"source\":\"PubMed\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DD-carboxypeptidase/endopeptidase Mpg\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E0N688\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E0N688\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 zinc ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Stohl E.A.\",\"Criss A.K.\",\"Seifert H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16194237\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1365-2958.2005.04839.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"16194237\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"532\",\"publicationDate\":\"2005\",\"title\":\"The transcriptome response of Neisseria gonorrhoeae to hydrogen peroxide reveals genes with previously uncharacterized roles in oxidative damage protection.\",\"volume\":\"58\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16194237\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Stohl E.A.\",\"Chan Y.A.\",\"Hackett K.T.\",\"Kohler P.L.\",\"Dillard J.P.\",\"Seifert H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22334697\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m111.338830\"}],\"citationType\":\"journal article\",\"firstPage\":\"11222\",\"id\":\"22334697\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"11233\",\"publicationDate\":\"2012\",\"title\":\"Neisseria gonorrhoeae virulence factor NG1686 is a bifunctional M23B family metallopeptidase that influences resistance to hydrogen peroxide and colony morphology.\",\"volume\":\"287\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22334697\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-295; ASP-299; HIS-373 AND HIS-375\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5F676.json",
  "source_sha256": "fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec",
  "retrieved_utc": "2026-11-02T04:31:11.230902+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Stohl E.A.\",\"Dale E.M.\",\"Criss A.K.\",\"Seifert H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23839218\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00399-13\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"23839218\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2013\",\"title\":\"Neisseria gonorrhoeae metalloprotease NGO1686 is required for full piliation, and piliation is required for resistance to H2O2- and neutrophil-mediated killing.\",\"volume\":\"4\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23839218\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 700825 / FA 1090\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "source_locator": "lines 1-23",
  "excerpt": "ID   MPG_NEIG1               Reviewed;         430 AA.\nAC   Q5F676;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-MAR-2005, sequence version 1.\nDT   28-JAN-2026, entry version 88.\nDE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};\nDE            EC=3.4.17.- {ECO:0000269|PubMed:22334697};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:22334697};\nDE   AltName: Full=Metalloprotease NGO1686 {ECO:0000303|PubMed:23839218};\nDE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000303|PubMed:23839218};\nDE   AltName: Full=Outer membrane protein {ECO:0000305};\nDE            Short=OMP {ECO:0000305};\nDE   AltName: Full=Virulence factor NG1686 {ECO:0000303|PubMed:22334697};\nDE   AltName: Full=Zinc metallopeptidase {ECO:0000303|PubMed:22334697, ECO:0000303|PubMed:23839218};\nDE   AltName: Full=Zinc metalloprotease {ECO:0000303|PubMed:16194237};\nDE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=mpg {ECO:0000303|PubMed:23839218};\nGN   OrderedLocusNames=NGO_1686 {ECO:0000312|EMBL:AAW90311.1};\nOS   Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;\nOC   Neisseriaceae; Neisseria.\nOX   NCBI_TaxID=242231 {ECO:0000312|EMBL:AAW90311.1, ECO:0000312|Proteomes:UP000000535};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 88,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "source_locator": "lines 6-17",
  "excerpt": "DE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};\nDE            EC=3.4.17.- {ECO:0000269|PubMed:22334697};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:22334697};\nDE   AltName: Full=Metalloprotease NGO1686 {ECO:0000303|PubMed:23839218};\nDE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000303|PubMed:23839218};\nDE   AltName: Full=Outer membrane protein {ECO:0000305};\nDE            Short=OMP {ECO:0000305};\nDE   AltName: Full=Virulence factor NG1686 {ECO:0000303|PubMed:22334697};\nDE   AltName: Full=Zinc metallopeptidase {ECO:0000303|PubMed:22334697, ECO:0000303|PubMed:23839218};\nDE   AltName: Full=Zinc metalloprotease {ECO:0000303|PubMed:16194237};\nDE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 88,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "source_locator": "lines 33-41",
  "excerpt": "RN   [2]\nRP   FUNCTION, INDUCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 700825 / FA 1090 {ECO:0000303|PubMed:16194237};\nRX   PubMed=16194237; DOI=10.1111/j.1365-2958.2005.04839.x;\nRA   Stohl E.A., Criss A.K., Seifert H.S.;\nRT   \"The transcriptome response of Neisseria gonorrhoeae to hydrogen peroxide\nRT   reveals genes with previously uncharacterized roles in oxidative damage\nRT   protection.\";\nRL   Mol. Microbiol. 58:520-532(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 88,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "source_locator": "lines 50-60",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, DISRUPTION PHENOTYPE,\nRP   AND MUTAGENESIS OF HIS-295; ASP-299; HIS-373 AND HIS-375.\nRC   STRAIN=ATCC 700825 / FA 1090 {ECO:0000303|PubMed:22334697};\nRX   PubMed=22334697; DOI=10.1074/jbc.m111.338830;\nRA   Stohl E.A., Chan Y.A., Hackett K.T., Kohler P.L., Dillard J.P.,\nRA   Seifert H.S.;\nRT   \"Neisseria gonorrhoeae virulence factor NG1686 is a bifunctional M23B\nRT   family metallopeptidase that influences resistance to hydrogen peroxide and\nRT   colony morphology.\";\nRL   J. Biol. Chem. 287:11222-11233(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 88,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "source_locator": "lines 61-69",
  "excerpt": "RN   [5]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 700825 / FA 1090 {ECO:0000303|PubMed:23839218};\nRX   PubMed=23839218; DOI=10.1128/mbio.00399-13;\nRA   Stohl E.A., Dale E.M., Criss A.K., Seifert H.S.;\nRT   \"Neisseria gonorrhoeae metalloprotease NGO1686 is required for full\nRT   piliation, and piliation is required for resistance to H2O2- and\nRT   neutrophil-mediated killing.\";\nRL   MBio 4:0-0(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 88,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88",
  "source_sha256": "1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15",
  "retrieved_utc": "2026-11-02T04:31:15.062188+00:00",
  "source_locator": "lines 96-99",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:E0N688};\nCC       Note=Binds 1 zinc ion per subunit. {ECO:0000250|UniProtKB:E0N688};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 88,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
