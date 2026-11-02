# pathway_0055

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Metabolic intermediate biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSFGESHGKAIGCVIDGFLPNVEINFDLIQRQLNRRRPNQSKLTSNRNEPDKLIVLSGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNLSGYPSNGSGNPPNGSDHPSNRSGNPPNRSDPRVDESTRETSPPSGEKLLVTTSNNCGGILAGITTGNNIVFRSAIKPVSSIQIEKETCNFFGEKCKLKVTGMHDCCILPRLPPIIEASTSIVIGDMILRQVAKYGHSKLPSVGSLSRSTRE

[Multiple Choices]
A. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
B. One-carbon metabolism
C. Antifungal biosynthesis. .
D. Metabolic intermediate biosynthesis
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

> The exact sequence matches the Plasmodium vivax chorismate synthase entry, whose pathway annotation places it in metabolic intermediate biosynthesis, specifically chorismate biosynthesis. The pathway annotation is transferred by similarity (ECO:0000250), so it supports the key as a database annotation rather than direct experimental evidence for that pathway assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices do not provide a reliable sequence-independent clue to this protein's specific pathway. Identifying chorismate synthase from the sequence would require protein-specific functional identification or sequence homology, then linking that enzyme to chorismate biosynthesis.


**Missing item-specific fact**

> The protein's identity or enzyme function as chorismate synthase, and its role in the chorismate biosynthesis pathway.


**Reason**

> The sequence and choices alone do not establish the protein-specific function needed to select D; knowing or retrieving that annotation is necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the supported chorismate synthase assignment, D is the matching pathway category; the other choices describe different pathways.


### Important caveats

