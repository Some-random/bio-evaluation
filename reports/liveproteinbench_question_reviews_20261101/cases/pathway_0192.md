# pathway_0192

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Capsule biogenesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKEIKIQNIIINEEKAPLVVPEIGINHNGSLELAKIMVDAAFSAGAKIIKHQTHIVEDEMSKAAKKVIPGNAKISIYEIMQKCALDYKDELALKEYTEKLGLVYLSTPFSRAGANRLEDMGVSAFKIGSGECNNYPLIKHIAAFKKPMIVSTGMNSIESIKPTVKILLDNEIPFVLMHTTNLYPTPHNLVRLNAMLELKKEFSCMVGLSDHTTDNLACLGAVALGACVLERHFTDSMDRSGPDIVCSMDTKALKELIMQSEQMAIMRGNNESKKAAKQEQVTIDFAFASVVSIKDIKKGEVLSMDNIWVKRPGLGGISAAEFENILGKKALRDIENDTQLSYEDFA

[Multiple Choices]
A. L-valine biosynthesis
B. Capsule biogenesis
C. ajmaline biosynthesis. .
D. L-threonine from L-aspartate: step 5/5. .
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

> The exact sequence matches a UniProt entry annotated as N-acetylneuraminate synthase, with capsule polysaccharide biosynthesis listed as its pathway. The pathway annotation cites experimental evidence (ECO:0000269) and a study specific to the matching strain.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying a protein family with specialized biochemical analysis, but it does not provide an evident, general biological argument that distinguishes capsule biogenesis from the listed alternatives.


**Missing item-specific fact**

> The protein's identity and pathway role as N-acetylneuraminate synthase in Campylobacter jejuni capsule polysaccharide biosynthesis.


**Reason**

> That function and pathway assignment are protein- and organism-specific facts absent from the supplied sequence context. The reviewer-only annotation supports the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports capsule biogenesis; the supplied evidence does not indicate another listed pathway as a competing assignment.


### Important caveats

