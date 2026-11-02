# transmembrane_0113

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 35..55

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEPSKLFIMSDNATFAPGPVVNAAGKKTFRTCFRILVLSVQAVTLILVIVTLGELIRMINDQGLSNQLSSITDKIRESAAMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTNRNQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTIKERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPPQELDQRALRSYFPSYFSSRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGLGKCSGENICPTVCVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLARLTIT

[Multiple Choices]
A. 35..55
B. 30..52
C. 100..120; 135..155; 182..202; 228..248; 263..283; 293..313; 329..349
D. 35..55; 667..689
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

> The exact sequence match has a UniProt transmembrane annotation at 35–55 in both the current and archived records. The annotation is computational (ECO:0000255), so it supports the key as a database prediction, not as independently verified experimental evidence.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region around residues 35 onward contains a strongly hydrophobic, helix-compatible stretch, consistent with a membrane-spanning helix. Choice A fits that stretch; B includes additional upstream polar/basic residues, while C proposes numerous internal spans and D includes positions beyond the 582-residue sequence.


**Missing item-specific fact**

> No protein-specific fact is necessary to identify the likely N-terminal transmembrane region from these choices. An external annotation would be needed to establish the exact canonical endpoints rather than infer them from sequence.


**Reason**

> Sequence hydrophobicity and the contrast among the choices meaningfully favor A, although sequence-based reasoning alone does not establish exact boundaries with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> B overlaps the hydrophobic core identified by A and could be interpreted as a broader segment containing a membrane-crossing helix. A is the better match to the annotated boundaries; the wording does not explicitly say how strictly the endpoints must match.


### Important caveats

