# active_site_0109: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0109.txt)

**Task:** `active_site`  
**Author key, unchanged:** **A** — Position 213 (Proton donor)

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
MVSSKELPPSTVPFFPNQFFRNQFRSKPQYPPPNTNLSEKVAIISGGNTGLGFEAATQLLSFKLGTLILAVRSTAKGEAAASKLRARYPKATIHVWKLDMSSYDSIQEFAGRVNTQLPRLDMVILNAGVSKLEFGTVSSTGHEETVQINYLSTALLAILLLPALKSKSPPGIPGRLTIVSAALTLVAKFPNRDESPLLPSFDNPKYWDPNDQYCSSKLLMHLFLWKLVDYISADDVIVNLADPGFVKGTELARDVSGGQRVGLSIFASLTGRNKKHGASTYVDAVVNKGKESHGGFIMSWQIHPYPTLLYTSEGQQITERLWDETLAEFEFANVRGIIESMKGN

[Multiple Choices]
A. Position 213 (Proton donor)
B. Position 422 (Nucleophile)
C. Position 318 (For beta-ketoacyl synthase activity)
D. Position 209 (Proton donor)
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

> The sequence matches the UniProt entry, whose active-site annotation identifies position 213 as the proton donor. The annotation is transferred by similarity from UniProtKB:O93868, so it supports the key as a database annotation but is not direct experimental evidence for this protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The supplied sequence may help identify a dehydrogenase-like enzyme, but it does not provide a reliable general biological argument for choosing the exact proton-donor position 213 over nearby position 209.


**Missing item-specific fact**

> The protein-specific active-site annotation assigning the proton-donor role to position 213, transferred from a homolog.


**Reason**

> Choosing the keyed residue requires a protein-specific annotation or equivalent evidence not supplied in the question; recognizing the sequence or consulting a predictor would not make the answer reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports A specifically. B is beyond the 344-residue sequence, and the evidence does not support D or C.


### Important caveats

