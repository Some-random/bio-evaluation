# pathway_0147

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSANTGKPARHYLISYPRTASNLLLKILALDSQPNFSSGGFDGGYFFMPADDILTDPRIRVRARSISDWTADERAQLKETFQACFEAQQRWLESAESQGQSVFVKEHTVFFADPTARSCLQFGPSATSEPAWTVEYAGGSTHSKLNITVLPDEFLLTWLPTFLIRHPALAFPSLYRTVIKREGKESAAADNFASLLTTVEWSRSLYDFYVQNRESLPCSPDQRLEWPIVLDADDIIAHPATVTLYCDKIGMDPRQLCFNWDQLKSEELSKIEPNQLAMRMSLYQSTGIDTSKSSRGINVDDEATKWRSEFGIAVADHIEKLVRGAMADYEYLRARRLRAD

[Multiple Choices]
A. Secondary metabolite biosynthesis. .
B. Alkaloid biosynthesis
C. pyruvate from D-glyceraldehyde 3-phosphate: step 2/5. .
D. ergot alkaloid biosynthesis. .
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

> The exact sequence matches UniProt entry A0A455ZLR3, which annotates this protein's pathway as “Secondary metabolite biosynthesis,” consistent with choice A. The annotation is linked to a cited publication, but the supplied excerpts do not establish a direct experimental measurement of pathway function.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently specific argument to identify this protein's pathway among the listed choices; recognizing a general enzyme family would not resolve its particular biosynthetic-cluster role.


**Missing item-specific fact**

> The protein-specific annotation that this sequence is sulfotransferase ppzF in a pyrrolopyrazine biosynthesis cluster, with a secondary-metabolite-biosynthesis pathway assignment.


**Reason**

> The pathway assignment depends on the protein's specific cluster annotation and associated literature, neither of which is supplied in the question. Exact-sequence recognition or recall of its database entry would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Secondary metabolite biosynthesis is a broad category that can include alkaloid biosynthesis, so A and B are not necessarily mutually exclusive. The matched database annotation supports A, but the option wording does not explicitly distinguish a broad pathway category from a more specific product-class category.


### Important caveats

