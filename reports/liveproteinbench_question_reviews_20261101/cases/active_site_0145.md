# active_site_0145

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 188 (Glycyl thioester intermediate; for adenylyltransferase activity)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLSLNEYLRYGRQLIVPEFGLQGQISLKNSRVLVVGAGGLGCPALQYLVGAGFGTVGIVDHDTVDISNLHRQILHTSETVEMLKCESAKLQLAKLNPLVQINTHPVALSPDNSFGIFEQYDIILDCTDTPATRYLINDTAVLLGLTVISGSGLKTEGQLSILNFNNTGPCYRCFYPTPPPPSSVTACSDGGVLGPVIGIMGVMMALEAIKVVSGYYLREDVEFQPFLSLYSGYGPLQSLRTFKMRRRSPKCRVCNAGTREITRHVIETELDYAVWCGKMDYNVLEKDERVSVEQLSAQRAPYLVDVRAKEQYSIVHLPNSINIPLNALKHMDTLDVPKETMIYVICRFGNDSQLAVKHLKSIGYENCVDVIGGLTQWSRQIDPNFPIY

[Multiple Choices]
A. Position 240 (Proton acceptor)
B. Position 188 (Glycyl thioester intermediate; for adenylyltransferase activity)
C. Position 118 (Nucleophile)
D. Position 203 (Proton donor)
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence’s UniProt annotation identifies position 188 as the glycyl thioester intermediate for adenylyltransferase activity. This supports choice B, but the annotation is rule-based computational evidence, not direct experimental validation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clear general biochemical argument that identifies position 188 as the glycyl thioester site rather than the listed alternatives.


**Missing item-specific fact**

> The protein-specific annotation that this UBA4 sequence uses residue 188 in a glycyl thioester intermediate during adenylyltransferase activity.


**Reason**

> The exact catalytic role and residue position require protein-family or database knowledge not supplied in the question; recognizing the sequence or relying on a predictor does not make the answer reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied matched-sequence annotation supports B among the listed options. The protein also has a separately annotated catalytic cysteine at position 347, but that residue is not offered as a choice.


### Important caveats

