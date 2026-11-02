# pathway_0133

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAATDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNDMGCFTYPLVPGFETVGTATEVGSKVTKVKVGDKVAVGIMVGSCGKCDECVNDRECYCPEVITSYGRIDHDGTPTYGGFSSETVANEKFVFCFPEKLPMAAGAPLLNAGVSVYSAMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSTSKKGEAINDLGADAFLVSTDAEQMQAGSGTLDGILDTVPVVHPIEALLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVVSTIGGSTKETQEMLDFAAEHDITASVEIIPMDYVNTAMERIEKGDVRYRFVIDIGNTLTPPES

[Multiple Choices]
A. Alkaloid biosynthesis
B. 5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis. .
C. Cell wall degradation
D. terpenoid biosynthesis. .
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

> The exact sequence matches a UniProt entry annotated as 1,2-dihydrovomilenine reductase, with the pathway listed as alkaloid biosynthesis, specifically ajmaline biosynthesis. The annotation cites experimental evidence codes and research papers, although those papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with an enzyme, but its sequence alone does not establish the particular metabolic pathway. Broad enzyme properties do not distinguish alkaloid biosynthesis from other possible pathways in the choices.


**Missing item-specific fact**

> The protein-specific function as a dihydrovomilenine reductase in ajmaline biosynthesis, or equivalent organism/function annotation, is absent from the model input.


**Reason**

> Selecting A requires knowing this protein's specific substrate and biological role. Recognizing the exact sequence or consulting its database annotation would supply that missing fact; generic sequence-based enzyme inference would not.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports A for this protein, but the supplied sequence and choices alone do not provide a clear basis for distinguishing the pathway.


### Important caveats

