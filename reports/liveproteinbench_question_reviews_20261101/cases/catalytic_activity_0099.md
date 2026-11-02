# catalytic_activity_0099

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — GTP + H2O = GDP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRAGRVRPLRASDMKKDVRILLVGEPRVGKTSLIMSLVSEEFPEEVPPRAEEITIPADVTPERVPTHIVDYSEAEQSDEQLHQEISQANVICIVYAVNNKHSIDKVTSRWIPLINERTDKDSRLPLILVGNKSDLVEYSSMETILPIMNQYTEIETCVECSAKNLKNISELFYYAQKAVLHPTGPLYCPEEKEMKPACIKALTRIFKISDQDNDGTLNDAELNFFQRICFNTPLAPQALEDVKNVVRKHLSDGVADSGLTLRGFLFLHTLFIQRGRHETTWTVLRRFGYDDDLDLTPEYLFPLLKIPPDCTTELNHHAYLFLQSTFDKHDLDRDCALSPDELKDLFQVFPYIPWGPDVNNTVCTNESGWITYQGFLSQWTLTTYLDVQRCLEYLGYLGYSILTEQESQASAITVTRDKKIDLQKKQTQRNVFRCNVIGVKGCGKTGVLQSLLGRNLMRQKKIRDDHKSYYAINTVYVYGQEKYLLLHDISESEFLTEAEIVCDVVCLVYDVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLKSSTFWLRASFGATVFAVVGFAMYRALLKQR

