# pathway_0183

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Antifungal biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MYDVIVIGAGWCGLVAAKTYLQACPDAQVLIVDGDTSIGGTWSKERLYPHLVAEAHYGLFEFSDLPMNGDSVLPDGRIPSTAVHAYLVEYATKFNLIQRIRLNTWIENVRREAGELGMHWTLTAAGSQEQLHAKKVIITTGLTSEAFIPSLPGRDEFEGEVLHSKALGHPQTVERISDPSIRHVVVYGGSKSAFDAVYLLLRAGKTVDWVIREGGGGPSMMTPLSVLGQPSFRLNNSRLLALLSPHPFGTPGEQLSWWQRVVHHRSGQWAQFMILTIWRVMNYLFLRPWGYDSSPNGKRLKPLLGLDSLFWSPATLGVMTHPELWEEIHSGQRVKIHRDAITGLARDKRVMLSSGQELSSADLVVCATGWHARHSFFAPEEQLAVGLPGTASFDPKSQQKWLDLQRTADREITEELPILQKNPIPPPPLRCEDDHHLYRFIAPSRETPSHERSIAFVGFLRTAGAPIVYEAQSLWATAYLTGALEVPEAPQREREIARTNAWIRRRYLCGRKVPFALFDFLPYVDMLYRDLGINPNRKPNQIAELCGLYRPQDFKGVVSEWLANQQAKDVNGN

[Multiple Choices]
A. ajmaline biosynthesis. .
B. Protein modification
C. Antifungal biosynthesis. .
D. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
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

> The sequence exactly matches the UniProt record, which annotates the protein to antifungal biosynthesis and cites a publication with functional and pathway evidence. This supports the key as an annotation-backed claim; the cited primary study was not independently reviewed here.

