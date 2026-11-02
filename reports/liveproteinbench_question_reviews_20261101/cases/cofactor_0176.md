# cofactor_0176

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Mn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSKTDFSHDLLRFSDEVKEALHSGKPVVALESTVIAHGLPYPENVATARKIEAAVRAEGAIPATIGIENGRFLIGMSDADLERFGSTRGIPKASSRDIPVILAQGGMGATTVASSLVAADLAGIPFFASAGIGGVHRGAERSMDISADLIQFTRSRVAVVCAGAKSILDLGLTLEYLETQCVPIISYQSDDFPAFYCRSSGFHSPHRLDDATVIARSIDMHWKLGNQSSVLITHPIHEEDAIGTDEVESIIREAAVQAEHEGIRGPGATPYLMRAVAKATEGKTVKANMSVLISTAALAGKLACAHIDYLRQQNQA

[Multiple Choices]
A. pyridoxal 5'-phosphate
B. cob(II)alamin
C. heme
D. Mn(2+)
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

> The exact sequence matches a UniProt entry annotated as pseudouridine-5'-phosphate glycosidase, with Mn(2+) as its cofactor and one ion bound per subunit. The annotation is attributed to a HAMAP rule, so this supports the key as a computational annotation, not as independently verified experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The supplied sequence and choices do not provide a clear general biological argument that specifically identifies Mn(2+) over the other candidates.


**Missing item-specific fact**

> The protein-specific functional or cofactor annotation identifying this sequence as a pseudouridine-5'-phosphate glycosidase that binds Mn(2+).


**Reason**

> The key is supported by a sequence-matched database annotation, but that annotation and protein identity are absent from the input. Recognizing the sequence or consulting a protein-specific annotation would be needed to select Mn(2+).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation specifies Mn(2+); no evidence provided supports another listed cofactor.


### Important caveats