[Multiple Choices]
A. GTP + H2O = GDP + phosphate + H(+)
B. L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA
C. (13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O
D. 2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2'-hydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence match is annotated as a mitochondrial Rho GTPase, and its UniProt catalytic-activity record includes GTP hydrolysis, matching choice A. The annotation is transferred by similarity (ECO:0000250), not evidence of a direct experiment on this rat sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a P-loop-like GTPase nucleotide-binding motif (including a GxxxxGKT pattern), and the sequence context is consistent with a GTPase. Of the choices, GTP hydrolysis is the matching type of reaction; the other options describe unrelated transferase or specialized oxidation/rearrangement activities.


**Missing item-specific fact**

> A direct experimental characterization or exact protein annotation is absent from the input; the motif supports the choice but does not independently establish all substrate specificity.


**Reason**

> The sequence provides a meaningful biological basis for distinguishing A from the alternatives, though the reviewer-only database annotation strengthens the conclusion and is not evidence supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only A corresponds to the GTPase activity indicated by the sequence.


### Important caveats

- The database activity annotation is similarity-transferred rather than direct experimental evidence for this sequence.
- The sequence match is exact, but the author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a P-loop-like GTPase nucleotide-binding motif (including a GxxxxGKT pattern), and the sequence context is consistent with a GTPase. Of the choices, GTP hydrolysis is the matching type of reaction; the other options describe unrelated transferase or specialized oxidation/rearrangement activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "A direct experimental characterization or exact protein annotation is absent from the input; the motif supports the choice but does not independently establish all substrate specificity.",
    "reason": "The sequence provides a meaningful biological basis for distinguishing A from the alternatives, though the reviewer-only database annotation strengthens the conclusion and is not evidence supplied to the evaluated model."
  },
  "case_id": "catalytic_activity_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a mitochondrial Rho GTPase, and its UniProt catalytic-activity record includes GTP hydrolysis, matching choice A. The annotation is transferred by similarity (ECO:0000250), not evidence of a direct experiment on this rat sequence."
  },
  "important_caveats": [
    "The database activity annotation is similarity-transferred rather than direct experimental evidence for this sequence.",
    "The sequence match is exact, but the author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only A corresponds to the GTPase activity indicated by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a mitochondrial Rho GTPase, and its UniProt catalytic-activity record includes GTP hydrolysis, matching choice A. The annotation is transferred by similarity (ECO:0000250), not evidence of a direct experiment on this rat sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a P-loop-like GTPase nucleotide-binding motif (including a GxxxxGKT pattern), and the sequence context is consistent with a GTPase. Of the choices, GTP hydrolysis is the matching type of reaction; the other options describe unrelated transferase or specialized oxidation/rearrangement activities.",
    "missing_item_specific_fact": "A direct experimental characterization or exact protein annotation is absent from the input; the motif supports the choice but does not independently establish all substrate specificity.",
    "reason": "The sequence provides a meaningful biological basis for distinguishing A from the alternatives, though the reviewer-only database annotation strengthens the conclusion and is not evidence supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only A corresponds to the GTPase activity indicated by the sequence."
  },
  "important_caveats": [
    "The database activity annotation is similarity-transferred rather than direct experimental evidence for this sequence.",
    "The sequence match is exact, but the author's source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A1L1L6 (MIRO1_RAT) explicitly annotates the catalytic activity 'GTP + H2O = GDP + phosphate + H(+)' (Rhea:RHEA:19669), matching choice A exactly. The protein is named 'Mitochondrial Rho GTPase' with EC 3.6.5.-. The evidence code is ECO:0000250 (inferred by similarity to human MIRO1, Q8IXI2), meaning this is a computational/annotation transfer rather than direct experimental measurement on the rat protein, but it is well-established that MIRO-1 is a GTPase. The sequence itself contains canonical GTPase motifs (P-loop GKT, NKxD, SAK, DxxG) consistent with GTP hydrolysis.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains textbook GTPase/Ras-superfamily motifs: the P-loop 'GKTSLIMSL' (GxGKS-type Walker A), the NKxD motif 'NKSDLV', the SAK motif, and a DxxG region. These are canonical signatures of the Ras superfamily of small GTPases. Additionally, the C-terminal region contains EF-hand calcium-binding motifs (DxDxDxDxD patterns), consistent with the MIRO-1 architecture (GTPase + EF-hands). The distractors represent entirely unrelated enzyme classes: homoserine O-acetyltransferase (EC 2.3.1.31, a transferase with no GTPase motifs), a lipoxygenase/peroxidase (EC 1.13.11.x, requiring a different catalytic fold), and a carotenoid hydroxylase (EC 1.14.x, a cytochrome P450-type or non-heme iron enzyme). None of these would display P-loop/NKxD GTPase signatures.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable biologist can identify the GTPase domain from its canonical sequence motifs (P-loop, NKxD, SAK, DxxG) and the overall two-domain architecture (GTPase + EF-hands) without needing to recognize the exact protein or look up a database entry. The distractors are from completely unrelated enzyme superfamilies with no sequence overlap in catalytic motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although UniProt also lists ATP and UTP hydrolysis for MIRO-1, only GTP hydrolysis appears among the four choices. The other three options (homoserine acetyltransferase, lipoxygenase, carotenoid hydroxylase) are from unrelated enzyme classes with no plausible sequence signature match. No ambiguity exists among the provided options.


### Important caveats

- The UniProt annotation for GTP hydrolysis carries evidence code ECO:0000250 (similarity to human MIRO1 Q8IXI2), not direct experimental evidence on the rat protein. However, the GTPase activity of MIRO-1 is well-supported in the literature.
- The P-loop in this sequence reads 'GKT' rather than the more common 'GKS' variant; this is a known variant within the Ras superfamily and does not alter GTPase classification.
- The protein also has documented ATP and UTP hydrolysis activity, but these are not offered as distractors, so the question remains unambiguous among the given choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains textbook GTPase/Ras-superfamily motifs: the P-loop 'GKTSLIMSL' (GxGKS-type Walker A), the NKxD motif 'NKSDLV', the SAK motif, and a DxxG region. These are canonical signatures of the Ras superfamily of small GTPases. Additionally, the C-terminal region contains EF-hand calcium-binding motifs (DxDxDxDxD patterns), consistent with the MIRO-1 architecture (GTPase + EF-hands). The distractors represent entirely unrelated enzyme classes: homoserine O-acetyltransferase (EC 2.3.1.31, a transferase with no GTPase motifs), a lipoxygenase/peroxidase (EC 1.13.11.x, requiring a different catalytic fold), and a carotenoid hydroxylase (EC 1.14.x, a cytochrome P450-type or non-heme iron enzyme). None of these would display P-loop/NKxD GTPase signatures.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable biologist can identify the GTPase domain from its canonical sequence motifs (P-loop, NKxD, SAK, DxxG) and the overall two-domain architecture (GTPase + EF-hands) without needing to recognize the exact protein or look up a database entry. The distractors are from completely unrelated enzyme superfamilies with no sequence overlap in catalytic motifs."
  },
  "case_id": "catalytic_activity_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A1L1L6 (MIRO1_RAT) explicitly annotates the catalytic activity 'GTP + H2O = GDP + phosphate + H(+)' (Rhea:RHEA:19669), matching choice A exactly. The protein is named 'Mitochondrial Rho GTPase' with EC 3.6.5.-. The evidence code is ECO:0000250 (inferred by similarity to human MIRO1, Q8IXI2), meaning this is a computational/annotation transfer rather than direct experimental measurement on the rat protein, but it is well-established that MIRO-1 is a GTPase. The sequence itself contains canonical GTPase motifs (P-loop GKT, NKxD, SAK, DxxG) consistent with GTP hydrolysis."
  },
  "important_caveats": [
    "The UniProt annotation for GTP hydrolysis carries evidence code ECO:0000250 (similarity to human MIRO1 Q8IXI2), not direct experimental evidence on the rat protein. However, the GTPase activity of MIRO-1 is well-supported in the literature.",
    "The P-loop in this sequence reads 'GKT' rather than the more common 'GKS' variant; this is a known variant within the Ras superfamily and does not alter GTPase classification.",
    "The protein also has documented ATP and UTP hydrolysis activity, but these are not offered as distractors, so the question remains unambiguous among the given choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although UniProt also lists ATP and UTP hydrolysis for MIRO-1, only GTP hydrolysis appears among the four choices. The other three options (homoserine acetyltransferase, lipoxygenase, carotenoid hydroxylase) are from unrelated enzyme classes with no plausible sequence signature match. No ambiguity exists among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A1L1L6 (MIRO1_RAT) explicitly annotates the catalytic activity 'GTP + H2O = GDP + phosphate + H(+)' (Rhea:RHEA:19669), matching choice A exactly. The protein is named 'Mitochondrial Rho GTPase' with EC 3.6.5.-. The evidence code is ECO:0000250 (inferred by similarity to human MIRO1, Q8IXI2), meaning this is a computational/annotation transfer rather than direct experimental measurement on the rat protein, but it is well-established that MIRO-1 is a GTPase. The sequence itself contains canonical GTPase motifs (P-loop GKT, NKxD, SAK, DxxG) consistent with GTP hydrolysis.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains textbook GTPase/Ras-superfamily motifs: the P-loop 'GKTSLIMSL' (GxGKS-type Walker A), the NKxD motif 'NKSDLV', the SAK motif, and a DxxG region. These are canonical signatures of the Ras superfamily of small GTPases. Additionally, the C-terminal region contains EF-hand calcium-binding motifs (DxDxDxDxD patterns), consistent with the MIRO-1 architecture (GTPase + EF-hands). The distractors represent entirely unrelated enzyme classes: homoserine O-acetyltransferase (EC 2.3.1.31, a transferase with no GTPase motifs), a lipoxygenase/peroxidase (EC 1.13.11.x, requiring a different catalytic fold), and a carotenoid hydroxylase (EC 1.14.x, a cytochrome P450-type or non-heme iron enzyme). None of these would display P-loop/NKxD GTPase signatures.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable biologist can identify the GTPase domain from its canonical sequence motifs (P-loop, NKxD, SAK, DxxG) and the overall two-domain architecture (GTPase + EF-hands) without needing to recognize the exact protein or look up a database entry. The distractors are from completely unrelated enzyme superfamilies with no sequence overlap in catalytic motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although UniProt also lists ATP and UTP hydrolysis for MIRO-1, only GTP hydrolysis appears among the four choices. The other three options (homoserine acetyltransferase, lipoxygenase, carotenoid hydroxylase) are from unrelated enzyme classes with no plausible sequence signature match. No ambiguity exists among the provided options."
  },
  "important_caveats": [
    "The UniProt annotation for GTP hydrolysis carries evidence code ECO:0000250 (similarity to human MIRO1 Q8IXI2), not direct experimental evidence on the rat protein. However, the GTPase activity of MIRO-1 is well-supported in the literature.",
    "The P-loop in this sequence reads 'GKT' rather than the more common 'GKS' variant; this is a known variant within the Ras superfamily and does not alter GTPase classification.",
    "The protein also has documented ATP and UTP hydrolysis activity, but these are not offered as distractors, so the question remains unambiguous among the given choices."
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

**Accession:** `A1L1L6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 147. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
"A1L1L6"
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"1307023","source":"RGD"}],"value":"Ras homolog gene family member T1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"value":"3.6.5.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"PIRNR037488","source":"PIRNR"}],"value":"Mitochondrial Rho GTPase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"MIRO-1"}]}}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19670"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"name":"GTP + H2O = GDP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19669"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:37565"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:58189"}]}}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
DE   RecName: Full=Mitochondrial Rho GTPase {ECO:0000255|PIRNR:PIRNR037488};
DE            Short=MIRO-1 {ECO:0000305};
DE            EC=3.6.5.- {ECO:0000250|UniProtKB:Q8IXI2};
DE   AltName: Full=Ras homolog gene family member T1 {ECO:0000312|RGD:1307023};
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 46-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=GTP + H2O = GDP + phosphate + H(+); Xref=Rhea:RHEA:19669,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:37565,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:58189;
CC         Evidence={ECO:0000250|UniProtKB:Q8IXI2};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19670;
CC         Evidence={ECO:0000250|UniProtKB:Q8IXI2};
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