- The sequence match is exact, but the original author's data source and annotation snapshot are unknown.
- The cited pathway assignment is similarity-transferred; the evidence does not independently verify that pathway experimentally for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices do not provide a reliable sequence-independent clue to this protein's specific pathway. Identifying chorismate synthase from the sequence would require protein-specific functional identification or sequence homology, then linking that enzyme to chorismate biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity or enzyme function as chorismate synthase, and its role in the chorismate biosynthesis pathway.",
    "reason": "The sequence and choices alone do not establish the protein-specific function needed to select D; knowing or retrieving that annotation is necessary."
  },
  "case_id": "pathway_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium vivax chorismate synthase entry, whose pathway annotation places it in metabolic intermediate biosynthesis, specifically chorismate biosynthesis. The pathway annotation is transferred by similarity (ECO:0000250), so it supports the key as a database annotation rather than direct experimental evidence for that pathway assignment."
  },
  "important_caveats": [
    "The sequence match is exact, but the original author's data source and annotation snapshot are unknown.",
    "The cited pathway assignment is similarity-transferred; the evidence does not independently verify that pathway experimentally for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the supported chorismate synthase assignment, D is the matching pathway category; the other choices describe different pathways."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium vivax chorismate synthase entry, whose pathway annotation places it in metabolic intermediate biosynthesis, specifically chorismate biosynthesis. The pathway annotation is transferred by similarity (ECO:0000250), so it supports the key as a database annotation rather than direct experimental evidence for that pathway assignment.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices do not provide a reliable sequence-independent clue to this protein's specific pathway. Identifying chorismate synthase from the sequence would require protein-specific functional identification or sequence homology, then linking that enzyme to chorismate biosynthesis.",
    "missing_item_specific_fact": "The protein's identity or enzyme function as chorismate synthase, and its role in the chorismate biosynthesis pathway.",
    "reason": "The sequence and choices alone do not establish the protein-specific function needed to select D; knowing or retrieving that annotation is necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the supported chorismate synthase assignment, D is the matching pathway category; the other choices describe different pathways."
  },
  "important_caveats": [
    "The sequence match is exact, but the original author's data source and annotation snapshot are unknown.",
    "The cited pathway assignment is similarity-transferred; the evidence does not independently verify that pathway experimentally for this specific protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A5K264 (Plasmodium vivax chorismate synthase, sequence matched) explicitly annotates the pathway as 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7' (C5, H3). The expected answer D ('Metabolic intermediate biosynthesis') is the exact top-level pathway category from this annotation. The other options are clearly incorrect: A describes dihydropteroate synthase, B (one-carbon metabolism) and C (antifungal biosynthesis) do not match chorismate synthase function.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If one could identify the protein as chorismate synthase from sequence, one could reason that chorismate is a well-known metabolic intermediate (branch-point precursor for aromatic amino acids, folate, ubiquinone), placing it in 'metabolic intermediate biosynthesis' and eliminating A (dihydrofolate/dihydropteroate synthase reaction), B (one-carbon metabolism), and C (antifungal biosynthesis). However, identifying chorismate synthase from a 547-aa Plasmodium sequence without database access requires recognizing specific conserved motifs (e.g., FMN-binding region) that are not trivially identifiable by general biological reasoning alone.


**Missing item-specific fact**

> The identification of this particular 547-aa sequence as chorismate synthase (EC 4.2.3.5 / EC 1.5.1.38) from Plasmodium vivax, and the UniProt-specific pathway taxonomy term 'Metabolic intermediate biosynthesis' as the top-level category for chorismate biosynthesis. The sequence lacks universally recognizable, easily-derivable motifs that would allow confident identification without prior database knowledge or memorization of chorismate synthase sequence signatures.


**Reason**

> The critical bottleneck is protein identification from sequence. While the downstream reasoning (chorismate = metabolic intermediate → eliminates A, B, C) is straightforward once the enzyme is known, the sequence itself does not present obvious, general-knowledge-accessible features that would let a model confidently identify it as chorismate synthase without database lookup or memorized sequence knowledge. The pathway label 'Metabolic intermediate biosynthesis' is also a UniProt-specific hierarchical term rather than a universally used biochemical pathway name.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the UniProt annotation, D is the only option matching the top-level pathway category. A describes a different enzyme's reaction, B and C describe unrelated pathways. No other option is defensible for chorismate synthase.


### Important caveats

- The UniProt pathway annotation (ECO:0000250, similarity-based from Q12640) is a computational/transferred annotation for the pathway assignment, though the protein's bifunctional catalytic activity (EC 1.5.1.38 and EC 4.2.3.5) was experimentally confirmed (ECO:0000269/305, PubMed:31381947).
- The term 'Metabolic intermediate biosynthesis' is a UniProt-specific pathway hierarchy label; in general biochemistry, chorismate biosynthesis is more commonly referred to as part of aromatic amino acid biosynthesis or the shikimate pathway. A model reasoning purely from general biochemistry might struggle with this specific taxonomy.
- The sequence is from Plasmodium vivax (Salvador I strain); the bifunctional nature (shikimate oxidoreductase + chorismate synthase) is a parasite-specific feature confirmed by the 2019 Khera et al. study.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If one could identify the protein as chorismate synthase from sequence, one could reason that chorismate is a well-known metabolic intermediate (branch-point precursor for aromatic amino acids, folate, ubiquinone), placing it in 'metabolic intermediate biosynthesis' and eliminating A (dihydrofolate/dihydropteroate synthase reaction), B (one-carbon metabolism), and C (antifungal biosynthesis). However, identifying chorismate synthase from a 547-aa Plasmodium sequence without database access requires recognizing specific conserved motifs (e.g., FMN-binding region) that are not trivially identifiable by general biological reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this particular 547-aa sequence as chorismate synthase (EC 4.2.3.5 / EC 1.5.1.38) from Plasmodium vivax, and the UniProt-specific pathway taxonomy term 'Metabolic intermediate biosynthesis' as the top-level category for chorismate biosynthesis. The sequence lacks universally recognizable, easily-derivable motifs that would allow confident identification without prior database knowledge or memorization of chorismate synthase sequence signatures.",
    "reason": "The critical bottleneck is protein identification from sequence. While the downstream reasoning (chorismate = metabolic intermediate → eliminates A, B, C) is straightforward once the enzyme is known, the sequence itself does not present obvious, general-knowledge-accessible features that would let a model confidently identify it as chorismate synthase without database lookup or memorized sequence knowledge. The pathway label 'Metabolic intermediate biosynthesis' is also a UniProt-specific hierarchical term rather than a universally used biochemical pathway name."
  },
  "case_id": "pathway_0055",
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
    "reason": "The UniProt entry A5K264 (Plasmodium vivax chorismate synthase, sequence matched) explicitly annotates the pathway as 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7' (C5, H3). The expected answer D ('Metabolic intermediate biosynthesis') is the exact top-level pathway category from this annotation. The other options are clearly incorrect: A describes dihydropteroate synthase, B (one-carbon metabolism) and C (antifungal biosynthesis) do not match chorismate synthase function."
  },
  "important_caveats": [
    "The UniProt pathway annotation (ECO:0000250, similarity-based from Q12640) is a computational/transferred annotation for the pathway assignment, though the protein's bifunctional catalytic activity (EC 1.5.1.38 and EC 4.2.3.5) was experimentally confirmed (ECO:0000269/305, PubMed:31381947).",
    "The term 'Metabolic intermediate biosynthesis' is a UniProt-specific pathway hierarchy label; in general biochemistry, chorismate biosynthesis is more commonly referred to as part of aromatic amino acid biosynthesis or the shikimate pathway. A model reasoning purely from general biochemistry might struggle with this specific taxonomy.",
    "The sequence is from Plasmodium vivax (Salvador I strain); the bifunctional nature (shikimate oxidoreductase + chorismate synthase) is a parasite-specific feature confirmed by the 2019 Khera et al. study."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the UniProt annotation, D is the only option matching the top-level pathway category. A describes a different enzyme's reaction, B and C describe unrelated pathways. No other option is defensible for chorismate synthase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A5K264 (Plasmodium vivax chorismate synthase, sequence matched) explicitly annotates the pathway as 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7' (C5, H3). The expected answer D ('Metabolic intermediate biosynthesis') is the exact top-level pathway category from this annotation. The other options are clearly incorrect: A describes dihydropteroate synthase, B (one-carbon metabolism) and C (antifungal biosynthesis) do not match chorismate synthase function.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If one could identify the protein as chorismate synthase from sequence, one could reason that chorismate is a well-known metabolic intermediate (branch-point precursor for aromatic amino acids, folate, ubiquinone), placing it in 'metabolic intermediate biosynthesis' and eliminating A (dihydrofolate/dihydropteroate synthase reaction), B (one-carbon metabolism), and C (antifungal biosynthesis). However, identifying chorismate synthase from a 547-aa Plasmodium sequence without database access requires recognizing specific conserved motifs (e.g., FMN-binding region) that are not trivially identifiable by general biological reasoning alone.",
    "missing_item_specific_fact": "The identification of this particular 547-aa sequence as chorismate synthase (EC 4.2.3.5 / EC 1.5.1.38) from Plasmodium vivax, and the UniProt-specific pathway taxonomy term 'Metabolic intermediate biosynthesis' as the top-level category for chorismate biosynthesis. The sequence lacks universally recognizable, easily-derivable motifs that would allow confident identification without prior database knowledge or memorization of chorismate synthase sequence signatures.",
    "reason": "The critical bottleneck is protein identification from sequence. While the downstream reasoning (chorismate = metabolic intermediate → eliminates A, B, C) is straightforward once the enzyme is known, the sequence itself does not present obvious, general-knowledge-accessible features that would let a model confidently identify it as chorismate synthase without database lookup or memorized sequence knowledge. The pathway label 'Metabolic intermediate biosynthesis' is also a UniProt-specific hierarchical term rather than a universally used biochemical pathway name."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the UniProt annotation, D is the only option matching the top-level pathway category. A describes a different enzyme's reaction, B and C describe unrelated pathways. No other option is defensible for chorismate synthase."
  },
  "important_caveats": [
    "The UniProt pathway annotation (ECO:0000250, similarity-based from Q12640) is a computational/transferred annotation for the pathway assignment, though the protein's bifunctional catalytic activity (EC 1.5.1.38 and EC 4.2.3.5) was experimentally confirmed (ECO:0000269/305, PubMed:31381947).",
    "The term 'Metabolic intermediate biosynthesis' is a UniProt-specific pathway hierarchy label; in general biochemistry, chorismate biosynthesis is more commonly referred to as part of aromatic amino acid biosynthesis or the shikimate pathway. A model reasoning purely from general biochemistry might struggle with this specific taxonomy.",
    "The sequence is from Plasmodium vivax (Salvador I strain); the bifunctional nature (shikimate oxidoreductase + chorismate synthase) is a parasite-specific feature confirmed by the 2019 Khera et al. study."
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

**Accession:** `A5K264` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 64. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
"A5K264"
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"31381947","source":"PubMed"}],"value":"1.5.1.38"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"value":"4.2.3.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"31381947","source":"PubMed"}],"value":"Chorismate synthase"}}}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q12640","source":"UniProtKB"}],"value":"Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7"}]}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"citation":{"authors":["Khera H.K.","Singh S.K.","Singh S."],"citationCrossReferences":[{"database":"PubMed","id":"31381947"},{"database":"DOI","id":"10.1016/j.molbiopara.2019.111202"}],"citationType":"journal article","firstPage":"111202","id":"31381947","journal":"Mol. Biochem. Parasitol.","lastPage":"111202","publicationDate":"2019","title":"Chorismate synthase from malaria parasites is bifunctional enzyme.","volume":"233"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
ID   AROC_PLAVS              Reviewed;         547 AA.
AC   A5K264;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   08-FEB-2011, sequence version 1.
DT   28-JAN-2026, entry version 64.
DE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:31381947};
DE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};
DE            EC=4.2.3.5 {ECO:0000269|PubMed:31381947};
GN   Name=CS {ECO:0000305}; ORFNames=PVX_114265 {ECO:0000312|EMBL:EDL46514.1};
OS   Plasmodium vivax (strain Salvador I).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).
OX   NCBI_TaxID=126793 {ECO:0000312|Proteomes:UP000008333};
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 29-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, AND CATALYTIC ACTIVITY.
RX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;
RA   Khera H.K., Singh S.K., Singh S.;
RT   "Chorismate synthase from malaria parasites is bifunctional enzyme.";
RL   Mol. Biochem. Parasitol. 233:111202-111202(2019).
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 54-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
CC   -!- PATHWAY: Metabolic intermediate biosynthesis; chorismate biosynthesis;
CC       chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step
CC       7/7. {ECO:0000250|UniProtKB:Q12640}.
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
