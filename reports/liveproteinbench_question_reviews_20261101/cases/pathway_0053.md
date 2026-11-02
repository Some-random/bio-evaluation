# pathway_0053

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHLASSLFLLATLPFGFAAGKGKGKGKDNSDVGLDVLAKKAGLKYFGAATDTPGQRERAGLEDKYPEYDRIMWHSPEFGSTTPTNGQKWLFVEPERGVFNFTEGDVVASKARQHGKLLRCHALVWHSQLAPWVEETEWTPEELRKVIVDHITAVAGHYKGQCYAWDVVNEALNEDGTYRESVFYKVLGEEYIKLAFETAAKVDPKAKLYYNDYNLEWPSAKTEGAKRIVKLLKDAKIPIHGVGLQAHLIAEQHPTLDDHIAAIRGFTQLGVEVALTELDIRLKTPATEENLALQREAYKNVVGACVQVCGCVGVTIWDFYDPFSWVPYFFEGEGAPLLWFEDFSKHPAYYGVVEALTNKTRRSKRSISDRRAKLLA

[Multiple Choices]
A. Glycan degradation
B. Polyketide biosynthesis. .
C. LPS O-antigen biosynthesis. .
D. Carotenoid biosynthesis
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

> The exact-matched sequence is annotated as endo-1,4-beta-xylanase A, with the pathway listed as glycan degradation (xylan degradation). The annotation cites experimental evidence for the enzyme's function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus has a clear hydrophobic signal-peptide-like region, consistent with secretion. A compact secreted enzyme from a fungus is a plausible extracellular polymer-degrading enzyme, favoring glycan degradation over the listed biosynthetic pathways; the other choices are not suggested by this sequence context.


**Missing item-specific fact**

> The exact substrate and xylanase activity are not established by the sequence context alone; identifying xylan specifically would require protein-specific annotation or experimental evidence.


**Reason**

> The sequence and choices provide a defensible basis for selecting the broad glycan-degradation pathway, though not for determining the exact xylan substrate without item-specific knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed broad pathways, glycan degradation best fits a likely secreted fungal enzyme; the other options do not have comparable support from the sequence.


### Important caveats

