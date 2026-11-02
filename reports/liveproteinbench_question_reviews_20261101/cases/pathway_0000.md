# pathway_0000

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Capsule biogenesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKKILFITGTRADYSKIKSLMYRVQNSSEFELCIFATGMHLSKNFGYTVKELYKNGFKNIYEFINYDKYYQTDKALATTIDGFSRYVNELKPDLIVVHGDRIEPLAAAIVGALNNILVAHIEGGEISGTIDDSLRHAISKLAHIHLVNDEFAKKRLMQLGEDEKSIFIIGSPDLELLNDNKISLNEAKKYYDINYENYALLMFHPVTTEITSIKNQADNLVKALIQSNKNYIVIYPNNDLGFELILQSYEELKNNPRFKLFPSLRFEYFITLLKNADFIIGNSSCILKEALYLKTAGILVGSRQNGRLGNENTLKVNANSDEILKAINTIHKKQDLFSAKLEILDSSKLFFEYLQSGEFFKLSTQKVFKDIII

[Multiple Choices]
A. Capsule biogenesis
B. Bacterial outer membrane biogenesis
C. Amino-acid degradation
D. peptidoglycan degradation. .
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

> The exact sequence matches the UniProt entry for UDP-N-acetylglucosamine 2-epimerase from Campylobacter jejuni. UniProt annotates this enzyme in capsule biogenesis, citing a publication whose reference covers the function and pathway and whose title concerns biosynthesis for capsular polysaccharides. The pathway annotation carries experimental-evidence code ECO:0000269, although the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clear, specific basis for distinguishing capsule biogenesis from the other listed pathways. Identifying the relevant enzyme and connecting it to capsule biosynthesis requires protein-specific functional knowledge.


**Missing item-specific fact**

> The protein is UDP-N-acetylglucosamine 2-epimerase and functions in capsule polysaccharide biosynthesis; that annotation or equivalent experimental knowledge is absent from the question input.


**Reason**

> The reviewer-only sequence match and annotation support the key, but they were not supplied to the evaluated model. Recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from a discriminating biological feature provided in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports capsule biogenesis as the pathway; it does not identify another listed option as comparably defensible.


### Important caveats