- The active-site annotation is supported by a HAMAP rule and was not independently established here by experimental evidence.
- The sequence matches both the current and historical UniProt entry; the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a clear general biochemical argument that identifies position 188 as the glycyl thioester site rather than the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation that this UBA4 sequence uses residue 188 in a glycyl thioester intermediate during adenylyltransferase activity.",
    "reason": "The exact catalytic role and residue position require protein-family or database knowledge not supplied in the question; recognizing the sequence or relying on a predictor does not make the answer reasoning-supported."
  },
  "case_id": "active_site_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence’s UniProt annotation identifies position 188 as the glycyl thioester intermediate for adenylyltransferase activity. This supports choice B, but the annotation is rule-based computational evidence, not direct experimental validation."
  },
  "important_caveats": [
    "The active-site annotation is supported by a HAMAP rule and was not independently established here by experimental evidence.",
    "The sequence matches both the current and historical UniProt entry; the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied matched-sequence annotation supports B among the listed options. The protein also has a separately annotated catalytic cysteine at position 347, but that residue is not offered as a choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence’s UniProt annotation identifies position 188 as the glycyl thioester intermediate for adenylyltransferase activity. This supports choice B, but the annotation is rule-based computational evidence, not direct experimental validation.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clear general biochemical argument that identifies position 188 as the glycyl thioester site rather than the listed alternatives.",
    "missing_item_specific_fact": "The protein-specific annotation that this UBA4 sequence uses residue 188 in a glycyl thioester intermediate during adenylyltransferase activity.",
    "reason": "The exact catalytic role and residue position require protein-family or database knowledge not supplied in the question; recognizing the sequence or relying on a predictor does not make the answer reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied matched-sequence annotation supports B among the listed options. The protein also has a separately annotated catalytic cysteine at position 347, but that residue is not offered as a choice."
  },
  "important_caveats": [
    "The active-site annotation is supported by a HAMAP rule and was not independently established here by experimental evidence.",
    "The sequence matches both the current and historical UniProt entry; the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation for W1QET1 (UBA4_OGAPD, 389 AA, sequence SHA256 match confirmed) explicitly annotates position 188 as 'Active site: Glycyl thioester intermediate; for adenylyltransferase activity' (evidence C5/H3). The residue at position 188 in the supplied sequence is Cys (C), consistent with the glycyl thioester mechanism. The annotation is computational (ECO:0000255, HAMAP-Rule MF_03049), not experimental, but it is a valid database annotation consistent with the well-established catalytic mechanism of UBA4-type adenylyltransferases.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable UBA4-family motifs (e.g., GAGGLGCPAL near the N-terminus, ACSD catalytic motif). UBA4-type adenylyltransferases catalyze glycyl thioester intermediate formation via a catalytic cysteine. Checking the amino acid at each listed position: position 188 = Cys (C), position 240 = Leu (L), position 118 = Phe (F), position 203 = Val (V). Only a cysteine can form a glycyl thioester; leucine, phenylalanine, and valine cannot serve as proton acceptors, nucleophiles, or proton donors in this enzymatic context. The ACSD motif (Ala187-Cys188-Ser189-Asp190) is a recognizable catalytic signature in this enzyme family.


**Missing item-specific fact**

> None strictly required. The protein family can be identified from sequence motifs, the catalytic mechanism is general knowledge for UBA4-type enzymes, and amino acid identity at each position can be verified by counting through the supplied sequence.


**Reason**

> A model with knowledge of UBA4-family adenylyltransferase mechanisms can reason that the catalytic residue must be a cysteine forming a glycyl thioester, then verify by counting to each listed position that only position 188 is a Cys. The distractors (Leu, Phe, Val) are chemically incapable of the functions described. This constitutes a concrete biological argument from the supplied sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein has two annotated active sites (Cys188 and Cys347), but only Cys188 appears among the options. The other three options assign catalytic roles to non-catalytic amino acids (Leu, Phe, Val), which are chemically implausible. No ambiguity exists among the choices.


### Important caveats

- The active site annotation is computational (ECO:0000255, HAMAP-Rule MF_03049), inferred by protein family similarity, not from direct experimental characterization of this specific Ogataea parapolymorpha UBA4.
- The protein also has a second active site at position 347 (Cys, persulfide intermediate for sulfurtransferase activity, annotated by PROSITE-ProRule PRU00173), but this is not offered as an option.
- Identifying the protein family from sequence and knowing the UBA4 catalytic mechanism requires specialized enzymology knowledge, though this is general biological knowledge for the relevant subfield.
- The reviewer-only evidence was not available to the evaluated model; the reasoning argument relies on the model's trained knowledge of UBA4-family enzymes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable UBA4-family motifs (e.g., GAGGLGCPAL near the N-terminus, ACSD catalytic motif). UBA4-type adenylyltransferases catalyze glycyl thioester intermediate formation via a catalytic cysteine. Checking the amino acid at each listed position: position 188 = Cys (C), position 240 = Leu (L), position 118 = Phe (F), position 203 = Val (V). Only a cysteine can form a glycyl thioester; leucine, phenylalanine, and valine cannot serve as proton acceptors, nucleophiles, or proton donors in this enzymatic context. The ACSD motif (Ala187-Cys188-Ser189-Asp190) is a recognizable catalytic signature in this enzyme family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The protein family can be identified from sequence motifs, the catalytic mechanism is general knowledge for UBA4-type enzymes, and amino acid identity at each position can be verified by counting through the supplied sequence.",
    "reason": "A model with knowledge of UBA4-family adenylyltransferase mechanisms can reason that the catalytic residue must be a cysteine forming a glycyl thioester, then verify by counting to each listed position that only position 188 is a Cys. The distractors (Leu, Phe, Val) are chemically incapable of the functions described. This constitutes a concrete biological argument from the supplied sequence and choices."
  },
  "case_id": "active_site_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation for W1QET1 (UBA4_OGAPD, 389 AA, sequence SHA256 match confirmed) explicitly annotates position 188 as 'Active site: Glycyl thioester intermediate; for adenylyltransferase activity' (evidence C5/H3). The residue at position 188 in the supplied sequence is Cys (C), consistent with the glycyl thioester mechanism. The annotation is computational (ECO:0000255, HAMAP-Rule MF_03049), not experimental, but it is a valid database annotation consistent with the well-established catalytic mechanism of UBA4-type adenylyltransferases."
  },
  "important_caveats": [
    "The active site annotation is computational (ECO:0000255, HAMAP-Rule MF_03049), inferred by protein family similarity, not from direct experimental characterization of this specific Ogataea parapolymorpha UBA4.",
    "The protein also has a second active site at position 347 (Cys, persulfide intermediate for sulfurtransferase activity, annotated by PROSITE-ProRule PRU00173), but this is not offered as an option.",
    "Identifying the protein family from sequence and knowing the UBA4 catalytic mechanism requires specialized enzymology knowledge, though this is general biological knowledge for the relevant subfield.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning argument relies on the model's trained knowledge of UBA4-family enzymes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has two annotated active sites (Cys188 and Cys347), but only Cys188 appears among the options. The other three options assign catalytic roles to non-catalytic amino acids (Leu, Phe, Val), which are chemically implausible. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation for W1QET1 (UBA4_OGAPD, 389 AA, sequence SHA256 match confirmed) explicitly annotates position 188 as 'Active site: Glycyl thioester intermediate; for adenylyltransferase activity' (evidence C5/H3). The residue at position 188 in the supplied sequence is Cys (C), consistent with the glycyl thioester mechanism. The annotation is computational (ECO:0000255, HAMAP-Rule MF_03049), not experimental, but it is a valid database annotation consistent with the well-established catalytic mechanism of UBA4-type adenylyltransferases.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable UBA4-family motifs (e.g., GAGGLGCPAL near the N-terminus, ACSD catalytic motif). UBA4-type adenylyltransferases catalyze glycyl thioester intermediate formation via a catalytic cysteine. Checking the amino acid at each listed position: position 188 = Cys (C), position 240 = Leu (L), position 118 = Phe (F), position 203 = Val (V). Only a cysteine can form a glycyl thioester; leucine, phenylalanine, and valine cannot serve as proton acceptors, nucleophiles, or proton donors in this enzymatic context. The ACSD motif (Ala187-Cys188-Ser189-Asp190) is a recognizable catalytic signature in this enzyme family.",
    "missing_item_specific_fact": "None strictly required. The protein family can be identified from sequence motifs, the catalytic mechanism is general knowledge for UBA4-type enzymes, and amino acid identity at each position can be verified by counting through the supplied sequence.",
    "reason": "A model with knowledge of UBA4-family adenylyltransferase mechanisms can reason that the catalytic residue must be a cysteine forming a glycyl thioester, then verify by counting to each listed position that only position 188 is a Cys. The distractors (Leu, Phe, Val) are chemically incapable of the functions described. This constitutes a concrete biological argument from the supplied sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has two annotated active sites (Cys188 and Cys347), but only Cys188 appears among the options. The other three options assign catalytic roles to non-catalytic amino acids (Leu, Phe, Val), which are chemically implausible. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The active site annotation is computational (ECO:0000255, HAMAP-Rule MF_03049), inferred by protein family similarity, not from direct experimental characterization of this specific Ogataea parapolymorpha UBA4.",
    "The protein also has a second active site at position 347 (Cys, persulfide intermediate for sulfurtransferase activity, annotated by PROSITE-ProRule PRU00173), but this is not offered as an option.",
    "Identifying the protein family from sequence and knowing the UBA4 catalytic mechanism requires specialized enzymology knowledge, though this is general biological knowledge for the relevant subfield.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning argument relies on the model's trained knowledge of UBA4-family enzymes."
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

**Accession:** `W1QET1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 67. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:06.106793+00:00.  

```json
"W1QET1"
```

Source SHA-256: `958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:06.106793+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Ubiquitin-like protein activator 4"}}],"includes":[{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Adenylyltransferase UBA4"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Sulfur carrier protein MOCS2A adenylyltransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O95396","source":"UniProtKB"}],"value":"2.7.7.80"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Molybdopterin-synthase adenylyltransferase"}}},{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Sulfur carrier protein MOCS2A sulfurtransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Sulfurtransferase UBA4"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O95396","source":"UniProtKB"}],"value":"2.8.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Molybdopterin-synthase sulfurtransferase"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Adenylyltransferase and sulfurtransferase uba4"}}}
```

Source SHA-256: `958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QET1.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:06.106793+00:00.  