- Reviewer-only annotations support the expected answer but were not part of the evaluated input.
- A predicted signal peptide supports secretion but does not, by itself, prove substrate specificity or pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus has a clear hydrophobic signal-peptide-like region, consistent with secretion. A compact secreted enzyme from a fungus is a plausible extracellular polymer-degrading enzyme, favoring glycan degradation over the listed biosynthetic pathways; the other choices are not suggested by this sequence context.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate and xylanase activity are not established by the sequence context alone; identifying xylan specifically would require protein-specific annotation or experimental evidence.",
    "reason": "The sequence and choices provide a defensible basis for selecting the broad glycan-degradation pathway, though not for determining the exact xylan substrate without item-specific knowledge."
  },
  "case_id": "pathway_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated as endo-1,4-beta-xylanase A, with the pathway listed as glycan degradation (xylan degradation). The annotation cites experimental evidence for the enzyme's function."
  },
  "important_caveats": [
    "Reviewer-only annotations support the expected answer but were not part of the evaluated input.",
    "A predicted signal peptide supports secretion but does not, by itself, prove substrate specificity or pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed broad pathways, glycan degradation best fits a likely secreted fungal enzyme; the other options do not have comparable support from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated as endo-1,4-beta-xylanase A, with the pathway listed as glycan degradation (xylan degradation). The annotation cites experimental evidence for the enzyme's function.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a clear hydrophobic signal-peptide-like region, consistent with secretion. A compact secreted enzyme from a fungus is a plausible extracellular polymer-degrading enzyme, favoring glycan degradation over the listed biosynthetic pathways; the other choices are not suggested by this sequence context.",
    "missing_item_specific_fact": "The exact substrate and xylanase activity are not established by the sequence context alone; identifying xylan specifically would require protein-specific annotation or experimental evidence.",
    "reason": "The sequence and choices provide a defensible basis for selecting the broad glycan-degradation pathway, though not for determining the exact xylan substrate without item-specific knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed broad pathways, glycan degradation best fits a likely secreted fungal enzyme; the other options do not have comparable support from the sequence."
  },
  "important_caveats": [
    "Reviewer-only annotations support the expected answer but were not part of the evaluated input.",
    "A predicted signal peptide supports secretion but does not, by itself, prove substrate specificity or pathway."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is UniProt M4MGK7 (XYNA_HUMIN), Endo-1,4-beta-xylanase A (EC 3.2.1.8) from Humicola insolens, with experimental evidence (ECO:0000269, PubMed:23306124). The UniProt PATHWAY annotation explicitly states 'Glycan degradation; xylan degradation.' Xylanases hydrolyze β-1,4-xylan linkages, a polysaccharide/glycan, placing the enzyme squarely in the glycan degradation pathway. The sequence matches exactly (376 AA, identical SHA256).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several general biological arguments distinguish the answer: (1) The N-terminal hydrophobic stretch (MHLASSLFLLATLPFGFAAG) is a classical eukaryotic signal peptide, indicating a secreted extracellular enzyme—consistent with extracellular glycan degradation but inconsistent with intracellular carotenoid biosynthesis or polyketide synthase assembly. (2) At ~376 AA, the protein is far too small for polyketide synthases (option B), which are typically >1000 AA multi-domain megasynthases. (3) LPS O-antigen biosynthesis (option C) is exclusively bacterial; the signal peptide architecture and overall sequence composition are eukaryotic/fungal, eliminating this option. (4) Carotenoid biosynthesis enzymes (phytoene synthase, desaturases, cyclases) possess distinctive features—transmembrane helices (desaturases) or DDXXD terpene-synthase motifs (phytoene synthase)—absent here. (5) The remaining sequence contains Glu and Asp residues in conserved contexts (e.g., 'FVEPERG', 'WDFYDP') consistent with the catalytic dyad of retaining glycosyl hydrolases, supporting a glycan-degrading function.


**Missing item-specific fact**

> Precise recognition of the GH10 xylanase family catalytic motif would require specific glycosyl hydrolase family knowledge, but among the four given options, the elimination logic (size, organism type, absence of transmembrane/terpene motifs, presence of signal peptide and hydrolase-like catalytic residues) provides a defensible reasoning path to glycan degradation without needing to memorize the exact database entry.


**Reason**

> The four options are sufficiently diverse (bacterial pathway, mega-enzyme pathway, terpene pathway, polysaccharide hydrolase pathway) that general biological reasoning—signal peptide → secreted; small size → not PKS; fungal context → not LPS; no transmembrane/terpene motifs → not carotenoid—meaningfully narrows to glycan degradation. The hydrolase-like catalytic residue pattern provides positive support. This does not require memorizing a specific UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct biological categories (bacterial LPS pathway, mega-enzyme polyketide synthesis, terpene-related carotenoid synthesis, polysaccharide hydrolase). The sequence features (signal peptide, small size, eukaryotic composition, absence of transmembrane domains or DDXXD motifs, presence of catalytic Glu/Asp in hydrolase-conserved contexts) uniquely support glycan degradation among the choices.


### Important caveats

- The UniProt pathway annotation is backed by experimental evidence (ECO:0000269, PubMed:23306124), not mere computational inference.
- The sequence-to-accession mapping was performed by the reviewer; the evaluated model sees only the raw sequence and four options.
- The reasoning path relies on recognizing general glycosyl hydrolase catalytic residue patterns; a model without any training on hydrolase families might struggle to positively confirm option A, though elimination of B, C, and D remains robust.
- The protein is a precursor (376 AA including signal peptide); the mature xylanase is ~358 AA.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several general biological arguments distinguish the answer: (1) The N-terminal hydrophobic stretch (MHLASSLFLLATLPFGFAAG) is a classical eukaryotic signal peptide, indicating a secreted extracellular enzyme—consistent with extracellular glycan degradation but inconsistent with intracellular carotenoid biosynthesis or polyketide synthase assembly. (2) At ~376 AA, the protein is far too small for polyketide synthases (option B), which are typically >1000 AA multi-domain megasynthases. (3) LPS O-antigen biosynthesis (option C) is exclusively bacterial; the signal peptide architecture and overall sequence composition are eukaryotic/fungal, eliminating this option. (4) Carotenoid biosynthesis enzymes (phytoene synthase, desaturases, cyclases) possess distinctive features—transmembrane helices (desaturases) or DDXXD terpene-synthase motifs (phytoene synthase)—absent here. (5) The remaining sequence contains Glu and Asp residues in conserved contexts (e.g., 'FVEPERG', 'WDFYDP') consistent with the catalytic dyad of retaining glycosyl hydrolases, supporting a glycan-degrading function.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of the GH10 xylanase family catalytic motif would require specific glycosyl hydrolase family knowledge, but among the four given options, the elimination logic (size, organism type, absence of transmembrane/terpene motifs, presence of signal peptide and hydrolase-like catalytic residues) provides a defensible reasoning path to glycan degradation without needing to memorize the exact database entry.",
    "reason": "The four options are sufficiently diverse (bacterial pathway, mega-enzyme pathway, terpene pathway, polysaccharide hydrolase pathway) that general biological reasoning—signal peptide → secreted; small size → not PKS; fungal context → not LPS; no transmembrane/terpene motifs → not carotenoid—meaningfully narrows to glycan degradation. The hydrolase-like catalytic residue pattern provides positive support. This does not require memorizing a specific UniProt annotation."
  },
  "case_id": "pathway_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The protein is UniProt M4MGK7 (XYNA_HUMIN), Endo-1,4-beta-xylanase A (EC 3.2.1.8) from Humicola insolens, with experimental evidence (ECO:0000269, PubMed:23306124). The UniProt PATHWAY annotation explicitly states 'Glycan degradation; xylan degradation.' Xylanases hydrolyze β-1,4-xylan linkages, a polysaccharide/glycan, placing the enzyme squarely in the glycan degradation pathway. The sequence matches exactly (376 AA, identical SHA256)."
  },
  "important_caveats": [
    "The UniProt pathway annotation is backed by experimental evidence (ECO:0000269, PubMed:23306124), not mere computational inference.",
    "The sequence-to-accession mapping was performed by the reviewer; the evaluated model sees only the raw sequence and four options.",
    "The reasoning path relies on recognizing general glycosyl hydrolase catalytic residue patterns; a model without any training on hydrolase families might struggle to positively confirm option A, though elimination of B, C, and D remains robust.",
    "The protein is a precursor (376 AA including signal peptide); the mature xylanase is ~358 AA."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct biological categories (bacterial LPS pathway, mega-enzyme polyketide synthesis, terpene-related carotenoid synthesis, polysaccharide hydrolase). The sequence features (signal peptide, small size, eukaryotic composition, absence of transmembrane domains or DDXXD motifs, presence of catalytic Glu/Asp in hydrolase-conserved contexts) uniquely support glycan degradation among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is UniProt M4MGK7 (XYNA_HUMIN), Endo-1,4-beta-xylanase A (EC 3.2.1.8) from Humicola insolens, with experimental evidence (ECO:0000269, PubMed:23306124). The UniProt PATHWAY annotation explicitly states 'Glycan degradation; xylan degradation.' Xylanases hydrolyze β-1,4-xylan linkages, a polysaccharide/glycan, placing the enzyme squarely in the glycan degradation pathway. The sequence matches exactly (376 AA, identical SHA256).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several general biological arguments distinguish the answer: (1) The N-terminal hydrophobic stretch (MHLASSLFLLATLPFGFAAG) is a classical eukaryotic signal peptide, indicating a secreted extracellular enzyme—consistent with extracellular glycan degradation but inconsistent with intracellular carotenoid biosynthesis or polyketide synthase assembly. (2) At ~376 AA, the protein is far too small for polyketide synthases (option B), which are typically >1000 AA multi-domain megasynthases. (3) LPS O-antigen biosynthesis (option C) is exclusively bacterial; the signal peptide architecture and overall sequence composition are eukaryotic/fungal, eliminating this option. (4) Carotenoid biosynthesis enzymes (phytoene synthase, desaturases, cyclases) possess distinctive features—transmembrane helices (desaturases) or DDXXD terpene-synthase motifs (phytoene synthase)—absent here. (5) The remaining sequence contains Glu and Asp residues in conserved contexts (e.g., 'FVEPERG', 'WDFYDP') consistent with the catalytic dyad of retaining glycosyl hydrolases, supporting a glycan-degrading function.",
    "missing_item_specific_fact": "Precise recognition of the GH10 xylanase family catalytic motif would require specific glycosyl hydrolase family knowledge, but among the four given options, the elimination logic (size, organism type, absence of transmembrane/terpene motifs, presence of signal peptide and hydrolase-like catalytic residues) provides a defensible reasoning path to glycan degradation without needing to memorize the exact database entry.",
    "reason": "The four options are sufficiently diverse (bacterial pathway, mega-enzyme pathway, terpene pathway, polysaccharide hydrolase pathway) that general biological reasoning—signal peptide → secreted; small size → not PKS; fungal context → not LPS; no transmembrane/terpene motifs → not carotenoid—meaningfully narrows to glycan degradation. The hydrolase-like catalytic residue pattern provides positive support. This does not require memorizing a specific UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct biological categories (bacterial LPS pathway, mega-enzyme polyketide synthesis, terpene-related carotenoid synthesis, polysaccharide hydrolase). The sequence features (signal peptide, small size, eukaryotic composition, absence of transmembrane domains or DDXXD motifs, presence of catalytic Glu/Asp in hydrolase-conserved contexts) uniquely support glycan degradation among the choices."
  },
  "important_caveats": [
    "The UniProt pathway annotation is backed by experimental evidence (ECO:0000269, PubMed:23306124), not mere computational inference.",
    "The sequence-to-accession mapping was performed by the reviewer; the evaluated model sees only the raw sequence and four options.",
    "The reasoning path relies on recognizing general glycosyl hydrolase catalytic residue patterns; a model without any training on hydrolase families might struggle to positively confirm option A, though elimination of B, C, and D remains robust.",
    "The protein is a precursor (376 AA including signal peptide); the mature xylanase is ~358 AA."
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

**Accession:** `M4MGK7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
"M4MGK7"
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1,4-beta-D-xylan xylanohydrolase A"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23306124","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase A"}}}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:05.622631+00:00.  

```json
{"citation":{"authors":["Du Y.","Shi P.","Huang H.","Zhang X.","Luo H.","Wang Y.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"23306124"},{"database":"DOI","id":"10.1016/j.biortech.2012.12.067"}],"citationType":"journal article","firstPage":"161","id":"23306124","journal":"Bioresour. Technol.","lastPage":"167","publicationDate":"2013","title":"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.","volume":"130"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:29:07.720781+00:00.  

```text
ID   XYNA_HUMIN              Reviewed;         376 AA.
AC   M4MGK7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-MAY-2013, sequence version 1.
DT   28-JAN-2026, entry version 31.
DE   RecName: Full=Endo-1,4-beta-xylanase A {ECO:0000303|PubMed:23306124};
DE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};
DE   AltName: Full=1,4-beta-D-xylan xylanohydrolase A {ECO:0000305};
DE   Flags: Precursor;
GN   Name=XynA {ECO:0000303|PubMed:23306124};
OS   Humicola insolens (Soft-rot fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.
OX   NCBI_TaxID=85995;
```

Source SHA-256: `7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)  
**Locator:** `lines 15-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:29:07.720781+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,
RP   AND BIOTECHNOLOGY.
RC   STRAIN=Y1;
RX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;
RA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;
RT   "Characterization of three novel thermophilic xylanases from Humicola
RT   insolens Y1 with application potentials in the brewing industry.";
RL   Bioresour. Technol. 130:161-167(2013).
```

Source SHA-256: `7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)  
**Locator:** `lines 65-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:29:07.720781+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation.
CC       {ECO:0000269|PubMed:23306124}.
```

Source SHA-256: `7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 53. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
