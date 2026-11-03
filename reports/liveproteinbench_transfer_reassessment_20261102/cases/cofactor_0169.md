# cofactor_0169: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0169.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **B** — Zn(2+)

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
MAVFPLSAKHRKYALRALAVSIILVSAAYIASTERTERVRPQRVEQNLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGGAREVQFFTDEDGERNLVALEKKGGIWRRSASEADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLMYDSLYFHGQQVAAGDILAAEVVKGGTRHQAFYYRSDKEGGGGGNYYDEDGKVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAEGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. tungstopterin
B. Zn(2+)
C. a divalent metal cation
D. Mn(2+)
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

> The supplied sequence exactly matches the UniProt entry for Mpg, annotated as a zinc metallopeptidase that binds one Zn(2+) per subunit. The cofactor annotation is transferred by similarity, not direct experimental evidence for this sequence, so support is annotation-based rather than independently demonstrated here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a protein with a signal peptide and a metalloprotease-like function, but the input alone does not establish that its cofactor is specifically zinc rather than another divalent metal.


**Missing item-specific fact**

> The protein's identity as Mpg and its zinc-cofactor annotation or equivalent protein-specific evidence.


**Reason**

> Choosing Zn(2+) over Mn(2+) or the broader divalent-metal option requires the protein-specific cofactor fact; it is not reliably determined by general sequence reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Zn(2+) is itself a divalent metal cation, so choice C is literally true if interpreted broadly, although B is the specific cofactor annotation.


### Important caveats

- The sequence match is exact, but the available cofactor annotation is transferred by similarity from another UniProt entry.
- The reviewer-only database identity and annotation were not supplied in the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a protein with a signal peptide and a metalloprotease-like function, but the input alone does not establish that its cofactor is specifically zinc rather than another divalent metal.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as Mpg and its zinc-cofactor annotation or equivalent protein-specific evidence.",
    "reason": "Choosing Zn(2+) over Mn(2+) or the broader divalent-metal option requires the protein-specific cofactor fact; it is not reliably determined by general sequence reasoning alone."
  },
  "case_id": "cofactor_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for Mpg, annotated as a zinc metallopeptidase that binds one Zn(2+) per subunit. The cofactor annotation is transferred by similarity, not direct experimental evidence for this sequence, so support is annotation-based rather than independently demonstrated here."
  },
  "important_caveats": [
    "The sequence match is exact, but the available cofactor annotation is transferred by similarity from another UniProt entry.",
    "The reviewer-only database identity and annotation were not supplied in the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Zn(2+) is itself a divalent metal cation, so choice C is literally true if interpreted broadly, although B is the specific cofactor annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for Mpg, annotated as a zinc metallopeptidase that binds one Zn(2+) per subunit. The cofactor annotation is transferred by similarity, not direct experimental evidence for this sequence, so support is annotation-based rather than independently demonstrated here.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a protein with a signal peptide and a metalloprotease-like function, but the input alone does not establish that its cofactor is specifically zinc rather than another divalent metal.",
    "missing_item_specific_fact": "The protein's identity as Mpg and its zinc-cofactor annotation or equivalent protein-specific evidence.",
    "reason": "Choosing Zn(2+) over Mn(2+) or the broader divalent-metal option requires the protein-specific cofactor fact; it is not reliably determined by general sequence reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Zn(2+) is itself a divalent metal cation, so choice C is literally true if interpreted broadly, although B is the specific cofactor annotation."
  },
  "important_caveats": [
    "The sequence match is exact, but the available cofactor annotation is transferred by similarity from another UniProt entry.",
    "The reviewer-only database identity and annotation were not supplied in the original question."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5, H5) explicitly lists Zn(2+) (ChEBI:29105) as the cofactor, noting 'Binds 1 zinc ion per subunit.' The protein is named 'Zinc metallopeptidase,' 'Zinc metalloprotease,' and 'Zinc-dependent metallopeptidase.' The EC numbers 3.4.17.- and 3.4.24.- are consistent with zinc metalloproteases. However, the evidence code is ECO:0000250 (similarity transfer from E0N688), meaning the Zn(2+) assignment is inferred by homology rather than direct experimental measurement. The protein name annotations carry ECO:0000305 (automatic assertion). The annotation is consistent and supports the key, though it is computational inference rather than direct experimental proof.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the GGDGG motif ('VLVGGDGGAREVQFF') and DED patterns ('QFFTDEDGERNL'), which are characteristic zinc-coordinating motifs of M23-family DD-carboxypeptidases. The overall architecture (signal peptide, outer membrane localization context, peptidase fold) combined with these motifs is diagnostic of a zinc-dependent metalloprotease rather than a manganese-dependent enzyme. This specifically implicates Zn(2+) over Mn(2+) (D) and over the generic 'a divalent metal cation' (C), since the question asks for the 'specific cofactor' and the GGDGG/DED signature is a zinc-specific coordination geometry in this peptidase family.


