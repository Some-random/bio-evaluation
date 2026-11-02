# transmembrane_0119

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 483..503

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKAFPVICLGFAIFSSSICVNINILQQIGYIKQQVWQLSYYSQSSSSYVVVKLLPNIQPTDNSCEFKSVTQYNKTLSNLLLPIAENINNIASPSPGSRRHKRFAGIAIGIAALGVATAAQVTAAVSLVQAQTNARAIAAMKNSIQATNRAVFEVKEGTQQLAIAVQAIQDHINTIMNTQLNNMSCQILDNQLATSLGLYLTELTTVFQPQLINPALSPISIQALRSLLGSMTPAVVQATLSTSISAAEILSAGLMEGQIVSVLLDEMQMIVKINIPTIVTQSNALVIDFHSISSFINNQESIIQLPDRILEIGNEQWRYPAKNCKLTRHHIFCQYNEAERLSLETKLCLAGNISACVFSPIAGSYMRRFVALDGTIVANCRSLTCLCKSPSYPIYQPDHHAVTTIDLTSCQTLSLDGLDFSIVSLSNITYAENLTISLSQTINTQPIDISTELSKVNASLQNAVKYIKESNHQLQSVSVSSKIGAIIVAALVLSILSIIISLLFCCWAYIATKEIRRINFKTNHINTISSSVDDLIRY

[Multiple Choices]
A. 39..59; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508; 528..548
B. 483..503
C. 483..507
D. 483..503; 558..583
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence exactly matches the UniProt record, whose transmembrane annotation is 483..503. The annotation carries evidence code ECO:0000255, indicating computational support rather than a reported experimental measurement.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a strong hydrophobic C-terminal stretch, which supports a membrane-spanning helix in this region and disfavors choices listing many unrelated segments. It does not establish the precise endpoint.


**Missing item-specific fact**

> The specific 483..503 boundary used by the protein's database annotation is absent from the input; distinguishing that boundary from 483..507 requires an item-specific annotation or other evidence.


**Reason**

> Sequence reasoning can locate the likely membrane anchor, but both B and C overlap the hydrophobic stretch. General membrane biology alone does not resolve their four-residue endpoint difference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both intervals cover the strongly hydrophobic segment beginning at 483. The additional residues in C remain hydrophobic/aromatic, so the sequence alone does not make the precise boundary between B and C unambiguous.


### Important caveats