- The cited UniProt annotation is computational rather than direct experimental evidence.
- The archived and current records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region around residues 35 onward contains a strongly hydrophobic, helix-compatible stretch, consistent with a membrane-spanning helix. Choice A fits that stretch; B includes additional upstream polar/basic residues, while C proposes numerous internal spans and D includes positions beyond the 582-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific fact is necessary to identify the likely N-terminal transmembrane region from these choices. An external annotation would be needed to establish the exact canonical endpoints rather than infer them from sequence.",
    "reason": "Sequence hydrophobicity and the contrast among the choices meaningfully favor A, although sequence-based reasoning alone does not establish exact boundaries with certainty."
  },
  "case_id": "transmembrane_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt transmembrane annotation at 35–55 in both the current and archived records. The annotation is computational (ECO:0000255), so it supports the key as a database prediction, not as independently verified experimental evidence."
  },
  "important_caveats": [
    "The cited UniProt annotation is computational rather than direct experimental evidence.",
    "The archived and current records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "B overlaps the hydrophobic core identified by A and could be interpreted as a broader segment containing a membrane-crossing helix. A is the better match to the annotated boundaries; the wording does not explicitly say how strictly the endpoints must match."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt transmembrane annotation at 35–55 in both the current and archived records. The annotation is computational (ECO:0000255), so it supports the key as a database prediction, not as independently verified experimental evidence.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region around residues 35 onward contains a strongly hydrophobic, helix-compatible stretch, consistent with a membrane-spanning helix. Choice A fits that stretch; B includes additional upstream polar/basic residues, while C proposes numerous internal spans and D includes positions beyond the 582-residue sequence.",
    "missing_item_specific_fact": "No protein-specific fact is necessary to identify the likely N-terminal transmembrane region from these choices. An external annotation would be needed to establish the exact canonical endpoints rather than infer them from sequence.",
    "reason": "Sequence hydrophobicity and the contrast among the choices meaningfully favor A, although sequence-based reasoning alone does not establish exact boundaries with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "B overlaps the hydrophobic core identified by A and could be interpreted as a broader segment containing a membrane-crossing helix. A is the better match to the annotated boundaries; the wording does not explicitly say how strictly the endpoints must match."
  },
  "important_caveats": [
    "The cited UniProt annotation is computational rather than direct experimental evidence.",
    "The archived and current records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q8QV65 (Mumps virus Hemagglutinin-neuraminidase, 582 AA, sequence SHA256 matched) annotates exactly one transmembrane helical region at positions 35..55 (evidence C5, H2). The evidence code is ECO:0000255 (inferred by similarity), so this is a computational transfer rather than an experimental determination, but the annotation is consistent with the known type II membrane topology of paramyxovirus HN proteins, which possess a single N-terminal transmembrane anchor. The expected answer A (35..55) matches the annotation exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence from approximately position 35 (I) to 55 (L) forms a highly hydrophobic 21-residue stretch (ILVLSVQAVTLILVIVTLGEL) consistent with a single-pass TM helix. Option B (30..52) includes charged arginine residues at positions 30 and 34, which are energetically unfavorable within the lipid bilayer core, making it a weaker TM candidate. Option C lists seven TM regions in the extracellular domain (e.g., 100..120 = LPLQIEGNQNQLLSTLATIC) containing numerous polar and charged residues (Q, E, N, S, T, C) inconsistent with membrane-spanning helices. Option D includes positions 667..689, which exceed the 582-residue protein length and are therefore impossible. These biological arguments concretely eliminate B, C, and D, leaving A.


**Missing item-specific fact**

> None critical. The exact boundary at position 55 (rather than 52, where a helix-breaking Gly and charged Glu appear) is somewhat tool-dependent, but among the given choices, A is uniquely defensible by hydrophobicity and length arguments.


**Reason**

> A model with general knowledge of membrane protein topology, hydrophobicity scales, and the constraint that a TM helix cannot include the protein's C-terminus beyond its length can eliminate C (extracellular polar regions), D (impossible coordinates), and B (charged R residues at 30 and 34), arriving at A. The reasoning relies on sequence-level hydrophobicity analysis and biological constraints, not on recalling a specific database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is eliminated by protein length (582 AA < 667). Option C is eliminated by the polar/charged composition of the listed regions. Option B is disfavored by the inclusion of two arginine residues (positions 30, 34) within the proposed helix. Only A presents a contiguous hydrophobic stretch of appropriate length (21 residues) without buried charges.


### Important caveats

- The UniProt TM annotation uses ECO:0000255 (inferred by similarity), meaning it is a computational prediction transferred from a homolog, not an experimentally validated boundary.
- The exact end boundary (55 vs ~52) is somewhat arbitrary; position 53 is Gly (helix breaker) and 54 is Glu (charged). However, among the provided choices, only A is fully defensible.
- The protein is a type II membrane protein (N-terminal TM anchor, large C-terminal extracellular domain), consistent with a single TM helix near the N-terminus.
- All reviewer evidence is sequence-matched (SHA256 identical) and applies to the supplied 582-residue sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence from approximately position 35 (I) to 55 (L) forms a highly hydrophobic 21-residue stretch (ILVLSVQAVTLILVIVTLGEL) consistent with a single-pass TM helix. Option B (30..52) includes charged arginine residues at positions 30 and 34, which are energetically unfavorable within the lipid bilayer core, making it a weaker TM candidate. Option C lists seven TM regions in the extracellular domain (e.g., 100..120 = LPLQIEGNQNQLLSTLATIC) containing numerous polar and charged residues (Q, E, N, S, T, C) inconsistent with membrane-spanning helices. Option D includes positions 667..689, which exceed the 582-residue protein length and are therefore impossible. These biological arguments concretely eliminate B, C, and D, leaving A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The exact boundary at position 55 (rather than 52, where a helix-breaking Gly and charged Glu appear) is somewhat tool-dependent, but among the given choices, A is uniquely defensible by hydrophobicity and length arguments.",
    "reason": "A model with general knowledge of membrane protein topology, hydrophobicity scales, and the constraint that a TM helix cannot include the protein's C-terminus beyond its length can eliminate C (extracellular polar regions), D (impossible coordinates), and B (charged R residues at 30 and 34), arriving at A. The reasoning relies on sequence-level hydrophobicity analysis and biological constraints, not on recalling a specific database annotation."
  },
  "case_id": "transmembrane_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt Q8QV65 (Mumps virus Hemagglutinin-neuraminidase, 582 AA, sequence SHA256 matched) annotates exactly one transmembrane helical region at positions 35..55 (evidence C5, H2). The evidence code is ECO:0000255 (inferred by similarity), so this is a computational transfer rather than an experimental determination, but the annotation is consistent with the known type II membrane topology of paramyxovirus HN proteins, which possess a single N-terminal transmembrane anchor. The expected answer A (35..55) matches the annotation exactly."
  },
  "important_caveats": [
    "The UniProt TM annotation uses ECO:0000255 (inferred by similarity), meaning it is a computational prediction transferred from a homolog, not an experimentally validated boundary.",
    "The exact end boundary (55 vs ~52) is somewhat arbitrary; position 53 is Gly (helix breaker) and 54 is Glu (charged). However, among the provided choices, only A is fully defensible.",
    "The protein is a type II membrane protein (N-terminal TM anchor, large C-terminal extracellular domain), consistent with a single TM helix near the N-terminus.",
    "All reviewer evidence is sequence-matched (SHA256 identical) and applies to the supplied 582-residue sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated by protein length (582 AA < 667). Option C is eliminated by the polar/charged composition of the listed regions. Option B is disfavored by the inclusion of two arginine residues (positions 30, 34) within the proposed helix. Only A presents a contiguous hydrophobic stretch of appropriate length (21 residues) without buried charges."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q8QV65 (Mumps virus Hemagglutinin-neuraminidase, 582 AA, sequence SHA256 matched) annotates exactly one transmembrane helical region at positions 35..55 (evidence C5, H2). The evidence code is ECO:0000255 (inferred by similarity), so this is a computational transfer rather than an experimental determination, but the annotation is consistent with the known type II membrane topology of paramyxovirus HN proteins, which possess a single N-terminal transmembrane anchor. The expected answer A (35..55) matches the annotation exactly.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence from approximately position 35 (I) to 55 (L) forms a highly hydrophobic 21-residue stretch (ILVLSVQAVTLILVIVTLGEL) consistent with a single-pass TM helix. Option B (30..52) includes charged arginine residues at positions 30 and 34, which are energetically unfavorable within the lipid bilayer core, making it a weaker TM candidate. Option C lists seven TM regions in the extracellular domain (e.g., 100..120 = LPLQIEGNQNQLLSTLATIC) containing numerous polar and charged residues (Q, E, N, S, T, C) inconsistent with membrane-spanning helices. Option D includes positions 667..689, which exceed the 582-residue protein length and are therefore impossible. These biological arguments concretely eliminate B, C, and D, leaving A.",
    "missing_item_specific_fact": "None critical. The exact boundary at position 55 (rather than 52, where a helix-breaking Gly and charged Glu appear) is somewhat tool-dependent, but among the given choices, A is uniquely defensible by hydrophobicity and length arguments.",
    "reason": "A model with general knowledge of membrane protein topology, hydrophobicity scales, and the constraint that a TM helix cannot include the protein's C-terminus beyond its length can eliminate C (extracellular polar regions), D (impossible coordinates), and B (charged R residues at 30 and 34), arriving at A. The reasoning relies on sequence-level hydrophobicity analysis and biological constraints, not on recalling a specific database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated by protein length (582 AA < 667). Option C is eliminated by the polar/charged composition of the listed regions. Option B is disfavored by the inclusion of two arginine residues (positions 30, 34) within the proposed helix. Only A presents a contiguous hydrophobic stretch of appropriate length (21 residues) without buried charges."
  },
  "important_caveats": [
    "The UniProt TM annotation uses ECO:0000255 (inferred by similarity), meaning it is a computational prediction transferred from a homolog, not an experimentally validated boundary.",
    "The exact end boundary (55 vs ~52) is somewhat arbitrary; position 53 is Gly (helix breaker) and 54 is Glu (charged). However, among the provided choices, only A is fully defensible.",
    "The protein is a type II membrane protein (N-terminal TM anchor, large C-terminal extracellular domain), consistent with a single TM helix near the N-terminus.",
    "All reviewer evidence is sequence-matched (SHA256 identical) and applies to the supplied 582-residue sequence."
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

**Accession:** `Q8QV65` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
"Q8QV65"
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"value":"3.2.1.18"}],"fullName":{"value":"Hemagglutinin-neuraminidase"}}}
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8QV65.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:24.225587+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":55},"start":{"modifier":"EXACT","value":35}},"type":"Transmembrane"}
```

Source SHA-256: `bc4438119d1c029de1baa6feae7ea6afaed8e7e0d19410c4fed725f8fcb3753b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:32:27.640645+00:00.  

```text
ID   HN_MUMPJ                Reviewed;         582 AA.
AC   Q8QV65; C7C5S5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2002, sequence version 1.
DT   28-JAN-2026, entry version 114.
DE   RecName: Full=Hemagglutinin-neuraminidase;
DE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};
GN   Name=HN;
OS   Mumps virus genotype A (strain Jeryl-Lynn) (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.
OX   NCBI_TaxID=11168;
OH   NCBI_TaxID=9606; Homo sapiens (Human).
```

Source SHA-256: `32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8QV65?format=txt&versions=114)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:32:27.640645+00:00.  

```text
FT   TRANSMEM        35..55
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `32a38cacb11cc75414f260107fe816d041e5d43d9075624a51461e99158215ec`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 113. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