**Missing item-specific fact**

> None critical. The sequence motifs are visible in the input. The distinction between B and C relies on the question wording ('specific cofactor') and the biological convention that GGDGG-containing metalloproteases specifically coordinate Zn(2+), not just any divalent cation.


**Reason**

> A model with knowledge of metalloprotease families can identify the GGDGG and DED motifs as zinc-coordinating signatures specific to M23 peptidases, distinguishing Zn(2+) from Mn(2+) and from the overly generic 'divalent metal cation' option. This is general biological reasoning from sequence features, not mere database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Zn(2+) IS a divalent metal cation, so option C is not factually wrong—it is simply less specific. The question asks for 'the specific cofactor,' which linguistically favors B. However, a model could reasonably argue C is also correct since it is a true statement about the cofactor. The distinction between B and C rests on the word 'specific' in the prompt and on the convention that GGDGG motifs specifically coordinate Zn(2+). This is a minor wording issue rather than a fundamental defect, but it creates mild ambiguity.


### Important caveats

- The Zn(2+) annotation is based on similarity transfer (ECO:0000250 from E0N688), not direct experimental measurement of metal content in this specific protein.
- The protein name annotations ('Zinc metallopeptidase' etc.) carry ECO:0000305 (automatic assertion), meaning they are inferred, not experimentally validated for this specific sequence.
- The identity of the protein (Q9K163, Mpg/OMP 0315) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.
- The GGDGG motif reasoning is a general family-level heuristic; whether it definitively excludes Mn(2+) for this specific protein without experimental data is an inference, not a certainty.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the GGDGG motif ('VLVGGDGGAREVQFF') and DED patterns ('QFFTDEDGERNL'), which are characteristic zinc-coordinating motifs of M23-family DD-carboxypeptidases. The overall architecture (signal peptide, outer membrane localization context, peptidase fold) combined with these motifs is diagnostic of a zinc-dependent metalloprotease rather than a manganese-dependent enzyme. This specifically implicates Zn(2+) over Mn(2+) (D) and over the generic 'a divalent metal cation' (C), since the question asks for the 'specific cofactor' and the GGDGG/DED signature is a zinc-specific coordination geometry in this peptidase family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The sequence motifs are visible in the input. The distinction between B and C relies on the question wording ('specific cofactor') and the biological convention that GGDGG-containing metalloproteases specifically coordinate Zn(2+), not just any divalent cation.",
    "reason": "A model with knowledge of metalloprotease families can identify the GGDGG and DED motifs as zinc-coordinating signatures specific to M23 peptidases, distinguishing Zn(2+) from Mn(2+) and from the overly generic 'divalent metal cation' option. This is general biological reasoning from sequence features, not mere database lookup."
  },
  "case_id": "cofactor_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H5) explicitly lists Zn(2+) (ChEBI:29105) as the cofactor, noting 'Binds 1 zinc ion per subunit.' The protein is named 'Zinc metallopeptidase,' 'Zinc metalloprotease,' and 'Zinc-dependent metallopeptidase.' The EC numbers 3.4.17.- and 3.4.24.- are consistent with zinc metalloproteases. However, the evidence code is ECO:0000250 (similarity transfer from E0N688), meaning the Zn(2+) assignment is inferred by homology rather than direct experimental measurement. The protein name annotations carry ECO:0000305 (automatic assertion). The annotation is consistent and supports the key, though it is computational inference rather than direct experimental proof."
  },
  "important_caveats": [
    "The Zn(2+) annotation is based on similarity transfer (ECO:0000250 from E0N688), not direct experimental measurement of metal content in this specific protein.",
    "The protein name annotations ('Zinc metallopeptidase' etc.) carry ECO:0000305 (automatic assertion), meaning they are inferred, not experimentally validated for this specific sequence.",
    "The identity of the protein (Q9K163, Mpg/OMP 0315) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.",
    "The GGDGG motif reasoning is a general family-level heuristic; whether it definitively excludes Mn(2+) for this specific protein without experimental data is an inference, not a certainty."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Zn(2+) IS a divalent metal cation, so option C is not factually wrong—it is simply less specific. The question asks for 'the specific cofactor,' which linguistically favors B. However, a model could reasonably argue C is also correct since it is a true statement about the cofactor. The distinction between B and C rests on the word 'specific' in the prompt and on the convention that GGDGG motifs specifically coordinate Zn(2+). This is a minor wording issue rather than a fundamental defect, but it creates mild ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H5) explicitly lists Zn(2+) (ChEBI:29105) as the cofactor, noting 'Binds 1 zinc ion per subunit.' The protein is named 'Zinc metallopeptidase,' 'Zinc metalloprotease,' and 'Zinc-dependent metallopeptidase.' The EC numbers 3.4.17.- and 3.4.24.- are consistent with zinc metalloproteases. However, the evidence code is ECO:0000250 (similarity transfer from E0N688), meaning the Zn(2+) assignment is inferred by homology rather than direct experimental measurement. The protein name annotations carry ECO:0000305 (automatic assertion). The annotation is consistent and supports the key, though it is computational inference rather than direct experimental proof.",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the GGDGG motif ('VLVGGDGGAREVQFF') and DED patterns ('QFFTDEDGERNL'), which are characteristic zinc-coordinating motifs of M23-family DD-carboxypeptidases. The overall architecture (signal peptide, outer membrane localization context, peptidase fold) combined with these motifs is diagnostic of a zinc-dependent metalloprotease rather than a manganese-dependent enzyme. This specifically implicates Zn(2+) over Mn(2+) (D) and over the generic 'a divalent metal cation' (C), since the question asks for the 'specific cofactor' and the GGDGG/DED signature is a zinc-specific coordination geometry in this peptidase family.",
    "missing_item_specific_fact": "None critical. The sequence motifs are visible in the input. The distinction between B and C relies on the question wording ('specific cofactor') and the biological convention that GGDGG-containing metalloproteases specifically coordinate Zn(2+), not just any divalent cation.",
    "reason": "A model with knowledge of metalloprotease families can identify the GGDGG and DED motifs as zinc-coordinating signatures specific to M23 peptidases, distinguishing Zn(2+) from Mn(2+) and from the overly generic 'divalent metal cation' option. This is general biological reasoning from sequence features, not mere database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Zn(2+) IS a divalent metal cation, so option C is not factually wrong—it is simply less specific. The question asks for 'the specific cofactor,' which linguistically favors B. However, a model could reasonably argue C is also correct since it is a true statement about the cofactor. The distinction between B and C rests on the word 'specific' in the prompt and on the convention that GGDGG motifs specifically coordinate Zn(2+). This is a minor wording issue rather than a fundamental defect, but it creates mild ambiguity."
  },
  "important_caveats": [
    "The Zn(2+) annotation is based on similarity transfer (ECO:0000250 from E0N688), not direct experimental measurement of metal content in this specific protein.",
    "The protein name annotations ('Zinc metallopeptidase' etc.) carry ECO:0000305 (automatic assertion), meaning they are inferred, not experimentally validated for this specific sequence.",
    "The identity of the protein (Q9K163, Mpg/OMP 0315) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.",
    "The GGDGG motif reasoning is a general family-level heuristic; whether it definitively excludes Mn(2+) for this specific protein without experimental data is an inference, not a certainty."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry annotates Zn(2+) as the cofactor and states that one zinc ion binds per subunit. This annotation is transferred by similarity (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a signal-peptide-like N-terminus and a histidine-rich region consistent with a bacterial metallopeptidase. Transferable knowledge that metallopeptidases commonly use zinc coordinated by histidines supports Zn(2+) over tungstopterin or manganese. Choice C is compatible with zinc but is less specific.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level metalloprotease inference gives a meaningful basis for selecting zinc from these choices without needing the exact protein's database annotation. The sequence alone does not establish direct experimental metal binding.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Zn(2+) is itself a divalent metal cation, but option C does not specify which one; the question asks for the specific cofactor, making B the more informative choice.


### Important caveats

- The cited cofactor annotation is based on similarity to another UniProt entry, not experimental evidence shown here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and a histidine-rich region consistent with a bacterial metallopeptidase. Transferable knowledge that metallopeptidases commonly use zinc coordinated by histidines supports Zn(2+) over tungstopterin or manganese. Choice C is compatible with zinc but is less specific.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level metalloprotease inference gives a meaningful basis for selecting zinc from these choices without needing the exact protein's database annotation. The sequence alone does not establish direct experimental metal binding."
  },
  "case_id": "cofactor_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates Zn(2+) as the cofactor and states that one zinc ion binds per subunit. This annotation is transferred by similarity (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The cited cofactor annotation is based on similarity to another UniProt entry, not experimental evidence shown here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Zn(2+) is itself a divalent metal cation, but option C does not specify which one; the question asks for the specific cofactor, making B the more informative choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates Zn(2+) as the cofactor and states that one zinc ion binds per subunit. This annotation is transferred by similarity (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and a histidine-rich region consistent with a bacterial metallopeptidase. Transferable knowledge that metallopeptidases commonly use zinc coordinated by histidines supports Zn(2+) over tungstopterin or manganese. Choice C is compatible with zinc but is less specific.",
    "missing_item_specific_fact": "",
    "reason": "A family-level metalloprotease inference gives a meaningful basis for selecting zinc from these choices without needing the exact protein's database annotation. The sequence alone does not establish direct experimental metal binding."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Zn(2+) is itself a divalent metal cation, but option C does not specify which one; the question asks for the specific cofactor, making B the more informative choice."
  },
  "important_caveats": [
    "The cited cofactor annotation is based on similarity to another UniProt entry, not experimental evidence shown here."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q9K163 (Mpg, DD-carboxypeptidase/endopeptidase) explicitly lists Zn(2+) as the cofactor (CHEBI:29105), with the note 'Binds 1 zinc ion per subunit.' The protein is named 'Zinc metallopeptidase,' 'Zinc metalloprotease,' and 'Zinc-dependent metallopeptidase,' and carries EC numbers 3.4.17.- and 3.4.24.- (metalloendopeptidase). The evidence code is ECO:0000250 (similarity-based transfer from E0N688), making this computational inference rather than direct experimental measurement, but the annotation is internally consistent and clearly supports Zn(2+) as the expected answer.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can use several transferable features: (1) The sequence contains a bacterial signal peptide and a peptidase-like architecture with clustered His residues (e.g., 'HANGVETLYAH', 'GPHLHY') consistent with zinc-coordination geometry typical of metalloproteases. (2) The overwhelming majority of metalloendopeptidases (EC 3.4.24.-) are zinc-dependent; zinc is the canonical metal for peptidase active sites, with His/His/Asp or His/His/His coordination. (3) Tungstopterin (A) is specific to formate dehydrogenases and related tungsten enzymes, an entirely different enzyme class. (4) Mn(2+) (D) is more commonly associated with phosphatases, arginase, and certain hydrolases; it is less typical for peptidase active sites. (5) The question asks for the 'specific cofactor,' which distinguishes Zn(2+) (B) from the generic 'a divalent metal cation' (C): in biological nomenclature, specifying Zn(2+) reflects the particular coordination chemistry (tetrahedral d10 geometry) that differentiates it from other divalent ions. Family-level knowledge of peptidase metal preferences thus meaningfully favors B over A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of sequence features (His clusters suggestive of zinc coordination, peptidase-like fold), family-level knowledge that metalloproteases overwhelmingly use Zn(2+), and the question's request for the 'specific' cofactor provides a concrete transferable argument distinguishing B from A (wrong enzyme class), D (less common metal for peptidases), and C (less specific than Zn(2+)). The inference does not require knowing the exact UniProt entry for Q9K163.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Zn(2+) is itself a divalent metal cation, so option C is technically true if B is true. The question resolves this by asking for the 'specific cofactor,' which should select the most precise answer (B). However, a model interpreting 'a divalent metal cation' as a valid but less-specific true statement could view C as not-wrong, creating mild ambiguity. The distinction is defensible in standard biological usage where cofactor identity is stated at the ion level (Zn2+ vs. Mn2+ vs. Mg2+), not the class level.


### Important caveats

- The Zn(2+) annotation is based on similarity transfer (ECO:0000250 from E0N688), not direct experimental cofactor determination for this exact protein.
- The B vs C distinction depends on the question phrasing 'specific cofactor'; without that qualifier, C would be a broadly correct but non-specific alternative.
- The protein was integrated into Swiss-Prot only in 2025; the author's source snapshot may have relied on TrEMBL or earlier annotations with less detailed cofactor information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can use several transferable features: (1) The sequence contains a bacterial signal peptide and a peptidase-like architecture with clustered His residues (e.g., 'HANGVETLYAH', 'GPHLHY') consistent with zinc-coordination geometry typical of metalloproteases. (2) The overwhelming majority of metalloendopeptidases (EC 3.4.24.-) are zinc-dependent; zinc is the canonical metal for peptidase active sites, with His/His/Asp or His/His/His coordination. (3) Tungstopterin (A) is specific to formate dehydrogenases and related tungsten enzymes, an entirely different enzyme class. (4) Mn(2+) (D) is more commonly associated with phosphatases, arginase, and certain hydrolases; it is less typical for peptidase active sites. (5) The question asks for the 'specific cofactor,' which distinguishes Zn(2+) (B) from the generic 'a divalent metal cation' (C): in biological nomenclature, specifying Zn(2+) reflects the particular coordination chemistry (tetrahedral d10 geometry) that differentiates it from other divalent ions. Family-level knowledge of peptidase metal preferences thus meaningfully favors B over A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of sequence features (His clusters suggestive of zinc coordination, peptidase-like fold), family-level knowledge that metalloproteases overwhelmingly use Zn(2+), and the question's request for the 'specific' cofactor provides a concrete transferable argument distinguishing B from A (wrong enzyme class), D (less common metal for peptidases), and C (less specific than Zn(2+)). The inference does not require knowing the exact UniProt entry for Q9K163."
  },
  "case_id": "cofactor_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9K163 (Mpg, DD-carboxypeptidase/endopeptidase) explicitly lists Zn(2+) as the cofactor (CHEBI:29105), with the note 'Binds 1 zinc ion per subunit.' The protein is named 'Zinc metallopeptidase,' 'Zinc metalloprotease,' and 'Zinc-dependent metallopeptidase,' and carries EC numbers 3.4.17.- and 3.4.24.- (metalloendopeptidase). The evidence code is ECO:0000250 (similarity-based transfer from E0N688), making this computational inference rather than direct experimental measurement, but the annotation is internally consistent and clearly supports Zn(2+) as the expected answer."
  },
  "important_caveats": [
    "The Zn(2+) annotation is based on similarity transfer (ECO:0000250 from E0N688), not direct experimental cofactor determination for this exact protein.",
    "The B vs C distinction depends on the question phrasing 'specific cofactor'; without that qualifier, C would be a broadly correct but non-specific alternative.",
    "The protein was integrated into Swiss-Prot only in 2025; the author's source snapshot may have relied on TrEMBL or earlier annotations with less detailed cofactor information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Zn(2+) is itself a divalent metal cation, so option C is technically true if B is true. The question resolves this by asking for the 'specific cofactor,' which should select the most precise answer (B). However, a model interpreting 'a divalent metal cation' as a valid but less-specific true statement could view C as not-wrong, creating mild ambiguity. The distinction is defensible in standard biological usage where cofactor identity is stated at the ion level (Zn2+ vs. Mn2+ vs. Mg2+), not the class level."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9K163 (Mpg, DD-carboxypeptidase/endopeptidase) explicitly lists Zn(2+) as the cofactor (CHEBI:29105), with the note 'Binds 1 zinc ion per subunit.' The protein is named 'Zinc metallopeptidase,' 'Zinc metalloprotease,' and 'Zinc-dependent metallopeptidase,' and carries EC numbers 3.4.17.- and 3.4.24.- (metalloendopeptidase). The evidence code is ECO:0000250 (similarity-based transfer from E0N688), making this computational inference rather than direct experimental measurement, but the annotation is internally consistent and clearly supports Zn(2+) as the expected answer.",
    "evidence_ids": ["C5", "H5", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can use several transferable features: (1) The sequence contains a bacterial signal peptide and a peptidase-like architecture with clustered His residues (e.g., 'HANGVETLYAH', 'GPHLHY') consistent with zinc-coordination geometry typical of metalloproteases. (2) The overwhelming majority of metalloendopeptidases (EC 3.4.24.-) are zinc-dependent; zinc is the canonical metal for peptidase active sites, with His/His/Asp or His/His/His coordination. (3) Tungstopterin (A) is specific to formate dehydrogenases and related tungsten enzymes, an entirely different enzyme class. (4) Mn(2+) (D) is more commonly associated with phosphatases, arginase, and certain hydrolases; it is less typical for peptidase active sites. (5) The question asks for the 'specific cofactor,' which distinguishes Zn(2+) (B) from the generic 'a divalent metal cation' (C): in biological nomenclature, specifying Zn(2+) reflects the particular coordination chemistry (tetrahedral d10 geometry) that differentiates it from other divalent ions. Family-level knowledge of peptidase metal preferences thus meaningfully favors B over A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The combination of sequence features (His clusters suggestive of zinc coordination, peptidase-like fold), family-level knowledge that metalloproteases overwhelmingly use Zn(2+), and the question's request for the 'specific' cofactor provides a concrete transferable argument distinguishing B from A (wrong enzyme class), D (less common metal for peptidases), and C (less specific than Zn(2+)). The inference does not require knowing the exact UniProt entry for Q9K163."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Zn(2+) is itself a divalent metal cation, so option C is technically true if B is true. The question resolves this by asking for the 'specific cofactor,' which should select the most precise answer (B). However, a model interpreting 'a divalent metal cation' as a valid but less-specific true statement could view C as not-wrong, creating mild ambiguity. The distinction is defensible in standard biological usage where cofactor identity is stated at the ion level (Zn2+ vs. Mn2+ vs. Mg2+), not the class level."
  },
  "important_caveats": [
    "The Zn(2+) annotation is based on similarity transfer (ECO:0000250 from E0N688), not direct experimental cofactor determination for this exact protein.",
    "The B vs C distinction depends on the question phrasing 'specific cofactor'; without that qualifier, C would be a broadly correct but non-specific alternative.",
    "The protein was integrated into Swiss-Prot only in 2025; the author's source snapshot may have relied on TrEMBL or earlier annotations with less detailed cofactor information."
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
  "requested_accession": "Q9K163",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "408c66280f8d66988edb935017c4298e17cf223293ee87d6ef970a50d0651da9",
  "benchmark_sequence_length": 430,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 112,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "23cecc52bb3f86d214f856ce8a5d816d83336c99efa420a37cfc89e96ef38c2a",
  "current_source_sequence_sha256": "408c66280f8d66988edb935017c4298e17cf223293ee87d6ef970a50d0651da9",
  "current_source_sequence_length": 430,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 110,
  "selected_historical_version": {
    "accession": "Q9K163",
    "database": "Swiss-Prot",
    "entryVersion": 110,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MPG_NEIMB",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "a6e47f3fa0bdfb70912a0b357cacefa3a3f1649b3ff1cc96843145dbf05b9af2",
  "selected_historical_source_sequence_sha256": "408c66280f8d66988edb935017c4298e17cf223293ee87d6ef970a50d0651da9",
  "selected_historical_source_sequence_length": 430,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 110,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9K163.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9K163.json",
  "source_sha256": "23cecc52bb3f86d214f856ce8a5d816d83336c99efa420a37cfc89e96ef38c2a",
  "retrieved_utc": "2026-11-02T04:32:53.795917+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9K163\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9K163.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9K163.json",
  "source_sha256": "23cecc52bb3f86d214f856ce8a5d816d83336c99efa420a37cfc89e96ef38c2a",
  "retrieved_utc": "2026-11-02T04:32:53.795917+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":112,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9K163.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9K163.json",
  "source_sha256": "23cecc52bb3f86d214f856ce8a5d816d83336c99efa420a37cfc89e96ef38c2a",
  "retrieved_utc": "2026-11-02T04:32:53.795917+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF40760.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000425\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Neisseriales\",\"Neisseriaceae\",\"Neisseria\"],\"scientificName\":\"Neisseria meningitidis serogroup B (strain ATCC BAA-335 / MC58)\",\"taxonId\":122586}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9K163.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9K163.json",
  "source_sha256": "23cecc52bb3f86d214f856ce8a5d816d83336c99efa420a37cfc89e96ef38c2a",
  "retrieved_utc": "2026-11-02T04:32:53.795917+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"Metalloprotease active against peptidoglycan\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29257302\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33548582\",\"source\":\"PubMed\"}],\"value\":\"Outer membrane protein 0315\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33548582\",\"source\":\"PubMed\"}],\"value\":\"OMP 0315\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc metallopeptidase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc metalloprotease\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc-dependent metallopeptidase\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.17.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DD-carboxypeptidase/endopeptidase Mpg\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9K163.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9K163.json",
  "source_sha256": "23cecc52bb3f86d214f856ce8a5d816d83336c99efa420a37cfc89e96ef38c2a",
  "retrieved_utc": "2026-11-02T04:32:53.795917+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E0N688\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"E0N688\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 zinc ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9K163.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9K163.json",
  "source_sha256": "23cecc52bb3f86d214f856ce8a5d816d83336c99efa420a37cfc89e96ef38c2a",
  "retrieved_utc": "2026-11-02T04:32:53.795917+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Wu X.\",\"Li K.\",\"Xie M.\",\"Yu M.\",\"Tang S.\",\"Li Z.\",\"Hu S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29257302\"},{\"database\":\"DOI\",\"id\":\"10.3892/mmr.2017.8255\"}],\"citationType\":\"journal article\",\"firstPage\":\"3178\",\"id\":\"29257302\",\"journal\":\"Mol. Med. Report.\",\"lastPage\":\"3185\",\"publicationDate\":\"2018\",\"title\":\"Construction and protective immunogenicity of DNA vaccine pNMB0315 against Neisseria meningitidis serogroup B.\",\"volume\":\"17\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29257302\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC BAA-335 / MC58\"}],\"referenceNumber\":2,\"referencePositions\":[\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9K163.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9K163.json",
  "source_sha256": "23cecc52bb3f86d214f856ce8a5d816d83336c99efa420a37cfc89e96ef38c2a",
  "retrieved_utc": "2026-11-02T04:32:53.795917+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Li Z.\",\"Li Y.\",\"Wang Y.\",\"Hou Y.\",\"Cao H.\",\"Wu X.\",\"Hu S.\",\"Long D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33548582\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.intimp.2021.107411\"}],\"citationType\":\"journal article\",\"firstPage\":\"107411\",\"id\":\"33548582\",\"journal\":\"Int. Immunopharmacol.\",\"lastPage\":\"107411\",\"publicationDate\":\"2021\",\"title\":\"Intranasal immunization with a rNMB0315 and combination adjuvants induces protective immunity against Neisseria meningitidis serogroup B in mice.\",\"volume\":\"93\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33548582\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC BAA-335 / MC58\"}],\"referenceNumber\":3,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110",
  "source_sha256": "a6e47f3fa0bdfb70912a0b357cacefa3a3f1649b3ff1cc96843145dbf05b9af2",
  "retrieved_utc": "2026-11-02T04:33:02.042767+00:00",
  "source_locator": "lines 1-21",
  "excerpt": "ID   MPG_NEIMB               Reviewed;         430 AA.\nAC   Q9K163;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 110.\nDE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};\nDE            EC=3.4.17.- {ECO:0000250|UniProtKB:Q5F676};\nDE            EC=3.4.24.- {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Outer membrane protein 0315 {ECO:0000303|PubMed:29257302, ECO:0000303|PubMed:33548582};\nDE            Short=OMP 0315 {ECO:0000303|PubMed:33548582};\nDE   AltName: Full=Zinc metallopeptidase {ECO:0000305};\nDE   AltName: Full=Zinc metalloprotease {ECO:0000305};\nDE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000305};\nDE   Flags: Precursor;\nGN   OrderedLocusNames=NMB0315 {ECO:0000303|PubMed:29257302,\nGN   ECO:0000303|PubMed:33548582, ECO:0000312|EMBL:AAF40760.1};\nOS   Neisseria meningitidis serogroup B (strain ATCC BAA-335 / MC58).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;\nOC   Neisseriaceae; Neisseria.\nOX   NCBI_TaxID=122586 {ECO:0000312|EMBL:AAF40760.1, ECO:0000312|Proteomes:UP000000425};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110",
  "source_sha256": "a6e47f3fa0bdfb70912a0b357cacefa3a3f1649b3ff1cc96843145dbf05b9af2",
  "retrieved_utc": "2026-11-02T04:33:02.042767+00:00",
  "source_locator": "lines 6-15",
  "excerpt": "DE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};\nDE            EC=3.4.17.- {ECO:0000250|UniProtKB:Q5F676};\nDE            EC=3.4.24.- {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Outer membrane protein 0315 {ECO:0000303|PubMed:29257302, ECO:0000303|PubMed:33548582};\nDE            Short=OMP 0315 {ECO:0000303|PubMed:33548582};\nDE   AltName: Full=Zinc metallopeptidase {ECO:0000305};\nDE   AltName: Full=Zinc metalloprotease {ECO:0000305};\nDE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110",
  "source_sha256": "a6e47f3fa0bdfb70912a0b357cacefa3a3f1649b3ff1cc96843145dbf05b9af2",
  "retrieved_utc": "2026-11-02T04:33:02.042767+00:00",
  "source_locator": "lines 38-45",
  "excerpt": "RN   [2]\nRP   BIOTECHNOLOGY.\nRC   STRAIN=ATCC BAA-335 / MC58 {ECO:0000303|PubMed:29257302};\nRX   PubMed=29257302; DOI=10.3892/mmr.2017.8255;\nRA   Wu X., Li K., Xie M., Yu M., Tang S., Li Z., Hu S.;\nRT   \"Construction and protective immunogenicity of DNA vaccine pNMB0315 against\nRT   Neisseria meningitidis serogroup B.\";\nRL   Mol. Med. Report. 17:3178-3185(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110",
  "source_sha256": "a6e47f3fa0bdfb70912a0b357cacefa3a3f1649b3ff1cc96843145dbf05b9af2",
  "retrieved_utc": "2026-11-02T04:33:02.042767+00:00",
  "source_locator": "lines 46-53",
  "excerpt": "RN   [3]\nRP   SUBCELLULAR LOCATION, AND BIOTECHNOLOGY.\nRC   STRAIN=ATCC BAA-335 / MC58 {ECO:0000303|PubMed:33548582};\nRX   PubMed=33548582; DOI=10.1016/j.intimp.2021.107411;\nRA   Li Z., Li Y., Wang Y., Hou Y., Cao H., Wu X., Hu S., Long D.;\nRT   \"Intranasal immunization with a rNMB0315 and combination adjuvants induces\nRT   protective immunity against Neisseria meningitidis serogroup B in mice.\";\nRL   Int. Immunopharmacol. 93:107411-107411(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9K163?format=txt&versions=110",
  "source_sha256": "a6e47f3fa0bdfb70912a0b357cacefa3a3f1649b3ff1cc96843145dbf05b9af2",
  "retrieved_utc": "2026-11-02T04:33:02.042767+00:00",
  "source_locator": "lines 57-60",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:E0N688};\nCC       Note=Binds 1 zinc ion per subunit. {ECO:0000250|UniProtKB:E0N688};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 110,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 169. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