- Reviewer-only database evidence supports the expected answer but was absent from the evaluated model input.
- The cited UniProt pathway annotation is linked to literature; these excerpts alone do not establish direct experimental validation.
- The author’s exact source snapshot is unknown, although a historical UniProt record with the matching sequence also contains the same pathway annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific argument to identify this protein's pathway among the listed choices; recognizing a general enzyme family would not resolve its particular biosynthetic-cluster role.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation that this sequence is sulfotransferase ppzF in a pyrrolopyrazine biosynthesis cluster, with a secondary-metabolite-biosynthesis pathway assignment.",
    "reason": "The pathway assignment depends on the protein's specific cluster annotation and associated literature, neither of which is supplied in the question. Exact-sequence recognition or recall of its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "pathway_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A0A455ZLR3, which annotates this protein's pathway as “Secondary metabolite biosynthesis,” consistent with choice A. The annotation is linked to a cited publication, but the supplied excerpts do not establish a direct experimental measurement of pathway function."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the expected answer but was absent from the evaluated model input.",
    "The cited UniProt pathway annotation is linked to literature; these excerpts alone do not establish direct experimental validation.",
    "The author’s exact source snapshot is unknown, although a historical UniProt record with the matching sequence also contains the same pathway annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Secondary metabolite biosynthesis is a broad category that can include alkaloid biosynthesis, so A and B are not necessarily mutually exclusive. The matched database annotation supports A, but the option wording does not explicitly distinguish a broad pathway category from a more specific product-class category."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A0A455ZLR3, which annotates this protein's pathway as “Secondary metabolite biosynthesis,” consistent with choice A. The annotation is linked to a cited publication, but the supplied excerpts do not establish a direct experimental measurement of pathway function.",
    "evidence_ids": ["C1", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific argument to identify this protein's pathway among the listed choices; recognizing a general enzyme family would not resolve its particular biosynthetic-cluster role.",
    "missing_item_specific_fact": "The protein-specific annotation that this sequence is sulfotransferase ppzF in a pyrrolopyrazine biosynthesis cluster, with a secondary-metabolite-biosynthesis pathway assignment.",
    "reason": "The pathway assignment depends on the protein's specific cluster annotation and associated literature, neither of which is supplied in the question. Exact-sequence recognition or recall of its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Secondary metabolite biosynthesis is a broad category that can include alkaloid biosynthesis, so A and B are not necessarily mutually exclusive. The matched database annotation supports A, but the option wording does not explicitly distinguish a broad pathway category from a more specific product-class category."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the expected answer but was absent from the evaluated model input.",
    "The cited UniProt pathway annotation is linked to literature; these excerpts alone do not establish direct experimental validation.",
    "The author’s exact source snapshot is unknown, although a historical UniProt record with the matching sequence also contains the same pathway annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A455ZLR3 (Sulfotransferase ppzF / Pyrrolopyrazine biosynthesis cluster protein F from Metarhizium majus ARSEF 297) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' (ECO:0000305, PubMed:30452111). The protein is a sulfotransferase (EC 2.8.2.-) in the pyrrolopyrazine biosynthetic gene cluster, which UniProt classifies under the broad 'Secondary metabolite biosynthesis' pathway. The sequence in the question matches the UniProt entry exactly (340 aa, SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could eliminate choice C (glycolytic step) by recognizing the sulfotransferase fold and transferase function, inconsistent with glycolysis. However, distinguishing A ('Secondary metabolite biosynthesis') from B ('Alkaloid biosynthesis') requires knowing that UniProt's pathway taxonomy classifies pyrrolopyrazine biosynthesis under the broad 'Secondary metabolite biosynthesis' heading rather than under 'Alkaloid biosynthesis,' even though pyrrolopyrazines are nitrogen-containing heterocyclic natural products that satisfy a chemical definition of 'alkaloid.' Distinguishing A from D requires knowing that pyrrolopyrazine biosynthesis is a distinct pathway from ergot alkaloid biosynthesis despite sharing tryptophan-derived precursors.


**Missing item-specific fact**

> The specific UniProt pathway taxonomy assignment for pyrrolopyrazine biosynthesis (i.e., that it is annotated under 'Secondary metabolite biosynthesis' rather than 'Alkaloid biosynthesis' or 'Ergot alkaloid biosynthesis'). This is a database classification decision not derivable from the sequence alone.


**Reason**

> While the sulfotransferase domain and fungal origin narrow the field, the critical distinction between the broad 'Secondary metabolite biosynthesis' label and the more specific 'Alkaloid biosynthesis' label depends on UniProt's particular pathway hierarchy for pyrrolopyrazine biosynthesis. A chemically literate model might reasonably classify pyrrolopyrazines as alkaloids. The correct answer depends on knowing the specific annotation taxonomy rather than on general biochemical reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Pyrrolopyrazines are nitrogen-containing heterocyclic compounds produced by fungi, which satisfies the general chemical definition of an alkaloid. A model reasoning from first principles could defensibly select B ('Alkaloid biosynthesis') as the pathway. The choice of A over B rests on UniProt's specific pathway taxonomy, which places pyrrolopyrazine biosynthesis under the broad 'Secondary metabolite biosynthesis' heading rather than under an 'alkaloid' sub-pathway. Choice D is less defensible since pyrrolopyrazines are biosynthetically and structurally distinct from ergot alkaloids (e.g., ergotamine, ergometrine).


### Important caveats

- The UniProt pathway annotation carries evidence code ECO:0000305 (inferred from a single PubMed reference, 30452111), indicating it was derived from the biosynthetic gene cluster characterization paper rather than direct enzymatic assay of this specific step.
- The 'Secondary metabolite biosynthesis' pathway label in UniProt is a broad umbrella category; it is not a specific metabolic pathway in the KEGG/Reactome sense but a UniProt-internal classification.
- The identity of the protein as ppzF was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence with no accession or organism information.
- Choice C (pyruvate from D-glyceraldehyde 3-phosphate: step 2/5) is an obvious glycolysis distractor irrelevant to a sulfotransferase.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could eliminate choice C (glycolytic step) by recognizing the sulfotransferase fold and transferase function, inconsistent with glycolysis. However, distinguishing A ('Secondary metabolite biosynthesis') from B ('Alkaloid biosynthesis') requires knowing that UniProt's pathway taxonomy classifies pyrrolopyrazine biosynthesis under the broad 'Secondary metabolite biosynthesis' heading rather than under 'Alkaloid biosynthesis,' even though pyrrolopyrazines are nitrogen-containing heterocyclic natural products that satisfy a chemical definition of 'alkaloid.' Distinguishing A from D requires knowing that pyrrolopyrazine biosynthesis is a distinct pathway from ergot alkaloid biosynthesis despite sharing tryptophan-derived precursors.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt pathway taxonomy assignment for pyrrolopyrazine biosynthesis (i.e., that it is annotated under 'Secondary metabolite biosynthesis' rather than 'Alkaloid biosynthesis' or 'Ergot alkaloid biosynthesis'). This is a database classification decision not derivable from the sequence alone.",
    "reason": "While the sulfotransferase domain and fungal origin narrow the field, the critical distinction between the broad 'Secondary metabolite biosynthesis' label and the more specific 'Alkaloid biosynthesis' label depends on UniProt's particular pathway hierarchy for pyrrolopyrazine biosynthesis. A chemically literate model might reasonably classify pyrrolopyrazines as alkaloids. The correct answer depends on knowing the specific annotation taxonomy rather than on general biochemical reasoning from the sequence."
  },
  "case_id": "pathway_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A455ZLR3 (Sulfotransferase ppzF / Pyrrolopyrazine biosynthesis cluster protein F from Metarhizium majus ARSEF 297) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' (ECO:0000305, PubMed:30452111). The protein is a sulfotransferase (EC 2.8.2.-) in the pyrrolopyrazine biosynthetic gene cluster, which UniProt classifies under the broad 'Secondary metabolite biosynthesis' pathway. The sequence in the question matches the UniProt entry exactly (340 aa, SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000305 (inferred from a single PubMed reference, 30452111), indicating it was derived from the biosynthetic gene cluster characterization paper rather than direct enzymatic assay of this specific step.",
    "The 'Secondary metabolite biosynthesis' pathway label in UniProt is a broad umbrella category; it is not a specific metabolic pathway in the KEGG/Reactome sense but a UniProt-internal classification.",
    "The identity of the protein as ppzF was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence with no accession or organism information.",
    "Choice C (pyruvate from D-glyceraldehyde 3-phosphate: step 2/5) is an obvious glycolysis distractor irrelevant to a sulfotransferase."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Pyrrolopyrazines are nitrogen-containing heterocyclic compounds produced by fungi, which satisfies the general chemical definition of an alkaloid. A model reasoning from first principles could defensibly select B ('Alkaloid biosynthesis') as the pathway. The choice of A over B rests on UniProt's specific pathway taxonomy, which places pyrrolopyrazine biosynthesis under the broad 'Secondary metabolite biosynthesis' heading rather than under an 'alkaloid' sub-pathway. Choice D is less defensible since pyrrolopyrazines are biosynthetically and structurally distinct from ergot alkaloids (e.g., ergotamine, ergometrine)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A455ZLR3 (Sulfotransferase ppzF / Pyrrolopyrazine biosynthesis cluster protein F from Metarhizium majus ARSEF 297) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' (ECO:0000305, PubMed:30452111). The protein is a sulfotransferase (EC 2.8.2.-) in the pyrrolopyrazine biosynthetic gene cluster, which UniProt classifies under the broad 'Secondary metabolite biosynthesis' pathway. The sequence in the question matches the UniProt entry exactly (340 aa, SHA-256 confirmed).",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could eliminate choice C (glycolytic step) by recognizing the sulfotransferase fold and transferase function, inconsistent with glycolysis. However, distinguishing A ('Secondary metabolite biosynthesis') from B ('Alkaloid biosynthesis') requires knowing that UniProt's pathway taxonomy classifies pyrrolopyrazine biosynthesis under the broad 'Secondary metabolite biosynthesis' heading rather than under 'Alkaloid biosynthesis,' even though pyrrolopyrazines are nitrogen-containing heterocyclic natural products that satisfy a chemical definition of 'alkaloid.' Distinguishing A from D requires knowing that pyrrolopyrazine biosynthesis is a distinct pathway from ergot alkaloid biosynthesis despite sharing tryptophan-derived precursors.",
    "missing_item_specific_fact": "The specific UniProt pathway taxonomy assignment for pyrrolopyrazine biosynthesis (i.e., that it is annotated under 'Secondary metabolite biosynthesis' rather than 'Alkaloid biosynthesis' or 'Ergot alkaloid biosynthesis'). This is a database classification decision not derivable from the sequence alone.",
    "reason": "While the sulfotransferase domain and fungal origin narrow the field, the critical distinction between the broad 'Secondary metabolite biosynthesis' label and the more specific 'Alkaloid biosynthesis' label depends on UniProt's particular pathway hierarchy for pyrrolopyrazine biosynthesis. A chemically literate model might reasonably classify pyrrolopyrazines as alkaloids. The correct answer depends on knowing the specific annotation taxonomy rather than on general biochemical reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Pyrrolopyrazines are nitrogen-containing heterocyclic compounds produced by fungi, which satisfies the general chemical definition of an alkaloid. A model reasoning from first principles could defensibly select B ('Alkaloid biosynthesis') as the pathway. The choice of A over B rests on UniProt's specific pathway taxonomy, which places pyrrolopyrazine biosynthesis under the broad 'Secondary metabolite biosynthesis' heading rather than under an 'alkaloid' sub-pathway. Choice D is less defensible since pyrrolopyrazines are biosynthetically and structurally distinct from ergot alkaloids (e.g., ergotamine, ergometrine)."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000305 (inferred from a single PubMed reference, 30452111), indicating it was derived from the biosynthetic gene cluster characterization paper rather than direct enzymatic assay of this specific step.",
    "The 'Secondary metabolite biosynthesis' pathway label in UniProt is a broad umbrella category; it is not a specific metabolic pathway in the KEGG/Reactome sense but a UniProt-internal classification.",
    "The identity of the protein as ppzF was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence with no accession or organism information.",
    "Choice C (pyruvate from D-glyceraldehyde 3-phosphate: step 2/5) is an obvious glycolysis distractor irrelevant to a sulfotransferase."
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