- The active-site assignment is based on similarity evidence (ECO:0000250), not demonstrated here as an experiment on the supplied protein.
- The historical UniProt record matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence may help identify a dehydrogenase-like enzyme, but it does not provide a reliable general biological argument for choosing the exact proton-donor position 213 over nearby position 209.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning the proton-donor role to position 213, transferred from a homolog.",
    "reason": "Choosing the keyed residue requires a protein-specific annotation or equivalent evidence not supplied in the question; recognizing the sequence or consulting a predictor would not make the answer reasoning-supported."
  },
  "case_id": "active_site_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose active-site annotation identifies position 213 as the proton donor. The annotation is transferred by similarity from UniProtKB:O93868, so it supports the key as a database annotation but is not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The active-site assignment is based on similarity evidence (ECO:0000250), not demonstrated here as an experiment on the supplied protein.",
    "The historical UniProt record matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports A specifically. B is beyond the 344-residue sequence, and the evidence does not support D or C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose active-site annotation identifies position 213 as the proton donor. The annotation is transferred by similarity from UniProtKB:O93868, so it supports the key as a database annotation but is not direct experimental evidence for this protein.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The supplied sequence may help identify a dehydrogenase-like enzyme, but it does not provide a reliable general biological argument for choosing the exact proton-donor position 213 over nearby position 209.",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning the proton-donor role to position 213, transferred from a homolog.",
    "reason": "Choosing the keyed residue requires a protein-specific annotation or equivalent evidence not supplied in the question; recognizing the sequence or consulting a predictor would not make the answer reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports A specifically. B is beyond the 344-residue sequence, and the evidence does not support D or C."
  },
  "important_caveats": [
    "The active-site assignment is based on similarity evidence (ECO:0000250), not demonstrated here as an experiment on the supplied protein.",
    "The historical UniProt record matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5, H3) explicitly lists ACT_SITE 213 as 'Proton donor' with evidence ECO:0000250 (inferred by similarity to O93868, another SDR). The residue at position 213 in the supplied sequence is Y (Tyrosine), consistent with the canonical SDR catalytic Tyr-X-X-X-Lys tetrad (Y213-C214-S215-S216-K217). The annotation is computational inference from a homolog rather than direct experimental data, but the SDR catalytic mechanism is extremely well-established across hundreds of characterized enzymes. The expected answer matches the database annotation and the sequence context.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable NAD(P)-binding Rossmann fold motif (GGNTG at ~47-51, G at 76, G at 99, G at 126), identifying the protein as a member of the short-chain dehydrogenase/reductase (SDR) superfamily. SDRs possess a universally conserved catalytic tetrad: Tyr-X-X-X-Lys, where Tyr serves as the proton donor and Lys lowers the pKa of the catalytic Tyr. Scanning the sequence reveals the motif Y(213)-C(214)-S(215)-S(216)-K(217), perfectly matching the Tyr-X-X-X-Lys pattern. Position 213 (Tyr) is therefore the proton donor. Distractor B (position 422) exceeds the protein length of 344 AA; distractor C (position 318 = Ile) is irrelevant to SDR catalysis and references a different enzyme class; distractor D (position 209 = Asp) does not fit the SDR catalytic tetrad.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SDR catalytic mechanism (Tyr-X-X-X-Lys tetrad with Tyr as proton donor) is standard textbook biochemistry. The motif is directly identifiable from the supplied sequence. Recognizing the SDR fold from the NAD(P)-binding region and locating the Tyr-X-X-X-Lys motif constitutes a concrete biological argument that distinguishes position 213 from the alternatives without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B references a non-existent position (422 > 344 AA). Option C references an unrelated enzyme class (beta-ketoacyl synthase) and position 318 is Ile. Option D (position 209 = Asp) does not match the SDR catalytic tetrad. Only option A correctly identifies the Tyr in the canonical Tyr-X-X-X-Lys motif as the proton donor.


### Important caveats

- The UniProt annotation for this active site carries evidence code ECO:0000250 (inferred by similarity to O93868), meaning it is computational transfer rather than direct experimental measurement for this specific protein.
- The protein was annotated in April 2025 based on a 2024 functional study (PubMed:38404388); the active site annotation itself is transferred by similarity, not directly assayed.
- The SDR Tyr-X-X-X-Lys catalytic mechanism is supported by extensive structural and biochemical literature across many family members, lending strong indirect support to the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable NAD(P)-binding Rossmann fold motif (GGNTG at ~47-51, G at 76, G at 99, G at 126), identifying the protein as a member of the short-chain dehydrogenase/reductase (SDR) superfamily. SDRs possess a universally conserved catalytic tetrad: Tyr-X-X-X-Lys, where Tyr serves as the proton donor and Lys lowers the pKa of the catalytic Tyr. Scanning the sequence reveals the motif Y(213)-C(214)-S(215)-S(216)-K(217), perfectly matching the Tyr-X-X-X-Lys pattern. Position 213 (Tyr) is therefore the proton donor. Distractor B (position 422) exceeds the protein length of 344 AA; distractor C (position 318 = Ile) is irrelevant to SDR catalysis and references a different enzyme class; distractor D (position 209 = Asp) does not fit the SDR catalytic tetrad.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SDR catalytic mechanism (Tyr-X-X-X-Lys tetrad with Tyr as proton donor) is standard textbook biochemistry. The motif is directly identifiable from the supplied sequence. Recognizing the SDR fold from the NAD(P)-binding region and locating the Tyr-X-X-X-Lys motif constitutes a concrete biological argument that distinguishes position 213 from the alternatives without requiring memorization of this specific protein's database entry."
  },
  "case_id": "active_site_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) explicitly lists ACT_SITE 213 as 'Proton donor' with evidence ECO:0000250 (inferred by similarity to O93868, another SDR). The residue at position 213 in the supplied sequence is Y (Tyrosine), consistent with the canonical SDR catalytic Tyr-X-X-X-Lys tetrad (Y213-C214-S215-S216-K217). The annotation is computational inference from a homolog rather than direct experimental data, but the SDR catalytic mechanism is extremely well-established across hundreds of characterized enzymes. The expected answer matches the database annotation and the sequence context."
  },
  "important_caveats": [
    "The UniProt annotation for this active site carries evidence code ECO:0000250 (inferred by similarity to O93868), meaning it is computational transfer rather than direct experimental measurement for this specific protein.",
    "The protein was annotated in April 2025 based on a 2024 functional study (PubMed:38404388); the active site annotation itself is transferred by similarity, not directly assayed.",
    "The SDR Tyr-X-X-X-Lys catalytic mechanism is supported by extensive structural and biochemical literature across many family members, lending strong indirect support to the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B references a non-existent position (422 > 344 AA). Option C references an unrelated enzyme class (beta-ketoacyl synthase) and position 318 is Ile. Option D (position 209 = Asp) does not match the SDR catalytic tetrad. Only option A correctly identifies the Tyr in the canonical Tyr-X-X-X-Lys motif as the proton donor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) explicitly lists ACT_SITE 213 as 'Proton donor' with evidence ECO:0000250 (inferred by similarity to O93868, another SDR). The residue at position 213 in the supplied sequence is Y (Tyrosine), consistent with the canonical SDR catalytic Tyr-X-X-X-Lys tetrad (Y213-C214-S215-S216-K217). The annotation is computational inference from a homolog rather than direct experimental data, but the SDR catalytic mechanism is extremely well-established across hundreds of characterized enzymes. The expected answer matches the database annotation and the sequence context.",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable NAD(P)-binding Rossmann fold motif (GGNTG at ~47-51, G at 76, G at 99, G at 126), identifying the protein as a member of the short-chain dehydrogenase/reductase (SDR) superfamily. SDRs possess a universally conserved catalytic tetrad: Tyr-X-X-X-Lys, where Tyr serves as the proton donor and Lys lowers the pKa of the catalytic Tyr. Scanning the sequence reveals the motif Y(213)-C(214)-S(215)-S(216)-K(217), perfectly matching the Tyr-X-X-X-Lys pattern. Position 213 (Tyr) is therefore the proton donor. Distractor B (position 422) exceeds the protein length of 344 AA; distractor C (position 318 = Ile) is irrelevant to SDR catalysis and references a different enzyme class; distractor D (position 209 = Asp) does not fit the SDR catalytic tetrad.",
    "missing_item_specific_fact": "",
    "reason": "The SDR catalytic mechanism (Tyr-X-X-X-Lys tetrad with Tyr as proton donor) is standard textbook biochemistry. The motif is directly identifiable from the supplied sequence. Recognizing the SDR fold from the NAD(P)-binding region and locating the Tyr-X-X-X-Lys motif constitutes a concrete biological argument that distinguishes position 213 from the alternatives without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B references a non-existent position (422 > 344 AA). Option C references an unrelated enzyme class (beta-ketoacyl synthase) and position 318 is Ile. Option D (position 209 = Asp) does not match the SDR catalytic tetrad. Only option A correctly identifies the Tyr in the canonical Tyr-X-X-X-Lys motif as the proton donor."
  },
  "important_caveats": [
    "The UniProt annotation for this active site carries evidence code ECO:0000250 (inferred by similarity to O93868), meaning it is computational transfer rather than direct experimental measurement for this specific protein.",
    "The protein was annotated in April 2025 based on a 2024 functional study (PubMed:38404388); the active site annotation itself is transferred by similarity, not directly assayed.",
    "The SDR Tyr-X-X-X-Lys catalytic mechanism is supported by extensive structural and biochemical literature across many family members, lending strong indirect support to the annotation."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched-sequence UniProt annotation identifies position 213 as the proton donor. Its evidence is transferred from a related UniProt entry (ECO:0000250), so this supports the key as a homology-based annotation rather than direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a glycine-rich N-terminal pattern consistent with an NAD(P)-dependent short-chain dehydrogenase/reductase, and contains a Tyr-X-X-X-Lys motif at positions 213–217. In SDR enzymes, the catalytic Tyr commonly acts as the proton donor, while the nearby Lys helps tune its pKa. This favors position 213 over the nearby alternative at 209; position 422 is beyond the 344-residue sequence, and the beta-ketoacyl synthase option does not fit this family-level pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable SDR family knowledge and the sequence motif provide a meaningful basis for distinguishing the offered options, though they do not substitute for direct experimental verification of this protein’s catalytic role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The nearby-position alternatives are distinguishable from the sequence: the conserved Tyr-X-X-X-Lys motif places the likely catalytic proton-donor Tyr at position 213, not 209.


### Important caveats

- The supporting database annotation is explicitly transferred by similarity; direct experimental confirmation for this exact protein is not established by the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich N-terminal pattern consistent with an NAD(P)-dependent short-chain dehydrogenase/reductase, and contains a Tyr-X-X-X-Lys motif at positions 213–217. In SDR enzymes, the catalytic Tyr commonly acts as the proton donor, while the nearby Lys helps tune its pKa. This favors position 213 over the nearby alternative at 209; position 422 is beyond the 344-residue sequence, and the beta-ketoacyl synthase option does not fit this family-level pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable SDR family knowledge and the sequence motif provide a meaningful basis for distinguishing the offered options, though they do not substitute for direct experimental verification of this protein’s catalytic role."
  },
  "case_id": "active_site_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 213 as the proton donor. Its evidence is transferred from a related UniProt entry (ECO:0000250), so this supports the key as a homology-based annotation rather than direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supporting database annotation is explicitly transferred by similarity; direct experimental confirmation for this exact protein is not established by the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nearby-position alternatives are distinguishable from the sequence: the conserved Tyr-X-X-X-Lys motif places the likely catalytic proton-donor Tyr at position 213, not 209."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 213 as the proton donor. Its evidence is transferred from a related UniProt entry (ECO:0000250), so this supports the key as a homology-based annotation rather than direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a glycine-rich N-terminal pattern consistent with an NAD(P)-dependent short-chain dehydrogenase/reductase, and contains a Tyr-X-X-X-Lys motif at positions 213–217. In SDR enzymes, the catalytic Tyr commonly acts as the proton donor, while the nearby Lys helps tune its pKa. This favors position 213 over the nearby alternative at 209; position 422 is beyond the 344-residue sequence, and the beta-ketoacyl synthase option does not fit this family-level pattern.",
    "missing_item_specific_fact": "",
    "reason": "Transferable SDR family knowledge and the sequence motif provide a meaningful basis for distinguishing the offered options, though they do not substitute for direct experimental verification of this protein’s catalytic role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nearby-position alternatives are distinguishable from the sequence: the conserved Tyr-X-X-X-Lys motif places the likely catalytic proton-donor Tyr at position 213, not 209."
  },
  "important_caveats": [
    "The supporting database annotation is explicitly transferred by similarity; direct experimental confirmation for this exact protein is not established by the supplied evidence."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5/H3) records ACT_SITE at position 213 with description 'Proton donor', matching option A exactly. The evidence code is ECO:0000250 (inferred by similarity from O93868), making this a computational transfer annotation rather than direct experimental evidence for this specific protein. However, the sequence itself independently supports the annotation: position 213 is Tyrosine, situated in a canonical SDR YXXXK catalytic dyad (Y213-C214-S215-S216-K217), which is the hallmark active-site architecture of the short-chain dehydrogenase/reductase family. The annotation is well-supported by the sequence context.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 344-residue sequence contains multiple diagnostic SDR (short-chain dehydrogenase/reductase) family motifs visible in the primary sequence: (1) a Rossmann-fold NAD(P)H-binding GxGxxG motif at positions ~46-52 (GGNTGLG), (2) the catalytic Ser in an STG motif around positions 138-141 (SSTG), and (3) the canonical YXXXK catalytic dyad at Y213-C214-S215-S216-K217. In the SDR family, the catalytic tetrad is Ser-Tyr-Lys-Asn, where Tyr acts as the proton donor and Lys lowers its pKa. This family-level knowledge, combined with reading the sequence, directly identifies Y213 as the proton donor. Option B (position 422) is eliminated because the protein is only 344 residues long. Option C (position 318, beta-ketoacyl synthase) refers to a completely unrelated enzyme class (fatty acid synthase); position 318 is Thr, and no beta-ketoacyl synthase motifs are present. Option D (position 209, Proline as proton donor) is chemically nonsensical—proline has no ionizable side-chain proton. Only option A is consistent with both the SDR family architecture and basic amino-acid chemistry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the SDR fold from the GxGxxG Rossmann motif, the STG serine motif, and the YXXXK catalytic dyad visible in the raw sequence. SDR family knowledge (catalytic tetrad Ser-Tyr-Lys-Asn, Tyr as proton donor) is standard transferable biochemistry. Three of four options are eliminated by straightforward reasoning: B by protein length, C by enzyme-class mismatch, D by amino-acid chemistry. This constitutes a concrete, credible inference from sequence features and family-level knowledge without requiring the target's specific database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A is chemically and structurally defensible. B references a nonexistent position, C references an unrelated enzyme class, and D assigns a proton-donor role to proline, which lacks an ionizable side-chain proton. No ambiguity exists among the choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000250 (similarity-based transfer from O93868), not direct experimental validation for this specific protein. However, the YXXXK motif in the sequence independently corroborates the annotation.