- The cited cofactor annotation is based on a HAMAP rule (computational inference); the supplied evidence does not establish experimental validation.
- The source sequence matches exactly, but the author's original database snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence and choices do not provide a clear general biological argument that specifically identifies Mn(2+) over the other candidates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional or cofactor annotation identifying this sequence as a pseudouridine-5'-phosphate glycosidase that binds Mn(2+).",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation and protein identity are absent from the input. Recognizing the sequence or consulting a protein-specific annotation would be needed to select Mn(2+)."
  },
  "case_id": "cofactor_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as pseudouridine-5'-phosphate glycosidase, with Mn(2+) as its cofactor and one ion bound per subunit. The annotation is attributed to a HAMAP rule, so this supports the key as a computational annotation, not as independently verified experimental evidence."
  },
  "important_caveats": [
    "The cited cofactor annotation is based on a HAMAP rule (computational inference); the supplied evidence does not establish experimental validation.",
    "The source sequence matches exactly, but the author's original database snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation specifies Mn(2+); no evidence provided supports another listed cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as pseudouridine-5'-phosphate glycosidase, with Mn(2+) as its cofactor and one ion bound per subunit. The annotation is attributed to a HAMAP rule, so this supports the key as a computational annotation, not as independently verified experimental evidence.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The supplied sequence and choices do not provide a clear general biological argument that specifically identifies Mn(2+) over the other candidates.",
    "missing_item_specific_fact": "The protein-specific functional or cofactor annotation identifying this sequence as a pseudouridine-5'-phosphate glycosidase that binds Mn(2+).",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation and protein identity are absent from the input. Recognizing the sequence or consulting a protein-specific annotation would be needed to select Mn(2+)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation specifies Mn(2+); no evidence provided supports another listed cofactor."
  },
  "important_caveats": [
    "The cited cofactor annotation is based on a HAMAP rule (computational inference); the supplied evidence does not establish experimental validation.",
    "The source sequence matches exactly, but the author's original database snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9L393 (PSUG_DICD3, Pseudouridine-5'-phosphate glycosidase, EC 4.2.1.70) annotates Mn(2+) as the cofactor, binding 1 Mn(2+) ion per subunit. The sequence matches exactly (316 aa, SHA256 confirmed). However, the evidence code is ECO:0000255 (HAMAP-Rule:MF_01876), indicating a computational/curatorial inference from family membership rather than direct experimental measurement of this specific protein. The annotation is consistent across both the current entry (v68) and the archived historical entry (v67).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A partial elimination argument exists: PLP (A) requires a characteristic lysine in a PLP-binding pocket found in transaminases/decarboxylases; cob(II)alamin (B) requires a dedicated B12-binding domain; heme (C) requires Cys/His heme-anchoring motifs. None of these are apparent in this 316-residue sequence, allowing their elimination. However, positively identifying Mn(2+) specifically—rather than Mg(2+), Zn(2+), Fe(2+), or other divalent cations common in glycosidases/hydrolases—requires knowledge of the PsiMP glycosidase (EC 4.2.1.70) family, which is an obscure enzyme family whose cofactor assignment derives from a HAMAP rule (MF_01876), not from a well-known general biochemical principle.


**Missing item-specific fact**

> The specific cofactor assignment (Mn(2+)) for the PsiMP glycosidase family (HAMAP MF_01876, EC 4.2.1.70). This is a family-specific annotation inferred computationally; no general metal-binding motif in the sequence uniquely identifies Mn(2+) over other divalent cations.


**Reason**

> The protein belongs to a specialized, low-profile enzyme family (PsiMP glycosidase). While the absence of PLP, cobalamin, and heme binding motifs permits elimination of A, B, and C, the positive identification of Mn(2+) requires memorization of this particular family's cofactor annotation. The cofactor itself is assigned by a HAMAP computational rule, not by a broadly applicable biochemical principle that a model could derive from sequence features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> PLP, cob(II)alamin, and heme each require highly distinctive structural motifs or domain architectures that are clearly absent from this 316-residue sequence, making A, B, and C readily eliminable. Mn(2+) is the only metal-ion option, and by elimination it is the only remaining choice. No other option is genuinely defensible given the sequence context, though the positive identification of Mn(2+) over other possible metals (Mg2+, Zn2+) relies on family-specific knowledge rather than sequence-intrinsic reasoning.


### Important caveats

- The cofactor annotation is based on ECO:0000255 (HAMAP-Rule:MF_01876), a computational/curatorial inference from family membership, not direct experimental evidence for this specific protein.
- The protein (IndA/PsiMP glycosidase, EC 4.2.1.70) is a relatively obscure enzyme; the cofactor assignment may not have been independently validated by metal-dependence assays for this particular ortholog.
- The sequence-to-accession mapping (Q9L393) was inferred from reviewer-only metadata, not provided to the evaluated model.
- The elimination of A, B, C by absence of characteristic motifs is reasonable but not airtight; cofactors can sometimes bind without canonical motifs, though this is rare for PLP, cobalamin, and heme.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A partial elimination argument exists: PLP (A) requires a characteristic lysine in a PLP-binding pocket found in transaminases/decarboxylases; cob(II)alamin (B) requires a dedicated B12-binding domain; heme (C) requires Cys/His heme-anchoring motifs. None of these are apparent in this 316-residue sequence, allowing their elimination. However, positively identifying Mn(2+) specifically—rather than Mg(2+), Zn(2+), Fe(2+), or other divalent cations common in glycosidases/hydrolases—requires knowledge of the PsiMP glycosidase (EC 4.2.1.70) family, which is an obscure enzyme family whose cofactor assignment derives from a HAMAP rule (MF_01876), not from a well-known general biochemical principle.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific cofactor assignment (Mn(2+)) for the PsiMP glycosidase family (HAMAP MF_01876, EC 4.2.1.70). This is a family-specific annotation inferred computationally; no general metal-binding motif in the sequence uniquely identifies Mn(2+) over other divalent cations.",
    "reason": "The protein belongs to a specialized, low-profile enzyme family (PsiMP glycosidase). While the absence of PLP, cobalamin, and heme binding motifs permits elimination of A, B, and C, the positive identification of Mn(2+) requires memorization of this particular family's cofactor annotation. The cofactor itself is assigned by a HAMAP computational rule, not by a broadly applicable biochemical principle that a model could derive from sequence features alone."
  },
  "case_id": "cofactor_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9L393 (PSUG_DICD3, Pseudouridine-5'-phosphate glycosidase, EC 4.2.1.70) annotates Mn(2+) as the cofactor, binding 1 Mn(2+) ion per subunit. The sequence matches exactly (316 aa, SHA256 confirmed). However, the evidence code is ECO:0000255 (HAMAP-Rule:MF_01876), indicating a computational/curatorial inference from family membership rather than direct experimental measurement of this specific protein. The annotation is consistent across both the current entry (v68) and the archived historical entry (v67)."
  },
  "important_caveats": [
    "The cofactor annotation is based on ECO:0000255 (HAMAP-Rule:MF_01876), a computational/curatorial inference from family membership, not direct experimental evidence for this specific protein.",
    "The protein (IndA/PsiMP glycosidase, EC 4.2.1.70) is a relatively obscure enzyme; the cofactor assignment may not have been independently validated by metal-dependence assays for this particular ortholog.",
    "The sequence-to-accession mapping (Q9L393) was inferred from reviewer-only metadata, not provided to the evaluated model.",
    "The elimination of A, B, C by absence of characteristic motifs is reasonable but not airtight; cofactors can sometimes bind without canonical motifs, though this is rare for PLP, cobalamin, and heme."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "PLP, cob(II)alamin, and heme each require highly distinctive structural motifs or domain architectures that are clearly absent from this 316-residue sequence, making A, B, and C readily eliminable. Mn(2+) is the only metal-ion option, and by elimination it is the only remaining choice. No other option is genuinely defensible given the sequence context, though the positive identification of Mn(2+) over other possible metals (Mg2+, Zn2+) relies on family-specific knowledge rather than sequence-intrinsic reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9L393 (PSUG_DICD3, Pseudouridine-5'-phosphate glycosidase, EC 4.2.1.70) annotates Mn(2+) as the cofactor, binding 1 Mn(2+) ion per subunit. The sequence matches exactly (316 aa, SHA256 confirmed). However, the evidence code is ECO:0000255 (HAMAP-Rule:MF_01876), indicating a computational/curatorial inference from family membership rather than direct experimental measurement of this specific protein. The annotation is consistent across both the current entry (v68) and the archived historical entry (v67).",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A partial elimination argument exists: PLP (A) requires a characteristic lysine in a PLP-binding pocket found in transaminases/decarboxylases; cob(II)alamin (B) requires a dedicated B12-binding domain; heme (C) requires Cys/His heme-anchoring motifs. None of these are apparent in this 316-residue sequence, allowing their elimination. However, positively identifying Mn(2+) specifically—rather than Mg(2+), Zn(2+), Fe(2+), or other divalent cations common in glycosidases/hydrolases—requires knowledge of the PsiMP glycosidase (EC 4.2.1.70) family, which is an obscure enzyme family whose cofactor assignment derives from a HAMAP rule (MF_01876), not from a well-known general biochemical principle.",
    "missing_item_specific_fact": "The specific cofactor assignment (Mn(2+)) for the PsiMP glycosidase family (HAMAP MF_01876, EC 4.2.1.70). This is a family-specific annotation inferred computationally; no general metal-binding motif in the sequence uniquely identifies Mn(2+) over other divalent cations.",
    "reason": "The protein belongs to a specialized, low-profile enzyme family (PsiMP glycosidase). While the absence of PLP, cobalamin, and heme binding motifs permits elimination of A, B, and C, the positive identification of Mn(2+) requires memorization of this particular family's cofactor annotation. The cofactor itself is assigned by a HAMAP computational rule, not by a broadly applicable biochemical principle that a model could derive from sequence features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "PLP, cob(II)alamin, and heme each require highly distinctive structural motifs or domain architectures that are clearly absent from this 316-residue sequence, making A, B, and C readily eliminable. Mn(2+) is the only metal-ion option, and by elimination it is the only remaining choice. No other option is genuinely defensible given the sequence context, though the positive identification of Mn(2+) over other possible metals (Mg2+, Zn2+) relies on family-specific knowledge rather than sequence-intrinsic reasoning."
  },
  "important_caveats": [
    "The cofactor annotation is based on ECO:0000255 (HAMAP-Rule:MF_01876), a computational/curatorial inference from family membership, not direct experimental evidence for this specific protein.",
    "The protein (IndA/PsiMP glycosidase, EC 4.2.1.70) is a relatively obscure enzyme; the cofactor assignment may not have been independently validated by metal-dependence assays for this particular ortholog.",
    "The sequence-to-accession mapping (Q9L393) was inferred from reviewer-only metadata, not provided to the evaluated model.",
    "The elimination of A, B, C by absence of characteristic motifs is reasonable but not airtight; cofactors can sometimes bind without canonical motifs, though this is rare for PLP, cobalamin, and heme."
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

**Accession:** `Q9L393` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 67. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:05.918269+00:00.  

```json
"Q9L393"
```

Source SHA-256: `e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:05.918269+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01876","source":"HAMAP-Rule"}],"value":"4.2.1.70"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01876","source":"HAMAP-Rule"}],"value":"Pseudouridine-5'-phosphate glycosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01876","source":"HAMAP-Rule"}],"value":"PsiMP glycosidase"}]}}
```

Source SHA-256: `e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:05.918269+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29035"},"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01876","source":"HAMAP-Rule"}],"name":"Mn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01876","source":"HAMAP-Rule"}],"value":"Binds 1 Mn(2+) ion per subunit."}]}}
```

Source SHA-256: `e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 2.  
**Retrieved:** 2026-11-02T04:33:13.935581+00:00.  

```text
ID   PSUG_DICD3              Reviewed;         316 AA.
AC   Q9L393; E0SMH8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 2.
DT   28-JAN-2026, entry version 67.
DE   RecName: Full=Pseudouridine-5'-phosphate glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};
DE            Short=PsiMP glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};
DE            EC=4.2.1.70 {ECO:0000255|HAMAP-Rule:MF_01876};
GN   Name=indA {ECO:0000303|PubMed:11790734};
GN   Synonyms=psuG {ECO:0000255|HAMAP-Rule:MF_01876};
GN   OrderedLocusNames=Dda3937_00974 {ECO:0000312|EMBL:ADN00617.1};
OS   Dickeya dadantii (strain 3937) (Erwinia chrysanthemi (strain 3937)).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Pectobacteriaceae; Dickeya.
OX   NCBI_TaxID=198628;
```

Source SHA-256: `b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 2.  
**Retrieved:** 2026-11-02T04:33:13.935581+00:00.  

```text
DE   RecName: Full=Pseudouridine-5'-phosphate glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};
DE            Short=PsiMP glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};
DE            EC=4.2.1.70 {ECO:0000255|HAMAP-Rule:MF_01876};
```

Source SHA-256: `b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)  
**Locator:** `lines 53-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 2.  
**Retrieved:** 2026-11-02T04:33:13.935581+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_01876};
CC       Note=Binds 1 Mn(2+) ion per subunit. {ECO:0000255|HAMAP-Rule:MF_01876};
```

Source SHA-256: `b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 176. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
