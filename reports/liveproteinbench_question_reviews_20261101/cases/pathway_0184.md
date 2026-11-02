# pathway_0184

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATPSKKRCGVLGATGAVGTRFILLLSQHPLLELVAVGASDRSSGKKYRDAVRWKQSAPMPAKVADLTVRCCDPAEFSDCDIIFSGLDPDAAGEIEMAFLKANFAVFSNAKNYRLDPMVPLVVPLVNAGHIDVIPAQRKHFGLDKGMLVCNSNCAVVGLVVPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPYIPGEEGKISSEARKILGDLNSDLAGFSDQKPLQISVACNRVPVLDGHTVCASLRFVNRPPPTASQVREALREYKPEVQTLGCPSAPKMSIHVMDEVDRPQPRLDRETEGGYACTVGRIREDDSDVFDIQFVALSHNTVLGASGSSILNAESAILKGFV

[Multiple Choices]
A. peptidoglycan biosynthesis. .
B. xylan degradation. .
C. L-isoleucine biosynthesis
D. Amino-acid biosynthesis
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

> The exact sequence matches a UniProt entry annotated as aspartate-semialdehyde dehydrogenase, with amino-acid biosynthesis pathway annotations for methionine and threonine biosynthesis. This supports the broad choice D.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Once identified as aspartate-semialdehyde dehydrogenase, its role in amino-acid biosynthesis distinguishes D from the other choices. The supplied sequence alone does not state that identity or pathway.


**Missing item-specific fact**

> The sequence's protein identity and its pathway annotation or experimentally established function.


**Reason**

> Choosing D depends on identifying this particular sequence as the enzyme and knowing its pathway role; that item-specific fact is not supplied, and exact-sequence recognition is not reasoning from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports the broad amino-acid biosynthesis option; the specific L-isoleucine option is not supported by the cited pathway annotations.


### Important caveats

- The cited UniProt pathway annotations carry experimental evidence codes, but the cited paper's strain is BMU01672; the excerpts do not establish that the exact benchmark protein was assayed directly.
- The accession and annotations are reviewer-only evidence, not information supplied with the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Once identified as aspartate-semialdehyde dehydrogenase, its role in amino-acid biosynthesis distinguishes D from the other choices. The supplied sequence alone does not state that identity or pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's protein identity and its pathway annotation or experimentally established function.",
    "reason": "Choosing D depends on identifying this particular sequence as the enzyme and knowing its pathway role; that item-specific fact is not supplied, and exact-sequence recognition is not reasoning from the input."
  },
  "case_id": "pathway_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as aspartate-semialdehyde dehydrogenase, with amino-acid biosynthesis pathway annotations for methionine and threonine biosynthesis. This supports the broad choice D."
  },
  "important_caveats": [
    "The cited UniProt pathway annotations carry experimental evidence codes, but the cited paper's strain is BMU01672; the excerpts do not establish that the exact benchmark protein was assayed directly.",
    "The accession and annotations are reviewer-only evidence, not information supplied with the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the broad amino-acid biosynthesis option; the specific L-isoleucine option is not supported by the cited pathway annotations."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as aspartate-semialdehyde dehydrogenase, with amino-acid biosynthesis pathway annotations for methionine and threonine biosynthesis. This supports the broad choice D.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Once identified as aspartate-semialdehyde dehydrogenase, its role in amino-acid biosynthesis distinguishes D from the other choices. The supplied sequence alone does not state that identity or pathway.",
    "missing_item_specific_fact": "The sequence's protein identity and its pathway annotation or experimentally established function.",
    "reason": "Choosing D depends on identifying this particular sequence as the enzyme and knowing its pathway role; that item-specific fact is not supplied, and exact-sequence recognition is not reasoning from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the broad amino-acid biosynthesis option; the specific L-isoleucine option is not supported by the cited pathway annotations."
  },
  "important_caveats": [
    "The cited UniProt pathway annotations carry experimental evidence codes, but the cited paper's strain is BMU01672; the excerpts do not establish that the exact benchmark protein was assayed directly.",
    "The accession and annotations are reviewer-only evidence, not information supplied with the question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A080WMA9 (sequence matched, 362 aa) identifies the protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, TrASADH) from Trichophyton rubrum. The PATHWAY annotation explicitly states 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway' and 'Amino-acid biosynthesis; L-threonine biosynthesis,' both supported by experimental evidence (ECO:0000269, PubMed:26869335, X-ray crystallography). Choice D 'Amino-acid biosynthesis' directly matches the annotated pathway category. Choice C (L-isoleucine biosynthesis) is specifically incorrect because in fungi the aspartate pathway does not lead to isoleucine (fungal Ile synthesis proceeds via pyruvate/2-ketobutyrate, not the aspartate pathway).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Some elimination is possible from general knowledge: fungi do not synthesize peptidoglycan (eliminates A), and xylan degradation uses glycoside hydrolases rather than NAD(P)-dependent dehydrogenases (eliminates B). Between C and D, D is the general superset category for any amino-acid biosynthesis pathway, so if one establishes the enzyme participates in amino-acid biosynthesis at all, D is correct. However, positively identifying the protein as aspartate-semialdehyde dehydrogenase (and thus placing it in amino-acid biosynthesis) from the raw 362-aa sequence requires recognizing the ASADH enzyme family or its specific catalytic motifs (conserved Cys, NADP-binding Rossmann fold with specific geometry). The NADP-binding GxGxxG-type motif present in the sequence is shared across many unrelated dehydrogenases and does not uniquely identify ASADH.


**Missing item-specific fact**

> The specific identification of this protein as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) and its placement in the fungal aspartate pathway (leading to Met/Thr, not Ile) requires either database lookup or memorization of the ASADH sequence family. Without this, the sequence alone does not unambiguously distinguish amino-acid biosynthesis from other NADP-dependent dehydrogenase pathways.


