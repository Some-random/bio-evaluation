# active_site_0124: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0124.txt)

**Task:** `active_site`  
**Author key, unchanged:** **B** — Position 154 (Acyl-thioester intermediate)

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
MASYPKKKCGVLGATGSVGQRFILLLADHPFLELHAIGASNRSAGKKYKDAVRWKQTTAMSERLSNLVLRDCRADQFSDCDLVFSGLNSDVAGEIEMEFIKAEIPVFSNAKNYRKHPLVPLVVPTVNPQHLDLIPHQRKEFGLKKGFLVCNSNCAVIGVVIPFAALQAKFGPVEEVEVFTEQAVSGAGYPGVPSMDIMDNVIPYISGEEDKLENEAQKILGSLNADATAFDEQKGLTVGATCTRVGVTDGHMAFVSLRFKNRPGPSAEEVKQAMREYQSEAQKLGCPSAPREAIKVFDEPDRPQPRLDRDISKGYTVSVGRVREAAPGSYFDLRFAALSHNTVIGAAGSSILNAEVAVIKGYI

[Multiple Choices]
A. Position 124 (Proton donor)
B. Position 154 (Acyl-thioester intermediate)
C. Position 58 (Proton donor)
D. Position 207 (Proton donor)
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

> Choice B matches the UniProt active-site annotation at position 154, described as an acyl-thioester intermediate. The annotation applies to the exact sequence supplied, but its evidence is computationally assigned by PIRSR rather than direct experimental evidence for this residue.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a cysteine-rich region that may be consistent with a catalytic cysteine, but the input does not establish the protein’s identity, reaction mechanism, or which residue carries the acyl-thioester intermediate.


**Missing item-specific fact**

> The protein-specific assignment of position 154 as the acyl-thioester intermediate site, available here as a PIRSR-based active-site annotation.


**Reason**

> Selecting B requires an item-specific catalytic-site assignment not stated in the question. Recognizing or inferring the protein family from the sequence would not, by itself, supply that exact residue-role annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports position 154 and none of the other listed positions is supported by the supplied reviewer evidence.


### Important caveats

