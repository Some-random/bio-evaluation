# pathway_0197

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
MKAIISVSPGRAALVHDRPLPSLRNGYLLVRTKAVALNPTDWKHIEITERPGILFGCDYAGVVEKIGPGISSRFQVGDRVAGFVHGGNSQEPQDGAFAEYILAKADIQILIPEHMSFEEAATLGVGVTSVGQGLYQALQLPFPGTQGEDPKTPTEEQQPLLIYGGSTASGVLGIQFAKLSGFAPLAVCSPDHFDLVETLGAVAQFDYADGEEAVQEIQDYVDRMSKPLRLAWDTVSIPSSAQFCGDALSALDECHYASLLPIKCQRSDVTSTTTMAYTVFGEDWGMGATRFPAVATDAEFGRRWWALVQELLDQGRIQTHRIIIGENGLDGVLAGLERLRDSQVRGAKLVYRV

[Multiple Choices]
A. O-acetyl-L-homoserine from L-homoserine: step 1/1. .
B. Protein biosynthesis
C. Antifungal biosynthesis. .
D. Secondary metabolite biosynthesis. .
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

> The exact sequence matches the UniProt entry for trans-enoyl reductase rstn7, whose pathway annotation is “Antifungal biosynthesis” and cites a 2021 publication. The historical entry also contains this annotation, so the key is supported, though the primary paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with an enzyme, which may make protein biosynthesis less plausible, but it does not by itself establish which specific biosynthetic pathway the enzyme serves.


**Missing item-specific fact**

> The protein-specific association of Rstn7 with the restricticin biosynthetic cluster and its antifungal-biosynthesis role.


**Reason**

> Distinguishing antifungal biosynthesis from other secondary-metabolite pathways requires a protein-specific annotation or equivalent knowledge not supplied in the question. Recognizing or looking up this sequence could provide that fact, but would not constitute reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Antifungal biosynthesis is a specific kind of secondary-metabolite biosynthesis, so option D is a broader description that also applies. Option C is the more specific pathway annotation, but the choices are not mutually exclusive.


### Important caveats

- The reviewer-only annotation is sequence-matched, but the author’s exact source snapshot is unknown.
- The cited pathway annotation is evidence for the key; the cited primary paper was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, which may make protein biosynthesis less plausible, but it does not by itself establish which specific biosynthetic pathway the enzyme serves.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific association of Rstn7 with the restricticin biosynthetic cluster and its antifungal-biosynthesis role.",
    "reason": "Distinguishing antifungal biosynthesis from other secondary-metabolite pathways requires a protein-specific annotation or equivalent knowledge not supplied in the question. Recognizing or looking up this sequence could provide that fact, but would not constitute reasoning from the supplied input."
  },
  "case_id": "pathway_0197",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for trans-enoyl reductase rstn7, whose pathway annotation is “Antifungal biosynthesis” and cites a 2021 publication. The historical entry also contains this annotation, so the key is supported, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched, but the author’s exact source snapshot is unknown.",
    "The cited pathway annotation is evidence for the key; the cited primary paper was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Antifungal biosynthesis is a specific kind of secondary-metabolite biosynthesis, so option D is a broader description that also applies. Option C is the more specific pathway annotation, but the choices are not mutually exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0197",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for trans-enoyl reductase rstn7, whose pathway annotation is “Antifungal biosynthesis” and cites a 2021 publication. The historical entry also contains this annotation, so the key is supported, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, which may make protein biosynthesis less plausible, but it does not by itself establish which specific biosynthetic pathway the enzyme serves.",
    "missing_item_specific_fact": "The protein-specific association of Rstn7 with the restricticin biosynthetic cluster and its antifungal-biosynthesis role.",
    "reason": "Distinguishing antifungal biosynthesis from other secondary-metabolite pathways requires a protein-specific annotation or equivalent knowledge not supplied in the question. Recognizing or looking up this sequence could provide that fact, but would not constitute reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Antifungal biosynthesis is a specific kind of secondary-metabolite biosynthesis, so option D is a broader description that also applies. Option C is the more specific pathway annotation, but the choices are not mutually exclusive."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched, but the author’s exact source snapshot is unknown.",
    "The cited pathway annotation is evidence for the key; the cited primary paper was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0L1JEX1 (sequence matched exactly, 353 AA) explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (direct assay) from PubMed:33857369. The protein is identified as Trans-enoyl reductase rstn7, part of the restricticin biosynthesis cluster. Restricticin is a CYP51 inhibitor with antifungal activity, as demonstrated in the cited JACS 2021 paper. The historical entry (version 28) contains the same pathway annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains motifs consistent with a trans-enoyl reductase domain (e.g., 'GQGLY' and related enoyl reductase signatures), identifying it as a component of a modular polyketide/nonribosomal peptide synthetase assembly line. This general feature points toward secondary metabolite biosynthesis (D). However, the specific 'Antifungal biosynthesis' (C) designation depends on knowing that the end product of this cluster (restricticin) inhibits CYP51 and is classified as an antifungal agent — a property of the final compound, not of the enzyme domain itself.


**Missing item-specific fact**