- The protein is annotated as EC 1.1.1.- (unspecified dehydrogenase/reductase activity), so the exact substrate and reaction mechanism are not fully characterized, but the catalytic tetrad assignment is standard for the SDR superfamily.
- The question asks for a single residue rather than the full catalytic tetrad (Ser-Tyr-Lys-Asn), which is a simplification but does not create ambiguity among the offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 344-residue sequence contains multiple diagnostic SDR (short-chain dehydrogenase/reductase) family motifs visible in the primary sequence: (1) a Rossmann-fold NAD(P)H-binding GxGxxG motif at positions ~46-52 (GGNTGLG), (2) the catalytic Ser in an STG motif around positions 138-141 (SSTG), and (3) the canonical YXXXK catalytic dyad at Y213-C214-S215-S216-K217. In the SDR family, the catalytic tetrad is Ser-Tyr-Lys-Asn, where Tyr acts as the proton donor and Lys lowers its pKa. This family-level knowledge, combined with reading the sequence, directly identifies Y213 as the proton donor. Option B (position 422) is eliminated because the protein is only 344 residues long. Option C (position 318, beta-ketoacyl synthase) refers to a completely unrelated enzyme class (fatty acid synthase); position 318 is Thr, and no beta-ketoacyl synthase motifs are present. Option D (position 209, Proline as proton donor) is chemically nonsensical—proline has no ionizable side-chain proton. Only option A is consistent with both the SDR family architecture and basic amino-acid chemistry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the SDR fold from the GxGxxG Rossmann motif, the STG serine motif, and the YXXXK catalytic dyad visible in the raw sequence. SDR family knowledge (catalytic tetrad Ser-Tyr-Lys-Asn, Tyr as proton donor) is standard transferable biochemistry. Three of four options are eliminated by straightforward reasoning: B by protein length, C by enzyme-class mismatch, D by amino-acid chemistry. This constitutes a concrete, credible inference from sequence features and family-level knowledge without requiring the target's specific database record."
  },
  "case_id": "active_site_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) records ACT_SITE at position 213 with description 'Proton donor', matching option A exactly. The evidence code is ECO:0000250 (inferred by similarity from O93868), making this a computational transfer annotation rather than direct experimental evidence for this specific protein. However, the sequence itself independently supports the annotation: position 213 is Tyrosine, situated in a canonical SDR YXXXK catalytic dyad (Y213-C214-S215-S216-K217), which is the hallmark active-site architecture of the short-chain dehydrogenase/reductase family. The annotation is well-supported by the sequence context."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity-based transfer from O93868), not direct experimental validation for this specific protein. However, the YXXXK motif in the sequence independently corroborates the annotation.",
    "The protein is annotated as EC 1.1.1.- (unspecified dehydrogenase/reductase activity), so the exact substrate and reaction mechanism are not fully characterized, but the catalytic tetrad assignment is standard for the SDR superfamily.",
    "The question asks for a single residue rather than the full catalytic tetrad (Ser-Tyr-Lys-Asn), which is a simplification but does not create ambiguity among the offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A is chemically and structurally defensible. B references a nonexistent position, C references an unrelated enzyme class, and D assigns a proton-donor role to proline, which lacks an ionizable side-chain proton. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) records ACT_SITE at position 213 with description 'Proton donor', matching option A exactly. The evidence code is ECO:0000250 (inferred by similarity from O93868), making this a computational transfer annotation rather than direct experimental evidence for this specific protein. However, the sequence itself independently supports the annotation: position 213 is Tyrosine, situated in a canonical SDR YXXXK catalytic dyad (Y213-C214-S215-S216-K217), which is the hallmark active-site architecture of the short-chain dehydrogenase/reductase family. The annotation is well-supported by the sequence context.",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 344-residue sequence contains multiple diagnostic SDR (short-chain dehydrogenase/reductase) family motifs visible in the primary sequence: (1) a Rossmann-fold NAD(P)H-binding GxGxxG motif at positions ~46-52 (GGNTGLG), (2) the catalytic Ser in an STG motif around positions 138-141 (SSTG), and (3) the canonical YXXXK catalytic dyad at Y213-C214-S215-S216-K217. In the SDR family, the catalytic tetrad is Ser-Tyr-Lys-Asn, where Tyr acts as the proton donor and Lys lowers its pKa. This family-level knowledge, combined with reading the sequence, directly identifies Y213 as the proton donor. Option B (position 422) is eliminated because the protein is only 344 residues long. Option C (position 318, beta-ketoacyl synthase) refers to a completely unrelated enzyme class (fatty acid synthase); position 318 is Thr, and no beta-ketoacyl synthase motifs are present. Option D (position 209, Proline as proton donor) is chemically nonsensical—proline has no ionizable side-chain proton. Only option A is consistent with both the SDR family architecture and basic amino-acid chemistry.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the SDR fold from the GxGxxG Rossmann motif, the STG serine motif, and the YXXXK catalytic dyad visible in the raw sequence. SDR family knowledge (catalytic tetrad Ser-Tyr-Lys-Asn, Tyr as proton donor) is standard transferable biochemistry. Three of four options are eliminated by straightforward reasoning: B by protein length, C by enzyme-class mismatch, D by amino-acid chemistry. This constitutes a concrete, credible inference from sequence features and family-level knowledge without requiring the target's specific database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A is chemically and structurally defensible. B references a nonexistent position, C references an unrelated enzyme class, and D assigns a proton-donor role to proline, which lacks an ionizable side-chain proton. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity-based transfer from O93868), not direct experimental validation for this specific protein. However, the YXXXK motif in the sequence independently corroborates the annotation.",
    "The protein is annotated as EC 1.1.1.- (unspecified dehydrogenase/reductase activity), so the exact substrate and reaction mechanism are not fully characterized, but the catalytic tetrad assignment is standard for the SDR superfamily.",
    "The question asks for a single residue rather than the full catalytic tetrad (Ser-Tyr-Lys-Asn), which is a simplification but does not create ambiguity among the offered choices."
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
  "requested_accession": "P9WEF8",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "0a30c027370e5819ffd6b616e044620add4aab1727c9776a8fe3c6b10140c2c0",
  "benchmark_sequence_length": 344,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "current_source_sequence_sha256": "0a30c027370e5819ffd6b616e044620add4aab1727c9776a8fe3c6b10140c2c0",
  "current_source_sequence_length": 344,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 3,
  "selected_historical_version": {
    "accession": "P9WEF8",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFMJ_ANNMO",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "selected_historical_source_sequence_sha256": "0a30c027370e5819ffd6b616e044620add4aab1727c9776a8fe3c6b10140c2c0",
  "selected_historical_source_sequence_length": 344,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P9WEF8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein J\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Short chain dehydrogenase/reductase mfmJ\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":213},\"start\":{\"modifier\":\"EXACT\",\"value\":213}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Lowers pKa of active site Tyr\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":217},\"start\":{\"modifier\":\"EXACT\",\"value\":217}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":51},\"start\":{\"modifier\":\"EXACT\",\"value\":51}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":76},\"start\":{\"modifier\":\"EXACT\",\"value\":76}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":99},\"start\":{\"modifier\":\"EXACT\",\"value\":99}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":126},\"start\":{\"modifier\":\"EXACT\",\"value\":126}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":213},\"start\":{\"modifier\":\"EXACT\",\"value\":213}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":217},\"start\":{\"modifier\":\"EXACT\",\"value\":217}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEF8.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEF8.json",
  "source_sha256": "9a494f2955cba14fda6801e28cd5d9e6a1f3b61da3369720080e6fbf19236119",
  "retrieved_utc": "2026-11-01T06:25:17.465258+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   MFMJ_ANNMO              Reviewed;         344 AA.\nAC   P9WEF8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Short chain dehydrogenase/reductase mfmJ {ECO:0000303|PubMed:38404388};\nDE            EC=1.1.1.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein J {ECO:0000303|PubMed:38404388};\nGN   Name=mfmJ {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_30196;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 28-35",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 77-79",
  "excerpt": "FT   ACT_SITE        213\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 80-82",
  "excerpt": "FT   ACT_SITE        217\nFT                   /note=\"Lowers pKa of active site Tyr\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 83-86",
  "excerpt": "FT   BINDING         51\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 87-90",
  "excerpt": "FT   BINDING         76\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 91-94",
  "excerpt": "FT   BINDING         99\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 95-98",
  "excerpt": "FT   BINDING         126\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 99-102",
  "excerpt": "FT   BINDING         213\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P9WEF8?format=txt&versions=3",
  "source_sha256": "3608734adc7ff5df9b0cabc554112ea4dc3d6cc16223d0ba3c879e8dd2be8cd0",
  "retrieved_utc": "2026-11-01T06:28:26.212556+00:00",
  "source_locator": "lines 103-106",
  "excerpt": "FT   BINDING         217\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 3,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