- The supporting annotation is computational, not direct experimental evidence.
- The reviewer-only source record matches the supplied sequence, including in the historical record checked; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a strong hydrophobic C-terminal stretch, which supports a membrane-spanning helix in this region and disfavors choices listing many unrelated segments. It does not establish the precise endpoint.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific 483..503 boundary used by the protein's database annotation is absent from the input; distinguishing that boundary from 483..507 requires an item-specific annotation or other evidence.",
    "reason": "Sequence reasoning can locate the likely membrane anchor, but both B and C overlap the hydrophobic stretch. General membrane biology alone does not resolve their four-residue endpoint difference."
  },
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, whose transmembrane annotation is 483..503. The annotation carries evidence code ECO:0000255, indicating computational support rather than a reported experimental measurement."
  },
  "important_caveats": [
    "The supporting annotation is computational, not direct experimental evidence.",
    "The reviewer-only source record matches the supplied sequence, including in the historical record checked; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both intervals cover the strongly hydrophobic segment beginning at 483. The additional residues in C remain hydrophobic/aromatic, so the sequence alone does not make the precise boundary between B and C unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, whose transmembrane annotation is 483..503. The annotation carries evidence code ECO:0000255, indicating computational support rather than a reported experimental measurement.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a strong hydrophobic C-terminal stretch, which supports a membrane-spanning helix in this region and disfavors choices listing many unrelated segments. It does not establish the precise endpoint.",
    "missing_item_specific_fact": "The specific 483..503 boundary used by the protein's database annotation is absent from the input; distinguishing that boundary from 483..507 requires an item-specific annotation or other evidence.",
    "reason": "Sequence reasoning can locate the likely membrane anchor, but both B and C overlap the hydrophobic stretch. General membrane biology alone does not resolve their four-residue endpoint difference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both intervals cover the strongly hydrophobic segment beginning at 483. The additional residues in C remain hydrophobic/aromatic, so the sequence alone does not make the precise boundary between B and C unambiguous."
  },
  "important_caveats": [
    "The supporting annotation is computational, not direct experimental evidence.",
    "The reviewer-only source record matches the supplied sequence, including in the historical record checked; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9JAE0 (Mumps virus Fusion glycoprotein F0) annotates a single transmembrane helical region at 483..503 (evidence code ECO:0000255, inferred by similarity). Both the current entry (C5) and the historical v90 record (H2) confirm this annotation. The sequence is 538 residues, consistent with a single-pass type I membrane protein typical of paramyxovirus F proteins. Option D is impossible (positions 558-583 exceed the 538-residue sequence), and option A lists 12 TM segments inconsistent with the known single-pass topology of paramyxovirus F proteins.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General knowledge that paramyxovirus F proteins are single-pass type I membrane proteins with one TM helix near the C-terminus eliminates options A (12 TM segments) and D (positions exceeding protein length). Identifying the hydrophobic stretch near the C-terminus (~IVAALVLSILSIIISLLFCCWAYI) as the TM region is reasonable. However, the precise end boundary (503 vs 507) hinges on whether the last ~4 residues (e.g., including W/Y interface residues or a few borderline hydrophobic residues) are counted within the helix. Both 21-residue and 25-residue TM helices fall within the normal range, and the hydrophobicity transition in that region is gradual rather than sharp.


**Missing item-specific fact**

> The exact annotation boundary (483..503 vs 483..507) from the UniProt entry or equivalent structural/hydrophobicity-profile determination. Without the specific annotation or a precise hydropathy plot with a defined threshold, the 4-residue difference between options B and C cannot be reliably resolved by general biological reasoning alone.


**Reason**

> While the general location (single TM near C-terminus, ~position 483) and the elimination of options A and D are reasoning-accessible, the fine discrimination between B (483..503) and C (483..507) depends on the specific annotation boundary. The hydrophobic stretch is ~24 residues long; whether the final 3-4 residues (borderline, near the W/Y interface) are included or excluded requires the item-specific annotation or a precise computational threshold, not general biological principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both 483..503 (21 residues) and 483..507 (25 residues) represent plausible TM helix lengths for a paramyxovirus F protein. The hydrophobic stretch in the C-terminal region is approximately 24 residues, and the boundary between TM core and membrane-interface residues (W, Y) is not sharply defined by sequence alone. Without the annotation, both B and C could be defended on hydrophobicity grounds.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary is a computational/transfer annotation rather than direct experimental measurement (e.g., cryo-EM of the full-length F protein).
- Option D is trivially eliminated because positions 558-583 exceed the 538-residue protein length.
- Option A is eliminated by the well-established single-pass topology of paramyxovirus fusion glycoproteins.
- The signal peptide at the N-terminus (MKAFPVICLGFAIFSSSIC) is cleaved and is not a TM domain, which is relevant to eliminating spurious hydrophobic segments in option A.
- The exact author source snapshot is unknown; the annotation has been stable across entry versions 90 and 91.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General knowledge that paramyxovirus F proteins are single-pass type I membrane proteins with one TM helix near the C-terminus eliminates options A (12 TM segments) and D (positions exceeding protein length). Identifying the hydrophobic stretch near the C-terminus (~IVAALVLSILSIIISLLFCCWAYI) as the TM region is reasonable. However, the precise end boundary (503 vs 507) hinges on whether the last ~4 residues (e.g., including W/Y interface residues or a few borderline hydrophobic residues) are counted within the helix. Both 21-residue and 25-residue TM helices fall within the normal range, and the hydrophobicity transition in that region is gradual rather than sharp.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotation boundary (483..503 vs 483..507) from the UniProt entry or equivalent structural/hydrophobicity-profile determination. Without the specific annotation or a precise hydropathy plot with a defined threshold, the 4-residue difference between options B and C cannot be reliably resolved by general biological reasoning alone.",
    "reason": "While the general location (single TM near C-terminus, ~position 483) and the elimination of options A and D are reasoning-accessible, the fine discrimination between B (483..503) and C (483..507) depends on the specific annotation boundary. The hydrophobic stretch is ~24 residues long; whether the final 3-4 residues (borderline, near the W/Y interface) are included or excluded requires the item-specific annotation or a precise computational threshold, not general biological principles."
  },
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9JAE0 (Mumps virus Fusion glycoprotein F0) annotates a single transmembrane helical region at 483..503 (evidence code ECO:0000255, inferred by similarity). Both the current entry (C5) and the historical v90 record (H2) confirm this annotation. The sequence is 538 residues, consistent with a single-pass type I membrane protein typical of paramyxovirus F proteins. Option D is impossible (positions 558-583 exceed the 538-residue sequence), and option A lists 12 TM segments inconsistent with the known single-pass topology of paramyxovirus F proteins."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary is a computational/transfer annotation rather than direct experimental measurement (e.g., cryo-EM of the full-length F protein).",
    "Option D is trivially eliminated because positions 558-583 exceed the 538-residue protein length.",
    "Option A is eliminated by the well-established single-pass topology of paramyxovirus fusion glycoproteins.",
    "The signal peptide at the N-terminus (MKAFPVICLGFAIFSSSIC) is cleaved and is not a TM domain, which is relevant to eliminating spurious hydrophobic segments in option A.",
    "The exact author source snapshot is unknown; the annotation has been stable across entry versions 90 and 91."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both 483..503 (21 residues) and 483..507 (25 residues) represent plausible TM helix lengths for a paramyxovirus F protein. The hydrophobic stretch in the C-terminal region is approximately 24 residues, and the boundary between TM core and membrane-interface residues (W, Y) is not sharply defined by sequence alone. Without the annotation, both B and C could be defended on hydrophobicity grounds."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9JAE0 (Mumps virus Fusion glycoprotein F0) annotates a single transmembrane helical region at 483..503 (evidence code ECO:0000255, inferred by similarity). Both the current entry (C5) and the historical v90 record (H2) confirm this annotation. The sequence is 538 residues, consistent with a single-pass type I membrane protein typical of paramyxovirus F proteins. Option D is impossible (positions 558-583 exceed the 538-residue sequence), and option A lists 12 TM segments inconsistent with the known single-pass topology of paramyxovirus F proteins.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General knowledge that paramyxovirus F proteins are single-pass type I membrane proteins with one TM helix near the C-terminus eliminates options A (12 TM segments) and D (positions exceeding protein length). Identifying the hydrophobic stretch near the C-terminus (~IVAALVLSILSIIISLLFCCWAYI) as the TM region is reasonable. However, the precise end boundary (503 vs 507) hinges on whether the last ~4 residues (e.g., including W/Y interface residues or a few borderline hydrophobic residues) are counted within the helix. Both 21-residue and 25-residue TM helices fall within the normal range, and the hydrophobicity transition in that region is gradual rather than sharp.",
    "missing_item_specific_fact": "The exact annotation boundary (483..503 vs 483..507) from the UniProt entry or equivalent structural/hydrophobicity-profile determination. Without the specific annotation or a precise hydropathy plot with a defined threshold, the 4-residue difference between options B and C cannot be reliably resolved by general biological reasoning alone.",
    "reason": "While the general location (single TM near C-terminus, ~position 483) and the elimination of options A and D are reasoning-accessible, the fine discrimination between B (483..503) and C (483..507) depends on the specific annotation boundary. The hydrophobic stretch is ~24 residues long; whether the final 3-4 residues (borderline, near the W/Y interface) are included or excluded requires the item-specific annotation or a precise computational threshold, not general biological principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both 483..503 (21 residues) and 483..507 (25 residues) represent plausible TM helix lengths for a paramyxovirus F protein. The hydrophobic stretch in the C-terminal region is approximately 24 residues, and the boundary between TM core and membrane-interface residues (W, Y) is not sharply defined by sequence alone. Without the annotation, both B and C could be defended on hydrophobicity grounds."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundary is a computational/transfer annotation rather than direct experimental measurement (e.g., cryo-EM of the full-length F protein).",
    "Option D is trivially eliminated because positions 558-583 exceed the 538-residue protein length.",
    "Option A is eliminated by the well-established single-pass topology of paramyxovirus fusion glycoproteins.",
    "The signal peptide at the N-terminus (MKAFPVICLGFAIFSSSIC) is cleaved and is not a TM domain, which is relevant to eliminating spurious hydrophobic segments in option A.",
    "The exact author source snapshot is unknown; the annotation has been stable across entry versions 90 and 91."
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

