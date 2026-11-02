# cofactor_0152

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — FAD

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRPNLFSGASRLLTYSRNGKLLTRGRSTKATSSSLDSQHQDAATTEGGRAESVEESPEQQRKLPTREPLAKNFFIGVVDKELLAYPEVIPRDEMAQLENSLLPLKNYFVEPRETEETSPETLRQLGLYGLNVSTDYEGKGYGWSASLMASEPDSTDINVTLGLQTHRVVVDLLKEVGTPLQQQRYLQDLATGKLIGTEAIYEISPPEEDYFNTTAELFPEYGKWQLNGEKSFVICTPGERQLFLVLAQTQQPNVPGVLGRGTTIFLVDSQQEGVRLGEKHATFGCRKAEIRRVHFEGVKLGEDQVVGLPHDGNRYSEQLVRSSRLRGSLVGLSLAKKLLNELAQYTVNTTQCGVQLQDLELTRIHMSRAMCSVYAMESMLYLTAGLLDEFRAQDVTLESAITKYFTLRQVYAIASQNLGVVGPKSLLSGETTELGLRDAAQLCTQGESLDTLGMFIALTGLQHAGQAMNTGVRKSRNPLFNPGHIFGKFLDNNSIDNPKTKMQLSEHVHPSLEAAAQCIELSVARLQMAVELMFTKHGNAVVERQSEMQRLAEVGTLIYAMWASVARASRSYCIGLPLADHELLTATAICSEGRDRVRTLCTEIYGGHFVNNDNNLVRLSKQVAKSKGYFAVHPLTFNF

[Multiple Choices]
A. Mn(2+)
B. FAD
C. Ca(2+)
D. pyridoxal 5'-phosphate
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

> The sequence exactly matches the historical UniProt sequence for this protein, whose record annotates FAD as a cofactor. That annotation is computationally assigned by RuleBase, not direct experimental evidence.

