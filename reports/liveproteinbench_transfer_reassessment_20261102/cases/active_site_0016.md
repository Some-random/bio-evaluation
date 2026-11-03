# active_site_0016: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0016.txt)

**Task:** `active_site`  
**Author key, unchanged:** **B** — Position 159 (Proton donor)

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
MPISIPKGEKLMDLLSMKGKVTIVTGASGPRGMGIEAARGIAEMGGNVALTYAGRKEGGEKNAAALEKEYGIKAKAYKLDVANYESCCQLVKDVIADFGQIDAFVANAGKTADSGVLDGEISAFEEVIQTDLLGVAYCAKAVGHHFKERQTGSFVITASMSGHIANFPQEQTSYNVAKAGCIHMARSLANEWRDFARVNSISPGYIDTGLSDFVDKETQKLWHSMIPMGRDGDAKELKAAYVYFCSDASTYTTGSDLVIDGGYCAR

[Multiple Choices]
A. Position 64 (Nucleophile (Probable))
B. Position 159 (Proton donor)
C. Position 153 (catalytic acid/base residue)
D. Position 342 (Charge relay system)
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

> For the exact supplied sequence, UniProt annotates position 159 as the proton donor. This supports choice B, but the annotation is transferred by similarity from UniProtKB:P0C0Y5 (ECO:0000250), not established here as a direct experiment on this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a 266-residue enzyme, so position 342 is out of range; however, general sequence reasoning does not identify position 159 as its proton donor or distinguish it reliably from the other in-range residue claims.


**Missing item-specific fact**

> The protein-specific active-site annotation assigning the proton-donor role to residue 159, or equivalent validated homolog or structural evidence.


**Reason**

> The key is supported by reviewer-only annotation, but that annotation and the protein identity are absent from the evaluated input. Exact residue-role assignment therefore depends on an item-specific external fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B; it does not support the different residue-role claims in A or C, and D names a position beyond the sequence length.


### Important caveats