- The cited pathway annotation is experimentally supported in the matching strain, but the actual source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying a protein family with specialized biochemical analysis, but it does not provide an evident, general biological argument that distinguishes capsule biogenesis from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and pathway role as N-acetylneuraminate synthase in Campylobacter jejuni capsule polysaccharide biosynthesis.",
    "reason": "That function and pathway assignment are protein- and organism-specific facts absent from the supplied sequence context. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "case_id": "pathway_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as N-acetylneuraminate synthase, with capsule polysaccharide biosynthesis listed as its pathway. The pathway annotation cites experimental evidence (ECO:0000269) and a study specific to the matching strain."
  },
  "important_caveats": [
    "The cited pathway annotation is experimentally supported in the matching strain, but the actual source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports capsule biogenesis; the supplied evidence does not indicate another listed pathway as a competing assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as N-acetylneuraminate synthase, with capsule polysaccharide biosynthesis listed as its pathway. The pathway annotation cites experimental evidence (ECO:0000269) and a study specific to the matching strain.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying a protein family with specialized biochemical analysis, but it does not provide an evident, general biological argument that distinguishes capsule biogenesis from the listed alternatives.",
    "missing_item_specific_fact": "The protein's identity and pathway role as N-acetylneuraminate synthase in Campylobacter jejuni capsule polysaccharide biosynthesis.",
    "reason": "That function and pathway assignment are protein- and organism-specific facts absent from the supplied sequence context. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports capsule biogenesis; the supplied evidence does not indicate another listed pathway as a competing assignment."
  },
  "important_caveats": [
    "The cited pathway annotation is experimentally supported in the matching strain, but the actual source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt P0DY06 (NEUAS_CAMJ8), annotated as N-acetylneuraminate synthase (EC 2.5.1.56) with experimental evidence (ECO:0000269, PubMed:38382015). The UniProt pathway comment explicitly states 'Capsule biogenesis; capsule polysaccharide biosynthesis,' directly supporting choice B. The sequence is from Campylobacter jejuni where Neu5Ac is incorporated into capsular polysaccharides.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can partially reason by elimination: choice C (ajmaline biosynthesis) is a plant monoterpene indole alkaloid pathway irrelevant to a bacterial protein; choices A and D are amino acid biosynthesis pathways involving entirely different enzyme classes (acetohydroxyacid synthase, threonine synthase, etc.) not matching this PEP-transferase-like fold. However, positively identifying choice B as 'Capsule biogenesis' requires recognizing this as a sialic acid (Neu5Ac) synthase family member AND knowing that in Campylobacter jejuni the product is channeled into capsular polysaccharide biosynthesis rather than, say, glycoprotein sialylation or other sialic-acid-consuming pathways.


**Missing item-specific fact**

> The specific identification of this 346-aa sequence as Neu5Ac synthase (EC 2.5.1.56) and the organism-specific biological context that in C. jejuni strain 81116, Neu5Ac is a building block of the capsular polysaccharide (not merely a free metabolite or glycoprotein modification). This is an item-specific annotation/experimental fact (PubMed:38382015) not derivable from generic sequence features alone.


**Reason**

> While distractors A, C, and D can be eliminated by general biological reasoning (wrong organism kingdom, wrong enzyme class), confirming B requires the specific knowledge that this sequence is a sialic acid synthase and that its biological role in C. jejuni is capsule polysaccharide biosynthesis. This is an annotation-level fact tied to this particular protein-organism pair.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, C, and D are clearly incompatible with a bacterial PEP-transferase enzyme: C is a plant alkaloid pathway, A and D are amino acid biosynthesis pathways with unrelated enzyme classes. Only B is biologically plausible for this protein, making the answer unambiguous despite the reliance on specific knowledge.


### Important caveats

- The UniProt entry P0DY06 was first released in 2025-06-18 with the pathway annotation present from the start (entry version 2, first release 2026_01). The experimental evidence (PubMed:38382015, 2024) supports the capsule biogenesis assignment.
- The pathway label 'Capsule biogenesis' is organism-context-specific; the same enzyme class in other organisms might be annotated under 'sialic acid biosynthesis' or 'glycan biosynthesis.'
- The trailing '. .' in choices C and D appear to be formatting artifacts and do not affect answerability.
- The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can partially reason by elimination: choice C (ajmaline biosynthesis) is a plant monoterpene indole alkaloid pathway irrelevant to a bacterial protein; choices A and D are amino acid biosynthesis pathways involving entirely different enzyme classes (acetohydroxyacid synthase, threonine synthase, etc.) not matching this PEP-transferase-like fold. However, positively identifying choice B as 'Capsule biogenesis' requires recognizing this as a sialic acid (Neu5Ac) synthase family member AND knowing that in Campylobacter jejuni the product is channeled into capsular polysaccharide biosynthesis rather than, say, glycoprotein sialylation or other sialic-acid-consuming pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this 346-aa sequence as Neu5Ac synthase (EC 2.5.1.56) and the organism-specific biological context that in C. jejuni strain 81116, Neu5Ac is a building block of the capsular polysaccharide (not merely a free metabolite or glycoprotein modification). This is an item-specific annotation/experimental fact (PubMed:38382015) not derivable from generic sequence features alone.",
    "reason": "While distractors A, C, and D can be eliminated by general biological reasoning (wrong organism kingdom, wrong enzyme class), confirming B requires the specific knowledge that this sequence is a sialic acid synthase and that its biological role in C. jejuni is capsule polysaccharide biosynthesis. This is an annotation-level fact tied to this particular protein-organism pair."
  },
  "case_id": "pathway_0192",
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
    "reason": "The sequence exactly matches UniProt P0DY06 (NEUAS_CAMJ8), annotated as N-acetylneuraminate synthase (EC 2.5.1.56) with experimental evidence (ECO:0000269, PubMed:38382015). The UniProt pathway comment explicitly states 'Capsule biogenesis; capsule polysaccharide biosynthesis,' directly supporting choice B. The sequence is from Campylobacter jejuni where Neu5Ac is incorporated into capsular polysaccharides."
  },
  "important_caveats": [
    "The UniProt entry P0DY06 was first released in 2025-06-18 with the pathway annotation present from the start (entry version 2, first release 2026_01). The experimental evidence (PubMed:38382015, 2024) supports the capsule biogenesis assignment.",
    "The pathway label 'Capsule biogenesis' is organism-context-specific; the same enzyme class in other organisms might be annotated under 'sialic acid biosynthesis' or 'glycan biosynthesis.'",
    "The trailing '. .' in choices C and D appear to be formatting artifacts and do not affect answerability.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D are clearly incompatible with a bacterial PEP-transferase enzyme: C is a plant alkaloid pathway, A and D are amino acid biosynthesis pathways with unrelated enzyme classes. Only B is biologically plausible for this protein, making the answer unambiguous despite the reliance on specific knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt P0DY06 (NEUAS_CAMJ8), annotated as N-acetylneuraminate synthase (EC 2.5.1.56) with experimental evidence (ECO:0000269, PubMed:38382015). The UniProt pathway comment explicitly states 'Capsule biogenesis; capsule polysaccharide biosynthesis,' directly supporting choice B. The sequence is from Campylobacter jejuni where Neu5Ac is incorporated into capsular polysaccharides.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can partially reason by elimination: choice C (ajmaline biosynthesis) is a plant monoterpene indole alkaloid pathway irrelevant to a bacterial protein; choices A and D are amino acid biosynthesis pathways involving entirely different enzyme classes (acetohydroxyacid synthase, threonine synthase, etc.) not matching this PEP-transferase-like fold. However, positively identifying choice B as 'Capsule biogenesis' requires recognizing this as a sialic acid (Neu5Ac) synthase family member AND knowing that in Campylobacter jejuni the product is channeled into capsular polysaccharide biosynthesis rather than, say, glycoprotein sialylation or other sialic-acid-consuming pathways.",
    "missing_item_specific_fact": "The specific identification of this 346-aa sequence as Neu5Ac synthase (EC 2.5.1.56) and the organism-specific biological context that in C. jejuni strain 81116, Neu5Ac is a building block of the capsular polysaccharide (not merely a free metabolite or glycoprotein modification). This is an item-specific annotation/experimental fact (PubMed:38382015) not derivable from generic sequence features alone.",
    "reason": "While distractors A, C, and D can be eliminated by general biological reasoning (wrong organism kingdom, wrong enzyme class), confirming B requires the specific knowledge that this sequence is a sialic acid synthase and that its biological role in C. jejuni is capsule polysaccharide biosynthesis. This is an annotation-level fact tied to this particular protein-organism pair."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D are clearly incompatible with a bacterial PEP-transferase enzyme: C is a plant alkaloid pathway, A and D are amino acid biosynthesis pathways with unrelated enzyme classes. Only B is biologically plausible for this protein, making the answer unambiguous despite the reliance on specific knowledge."
  },
  "important_caveats": [
    "The UniProt entry P0DY06 was first released in 2025-06-18 with the pathway annotation present from the start (entry version 2, first release 2026_01). The experimental evidence (PubMed:38382015, 2024) supports the capsule biogenesis assignment.",
    "The pathway label 'Capsule biogenesis' is organism-context-specific; the same enzyme class in other organisms might be annotated under 'sialic acid biosynthesis' or 'glycan biosynthesis.'",
    "The trailing '. .' in choices C and D appear to be formatting artifacts and do not affect answerability.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model."
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

**Accession:** `P0DY06` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
"P0DY06"
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"2.5.1.56"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"N-acetylneuraminate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"Neu5Ac synthase"}]}}
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"Capsule biogenesis; capsule polysaccharide biosynthesis"}]}
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:03.200320+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"81116 / NCTC 11828"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
ID   NEUAS_CAMJ8             Reviewed;         346 AA.
AC   P0DY06;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};
DE            Short=Neu5Ac synthase {ECO:0000303|PubMed:38382015};
DE            EC=2.5.1.56 {ECO:0000269|PubMed:38382015};
GN   Name=HS6.11 {ECO:0000303|PubMed:38382015};
GN   OrderedLocusNames=C8J_1339 {ECO:0000312|EMBL:ABV52937.1};
OS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC
OS   11828).
OC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;
OC   Campylobacterales; Campylobacteraceae; Campylobacter.
OX   NCBI_TaxID=407148;
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

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

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)  
**Locator:** `lines 51-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:07.414593+00:00.  

```text
CC   -!- PATHWAY: Capsule biogenesis; capsule polysaccharide biosynthesis.
CC       {ECO:0000269|PubMed:38382015}.
CC   ---------------------------------------------------------------------------
CC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms
CC   Distributed under the Creative Commons Attribution (CC BY 4.0) License
CC   ---------------------------------------------------------------------------
```

Source SHA-256: `7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 192. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