Citations as saved: [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but general sequence features do not identify which specific biosynthetic pathway it serves.


**Missing item-specific fact**

> The protein-specific functional assignment linking this sequence to the restricticin/antifungal biosynthesis pathway, or equivalent pathway evidence.


**Reason**

> Distinguishing antifungal biosynthesis from the other named pathways requires protein-specific annotation or experimental context absent from the prompt. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices name distinct pathway categories, and the supporting annotation selects C. The lack of sequence-based grounds to identify that pathway is a lookup-dependence issue, not evidence that multiple choices are equally correct.


### Important caveats

- The pathway claim is supported by a UniProt annotation carrying ECO:0000269 and a publication citation; the primary paper's results were not independently checked.
- The sequence match and relevant historical record support applying the annotation to this sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but general sequence features do not identify which specific biosynthetic pathway it serves.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment linking this sequence to the restricticin/antifungal biosynthesis pathway, or equivalent pathway evidence.",
    "reason": "Distinguishing antifungal biosynthesis from the other named pathways requires protein-specific annotation or experimental context absent from the prompt. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "pathway_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, which annotates the protein to antifungal biosynthesis and cites a publication with functional and pathway evidence. This supports the key as an annotation-backed claim; the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The pathway claim is supported by a UniProt annotation carrying ECO:0000269 and a publication citation; the primary paper's results were not independently checked.",
    "The sequence match and relevant historical record support applying the annotation to this sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct pathway categories, and the supporting annotation selects C. The lack of sequence-based grounds to identify that pathway is a lookup-dependence issue, not evidence that multiple choices are equally correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, which annotates the protein to antifungal biosynthesis and cites a publication with functional and pathway evidence. This supports the key as an annotation-backed claim; the cited primary study was not independently reviewed here.",
    "evidence_ids": ["H3", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but general sequence features do not identify which specific biosynthetic pathway it serves.",
    "missing_item_specific_fact": "The protein-specific functional assignment linking this sequence to the restricticin/antifungal biosynthesis pathway, or equivalent pathway evidence.",
    "reason": "Distinguishing antifungal biosynthesis from the other named pathways requires protein-specific annotation or experimental context absent from the prompt. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct pathway categories, and the supporting annotation selects C. The lack of sequence-based grounds to identify that pathway is a lookup-dependence issue, not evidence that multiple choices are equally correct."
  },
  "important_caveats": [
    "The pathway claim is supported by a UniProt annotation carrying ECO:0000269 and a publication citation; the primary paper's results were not independently checked.",
    "The sequence match and relevant historical record support applying the annotation to this sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry P0DXV5 (RESA_ASPSL, FAD-dependent monooxygenase resA / Restricticin biosynthesis cluster protein A) from Aspergillus sclerotiorum. The pathway comment explicitly states 'Antifungal biosynthesis' with evidence code ECO:0000269 (inferred from direct assay), referencing PubMed:39105744 (2024, J. Agric. Food Chem.). The protein is part of the restricticin biosynthesis cluster, and restricticin is an antifungal compound. The annotation is experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a Rossmann-fold-like FAD-binding motif (GAGWCGLVAA near N-terminus), consistent with FAD-dependent monooxygenase activity. This could help eliminate option D (chorismate step 7/7 = DAHP synthase, a completely different enzyme class) and arguably option A (ajmaline biosynthesis is a plant-specific alkaloid pathway involving strictosidine synthase and other enzymes, not FAD monooxygenases). However, FAD-dependent monooxygenases participate in numerous fungal secondary metabolite pathways, and the specific assignment to 'Antifungal biosynthesis' (i.e., the restricticin cluster) cannot be derived from sequence motifs alone.


**Missing item-specific fact**

> The specific identity of this protein as 'Restricticin biosynthesis cluster protein A' and the classification of the restricticin pathway under 'Antifungal biosynthesis' in UniProt. This is a very recent annotation (entry first published 2025-02-05, reference paper 2024) and the restricticin biosynthesis cluster was characterized via genome mining and heterologous expression. Without knowing the protein's specific role in the restricticin gene cluster, a model cannot uniquely assign it to 'Antifungal biosynthesis' rather than another fungal secondary metabolite biosynthesis pathway.


**Reason**

> While sequence-level FAD-binding motifs can partially eliminate some distractors (D, possibly A), the positive identification of 'Antifungal biosynthesis' as the pathway requires knowledge of this protein's membership in the restricticin biosynthesis cluster, a specific and recently characterized gene cluster. This is an item-specific database/experimental fact not derivable from general biological reasoning on the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are sufficiently distinct: ajmaline biosynthesis (plant alkaloid pathway), protein modification (generic post-translational category), antifungal biosynthesis (fungal specialized metabolite pathway), and chorismate step 7/7 (aromatic amino acid biosynthesis). Given the evidence, only C is correct. The distractors are not defensible alternatives.


### Important caveats

- The UniProt entry P0DXV5 was first published on 2025-02-05, making this a very recent annotation. The underlying paper (PubMed:39105744) was published in 2024.
- The EC number is listed as 1.-.-.- (incomplete), indicating the precise catalytic mechanism is not fully characterized.
- The paper title emphasizes 'phytotoxic activity' rather than antifungal activity, though the UniProt pathway annotation explicitly states 'Antifungal biosynthesis' with direct-assay evidence. Restricticin is known in the literature as an antifungal compound.
- The sequence is 573 aa and flagged as 'Precursor' in UniProt, suggesting post-translational processing; the pathway annotation applies to the mature protein's function within the cluster.
- The identity origin note states the accession was inferred mechanically from dataset image-path metadata, not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold-like FAD-binding motif (GAGWCGLVAA near N-terminus), consistent with FAD-dependent monooxygenase activity. This could help eliminate option D (chorismate step 7/7 = DAHP synthase, a completely different enzyme class) and arguably option A (ajmaline biosynthesis is a plant-specific alkaloid pathway involving strictosidine synthase and other enzymes, not FAD monooxygenases). However, FAD-dependent monooxygenases participate in numerous fungal secondary metabolite pathways, and the specific assignment to 'Antifungal biosynthesis' (i.e., the restricticin cluster) cannot be derived from sequence motifs alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as 'Restricticin biosynthesis cluster protein A' and the classification of the restricticin pathway under 'Antifungal biosynthesis' in UniProt. This is a very recent annotation (entry first published 2025-02-05, reference paper 2024) and the restricticin biosynthesis cluster was characterized via genome mining and heterologous expression. Without knowing the protein's specific role in the restricticin gene cluster, a model cannot uniquely assign it to 'Antifungal biosynthesis' rather than another fungal secondary metabolite biosynthesis pathway.",
    "reason": "While sequence-level FAD-binding motifs can partially eliminate some distractors (D, possibly A), the positive identification of 'Antifungal biosynthesis' as the pathway requires knowledge of this protein's membership in the restricticin biosynthesis cluster, a specific and recently characterized gene cluster. This is an item-specific database/experimental fact not derivable from general biological reasoning on the sequence alone."
  },
  "case_id": "pathway_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry P0DXV5 (RESA_ASPSL, FAD-dependent monooxygenase resA / Restricticin biosynthesis cluster protein A) from Aspergillus sclerotiorum. The pathway comment explicitly states 'Antifungal biosynthesis' with evidence code ECO:0000269 (inferred from direct assay), referencing PubMed:39105744 (2024, J. Agric. Food Chem.). The protein is part of the restricticin biosynthesis cluster, and restricticin is an antifungal compound. The annotation is experimentally supported."
  },
  "important_caveats": [
    "The UniProt entry P0DXV5 was first published on 2025-02-05, making this a very recent annotation. The underlying paper (PubMed:39105744) was published in 2024.",
    "The EC number is listed as 1.-.-.- (incomplete), indicating the precise catalytic mechanism is not fully characterized.",
    "The paper title emphasizes 'phytotoxic activity' rather than antifungal activity, though the UniProt pathway annotation explicitly states 'Antifungal biosynthesis' with direct-assay evidence. Restricticin is known in the literature as an antifungal compound.",
    "The sequence is 573 aa and flagged as 'Precursor' in UniProt, suggesting post-translational processing; the pathway annotation applies to the mature protein's function within the cluster.",
    "The identity origin note states the accession was inferred mechanically from dataset image-path metadata, not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct: ajmaline biosynthesis (plant alkaloid pathway), protein modification (generic post-translational category), antifungal biosynthesis (fungal specialized metabolite pathway), and chorismate step 7/7 (aromatic amino acid biosynthesis). Given the evidence, only C is correct. The distractors are not defensible alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry P0DXV5 (RESA_ASPSL, FAD-dependent monooxygenase resA / Restricticin biosynthesis cluster protein A) from Aspergillus sclerotiorum. The pathway comment explicitly states 'Antifungal biosynthesis' with evidence code ECO:0000269 (inferred from direct assay), referencing PubMed:39105744 (2024, J. Agric. Food Chem.). The protein is part of the restricticin biosynthesis cluster, and restricticin is an antifungal compound. The annotation is experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold-like FAD-binding motif (GAGWCGLVAA near N-terminus), consistent with FAD-dependent monooxygenase activity. This could help eliminate option D (chorismate step 7/7 = DAHP synthase, a completely different enzyme class) and arguably option A (ajmaline biosynthesis is a plant-specific alkaloid pathway involving strictosidine synthase and other enzymes, not FAD monooxygenases). However, FAD-dependent monooxygenases participate in numerous fungal secondary metabolite pathways, and the specific assignment to 'Antifungal biosynthesis' (i.e., the restricticin cluster) cannot be derived from sequence motifs alone.",
    "missing_item_specific_fact": "The specific identity of this protein as 'Restricticin biosynthesis cluster protein A' and the classification of the restricticin pathway under 'Antifungal biosynthesis' in UniProt. This is a very recent annotation (entry first published 2025-02-05, reference paper 2024) and the restricticin biosynthesis cluster was characterized via genome mining and heterologous expression. Without knowing the protein's specific role in the restricticin gene cluster, a model cannot uniquely assign it to 'Antifungal biosynthesis' rather than another fungal secondary metabolite biosynthesis pathway.",
    "reason": "While sequence-level FAD-binding motifs can partially eliminate some distractors (D, possibly A), the positive identification of 'Antifungal biosynthesis' as the pathway requires knowledge of this protein's membership in the restricticin biosynthesis cluster, a specific and recently characterized gene cluster. This is an item-specific database/experimental fact not derivable from general biological reasoning on the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct: ajmaline biosynthesis (plant alkaloid pathway), protein modification (generic post-translational category), antifungal biosynthesis (fungal specialized metabolite pathway), and chorismate step 7/7 (aromatic amino acid biosynthesis). Given the evidence, only C is correct. The distractors are not defensible alternatives."
  },
  "important_caveats": [
    "The UniProt entry P0DXV5 was first published on 2025-02-05, making this a very recent annotation. The underlying paper (PubMed:39105744) was published in 2024.",
    "The EC number is listed as 1.-.-.- (incomplete), indicating the precise catalytic mechanism is not fully characterized.",
    "The paper title emphasizes 'phytotoxic activity' rather than antifungal activity, though the UniProt pathway annotation explicitly states 'Antifungal biosynthesis' with direct-assay evidence. Restricticin is known in the literature as an antifungal compound.",
    "The sequence is 573 aa and flagged as 'Precursor' in UniProt, suggesting post-translational processing; the pathway annotation applies to the mature protein's function within the cluster.",
    "The identity origin note states the accession was inferred mechanically from dataset image-path metadata, not provided to the evaluated model."
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

**Accession:** `P0DXV5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:47.174193+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein A"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"value":"1.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"FAD-dependent monooxygenase resA"}}}
```

Source SHA-256: `e707f20abd7826b390bb5fc8cb46d8df7f258be31be61e0129f1d19c24be05d4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:47.174193+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39105744","source":"PubMed"}],"value":"Antifungal biosynthesis"}]}
```

Source SHA-256: `e707f20abd7826b390bb5fc8cb46d8df7f258be31be61e0129f1d19c24be05d4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV5.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:47.174193+00:00.  

```json
{"citation":{"authors":["Lu Y.","Li Y.","Dou M.","Liu D.","Lin W.","Fan A."],"citationCrossReferences":[{"database":"PubMed","id":"39105744"},{"database":"DOI","id":"10.1021/acs.jafc.4c04244"}],"citationType":"journal article","firstPage":"18520","id":"39105744","journal":"J. Agric. Food Chem.","lastPage":"18527","publicationDate":"2024","title":"Discovery of a hybrid molecule with phytotoxic activity by genome mining, heterologous expression, and OSMAC strategy.","volume":"72"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","PATHWAY"]}
```

Source SHA-256: `e707f20abd7826b390bb5fc8cb46d8df7f258be31be61e0129f1d19c24be05d4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV5?format=txt&versions=3)  
**Locator:** `lines 16-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:49.115408+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.
RX   PubMed=39105744; DOI=10.1021/acs.jafc.4c04244;
RA   Lu Y., Li Y., Dou M., Liu D., Lin W., Fan A.;
RT   "Discovery of a hybrid molecule with phytotoxic activity by genome mining,
RT   heterologous expression, and OSMAC strategy.";
RL   J. Agric. Food Chem. 72:18520-18527(2024).
```

Source SHA-256: `8f3c70f33ba4a6cc4d094784bec8580161b3aa6521967c7a1063dc12558b2f14`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV5?format=txt&versions=3)  
**Locator:** `lines 41-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:49.115408+00:00.  

```text
CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000269|PubMed:39105744}.
```

Source SHA-256: `8f3c70f33ba4a6cc4d094784bec8580161b3aa6521967c7a1063dc12558b2f14`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 183. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