> Knowledge that the rstn7-containing biosynthetic gene cluster produces restricticin, a CYP51 inhibitor classified under the 'Antifungal biosynthesis' pathway in UniProt, rather than the broader 'Secondary metabolite biosynthesis' category. This product-level biological activity annotation is not inferable from the enoyl reductase domain sequence alone.


**Reason**

> From the sequence, a model can reasonably identify a trans-enoyl reductase domain within a fungal secondary metabolite biosynthetic assembly line, supporting option D. Distinguishing C from D requires knowing that this specific cluster's product (restricticin) is an antifungal CYP51 inhibitor and that UniProt classifies it under 'Antifungal biosynthesis' rather than the generic 'Secondary metabolite biosynthesis' label. This is an item-specific database annotation fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Restricticin is simultaneously a secondary metabolite and an antifungal agent. Option D ('Secondary metabolite biosynthesis') is a valid broader description of the pathway this enzyme participates in. Option C ('Antifungal biosynthesis') is the specific UniProt pathway annotation. Without the database-specific classification, the sequence features of an enoyl reductase domain in a fungal PKS/NRPS cluster do not uniquely favor C over D. The question relies on the specific UniProt pathway label to disambiguate.


### Important caveats

- The evidence code ECO:0000269 (direct assay) confirms experimental support for the antifungal annotation, but this experimental knowledge is not derivable from the sequence.
- The UniProt pathway taxonomy places this under 'Antifungal biosynthesis' rather than a generic 'Secondary metabolite biosynthesis' heading, which is a database-specific classification choice.
- Options A and B are clearly incorrect distractors (homoserine O-acetyltransferase reaction; ribosomal protein synthesis), so the effective discrimination is between C and D.
- The accession and pathway annotation were absent from the evaluated model input; the model sees only the 353-aa sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs consistent with a trans-enoyl reductase domain (e.g., 'GQGLY' and related enoyl reductase signatures), identifying it as a component of a modular polyketide/nonribosomal peptide synthetase assembly line. This general feature points toward secondary metabolite biosynthesis (D). However, the specific 'Antifungal biosynthesis' (C) designation depends on knowing that the end product of this cluster (restricticin) inhibits CYP51 and is classified as an antifungal agent — a property of the final compound, not of the enzyme domain itself.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowledge that the rstn7-containing biosynthetic gene cluster produces restricticin, a CYP51 inhibitor classified under the 'Antifungal biosynthesis' pathway in UniProt, rather than the broader 'Secondary metabolite biosynthesis' category. This product-level biological activity annotation is not inferable from the enoyl reductase domain sequence alone.",
    "reason": "From the sequence, a model can reasonably identify a trans-enoyl reductase domain within a fungal secondary metabolite biosynthetic assembly line, supporting option D. Distinguishing C from D requires knowing that this specific cluster's product (restricticin) is an antifungal CYP51 inhibitor and that UniProt classifies it under 'Antifungal biosynthesis' rather than the generic 'Secondary metabolite biosynthesis' label. This is an item-specific database annotation fact."
  },
  "case_id": "pathway_0197",
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
    "reason": "The UniProt entry A0A0L1JEX1 (sequence matched exactly, 353 AA) explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (direct assay) from PubMed:33857369. The protein is identified as Trans-enoyl reductase rstn7, part of the restricticin biosynthesis cluster. Restricticin is a CYP51 inhibitor with antifungal activity, as demonstrated in the cited JACS 2021 paper. The historical entry (version 28) contains the same pathway annotation."
  },
  "important_caveats": [
    "The evidence code ECO:0000269 (direct assay) confirms experimental support for the antifungal annotation, but this experimental knowledge is not derivable from the sequence.",
    "The UniProt pathway taxonomy places this under 'Antifungal biosynthesis' rather than a generic 'Secondary metabolite biosynthesis' heading, which is a database-specific classification choice.",
    "Options A and B are clearly incorrect distractors (homoserine O-acetyltransferase reaction; ribosomal protein synthesis), so the effective discrimination is between C and D.",
    "The accession and pathway annotation were absent from the evaluated model input; the model sees only the 353-aa sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Restricticin is simultaneously a secondary metabolite and an antifungal agent. Option D ('Secondary metabolite biosynthesis') is a valid broader description of the pathway this enzyme participates in. Option C ('Antifungal biosynthesis') is the specific UniProt pathway annotation. Without the database-specific classification, the sequence features of an enoyl reductase domain in a fungal PKS/NRPS cluster do not uniquely favor C over D. The question relies on the specific UniProt pathway label to disambiguate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0197",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0L1JEX1 (sequence matched exactly, 353 AA) explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (direct assay) from PubMed:33857369. The protein is identified as Trans-enoyl reductase rstn7, part of the restricticin biosynthesis cluster. Restricticin is a CYP51 inhibitor with antifungal activity, as demonstrated in the cited JACS 2021 paper. The historical entry (version 28) contains the same pathway annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains motifs consistent with a trans-enoyl reductase domain (e.g., 'GQGLY' and related enoyl reductase signatures), identifying it as a component of a modular polyketide/nonribosomal peptide synthetase assembly line. This general feature points toward secondary metabolite biosynthesis (D). However, the specific 'Antifungal biosynthesis' (C) designation depends on knowing that the end product of this cluster (restricticin) inhibits CYP51 and is classified as an antifungal agent — a property of the final compound, not of the enzyme domain itself.",
    "missing_item_specific_fact": "Knowledge that the rstn7-containing biosynthetic gene cluster produces restricticin, a CYP51 inhibitor classified under the 'Antifungal biosynthesis' pathway in UniProt, rather than the broader 'Secondary metabolite biosynthesis' category. This product-level biological activity annotation is not inferable from the enoyl reductase domain sequence alone.",
    "reason": "From the sequence, a model can reasonably identify a trans-enoyl reductase domain within a fungal secondary metabolite biosynthetic assembly line, supporting option D. Distinguishing C from D requires knowing that this specific cluster's product (restricticin) is an antifungal CYP51 inhibitor and that UniProt classifies it under 'Antifungal biosynthesis' rather than the generic 'Secondary metabolite biosynthesis' label. This is an item-specific database annotation fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Restricticin is simultaneously a secondary metabolite and an antifungal agent. Option D ('Secondary metabolite biosynthesis') is a valid broader description of the pathway this enzyme participates in. Option C ('Antifungal biosynthesis') is the specific UniProt pathway annotation. Without the database-specific classification, the sequence features of an enoyl reductase domain in a fungal PKS/NRPS cluster do not uniquely favor C over D. The question relies on the specific UniProt pathway label to disambiguate."
  },
  "important_caveats": [
    "The evidence code ECO:0000269 (direct assay) confirms experimental support for the antifungal annotation, but this experimental knowledge is not derivable from the sequence.",
    "The UniProt pathway taxonomy places this under 'Antifungal biosynthesis' rather than a generic 'Secondary metabolite biosynthesis' heading, which is a database-specific classification choice.",
    "Options A and B are clearly incorrect distractors (homoserine O-acetyltransferase reaction; ribosomal protein synthesis), so the effective discrimination is between C and D.",
    "The accession and pathway annotation were absent from the evaluated model input; the model sees only the 353-aa sequence and four choices."
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

**Accession:** `A0A0L1JEX1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 28. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEX1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.830871+00:00.  

```json
"A0A0L1JEX1"
```

Source SHA-256: `93c2ef537b4216da1fc60d3e1a5b3b72e3ab1e402adbf6bf0765a355bb253bef`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEX1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.830871+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 7"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"1.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Trans-enoyl reductase rstn7"}}}
```

Source SHA-256: `93c2ef537b4216da1fc60d3e1a5b3b72e3ab1e402adbf6bf0765a355bb253bef`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEX1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.830871+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"Antifungal biosynthesis"}]}
```

Source SHA-256: `93c2ef537b4216da1fc60d3e1a5b3b72e3ab1e402adbf6bf0765a355bb253bef`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEX1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.830871+00:00.  

```json
{"citation":{"authors":["Liu N.","Abramyan E.D.","Cheng W.","Perlatti B.","Harvey C.J.B.","Bills G.F.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33857369"},{"database":"DOI","id":"10.1021/jacs.1c01516"}],"citationType":"journal article","firstPage":"6043","id":"33857369","journal":"J. Am. Chem. Soc.","lastPage":"6047","publicationDate":"2021","title":"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.","volume":"143"},"referenceNumber":2,"referencePositions":["FUNCTION","PATHWAY"]}
```

Source SHA-256: `93c2ef537b4216da1fc60d3e1a5b3b72e3ab1e402adbf6bf0765a355bb253bef`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEX1?format=txt&versions=28)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:15.236581+00:00.  

```text
ID   RSTN7_ASPN3             Reviewed;         353 AA.
AC   A0A0L1JEX1;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-NOV-2015, sequence version 1.
DT   28-JAN-2026, entry version 28.
DE   RecName: Full=Trans-enoyl reductase rstn7 {ECO:0000303|PubMed:33857369};
DE            EC=1.-.-.- {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 7 {ECO:0000303|PubMed:33857369};
GN   Name=rstn7 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001446;
OS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /
OS   M93).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=1509407;
```

Source SHA-256: `b0c5088300010a6f92ba849941ad2568759c78d66be84ee67a93fca4e39f4e91`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEX1?format=txt&versions=28)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:15.236581+00:00.  

```text
RN   [2]
RP   FUNCTION, AND PATHWAY.
RX   PubMed=33857369; DOI=10.1021/jacs.1c01516;
RA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,
RA   Tang Y.;
RT   "Targeted genome mining reveals the biosynthetic gene clusters of natural
RT   product CYP51 inhibitors.";
RL   J. Am. Chem. Soc. 143:6043-6047(2021).
```

Source SHA-256: `b0c5088300010a6f92ba849941ad2568759c78d66be84ee67a93fca4e39f4e91`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEX1?format=txt&versions=28)  
**Locator:** `lines 47-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:15.236581+00:00.  

```text
CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000269|PubMed:33857369}.
```

Source SHA-256: `b0c5088300010a6f92ba849941ad2568759c78d66be84ee67a93fca4e39f4e91`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 197. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
