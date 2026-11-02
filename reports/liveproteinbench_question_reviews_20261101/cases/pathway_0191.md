# pathway_0191

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFKSLLLAASAFTAVLGRPFDSFDGPDVNITDADELLVRRQVTANSEGTHNGYFYSWWSDGGGQVTYTMGAGSRYSVTWKDTGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGWTRNPLIEYYVVESYGTYNPGSGGQLKGTVTTDGGTYNVYVSTRTNQPSIDGTRTFQQYWSVRTSKRVGGAVTMQNHFNAWAQFGMNLGAHYYQIVATEGNGDFVGTEIWGLARGCRR

[Multiple Choices]
A. Antifungal biosynthesis. .
B. iron-sulfur cluster biosynthesis. .
C. terpenoid biosynthesis.
D. Glycan degradation
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

> The supplied sequence exactly matches the historical sequence for an entry annotated as a xylanase (EC 3.2.1.8) and assigned to glycan/xylan degradation. The pathway assignment is computationally supported by a PROSITE-ProRule annotation; it is not, by itself, direct experimental evidence for the pathway.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a likely secretion signal and enzyme-like features, but those general clues do not identify its specific substrate or distinguish xylan degradation from the other listed pathways.


**Missing item-specific fact**

> The protein's xylanase identity and activity (EC 3.2.1.8), or an equivalent protein-specific functional annotation, are needed to select glycan degradation.


**Reason**

> Choosing D requires a protein-specific functional fact not supplied in the question. Recognizing the exact sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided choices and sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the xylanase annotation, glycan degradation is the distinct matching option; the other choices do not describe xylan breakdown.


### Important caveats

