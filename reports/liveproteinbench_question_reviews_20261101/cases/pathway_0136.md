# pathway_0136

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLKSLVVLLLTSRVIAFPTLDTDQTAALHKPQATPNSQGTHGGFFYYWWSDGQSPAAYTNLDGGSYCLRWESGGNLIGGKGWSPGTDNRTIQISGTFQGVENSYLAVYGWLETPKVEYYIVEYHGVFNPAYDAQILGTVICDGSVYDISRSTRVSSGGTKILPRYWSVRRNKRTGGTVQTGCHFDAWRSTGLSAADHGFQIVATEGYFSSGFAEMTVADTSAEE

[Multiple Choices]
A. molybdopterin biosynthesis. .
B. Glycan degradation
C. LPS O-antigen biosynthesis. .
D. L-threonine from L-aspartate: step 1/5. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as endo-1,4-beta-xylanase EIX5, with the pathway “Glycan degradation; xylan degradation.” The pathway annotation is computationally supported by a PROSITE-ProRule, not shown here as direct experimental evidence for pathway activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, which makes extracellular glycan degradation more plausible than the listed biosynthetic pathways. But that clue alone does not establish xylanase activity or identify the pathway.


**Missing item-specific fact**

> That this particular sequence is annotated as EIX5, an endo-1,4-beta-xylanase, and is assigned to xylan degradation.


**Reason**

> The sequence and choices provide a suggestive secretion-based clue, but distinguishing the pathway depends on protein-specific functional identification. The reviewer-only annotation supports the key but was not supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the matched-sequence xylanase annotation, glycan degradation is the only listed choice that fits.


### Important caveats

