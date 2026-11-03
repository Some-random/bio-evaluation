# active_site_0091: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0091.txt)

**Task:** `active_site`  
**Author key, unchanged:** **C** — Position 122 (Nucleophile)

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
MVCFSSLFVAASAIAGVFASPVDHEQLAKRQSTPSSQGTHDGYFYSWWTDGGAAATYTNLAGGEYSVSWSNGGNLVGGKGWNPGSARTITYSGTYNPNGNSYLAVYGWTRNPQPWLTPLVVEYYVVENFGTYNPSSGATARGQVTHDGALYRLFESTRTNQPSIDGTATFQQYWAVRDVKRTGGTVNMATFFNAWTAAGMRLGTHNYQVVATEGYFSSGSARINVAGGGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL

[Multiple Choices]
A. Position 140 (Charge relay system)
B. Position 200 (Proton acceptor)
C. Position 122 (Nucleophile)
D. Position 381 (For beta-ketoacyl synthase activity)
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

> The exact sequence match has a UniProt active-site annotation identifying position 122 as the nucleophile, supporting choice C. This annotation is attributed to a PROSITE-ProRule computational rule, not presented here as direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a sufficiently specific general biological argument to assign the catalytic role to residue 122. Recognizing a likely enzyme family or its conserved catalytic-residue pattern would require family-specific knowledge.


**Missing item-specific fact**

> The family-specific assignment that residue 122 is the nucleophile, as recorded in the PROSITE-ProRule/UniProt annotation, is absent from the question input.


**Reason**

> The key is supported by an annotation for the matched sequence, but retrieving or applying that protein-family-specific residue assignment is needed to distinguish the choices; knowing the exact sequence or its database entry is not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports position 122 as the nucleophile; it does not support another listed choice as that residue.


### Important caveats

