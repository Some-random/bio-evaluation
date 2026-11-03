# cofactor_0130: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0130.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **C** — &#91;2Fe-2S&#93; cluster

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
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. [4Fe-4S] cluster
B. FAD
C. [2Fe-2S] cluster
D. Mg(2+)
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

> The exact sequence matches the annotated protein, and the source records a &#91;2Fe-2S&#93; cluster as a cofactor with experimental evidence code ECO:0000269. The source also records Mg(2+) as a cofactor with the same evidence code.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features might suggest an iron-sulfur protein, but they do not establish the specific cofactor requirements or distinguish the &#91;2Fe-2S&#93; annotation from the separately annotated Mg(2+).


**Missing item-specific fact**

> The protein-specific cofactor annotations or experimental characterization are absent from the input.


**Reason**

> The sequence alone does not provide a clear basis for selecting one cofactor, particularly because the matched protein is annotated with both &#91;2Fe-2S&#93; and Mg(2+).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both &#91;2Fe-2S&#93; cluster and Mg(2+) are listed as cofactors for the matched protein with experimental evidence.


### Important caveats

- The reviewer-only source evidence was not supplied to the evaluated model.
- The source supports the expected answer but does not make it the only defensible choice under the wording.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features might suggest an iron-sulfur protein, but they do not establish the specific cofactor requirements or distinguish the [2Fe-2S] annotation from the separately annotated Mg(2+).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cofactor annotations or experimental characterization are absent from the input.",
    "reason": "The sequence alone does not provide a clear basis for selecting one cofactor, particularly because the matched protein is annotated with both [2Fe-2S] and Mg(2+)."
  },
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated protein, and the source records a [2Fe-2S] cluster as a cofactor with experimental evidence code ECO:0000269. The source also records Mg(2+) as a cofactor with the same evidence code."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not supplied to the evaluated model.",
    "The source supports the expected answer but does not make it the only defensible choice under the wording."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both [2Fe-2S] cluster and Mg(2+) are listed as cofactors for the matched protein with experimental evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated protein, and the source records a [2Fe-2S] cluster as a cofactor with experimental evidence code ECO:0000269. The source also records Mg(2+) as a cofactor with the same evidence code.",
    "evidence_ids": ["C1", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features might suggest an iron-sulfur protein, but they do not establish the specific cofactor requirements or distinguish the [2Fe-2S] annotation from the separately annotated Mg(2+).",
    "missing_item_specific_fact": "The protein-specific cofactor annotations or experimental characterization are absent from the input.",
    "reason": "The sequence alone does not provide a clear basis for selecting one cofactor, particularly because the matched protein is annotated with both [2Fe-2S] and Mg(2+)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both [2Fe-2S] cluster and Mg(2+) are listed as cofactors for the matched protein with experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not supplied to the evaluated model.",
    "The source supports the expected answer but does not make it the only defensible choice under the wording."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q0CPG9 (DHAD astD, EC 4.2.1.9) annotates &#91;2Fe-2S&#93; cluster as a cofactor with ECO:0000269 (inferred from direct assay, PubMed:29995859), stating 'Binds 1 &#91;2Fe-2S&#93; cluster per subunit.' The expected answer C is therefore scientifically supported. However, the same entry also annotates Mg(2+) as a cofactor with the identical evidence level (ECO:0000269, same PubMed reference). The &#91;2Fe-2S&#93; cluster is correct but not the sole cofactor.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence corresponds to a dihydroxy-acid dehydratase (DHAD/ILV3 family, EC 4.2.1.9), identifiable from conserved motifs in the branched-chain amino acid biosynthesis pathway. Members of the DHAD/ILV3 family are well-characterized in biochemistry as requiring a &#91;2Fe-2S&#93; cluster for catalysis, distinguishing them from enzymes that use &#91;4Fe-4S&#93; clusters (e.g., aconitase, radical SAM enzymes) or FAD-dependent oxidoreductases. A knowledgeable biologist could reason from the DHAD family assignment to the &#91;2Fe-2S&#93; answer over &#91;4Fe-4S&#93; and FAD.


**Missing item-specific fact**

> The critical unresolved issue is that Mg(2+) is also an experimentally confirmed cofactor for this exact enzyme (same ECO:0000269 evidence). Distinguishing &#91;2Fe-2S&#93; from Mg(2+) as 'the' cofactor requires knowing which one the question intends as the answer, since both are required. Family-level knowledge that DHAD uses &#91;2Fe-2S&#93; helps exclude FAD and &#91;4Fe-4S&#93;, but does not uniquely exclude Mg(2+).


**Reason**

> The DHAD/ILV3 family assignment provides a general biological argument to favor &#91;2Fe-2S&#93; over FAD and &#91;4Fe-4S&#93;. However, the question's phrasing 'the specific cofactor' (singular) is ambiguous because the enzyme requires both &#91;2Fe-2S&#93; and Mg(2+). Reasoning can narrow from four choices to two (C and D), but cannot definitively select C over D without an implicit convention that the metal-cluster cofactor is 'the' answer over a ubiquitous divalent cation. This is a borderline case: the &#91;2Fe-2S&#93; vs &#91;4Fe-4S&#93; vs FAD discrimination is reasoning-supported via family knowledge, but the &#91;2Fe-2S&#93; vs Mg(2+) discrimination relies on an unstated convention.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The UniProt entry lists both &#91;2Fe-2S&#93; cluster and Mg(2+) as cofactors with identical experimental evidence (ECO:0000269, PubMed:29995859). The question asks for 'the specific cofactor' in the singular, but the enzyme requires both. Choice D (Mg(2+)) is equally defensible as a required cofactor. The question would be unambiguous if it asked for 'the iron-sulfur cluster type' or explicitly excluded metal-ion cofactors.


### Important caveats

- Both &#91;2Fe-2S&#93; and Mg(2+) are annotated cofactors with the same evidence level (ECO:0000269, direct assay from PubMed:29995859). The expected answer is correct but not uniquely so given the question wording.
- The &#91;2Fe-2S&#93; annotation note ('Binds 1 &#91;2Fe-2S&#93; cluster per subunit') carries a secondary evidence code ECO:0000250 (similarity to P39522), while the primary &#91;2Fe-2S&#93; cofactor claim is ECO:0000269.
- The DHAD/ILV3 family's use of &#91;2Fe-2S&#93; is well-established general biochemistry, making the &#91;2Fe-2S&#93; vs &#91;4Fe-4S&#93; and FAD discrimination reasoning-supported. The &#91;2Fe-2S&#93; vs Mg(2+) discrimination is not cleanly resolvable by reasoning alone.
- Sequence identity is confirmed: the benchmark sequence (598 aa, SHA-256 fa9e543b...) matches UniProt Q0CPG9 exactly in both current and historical (v90) snapshots.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence corresponds to a dihydroxy-acid dehydratase (DHAD/ILV3 family, EC 4.2.1.9), identifiable from conserved motifs in the branched-chain amino acid biosynthesis pathway. Members of the DHAD/ILV3 family are well-characterized in biochemistry as requiring a [2Fe-2S] cluster for catalysis, distinguishing them from enzymes that use [4Fe-4S] clusters (e.g., aconitase, radical SAM enzymes) or FAD-dependent oxidoreductases. A knowledgeable biologist could reason from the DHAD family assignment to the [2Fe-2S] answer over [4Fe-4S] and FAD.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The critical unresolved issue is that Mg(2+) is also an experimentally confirmed cofactor for this exact enzyme (same ECO:0000269 evidence). Distinguishing [2Fe-2S] from Mg(2+) as 'the' cofactor requires knowing which one the question intends as the answer, since both are required. Family-level knowledge that DHAD uses [2Fe-2S] helps exclude FAD and [4Fe-4S], but does not uniquely exclude Mg(2+).",
    "reason": "The DHAD/ILV3 family assignment provides a general biological argument to favor [2Fe-2S] over FAD and [4Fe-4S]. However, the question's phrasing 'the specific cofactor' (singular) is ambiguous because the enzyme requires both [2Fe-2S] and Mg(2+). Reasoning can narrow from four choices to two (C and D), but cannot definitively select C over D without an implicit convention that the metal-cluster cofactor is 'the' answer over a ubiquitous divalent cation. This is a borderline case: the [2Fe-2S] vs [4Fe-4S] vs FAD discrimination is reasoning-supported via family knowledge, but the [2Fe-2S] vs Mg(2+) discrimination relies on an unstated convention."
  },
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG9 (DHAD astD, EC 4.2.1.9) annotates [2Fe-2S] cluster as a cofactor with ECO:0000269 (inferred from direct assay, PubMed:29995859), stating 'Binds 1 [2Fe-2S] cluster per subunit.' The expected answer C is therefore scientifically supported. However, the same entry also annotates Mg(2+) as a cofactor with the identical evidence level (ECO:0000269, same PubMed reference). The [2Fe-2S] cluster is correct but not the sole cofactor."
  },
  "important_caveats": [
    "Both [2Fe-2S] and Mg(2+) are annotated cofactors with the same evidence level (ECO:0000269, direct assay from PubMed:29995859). The expected answer is correct but not uniquely so given the question wording.",
    "The [2Fe-2S] annotation note ('Binds 1 [2Fe-2S] cluster per subunit') carries a secondary evidence code ECO:0000250 (similarity to P39522), while the primary [2Fe-2S] cofactor claim is ECO:0000269.",
    "The DHAD/ILV3 family's use of [2Fe-2S] is well-established general biochemistry, making the [2Fe-2S] vs [4Fe-4S] and FAD discrimination reasoning-supported. The [2Fe-2S] vs Mg(2+) discrimination is not cleanly resolvable by reasoning alone.",
    "Sequence identity is confirmed: the benchmark sequence (598 aa, SHA-256 fa9e543b...) matches UniProt Q0CPG9 exactly in both current and historical (v90) snapshots."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The UniProt entry lists both [2Fe-2S] cluster and Mg(2+) as cofactors with identical experimental evidence (ECO:0000269, PubMed:29995859). The question asks for 'the specific cofactor' in the singular, but the enzyme requires both. Choice D (Mg(2+)) is equally defensible as a required cofactor. The question would be unambiguous if it asked for 'the iron-sulfur cluster type' or explicitly excluded metal-ion cofactors."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG9 (DHAD astD, EC 4.2.1.9) annotates [2Fe-2S] cluster as a cofactor with ECO:0000269 (inferred from direct assay, PubMed:29995859), stating 'Binds 1 [2Fe-2S] cluster per subunit.' The expected answer C is therefore scientifically supported. However, the same entry also annotates Mg(2+) as a cofactor with the identical evidence level (ECO:0000269, same PubMed reference). The [2Fe-2S] cluster is correct but not the sole cofactor.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence corresponds to a dihydroxy-acid dehydratase (DHAD/ILV3 family, EC 4.2.1.9), identifiable from conserved motifs in the branched-chain amino acid biosynthesis pathway. Members of the DHAD/ILV3 family are well-characterized in biochemistry as requiring a [2Fe-2S] cluster for catalysis, distinguishing them from enzymes that use [4Fe-4S] clusters (e.g., aconitase, radical SAM enzymes) or FAD-dependent oxidoreductases. A knowledgeable biologist could reason from the DHAD family assignment to the [2Fe-2S] answer over [4Fe-4S] and FAD.",
    "missing_item_specific_fact": "The critical unresolved issue is that Mg(2+) is also an experimentally confirmed cofactor for this exact enzyme (same ECO:0000269 evidence). Distinguishing [2Fe-2S] from Mg(2+) as 'the' cofactor requires knowing which one the question intends as the answer, since both are required. Family-level knowledge that DHAD uses [2Fe-2S] helps exclude FAD and [4Fe-4S], but does not uniquely exclude Mg(2+).",
    "reason": "The DHAD/ILV3 family assignment provides a general biological argument to favor [2Fe-2S] over FAD and [4Fe-4S]. However, the question's phrasing 'the specific cofactor' (singular) is ambiguous because the enzyme requires both [2Fe-2S] and Mg(2+). Reasoning can narrow from four choices to two (C and D), but cannot definitively select C over D without an implicit convention that the metal-cluster cofactor is 'the' answer over a ubiquitous divalent cation. This is a borderline case: the [2Fe-2S] vs [4Fe-4S] vs FAD discrimination is reasoning-supported via family knowledge, but the [2Fe-2S] vs Mg(2+) discrimination relies on an unstated convention."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The UniProt entry lists both [2Fe-2S] cluster and Mg(2+) as cofactors with identical experimental evidence (ECO:0000269, PubMed:29995859). The question asks for 'the specific cofactor' in the singular, but the enzyme requires both. Choice D (Mg(2+)) is equally defensible as a required cofactor. The question would be unambiguous if it asked for 'the iron-sulfur cluster type' or explicitly excluded metal-ion cofactors."
  },
  "important_caveats": [
    "Both [2Fe-2S] and Mg(2+) are annotated cofactors with the same evidence level (ECO:0000269, direct assay from PubMed:29995859). The expected answer is correct but not uniquely so given the question wording.",
    "The [2Fe-2S] annotation note ('Binds 1 [2Fe-2S] cluster per subunit') carries a secondary evidence code ECO:0000250 (similarity to P39522), while the primary [2Fe-2S] cofactor claim is ECO:0000269.",
    "The DHAD/ILV3 family's use of [2Fe-2S] is well-established general biochemistry, making the [2Fe-2S] vs [4Fe-4S] and FAD discrimination reasoning-supported. The [2Fe-2S] vs Mg(2+) discrimination is not cleanly resolvable by reasoning alone.",
    "Sequence identity is confirmed: the benchmark sequence (598 aa, SHA-256 fa9e543b...) matches UniProt Q0CPG9 exactly in both current and historical (v90) snapshots."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched records identify a &#91;2Fe-2S&#93; cluster as a cofactor, with experimental evidence cited, so choice C is supported. The same records also list Mg(2+), making C non-exclusive.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence’s Cys-rich region and enzyme-like architecture are consistent with an IlvD/dihydroxy-acid-dehydratase family protein. Transferable knowledge of this family’s iron-sulfur cofactor gives a meaningful basis for choosing &#91;2Fe-2S&#93; over FAD or Mg(2+) alone; the family association also argues against &#91;4Fe-4S&#93; as the cluster choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition can support choice C without access to this protein’s exact database record. However, that does not make C the only defensible answer: Mg(2+) is also listed as a cofactor for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The sequence-matched evidence lists both a &#91;2Fe-2S&#93; cluster and Mg(2+) as cofactors. The singular wording and choices do not distinguish between these two.


### Important caveats

- The reviewer-only evidence supports both cofactors, but the original input did not provide the protein’s name or database annotation.
- The family-based sequence inference supports the iron-sulfur choice; it does not independently establish the exact cofactor requirements or conditions for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s Cys-rich region and enzyme-like architecture are consistent with an IlvD/dihydroxy-acid-dehydratase family protein. Transferable knowledge of this family’s iron-sulfur cofactor gives a meaningful basis for choosing [2Fe-2S] over FAD or Mg(2+) alone; the family association also argues against [4Fe-4S] as the cluster choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition can support choice C without access to this protein’s exact database record. However, that does not make C the only defensible answer: Mg(2+) is also listed as a cofactor for this protein."
  },
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched records identify a [2Fe-2S] cluster as a cofactor, with experimental evidence cited, so choice C is supported. The same records also list Mg(2+), making C non-exclusive."
  },
  "important_caveats": [
    "The reviewer-only evidence supports both cofactors, but the original input did not provide the protein’s name or database annotation.",
    "The family-based sequence inference supports the iron-sulfur choice; it does not independently establish the exact cofactor requirements or conditions for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The sequence-matched evidence lists both a [2Fe-2S] cluster and Mg(2+) as cofactors. The singular wording and choices do not distinguish between these two."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched records identify a [2Fe-2S] cluster as a cofactor, with experimental evidence cited, so choice C is supported. The same records also list Mg(2+), making C non-exclusive.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence’s Cys-rich region and enzyme-like architecture are consistent with an IlvD/dihydroxy-acid-dehydratase family protein. Transferable knowledge of this family’s iron-sulfur cofactor gives a meaningful basis for choosing [2Fe-2S] over FAD or Mg(2+) alone; the family association also argues against [4Fe-4S] as the cluster choice.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition can support choice C without access to this protein’s exact database record. However, that does not make C the only defensible answer: Mg(2+) is also listed as a cofactor for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The sequence-matched evidence lists both a [2Fe-2S] cluster and Mg(2+) as cofactors. The singular wording and choices do not distinguish between these two."
  },
  "important_caveats": [
    "The reviewer-only evidence supports both cofactors, but the original input did not provide the protein’s name or database annotation.",
    "The family-based sequence inference supports the iron-sulfur choice; it does not independently establish the exact cofactor requirements or conditions for this specific protein."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q0CPG9) explicitly annotates a &#91;2Fe-2S&#93; cluster as a cofactor with experimental evidence (ECO:0000269|PubMed:29995859), stating 'Binds 1 &#91;2Fe-2S&#93; cluster per subunit' (evidence C5, H4). The protein is identified as dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9), a well-characterized enzyme family whose defining catalytic cofactor is the &#91;2Fe-2S&#93; cluster. Note that Mg(2+) is also annotated as a cofactor (C6, H5), but the &#91;2Fe-2S&#93; cluster is the primary, mechanistically essential cofactor for DHAD catalysis.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region of the sequence contains multiple cysteine residues at positions consistent with &#91;2Fe-2S&#93; coordination in the DHAD family: C in 'NPCNMHLHDLS' (~pos 75), C in 'GCDKNMPG' (~pos 143), C in 'GRGACGGMYTANT' (~pos 215), and C in 'GSSSCPADDPKK' (~pos 240). The spacing pattern (~68-72-25 residues) is characteristic of &#91;2Fe-2S&#93; tetrahedral cysteine ligation in DHAD, distinct from the CxxC...CxxC motifs typical of &#91;4Fe-4S&#93; radical SAM enzymes. The overall ~600-residue architecture with an N-terminal cluster-binding domain and a C-terminal catalytic domain matches the DHAD fold. DHAD (EC 4.2.1.9) is a well-known enzyme family whose hallmark is the &#91;2Fe-2S&#93; cluster required for radical-based dehydration catalysis. FAD would require a Rossmann fold (GxGxxG motif) which is absent. Mg(2+) alone cannot explain the cysteine-rich N-terminal region. The distinction between &#91;2Fe-2S&#93; and &#91;4Fe-4S&#93; follows from the cysteine spacing pattern and the DHAD family identity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the DHAD family architecture and the characteristic &#91;2Fe-2S&#93; cysteine ligation pattern in the N-terminal region can distinguish option C from A (&#91;4Fe-4S&#93; has different Cys spacing), B (FAD requires Rossmann fold), and D (Mg2+ alone doesn't explain the Cys cluster). The DHAD family's &#91;2Fe-2S&#93; dependence is a well-established, transferable biochemical fact learned from E. coli IlvD and other homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The UniProt entry annotates both &#91;2Fe-2S&#93; cluster and Mg(2+) as cofactors for this protein (C5 and C6). The question asks for 'the specific cofactor' (singular), but both are experimentally verified cofactors. However, &#91;2Fe-2S&#93; is the more distinctive and mechanistically essential cofactor that defines DHAD's catalytic mechanism, while Mg2+ plays a more auxiliary structural/electrostatic role. In standard biochemistry pedagogy, &#91;2Fe-2S&#93; is considered THE cofactor of DHAD. The ambiguity is mild because the &#91;2Fe-2S&#93; cluster is the defining cofactor that distinguishes DHAD from most other enzymes.


