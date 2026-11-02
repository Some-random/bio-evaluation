# pathway_0173

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Carbohydrate degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK

[Multiple Choices]
A. NAD(+) biosynthesis
B. Carbohydrate degradation
C. L-threonine from L-aspartate: step 4/5. .
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

> The supplied sequence exactly matches the rabbit HSD17B14/L-fucose dehydrogenase entry. That entry places the protein in L-fucose degradation, a carbohydrate-degradation pathway; the entry also cites a paper identifying it as the initial enzyme of that pathway. This supports broad choice B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has features consistent with a nucleotide-cofactor-dependent dehydrogenase, which may distinguish it from some choices, but those features do not identify its substrate as L-fucose or establish its pathway.


**Missing item-specific fact**

> The protein-specific substrate and pathway assignment: that this dehydrogenase acts on L-fucose in L-fucose degradation.


**Reason**

> Choosing carbohydrate degradation over the other options depends on the specific enzyme function, which is not supplied by the sequence context or choices and cannot be established from general dehydrogenase-family features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The documented L-fucose degradation role fits the broad carbohydrate-degradation option; the other choices are not comparably supported by the supplied sequence alone.


### Important caveats

- The pathway annotation is a database annotation; its cited paper is identified as reporting the enzyme's L-fucose dehydrogenase function, but the supplied excerpts do not independently present the experimental results.
- The reviewer-only accession and annotations were not available to the evaluated model; the historical and current records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a nucleotide-cofactor-dependent dehydrogenase, which may distinguish it from some choices, but those features do not identify its substrate as L-fucose or establish its pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate and pathway assignment: that this dehydrogenase acts on L-fucose in L-fucose degradation.",
    "reason": "Choosing carbohydrate degradation over the other options depends on the specific enzyme function, which is not supplied by the sequence context or choices and cannot be established from general dehydrogenase-family features alone."
  },
  "case_id": "pathway_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rabbit HSD17B14/L-fucose dehydrogenase entry. That entry places the protein in L-fucose degradation, a carbohydrate-degradation pathway; the entry also cites a paper identifying it as the initial enzyme of that pathway. This supports broad choice B."
  },
  "important_caveats": [
    "The pathway annotation is a database annotation; its cited paper is identified as reporting the enzyme's L-fucose dehydrogenase function, but the supplied excerpts do not independently present the experimental results.",
    "The reviewer-only accession and annotations were not available to the evaluated model; the historical and current records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The documented L-fucose degradation role fits the broad carbohydrate-degradation option; the other choices are not comparably supported by the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rabbit HSD17B14/L-fucose dehydrogenase entry. That entry places the protein in L-fucose degradation, a carbohydrate-degradation pathway; the entry also cites a paper identifying it as the initial enzyme of that pathway. This supports broad choice B.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has features consistent with a nucleotide-cofactor-dependent dehydrogenase, which may distinguish it from some choices, but those features do not identify its substrate as L-fucose or establish its pathway.",
    "missing_item_specific_fact": "The protein-specific substrate and pathway assignment: that this dehydrogenase acts on L-fucose in L-fucose degradation.",
    "reason": "Choosing carbohydrate degradation over the other options depends on the specific enzyme function, which is not supplied by the sequence context or choices and cannot be established from general dehydrogenase-family features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The documented L-fucose degradation role fits the broad carbohydrate-degradation option; the other choices are not comparably supported by the supplied sequence alone."
  },
  "important_caveats": [
    "The pathway annotation is a database annotation; its cited paper is identified as reporting the enzyme's L-fucose dehydrogenase function, but the supplied excerpts do not independently present the experimental results.",
    "The reviewer-only accession and annotations were not available to the evaluated model; the historical and current records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAT9JA24 (sequence matched exactly) annotates this protein as L-fucose dehydrogenase (EC 1.1.1.122) with the pathway comment 'Carbohydrate degradation; L-fucose degradation' (evidence codes ECO:0000305 for pathway, ECO:0000269/PubMed:38944119 for EC assignment). The 2024 JBC paper by Witecka et al. experimentally established HSD17B14 as L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway. The expected answer 'Carbohydrate degradation' matches the top-level UniProt pathway category.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a Rossmann-fold motif (GxGxxG in 'GAARGIGAG' and 'GAVGQLQG'), indicating an NAD(P)-dependent dehydrogenase/reductase. This narrows the field somewhat: option D (aspartate kinase, step 1) is a kinase, not a dehydrogenase, and mammalian threonine biosynthesis from aspartate is not a functional pathway (threonine is essential in mammals), potentially eliminating C and D. However, the Rossmann fold is extremely generic across dehydrogenases and does not uniquely point to carbohydrate degradation over NAD(+) biosynthesis or other oxidoreductase-containing pathways.


**Missing item-specific fact**

> The specific substrate identity of this protein as L-fucose (rather than a steroid, an amino acid intermediate, or a NAD-pathway metabolite) is the critical fact. HSD17B14 was historically annotated as a hydroxysteroid dehydrogenase and only re-annotated as L-fucose dehydrogenase in 2024. Without knowing this specific protein's substrate, the sequence alone cannot distinguish 'Carbohydrate degradation' from other oxidoreductase-associated pathways.


**Reason**

> The Rossmann-fold dehydrogenase signature is shared by thousands of enzymes across many pathways. The correct answer depends on recognizing this specific sequence as HSD17B14/L-fucose dehydrogenase, a recent (2024) functional re-annotation. This is an item-specific database fact, not a property derivable from general sequence analysis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the Rossmann fold could superficially fit multiple dehydrogenase pathways, options C and D (threonine biosynthesis from aspartate) are biologically implausible in a mammalian (rabbit) protein since mammals lack this biosynthetic pathway. Option A (NAD+ biosynthesis) involves primarily kinases and transferases in mammals, not a Rossmann-fold dehydrogenase of this architecture. Thus, with general biological knowledge, B is the most defensible choice among the four, even though the precise identification still relies on knowing the substrate.


### Important caveats

- The functional re-annotation of HSD17B14 from hydroxysteroid dehydrogenase to L-fucose dehydrogenase is recent (2024, PubMed:38944119). Models trained on older data may still associate this sequence with steroid metabolism, which is not among the options.
- The UniProt pathway annotation carries ECO:0000305 (inferred by curator), while the EC assignment carries experimental evidence (ECO:0000269). The pathway assignment is thus a curated inference from the experimental function, not independently measured.
- The reviewer-only evidence confirms the sequence matches A0AAT9JA24 exactly (SHA-256 match), but the accession was absent from the model input.
- Mammalian threonine is an essential amino acid; the pathway 'L-threonine from L-aspartate' does not operate in mammals, making C and D biologically implausible for a rabbit protein regardless of sequence features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold motif (GxGxxG in 'GAARGIGAG' and 'GAVGQLQG'), indicating an NAD(P)-dependent dehydrogenase/reductase. This narrows the field somewhat: option D (aspartate kinase, step 1) is a kinase, not a dehydrogenase, and mammalian threonine biosynthesis from aspartate is not a functional pathway (threonine is essential in mammals), potentially eliminating C and D. However, the Rossmann fold is extremely generic across dehydrogenases and does not uniquely point to carbohydrate degradation over NAD(+) biosynthesis or other oxidoreductase-containing pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of this protein as L-fucose (rather than a steroid, an amino acid intermediate, or a NAD-pathway metabolite) is the critical fact. HSD17B14 was historically annotated as a hydroxysteroid dehydrogenase and only re-annotated as L-fucose dehydrogenase in 2024. Without knowing this specific protein's substrate, the sequence alone cannot distinguish 'Carbohydrate degradation' from other oxidoreductase-associated pathways.",
    "reason": "The Rossmann-fold dehydrogenase signature is shared by thousands of enzymes across many pathways. The correct answer depends on recognizing this specific sequence as HSD17B14/L-fucose dehydrogenase, a recent (2024) functional re-annotation. This is an item-specific database fact, not a property derivable from general sequence analysis."
  },
  "case_id": "pathway_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAT9JA24 (sequence matched exactly) annotates this protein as L-fucose dehydrogenase (EC 1.1.1.122) with the pathway comment 'Carbohydrate degradation; L-fucose degradation' (evidence codes ECO:0000305 for pathway, ECO:0000269/PubMed:38944119 for EC assignment). The 2024 JBC paper by Witecka et al. experimentally established HSD17B14 as L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway. The expected answer 'Carbohydrate degradation' matches the top-level UniProt pathway category."
  },
  "important_caveats": [
    "The functional re-annotation of HSD17B14 from hydroxysteroid dehydrogenase to L-fucose dehydrogenase is recent (2024, PubMed:38944119). Models trained on older data may still associate this sequence with steroid metabolism, which is not among the options.",
    "The UniProt pathway annotation carries ECO:0000305 (inferred by curator), while the EC assignment carries experimental evidence (ECO:0000269). The pathway assignment is thus a curated inference from the experimental function, not independently measured.",
    "The reviewer-only evidence confirms the sequence matches A0AAT9JA24 exactly (SHA-256 match), but the accession was absent from the model input.",
    "Mammalian threonine is an essential amino acid; the pathway 'L-threonine from L-aspartate' does not operate in mammals, making C and D biologically implausible for a rabbit protein regardless of sequence features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the Rossmann fold could superficially fit multiple dehydrogenase pathways, options C and D (threonine biosynthesis from aspartate) are biologically implausible in a mammalian (rabbit) protein since mammals lack this biosynthetic pathway. Option A (NAD+ biosynthesis) involves primarily kinases and transferases in mammals, not a Rossmann-fold dehydrogenase of this architecture. Thus, with general biological knowledge, B is the most defensible choice among the four, even though the precise identification still relies on knowing the substrate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAT9JA24 (sequence matched exactly) annotates this protein as L-fucose dehydrogenase (EC 1.1.1.122) with the pathway comment 'Carbohydrate degradation; L-fucose degradation' (evidence codes ECO:0000305 for pathway, ECO:0000269/PubMed:38944119 for EC assignment). The 2024 JBC paper by Witecka et al. experimentally established HSD17B14 as L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway. The expected answer 'Carbohydrate degradation' matches the top-level UniProt pathway category.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold motif (GxGxxG in 'GAARGIGAG' and 'GAVGQLQG'), indicating an NAD(P)-dependent dehydrogenase/reductase. This narrows the field somewhat: option D (aspartate kinase, step 1) is a kinase, not a dehydrogenase, and mammalian threonine biosynthesis from aspartate is not a functional pathway (threonine is essential in mammals), potentially eliminating C and D. However, the Rossmann fold is extremely generic across dehydrogenases and does not uniquely point to carbohydrate degradation over NAD(+) biosynthesis or other oxidoreductase-containing pathways.",
    "missing_item_specific_fact": "The specific substrate identity of this protein as L-fucose (rather than a steroid, an amino acid intermediate, or a NAD-pathway metabolite) is the critical fact. HSD17B14 was historically annotated as a hydroxysteroid dehydrogenase and only re-annotated as L-fucose dehydrogenase in 2024. Without knowing this specific protein's substrate, the sequence alone cannot distinguish 'Carbohydrate degradation' from other oxidoreductase-associated pathways.",
    "reason": "The Rossmann-fold dehydrogenase signature is shared by thousands of enzymes across many pathways. The correct answer depends on recognizing this specific sequence as HSD17B14/L-fucose dehydrogenase, a recent (2024) functional re-annotation. This is an item-specific database fact, not a property derivable from general sequence analysis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the Rossmann fold could superficially fit multiple dehydrogenase pathways, options C and D (threonine biosynthesis from aspartate) are biologically implausible in a mammalian (rabbit) protein since mammals lack this biosynthetic pathway. Option A (NAD+ biosynthesis) involves primarily kinases and transferases in mammals, not a Rossmann-fold dehydrogenase of this architecture. Thus, with general biological knowledge, B is the most defensible choice among the four, even though the precise identification still relies on knowing the substrate."
  },
  "important_caveats": [
    "The functional re-annotation of HSD17B14 from hydroxysteroid dehydrogenase to L-fucose dehydrogenase is recent (2024, PubMed:38944119). Models trained on older data may still associate this sequence with steroid metabolism, which is not among the options.",
    "The UniProt pathway annotation carries ECO:0000305 (inferred by curator), while the EC assignment carries experimental evidence (ECO:0000269). The pathway assignment is thus a curated inference from the experimental function, not independently measured.",
    "The reviewer-only evidence confirms the sequence matches A0AAT9JA24 exactly (SHA-256 match), but the accession was absent from the model input.",
    "Mammalian threonine is an essential amino acid; the pathway 'L-threonine from L-aspartate' does not operate in mammals, making C and D biologically implausible for a rabbit protein regardless of sequence features."
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

**Accession:** `A0AAT9JA24` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Hydroxysteroid 17-beta dehydrogenase 14"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"value":"1.1.1.122"}],"fullName":{"value":"L-fucose dehydrogenase"}}}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Carbohydrate degradation; L-fucose degradation"}]}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"citation":{"authors":["Witecka A.","Kazak V.","Kwiatkowski S.","Kiersztan A.","Jagielski A.K.","Kozminski W.","Augustyniak R.","Drozak J."],"citationCrossReferences":[{"database":"PubMed","id":"38944119"},{"database":"DOI","id":"10.1016/j.jbc.2024.107501"}],"citationType":"journal article","firstPage":"107501","id":"38944119","journal":"J. Biol. Chem.","lastPage":"107501","publicationDate":"2024","title":"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.","volume":"300"},"referenceNumber":2,"referencePositions":["IDENTIFICATION","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF TYR-154"]}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
ID   DHB14_RABIT             Reviewed;         284 AA.
AC   A0AAT9JA24; A0A5F9CLT4;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 2.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=L-fucose dehydrogenase;
DE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};
DE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;
GN   Name=HSD17B14;
OS   Oryctolagus cuniculus (Rabbit).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Lagomorpha; Leporidae; Oryctolagus.
OX   NCBI_TaxID=9986;
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 35-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
RN   [2]
RP   IDENTIFICATION, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL
RP   PROPERTIES, AND MUTAGENESIS OF TYR-154.
RX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;
RA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,
RA   Kozminski W., Augustyniak R., Drozak J.;
RT   "Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose
RT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.";
RL   J. Biol. Chem. 300:107501-107501(2024).
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 85-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
CC   -!- PATHWAY: Carbohydrate degradation; L-fucose degradation. {ECO:0000305}.
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