- The matching historical record supports the annotation's applicability to this sequence; the current UniProt sequence differs.
- The pathway annotation is attributed to a PROSITE-ProRule, so it should be distinguished from direct experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a likely secretion signal and enzyme-like features, but those general clues do not identify its specific substrate or distinguish xylan degradation from the other listed pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's xylanase identity and activity (EC 3.2.1.8), or an equivalent protein-specific functional annotation, are needed to select glycan degradation.",
    "reason": "Choosing D requires a protein-specific functional fact not supplied in the question. Recognizing the exact sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided choices and sequence alone."
  },
  "case_id": "pathway_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical sequence for an entry annotated as a xylanase (EC 3.2.1.8) and assigned to glycan/xylan degradation. The pathway assignment is computationally supported by a PROSITE-ProRule annotation; it is not, by itself, direct experimental evidence for the pathway."
  },
  "important_caveats": [
    "The matching historical record supports the annotation's applicability to this sequence; the current UniProt sequence differs.",
    "The pathway annotation is attributed to a PROSITE-ProRule, so it should be distinguished from direct experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the xylanase annotation, glycan degradation is the distinct matching option; the other choices do not describe xylan breakdown."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0191",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical sequence for an entry annotated as a xylanase (EC 3.2.1.8) and assigned to glycan/xylan degradation. The pathway assignment is computationally supported by a PROSITE-ProRule annotation; it is not, by itself, direct experimental evidence for the pathway.",
    "evidence_ids": ["H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a likely secretion signal and enzyme-like features, but those general clues do not identify its specific substrate or distinguish xylan degradation from the other listed pathways.",
    "missing_item_specific_fact": "The protein's xylanase identity and activity (EC 3.2.1.8), or an equivalent protein-specific functional annotation, are needed to select glycan degradation.",
    "reason": "Choosing D requires a protein-specific functional fact not supplied in the question. Recognizing the exact sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided choices and sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the xylanase annotation, glycan degradation is the distinct matching option; the other choices do not describe xylan breakdown."
  },
  "important_caveats": [
    "The matching historical record supports the annotation's applicability to this sequence; the current UniProt sequence differs.",
    "The pathway annotation is attributed to a PROSITE-ProRule, so it should be distinguished from direct experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The historical UniProt entry G2X0L1 (entry version 60, sequence version 1, 237 AA) matches the benchmark sequence exactly (sha256 confirmed). The entry annotates the protein as Ethylene-inducing xylanase 2 (EIX2) with EC 3.2.1.8 (endo-1,4-beta-xylanase) and explicitly states PATHWAY: Glycan degradation; xylan degradation (ECO:0000255|PROSITE-ProRule:PRU01097). The EC number assignment is additionally supported by experimental evidence (PubMed:18720841, ECO:0000269). Xylanases are glycoside hydrolases that degrade xylan, a polysaccharide (glycan), making 'Glycan degradation' the correct pathway classification.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cleavable N-terminal signal peptide (MVSFKSLLLAASAFTAVLGRPF...) indicating a secreted protein. The core domain exhibits hallmarks of glycoside hydrolase family 11 (GH11): the 'WWSDGGGQ' catalytic motif, the 'GWNPGTGRT' and 'GGSFSPQGNGYLAVYGWTRNPLIEYYVVESYGTYNPGSGGQLKGTVTTDGGTYNVYVSTRTNQPSIDGTRTFQQYWSVRTSKRVGGAVTMQNHFNAWAQFGMNLGAHYYQIVATEGNGDFVGTEIWGLARGCRR' β-jelly-roll pattern characteristic of GH11 xylanases. A small (~237 AA) secreted fungal protein with these carbohydrate-active enzyme motifs points to glycan (xylan) degradation. Options B (Fe-S cluster biosynthesis) and C (terpenoid biosynthesis) are eliminated by absence of Fe-S cluster motifs and terpene synthase motifs respectively. Option A (antifungal biosynthesis) is implausible for a secreted fungal enzyme; antifungal pathways typically involve large NRPS/PKS assembly lines or plant defense responses, not small secreted hydrolases.


**Missing item-specific fact**

> None strictly required, though confident positive identification of the GH11 fold from sequence alone requires specialized knowledge of glycoside hydrolase family motifs (particularly the WWSDGGGQ signature). General elimination of B and C is straightforward; distinguishing D from A benefits from recognizing carbohydrate-active enzyme architecture.


**Reason**

> The sequence provides concrete structural motifs (GH11 catalytic and binding signatures) that a knowledgeable model can use to infer glycoside hydrolase function. The elimination of Fe-S cluster biosynthesis and terpenoid biosynthesis is straightforward from absence of relevant motifs. The distinction between glycan degradation and antifungal biosynthesis relies on recognizing the protein as a secreted hydrolase rather than a biosynthetic enzyme, which is supported by sequence features (small size, signal peptide, GH11 motifs).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated biologically. Fe-S cluster biosynthesis requires Fe-S cluster motifs (CX2CX4C or similar), terpenoid biosynthesis requires terpene cyclase motifs, and antifungal biosynthesis implies large multi-domain assembly enzymes. The GH11 xylanase fold is distinctive enough to unambiguously point to glycan degradation.


### Important caveats

- The current UniProt sequence (version 2, 250 AA) differs from the benchmark sequence (version 1, 237 AA); however, the historical entry (version 60) matches exactly, confirming the annotation applies to the supplied sequence.
- The pathway annotation carries ECO:0000255 (PROSITE-ProRule), a computational annotation based on sequence similarity to characterized xylanases, though the EC number has independent experimental support (PubMed:18720841).
- EIX2 also functions as an ethylene-inducing elicitor in plant-pathogen interactions (PubMed:33205907), but its enzymatic pathway classification is glycan degradation, not signaling biosynthesis.
- The accession G2X0L1 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must rely solely on sequence analysis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cleavable N-terminal signal peptide (MVSFKSLLLAASAFTAVLGRPF...) indicating a secreted protein. The core domain exhibits hallmarks of glycoside hydrolase family 11 (GH11): the 'WWSDGGGQ' catalytic motif, the 'GWNPGTGRT' and 'GGSFSPQGNGYLAVYGWTRNPLIEYYVVESYGTYNPGSGGQLKGTVTTDGGTYNVYVSTRTNQPSIDGTRTFQQYWSVRTSKRVGGAVTMQNHFNAWAQFGMNLGAHYYQIVATEGNGDFVGTEIWGLARGCRR' β-jelly-roll pattern characteristic of GH11 xylanases. A small (~237 AA) secreted fungal protein with these carbohydrate-active enzyme motifs points to glycan (xylan) degradation. Options B (Fe-S cluster biosynthesis) and C (terpenoid biosynthesis) are eliminated by absence of Fe-S cluster motifs and terpene synthase motifs respectively. Option A (antifungal biosynthesis) is implausible for a secreted fungal enzyme; antifungal pathways typically involve large NRPS/PKS assembly lines or plant defense responses, not small secreted hydrolases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required, though confident positive identification of the GH11 fold from sequence alone requires specialized knowledge of glycoside hydrolase family motifs (particularly the WWSDGGGQ signature). General elimination of B and C is straightforward; distinguishing D from A benefits from recognizing carbohydrate-active enzyme architecture.",
    "reason": "The sequence provides concrete structural motifs (GH11 catalytic and binding signatures) that a knowledgeable model can use to infer glycoside hydrolase function. The elimination of Fe-S cluster biosynthesis and terpenoid biosynthesis is straightforward from absence of relevant motifs. The distinction between glycan degradation and antifungal biosynthesis relies on recognizing the protein as a secreted hydrolase rather than a biosynthetic enzyme, which is supported by sequence features (small size, signal peptide, GH11 motifs)."
  },
  "case_id": "pathway_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The historical UniProt entry G2X0L1 (entry version 60, sequence version 1, 237 AA) matches the benchmark sequence exactly (sha256 confirmed). The entry annotates the protein as Ethylene-inducing xylanase 2 (EIX2) with EC 3.2.1.8 (endo-1,4-beta-xylanase) and explicitly states PATHWAY: Glycan degradation; xylan degradation (ECO:0000255|PROSITE-ProRule:PRU01097). The EC number assignment is additionally supported by experimental evidence (PubMed:18720841, ECO:0000269). Xylanases are glycoside hydrolases that degrade xylan, a polysaccharide (glycan), making 'Glycan degradation' the correct pathway classification."
  },
  "important_caveats": [
    "The current UniProt sequence (version 2, 250 AA) differs from the benchmark sequence (version 1, 237 AA); however, the historical entry (version 60) matches exactly, confirming the annotation applies to the supplied sequence.",
    "The pathway annotation carries ECO:0000255 (PROSITE-ProRule), a computational annotation based on sequence similarity to characterized xylanases, though the EC number has independent experimental support (PubMed:18720841).",
    "EIX2 also functions as an ethylene-inducing elicitor in plant-pathogen interactions (PubMed:33205907), but its enzymatic pathway classification is glycan degradation, not signaling biosynthesis.",
    "The accession G2X0L1 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must rely solely on sequence analysis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated biologically. Fe-S cluster biosynthesis requires Fe-S cluster motifs (CX2CX4C or similar), terpenoid biosynthesis requires terpene cyclase motifs, and antifungal biosynthesis implies large multi-domain assembly enzymes. The GH11 xylanase fold is distinctive enough to unambiguously point to glycan degradation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0191",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The historical UniProt entry G2X0L1 (entry version 60, sequence version 1, 237 AA) matches the benchmark sequence exactly (sha256 confirmed). The entry annotates the protein as Ethylene-inducing xylanase 2 (EIX2) with EC 3.2.1.8 (endo-1,4-beta-xylanase) and explicitly states PATHWAY: Glycan degradation; xylan degradation (ECO:0000255|PROSITE-ProRule:PRU01097). The EC number assignment is additionally supported by experimental evidence (PubMed:18720841, ECO:0000269). Xylanases are glycoside hydrolases that degrade xylan, a polysaccharide (glycan), making 'Glycan degradation' the correct pathway classification.",
    "evidence_ids": ["H1", "H3", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cleavable N-terminal signal peptide (MVSFKSLLLAASAFTAVLGRPF...) indicating a secreted protein. The core domain exhibits hallmarks of glycoside hydrolase family 11 (GH11): the 'WWSDGGGQ' catalytic motif, the 'GWNPGTGRT' and 'GGSFSPQGNGYLAVYGWTRNPLIEYYVVESYGTYNPGSGGQLKGTVTTDGGTYNVYVSTRTNQPSIDGTRTFQQYWSVRTSKRVGGAVTMQNHFNAWAQFGMNLGAHYYQIVATEGNGDFVGTEIWGLARGCRR' β-jelly-roll pattern characteristic of GH11 xylanases. A small (~237 AA) secreted fungal protein with these carbohydrate-active enzyme motifs points to glycan (xylan) degradation. Options B (Fe-S cluster biosynthesis) and C (terpenoid biosynthesis) are eliminated by absence of Fe-S cluster motifs and terpene synthase motifs respectively. Option A (antifungal biosynthesis) is implausible for a secreted fungal enzyme; antifungal pathways typically involve large NRPS/PKS assembly lines or plant defense responses, not small secreted hydrolases.",
    "missing_item_specific_fact": "None strictly required, though confident positive identification of the GH11 fold from sequence alone requires specialized knowledge of glycoside hydrolase family motifs (particularly the WWSDGGGQ signature). General elimination of B and C is straightforward; distinguishing D from A benefits from recognizing carbohydrate-active enzyme architecture.",
    "reason": "The sequence provides concrete structural motifs (GH11 catalytic and binding signatures) that a knowledgeable model can use to infer glycoside hydrolase function. The elimination of Fe-S cluster biosynthesis and terpenoid biosynthesis is straightforward from absence of relevant motifs. The distinction between glycan degradation and antifungal biosynthesis relies on recognizing the protein as a secreted hydrolase rather than a biosynthetic enzyme, which is supported by sequence features (small size, signal peptide, GH11 motifs)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated biologically. Fe-S cluster biosynthesis requires Fe-S cluster motifs (CX2CX4C or similar), terpenoid biosynthesis requires terpene cyclase motifs, and antifungal biosynthesis implies large multi-domain assembly enzymes. The GH11 xylanase fold is distinctive enough to unambiguously point to glycan degradation."
  },
  "important_caveats": [
    "The current UniProt sequence (version 2, 250 AA) differs from the benchmark sequence (version 1, 237 AA); however, the historical entry (version 60) matches exactly, confirming the annotation applies to the supplied sequence.",
    "The pathway annotation carries ECO:0000255 (PROSITE-ProRule), a computational annotation based on sequence similarity to characterized xylanases, though the EC number has independent experimental support (PubMed:18720841).",
    "EIX2 also functions as an ethylene-inducing elicitor in plant-pathogen interactions (PubMed:33205907), but its enzymatic pathway classification is glycan degradation, not signaling biosynthesis.",
    "The accession G2X0L1 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must rely solely on sequence analysis."
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

**Accession:** `G2X0L1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current mismatch.  
**Historical cutoff:** 2026-05-07; archived entry version 60. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- The current UniProt sequence differs from the supplied sequence; applicability of current annotation excerpts is qualified by that mismatch.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** mismatch.  
**Retrieved:** 2026-11-01T06:25:06.423596+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"1,4-beta-D-xylan xylanohydrolase G"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18720841","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase G"},"shortNames":[{"value":"Xylanase G"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18720841","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 2"}}}
```

Source SHA-256: `b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** mismatch.  
**Retrieved:** 2026-11-01T06:25:06.423596+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** mismatch.  
**Retrieved:** 2026-11-01T06:25:06.423596+00:00.  

```json
{"citation":{"authors":["Zhang G.","Rao B.","Ye J.","Ma L.","Zhang X."],"citationCrossReferences":[{"database":"PubMed","id":"18720841"}],"citationType":"journal article","firstPage":"765","id":"18720841","journal":"Wei Sheng Wu Xue Bao","lastPage":"771","publicationDate":"2008","title":"Molecular cloning and heterologous expression of a new xylanase gene from Verticillium dahliae.","volume":"48"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","SUBCELLULAR LOCATION","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-01T06:28:04.256317+00:00.  

```text
ID   EIX2_VERDV              Reviewed;         237 AA.
AC   G2X0L1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-NOV-2011, sequence version 1.
DT   28-JAN-2026, entry version 60.
DE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};
DE            Short=EIX2 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_03790;
OS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)
OS   (Verticillium wilt).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.
OX   NCBI_TaxID=498257;
```

Source SHA-256: `fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)  
**Locator:** `lines 47-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-01T06:28:04.256317+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-
CC       ProRule:PRU01097}.
```

Source SHA-256: `fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 191. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