- The pathway annotation is attributed to a PROSITE-ProRule; it should not be represented as direct experimental validation of the pathway assignment.
- The cited paper concerns perception of an EIX-like protein, which is not itself evidence of xylan degradation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, which makes extracellular glycan degradation more plausible than the listed biosynthetic pathways. But that clue alone does not establish xylanase activity or identify the pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular sequence is annotated as EIX5, an endo-1,4-beta-xylanase, and is assigned to xylan degradation.",
    "reason": "The sequence and choices provide a suggestive secretion-based clue, but distinguishing the pathway depends on protein-specific functional identification. The reviewer-only annotation supports the key but was not supplied to the model."
  },
  "case_id": "pathway_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as endo-1,4-beta-xylanase EIX5, with the pathway “Glycan degradation; xylan degradation.” The pathway annotation is computationally supported by a PROSITE-ProRule, not shown here as direct experimental evidence for pathway activity."
  },
  "important_caveats": [
    "The pathway annotation is attributed to a PROSITE-ProRule; it should not be represented as direct experimental validation of the pathway assignment.",
    "The cited paper concerns perception of an EIX-like protein, which is not itself evidence of xylan degradation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched-sequence xylanase annotation, glycan degradation is the only listed choice that fits."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as endo-1,4-beta-xylanase EIX5, with the pathway “Glycan degradation; xylan degradation.” The pathway annotation is computationally supported by a PROSITE-ProRule, not shown here as direct experimental evidence for pathway activity.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, which makes extracellular glycan degradation more plausible than the listed biosynthetic pathways. But that clue alone does not establish xylanase activity or identify the pathway.",
    "missing_item_specific_fact": "That this particular sequence is annotated as EIX5, an endo-1,4-beta-xylanase, and is assigned to xylan degradation.",
    "reason": "The sequence and choices provide a suggestive secretion-based clue, but distinguishing the pathway depends on protein-specific functional identification. The reviewer-only annotation supports the key but was not supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched-sequence xylanase annotation, glycan degradation is the only listed choice that fits."
  },
  "important_caveats": [
    "The pathway annotation is attributed to a PROSITE-ProRule; it should not be represented as direct experimental validation of the pathway assignment.",
    "The cited paper concerns perception of an EIX-like protein, which is not itself evidence of xylan degradation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G2X4G1 (sequence matched exactly, 224 AA) annotates this protein as Ethylene-inducing xylanase 5 (EIX5), EC 3.2.1.8 (Endo-1,4-beta-xylanase), with pathway 'Glycan degradation; xylan degradation' (evidence code ECO:0000255|PROSITE-ProRule:PRU01097). This directly supports option B. The annotation is based on PROSITE-ProRule family assignment (computational inference from conserved motifs) rather than direct experimental pathway tracing, but the EC assignment as a xylanase and the pathway classification are well-established for GH11 xylanases.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmarks of a secreted glycoside hydrolase: (1) a clear N-terminal hydrophobic signal peptide (MLKSLVVLLLTSRVIAFPT) indicating secretion, consistent with an extracellular degradative enzyme; (2) multiple 'GG' dipeptide repeats (GGFFYYWW, GGSYCLRWESGG, GGKGWSPG, GSVYDISRSTRVSSGG, GGTKILPRYWSVRRNKRTGG) and tryptophan clusters characteristic of the GH11 xylanase 'beta-jelly roll' fold; (3) glutamate residues in EY contexts (VEYYIVEYHGVFNPAY) consistent with GH11 catalytic dyad motifs. Among the four options, only 'Glycan degradation' is compatible with a secreted glycoside hydrolase. The distractors are clearly incompatible: LPS O-antigen biosynthesis is a bacterial pathway (this is a eukaryotic/fungal protein); molybdopterin biosynthesis involves radical SAM enzymes (MoaA) and small sulfur-transfer proteins with entirely different sequence architecture; aspartate kinase (threonine step 1) is a large cytoplasmic regulatory enzyme with ACT domains, not a small secreted protein.


**Missing item-specific fact**

> None critically missing. Positive identification of the exact GH11 xylanase family requires recognizing specific catalytic motifs, but elimination of the three clearly incompatible distractors is achievable through general biological knowledge (LPS is bacterial; molybdopterin/threonine enzymes have different folds and cellular localization).


**Reason**

> A model with general biological knowledge can reason that: (a) the signal peptide and small size suggest a secreted degradative enzyme; (b) the GG/W-rich composition is suggestive of a glycoside hydrolase; (c) LPS biosynthesis is exclusively bacterial; (d) molybdopterin and threonine biosynthesis enzymes have completely different sequence characteristics and are not secreted. This elimination-based reasoning, combined with the suggestive sequence composition, provides meaningful grounds to select B without memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option B is compatible with the sequence features. LPS O-antigen biosynthesis (C) is a bacterial pathway incompatible with a eukaryotic secreted protein. Molybdopterin biosynthesis (A) and aspartate kinase (D) involve enzymes with entirely different structural classes and cellular localization. No ambiguity among the choices.


### Important caveats

- The UniProt pathway annotation uses evidence code ECO:0000255 (PROSITE-ProRule), indicating computational family assignment rather than direct experimental pathway tracing. However, EC 3.2.1.8 (xylanase) is a well-characterized enzyme class whose pathway role is unambiguous.
- The protein was first integrated into Swiss-Prot on 2025-06-18 (entry version 57 archived at 2026-01-28). The benchmark construction date relative to this annotation is uncertain.
- The accession G2X4G1 was inferred by the reviewer from dataset image-path metadata; the evaluated model received only the raw sequence.
- The 'ethylene-inducing' activity (elicitor function) noted in the literature (PubMed 33205907) is a separate biological role from the xylanase catalytic activity; the pathway annotation refers to the enzymatic function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmarks of a secreted glycoside hydrolase: (1) a clear N-terminal hydrophobic signal peptide (MLKSLVVLLLTSRVIAFPT) indicating secretion, consistent with an extracellular degradative enzyme; (2) multiple 'GG' dipeptide repeats (GGFFYYWW, GGSYCLRWESGG, GGKGWSPG, GSVYDISRSTRVSSGG, GGTKILPRYWSVRRNKRTGG) and tryptophan clusters characteristic of the GH11 xylanase 'beta-jelly roll' fold; (3) glutamate residues in EY contexts (VEYYIVEYHGVFNPAY) consistent with GH11 catalytic dyad motifs. Among the four options, only 'Glycan degradation' is compatible with a secreted glycoside hydrolase. The distractors are clearly incompatible: LPS O-antigen biosynthesis is a bacterial pathway (this is a eukaryotic/fungal protein); molybdopterin biosynthesis involves radical SAM enzymes (MoaA) and small sulfur-transfer proteins with entirely different sequence architecture; aspartate kinase (threonine step 1) is a large cytoplasmic regulatory enzyme with ACT domains, not a small secreted protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critically missing. Positive identification of the exact GH11 xylanase family requires recognizing specific catalytic motifs, but elimination of the three clearly incompatible distractors is achievable through general biological knowledge (LPS is bacterial; molybdopterin/threonine enzymes have different folds and cellular localization).",
    "reason": "A model with general biological knowledge can reason that: (a) the signal peptide and small size suggest a secreted degradative enzyme; (b) the GG/W-rich composition is suggestive of a glycoside hydrolase; (c) LPS biosynthesis is exclusively bacterial; (d) molybdopterin and threonine biosynthesis enzymes have completely different sequence characteristics and are not secreted. This elimination-based reasoning, combined with the suggestive sequence composition, provides meaningful grounds to select B without memorizing this specific UniProt entry."
  },
  "case_id": "pathway_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G2X4G1 (sequence matched exactly, 224 AA) annotates this protein as Ethylene-inducing xylanase 5 (EIX5), EC 3.2.1.8 (Endo-1,4-beta-xylanase), with pathway 'Glycan degradation; xylan degradation' (evidence code ECO:0000255|PROSITE-ProRule:PRU01097). This directly supports option B. The annotation is based on PROSITE-ProRule family assignment (computational inference from conserved motifs) rather than direct experimental pathway tracing, but the EC assignment as a xylanase and the pathway classification are well-established for GH11 xylanases."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses evidence code ECO:0000255 (PROSITE-ProRule), indicating computational family assignment rather than direct experimental pathway tracing. However, EC 3.2.1.8 (xylanase) is a well-characterized enzyme class whose pathway role is unambiguous.",
    "The protein was first integrated into Swiss-Prot on 2025-06-18 (entry version 57 archived at 2026-01-28). The benchmark construction date relative to this annotation is uncertain.",
    "The accession G2X4G1 was inferred by the reviewer from dataset image-path metadata; the evaluated model received only the raw sequence.",
    "The 'ethylene-inducing' activity (elicitor function) noted in the literature (PubMed 33205907) is a separate biological role from the xylanase catalytic activity; the pathway annotation refers to the enzymatic function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B is compatible with the sequence features. LPS O-antigen biosynthesis (C) is a bacterial pathway incompatible with a eukaryotic secreted protein. Molybdopterin biosynthesis (A) and aspartate kinase (D) involve enzymes with entirely different structural classes and cellular localization. No ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G2X4G1 (sequence matched exactly, 224 AA) annotates this protein as Ethylene-inducing xylanase 5 (EIX5), EC 3.2.1.8 (Endo-1,4-beta-xylanase), with pathway 'Glycan degradation; xylan degradation' (evidence code ECO:0000255|PROSITE-ProRule:PRU01097). This directly supports option B. The annotation is based on PROSITE-ProRule family assignment (computational inference from conserved motifs) rather than direct experimental pathway tracing, but the EC assignment as a xylanase and the pathway classification are well-established for GH11 xylanases.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmarks of a secreted glycoside hydrolase: (1) a clear N-terminal hydrophobic signal peptide (MLKSLVVLLLTSRVIAFPT) indicating secretion, consistent with an extracellular degradative enzyme; (2) multiple 'GG' dipeptide repeats (GGFFYYWW, GGSYCLRWESGG, GGKGWSPG, GSVYDISRSTRVSSGG, GGTKILPRYWSVRRNKRTGG) and tryptophan clusters characteristic of the GH11 xylanase 'beta-jelly roll' fold; (3) glutamate residues in EY contexts (VEYYIVEYHGVFNPAY) consistent with GH11 catalytic dyad motifs. Among the four options, only 'Glycan degradation' is compatible with a secreted glycoside hydrolase. The distractors are clearly incompatible: LPS O-antigen biosynthesis is a bacterial pathway (this is a eukaryotic/fungal protein); molybdopterin biosynthesis involves radical SAM enzymes (MoaA) and small sulfur-transfer proteins with entirely different sequence architecture; aspartate kinase (threonine step 1) is a large cytoplasmic regulatory enzyme with ACT domains, not a small secreted protein.",
    "missing_item_specific_fact": "None critically missing. Positive identification of the exact GH11 xylanase family requires recognizing specific catalytic motifs, but elimination of the three clearly incompatible distractors is achievable through general biological knowledge (LPS is bacterial; molybdopterin/threonine enzymes have different folds and cellular localization).",
    "reason": "A model with general biological knowledge can reason that: (a) the signal peptide and small size suggest a secreted degradative enzyme; (b) the GG/W-rich composition is suggestive of a glycoside hydrolase; (c) LPS biosynthesis is exclusively bacterial; (d) molybdopterin and threonine biosynthesis enzymes have completely different sequence characteristics and are not secreted. This elimination-based reasoning, combined with the suggestive sequence composition, provides meaningful grounds to select B without memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B is compatible with the sequence features. LPS O-antigen biosynthesis (C) is a bacterial pathway incompatible with a eukaryotic secreted protein. Molybdopterin biosynthesis (A) and aspartate kinase (D) involve enzymes with entirely different structural classes and cellular localization. No ambiguity among the choices."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses evidence code ECO:0000255 (PROSITE-ProRule), indicating computational family assignment rather than direct experimental pathway tracing. However, EC 3.2.1.8 (xylanase) is a well-characterized enzyme class whose pathway role is unambiguous.",
    "The protein was first integrated into Swiss-Prot on 2025-06-18 (entry version 57 archived at 2026-01-28). The benchmark construction date relative to this annotation is uncertain.",
    "The accession G2X4G1 was inferred by the reviewer from dataset image-path metadata; the evaluated model received only the raw sequence.",
    "The 'ethylene-inducing' activity (elicitor function) noted in the literature (PubMed 33205907) is a separate biological role from the xylanase catalytic activity; the pathway annotation refers to the enzymatic function."
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