```json
{"description":"Glycyl thioester intermediate; for adenylyltransferase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_03049","source":"HAMAP-Rule"}],"location":{"end":{"modifier":"EXACT","value":188},"start":{"modifier":"EXACT","value":188}},"type":"Active site"}
```

Source SHA-256: `958c25c940d458086b51fa46493ccb8538925f70cafe7242c4eeff6965bc6e08`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)  
**Locator:** `lines 1-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:34:08.361822+00:00.  

```text
ID   UBA4_OGAPD              Reviewed;         389 AA.
AC   W1QET1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-MAR-2014, sequence version 1.
DT   28-JAN-2026, entry version 67.
DE   RecName: Full=Adenylyltransferase and sulfurtransferase uba4 {ECO:0000305};
DE   AltName: Full=Ubiquitin-like protein activator 4 {ECO:0000305};
DE   Includes:
DE     RecName: Full=Molybdopterin-synthase adenylyltransferase {ECO:0000305};
DE              EC=2.7.7.80 {ECO:0000250|UniProtKB:O95396};
DE     AltName: Full=Adenylyltransferase UBA4 {ECO:0000305};
DE     AltName: Full=Sulfur carrier protein MOCS2A adenylyltransferase {ECO:0000305};
DE   Includes:
DE     RecName: Full=Molybdopterin-synthase sulfurtransferase {ECO:0000305};
DE              EC=2.8.1.11 {ECO:0000250|UniProtKB:O95396};
DE     AltName: Full=Sulfur carrier protein MOCS2A sulfurtransferase {ECO:0000305};
DE     AltName: Full=Sulfurtransferase UBA4 {ECO:0000305};
GN   Name=UBA4 {ECO:0000305}; Synonyms=CNX4 {ECO:0000303|PubMed:33617956};
GN   ORFNames=HPODL_00948 {ECO:0000312|EMBL:ESX00063.1};
OS   Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL
OS   Y-7560 / DL-1) (Yeast) (Hansenula polymorpha).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;
OC   Pichiales; Pichiaceae; Ogataea.
OX   NCBI_TaxID=871575 {ECO:0000312|Proteomes:UP000008673};
```

Source SHA-256: `1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QET1?format=txt&versions=67)  
**Locator:** `lines 153-156`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:34:08.361822+00:00.  

```text
FT   ACT_SITE        188
FT                   /note="Glycyl thioester intermediate; for
FT                   adenylyltransferase activity"
FT                   /evidence="ECO:0000255|HAMAP-Rule:MF_03049"
```

Source SHA-256: `1439891a4b0a62345927d6f7a896540071a99c07ab5153e3c7dc6126a8edc193`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 145. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
