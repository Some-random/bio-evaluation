# pathway_0078

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Capsule biogenesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVKKILIVFGTRPEAIKMAPLVKIMENRNDVNFRVCVTGQHRQMLDQILNIFDIKPDYDLNIMQENQDLYDITLKILCGMKNVLNDFKPNIVLVHGDTTTASVTALAAFYQKIKIAHVEAGLRTYNICNPWPEEANRQIIGVLANIHFTPTVKSAENLIKEGKNKEGIFITGNTVIDALFYMTEKIKNDKTFKIKVLSSIGNEYKINDNKKFILVTGHRRENFGEGFLQICEALKIIAINNPDIDIVYPVHLNPNVQKPVKMLLLNISNIYLINPLKYEEFIYLMSKSYFIITDSGGIQEEAPSLGKPILVMRETTERPEAVEAGVVKLVGACKQNIIRESQKLIDDQDEYEKMSKAYNPYGDGRACEKIINILIKGKNNESI

[Multiple Choices]
A. protein ubiquitination. .
B. Capsule biogenesis
C. ajmaline biosynthesis. .
D. iron-sulfur cluster biosynthesis. .
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

> The exact sequence matches the Campylobacter jejuni UniProt entry annotated for capsule biogenesis and capsule polysaccharide biosynthesis. That pathway annotation cites a 2024 paper and carries an experimental-evidence code; the excerpts support the key, though they do not independently establish the paper’s experimental results.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying an enzyme family, but the input gives no organism, pathway context, or experimentally established role. Inferring which pathway this particular enzyme serves requires a protein-specific functional annotation or equivalent knowledge.


**Missing item-specific fact**

> The sequence-matched protein is annotated as UDP-N-acetylglucosamine 2-epimerase functioning in capsule polysaccharide biosynthesis.


**Reason**

> The reviewer-only annotation supports the key but was absent from the evaluated input. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct, and the matched-entry pathway annotation supports B. The supplied input alone does not identify the pathway, but the reviewer evidence does not support another listed option.


### Important caveats