Citations as saved: [H5](#evidence-h5), [C5](#evidence-c5), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an ACAD9/acyl-CoA dehydrogenase-family protein; this enzyme family uses FAD, distinguishing it from the listed metal-ion and PLP options.


**Missing item-specific fact**

> The exact accession and its database cofactor annotation are absent, but are not essential if the ACAD-family sequence relationship is recognized.


**Reason**

> A family-level sequence inference paired with general knowledge of acyl-CoA dehydrogenases provides a biological basis for selecting FAD, rather than requiring recall of this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> FAD is supported by the matched protein annotation and by the ACAD-family cofactor relationship; no other listed option is comparably supported.


### Important caveats

- The cited FAD annotation is RuleBase computational evidence, not an experimentally demonstrated cofactor measurement in the supplied evidence.
- The protein is also annotated as a mitochondrial complex I assembly factor; its ACAD9-family relationship informs the cofactor inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an ACAD9/acyl-CoA dehydrogenase-family protein; this enzyme family uses FAD, distinguishing it from the listed metal-ion and PLP options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact accession and its database cofactor annotation are absent, but are not essential if the ACAD-family sequence relationship is recognized.",
    "reason": "A family-level sequence inference paired with general knowledge of acyl-CoA dehydrogenases provides a biological basis for selecting FAD, rather than requiring recall of this exact protein's database entry."
  },
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "C5",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt sequence for this protein, whose record annotates FAD as a cofactor. That annotation is computationally assigned by RuleBase, not direct experimental evidence."
  },
  "important_caveats": [
    "The cited FAD annotation is RuleBase computational evidence, not an experimentally demonstrated cofactor measurement in the supplied evidence.",
    "The protein is also annotated as a mitochondrial complex I assembly factor; its ACAD9-family relationship informs the cofactor inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is supported by the matched protein annotation and by the ACAD-family cofactor relationship; no other listed option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt sequence for this protein, whose record annotates FAD as a cofactor. That annotation is computationally assigned by RuleBase, not direct experimental evidence.",
    "evidence_ids": ["H5", "C5", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an ACAD9/acyl-CoA dehydrogenase-family protein; this enzyme family uses FAD, distinguishing it from the listed metal-ion and PLP options.",
    "missing_item_specific_fact": "The exact accession and its database cofactor annotation are absent, but are not essential if the ACAD-family sequence relationship is recognized.",
    "reason": "A family-level sequence inference paired with general knowledge of acyl-CoA dehydrogenases provides a biological basis for selecting FAD, rather than requiring recall of this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is supported by the matched protein annotation and by the ACAD-family cofactor relationship; no other listed option is comparably supported."
  },
  "important_caveats": [
    "The cited FAD annotation is RuleBase computational evidence, not an experimentally demonstrated cofactor measurement in the supplied evidence.",
    "The protein is also annotated as a mitochondrial complex I assembly factor; its ACAD9-family relationship informs the cofactor inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5U117 (ACAD9_DROME) explicitly annotates FAD as a cofactor (C5, H5). However, the evidence code is ECO:0000255 (RuleBase pattern matching), meaning the FAD assignment is computationally inferred from sequence motifs rather than experimentally demonstrated. The EC number (1.3.8.-) is also transferred by similarity from human ACAD9 (ECO:0000250). The protein's primary recommended name is 'Complex I assembly factor Egm, mitochondrial,' and the 'acyl-CoA dehydrogenase family member 9 homolog' designation is an alternative name. The FAD annotation is consistent with ACAD-family membership (all characterized ACADs are FAD-dependent flavoproteins), but direct experimental confirmation of FAD binding to this specific Drosophila protein is not cited.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Acyl-CoA dehydrogenases are a well-characterized family of FAD-dependent flavoproteins, and the sequence does exhibit a three-domain ACAD-like architecture (N-terminal FAD-binding Rossmann fold, middle catalytic domain, C-terminal substrate-binding domain). In principle, recognizing these motifs could lead to FAD. However, the protein's primary annotated function is as a mitochondrial Complex I assembly factor, not a classic acyl-CoA dehydrogenase. The EC number is incomplete (1.3.8.-) and transferred by similarity. Distinguishing FAD from the other options (Mn²⁺, Ca²⁺, PLP) from a 639-aa sequence without prior knowledge of the protein's ACAD-family identity is extremely difficult, as the FAD-binding motifs are not uniquely diagnostic in isolation.


**Missing item-specific fact**

> The specific identification of this sequence as ACAD9/Egm (Q5U117), a member of the acyl-CoA dehydrogenase family whose RuleBase annotation assigns FAD. Without knowing the protein's family identity, the sequence alone does not provide a clear, unambiguous signal to select FAD over the other cofactor options, particularly since the protein's primary role is Complex I assembly rather than classic FAD-dependent dehydrogenation.


**Reason**

> The question requires recognizing a specific protein's family annotation. While ACAD-family sequence features could theoretically guide inference, the protein's primary identity is as a Complex I assembly factor, its FAD annotation is a RuleBase/similarity inference (not experimental), and the EC number is incomplete. A model would most reliably arrive at FAD by identifying the protein as ACAD9 and recalling its annotation, rather than by de novo motif analysis of the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, FAD is the only cofactor consistent with acyl-CoA dehydrogenase family membership. Mn²⁺, Ca²⁺, and PLP are not associated with this protein family. While the FAD annotation is inference-based, no other option has any plausible connection to this protein's annotation or family. The distractors are clearly wrong for an ACAD-family protein.


### Important caveats

- The FAD annotation carries evidence code ECO:0000255 (RuleBase), meaning it is a computational pattern-match inference, not an experimental measurement of FAD binding or catalytic use.
- The protein's primary recommended name is 'Complex I assembly factor Egm,' and its role as a classic acyl-CoA dehydrogenase is tentative (EC 1.3.8.-, incomplete). Whether FAD is functionally used in its assembly-factor role versus being a vestigial family trait is not resolved by the annotation.
- The EC number and cofactor annotation are transferred from human ACAD9 (Q9H845) by similarity (ECO:0000250), not determined experimentally for the Drosophila protein.
- The sequence matches Q5U117 exactly (SHA-256 confirmed), and the annotation was present in entry version 160 (released January 2026), predating the benchmark cutoff.
- Reviewer-only evidence was not available to the evaluated model; the model saw only the raw sequence and four cofactor options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Acyl-CoA dehydrogenases are a well-characterized family of FAD-dependent flavoproteins, and the sequence does exhibit a three-domain ACAD-like architecture (N-terminal FAD-binding Rossmann fold, middle catalytic domain, C-terminal substrate-binding domain). In principle, recognizing these motifs could lead to FAD. However, the protein's primary annotated function is as a mitochondrial Complex I assembly factor, not a classic acyl-CoA dehydrogenase. The EC number is incomplete (1.3.8.-) and transferred by similarity. Distinguishing FAD from the other options (Mn²⁺, Ca²⁺, PLP) from a 639-aa sequence without prior knowledge of the protein's ACAD-family identity is extremely difficult, as the FAD-binding motifs are not uniquely diagnostic in isolation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this sequence as ACAD9/Egm (Q5U117), a member of the acyl-CoA dehydrogenase family whose RuleBase annotation assigns FAD. Without knowing the protein's family identity, the sequence alone does not provide a clear, unambiguous signal to select FAD over the other cofactor options, particularly since the protein's primary role is Complex I assembly rather than classic FAD-dependent dehydrogenation.",
    "reason": "The question requires recognizing a specific protein's family annotation. While ACAD-family sequence features could theoretically guide inference, the protein's primary identity is as a Complex I assembly factor, its FAD annotation is a RuleBase/similarity inference (not experimental), and the EC number is incomplete. A model would most reliably arrive at FAD by identifying the protein as ACAD9 and recalling its annotation, rather than by de novo motif analysis of the sequence."
  },
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5U117 (ACAD9_DROME) explicitly annotates FAD as a cofactor (C5, H5). However, the evidence code is ECO:0000255 (RuleBase pattern matching), meaning the FAD assignment is computationally inferred from sequence motifs rather than experimentally demonstrated. The EC number (1.3.8.-) is also transferred by similarity from human ACAD9 (ECO:0000250). The protein's primary recommended name is 'Complex I assembly factor Egm, mitochondrial,' and the 'acyl-CoA dehydrogenase family member 9 homolog' designation is an alternative name. The FAD annotation is consistent with ACAD-family membership (all characterized ACADs are FAD-dependent flavoproteins), but direct experimental confirmation of FAD binding to this specific Drosophila protein is not cited."
  },
  "important_caveats": [
    "The FAD annotation carries evidence code ECO:0000255 (RuleBase), meaning it is a computational pattern-match inference, not an experimental measurement of FAD binding or catalytic use.",
    "The protein's primary recommended name is 'Complex I assembly factor Egm,' and its role as a classic acyl-CoA dehydrogenase is tentative (EC 1.3.8.-, incomplete). Whether FAD is functionally used in its assembly-factor role versus being a vestigial family trait is not resolved by the annotation.",
    "The EC number and cofactor annotation are transferred from human ACAD9 (Q9H845) by similarity (ECO:0000250), not determined experimentally for the Drosophila protein.",
    "The sequence matches Q5U117 exactly (SHA-256 confirmed), and the annotation was present in entry version 160 (released January 2026), predating the benchmark cutoff.",
    "Reviewer-only evidence was not available to the evaluated model; the model saw only the raw sequence and four cofactor options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, FAD is the only cofactor consistent with acyl-CoA dehydrogenase family membership. Mn²⁺, Ca²⁺, and PLP are not associated with this protein family. While the FAD annotation is inference-based, no other option has any plausible connection to this protein's annotation or family. The distractors are clearly wrong for an ACAD-family protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5U117 (ACAD9_DROME) explicitly annotates FAD as a cofactor (C5, H5). However, the evidence code is ECO:0000255 (RuleBase pattern matching), meaning the FAD assignment is computationally inferred from sequence motifs rather than experimentally demonstrated. The EC number (1.3.8.-) is also transferred by similarity from human ACAD9 (ECO:0000250). The protein's primary recommended name is 'Complex I assembly factor Egm, mitochondrial,' and the 'acyl-CoA dehydrogenase family member 9 homolog' designation is an alternative name. The FAD annotation is consistent with ACAD-family membership (all characterized ACADs are FAD-dependent flavoproteins), but direct experimental confirmation of FAD binding to this specific Drosophila protein is not cited.",
    "evidence_ids": ["C5", "H5", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Acyl-CoA dehydrogenases are a well-characterized family of FAD-dependent flavoproteins, and the sequence does exhibit a three-domain ACAD-like architecture (N-terminal FAD-binding Rossmann fold, middle catalytic domain, C-terminal substrate-binding domain). In principle, recognizing these motifs could lead to FAD. However, the protein's primary annotated function is as a mitochondrial Complex I assembly factor, not a classic acyl-CoA dehydrogenase. The EC number is incomplete (1.3.8.-) and transferred by similarity. Distinguishing FAD from the other options (Mn²⁺, Ca²⁺, PLP) from a 639-aa sequence without prior knowledge of the protein's ACAD-family identity is extremely difficult, as the FAD-binding motifs are not uniquely diagnostic in isolation.",
    "missing_item_specific_fact": "The specific identification of this sequence as ACAD9/Egm (Q5U117), a member of the acyl-CoA dehydrogenase family whose RuleBase annotation assigns FAD. Without knowing the protein's family identity, the sequence alone does not provide a clear, unambiguous signal to select FAD over the other cofactor options, particularly since the protein's primary role is Complex I assembly rather than classic FAD-dependent dehydrogenation.",
    "reason": "The question requires recognizing a specific protein's family annotation. While ACAD-family sequence features could theoretically guide inference, the protein's primary identity is as a Complex I assembly factor, its FAD annotation is a RuleBase/similarity inference (not experimental), and the EC number is incomplete. A model would most reliably arrive at FAD by identifying the protein as ACAD9 and recalling its annotation, rather than by de novo motif analysis of the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, FAD is the only cofactor consistent with acyl-CoA dehydrogenase family membership. Mn²⁺, Ca²⁺, and PLP are not associated with this protein family. While the FAD annotation is inference-based, no other option has any plausible connection to this protein's annotation or family. The distractors are clearly wrong for an ACAD-family protein."
  },
  "important_caveats": [
    "The FAD annotation carries evidence code ECO:0000255 (RuleBase), meaning it is a computational pattern-match inference, not an experimental measurement of FAD binding or catalytic use.",
    "The protein's primary recommended name is 'Complex I assembly factor Egm,' and its role as a classic acyl-CoA dehydrogenase is tentative (EC 1.3.8.-, incomplete). Whether FAD is functionally used in its assembly-factor role versus being a vestigial family trait is not resolved by the annotation.",
    "The EC number and cofactor annotation are transferred from human ACAD9 (Q9H845) by similarity (ECO:0000250), not determined experimentally for the Drosophila protein.",
    "The sequence matches Q5U117 exactly (SHA-256 confirmed), and the annotation was present in entry version 160 (released January 2026), predating the benchmark cutoff.",
    "Reviewer-only evidence was not available to the evaluated model; the model saw only the raw sequence and four cofactor options."
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

**Accession:** `Q5U117` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 160. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:32.531924+00:00.  

```json
"Q5U117"
```

Source SHA-256: `eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:32.531924+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9H845","source":"UniProtKB"}],"value":"1.3.8.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34386730","source":"PubMed"}],"value":"Acyl-CoA dehydrogenase family member 9 homolog"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34386730","source":"PubMed"}],"value":"dACAD9"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16434470","source":"PubMed"},{"evidenceCode":"ECO:0000312","id":"FBgn0086712","source":"FlyBase"}],"value":"Protein Enigma"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9H845","source":"UniProtKB"}],"value":"Complex I assembly factor Egm, mitochondrial"}}}
```

Source SHA-256: `eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:32.531924+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:57692"},"evidences":[{"evidenceCode":"ECO:0000255","id":"RU362125","source":"RuleBase"}],"name":"FAD"}],"commentType":"COFACTOR"}
```

Source SHA-256: `eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 160 / 1.  
**Retrieved:** 2026-11-02T04:31:37.417263+00:00.  

```text
DE   RecName: Full=Complex I assembly factor Egm, mitochondrial {ECO:0000250|UniProtKB:Q9H845};
DE   AltName: Full=Acyl-CoA dehydrogenase family member 9 homolog {ECO:0000303|PubMed:34386730};
DE            Short=dACAD9 {ECO:0000303|PubMed:34386730};
DE            EC=1.3.8.- {ECO:0000250|UniProtKB:Q9H845};
DE   AltName: Full=Protein Enigma {ECO:0000303|PubMed:16434470, ECO:0000312|FlyBase:FBgn0086712};
DE   Flags: Precursor;
```

Source SHA-256: `ba991d46e99d0d7589b3036a1d8dc35d92587856d686f5c53968f3978aaa1afe`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160)  
**Locator:** `lines 97-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 160 / 1.  
**Retrieved:** 2026-11-02T04:31:37.417263+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=FAD; Xref=ChEBI:CHEBI:57692;
CC         Evidence={ECO:0000255|RuleBase:RU362125};
```

Source SHA-256: `ba991d46e99d0d7589b3036a1d8dc35d92587856d686f5c53968f3978aaa1afe`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 152. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
