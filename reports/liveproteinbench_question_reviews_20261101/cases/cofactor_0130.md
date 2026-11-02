# cofactor_0130

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — &#91;2Fe-2S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q0CPG9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 90. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
"Q0CPG9"
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:190135"},"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"name":"[2Fe-2S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39522","source":"UniProtKB"}],"value":"Binds 1 [2Fe-2S] cluster per subunit."}]}}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"name":"Mg(2+)"}],"commentType":"COFACTOR"}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 66-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;
CC         Evidence={ECO:0000269|PubMed:29995859};
CC       Note=Binds 1 [2Fe-2S] cluster per subunit.
CC       {ECO:0000250|UniProtKB:P39522};
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 71-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000269|PubMed:29995859};
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