**Accession:** `Q9JAE0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 90. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JAE0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:53.076550+00:00.  

```json
"Q9JAE0"
```

Source SHA-256: `a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JAE0.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:53.076550+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis","Mumps orthorubulavirus"],"scientificName":"Mumps virus (strain Kilham)","taxonId":11169}
```

Source SHA-256: `a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JAE0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:53.076550+00:00.  

```json
{"contains":[{"recommendedName":{"fullName":{"value":"Fusion glycoprotein F2"}}},{"recommendedName":{"fullName":{"value":"Fusion glycoprotein F1"}}}],"flag":"Precursor","recommendedName":{"fullName":{"value":"Fusion glycoprotein F0"}}}
```

Source SHA-256: `a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JAE0.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:53.076550+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":503},"start":{"modifier":"EXACT","value":483}},"type":"Transmembrane"}
```

Source SHA-256: `a780478bc274d83b2ecd8193dfbe338e0c35241fcd823c0246f785340a757c97`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JAE0?format=txt&versions=90)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:32:57.440303+00:00.  

```text
ID   FUS_MUMPK               Reviewed;         538 AA.
AC   Q9JAE0;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2000, sequence version 1.
DT   28-JAN-2026, entry version 90.
DE   RecName: Full=Fusion glycoprotein F0;
DE   Contains:
DE     RecName: Full=Fusion glycoprotein F2;
DE   Contains:
DE     RecName: Full=Fusion glycoprotein F1;
DE   Flags: Precursor;
GN   Name=F;
OS   Mumps virus (strain Kilham) (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.
OX   NCBI_TaxID=11169;
OH   NCBI_TaxID=9606; Homo sapiens (Human).
```

Source SHA-256: `08d7f73eabc93f41a14ddf3a765bb47e6225789823b6283397bfc28281fbc95b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JAE0?format=txt&versions=90)  
**Locator:** `lines 108-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:32:57.440303+00:00.  

```text
FT   TRANSMEM        483..503
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `08d7f73eabc93f41a14ddf3a765bb47e6225789823b6283397bfc28281fbc95b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