- The pathway annotation is from UniProt and cites experimental evidence, but the cited primary paper was not independently retrieved or validated here.
- The sequence matches both the current UniProt entry and a historical entry available by the stated cutoff; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a clear, specific basis for distinguishing capsule biogenesis from the other listed pathways. Identifying the relevant enzyme and connecting it to capsule biosynthesis requires protein-specific functional knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein is UDP-N-acetylglucosamine 2-epimerase and functions in capsule polysaccharide biosynthesis; that annotation or equivalent experimental knowledge is absent from the question input.",
    "reason": "The reviewer-only sequence match and annotation support the key, but they were not supplied to the evaluated model. Recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from a discriminating biological feature provided in the question."
  },
  "case_id": "pathway_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for UDP-N-acetylglucosamine 2-epimerase from Campylobacter jejuni. UniProt annotates this enzyme in capsule biogenesis, citing a publication whose reference covers the function and pathway and whose title concerns biosynthesis for capsular polysaccharides. The pathway annotation carries experimental-evidence code ECO:0000269, although the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The pathway annotation is from UniProt and cites experimental evidence, but the cited primary paper was not independently retrieved or validated here.",
    "The sequence matches both the current UniProt entry and a historical entry available by the stated cutoff; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports capsule biogenesis as the pathway; it does not identify another listed option as comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for UDP-N-acetylglucosamine 2-epimerase from Campylobacter jejuni. UniProt annotates this enzyme in capsule biogenesis, citing a publication whose reference covers the function and pathway and whose title concerns biosynthesis for capsular polysaccharides. The pathway annotation carries experimental-evidence code ECO:0000269, although the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clear, specific basis for distinguishing capsule biogenesis from the other listed pathways. Identifying the relevant enzyme and connecting it to capsule biosynthesis requires protein-specific functional knowledge.",
    "missing_item_specific_fact": "The protein is UDP-N-acetylglucosamine 2-epimerase and functions in capsule polysaccharide biosynthesis; that annotation or equivalent experimental knowledge is absent from the question input.",
    "reason": "The reviewer-only sequence match and annotation support the key, but they were not supplied to the evaluated model. Recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from a discriminating biological feature provided in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports capsule biogenesis as the pathway; it does not identify another listed option as comparably defensible."
  },
  "important_caveats": [
    "The pathway annotation is from UniProt and cites experimental evidence, but the cited primary paper was not independently retrieved or validated here.",
    "The sequence matches both the current UniProt entry and a historical entry available by the stated cutoff; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt P0DY05 (UDP-N-acetylglucosamine 2-epimerase, EC 3.2.1.183, from Campylobacter jejuni 81116). The UniProt PATHWAY annotation explicitly states 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence code ECO:0000269 backed by PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The sequence match is confirmed in both the current entry (entryVersion 4) and the historical entry (entryVersion 2, first released 2026-01-28).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can eliminate C (amino-acid degradation) and D (peptidoglycan degradation) by recognizing the sequence as a nucleotide-sugar-modifying enzyme (epimerase/hydrolase acting on UDP-GlcNAc) rather than a deaminase, transaminase, or peptidoglycan hydrolase. However, the critical distinction between A (capsule biogenesis) and B (bacterial outer membrane biogenesis) cannot be resolved from sequence alone. In Campylobacter, sialic acid and related UDP-sugar derivatives are incorporated into BOTH capsular polysaccharides AND lipooligosaccharide (LOS) at the outer membrane. The specific assignment of this hydrolyzing UDP-GlcNAc 2-epimerase to capsule biogenesis rather than LOS/outer-membrane biogenesis is an organism-specific metabolic fact established by the 2024 Ghosh & Raushel experimental study, not a property inferable from the amino acid sequence.


**Missing item-specific fact**

> Knowledge that in Campylobacter jejuni 81116, this particular UDP-GlcNAc 2-epimerase (HS6.10 / C8J_1338) was experimentally shown to feed specifically into capsule polysaccharide biosynthesis (producing UDP-ManNAcA and CMP-Neu5Ac for capsule) rather than into LOS modification at the outer membrane. This is documented in PubMed:38382015.


**Reason**

> Eliminating C and D relies on general enzyme-class reasoning, but the A-vs-B choice requires knowing the specific downstream metabolic fate of the epimerase product in this organism, which is an item-specific experimental/annotation fact absent from the sequence input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Without the specific annotation or knowledge of the 2024 study, a knowledgeable model could argue that sialic acid biosynthesis in Campylobacter feeds into LOS (outer membrane) as well as capsule. The sequence provides no feature that distinguishes a capsule-specific glycan pathway enzyme from an outer-membrane glycan pathway enzyme. Both A and B are plausible glycan-biosynthesis contexts for a UDP-GlcNAc 2-epimerase in a Gram-negative bacterium.


### Important caveats

- The UniProt entry P0DY05 was first integrated on 2025-06-18; the pathway annotation citing PubMed:38382015 (published 2024) may or may not have been available at the author's data-construction date, which is unknown.
- The pathway assignment is based on a single 2024 experimental study; the enzyme's product (UDP-ManNAcA / CMP-Neu5Ac) could in principle also contribute to LOS biosynthesis in Campylobacter, making the exclusive 'capsule biogenesis' label a simplification of a shared biosynthetic step.
- The identity of the protein (P0DY05) was inferred from dataset image-path metadata absent from the model input; the model sees only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can eliminate C (amino-acid degradation) and D (peptidoglycan degradation) by recognizing the sequence as a nucleotide-sugar-modifying enzyme (epimerase/hydrolase acting on UDP-GlcNAc) rather than a deaminase, transaminase, or peptidoglycan hydrolase. However, the critical distinction between A (capsule biogenesis) and B (bacterial outer membrane biogenesis) cannot be resolved from sequence alone. In Campylobacter, sialic acid and related UDP-sugar derivatives are incorporated into BOTH capsular polysaccharides AND lipooligosaccharide (LOS) at the outer membrane. The specific assignment of this hydrolyzing UDP-GlcNAc 2-epimerase to capsule biogenesis rather than LOS/outer-membrane biogenesis is an organism-specific metabolic fact established by the 2024 Ghosh & Raushel experimental study, not a property inferable from the amino acid sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowledge that in Campylobacter jejuni 81116, this particular UDP-GlcNAc 2-epimerase (HS6.10 / C8J_1338) was experimentally shown to feed specifically into capsule polysaccharide biosynthesis (producing UDP-ManNAcA and CMP-Neu5Ac for capsule) rather than into LOS modification at the outer membrane. This is documented in PubMed:38382015.",
    "reason": "Eliminating C and D relies on general enzyme-class reasoning, but the A-vs-B choice requires knowing the specific downstream metabolic fate of the epimerase product in this organism, which is an item-specific experimental/annotation fact absent from the sequence input."
  },
  "case_id": "pathway_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DY05 (UDP-N-acetylglucosamine 2-epimerase, EC 3.2.1.183, from Campylobacter jejuni 81116). The UniProt PATHWAY annotation explicitly states 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence code ECO:0000269 backed by PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The sequence match is confirmed in both the current entry (entryVersion 4) and the historical entry (entryVersion 2, first released 2026-01-28)."
  },
  "important_caveats": [
    "The UniProt entry P0DY05 was first integrated on 2025-06-18; the pathway annotation citing PubMed:38382015 (published 2024) may or may not have been available at the author's data-construction date, which is unknown.",
    "The pathway assignment is based on a single 2024 experimental study; the enzyme's product (UDP-ManNAcA / CMP-Neu5Ac) could in principle also contribute to LOS biosynthesis in Campylobacter, making the exclusive 'capsule biogenesis' label a simplification of a shared biosynthetic step.",
    "The identity of the protein (P0DY05) was inferred from dataset image-path metadata absent from the model input; the model sees only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Without the specific annotation or knowledge of the 2024 study, a knowledgeable model could argue that sialic acid biosynthesis in Campylobacter feeds into LOS (outer membrane) as well as capsule. The sequence provides no feature that distinguishes a capsule-specific glycan pathway enzyme from an outer-membrane glycan pathway enzyme. Both A and B are plausible glycan-biosynthesis contexts for a UDP-GlcNAc 2-epimerase in a Gram-negative bacterium."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DY05 (UDP-N-acetylglucosamine 2-epimerase, EC 3.2.1.183, from Campylobacter jejuni 81116). The UniProt PATHWAY annotation explicitly states 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence code ECO:0000269 backed by PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The sequence match is confirmed in both the current entry (entryVersion 4) and the historical entry (entryVersion 2, first released 2026-01-28).",
    "evidence_ids": ["C5", "H3", "C4", "C6", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can eliminate C (amino-acid degradation) and D (peptidoglycan degradation) by recognizing the sequence as a nucleotide-sugar-modifying enzyme (epimerase/hydrolase acting on UDP-GlcNAc) rather than a deaminase, transaminase, or peptidoglycan hydrolase. However, the critical distinction between A (capsule biogenesis) and B (bacterial outer membrane biogenesis) cannot be resolved from sequence alone. In Campylobacter, sialic acid and related UDP-sugar derivatives are incorporated into BOTH capsular polysaccharides AND lipooligosaccharide (LOS) at the outer membrane. The specific assignment of this hydrolyzing UDP-GlcNAc 2-epimerase to capsule biogenesis rather than LOS/outer-membrane biogenesis is an organism-specific metabolic fact established by the 2024 Ghosh & Raushel experimental study, not a property inferable from the amino acid sequence.",
    "missing_item_specific_fact": "Knowledge that in Campylobacter jejuni 81116, this particular UDP-GlcNAc 2-epimerase (HS6.10 / C8J_1338) was experimentally shown to feed specifically into capsule polysaccharide biosynthesis (producing UDP-ManNAcA and CMP-Neu5Ac for capsule) rather than into LOS modification at the outer membrane. This is documented in PubMed:38382015.",
    "reason": "Eliminating C and D relies on general enzyme-class reasoning, but the A-vs-B choice requires knowing the specific downstream metabolic fate of the epimerase product in this organism, which is an item-specific experimental/annotation fact absent from the sequence input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Without the specific annotation or knowledge of the 2024 study, a knowledgeable model could argue that sialic acid biosynthesis in Campylobacter feeds into LOS (outer membrane) as well as capsule. The sequence provides no feature that distinguishes a capsule-specific glycan pathway enzyme from an outer-membrane glycan pathway enzyme. Both A and B are plausible glycan-biosynthesis contexts for a UDP-GlcNAc 2-epimerase in a Gram-negative bacterium."
  },
  "important_caveats": [
    "The UniProt entry P0DY05 was first integrated on 2025-06-18; the pathway annotation citing PubMed:38382015 (published 2024) may or may not have been available at the author's data-construction date, which is unknown.",
    "The pathway assignment is based on a single 2024 experimental study; the enzyme's product (UDP-ManNAcA / CMP-Neu5Ac) could in principle also contribute to LOS biosynthesis in Campylobacter, making the exclusive 'capsule biogenesis' label a simplification of a shared biosynthetic step.",
    "The identity of the protein (P0DY05) was inferred from dataset image-path metadata absent from the model input; the model sees only the raw sequence."
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

**Accession:** `P0DY05` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
"P0DY05"
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"Hydrolyzing UDP-GlcNAc 2-epimerase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"3.2.1.183"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetylglucosamine 2-epimerase"}}}
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"Capsule biogenesis; capsule polysaccharide biosynthesis"}]}
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"81116 / NCTC 11828"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

```text
ID   UAEPH_CAMJ8             Reviewed;         373 AA.
AC   P0DY05;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};
DE            EC=3.2.1.183 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=Hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};
GN   Name=HS6.10 {ECO:0000303|PubMed:38382015};
GN   OrderedLocusNames=C8J_1338 {ECO:0000312|EMBL:ABV52936.1};
OS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC
OS   11828).
OC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;
OC   Campylobacterales; Campylobacteraceae; Campylobacter.
OX   NCBI_TaxID=407148;
```

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RC   STRAIN=81116 / NCTC 11828;
RX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;
RA   Ghosh M.K., Raushel F.M.;
RT   "Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-
RT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter
RT   jejuni.";
RL   Biochemistry 63:688-698(2024).
```

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 52-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

```text
CC   -!- PATHWAY: Capsule biogenesis; capsule polysaccharide biosynthesis.
CC       {ECO:0000269|PubMed:38382015}.
```

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