- The sequence matches both current and historical UniProt records, but the author's exact source snapshot is unknown.
- The pathway annotation cites experimental evidence, but the cited primary studies were not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, but its sequence alone does not establish the particular metabolic pathway. Broad enzyme properties do not distinguish alkaloid biosynthesis from other possible pathways in the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific function as a dihydrovomilenine reductase in ajmaline biosynthesis, or equivalent organism/function annotation, is absent from the model input.",
    "reason": "Selecting A requires knowing this protein's specific substrate and biological role. Recognizing the exact sequence or consulting its database annotation would supply that missing fact; generic sequence-based enzyme inference would not."
  },
  "case_id": "pathway_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as 1,2-dihydrovomilenine reductase, with the pathway listed as alkaloid biosynthesis, specifically ajmaline biosynthesis. The annotation cites experimental evidence codes and research papers, although those papers were not independently reviewed here."
  },
  "important_caveats": [
    "The sequence matches both current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The pathway annotation cites experimental evidence, but the cited primary studies were not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports A for this protein, but the supplied sequence and choices alone do not provide a clear basis for distinguishing the pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as 1,2-dihydrovomilenine reductase, with the pathway listed as alkaloid biosynthesis, specifically ajmaline biosynthesis. The annotation cites experimental evidence codes and research papers, although those papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, but its sequence alone does not establish the particular metabolic pathway. Broad enzyme properties do not distinguish alkaloid biosynthesis from other possible pathways in the choices.",
    "missing_item_specific_fact": "The protein-specific function as a dihydrovomilenine reductase in ajmaline biosynthesis, or equivalent organism/function annotation, is absent from the model input.",
    "reason": "Selecting A requires knowing this protein's specific substrate and biological role. Recognizing the exact sequence or consulting its database annotation would supply that missing fact; generic sequence-based enzyme inference would not."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports A for this protein, but the supplied sequence and choices alone do not provide a clear basis for distinguishing the pathway."
  },
  "important_caveats": [
    "The sequence matches both current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The pathway annotation cites experimental evidence, but the cited primary studies were not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0U3S9Q3 (sequence SHA-256 exact match, 363 AA) annotates this protein as 1,2-Dihydrovomilenine reductase (EC 1.3.1.73) from Rauvolfia serpentina, with pathway annotation 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence codes (ECO:0000269) from three independent publications (PubMed 12391554, 26715562, 38212296). The enzyme catalyzes a defined step in ajmaline (an indole alkaloid) biosynthesis. Answer A is well-supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence displays a Rossmann-fold-like nucleotide-binding motif (GGLGGLGHLAV) and zinc-binding cysteine clusters (GSCGKCDECVNDRECYCPE), consistent with a cinnamyl alcohol dehydrogenase (CAD)-like reductase. These features indicate a reductase involved in secondary metabolism but do not specify the substrate or pathway. CAD-like enzymes in plants participate in lignin biosynthesis, phenylpropanoid metabolism, and various alkaloid/terpenoid pathways. Distinguishing 'alkaloid biosynthesis' from 'terpenoid biosynthesis' requires knowing that this enzyme's substrate is dihydrovomilenine, a late intermediate in the ajmaline (monoterpene indole alkaloid) pathway—a protein-specific fact not inferable from sequence features alone.


**Missing item-specific fact**

> The substrate specificity of this particular CAD-like reductase (dihydrovomilenine/vomilenine) and its placement in the ajmaline biosynthetic pathway rather than in lignin, phenylpropanoid, or general terpenoid metabolism. This requires knowledge of the specific enzymatic reaction or the organism's (Rauvolfia serpentina) specialized alkaloid pathway.


**Reason**

> The sequence reveals a reductase with CAD-like architecture, but this class of enzyme spans multiple secondary metabolic pathways. The correct assignment to 'alkaloid biosynthesis' over 'terpenoid biosynthesis' depends on knowing the specific substrate (dihydrovomilenine) and its role in ajmaline biosynthesis—an item-specific experimental fact documented in the cited publications but absent from the provided sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Ajmaline is classified as a 'monoterpene indole alkaloid,' containing both a monoterpene moiety (terpenoid-derived) and an indole moiety (alkaloid-derived). A student aware that the enzyme acts on a monoterpene indole alkaloid intermediate could reasonably argue for 'terpenoid biosynthesis' (D). UniProt specifically assigns it to 'Alkaloid biosynthesis; ajmaline biosynthesis,' but the boundary between terpenoid and alkaloid biosynthesis for MIA (monoterpene indole alkaloid) intermediates is not unambiguous from the pathway name alone. The distractor D is not trivially eliminable by sequence reasoning.


### Important caveats

- The reviewer evidence confirms the UniProt annotation is experimentally supported (ECO:0000269) across three publications, strengthening the key's validity.
- The evaluated model receives only the raw sequence and four pathway names; no organism, substrate, or EC number context is provided.
- The historical UniProt record (entry version 32) and current record (version 34) both carry the same pathway annotation with matching sequence.
- The question does not specify whether 'primary pathway' means the immediate reaction context or the broader biosynthetic category; UniProt uses 'Alkaloid biosynthesis' as the top-level pathway heading.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays a Rossmann-fold-like nucleotide-binding motif (GGLGGLGHLAV) and zinc-binding cysteine clusters (GSCGKCDECVNDRECYCPE), consistent with a cinnamyl alcohol dehydrogenase (CAD)-like reductase. These features indicate a reductase involved in secondary metabolism but do not specify the substrate or pathway. CAD-like enzymes in plants participate in lignin biosynthesis, phenylpropanoid metabolism, and various alkaloid/terpenoid pathways. Distinguishing 'alkaloid biosynthesis' from 'terpenoid biosynthesis' requires knowing that this enzyme's substrate is dihydrovomilenine, a late intermediate in the ajmaline (monoterpene indole alkaloid) pathway—a protein-specific fact not inferable from sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The substrate specificity of this particular CAD-like reductase (dihydrovomilenine/vomilenine) and its placement in the ajmaline biosynthetic pathway rather than in lignin, phenylpropanoid, or general terpenoid metabolism. This requires knowledge of the specific enzymatic reaction or the organism's (Rauvolfia serpentina) specialized alkaloid pathway.",
    "reason": "The sequence reveals a reductase with CAD-like architecture, but this class of enzyme spans multiple secondary metabolic pathways. The correct assignment to 'alkaloid biosynthesis' over 'terpenoid biosynthesis' depends on knowing the specific substrate (dihydrovomilenine) and its role in ajmaline biosynthesis—an item-specific experimental fact documented in the cited publications but absent from the provided sequence and choices."
  },
  "case_id": "pathway_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3S9Q3 (sequence SHA-256 exact match, 363 AA) annotates this protein as 1,2-Dihydrovomilenine reductase (EC 1.3.1.73) from Rauvolfia serpentina, with pathway annotation 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence codes (ECO:0000269) from three independent publications (PubMed 12391554, 26715562, 38212296). The enzyme catalyzes a defined step in ajmaline (an indole alkaloid) biosynthesis. Answer A is well-supported."
  },
  "important_caveats": [
    "The reviewer evidence confirms the UniProt annotation is experimentally supported (ECO:0000269) across three publications, strengthening the key's validity.",
    "The evaluated model receives only the raw sequence and four pathway names; no organism, substrate, or EC number context is provided.",
    "The historical UniProt record (entry version 32) and current record (version 34) both carry the same pathway annotation with matching sequence.",
    "The question does not specify whether 'primary pathway' means the immediate reaction context or the broader biosynthetic category; UniProt uses 'Alkaloid biosynthesis' as the top-level pathway heading."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Ajmaline is classified as a 'monoterpene indole alkaloid,' containing both a monoterpene moiety (terpenoid-derived) and an indole moiety (alkaloid-derived). A student aware that the enzyme acts on a monoterpene indole alkaloid intermediate could reasonably argue for 'terpenoid biosynthesis' (D). UniProt specifically assigns it to 'Alkaloid biosynthesis; ajmaline biosynthesis,' but the boundary between terpenoid and alkaloid biosynthesis for MIA (monoterpene indole alkaloid) intermediates is not unambiguous from the pathway name alone. The distractor D is not trivially eliminable by sequence reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3S9Q3 (sequence SHA-256 exact match, 363 AA) annotates this protein as 1,2-Dihydrovomilenine reductase (EC 1.3.1.73) from Rauvolfia serpentina, with pathway annotation 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence codes (ECO:0000269) from three independent publications (PubMed 12391554, 26715562, 38212296). The enzyme catalyzes a defined step in ajmaline (an indole alkaloid) biosynthesis. Answer A is well-supported.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H1", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence displays a Rossmann-fold-like nucleotide-binding motif (GGLGGLGHLAV) and zinc-binding cysteine clusters (GSCGKCDECVNDRECYCPE), consistent with a cinnamyl alcohol dehydrogenase (CAD)-like reductase. These features indicate a reductase involved in secondary metabolism but do not specify the substrate or pathway. CAD-like enzymes in plants participate in lignin biosynthesis, phenylpropanoid metabolism, and various alkaloid/terpenoid pathways. Distinguishing 'alkaloid biosynthesis' from 'terpenoid biosynthesis' requires knowing that this enzyme's substrate is dihydrovomilenine, a late intermediate in the ajmaline (monoterpene indole alkaloid) pathway—a protein-specific fact not inferable from sequence features alone.",
    "missing_item_specific_fact": "The substrate specificity of this particular CAD-like reductase (dihydrovomilenine/vomilenine) and its placement in the ajmaline biosynthetic pathway rather than in lignin, phenylpropanoid, or general terpenoid metabolism. This requires knowledge of the specific enzymatic reaction or the organism's (Rauvolfia serpentina) specialized alkaloid pathway.",
    "reason": "The sequence reveals a reductase with CAD-like architecture, but this class of enzyme spans multiple secondary metabolic pathways. The correct assignment to 'alkaloid biosynthesis' over 'terpenoid biosynthesis' depends on knowing the specific substrate (dihydrovomilenine) and its role in ajmaline biosynthesis—an item-specific experimental fact documented in the cited publications but absent from the provided sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Ajmaline is classified as a 'monoterpene indole alkaloid,' containing both a monoterpene moiety (terpenoid-derived) and an indole moiety (alkaloid-derived). A student aware that the enzyme acts on a monoterpene indole alkaloid intermediate could reasonably argue for 'terpenoid biosynthesis' (D). UniProt specifically assigns it to 'Alkaloid biosynthesis; ajmaline biosynthesis,' but the boundary between terpenoid and alkaloid biosynthesis for MIA (monoterpene indole alkaloid) intermediates is not unambiguous from the pathway name alone. The distractor D is not trivially eliminable by sequence reasoning."
  },
  "important_caveats": [
    "The reviewer evidence confirms the UniProt annotation is experimentally supported (ECO:0000269) across three publications, strengthening the key's validity.",
    "The evaluated model receives only the raw sequence and four pathway names; no organism, substrate, or EC number context is provided.",
    "The historical UniProt record (entry version 32) and current record (version 34) both carry the same pathway annotation with matching sequence.",
    "The question does not specify whether 'primary pathway' means the immediate reaction context or the broader biosynthetic category; UniProt uses 'Alkaloid biosynthesis' as the top-level pathway heading."
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

**Accession:** `A0A0U3S9Q3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
"A0A0U3S9Q3"
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Protein RR4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsRR4"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Vomilenine reductase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsVR2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"12391554","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.3.1.73"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"1,2-Dihydrovomilenine reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsDHVR"}]}}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"12391554","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"citation":{"authors":["Geissler M.","Burghard M.","Volk J.","Staniek A.","Warzecha H."],"citationCrossReferences":[{"database":"PubMed","id":"26715562"},{"database":"DOI","id":"10.1007/s00425-015-2446-6"}],"citationType":"journal article","firstPage":"813","id":"26715562","journal":"Planta","lastPage":"824","publicationDate":"2016","title":"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.","volume":"243"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ALW82981.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1)","PROTEIN SEQUENCE OF 5-13 AND 298-308","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WKU61918.1","source":"EMBL"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"citation":{"authors":["Gao S.","von Schumann G.","Stoeckigt J."],"citationCrossReferences":[{"database":"PubMed","id":"12391554"},{"database":"DOI","id":"10.1055/s-2002-34935"}],"citationType":"journal article","firstPage":"906","id":"12391554","journal":"Planta Med.","lastPage":"911","publicationDate":"2002","title":"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis of the antiarrhythmic alkaloid ajmaline.","volume":"68"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)  
**Locator:** `lines 1-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:20.990872+00:00.  

```text
ID   DHVOR_RAUSE             Reviewed;         363 AA.
AC   A0A0U3S9Q3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-MAR-2016, sequence version 1.
DT   28-JAN-2026, entry version 32.
DE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};
DE            Short=RsDHVR {ECO:0000303|PubMed:26715562};
DE            EC=1.3.1.73 {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};
DE   AltName: Full=Protein RR4 {ECO:0000303|PubMed:26715562};
DE            Short=RsRR4 {ECO:0000303|PubMed:26715562};
DE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};
DE            Short=RsVR2 {ECO:0000303|PubMed:26715562};
DE            EC=1.5.1.- {ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296};
GN   Name=DHVR {ECO:0000303|PubMed:26715562};
GN   Synonyms=RR4 {ECO:0000303|PubMed:26715562},
GN   VR2 {ECO:0000303|PubMed:26715562};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:20.990872+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:26715562,
CC       ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