- The sequence matches the 266-residue UniProt entry, but the actual source snapshot used by the author is unknown.
- The position-159 annotation is similarity-based, transferred from P0C0Y5; it should not be represented as direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a 266-residue enzyme, so position 342 is out of range; however, general sequence reasoning does not identify position 159 as its proton donor or distinguish it reliably from the other in-range residue claims.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning the proton-donor role to residue 159, or equivalent validated homolog or structural evidence.",
    "reason": "The key is supported by reviewer-only annotation, but that annotation and the protein identity are absent from the evaluated input. Exact residue-role assignment therefore depends on an item-specific external fact."
  },
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "For the exact supplied sequence, UniProt annotates position 159 as the proton donor. This supports choice B, but the annotation is transferred by similarity from UniProtKB:P0C0Y5 (ECO:0000250), not established here as a direct experiment on this protein."
  },
  "important_caveats": [
    "The sequence matches the 266-residue UniProt entry, but the actual source snapshot used by the author is unknown.",
    "The position-159 annotation is similarity-based, transferred from P0C0Y5; it should not be represented as direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; it does not support the different residue-role claims in A or C, and D names a position beyond the sequence length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "For the exact supplied sequence, UniProt annotates position 159 as the proton donor. This supports choice B, but the annotation is transferred by similarity from UniProtKB:P0C0Y5 (ECO:0000250), not established here as a direct experiment on this protein.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a 266-residue enzyme, so position 342 is out of range; however, general sequence reasoning does not identify position 159 as its proton donor or distinguish it reliably from the other in-range residue claims.",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning the proton-donor role to residue 159, or equivalent validated homolog or structural evidence.",
    "reason": "The key is supported by reviewer-only annotation, but that annotation and the protein identity are absent from the evaluated input. Exact residue-role assignment therefore depends on an item-specific external fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; it does not support the different residue-role claims in A or C, and D names a position beyond the sequence length."
  },
  "important_caveats": [
    "The sequence matches the 266-residue UniProt entry, but the actual source snapshot used by the author is unknown.",
    "The position-159 annotation is similarity-based, transferred from P0C0Y5; it should not be represented as direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A223HDI5 (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) annotates position 159 as 'Proton donor' (Active site), matching choice B exactly. The sequence in the question matches the entry (266 aa, SHA-256 match). However, the evidence code is ECO:0000250 (inferred by similarity to P0C0Y5), making this a computational/transfer annotation rather than direct experimental evidence for this specific protein. The annotation is nonetheless the authoritative database claim and is consistent with the SDR-family catalytic mechanism (Ser as proton donor in the Ser-Tyr-Lys catalytic triad).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several reasoning steps distinguish B from the distractors using general biochemistry: (1) The N-terminal region contains a Rossmann-fold-like NAD(P)-binding motif (GASGPR at ~26-31), identifying this as an NAD(P)-dependent dehydrogenase. (2) The YxxxK motif at positions 174-178 (Y-N-V-A-K) is the hallmark SDR (short-chain dehydrogenase/reductase) catalytic Tyr-Lys dyad. (3) In the SDR catalytic mechanism, the catalytic Ser acts specifically as a proton donor (donating H+ to the substrate carbonyl oxygen), the Tyr as proton acceptor, and the Lys lowers the Tyr pKa. The functional label 'Proton donor' in choice B matches this mechanism precisely. (4) Choice D (position 342) is impossible in a 266-residue protein. (5) Choice A (position 64, Alanine) cannot serve as a nucleophile. (6) Choice C labels Ser153 as 'catalytic acid/base residue,' which is not the standard SDR terminology for the catalytic Ser (it is specifically a proton donor, not a general acid/base). The Ser at 159 is ~15 residues upstream of the catalytic Tyr(174), consistent with typical SDR catalytic-tetrad spacing, while Ser(153) is ~21 residues upstream.


**Missing item-specific fact**

> Distinguishing Ser159 from Ser153 as the catalytic proton donor relies on the specific spacing (~15 residues) between the catalytic Ser and the YxxxK dyad in SDR enzymes, which is a family-specific structural detail. A model without SDR-family knowledge would struggle to choose between the two Ser residues purely from the sequence.


**Reason**

> The SDR catalytic mechanism (Ser = proton donor, Tyr = proton acceptor, Lys = pKa modulator), the identifiable YxxxK motif, and the functional labels in the choices provide a concrete biological argument for B over the other options. The elimination of D (impossible position) and A (Ala cannot be nucleophile) is straightforward. The B-vs-C distinction is supported by the correct SDR functional terminology ('Proton donor' vs. non-standard 'acid/base'). The residual difficulty in pinpointing Ser159 over Ser153 is a matter of SDR-specific structural spacing, which is specialized but defensible general biochemistry knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, C, and D are clearly eliminable: A assigns nucleophile function to Alanine (position 64), C uses non-standard terminology ('acid/base') for a Ser that in SDR enzymes is specifically a proton donor, and D references position 342 in a 266-residue protein. Only B corresponds to an annotated active-site residue with a mechanistically accurate functional label. While positions 174 (Proton acceptor) and 178 (Lowers pKa of Tyr) are also active-site residues, they do not appear among the choices, so there is no competing correct option.


### Important caveats

- The UniProt annotation for position 159 uses evidence code ECO:0000250 (inferred by similarity to P0C0Y5), meaning it is a computational transfer annotation, not direct experimental evidence (e.g., site-directed mutagenesis or crystallography) for this specific Aureobasidium enzyme.
- The protein is 266 residues long; choice D (position 342) is trivially impossible, making it an unusually easy distractor.
- The question stem asks to identify 'the enzyme's catalytic center' (singular), but the SDR catalytic center comprises multiple residues (Ser159, Tyr174, Lys178). Only Ser159 appears among the choices, so the question is effectively asking which single annotated active-site residue is correctly described.
- The entry was first public on 2025-02-05 with annotation updates through 2026-01-28; the author's source snapshot date is unknown, but the sequence has been stable since 2017-10-25 (sequence version 1).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several reasoning steps distinguish B from the distractors using general biochemistry: (1) The N-terminal region contains a Rossmann-fold-like NAD(P)-binding motif (GASGPR at ~26-31), identifying this as an NAD(P)-dependent dehydrogenase. (2) The YxxxK motif at positions 174-178 (Y-N-V-A-K) is the hallmark SDR (short-chain dehydrogenase/reductase) catalytic Tyr-Lys dyad. (3) In the SDR catalytic mechanism, the catalytic Ser acts specifically as a proton donor (donating H+ to the substrate carbonyl oxygen), the Tyr as proton acceptor, and the Lys lowers the Tyr pKa. The functional label 'Proton donor' in choice B matches this mechanism precisely. (4) Choice D (position 342) is impossible in a 266-residue protein. (5) Choice A (position 64, Alanine) cannot serve as a nucleophile. (6) Choice C labels Ser153 as 'catalytic acid/base residue,' which is not the standard SDR terminology for the catalytic Ser (it is specifically a proton donor, not a general acid/base). The Ser at 159 is ~15 residues upstream of the catalytic Tyr(174), consistent with typical SDR catalytic-tetrad spacing, while Ser(153) is ~21 residues upstream.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Distinguishing Ser159 from Ser153 as the catalytic proton donor relies on the specific spacing (~15 residues) between the catalytic Ser and the YxxxK dyad in SDR enzymes, which is a family-specific structural detail. A model without SDR-family knowledge would struggle to choose between the two Ser residues purely from the sequence.",
    "reason": "The SDR catalytic mechanism (Ser = proton donor, Tyr = proton acceptor, Lys = pKa modulator), the identifiable YxxxK motif, and the functional labels in the choices provide a concrete biological argument for B over the other options. The elimination of D (impossible position) and A (Ala cannot be nucleophile) is straightforward. The B-vs-C distinction is supported by the correct SDR functional terminology ('Proton donor' vs. non-standard 'acid/base'). The residual difficulty in pinpointing Ser159 over Ser153 is a matter of SDR-specific structural spacing, which is specialized but defensible general biochemistry knowledge."
  },
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A223HDI5 (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) annotates position 159 as 'Proton donor' (Active site), matching choice B exactly. The sequence in the question matches the entry (266 aa, SHA-256 match). However, the evidence code is ECO:0000250 (inferred by similarity to P0C0Y5), making this a computational/transfer annotation rather than direct experimental evidence for this specific protein. The annotation is nonetheless the authoritative database claim and is consistent with the SDR-family catalytic mechanism (Ser as proton donor in the Ser-Tyr-Lys catalytic triad)."
  },
  "important_caveats": [
    "The UniProt annotation for position 159 uses evidence code ECO:0000250 (inferred by similarity to P0C0Y5), meaning it is a computational transfer annotation, not direct experimental evidence (e.g., site-directed mutagenesis or crystallography) for this specific Aureobasidium enzyme.",
    "The protein is 266 residues long; choice D (position 342) is trivially impossible, making it an unusually easy distractor.",
    "The question stem asks to identify 'the enzyme's catalytic center' (singular), but the SDR catalytic center comprises multiple residues (Ser159, Tyr174, Lys178). Only Ser159 appears among the choices, so the question is effectively asking which single annotated active-site residue is correctly described.",
    "The entry was first public on 2025-02-05 with annotation updates through 2026-01-28; the author's source snapshot date is unknown, but the sequence has been stable since 2017-10-25 (sequence version 1)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D are clearly eliminable: A assigns nucleophile function to Alanine (position 64), C uses non-standard terminology ('acid/base') for a Ser that in SDR enzymes is specifically a proton donor, and D references position 342 in a 266-residue protein. Only B corresponds to an annotated active-site residue with a mechanistically accurate functional label. While positions 174 (Proton acceptor) and 178 (Lowers pKa of Tyr) are also active-site residues, they do not appear among the choices, so there is no competing correct option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A223HDI5 (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) annotates position 159 as 'Proton donor' (Active site), matching choice B exactly. The sequence in the question matches the entry (266 aa, SHA-256 match). However, the evidence code is ECO:0000250 (inferred by similarity to P0C0Y5), making this a computational/transfer annotation rather than direct experimental evidence for this specific protein. The annotation is nonetheless the authoritative database claim and is consistent with the SDR-family catalytic mechanism (Ser as proton donor in the Ser-Tyr-Lys catalytic triad).",
    "evidence_ids": ["C5", "H3", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several reasoning steps distinguish B from the distractors using general biochemistry: (1) The N-terminal region contains a Rossmann-fold-like NAD(P)-binding motif (GASGPR at ~26-31), identifying this as an NAD(P)-dependent dehydrogenase. (2) The YxxxK motif at positions 174-178 (Y-N-V-A-K) is the hallmark SDR (short-chain dehydrogenase/reductase) catalytic Tyr-Lys dyad. (3) In the SDR catalytic mechanism, the catalytic Ser acts specifically as a proton donor (donating H+ to the substrate carbonyl oxygen), the Tyr as proton acceptor, and the Lys lowers the Tyr pKa. The functional label 'Proton donor' in choice B matches this mechanism precisely. (4) Choice D (position 342) is impossible in a 266-residue protein. (5) Choice A (position 64, Alanine) cannot serve as a nucleophile. (6) Choice C labels Ser153 as 'catalytic acid/base residue,' which is not the standard SDR terminology for the catalytic Ser (it is specifically a proton donor, not a general acid/base). The Ser at 159 is ~15 residues upstream of the catalytic Tyr(174), consistent with typical SDR catalytic-tetrad spacing, while Ser(153) is ~21 residues upstream.",
    "missing_item_specific_fact": "Distinguishing Ser159 from Ser153 as the catalytic proton donor relies on the specific spacing (~15 residues) between the catalytic Ser and the YxxxK dyad in SDR enzymes, which is a family-specific structural detail. A model without SDR-family knowledge would struggle to choose between the two Ser residues purely from the sequence.",
    "reason": "The SDR catalytic mechanism (Ser = proton donor, Tyr = proton acceptor, Lys = pKa modulator), the identifiable YxxxK motif, and the functional labels in the choices provide a concrete biological argument for B over the other options. The elimination of D (impossible position) and A (Ala cannot be nucleophile) is straightforward. The B-vs-C distinction is supported by the correct SDR functional terminology ('Proton donor' vs. non-standard 'acid/base'). The residual difficulty in pinpointing Ser159 over Ser153 is a matter of SDR-specific structural spacing, which is specialized but defensible general biochemistry knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D are clearly eliminable: A assigns nucleophile function to Alanine (position 64), C uses non-standard terminology ('acid/base') for a Ser that in SDR enzymes is specifically a proton donor, and D references position 342 in a 266-residue protein. Only B corresponds to an annotated active-site residue with a mechanistically accurate functional label. While positions 174 (Proton acceptor) and 178 (Lowers pKa of Tyr) are also active-site residues, they do not appear among the choices, so there is no competing correct option."
  },
  "important_caveats": [
    "The UniProt annotation for position 159 uses evidence code ECO:0000250 (inferred by similarity to P0C0Y5), meaning it is a computational transfer annotation, not direct experimental evidence (e.g., site-directed mutagenesis or crystallography) for this specific Aureobasidium enzyme.",
    "The protein is 266 residues long; choice D (position 342) is trivially impossible, making it an unusually easy distractor.",
    "The question stem asks to identify 'the enzyme's catalytic center' (singular), but the SDR catalytic center comprises multiple residues (Ser159, Tyr174, Lys178). Only Ser159 appears among the choices, so the question is effectively asking which single annotated active-site residue is correctly described.",
    "The entry was first public on 2025-02-05 with annotation updates through 2026-01-28; the author's source snapshot date is unknown, but the sequence has been stable since 2017-10-25 (sequence version 1)."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates position 159 as the proton donor. This annotation is transferred by similarity from another UniProt entry, so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a glycine-rich dinucleotide-binding motif and a downstream Tyr-X3-Lys motif consistent with a short-chain dehydrogenase/reductase. In this enzyme-family pattern, the catalytic Ser is often positioned shortly before the Tyr; here Ser159 lies 15 residues before Tyr174, making option B a credible family-based inference. Ser153 is another nearby serine, but it does not fit that spacing as well.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence-family knowledge gives a meaningful basis for favoring B over the offered alternatives. This is a probabilistic inference, not proof of the precise proton-donor role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence provides a plausible catalytic-motif basis for B; position 342 is beyond the 266-residue sequence.


### Important caveats

- The supporting database annotation is similarity-based, not direct experimental evidence for this protein.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich dinucleotide-binding motif and a downstream Tyr-X3-Lys motif consistent with a short-chain dehydrogenase/reductase. In this enzyme-family pattern, the catalytic Ser is often positioned shortly before the Tyr; here Ser159 lies 15 residues before Tyr174, making option B a credible family-based inference. Ser153 is another nearby serine, but it does not fit that spacing as well.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-family knowledge gives a meaningful basis for favoring B over the offered alternatives. This is a probabilistic inference, not proof of the precise proton-donor role."
  },
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 159 as the proton donor. This annotation is transferred by similarity from another UniProt entry, so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supporting database annotation is similarity-based, not direct experimental evidence for this protein.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence provides a plausible catalytic-motif basis for B; position 342 is beyond the 266-residue sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 159 as the proton donor. This annotation is transferred by similarity from another UniProt entry, so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a glycine-rich dinucleotide-binding motif and a downstream Tyr-X3-Lys motif consistent with a short-chain dehydrogenase/reductase. In this enzyme-family pattern, the catalytic Ser is often positioned shortly before the Tyr; here Ser159 lies 15 residues before Tyr174, making option B a credible family-based inference. Ser153 is another nearby serine, but it does not fit that spacing as well.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-family knowledge gives a meaningful basis for favoring B over the offered alternatives. This is a probabilistic inference, not proof of the precise proton-donor role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence provides a plausible catalytic-motif basis for B; position 342 is beyond the 266-residue sequence."
  },
  "important_caveats": [
    "The supporting database annotation is similarity-based, not direct experimental evidence for this protein.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation at position 159 lists 'Proton donor' (evidence ECO:0000250, inferred by similarity to P0C0Y5, a characterized mannitol dehydrogenase). The residue at position 159 in the supplied 266-aa sequence is indeed Serine (S), consistent with the SDR-family catalytic tetrad mechanism (Ser-Tyr-Lys) in which the Ser acts as proton donor to the substrate. The annotation is computational/similarity-based rather than directly experimental for this exact protein, but the SDR proton-donor role of the Ser is a well-established family-level mechanism. The sequence match is confirmed (SHA256 identical).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical Rossmann-fold glycine-rich motif 'GASGPRG' (positions 26–32), identifying it as an NAD(P)-dependent dehydrogenase. The 266-aa length and the downstream 'S…YxxxK' pattern (Ser159…Tyr174…Lys178) match the well-characterized SDR (Short-chain Dehydrogenase/Reductase) catalytic tetrad. In SDRs, the Ser of the tetrad is the proton donor/orienting residue, the Tyr is the catalytic acid/base, and the Lys is part of the charge relay that lowers the Tyr pKa. Applying this family-level mechanism: (A) position 64 is Ala—not a nucleophile, and SDRs do not employ nucleophilic catalysis; (C) position 153 is a Ser outside the canonical tetrad, and calling any Ser the 'catalytic acid/base' contradicts SDR mechanism (the Tyr fulfills that role); (D) position 342 exceeds the 266-residue sequence length and is impossible. Only (B) Ser159 as 'Proton donor' is consistent with the SDR tetrad geometry and mechanism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the Rossmann fold, recognize the SDR family catalytic tetrad (S…YxxxK), and apply the well-established SDR mechanism (Ser = proton donor, Tyr = acid/base, Lys = charge relay) to eliminate A (Ala, no nucleophile in SDRs), C (Ser is not the acid/base in SDRs), and D (position 342 does not exist in a 266-aa protein). This is a concrete family-level inference from transferable SDR biochemistry, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is eliminated because position 342 exceeds the sequence length (266 aa). Option A is eliminated because position 64 is Ala, which is not a nucleophile and SDRs do not use nucleophilic catalysis. Option C is inconsistent with SDR mechanism because the catalytic acid/base is the Tyr (position 174), not a Ser. Only B remains defensible.


### Important caveats

- The UniProt annotation at position 159 is based on similarity (ECO:0000250 to P0C0Y5), not direct experimental mutagenesis or structural determination of this exact protein.
- The SDR tetrad mechanism (Ser proton donor, Tyr acid/base, Lys charge relay) is well-established across the family but individual members may show mechanistic variations.
- Option D (position 342) is trivially eliminated by sequence length, making it a very easy distractor.
- The protein identity (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) was not provided in the model input; identification relies on sequence pattern recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical Rossmann-fold glycine-rich motif 'GASGPRG' (positions 26–32), identifying it as an NAD(P)-dependent dehydrogenase. The 266-aa length and the downstream 'S…YxxxK' pattern (Ser159…Tyr174…Lys178) match the well-characterized SDR (Short-chain Dehydrogenase/Reductase) catalytic tetrad. In SDRs, the Ser of the tetrad is the proton donor/orienting residue, the Tyr is the catalytic acid/base, and the Lys is part of the charge relay that lowers the Tyr pKa. Applying this family-level mechanism: (A) position 64 is Ala—not a nucleophile, and SDRs do not employ nucleophilic catalysis; (C) position 153 is a Ser outside the canonical tetrad, and calling any Ser the 'catalytic acid/base' contradicts SDR mechanism (the Tyr fulfills that role); (D) position 342 exceeds the 266-residue sequence length and is impossible. Only (B) Ser159 as 'Proton donor' is consistent with the SDR tetrad geometry and mechanism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann fold, recognize the SDR family catalytic tetrad (S…YxxxK), and apply the well-established SDR mechanism (Ser = proton donor, Tyr = acid/base, Lys = charge relay) to eliminate A (Ala, no nucleophile in SDRs), C (Ser is not the acid/base in SDRs), and D (position 342 does not exist in a 266-aa protein). This is a concrete family-level inference from transferable SDR biochemistry, not a lookup of this protein's specific annotation."
  },
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation at position 159 lists 'Proton donor' (evidence ECO:0000250, inferred by similarity to P0C0Y5, a characterized mannitol dehydrogenase). The residue at position 159 in the supplied 266-aa sequence is indeed Serine (S), consistent with the SDR-family catalytic tetrad mechanism (Ser-Tyr-Lys) in which the Ser acts as proton donor to the substrate. The annotation is computational/similarity-based rather than directly experimental for this exact protein, but the SDR proton-donor role of the Ser is a well-established family-level mechanism. The sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt annotation at position 159 is based on similarity (ECO:0000250 to P0C0Y5), not direct experimental mutagenesis or structural determination of this exact protein.",
    "The SDR tetrad mechanism (Ser proton donor, Tyr acid/base, Lys charge relay) is well-established across the family but individual members may show mechanistic variations.",
    "Option D (position 342) is trivially eliminated by sequence length, making it a very easy distractor.",
    "The protein identity (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) was not provided in the model input; identification relies on sequence pattern recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated because position 342 exceeds the sequence length (266 aa). Option A is eliminated because position 64 is Ala, which is not a nucleophile and SDRs do not use nucleophilic catalysis. Option C is inconsistent with SDR mechanism because the catalytic acid/base is the Tyr (position 174), not a Ser. Only B remains defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation at position 159 lists 'Proton donor' (evidence ECO:0000250, inferred by similarity to P0C0Y5, a characterized mannitol dehydrogenase). The residue at position 159 in the supplied 266-aa sequence is indeed Serine (S), consistent with the SDR-family catalytic tetrad mechanism (Ser-Tyr-Lys) in which the Ser acts as proton donor to the substrate. The annotation is computational/similarity-based rather than directly experimental for this exact protein, but the SDR proton-donor role of the Ser is a well-established family-level mechanism. The sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical Rossmann-fold glycine-rich motif 'GASGPRG' (positions 26–32), identifying it as an NAD(P)-dependent dehydrogenase. The 266-aa length and the downstream 'S…YxxxK' pattern (Ser159…Tyr174…Lys178) match the well-characterized SDR (Short-chain Dehydrogenase/Reductase) catalytic tetrad. In SDRs, the Ser of the tetrad is the proton donor/orienting residue, the Tyr is the catalytic acid/base, and the Lys is part of the charge relay that lowers the Tyr pKa. Applying this family-level mechanism: (A) position 64 is Ala—not a nucleophile, and SDRs do not employ nucleophilic catalysis; (C) position 153 is a Ser outside the canonical tetrad, and calling any Ser the 'catalytic acid/base' contradicts SDR mechanism (the Tyr fulfills that role); (D) position 342 exceeds the 266-residue sequence length and is impossible. Only (B) Ser159 as 'Proton donor' is consistent with the SDR tetrad geometry and mechanism.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann fold, recognize the SDR family catalytic tetrad (S…YxxxK), and apply the well-established SDR mechanism (Ser = proton donor, Tyr = acid/base, Lys = charge relay) to eliminate A (Ala, no nucleophile in SDRs), C (Ser is not the acid/base in SDRs), and D (position 342 does not exist in a 266-aa protein). This is a concrete family-level inference from transferable SDR biochemistry, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated because position 342 exceeds the sequence length (266 aa). Option A is eliminated because position 64 is Ala, which is not a nucleophile and SDRs do not use nucleophilic catalysis. Option C is inconsistent with SDR mechanism because the catalytic acid/base is the Tyr (position 174), not a Ser. Only B remains defensible."
  },
  "important_caveats": [
    "The UniProt annotation at position 159 is based on similarity (ECO:0000250 to P0C0Y5), not direct experimental mutagenesis or structural determination of this exact protein.",
    "The SDR tetrad mechanism (Ser proton donor, Tyr acid/base, Lys charge relay) is well-established across the family but individual members may show mechanistic variations.",
    "Option D (position 342) is trivially eliminated by sequence length, making it a very easy distractor.",
    "The protein identity (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) was not provided in the model input; identification relies on sequence pattern recognition."
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
  "requested_accession": "A0A223HDI5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "9ba750d830f9b17efbb379114b2586beae27b485e183fc99fdd2ab0bad2a96aa",
  "benchmark_sequence_length": 266,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "current_source_sequence_sha256": "9ba750d830f9b17efbb379114b2586beae27b485e183fc99fdd2ab0bad2a96aa",
  "current_source_sequence_length": 266,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 15,
  "selected_historical_version": {
    "accession": "A0A223HDI5",
    "database": "Swiss-Prot",
    "entryVersion": 15,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMTDH_AURME",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "selected_historical_source_sequence_sha256": "9ba750d830f9b17efbb379114b2586beae27b485e183fc99fdd2ab0bad2a96aa",
  "selected_historical_source_sequence_length": 266,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 15,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A223HDI5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.138\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"NADP-dependent mannitol dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"MtDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C0Y5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":159},\"start\":{\"modifier\":\"EXACT\",\"value\":159}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C0Y5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":174},\"start\":{\"modifier\":\"EXACT\",\"value\":174}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Lowers pKa of active site Tyr\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C0Y5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":107},\"start\":{\"modifier\":\"EXACT\",\"value\":107}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":140},\"start\":{\"modifier\":\"EXACT\",\"value\":140}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":174},\"start\":{\"modifier\":\"EXACT\",\"value\":174}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":206},\"start\":{\"modifier\":\"EXACT\",\"value\":206}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":208},\"start\":{\"modifier\":\"EXACT\",\"value\":208}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   NMTDH_AURME             Reviewed;         266 AA.\nAC   A0A223HDI5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 15.\nDE   RecName: Full=NADP-dependent mannitol dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=MtDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.138 {ECO:0000269|PubMed:32003433};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 31-37",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 101-103",
  "excerpt": "FT   ACT_SITE        159\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P0C0Y5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 104-106",
  "excerpt": "FT   ACT_SITE        174\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P0C0Y5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 107-109",
  "excerpt": "FT   ACT_SITE        178\nFT                   /note=\"Lowers pKa of active site Tyr\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P0C0Y5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 110-113",
  "excerpt": "FT   BINDING         107\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 114-117",
  "excerpt": "FT   BINDING         140\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 118-121",
  "excerpt": "FT   BINDING         174\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 122-125",
  "excerpt": "FT   BINDING         178\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 126-129",
  "excerpt": "FT   BINDING         206\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "source_locator": "lines 130-133",
  "excerpt": "FT   BINDING         208\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 15,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 16. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