- The active-site assignment is computationally attributed to PROSITE-ProRule; the excerpts do not establish independent experimental validation.
- The exact source snapshot used by the question author is unknown, although the sequence matches both the historical and current records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific general biological argument to assign the catalytic role to residue 122. Recognizing a likely enzyme family or its conserved catalytic-residue pattern would require family-specific knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The family-specific assignment that residue 122 is the nucleophile, as recorded in the PROSITE-ProRule/UniProt annotation, is absent from the question input.",
    "reason": "The key is supported by an annotation for the matched sequence, but retrieving or applying that protein-family-specific residue assignment is needed to distinguish the choices; knowing the exact sequence or its database entry is not reasoning from the supplied information."
  },
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt active-site annotation identifying position 122 as the nucleophile, supporting choice C. This annotation is attributed to a PROSITE-ProRule computational rule, not presented here as direct experimental evidence."
  },
  "important_caveats": [
    "The active-site assignment is computationally attributed to PROSITE-ProRule; the excerpts do not establish independent experimental validation.",
    "The exact source snapshot used by the question author is unknown, although the sequence matches both the historical and current records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports position 122 as the nucleophile; it does not support another listed choice as that residue."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt active-site annotation identifying position 122 as the nucleophile, supporting choice C. This annotation is attributed to a PROSITE-ProRule computational rule, not presented here as direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific general biological argument to assign the catalytic role to residue 122. Recognizing a likely enzyme family or its conserved catalytic-residue pattern would require family-specific knowledge.",
    "missing_item_specific_fact": "The family-specific assignment that residue 122 is the nucleophile, as recorded in the PROSITE-ProRule/UniProt annotation, is absent from the question input.",
    "reason": "The key is supported by an annotation for the matched sequence, but retrieving or applying that protein-family-specific residue assignment is needed to distinguish the choices; knowing the exact sequence or its database entry is not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports position 122 as the nucleophile; it does not support another listed choice as that residue."
  },
  "important_caveats": [
    "The active-site assignment is computationally attributed to PROSITE-ProRule; the excerpts do not establish independent experimental validation.",
    "The exact source snapshot used by the question author is unknown, although the sequence matches both the historical and current records."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G2X8M4 (Ethylene-inducing xylanase 3, EC 3.2.1.8, GH11 family) annotates position 122 as 'Nucleophile' (Active site feature). The residue at position 122 in the supplied sequence is E (glutamic acid), consistent with a nucleophile in glycoside hydrolases. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU01097), indicating computational/profile-based annotation rather than direct experimental determination. The historical archived entry (version 61) confirms the same annotation. The sequence match is exact (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General enzymology knowledge allows partial elimination: (1) Option D is trivially impossible since the protein is only 294 AA; (2) Option A invokes a 'charge relay system,' a concept specific to serine proteases (Asp-His-Ser triad), not glycoside hydrolases; (3) Option B uses 'proton acceptor' terminology, whereas GH catalysis employs a proton donor (acid/base) and nucleophile. This narrows the field to C. However, confirming that position 122 specifically (rather than other Glu residues at positions 127, 155, etc.) is the nucleophile requires knowing the precise catalytic geometry of GH11 xylanases or looking up the PROSITE-ProRule annotation for this entry.


**Missing item-specific fact**

> The exact mapping of which glutamate residue in the sequence serves as the nucleophile versus other Glu residues requires either the PROSITE-ProRule profile match (PRU01097) for GH11 or structural knowledge of the specific catalytic geometry in this xylanase. The sequence alone contains multiple Glu residues, and their catalytic roles cannot be unambiguously assigned without the profile/structural annotation.


**Reason**

> While general enzymology (GH mechanism, elimination of serine-protease concepts, out-of-range position) provides partial discrimination, the precise positional assignment (122 vs. other Glu residues) depends on the PROSITE-ProRule annotation or equivalent item-specific structural knowledge not derivable from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are each independently eliminable: D exceeds the protein length (381 > 294); A invokes a mechanism (charge relay) not applicable to glycoside hydrolases; B uses incorrect terminology ('proton acceptor' rather than 'proton donor/acid-base') for GH catalysis. Only C uses correct mechanistic terminology (nucleophile) for a glycoside hydrolase and cites a position within the sequence. No other option is defensible.


### Important caveats

- The active-site annotation is based on PROSITE-ProRule (ECO:0000255), a computational profile-based prediction, not on site-directed mutagenesis or crystallographic evidence for this specific protein.
- The UniProt entry was first publicly released on 2025-06-18; the author's source snapshot is unknown but the sequence has been unchanged since 2011-11-16.
- The protein is flagged as a Precursor (signal peptide present), but the annotation numbering uses full precursor coordinates, which matches the supplied sequence.
- Position 213 is annotated as 'Proton donor' (not 'proton acceptor' as option B states), and is at a different position than option B's position 200.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General enzymology knowledge allows partial elimination: (1) Option D is trivially impossible since the protein is only 294 AA; (2) Option A invokes a 'charge relay system,' a concept specific to serine proteases (Asp-His-Ser triad), not glycoside hydrolases; (3) Option B uses 'proton acceptor' terminology, whereas GH catalysis employs a proton donor (acid/base) and nucleophile. This narrows the field to C. However, confirming that position 122 specifically (rather than other Glu residues at positions 127, 155, etc.) is the nucleophile requires knowing the precise catalytic geometry of GH11 xylanases or looking up the PROSITE-ProRule annotation for this entry.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact mapping of which glutamate residue in the sequence serves as the nucleophile versus other Glu residues requires either the PROSITE-ProRule profile match (PRU01097) for GH11 or structural knowledge of the specific catalytic geometry in this xylanase. The sequence alone contains multiple Glu residues, and their catalytic roles cannot be unambiguously assigned without the profile/structural annotation.",
    "reason": "While general enzymology (GH mechanism, elimination of serine-protease concepts, out-of-range position) provides partial discrimination, the precise positional assignment (122 vs. other Glu residues) depends on the PROSITE-ProRule annotation or equivalent item-specific structural knowledge not derivable from the sequence alone."
  },
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G2X8M4 (Ethylene-inducing xylanase 3, EC 3.2.1.8, GH11 family) annotates position 122 as 'Nucleophile' (Active site feature). The residue at position 122 in the supplied sequence is E (glutamic acid), consistent with a nucleophile in glycoside hydrolases. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU01097), indicating computational/profile-based annotation rather than direct experimental determination. The historical archived entry (version 61) confirms the same annotation. The sequence match is exact (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The active-site annotation is based on PROSITE-ProRule (ECO:0000255), a computational profile-based prediction, not on site-directed mutagenesis or crystallographic evidence for this specific protein.",
    "The UniProt entry was first publicly released on 2025-06-18; the author's source snapshot is unknown but the sequence has been unchanged since 2011-11-16.",
    "The protein is flagged as a Precursor (signal peptide present), but the annotation numbering uses full precursor coordinates, which matches the supplied sequence.",
    "Position 213 is annotated as 'Proton donor' (not 'proton acceptor' as option B states), and is at a different position than option B's position 200."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are each independently eliminable: D exceeds the protein length (381 > 294); A invokes a mechanism (charge relay) not applicable to glycoside hydrolases; B uses incorrect terminology ('proton acceptor' rather than 'proton donor/acid-base') for GH catalysis. Only C uses correct mechanistic terminology (nucleophile) for a glycoside hydrolase and cites a position within the sequence. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G2X8M4 (Ethylene-inducing xylanase 3, EC 3.2.1.8, GH11 family) annotates position 122 as 'Nucleophile' (Active site feature). The residue at position 122 in the supplied sequence is E (glutamic acid), consistent with a nucleophile in glycoside hydrolases. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU01097), indicating computational/profile-based annotation rather than direct experimental determination. The historical archived entry (version 61) confirms the same annotation. The sequence match is exact (SHA-256 confirmed).",
    "evidence_ids": ["C5", "H3", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General enzymology knowledge allows partial elimination: (1) Option D is trivially impossible since the protein is only 294 AA; (2) Option A invokes a 'charge relay system,' a concept specific to serine proteases (Asp-His-Ser triad), not glycoside hydrolases; (3) Option B uses 'proton acceptor' terminology, whereas GH catalysis employs a proton donor (acid/base) and nucleophile. This narrows the field to C. However, confirming that position 122 specifically (rather than other Glu residues at positions 127, 155, etc.) is the nucleophile requires knowing the precise catalytic geometry of GH11 xylanases or looking up the PROSITE-ProRule annotation for this entry.",
    "missing_item_specific_fact": "The exact mapping of which glutamate residue in the sequence serves as the nucleophile versus other Glu residues requires either the PROSITE-ProRule profile match (PRU01097) for GH11 or structural knowledge of the specific catalytic geometry in this xylanase. The sequence alone contains multiple Glu residues, and their catalytic roles cannot be unambiguously assigned without the profile/structural annotation.",
    "reason": "While general enzymology (GH mechanism, elimination of serine-protease concepts, out-of-range position) provides partial discrimination, the precise positional assignment (122 vs. other Glu residues) depends on the PROSITE-ProRule annotation or equivalent item-specific structural knowledge not derivable from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are each independently eliminable: D exceeds the protein length (381 > 294); A invokes a mechanism (charge relay) not applicable to glycoside hydrolases; B uses incorrect terminology ('proton acceptor' rather than 'proton donor/acid-base') for GH catalysis. Only C uses correct mechanistic terminology (nucleophile) for a glycoside hydrolase and cites a position within the sequence. No other option is defensible."
  },
  "important_caveats": [
    "The active-site annotation is based on PROSITE-ProRule (ECO:0000255), a computational profile-based prediction, not on site-directed mutagenesis or crystallographic evidence for this specific protein.",
    "The UniProt entry was first publicly released on 2025-06-18; the author's source snapshot is unknown but the sequence has been unchanged since 2011-11-16.",
    "The protein is flagged as a Precursor (signal peptide present), but the annotation numbering uses full precursor coordinates, which matches the supplied sequence.",
    "Position 213 is annotated as 'Proton donor' (not 'proton acceptor' as option B states), and is at a different position than option B's position 200."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches the source sequence, whose UniProt annotation identifies residue 122 as the nucleophile. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a secretory signal and features consistent with a fungal GH11 xylanase. GH11 xylanases use conserved catalytic glutamates, including a nucleophile; residue 122 is a glutamate in this sequence and is a credible match for that role. This favors C, while position 381 in D is beyond the 294-residue sequence and the other listed positions/roles do not fit the conserved catalytic-residue pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and conserved xylanase catalytic mechanism meaningfully distinguishes the offered choices; recalling this exact protein's database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, only C provides a plausible catalytic-residue assignment consistent with the sequence and family mechanism.


### Important caveats

- The source annotation is computationally inferred by PROSITE-ProRule; the excerpts do not establish experimental validation of residue 122.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a secretory signal and features consistent with a fungal GH11 xylanase. GH11 xylanases use conserved catalytic glutamates, including a nucleophile; residue 122 is a glutamate in this sequence and is a credible match for that role. This favors C, while position 381 in D is beyond the 294-residue sequence and the other listed positions/roles do not fit the conserved catalytic-residue pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and conserved xylanase catalytic mechanism meaningfully distinguishes the offered choices; recalling this exact protein's database record is not necessary."
  },
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence, whose UniProt annotation identifies residue 122 as the nucleophile. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The source annotation is computationally inferred by PROSITE-ProRule; the excerpts do not establish experimental validation of residue 122."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only C provides a plausible catalytic-residue assignment consistent with the sequence and family mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence, whose UniProt annotation identifies residue 122 as the nucleophile. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a secretory signal and features consistent with a fungal GH11 xylanase. GH11 xylanases use conserved catalytic glutamates, including a nucleophile; residue 122 is a glutamate in this sequence and is a credible match for that role. This favors C, while position 381 in D is beyond the 294-residue sequence and the other listed positions/roles do not fit the conserved catalytic-residue pattern.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and conserved xylanase catalytic mechanism meaningfully distinguishes the offered choices; recalling this exact protein's database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only C provides a plausible catalytic-residue assignment consistent with the sequence and family mechanism."
  },
  "important_caveats": [
    "The source annotation is computationally inferred by PROSITE-ProRule; the excerpts do not establish experimental validation of residue 122."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for G2X8M4 (EIX3, EC 3.2.1.8, endo-1,4-beta-xylanase) explicitly annotates position 122 as 'Nucleophile' active site with evidence code ECO:0000255|PROSITE-ProRule:PRU01097 (glycoside hydrolase family 11). The sequence at position 122 is Glu (E), consistent with the GH11 catalytic nucleophile. The annotation is computational (PROSITE-ProRule) rather than experimentally validated, but it is well-established for this enzyme family. The reviewer evidence (C5, H3) directly supports the author's key.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable inferences meaningfully distinguish C from the alternatives. (1) Option D (position 381) is eliminated immediately because the protein is only 294 residues long. (2) Option A ('Charge relay system') uses terminology specific to serine/cysteine proteases (Ser-His-Asp triad), not glycoside hydrolases, making it mechanistically inconsistent with the sequence's family. (3) The sequence contains hallmark GH11 xylanase features: ~294 aa length, the 'TITYSG' motif (~positions 95-100), multiple 'NP' patterns, and a beta-jelly-roll–compatible composition. Family-level knowledge of GH11 establishes that catalysis uses two Glu residues (nucleophile and proton donor) separated by ~90 residues. (4) The conserved GH11 nucleophile Glu appears in a 'VVE' context; positions 120-123 read 'VVEY', placing Glu at 122 in the canonical nucleophile slot. (5) Option B (position 200, 'Proton acceptor') is inconsistent: the GH11 proton donor is typically ~90 residues downstream of the nucleophile (position 213 in this family context), and the standard terminology is 'proton donor,' not 'proton acceptor.' Thus, family recognition plus mechanistic knowledge of GH11 catalysis distinguishes C from the other options without needing the exact database entry for this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing GH11 family features in the sequence can apply well-established family-level catalytic mechanism knowledge (two Glu nucleophile/proton donor, conserved 'VVE' nucleophile context, ~90-residue spacing) to identify position 122 as the nucleophile. The distractors are eliminated by sequence length (D), wrong mechanism terminology (A), and wrong position/terminology (B). This is a defensible transferable inference from other GH11 enzymes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is physically impossible (position 381 > 294 aa). Option A uses protease-specific terminology inapplicable to glycoside hydrolases. Option B has both a positional mismatch and non-standard terminology. Only C is consistent with GH11 family catalytic mechanism and the sequence context.


### Important caveats

- The UniProt annotation is computational (PROSITE-ProRule PRU01097), not experimentally determined by mutagenesis or crystallography for this specific protein.
- The PROSITE-ProRule assignment is a family-level transfer; it assumes the protein is a true GH11 member with the canonical catalytic Glu pair.
- The reviewer-only evidence (accession, organism, PROSITE rule) was not available to the evaluated model; the reasoning argument relies solely on sequence features and general GH11 family knowledge.
- The entry was only recently integrated into Swiss-Prot (first public date 2025-06-18), so it may not have been in training data at the time of benchmark construction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable inferences meaningfully distinguish C from the alternatives. (1) Option D (position 381) is eliminated immediately because the protein is only 294 residues long. (2) Option A ('Charge relay system') uses terminology specific to serine/cysteine proteases (Ser-His-Asp triad), not glycoside hydrolases, making it mechanistically inconsistent with the sequence's family. (3) The sequence contains hallmark GH11 xylanase features: ~294 aa length, the 'TITYSG' motif (~positions 95-100), multiple 'NP' patterns, and a beta-jelly-roll–compatible composition. Family-level knowledge of GH11 establishes that catalysis uses two Glu residues (nucleophile and proton donor) separated by ~90 residues. (4) The conserved GH11 nucleophile Glu appears in a 'VVE' context; positions 120-123 read 'VVEY', placing Glu at 122 in the canonical nucleophile slot. (5) Option B (position 200, 'Proton acceptor') is inconsistent: the GH11 proton donor is typically ~90 residues downstream of the nucleophile (position 213 in this family context), and the standard terminology is 'proton donor,' not 'proton acceptor.' Thus, family recognition plus mechanistic knowledge of GH11 catalysis distinguishes C from the other options without needing the exact database entry for this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing GH11 family features in the sequence can apply well-established family-level catalytic mechanism knowledge (two Glu nucleophile/proton donor, conserved 'VVE' nucleophile context, ~90-residue spacing) to identify position 122 as the nucleophile. The distractors are eliminated by sequence length (D), wrong mechanism terminology (A), and wrong position/terminology (B). This is a defensible transferable inference from other GH11 enzymes."
  },
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for G2X8M4 (EIX3, EC 3.2.1.8, endo-1,4-beta-xylanase) explicitly annotates position 122 as 'Nucleophile' active site with evidence code ECO:0000255|PROSITE-ProRule:PRU01097 (glycoside hydrolase family 11). The sequence at position 122 is Glu (E), consistent with the GH11 catalytic nucleophile. The annotation is computational (PROSITE-ProRule) rather than experimentally validated, but it is well-established for this enzyme family. The reviewer evidence (C5, H3) directly supports the author's key."
  },
  "important_caveats": [
    "The UniProt annotation is computational (PROSITE-ProRule PRU01097), not experimentally determined by mutagenesis or crystallography for this specific protein.",
    "The PROSITE-ProRule assignment is a family-level transfer; it assumes the protein is a true GH11 member with the canonical catalytic Glu pair.",
    "The reviewer-only evidence (accession, organism, PROSITE rule) was not available to the evaluated model; the reasoning argument relies solely on sequence features and general GH11 family knowledge.",
    "The entry was only recently integrated into Swiss-Prot (first public date 2025-06-18), so it may not have been in training data at the time of benchmark construction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is physically impossible (position 381 > 294 aa). Option A uses protease-specific terminology inapplicable to glycoside hydrolases. Option B has both a positional mismatch and non-standard terminology. Only C is consistent with GH11 family catalytic mechanism and the sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for G2X8M4 (EIX3, EC 3.2.1.8, endo-1,4-beta-xylanase) explicitly annotates position 122 as 'Nucleophile' active site with evidence code ECO:0000255|PROSITE-ProRule:PRU01097 (glycoside hydrolase family 11). The sequence at position 122 is Glu (E), consistent with the GH11 catalytic nucleophile. The annotation is computational (PROSITE-ProRule) rather than experimentally validated, but it is well-established for this enzyme family. The reviewer evidence (C5, H3) directly supports the author's key.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable inferences meaningfully distinguish C from the alternatives. (1) Option D (position 381) is eliminated immediately because the protein is only 294 residues long. (2) Option A ('Charge relay system') uses terminology specific to serine/cysteine proteases (Ser-His-Asp triad), not glycoside hydrolases, making it mechanistically inconsistent with the sequence's family. (3) The sequence contains hallmark GH11 xylanase features: ~294 aa length, the 'TITYSG' motif (~positions 95-100), multiple 'NP' patterns, and a beta-jelly-roll–compatible composition. Family-level knowledge of GH11 establishes that catalysis uses two Glu residues (nucleophile and proton donor) separated by ~90 residues. (4) The conserved GH11 nucleophile Glu appears in a 'VVE' context; positions 120-123 read 'VVEY', placing Glu at 122 in the canonical nucleophile slot. (5) Option B (position 200, 'Proton acceptor') is inconsistent: the GH11 proton donor is typically ~90 residues downstream of the nucleophile (position 213 in this family context), and the standard terminology is 'proton donor,' not 'proton acceptor.' Thus, family recognition plus mechanistic knowledge of GH11 catalysis distinguishes C from the other options without needing the exact database entry for this protein.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing GH11 family features in the sequence can apply well-established family-level catalytic mechanism knowledge (two Glu nucleophile/proton donor, conserved 'VVE' nucleophile context, ~90-residue spacing) to identify position 122 as the nucleophile. The distractors are eliminated by sequence length (D), wrong mechanism terminology (A), and wrong position/terminology (B). This is a defensible transferable inference from other GH11 enzymes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is physically impossible (position 381 > 294 aa). Option A uses protease-specific terminology inapplicable to glycoside hydrolases. Option B has both a positional mismatch and non-standard terminology. Only C is consistent with GH11 family catalytic mechanism and the sequence context."
  },
  "important_caveats": [
    "The UniProt annotation is computational (PROSITE-ProRule PRU01097), not experimentally determined by mutagenesis or crystallography for this specific protein.",
    "The PROSITE-ProRule assignment is a family-level transfer; it assumes the protein is a true GH11 member with the canonical catalytic Glu pair.",
    "The reviewer-only evidence (accession, organism, PROSITE rule) was not available to the evaluated model; the reasoning argument relies solely on sequence features and general GH11 family knowledge.",
    "The entry was only recently integrated into Swiss-Prot (first public date 2025-06-18), so it may not have been in training data at the time of benchmark construction."
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
  "requested_accession": "G2X8M4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "benchmark_sequence_length": 294,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 62,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "current_source_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "current_source_sequence_length": 294,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 61,
  "selected_historical_version": {
    "accession": "G2X8M4",
    "database": "Swiss-Prot",
    "entryVersion": 61,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX3_VERDV",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "selected_historical_source_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "selected_historical_source_sequence_length": 294,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 61,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"G2X8M4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":62,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX3\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":122},\"start\":{\"modifier\":\"EXACT\",\"value\":122}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":213},\"start\":{\"modifier\":\"EXACT\",\"value\":213}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   EIX3_VERDV              Reviewed;         294 AA.\nAC   G2X8M4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 61.\nDE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX3 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX3 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_06165;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 61,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "source_locator": "lines 30-36",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 61,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "source_locator": "lines 117-119",
  "excerpt": "FT   ACT_SITE        122\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 61,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "source_locator": "lines 120-122",
  "excerpt": "FT   ACT_SITE        213\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 61,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