### Important caveats

- The UniProt entry lists both &#91;2Fe-2S&#93; cluster and Mg(2+) as cofactors; the question's singular phrasing ('the specific cofactor') slightly favors &#91;2Fe-2S&#93; as the defining cofactor but creates mild ambiguity with Mg(2+).
- The &#91;2Fe-2S&#93; annotation carries experimental evidence (ECO:0000269, PubMed:29995859) plus a similarity-based note referencing E. coli DHAD (P39522, ECO:0000250).
- The entry was first publicly released in April 2025; the author's source snapshot date is unknown, though the sequence itself dates to 2006.
- The protein is a mitochondrial precursor (Flags: Precursor), which is consistent with DHAD localization in fungi.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region of the sequence contains multiple cysteine residues at positions consistent with [2Fe-2S] coordination in the DHAD family: C in 'NPCNMHLHDLS' (~pos 75), C in 'GCDKNMPG' (~pos 143), C in 'GRGACGGMYTANT' (~pos 215), and C in 'GSSSCPADDPKK' (~pos 240). The spacing pattern (~68-72-25 residues) is characteristic of [2Fe-2S] tetrahedral cysteine ligation in DHAD, distinct from the CxxC...CxxC motifs typical of [4Fe-4S] radical SAM enzymes. The overall ~600-residue architecture with an N-terminal cluster-binding domain and a C-terminal catalytic domain matches the DHAD fold. DHAD (EC 4.2.1.9) is a well-known enzyme family whose hallmark is the [2Fe-2S] cluster required for radical-based dehydration catalysis. FAD would require a Rossmann fold (GxGxxG motif) which is absent. Mg(2+) alone cannot explain the cysteine-rich N-terminal region. The distinction between [2Fe-2S] and [4Fe-4S] follows from the cysteine spacing pattern and the DHAD family identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the DHAD family architecture and the characteristic [2Fe-2S] cysteine ligation pattern in the N-terminal region can distinguish option C from A ([4Fe-4S] has different Cys spacing), B (FAD requires Rossmann fold), and D (Mg2+ alone doesn't explain the Cys cluster). The DHAD family's [2Fe-2S] dependence is a well-established, transferable biochemical fact learned from E. coli IlvD and other homologs."
  },
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q0CPG9) explicitly annotates a [2Fe-2S] cluster as a cofactor with experimental evidence (ECO:0000269|PubMed:29995859), stating 'Binds 1 [2Fe-2S] cluster per subunit' (evidence C5, H4). The protein is identified as dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9), a well-characterized enzyme family whose defining catalytic cofactor is the [2Fe-2S] cluster. Note that Mg(2+) is also annotated as a cofactor (C6, H5), but the [2Fe-2S] cluster is the primary, mechanistically essential cofactor for DHAD catalysis."
  },
  "important_caveats": [
    "The UniProt entry lists both [2Fe-2S] cluster and Mg(2+) as cofactors; the question's singular phrasing ('the specific cofactor') slightly favors [2Fe-2S] as the defining cofactor but creates mild ambiguity with Mg(2+).",
    "The [2Fe-2S] annotation carries experimental evidence (ECO:0000269, PubMed:29995859) plus a similarity-based note referencing E. coli DHAD (P39522, ECO:0000250).",
    "The entry was first publicly released in April 2025; the author's source snapshot date is unknown, though the sequence itself dates to 2006.",
    "The protein is a mitochondrial precursor (Flags: Precursor), which is consistent with DHAD localization in fungi."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The UniProt entry annotates both [2Fe-2S] cluster and Mg(2+) as cofactors for this protein (C5 and C6). The question asks for 'the specific cofactor' (singular), but both are experimentally verified cofactors. However, [2Fe-2S] is the more distinctive and mechanistically essential cofactor that defines DHAD's catalytic mechanism, while Mg2+ plays a more auxiliary structural/electrostatic role. In standard biochemistry pedagogy, [2Fe-2S] is considered THE cofactor of DHAD. The ambiguity is mild because the [2Fe-2S] cluster is the defining cofactor that distinguishes DHAD from most other enzymes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q0CPG9) explicitly annotates a [2Fe-2S] cluster as a cofactor with experimental evidence (ECO:0000269|PubMed:29995859), stating 'Binds 1 [2Fe-2S] cluster per subunit' (evidence C5, H4). The protein is identified as dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9), a well-characterized enzyme family whose defining catalytic cofactor is the [2Fe-2S] cluster. Note that Mg(2+) is also annotated as a cofactor (C6, H5), but the [2Fe-2S] cluster is the primary, mechanistically essential cofactor for DHAD catalysis.",
    "evidence_ids": ["C5", "H4", "C4", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region of the sequence contains multiple cysteine residues at positions consistent with [2Fe-2S] coordination in the DHAD family: C in 'NPCNMHLHDLS' (~pos 75), C in 'GCDKNMPG' (~pos 143), C in 'GRGACGGMYTANT' (~pos 215), and C in 'GSSSCPADDPKK' (~pos 240). The spacing pattern (~68-72-25 residues) is characteristic of [2Fe-2S] tetrahedral cysteine ligation in DHAD, distinct from the CxxC...CxxC motifs typical of [4Fe-4S] radical SAM enzymes. The overall ~600-residue architecture with an N-terminal cluster-binding domain and a C-terminal catalytic domain matches the DHAD fold. DHAD (EC 4.2.1.9) is a well-known enzyme family whose hallmark is the [2Fe-2S] cluster required for radical-based dehydration catalysis. FAD would require a Rossmann fold (GxGxxG motif) which is absent. Mg(2+) alone cannot explain the cysteine-rich N-terminal region. The distinction between [2Fe-2S] and [4Fe-4S] follows from the cysteine spacing pattern and the DHAD family identity.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the DHAD family architecture and the characteristic [2Fe-2S] cysteine ligation pattern in the N-terminal region can distinguish option C from A ([4Fe-4S] has different Cys spacing), B (FAD requires Rossmann fold), and D (Mg2+ alone doesn't explain the Cys cluster). The DHAD family's [2Fe-2S] dependence is a well-established, transferable biochemical fact learned from E. coli IlvD and other homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The UniProt entry annotates both [2Fe-2S] cluster and Mg(2+) as cofactors for this protein (C5 and C6). The question asks for 'the specific cofactor' (singular), but both are experimentally verified cofactors. However, [2Fe-2S] is the more distinctive and mechanistically essential cofactor that defines DHAD's catalytic mechanism, while Mg2+ plays a more auxiliary structural/electrostatic role. In standard biochemistry pedagogy, [2Fe-2S] is considered THE cofactor of DHAD. The ambiguity is mild because the [2Fe-2S] cluster is the defining cofactor that distinguishes DHAD from most other enzymes."
  },
  "important_caveats": [
    "The UniProt entry lists both [2Fe-2S] cluster and Mg(2+) as cofactors; the question's singular phrasing ('the specific cofactor') slightly favors [2Fe-2S] as the defining cofactor but creates mild ambiguity with Mg(2+).",
    "The [2Fe-2S] annotation carries experimental evidence (ECO:0000269, PubMed:29995859) plus a similarity-based note referencing E. coli DHAD (P39522, ECO:0000250).",
    "The entry was first publicly released in April 2025; the author's source snapshot date is unknown, though the sequence itself dates to 2006.",
    "The protein is a mitochondrial precursor (Flags: Precursor), which is consistent with DHAD localization in fungi."
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
  "requested_accession": "Q0CPG9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "benchmark_sequence_length": 598,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_source_sequence_length": 598,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 90,
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_source_sequence_length": 598,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"name\":\"[2Fe-2S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P39522\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 [2Fe-2S] cluster per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 29-37",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 66-70",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;\nCC         Evidence={ECO:0000269|PubMed:29995859};\nCC       Note=Binds 1 [2Fe-2S] cluster per subunit.\nCC       {ECO:0000250|UniProtKB:P39522};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 71-73",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000269|PubMed:29995859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
