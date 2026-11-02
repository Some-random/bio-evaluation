# transmembrane_0098

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 35..55

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEPSKLFTISDNATFAPGPVINVADKKTFRTCFRILVLSVQAVTLILVIVNLGELVRMINDQGLSNQLSSITDKIRESANMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTSKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYISTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. 371..391; 409..429; 444..464; 472..492; 531..551; 564..586; 596..618
B. 33..50
C. 35..55; 310..330
D. 35..55
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

> The sequence-matched UniProt record annotates residues 35–55 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational support, not direct experimental validation.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues 35–55 form a long, predominantly hydrophobic stretch consistent with a membrane-spanning helix. Starting at 35 avoids the preceding Arg at 34, while D includes more of the hydrophobic stretch than B.


**Missing item-specific fact**

> No item-specific fact is essential to identify the likely transmembrane segment, though exact boundaries are approximate and the annotation itself is not supplied to the model.


**Reason**

> The sequence provides a concrete hydrophobic-helix signal that favors D over the distractors; this is more than recognition of a protein-specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B overlaps the likely membrane-spanning core, but it includes a preceding charged residue and truncates the hydrophobic stretch relative to D.


### Important caveats

- The supporting UniProt annotation is computational (ECO:0000255), not experimental evidence.
- The reviewer-only record matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Residues 35–55 form a long, predominantly hydrophobic stretch consistent with a membrane-spanning helix. Starting at 35 avoids the preceding Arg at 34, while D includes more of the hydrophobic stretch than B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is essential to identify the likely transmembrane segment, though exact boundaries are approximate and the annotation itself is not supplied to the model.",
    "reason": "The sequence provides a concrete hydrophobic-helix signal that favors D over the distractors; this is more than recognition of a protein-specific database entry."
  },
  "case_id": "transmembrane_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residues 35–55 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational support, not direct experimental validation."
  },
  "important_caveats": [
    "The supporting UniProt annotation is computational (ECO:0000255), not experimental evidence.",
    "The reviewer-only record matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B overlaps the likely membrane-spanning core, but it includes a preceding charged residue and truncates the hydrophobic stretch relative to D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residues 35–55 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational support, not direct experimental validation.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues 35–55 form a long, predominantly hydrophobic stretch consistent with a membrane-spanning helix. Starting at 35 avoids the preceding Arg at 34, while D includes more of the hydrophobic stretch than B.",
    "missing_item_specific_fact": "No item-specific fact is essential to identify the likely transmembrane segment, though exact boundaries are approximate and the annotation itself is not supplied to the model.",
    "reason": "The sequence provides a concrete hydrophobic-helix signal that favors D over the distractors; this is more than recognition of a protein-specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B overlaps the likely membrane-spanning core, but it includes a preceding charged residue and truncates the hydrophobic stretch relative to D."
  },
  "important_caveats": [
    "The supporting UniProt annotation is computational (ECO:0000255), not experimental evidence.",
    "The reviewer-only record matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5SC51 (Mumps virus HN protein, 582 AA, sequence matched) annotates a single transmembrane helix at positions 35-55 (evidence code ECO:0000255, by similarity). The sequence at positions 35-55 (ILVLSVQAVTLILVIVNLGEL) is predominantly hydrophobic (~21 residues), consistent with a single-pass type II membrane anchor. The HN protein of paramyxoviruses is well-established as a type II membrane protein with one N-terminal TM anchor and a large extracellular domain, consistent with the annotation. The evidence is computational (by similarity) rather than experimentally determined, but the biology is well-supported.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple reasoning paths distinguish D from other choices: (1) Paramyxovirus HN proteins are well-known single-pass type II membrane proteins with one N-terminal TM anchor, eliminating multi-TM options A and C. (2) Option A contains segment 596..618 which exceeds the protein length of 582 aa, a clear factual error. (3) Hydrophobicity analysis of the N-terminal region reveals a hydrophobic stretch starting at position 35 (I-L-V-L-S-V-Q-A-V-T-L-I-L-V-I-V-N-L-G-E-L); position 34 is Arginine (charged), making a TM start at 33 (option B) biologically implausible since charged residues are strongly disfavored within the lipid bilayer. (4) The remainder of the protein (positions ~56-582) is dominated by charged/polar residues, glycosylation sites, and enzymatic (neuraminidase) domains, clearly extracellular, confirming a single-pass architecture.


**Missing item-specific fact**

> None critical. The exact boundary at 35 vs 33 can be argued from the charged Arg at position 34. The single-pass architecture is general paramyxovirus virology knowledge.


**Reason**

> The question provides sufficient sequence information and general biological context (paramyxovirus HN architecture, hydrophobicity principles, sequence length constraint) to reason toward the correct answer without memorizing a specific database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is eliminated by exceeding sequence length (596>582) and by the known single-pass architecture. Option C adds an unsupported second TM region. Option B includes a charged Arg at position 34 within the TM span, which is inconsistent with hydrophobic TM helix requirements. Option D is the only choice consistent with hydrophobicity analysis, single-pass architecture, and sequence length.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (by similarity), indicating computational/annotation-based assignment rather than direct experimental determination of the TM region.
- The exact TM boundaries (35-55) are somewhat approximate; the hydrophobic core could be argued to end slightly earlier (~50) or the polar residues at 51-55 might be considered interfacial rather than truly transmembrane. However, the annotation and hydrophobicity window support 35-55 as the best single answer.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning paths identified rely only on the supplied sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple reasoning paths distinguish D from other choices: (1) Paramyxovirus HN proteins are well-known single-pass type II membrane proteins with one N-terminal TM anchor, eliminating multi-TM options A and C. (2) Option A contains segment 596..618 which exceeds the protein length of 582 aa, a clear factual error. (3) Hydrophobicity analysis of the N-terminal region reveals a hydrophobic stretch starting at position 35 (I-L-V-L-S-V-Q-A-V-T-L-I-L-V-I-V-N-L-G-E-L); position 34 is Arginine (charged), making a TM start at 33 (option B) biologically implausible since charged residues are strongly disfavored within the lipid bilayer. (4) The remainder of the protein (positions ~56-582) is dominated by charged/polar residues, glycosylation sites, and enzymatic (neuraminidase) domains, clearly extracellular, confirming a single-pass architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The exact boundary at 35 vs 33 can be argued from the charged Arg at position 34. The single-pass architecture is general paramyxovirus virology knowledge.",
    "reason": "The question provides sufficient sequence information and general biological context (paramyxovirus HN architecture, hydrophobicity principles, sequence length constraint) to reason toward the correct answer without memorizing a specific database annotation."
  },
  "case_id": "transmembrane_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "C1",
      "C3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5SC51 (Mumps virus HN protein, 582 AA, sequence matched) annotates a single transmembrane helix at positions 35-55 (evidence code ECO:0000255, by similarity). The sequence at positions 35-55 (ILVLSVQAVTLILVIVNLGEL) is predominantly hydrophobic (~21 residues), consistent with a single-pass type II membrane anchor. The HN protein of paramyxoviruses is well-established as a type II membrane protein with one N-terminal TM anchor and a large extracellular domain, consistent with the annotation. The evidence is computational (by similarity) rather than experimentally determined, but the biology is well-supported."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (by similarity), indicating computational/annotation-based assignment rather than direct experimental determination of the TM region.",
    "The exact TM boundaries (35-55) are somewhat approximate; the hydrophobic core could be argued to end slightly earlier (~50) or the polar residues at 51-55 might be considered interfacial rather than truly transmembrane. However, the annotation and hydrophobicity window support 35-55 as the best single answer.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning paths identified rely only on the supplied sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by exceeding sequence length (596>582) and by the known single-pass architecture. Option C adds an unsupported second TM region. Option B includes a charged Arg at position 34 within the TM span, which is inconsistent with hydrophobic TM helix requirements. Option D is the only choice consistent with hydrophobicity analysis, single-pass architecture, and sequence length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5SC51 (Mumps virus HN protein, 582 AA, sequence matched) annotates a single transmembrane helix at positions 35-55 (evidence code ECO:0000255, by similarity). The sequence at positions 35-55 (ILVLSVQAVTLILVIVNLGEL) is predominantly hydrophobic (~21 residues), consistent with a single-pass type II membrane anchor. The HN protein of paramyxoviruses is well-established as a type II membrane protein with one N-terminal TM anchor and a large extracellular domain, consistent with the annotation. The evidence is computational (by similarity) rather than experimentally determined, but the biology is well-supported.",
    "evidence_ids": ["C5", "H2", "C1", "C3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple reasoning paths distinguish D from other choices: (1) Paramyxovirus HN proteins are well-known single-pass type II membrane proteins with one N-terminal TM anchor, eliminating multi-TM options A and C. (2) Option A contains segment 596..618 which exceeds the protein length of 582 aa, a clear factual error. (3) Hydrophobicity analysis of the N-terminal region reveals a hydrophobic stretch starting at position 35 (I-L-V-L-S-V-Q-A-V-T-L-I-L-V-I-V-N-L-G-E-L); position 34 is Arginine (charged), making a TM start at 33 (option B) biologically implausible since charged residues are strongly disfavored within the lipid bilayer. (4) The remainder of the protein (positions ~56-582) is dominated by charged/polar residues, glycosylation sites, and enzymatic (neuraminidase) domains, clearly extracellular, confirming a single-pass architecture.",
    "missing_item_specific_fact": "None critical. The exact boundary at 35 vs 33 can be argued from the charged Arg at position 34. The single-pass architecture is general paramyxovirus virology knowledge.",
    "reason": "The question provides sufficient sequence information and general biological context (paramyxovirus HN architecture, hydrophobicity principles, sequence length constraint) to reason toward the correct answer without memorizing a specific database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by exceeding sequence length (596>582) and by the known single-pass architecture. Option C adds an unsupported second TM region. Option B includes a charged Arg at position 34 within the TM span, which is inconsistent with hydrophobic TM helix requirements. Option D is the only choice consistent with hydrophobicity analysis, single-pass architecture, and sequence length."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (by similarity), indicating computational/annotation-based assignment rather than direct experimental determination of the TM region.",
    "The exact TM boundaries (35-55) are somewhat approximate; the hydrophobic core could be argued to end slightly earlier (~50) or the polar residues at 51-55 might be considered interfacial rather than truly transmembrane. However, the annotation and hydrophobicity window support 35-55 as the best single answer.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning paths identified rely only on the supplied sequence and general biological knowledge."
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

**Accession:** `Q5SC51` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 105. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
"Q5SC51"
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis","Mumps orthorubulavirus"],"scientificName":"Mumps virus genotype N (strain L-Zagreb vaccine)","taxonId":301186}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"value":"3.2.1.18"}],"fullName":{"value":"Hemagglutinin-neuraminidase"}}}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":55},"start":{"modifier":"EXACT","value":35}},"type":"Transmembrane"}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:31:32.054381+00:00.  

```text
FT   TRANSMEM        35..55
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 98. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