**Reason**

> While A and B can be eliminated by general biological reasoning (no peptidoglycan in fungi; xylanases are hydrolases), the positive assignment to amino-acid biosynthesis depends on recognizing the protein as ASADH, which is a specific enzyme-family identification not derivable from generic sequence features alone. The distinction between C (L-isoleucine biosynthesis) and D (general amino-acid biosynthesis) additionally requires knowing that fungal aspartate-pathway ASADH does not feed into isoleucine synthesis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is unambiguously correct as the general pathway category explicitly stated in the annotation. C is specifically wrong (wrong amino acid for fungal aspartate pathway). A and B are clearly incompatible with a fungal NADP-dependent dehydrogenase. No other option is defensible.


### Important caveats

- The UniProt annotation is supported by experimental evidence (X-ray crystallography, PubMed:26869335), not merely computational inference.
- The question design places D as the general superset of C, making D correct for any amino-acid biosynthesis enzyme regardless of the specific amino acid. This somewhat trivializes the C-vs-D discrimination once one establishes the enzyme is in amino-acid biosynthesis.
- The entry was first publicly released in 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2014-10-29.
- The identity of the protein (ASADH) was inferred from reviewer-only UniProt accession metadata absent from the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Some elimination is possible from general knowledge: fungi do not synthesize peptidoglycan (eliminates A), and xylan degradation uses glycoside hydrolases rather than NAD(P)-dependent dehydrogenases (eliminates B). Between C and D, D is the general superset category for any amino-acid biosynthesis pathway, so if one establishes the enzyme participates in amino-acid biosynthesis at all, D is correct. However, positively identifying the protein as aspartate-semialdehyde dehydrogenase (and thus placing it in amino-acid biosynthesis) from the raw 362-aa sequence requires recognizing the ASADH enzyme family or its specific catalytic motifs (conserved Cys, NADP-binding Rossmann fold with specific geometry). The NADP-binding GxGxxG-type motif present in the sequence is shared across many unrelated dehydrogenases and does not uniquely identify ASADH.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this protein as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) and its placement in the fungal aspartate pathway (leading to Met/Thr, not Ile) requires either database lookup or memorization of the ASADH sequence family. Without this, the sequence alone does not unambiguously distinguish amino-acid biosynthesis from other NADP-dependent dehydrogenase pathways.",
    "reason": "While A and B can be eliminated by general biological reasoning (no peptidoglycan in fungi; xylanases are hydrolases), the positive assignment to amino-acid biosynthesis depends on recognizing the protein as ASADH, which is a specific enzyme-family identification not derivable from generic sequence features alone. The distinction between C (L-isoleucine biosynthesis) and D (general amino-acid biosynthesis) additionally requires knowing that fungal aspartate-pathway ASADH does not feed into isoleucine synthesis."
  },
  "case_id": "pathway_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A080WMA9 (sequence matched, 362 aa) identifies the protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, TrASADH) from Trichophyton rubrum. The PATHWAY annotation explicitly states 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway' and 'Amino-acid biosynthesis; L-threonine biosynthesis,' both supported by experimental evidence (ECO:0000269, PubMed:26869335, X-ray crystallography). Choice D 'Amino-acid biosynthesis' directly matches the annotated pathway category. Choice C (L-isoleucine biosynthesis) is specifically incorrect because in fungi the aspartate pathway does not lead to isoleucine (fungal Ile synthesis proceeds via pyruvate/2-ketobutyrate, not the aspartate pathway)."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (X-ray crystallography, PubMed:26869335), not merely computational inference.",
    "The question design places D as the general superset of C, making D correct for any amino-acid biosynthesis enzyme regardless of the specific amino acid. This somewhat trivializes the C-vs-D discrimination once one establishes the enzyme is in amino-acid biosynthesis.",
    "The entry was first publicly released in 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2014-10-29.",
    "The identity of the protein (ASADH) was inferred from reviewer-only UniProt accession metadata absent from the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is unambiguously correct as the general pathway category explicitly stated in the annotation. C is specifically wrong (wrong amino acid for fungal aspartate pathway). A and B are clearly incompatible with a fungal NADP-dependent dehydrogenase. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A080WMA9 (sequence matched, 362 aa) identifies the protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, TrASADH) from Trichophyton rubrum. The PATHWAY annotation explicitly states 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway' and 'Amino-acid biosynthesis; L-threonine biosynthesis,' both supported by experimental evidence (ECO:0000269, PubMed:26869335, X-ray crystallography). Choice D 'Amino-acid biosynthesis' directly matches the annotated pathway category. Choice C (L-isoleucine biosynthesis) is specifically incorrect because in fungi the aspartate pathway does not lead to isoleucine (fungal Ile synthesis proceeds via pyruvate/2-ketobutyrate, not the aspartate pathway).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Some elimination is possible from general knowledge: fungi do not synthesize peptidoglycan (eliminates A), and xylan degradation uses glycoside hydrolases rather than NAD(P)-dependent dehydrogenases (eliminates B). Between C and D, D is the general superset category for any amino-acid biosynthesis pathway, so if one establishes the enzyme participates in amino-acid biosynthesis at all, D is correct. However, positively identifying the protein as aspartate-semialdehyde dehydrogenase (and thus placing it in amino-acid biosynthesis) from the raw 362-aa sequence requires recognizing the ASADH enzyme family or its specific catalytic motifs (conserved Cys, NADP-binding Rossmann fold with specific geometry). The NADP-binding GxGxxG-type motif present in the sequence is shared across many unrelated dehydrogenases and does not uniquely identify ASADH.",
    "missing_item_specific_fact": "The specific identification of this protein as aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) and its placement in the fungal aspartate pathway (leading to Met/Thr, not Ile) requires either database lookup or memorization of the ASADH sequence family. Without this, the sequence alone does not unambiguously distinguish amino-acid biosynthesis from other NADP-dependent dehydrogenase pathways.",
    "reason": "While A and B can be eliminated by general biological reasoning (no peptidoglycan in fungi; xylanases are hydrolases), the positive assignment to amino-acid biosynthesis depends on recognizing the protein as ASADH, which is a specific enzyme-family identification not derivable from generic sequence features alone. The distinction between C (L-isoleucine biosynthesis) and D (general amino-acid biosynthesis) additionally requires knowing that fungal aspartate-pathway ASADH does not feed into isoleucine synthesis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is unambiguously correct as the general pathway category explicitly stated in the annotation. C is specifically wrong (wrong amino acid for fungal aspartate pathway). A and B are clearly incompatible with a fungal NADP-dependent dehydrogenase. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (X-ray crystallography, PubMed:26869335), not merely computational inference.",
    "The question design places D as the general superset of C, making D correct for any amino-acid biosynthesis enzyme regardless of the specific amino acid. This somewhat trivializes the C-vs-D discrimination once one establishes the enzyme is in amino-acid biosynthesis.",
    "The entry was first publicly released in 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2014-10-29.",
    "The identity of the protein (ASADH) was inferred from reviewer-only UniProt accession metadata absent from the evaluated model input."
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