- The sequence match is exact and applies to the 383-residue sequence.
- The annotated pathway is linked to a cited publication with an experimental-evidence code; the excerpts do not include the primary experimental results.
- The actual author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying an enzyme family, but the input gives no organism, pathway context, or experimentally established role. Inferring which pathway this particular enzyme serves requires a protein-specific functional annotation or equivalent knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-matched protein is annotated as UDP-N-acetylglucosamine 2-epimerase functioning in capsule polysaccharide biosynthesis.",
    "reason": "The reviewer-only annotation supports the key but was absent from the evaluated input. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "case_id": "pathway_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Campylobacter jejuni UniProt entry annotated for capsule biogenesis and capsule polysaccharide biosynthesis. That pathway annotation cites a 2024 paper and carries an experimental-evidence code; the excerpts support the key, though they do not independently establish the paper’s experimental results."
  },
  "important_caveats": [
    "The sequence match is exact and applies to the 383-residue sequence.",
    "The annotated pathway is linked to a cited publication with an experimental-evidence code; the excerpts do not include the primary experimental results.",
    "The actual author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct, and the matched-entry pathway annotation supports B. The supplied input alone does not identify the pathway, but the reviewer evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Campylobacter jejuni UniProt entry annotated for capsule biogenesis and capsule polysaccharide biosynthesis. That pathway annotation cites a 2024 paper and carries an experimental-evidence code; the excerpts support the key, though they do not independently establish the paper’s experimental results.",
    "evidence_ids": ["C1", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying an enzyme family, but the input gives no organism, pathway context, or experimentally established role. Inferring which pathway this particular enzyme serves requires a protein-specific functional annotation or equivalent knowledge.",
    "missing_item_specific_fact": "The sequence-matched protein is annotated as UDP-N-acetylglucosamine 2-epimerase functioning in capsule polysaccharide biosynthesis.",
    "reason": "The reviewer-only annotation supports the key but was absent from the evaluated input. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct, and the matched-entry pathway annotation supports B. The supplied input alone does not identify the pathway, but the reviewer evidence does not support another listed option."
  },
  "important_caveats": [
    "The sequence match is exact and applies to the 383-residue sequence.",
    "The annotated pathway is linked to a cited publication with an experimental-evidence code; the excerpts do not include the primary experimental results.",
    "The actual author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0U3CEN8 (UAGEP_CAMJU) is annotated with PATHWAY: 'Capsule biogenesis; capsule polysaccharide biosynthesis' with evidence code ECO:0000269 (direct assay) from PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The protein is UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) from Campylobacter jejuni, experimentally shown to produce UDP-ManNAcA and CMP-Neu5Ac for capsular polysaccharides. Sequence match is exact (SHA256 confirmed).

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains NAD-binding Rossmann-fold motifs (e.g., 'GDTTTAS') characteristic of sugar-processing epimerases/dehydratases, identifying it as a UDP-sugar-processing enzyme in a bacterium. Among the four choices: (A) protein ubiquitination is a eukaryotic-specific process absent in bacteria; (C) ajmaline biosynthesis is a plant-specific monoterpene indole alkaloid pathway; (D) iron-sulfur cluster biosynthesis involves cysteine desulfurases, scaffold proteins, and Fe-S ligases—entirely different enzyme classes with no NAD-dependent epimerase architecture. Only (B) capsule biogenesis is consistent with a bacterial UDP-sugar-processing enzyme involved in surface polysaccharide assembly. Elimination of the three clearly incompatible options leaves B as the sole biologically coherent choice.


**Missing item-specific fact**

> Positive identification that UDP-GlcNAc 2-epimerase specifically feeds into capsule polysaccharide biosynthesis in Campylobacter (as opposed to peptidoglycan, LPS, or other glycan pathways) requires organism-specific metabolic knowledge. However, this specificity is not needed to eliminate the three distractors, which are categorically incompatible with a bacterial NAD-dependent sugar epimerase.


**Reason**

> While the strongest positive identification of 'capsule biogenesis' benefits from knowing the organism and its specific metabolic network, the provided distractors are all categorically incompatible with a bacterial UDP-sugar epimerase. A model can reason through elimination using general biology: ubiquitination is eukaryotic, ajmaline is a plant alkaloid, and Fe-S cluster machinery is structurally unrelated. This provides meaningful, concrete biological grounds to select B without memorizing the exact database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are categorically incompatible with a bacterial NAD-dependent UDP-sugar epimerase. No reasonable biological argument supports selecting them over B. The question is unambiguous among the given choices.


### Important caveats

- The positive pathway assignment (capsule vs. other glycan pathways like peptidoglycan or LPS) is organism-specific and would require knowledge of Campylobacter metabolism if the distractors included other glycan-related pathways.
- The UniProt annotation is based on experimental evidence (ECO:0000269) from a 2024 Biochemistry paper, not merely computational transfer.
- The firstPublicDate of the UniProt entry is 2025-06-18, meaning this annotation may not have been available at the time the benchmark was constructed; the underlying experimental paper (2024) predates the entry but the curated annotation is recent.
- The reasoning path is primarily eliminative rather than a direct positive identification from sequence features to 'capsule biogenesis' specifically.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains NAD-binding Rossmann-fold motifs (e.g., 'GDTTTAS') characteristic of sugar-processing epimerases/dehydratases, identifying it as a UDP-sugar-processing enzyme in a bacterium. Among the four choices: (A) protein ubiquitination is a eukaryotic-specific process absent in bacteria; (C) ajmaline biosynthesis is a plant-specific monoterpene indole alkaloid pathway; (D) iron-sulfur cluster biosynthesis involves cysteine desulfurases, scaffold proteins, and Fe-S ligases—entirely different enzyme classes with no NAD-dependent epimerase architecture. Only (B) capsule biogenesis is consistent with a bacterial UDP-sugar-processing enzyme involved in surface polysaccharide assembly. Elimination of the three clearly incompatible options leaves B as the sole biologically coherent choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification that UDP-GlcNAc 2-epimerase specifically feeds into capsule polysaccharide biosynthesis in Campylobacter (as opposed to peptidoglycan, LPS, or other glycan pathways) requires organism-specific metabolic knowledge. However, this specificity is not needed to eliminate the three distractors, which are categorically incompatible with a bacterial NAD-dependent sugar epimerase.",
    "reason": "While the strongest positive identification of 'capsule biogenesis' benefits from knowing the organism and its specific metabolic network, the provided distractors are all categorically incompatible with a bacterial UDP-sugar epimerase. A model can reason through elimination using general biology: ubiquitination is eukaryotic, ajmaline is a plant alkaloid, and Fe-S cluster machinery is structurally unrelated. This provides meaningful, concrete biological grounds to select B without memorizing the exact database entry."
  },
  "case_id": "pathway_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3CEN8 (UAGEP_CAMJU) is annotated with PATHWAY: 'Capsule biogenesis; capsule polysaccharide biosynthesis' with evidence code ECO:0000269 (direct assay) from PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The protein is UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) from Campylobacter jejuni, experimentally shown to produce UDP-ManNAcA and CMP-Neu5Ac for capsular polysaccharides. Sequence match is exact (SHA256 confirmed)."
  },
  "important_caveats": [
    "The positive pathway assignment (capsule vs. other glycan pathways like peptidoglycan or LPS) is organism-specific and would require knowledge of Campylobacter metabolism if the distractors included other glycan-related pathways.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269) from a 2024 Biochemistry paper, not merely computational transfer.",
    "The firstPublicDate of the UniProt entry is 2025-06-18, meaning this annotation may not have been available at the time the benchmark was constructed; the underlying experimental paper (2024) predates the entry but the curated annotation is recent.",
    "The reasoning path is primarily eliminative rather than a direct positive identification from sequence features to 'capsule biogenesis' specifically."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are categorically incompatible with a bacterial NAD-dependent UDP-sugar epimerase. No reasonable biological argument supports selecting them over B. The question is unambiguous among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3CEN8 (UAGEP_CAMJU) is annotated with PATHWAY: 'Capsule biogenesis; capsule polysaccharide biosynthesis' with evidence code ECO:0000269 (direct assay) from PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The protein is UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) from Campylobacter jejuni, experimentally shown to produce UDP-ManNAcA and CMP-Neu5Ac for capsular polysaccharides. Sequence match is exact (SHA256 confirmed).",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains NAD-binding Rossmann-fold motifs (e.g., 'GDTTTAS') characteristic of sugar-processing epimerases/dehydratases, identifying it as a UDP-sugar-processing enzyme in a bacterium. Among the four choices: (A) protein ubiquitination is a eukaryotic-specific process absent in bacteria; (C) ajmaline biosynthesis is a plant-specific monoterpene indole alkaloid pathway; (D) iron-sulfur cluster biosynthesis involves cysteine desulfurases, scaffold proteins, and Fe-S ligases—entirely different enzyme classes with no NAD-dependent epimerase architecture. Only (B) capsule biogenesis is consistent with a bacterial UDP-sugar-processing enzyme involved in surface polysaccharide assembly. Elimination of the three clearly incompatible options leaves B as the sole biologically coherent choice.",
    "missing_item_specific_fact": "Positive identification that UDP-GlcNAc 2-epimerase specifically feeds into capsule polysaccharide biosynthesis in Campylobacter (as opposed to peptidoglycan, LPS, or other glycan pathways) requires organism-specific metabolic knowledge. However, this specificity is not needed to eliminate the three distractors, which are categorically incompatible with a bacterial NAD-dependent sugar epimerase.",
    "reason": "While the strongest positive identification of 'capsule biogenesis' benefits from knowing the organism and its specific metabolic network, the provided distractors are all categorically incompatible with a bacterial UDP-sugar epimerase. A model can reason through elimination using general biology: ubiquitination is eukaryotic, ajmaline is a plant alkaloid, and Fe-S cluster machinery is structurally unrelated. This provides meaningful, concrete biological grounds to select B without memorizing the exact database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are categorically incompatible with a bacterial NAD-dependent UDP-sugar epimerase. No reasonable biological argument supports selecting them over B. The question is unambiguous among the given choices."
  },
  "important_caveats": [
    "The positive pathway assignment (capsule vs. other glycan pathways like peptidoglycan or LPS) is organism-specific and would require knowledge of Campylobacter metabolism if the distractors included other glycan-related pathways.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269) from a 2024 Biochemistry paper, not merely computational transfer.",
    "The firstPublicDate of the UniProt entry is 2025-06-18, meaning this annotation may not have been available at the time the benchmark was constructed; the underlying experimental paper (2024) predates the entry but the curated annotation is recent.",
    "The reasoning path is primarily eliminative rather than a direct positive identification from sequence features to 'capsule biogenesis' specifically."
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

**Accession:** `A0A0U3CEN8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:21.799773+00:00.  

```json
"A0A0U3CEN8"
```

Source SHA-256: `79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:21.799773+00:00.  

```json
{"lineage":["Bacteria","Pseudomonadati","Campylobacterota","Epsilonproteobacteria","Campylobacterales","Campylobacteraceae","Campylobacter"],"scientificName":"Campylobacter jejuni","taxonId":197}
```

Source SHA-256: `79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:21.799773+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"Non-hydrolyzing UDP-GlcNAc 2-epimerase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"5.1.3.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetylglucosamine 2-epimerase"}}}
```

Source SHA-256: `79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:21.799773+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"Capsule biogenesis; capsule polysaccharide biosynthesis"}]}
```

Source SHA-256: `79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:21.799773+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"HS:11"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:23.855684+00:00.  

```text
ID   UAGEP_CAMJU             Reviewed;         383 AA.
AC   A0A0U3CEN8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-MAR-2016, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};
DE            EC=5.1.3.14 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=Non-hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};
GN   Name=HS11.17 {ECO:0000303|PubMed:38382015};
OS   Campylobacter jejuni.
OC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;
OC   Campylobacterales; Campylobacteraceae; Campylobacter.
OX   NCBI_TaxID=197;
```

Source SHA-256: `ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19)  
**Locator:** `lines 29-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:23.855684+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RC   STRAIN=HS:11;
RX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;
RA   Ghosh M.K., Raushel F.M.;
RT   "Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-
RT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter
RT   jejuni.";
RL   Biochemistry 63:688-698(2024).
```

Source SHA-256: `ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19)  
**Locator:** `lines 54-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:23.855684+00:00.  

```text
CC   -!- PATHWAY: Capsule biogenesis; capsule polysaccharide biosynthesis.
CC       {ECO:0000269|PubMed:38382015}.
```

Source SHA-256: `ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