- The annotation is computationally assigned (ECO:0000255; PIRSR), not shown here to be experimentally validated.
- The exact sequence match is established by reviewer-only evidence; this identity and annotation were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine-rich region that may be consistent with a catalytic cysteine, but the input does not establish the protein’s identity, reaction mechanism, or which residue carries the acyl-thioester intermediate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of position 154 as the acyl-thioester intermediate site, available here as a PIRSR-based active-site annotation.",
    "reason": "Selecting B requires an item-specific catalytic-site assignment not stated in the question. Recognizing or inferring the protein family from the sequence would not, by itself, supply that exact residue-role annotation."
  },
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "Choice B matches the UniProt active-site annotation at position 154, described as an acyl-thioester intermediate. The annotation applies to the exact sequence supplied, but its evidence is computationally assigned by PIRSR rather than direct experimental evidence for this residue."
  },
  "important_caveats": [
    "The annotation is computationally assigned (ECO:0000255; PIRSR), not shown here to be experimentally validated.",
    "The exact sequence match is established by reviewer-only evidence; this identity and annotation were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports position 154 and none of the other listed positions is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice B matches the UniProt active-site annotation at position 154, described as an acyl-thioester intermediate. The annotation applies to the exact sequence supplied, but its evidence is computationally assigned by PIRSR rather than direct experimental evidence for this residue.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a cysteine-rich region that may be consistent with a catalytic cysteine, but the input does not establish the protein’s identity, reaction mechanism, or which residue carries the acyl-thioester intermediate.",
    "missing_item_specific_fact": "The protein-specific assignment of position 154 as the acyl-thioester intermediate site, available here as a PIRSR-based active-site annotation.",
    "reason": "Selecting B requires an item-specific catalytic-site assignment not stated in the question. Recognizing or inferring the protein family from the sequence would not, by itself, supply that exact residue-role annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports position 154 and none of the other listed positions is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The annotation is computationally assigned (ECO:0000255; PIRSR), not shown here to be experimentally validated.",
    "The exact sequence match is established by reviewer-only evidence; this identity and annotation were not provided to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WWR8 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Aspergillus fumigatus) explicitly annotates position 154 as 'Active site: Acyl-thioester intermediate' (evidence C5, H4). The sequence at position 154 is indeed Cysteine, consistent with the known ASADH catalytic mechanism. The annotation evidence code is ECO:0000255 (inferred by similarity, PIRSR000148-1), meaning it is a computational/curatorial inference from homology to characterized ASADH enzymes rather than direct experimental measurement on this specific protein, but it is consistent with well-established ASADH biochemistry and supported by X-ray crystallography (PDB 5JW6, evidence H3).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C1](#evidence-c1), [C4](#evidence-c4), [C17](#evidence-c17), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the Rossmann fold motif 'GATGSVG' (positions 12-18), identifying this as an NAD(P)-binding dehydrogenase. The well-known ASADH catalytic mechanism requires a catalytic Cysteine to form an acyl-thioester intermediate with the aspartyl-phosphate substrate. Among the four options, only position 154 is a Cysteine; position 124 is Proline, position 58 is Threonine, and position 207 is Glycine. None of Pro, Thr, or Gly can form a thioester bond (which requires a thiol group). The described chemical role 'Acyl-thioester intermediate' is chemically incompatible with Pro, Thr, or Gly, leaving only the Cys at 154 as the viable answer. Additionally, Pro and Gly lack the side-chain functionality needed for proton donation, further eliminating A, C, and D.


**Missing item-specific fact**

> Precise recognition that this is ASADH (rather than another NAD(P)-dependent dehydrogenase) requires either homology knowledge or database lookup, though the Rossmann fold and overall sequence composition provide partial clues. The exact catalytic Cys position among the multiple Cys residues (9, 72, 80, 150, 154, 242, 286) in the sequence is not trivially derivable from sequence alone without structural context.


**Reason**

> The amino acid chemistry provides a concrete discriminating argument: only a Cys thiol can form an acyl-thioester intermediate, and only option B places a Cys at the stated position. The other three options assign roles (proton donor) to residues (Pro, Thr, Gly) that are chemically implausible for that role in a dehydrogenase active site. This chemical reasoning, combined with recognition of the Rossmann fold as an NAD(P)-binding motif, provides meaningful grounds to select B without requiring memorization of the specific UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The chemical requirement of a Cys thiol for acyl-thioester formation uniquely selects position 154 among the four options. The other options assign chemically implausible roles to their respective residues (Pro as proton donor, Thr as proton donor in this context, Gly as proton donor). No ambiguity in defensible answers.


### Important caveats

- The UniProt active-site annotation (position 154) is based on ECO:0000255 (inferred by similarity via PIRSR000148-1), not direct experimental mutagenesis on this specific A. fumigatus enzyme. However, the ASADH catalytic mechanism (catalytic Cys forming acyl-thioester) is well-established across the enzyme family.
- The sequence contains multiple Cysteines (positions 9, 72, 80, 150, 154, 242, 286); identifying position 154 specifically as THE catalytic Cys among these requires structural or homology knowledge beyond simple amino-acid chemistry.
- The question does not name the enzyme; identification as ASADH relies on recognizing the Rossmann fold and sequence context, which is partially but not fully derivable from the provided sequence alone.
- The reviewer evidence is from UniProt entry Q4WWR8 (entry version 118-120), which post-dates the likely author construction date; the annotation may have been added after the benchmark was created.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the Rossmann fold motif 'GATGSVG' (positions 12-18), identifying this as an NAD(P)-binding dehydrogenase. The well-known ASADH catalytic mechanism requires a catalytic Cysteine to form an acyl-thioester intermediate with the aspartyl-phosphate substrate. Among the four options, only position 154 is a Cysteine; position 124 is Proline, position 58 is Threonine, and position 207 is Glycine. None of Pro, Thr, or Gly can form a thioester bond (which requires a thiol group). The described chemical role 'Acyl-thioester intermediate' is chemically incompatible with Pro, Thr, or Gly, leaving only the Cys at 154 as the viable answer. Additionally, Pro and Gly lack the side-chain functionality needed for proton donation, further eliminating A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition that this is ASADH (rather than another NAD(P)-dependent dehydrogenase) requires either homology knowledge or database lookup, though the Rossmann fold and overall sequence composition provide partial clues. The exact catalytic Cys position among the multiple Cys residues (9, 72, 80, 150, 154, 242, 286) in the sequence is not trivially derivable from sequence alone without structural context.",
    "reason": "The amino acid chemistry provides a concrete discriminating argument: only a Cys thiol can form an acyl-thioester intermediate, and only option B places a Cys at the stated position. The other three options assign roles (proton donor) to residues (Pro, Thr, Gly) that are chemically implausible for that role in a dehydrogenase active site. This chemical reasoning, combined with recognition of the Rossmann fold as an NAD(P)-binding motif, provides meaningful grounds to select B without requiring memorization of the specific UniProt annotation."
  },
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C1",
      "C4",
      "C17",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WWR8 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Aspergillus fumigatus) explicitly annotates position 154 as 'Active site: Acyl-thioester intermediate' (evidence C5, H4). The sequence at position 154 is indeed Cysteine, consistent with the known ASADH catalytic mechanism. The annotation evidence code is ECO:0000255 (inferred by similarity, PIRSR000148-1), meaning it is a computational/curatorial inference from homology to characterized ASADH enzymes rather than direct experimental measurement on this specific protein, but it is consistent with well-established ASADH biochemistry and supported by X-ray crystallography (PDB 5JW6, evidence H3)."
  },
  "important_caveats": [
    "The UniProt active-site annotation (position 154) is based on ECO:0000255 (inferred by similarity via PIRSR000148-1), not direct experimental mutagenesis on this specific A. fumigatus enzyme. However, the ASADH catalytic mechanism (catalytic Cys forming acyl-thioester) is well-established across the enzyme family.",
    "The sequence contains multiple Cysteines (positions 9, 72, 80, 150, 154, 242, 286); identifying position 154 specifically as THE catalytic Cys among these requires structural or homology knowledge beyond simple amino-acid chemistry.",
    "The question does not name the enzyme; identification as ASADH relies on recognizing the Rossmann fold and sequence context, which is partially but not fully derivable from the provided sequence alone.",
    "The reviewer evidence is from UniProt entry Q4WWR8 (entry version 118-120), which post-dates the likely author construction date; the annotation may have been added after the benchmark was created."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The chemical requirement of a Cys thiol for acyl-thioester formation uniquely selects position 154 among the four options. The other options assign chemically implausible roles to their respective residues (Pro as proton donor, Thr as proton donor in this context, Gly as proton donor). No ambiguity in defensible answers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WWR8 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Aspergillus fumigatus) explicitly annotates position 154 as 'Active site: Acyl-thioester intermediate' (evidence C5, H4). The sequence at position 154 is indeed Cysteine, consistent with the known ASADH catalytic mechanism. The annotation evidence code is ECO:0000255 (inferred by similarity, PIRSR000148-1), meaning it is a computational/curatorial inference from homology to characterized ASADH enzymes rather than direct experimental measurement on this specific protein, but it is consistent with well-established ASADH biochemistry and supported by X-ray crystallography (PDB 5JW6, evidence H3).",
    "evidence_ids": ["C5", "H4", "C1", "C4", "C17", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the Rossmann fold motif 'GATGSVG' (positions 12-18), identifying this as an NAD(P)-binding dehydrogenase. The well-known ASADH catalytic mechanism requires a catalytic Cysteine to form an acyl-thioester intermediate with the aspartyl-phosphate substrate. Among the four options, only position 154 is a Cysteine; position 124 is Proline, position 58 is Threonine, and position 207 is Glycine. None of Pro, Thr, or Gly can form a thioester bond (which requires a thiol group). The described chemical role 'Acyl-thioester intermediate' is chemically incompatible with Pro, Thr, or Gly, leaving only the Cys at 154 as the viable answer. Additionally, Pro and Gly lack the side-chain functionality needed for proton donation, further eliminating A, C, and D.",
    "missing_item_specific_fact": "Precise recognition that this is ASADH (rather than another NAD(P)-dependent dehydrogenase) requires either homology knowledge or database lookup, though the Rossmann fold and overall sequence composition provide partial clues. The exact catalytic Cys position among the multiple Cys residues (9, 72, 80, 150, 154, 242, 286) in the sequence is not trivially derivable from sequence alone without structural context.",
    "reason": "The amino acid chemistry provides a concrete discriminating argument: only a Cys thiol can form an acyl-thioester intermediate, and only option B places a Cys at the stated position. The other three options assign roles (proton donor) to residues (Pro, Thr, Gly) that are chemically implausible for that role in a dehydrogenase active site. This chemical reasoning, combined with recognition of the Rossmann fold as an NAD(P)-binding motif, provides meaningful grounds to select B without requiring memorization of the specific UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The chemical requirement of a Cys thiol for acyl-thioester formation uniquely selects position 154 among the four options. The other options assign chemically implausible roles to their respective residues (Pro as proton donor, Thr as proton donor in this context, Gly as proton donor). No ambiguity in defensible answers."
  },
  "important_caveats": [
    "The UniProt active-site annotation (position 154) is based on ECO:0000255 (inferred by similarity via PIRSR000148-1), not direct experimental mutagenesis on this specific A. fumigatus enzyme. However, the ASADH catalytic mechanism (catalytic Cys forming acyl-thioester) is well-established across the enzyme family.",
    "The sequence contains multiple Cysteines (positions 9, 72, 80, 150, 154, 242, 286); identifying position 154 specifically as THE catalytic Cys among these requires structural or homology knowledge beyond simple amino-acid chemistry.",
    "The question does not name the enzyme; identification as ASADH relies on recognizing the Rossmann fold and sequence context, which is partially but not fully derivable from the provided sequence alone.",
    "The reviewer evidence is from UniProt entry Q4WWR8 (entry version 118-120), which post-dates the likely author construction date; the annotation may have been added after the benchmark was created."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation assigns position 154 the role “Acyl-thioester intermediate,” matching choice B. This is a computational PIRSR annotation, not direct residue-specific experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cysteine at position 154 in a cysteine-containing motif. Transferable knowledge of aspartate-semialdehyde dehydrogenase and related enzyme chemistry supports a catalytic cysteine forming a thioester intermediate. That distinguishes B from the alternatives, which describe other positions as proton donors.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence and mechanism inference provides a meaningful basis for choosing B; recalling this exact protein’s database annotation is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, only B pairs the catalytic cysteine position with the thioester-intermediate role supported by the family-level inference.


### Important caveats

- The reviewer-only annotation supports the key but is computationally inferred; the excerpts do not provide direct experimental confirmation of the residue’s role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine at position 154 in a cysteine-containing motif. Transferable knowledge of aspartate-semialdehyde dehydrogenase and related enzyme chemistry supports a catalytic cysteine forming a thioester intermediate. That distinguishes B from the alternatives, which describe other positions as proton donors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and mechanism inference provides a meaningful basis for choosing B; recalling this exact protein’s database annotation is not necessary."
  },
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the role “Acyl-thioester intermediate,” matching choice B. This is a computational PIRSR annotation, not direct residue-specific experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but is computationally inferred; the excerpts do not provide direct experimental confirmation of the residue’s role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only B pairs the catalytic cysteine position with the thioester-intermediate role supported by the family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the role “Acyl-thioester intermediate,” matching choice B. This is a computational PIRSR annotation, not direct residue-specific experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cysteine at position 154 in a cysteine-containing motif. Transferable knowledge of aspartate-semialdehyde dehydrogenase and related enzyme chemistry supports a catalytic cysteine forming a thioester intermediate. That distinguishes B from the alternatives, which describe other positions as proton donors.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and mechanism inference provides a meaningful basis for choosing B; recalling this exact protein’s database annotation is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only B pairs the catalytic cysteine position with the thioester-intermediate role supported by the family-level inference."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but is computationally inferred; the excerpts do not provide direct experimental confirmation of the residue’s role."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WWR8 annotates position 154 as 'Acyl-thioester intermediate' active site (evidence: PIRSR000148-1, ECO:0000255). The residue at position 154 in the supplied sequence is C (Cysteine), which is biochemically consistent with forming a thioester intermediate. The protein is annotated as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism across many characterized homologs (E. coli, C. glutamicum, etc.) involves a conserved catalytic Cys attacking the hemithioacetal to form a thioester. A PDB structure (5JW6, 2.39 Å) provides structural context. The annotation is computational/curated (PIRSR) rather than directly experimental for this specific protein, but it is consistent with well-established family mechanism and structural data.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C17](#evidence-c17), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The question can be answered through fundamental enzyme mechanism knowledge and sequence analysis. (1) The sequence contains 'GATGSVG' at positions 13-19, a canonical Rossmann-fold NAD(P)-binding motif, identifying this as an NAD(P)-dependent dehydrogenase. (2) The phrase 'acyl-thioester intermediate' in option B uniquely requires a cysteine nucleophile (sulfur attacks a carbonyl to form R-S-C(=O)-R'), which is textbook biochemistry. (3) Reading the sequence at the four candidate positions: position 124 is Pro (P), position 154 is Cys (C), position 58 is Thr (T), position 207 is Gly (G). Only Cys can form a thioester. (4) The 'proton donor' role in options A, C, D is typically fulfilled by His, Asp, Glu, or Tyr—Pro, Gly, and (rarely) Thr are implausible as catalytic proton donors in dehydrogenase active sites. (5) The sequence context around position 154 ('GFLVCNSNCAVIGVVIPFAALQAKFGP') matches the conserved ASADH catalytic-domain signature seen in homologs. Thus, a model using family-level knowledge of ASADH and general mechanistic biochemistry can eliminate A, C, D and select B without memorizing this specific entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The discriminating logic relies on: (a) recognizing the Rossmann fold to classify the enzyme, (b) the universal biochemical requirement that thioester intermediates require a Cys thiol, and (c) reading amino acid identities from the sequence to eliminate non-Cys options. All are transferable knowledge from enzyme mechanism and protein-family recognition, not lookup of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 154 corresponds to a Cys residue, and only a Cys can form an acyl-thioester intermediate. The other three positions (Pro, Thr, Gly) are biochemically implausible as proton donors in a dehydrogenase active site. No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation for position 154 uses evidence code ECO:0000255 (PIRSR), which is computational/curated rather than direct experimental measurement on this exact protein. However, the mechanism is well-established across the ASADH family and supported by the 5JW6 crystal structure.
- The position numbering in the question matches the canonical UniProt coordinates (363-residue full-length sequence), confirmed by sequence match.
- The PDB structure 5JW6 (2.39 Å) provides structural evidence for this fungal ASADH but was not independently validated in this audit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The question can be answered through fundamental enzyme mechanism knowledge and sequence analysis. (1) The sequence contains 'GATGSVG' at positions 13-19, a canonical Rossmann-fold NAD(P)-binding motif, identifying this as an NAD(P)-dependent dehydrogenase. (2) The phrase 'acyl-thioester intermediate' in option B uniquely requires a cysteine nucleophile (sulfur attacks a carbonyl to form R-S-C(=O)-R'), which is textbook biochemistry. (3) Reading the sequence at the four candidate positions: position 124 is Pro (P), position 154 is Cys (C), position 58 is Thr (T), position 207 is Gly (G). Only Cys can form a thioester. (4) The 'proton donor' role in options A, C, D is typically fulfilled by His, Asp, Glu, or Tyr—Pro, Gly, and (rarely) Thr are implausible as catalytic proton donors in dehydrogenase active sites. (5) The sequence context around position 154 ('GFLVCNSNCAVIGVVIPFAALQAKFGP') matches the conserved ASADH catalytic-domain signature seen in homologs. Thus, a model using family-level knowledge of ASADH and general mechanistic biochemistry can eliminate A, C, D and select B without memorizing this specific entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The discriminating logic relies on: (a) recognizing the Rossmann fold to classify the enzyme, (b) the universal biochemical requirement that thioester intermediates require a Cys thiol, and (c) reading amino acid identities from the sequence to eliminate non-Cys options. All are transferable knowledge from enzyme mechanism and protein-family recognition, not lookup of this specific entry's annotation."
  },
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C17",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WWR8 annotates position 154 as 'Acyl-thioester intermediate' active site (evidence: PIRSR000148-1, ECO:0000255). The residue at position 154 in the supplied sequence is C (Cysteine), which is biochemically consistent with forming a thioester intermediate. The protein is annotated as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism across many characterized homologs (E. coli, C. glutamicum, etc.) involves a conserved catalytic Cys attacking the hemithioacetal to form a thioester. A PDB structure (5JW6, 2.39 Å) provides structural context. The annotation is computational/curated (PIRSR) rather than directly experimental for this specific protein, but it is consistent with well-established family mechanism and structural data."
  },
  "important_caveats": [
    "The UniProt annotation for position 154 uses evidence code ECO:0000255 (PIRSR), which is computational/curated rather than direct experimental measurement on this exact protein. However, the mechanism is well-established across the ASADH family and supported by the 5JW6 crystal structure.",
    "The position numbering in the question matches the canonical UniProt coordinates (363-residue full-length sequence), confirmed by sequence match.",
    "The PDB structure 5JW6 (2.39 Å) provides structural evidence for this fungal ASADH but was not independently validated in this audit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 154 corresponds to a Cys residue, and only a Cys can form an acyl-thioester intermediate. The other three positions (Pro, Thr, Gly) are biochemically implausible as proton donors in a dehydrogenase active site. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WWR8 annotates position 154 as 'Acyl-thioester intermediate' active site (evidence: PIRSR000148-1, ECO:0000255). The residue at position 154 in the supplied sequence is C (Cysteine), which is biochemically consistent with forming a thioester intermediate. The protein is annotated as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), whose catalytic mechanism across many characterized homologs (E. coli, C. glutamicum, etc.) involves a conserved catalytic Cys attacking the hemithioacetal to form a thioester. A PDB structure (5JW6, 2.39 Å) provides structural context. The annotation is computational/curated (PIRSR) rather than directly experimental for this specific protein, but it is consistent with well-established family mechanism and structural data.",
    "evidence_ids": ["C5", "H4", "C17", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The question can be answered through fundamental enzyme mechanism knowledge and sequence analysis. (1) The sequence contains 'GATGSVG' at positions 13-19, a canonical Rossmann-fold NAD(P)-binding motif, identifying this as an NAD(P)-dependent dehydrogenase. (2) The phrase 'acyl-thioester intermediate' in option B uniquely requires a cysteine nucleophile (sulfur attacks a carbonyl to form R-S-C(=O)-R'), which is textbook biochemistry. (3) Reading the sequence at the four candidate positions: position 124 is Pro (P), position 154 is Cys (C), position 58 is Thr (T), position 207 is Gly (G). Only Cys can form a thioester. (4) The 'proton donor' role in options A, C, D is typically fulfilled by His, Asp, Glu, or Tyr—Pro, Gly, and (rarely) Thr are implausible as catalytic proton donors in dehydrogenase active sites. (5) The sequence context around position 154 ('GFLVCNSNCAVIGVVIPFAALQAKFGP') matches the conserved ASADH catalytic-domain signature seen in homologs. Thus, a model using family-level knowledge of ASADH and general mechanistic biochemistry can eliminate A, C, D and select B without memorizing this specific entry.",
    "missing_item_specific_fact": "",
    "reason": "The discriminating logic relies on: (a) recognizing the Rossmann fold to classify the enzyme, (b) the universal biochemical requirement that thioester intermediates require a Cys thiol, and (c) reading amino acid identities from the sequence to eliminate non-Cys options. All are transferable knowledge from enzyme mechanism and protein-family recognition, not lookup of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 154 corresponds to a Cys residue, and only a Cys can form an acyl-thioester intermediate. The other three positions (Pro, Thr, Gly) are biochemically implausible as proton donors in a dehydrogenase active site. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for position 154 uses evidence code ECO:0000255 (PIRSR), which is computational/curated rather than direct experimental measurement on this exact protein. However, the mechanism is well-established across the ASADH family and supported by the 5JW6 crystal structure.",
    "The position numbering in the question matches the canonical UniProt coordinates (363-residue full-length sequence), confirmed by sequence match.",
    "The PDB structure 5JW6 (2.39 Å) provides structural evidence for this fungal ASADH but was not independently validated in this audit."
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
  "requested_accession": "Q4WWR8",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "benchmark_sequence_length": 363,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "current_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "current_source_sequence_length": 363,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 118,
  "selected_historical_version": {
    "accession": "Q4WWR8",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_ASPFU",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "selected_historical_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "selected_historical_source_sequence_length": 363,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 118,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q4WWR8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002530\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28045392\",\"source\":\"PubMed\"}],\"value\":\"AfASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Acyl-thioester intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":154},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":15},\"start\":{\"modifier\":\"EXACT\",\"value\":15}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":16},\"start\":{\"modifier\":\"EXACT\",\"value\":16}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":17},\"start\":{\"modifier\":\"EXACT\",\"value\":17}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A179UL48\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":18},\"start\":{\"modifier\":\"EXACT\",\"value\":18}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":40},\"start\":{\"modifier\":\"EXACT\",\"value\":40}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":43},\"start\":{\"modifier\":\"EXACT\",\"value\":43}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":87},\"start\":{\"modifier\":\"EXACT\",\"value\":87}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A179UL48\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":341},\"start\":{\"modifier\":\"EXACT\",\"value\":341}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28045392\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2053230x16020070\"}],\"citationType\":\"journal article\",\"firstPage\":\"36\",\"id\":\"28045392\",\"journal\":\"Acta Crystallogr. F\",\"lastPage\":\"44\",\"publicationDate\":\"2017\",\"title\":\"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from Aspergillus fumigatus.\",\"volume\":\"73\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5JW6\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   DHAS_ASPFU              Reviewed;         363 AA.\nAC   Q4WWR8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\nDE   AltName: Full=AfASADH {ECO:0000303|PubMed:28045392};\nGN   Name=hom2 {ECO:0000305};\nGN   ORFNames=AFUA_3G06830 {ECO:0000312|EMBL:EAL92885.1};\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879 {ECO:0000312|Proteomes:UP000002530};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 50-56",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 57-64",
  "excerpt": "RN   [4] {ECO:0007744|PDB:5JW6}\nRP   X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=28045392; DOI=10.1107/s2053230x16020070;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from\nRT   Aspergillus fumigatus.\";\nRL   Acta Crystallogr. F 73:36-44(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 165-167",
  "excerpt": "FT   ACT_SITE        154\nFT                   /note=\"Acyl-thioester intermediate\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 168-170",
  "excerpt": "FT   ACT_SITE        251\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 171-174",
  "excerpt": "FT   BINDING         15\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 175-178",
  "excerpt": "FT   BINDING         16\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 179-182",
  "excerpt": "FT   BINDING         17\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 183-186",
  "excerpt": "FT   BINDING         18\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A179UL48\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 187-190",
  "excerpt": "FT   BINDING         40\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 191-194",
  "excerpt": "FT   BINDING         43\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 195-198",
  "excerpt": "FT   BINDING         87\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 199-202",
  "excerpt": "FT   BINDING         186\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "source_locator": "lines 203-206",
  "excerpt": "FT   BINDING         341\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A179UL48\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