**Accession:** `A0A080WMA9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
"A0A080WMA9"
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26869335","source":"PubMed"}],"value":"TrASADH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26869335","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26869335","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3"}]}
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26869335","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5"}]}
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
{"citation":{"authors":["Li Q.","Mu Z.","Zhao R.","Dahal G.","Viola R.E.","Liu T.","Jin Q.","Cui S."],"citationCrossReferences":[{"database":"PubMed","id":"26869335"},{"database":"DOI","id":"10.1038/srep21067"}],"citationType":"journal article","firstPage":"21067","id":"26869335","journal":"Sci. Rep.","lastPage":"21067","publicationDate":"2016","title":"Structural Insights into the Tetrameric State of Aspartate-beta-semialdehyde Dehydrogenases from Fungal Species.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4ZHS","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4ZIC","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26869335","source":"PubMed"}],"type":"STRAIN","value":"BMU01672"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.55 ANGSTROMS) IN COMPLEX WITH NADP(+)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT","MUTAGENESIS OF 196-ASP--PHE-198 AND ARG-309"]}
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:57.418115+00:00.  

```text
ID   DHAS_TRIRC              Reviewed;         362 AA.
AC   A0A080WMA9; A0A140UHG6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-OCT-2014, sequence version 1.
DT   18-JUN-2025, entry version 38.
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:26869335};
DE   AltName: Full=TrASADH {ECO:0000303|PubMed:26869335};
GN   ORFNames=TERG_03598 {ECO:0000312|EMBL:KFL61260.1};
OS   Trichophyton rubrum (strain ATCC MYA-4607 / CBS 118892) (Athlete's foot
OS   fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Onygenales; Arthrodermataceae; Trichophyton.
OX   NCBI_TaxID=559305 {ECO:0000312|Proteomes:UP000008864};
```

Source SHA-256: `319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)  
**Locator:** `lines 57-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:57.418115+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo
CC       pathway; L-homoserine from L-aspartate: step 2/3.
CC       {ECO:0000269|PubMed:26869335}.
```

Source SHA-256: `319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)  
**Locator:** `lines 60-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:57.418115+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine
CC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:26869335}.
```

Source SHA-256: `319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