**Accession:** `A0A455ZLR3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 10. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.946847+00:00.  

```json
"A0A455ZLR3"
```

Source SHA-256: `4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.946847+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"Pyrrolopyrazine biosynthesis cluster protein F"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30452111","source":"PubMed"}],"value":"2.8.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"Sulfotransferase ppzF"}}}
```

Source SHA-256: `4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.946847+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30452111","source":"PubMed"}],"value":"Secondary metabolite biosynthesis"}]}
```

Source SHA-256: `4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.946847+00:00.  

```json
{"citation":{"authors":["Berry D.","Mace W.","Rehner S.A.","Grage K.","Dijkwel P.P.","Young C.A.","Scott B."],"citationCrossReferences":[{"database":"PubMed","id":"30452111"},{"database":"DOI","id":"10.1111/1462-2920.14483"}],"citationType":"journal article","firstPage":"928","id":"30452111","journal":"Environ. Microbiol.","lastPage":"939","publicationDate":"2019","title":"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.","volume":"21"},"referenceComments":[{"type":"STRAIN","value":"ARSEF 297"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","PATHWAY"]}
```

Source SHA-256: `4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)  
**Locator:** `lines 50-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 10 / 1.  
**Retrieved:** 2026-11-02T04:25:19.015576+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis.
CC       {ECO:0000305|PubMed:30452111}.
CC   ---------------------------------------------------------------------------
CC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms
CC   Distributed under the Creative Commons Attribution (CC BY 4.0) License
CC   ---------------------------------------------------------------------------
```

Source SHA-256: `ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