**Accession:** `G2X4G1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 57. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.575092+00:00.  

```json
"G2X4G1"
```

Source SHA-256: `1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.575092+00:00.  

```json
{"commonName":"Verticillium wilt","lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Sordariomycetes","Hypocreomycetidae","Glomerellales","Plectosphaerellaceae","Verticillium"],"scientificName":"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)","taxonId":498257}
```

Source SHA-256: `1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.575092+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX5"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 5"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX5"}]}}
```

Source SHA-256: `1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.575092+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:04.705992+00:00.  

```text
ID   EIX5_VERDV              Reviewed;         224 AA.
AC   G2X4G1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-NOV-2011, sequence version 1.
DT   28-JAN-2026, entry version 57.
DE   RecName: Full=Ethylene-inducing xylanase 5 {ECO:0000303|PubMed:33205907};
DE            Short=EIX5 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX5 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX5 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_05043;
OS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)
OS   (Verticillium wilt).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.
OX   NCBI_TaxID=498257;
```

Source SHA-256: `e0c511e580167b3398281d34cf1b42f13481b77974f64acc52440d0b06a7af8b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57)  
**Locator:** `lines 47-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 57 / 1.  
**Retrieved:** 2026-11-01T06:28:04.705992+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-
CC       ProRule:PRU01097}.
```

Source SHA-256: `e0c511e580167b3398281d34cf1b42f13481b77974f64acc52440d0b06a7af8b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
