# pathway_0028

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEELTRSLVNDVEVLNNHFVSTGHPLPSFDRHTPTVVLPNDASPDAHAARERILDNALRLFQLAAGPSAYLLNLQTGYQYASCVRWLCHFQIFHLVPLEGSIAYADLAVLAKAPEPQLISVVRMAMTNGLFLESPPQHLAHSATSALLRNDADFHDWAVTMSDLSFPTAFAMVEAHERWPNSVEGNQTAYNIAVGSELPFFSHLAEQSDRKRQFAGFMRSMARSQGTDVEKLAEGWDWAALGQACVVDVGGSTGHTSVALARKYPDLNFVVEDLPEVVAEGPGYLSYLDDAQDLKSRIGYRAHSFFDPQPVQDADVYMLRMILHNWSFDDCVRILSRLVQTLKPGARIIIVDIVLPDPGVVSASKERLLRVQDLIMQQVFNSMERYLENWMDIFRKVDERLEVKRIVEPPGSLMSLIELSMAA

[Multiple Choices]
A. Polyketide biosynthesis. .
B. Antibiotic biosynthesis. .
C. Secondary metabolite biosynthesis. .
D. One-carbon metabolism
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

> The exact sequence matches the UniProt entry for O-methyltransferase aoiF, whose pathway annotation is “Secondary metabolite biosynthesis.” That annotation cites experimental evidence, although the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may be compatible with an enzyme such as an O-methyltransferase, but enzyme family or catalytic activity alone does not identify the particular biosynthetic pathway it serves.


**Missing item-specific fact**

> The protein-specific association of AoiF with secondary-metabolite biosynthesis, supported by its annotation and cited study, is absent from the input.


**Reason**

> Choosing the annotated pathway requires a protein-specific functional association not established by the sequence and choices alone; recognizing the exact sequence or using a predictor would not make this reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The cited study describes production of a novel polyketide, making polyketide biosynthesis a defensible narrower description, while the protein annotation uses the broader secondary-metabolite-biosynthesis category. The options therefore overlap.


### Important caveats

- The sequence match is exact, but reviewer-only accession and annotation information was not supplied to the evaluated model.
- The UniProt pathway annotation cites experimental evidence; the cited primary paper was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may be compatible with an enzyme such as an O-methyltransferase, but enzyme family or catalytic activity alone does not identify the particular biosynthetic pathway it serves.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific association of AoiF with secondary-metabolite biosynthesis, supported by its annotation and cited study, is absent from the input.",
    "reason": "Choosing the annotated pathway requires a protein-specific functional association not established by the sequence and choices alone; recognizing the exact sequence or using a predictor would not make this reasoning-supported."
  },
  "case_id": "pathway_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for O-methyltransferase aoiF, whose pathway annotation is “Secondary metabolite biosynthesis.” That annotation cites experimental evidence, although the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact, but reviewer-only accession and annotation information was not supplied to the evaluated model.",
    "The UniProt pathway annotation cites experimental evidence; the cited primary paper was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The cited study describes production of a novel polyketide, making polyketide biosynthesis a defensible narrower description, while the protein annotation uses the broader secondary-metabolite-biosynthesis category. The options therefore overlap."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for O-methyltransferase aoiF, whose pathway annotation is “Secondary metabolite biosynthesis.” That annotation cites experimental evidence, although the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may be compatible with an enzyme such as an O-methyltransferase, but enzyme family or catalytic activity alone does not identify the particular biosynthetic pathway it serves.",
    "missing_item_specific_fact": "The protein-specific association of AoiF with secondary-metabolite biosynthesis, supported by its annotation and cited study, is absent from the input.",
    "reason": "Choosing the annotated pathway requires a protein-specific functional association not established by the sequence and choices alone; recognizing the exact sequence or using a predictor would not make this reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The cited study describes production of a novel polyketide, making polyketide biosynthesis a defensible narrower description, while the protein annotation uses the broader secondary-metabolite-biosynthesis category. The options therefore overlap."
  },
  "important_caveats": [
    "The sequence match is exact, but reviewer-only accession and annotation information was not supplied to the evaluated model.",
    "The UniProt pathway annotation cites experimental evidence; the cited primary paper was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q2TXQ9 (O-methyltransferase aoiF, Aspergillus oryzae) carries an experimental PATHWAY annotation (ECO:0000269|PubMed:22447538) stating 'Secondary metabolite biosynthesis,' which exactly matches choice C. The underlying paper (Nakazawa et al. 2012) characterizes the enzyme's role in a silent biosynthetic gene cluster producing a novel polyketide, confirming its involvement in secondary metabolism. Choice D (one-carbon metabolism) is clearly wrong as this is an SAM-dependent O-methyltransferase, not a folate-cycle enzyme. Choice B (antibiotic biosynthesis) is not supported—the paper describes a polyketide but does not classify it as an antibiotic. However, choice A (polyketide biosynthesis) is also arguably correct since the paper explicitly describes a polyketide pathway, and polyketide biosynthesis is a subtype of secondary metabolite biosynthesis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> From the sequence alone, a knowledgeable model could identify conserved motifs of an SAM-dependent methyltransferase and rule out one-carbon metabolism (D), which relies on folate-dependent one-carbon transfer enzymes with entirely different folds. However, O-methyltransferases are ubiquitous across many biosynthetic pathways, and the sequence lacks polyketide synthase domains (KS, AT, ACP) that would signal polyketide-specific function. The organism identity (Aspergillus oryzae) is not derivable from the sequence, so even narrowing to fungal secondary metabolism requires external knowledge. The critical distinction between 'polyketide biosynthesis' (A) and the broader 'secondary metabolite biosynthesis' (C) depends on knowing which gene cluster this methyltransferase belongs to or recalling the specific UniProt PATHWAY annotation.


**Missing item-specific fact**

> The specific biosynthetic gene cluster context (that aoiF belongs to a polyketide gene cluster in A. oryzae) and the exact UniProt PATHWAY annotation wording ('Secondary metabolite biosynthesis' rather than 'Polyketide biosynthesis') are required to select C over A. Neither is inferable from the 423-amino-acid sequence alone.


**Reason**

> The sequence identifies a methyltransferase but provides no substrate specificity, gene-cluster membership, or organism context. Distinguishing C from A requires knowing the specific annotation or the experimental paper's pathway classification, which is an item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The reference paper (PubMed:22447538) explicitly describes the pathway as producing 'a novel polyketide,' making choice A (Polyketide biosynthesis) a defensible answer. The UniProt annotation uses the broader term 'Secondary metabolite biosynthesis' (C), which encompasses polyketide biosynthesis. Since polyketide biosynthesis is a well-recognized subtype of secondary metabolite biosynthesis, both A and C are scientifically accurate descriptions of the pathway. The question's phrasing 'primary metabolic or signaling pathway' does not clearly indicate whether the broader or narrower classification is preferred, leaving both A and C defensible.


### Important caveats

- The UniProt PATHWAY annotation (C) is backed by experimental evidence (ECO:0000269), but the underlying paper's title and content emphasize polyketide biosynthesis, creating genuine overlap between choices A and C.
- The sequence-match is confirmed (SHA-256 match between benchmark sequence and UniProt Q2TXQ9), so the annotation applies to the exact sequence presented.
- The entry was first publicly released in Swiss-Prot on 2025-04-09; depending on the author's data-construction date, this annotation may or may not have been available at benchmark creation.
- Choice B (antibiotic biosynthesis) is not supported by the evidence; the polyketide product is not described as an antibiotic.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "From the sequence alone, a knowledgeable model could identify conserved motifs of an SAM-dependent methyltransferase and rule out one-carbon metabolism (D), which relies on folate-dependent one-carbon transfer enzymes with entirely different folds. However, O-methyltransferases are ubiquitous across many biosynthetic pathways, and the sequence lacks polyketide synthase domains (KS, AT, ACP) that would signal polyketide-specific function. The organism identity (Aspergillus oryzae) is not derivable from the sequence, so even narrowing to fungal secondary metabolism requires external knowledge. The critical distinction between 'polyketide biosynthesis' (A) and the broader 'secondary metabolite biosynthesis' (C) depends on knowing which gene cluster this methyltransferase belongs to or recalling the specific UniProt PATHWAY annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific biosynthetic gene cluster context (that aoiF belongs to a polyketide gene cluster in A. oryzae) and the exact UniProt PATHWAY annotation wording ('Secondary metabolite biosynthesis' rather than 'Polyketide biosynthesis') are required to select C over A. Neither is inferable from the 423-amino-acid sequence alone.",
    "reason": "The sequence identifies a methyltransferase but provides no substrate specificity, gene-cluster membership, or organism context. Distinguishing C from A requires knowing the specific annotation or the experimental paper's pathway classification, which is an item-specific lookup."
  },
  "case_id": "pathway_0028",
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
    "reason": "The UniProt entry Q2TXQ9 (O-methyltransferase aoiF, Aspergillus oryzae) carries an experimental PATHWAY annotation (ECO:0000269|PubMed:22447538) stating 'Secondary metabolite biosynthesis,' which exactly matches choice C. The underlying paper (Nakazawa et al. 2012) characterizes the enzyme's role in a silent biosynthetic gene cluster producing a novel polyketide, confirming its involvement in secondary metabolism. Choice D (one-carbon metabolism) is clearly wrong as this is an SAM-dependent O-methyltransferase, not a folate-cycle enzyme. Choice B (antibiotic biosynthesis) is not supported—the paper describes a polyketide but does not classify it as an antibiotic. However, choice A (polyketide biosynthesis) is also arguably correct since the paper explicitly describes a polyketide pathway, and polyketide biosynthesis is a subtype of secondary metabolite biosynthesis."
  },
  "important_caveats": [
    "The UniProt PATHWAY annotation (C) is backed by experimental evidence (ECO:0000269), but the underlying paper's title and content emphasize polyketide biosynthesis, creating genuine overlap between choices A and C.",
    "The sequence-match is confirmed (SHA-256 match between benchmark sequence and UniProt Q2TXQ9), so the annotation applies to the exact sequence presented.",
    "The entry was first publicly released in Swiss-Prot on 2025-04-09; depending on the author's data-construction date, this annotation may or may not have been available at benchmark creation.",
    "Choice B (antibiotic biosynthesis) is not supported by the evidence; the polyketide product is not described as an antibiotic."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The reference paper (PubMed:22447538) explicitly describes the pathway as producing 'a novel polyketide,' making choice A (Polyketide biosynthesis) a defensible answer. The UniProt annotation uses the broader term 'Secondary metabolite biosynthesis' (C), which encompasses polyketide biosynthesis. Since polyketide biosynthesis is a well-recognized subtype of secondary metabolite biosynthesis, both A and C are scientifically accurate descriptions of the pathway. The question's phrasing 'primary metabolic or signaling pathway' does not clearly indicate whether the broader or narrower classification is preferred, leaving both A and C defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q2TXQ9 (O-methyltransferase aoiF, Aspergillus oryzae) carries an experimental PATHWAY annotation (ECO:0000269|PubMed:22447538) stating 'Secondary metabolite biosynthesis,' which exactly matches choice C. The underlying paper (Nakazawa et al. 2012) characterizes the enzyme's role in a silent biosynthetic gene cluster producing a novel polyketide, confirming its involvement in secondary metabolism. Choice D (one-carbon metabolism) is clearly wrong as this is an SAM-dependent O-methyltransferase, not a folate-cycle enzyme. Choice B (antibiotic biosynthesis) is not supported—the paper describes a polyketide but does not classify it as an antibiotic. However, choice A (polyketide biosynthesis) is also arguably correct since the paper explicitly describes a polyketide pathway, and polyketide biosynthesis is a subtype of secondary metabolite biosynthesis.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "From the sequence alone, a knowledgeable model could identify conserved motifs of an SAM-dependent methyltransferase and rule out one-carbon metabolism (D), which relies on folate-dependent one-carbon transfer enzymes with entirely different folds. However, O-methyltransferases are ubiquitous across many biosynthetic pathways, and the sequence lacks polyketide synthase domains (KS, AT, ACP) that would signal polyketide-specific function. The organism identity (Aspergillus oryzae) is not derivable from the sequence, so even narrowing to fungal secondary metabolism requires external knowledge. The critical distinction between 'polyketide biosynthesis' (A) and the broader 'secondary metabolite biosynthesis' (C) depends on knowing which gene cluster this methyltransferase belongs to or recalling the specific UniProt PATHWAY annotation.",
    "missing_item_specific_fact": "The specific biosynthetic gene cluster context (that aoiF belongs to a polyketide gene cluster in A. oryzae) and the exact UniProt PATHWAY annotation wording ('Secondary metabolite biosynthesis' rather than 'Polyketide biosynthesis') are required to select C over A. Neither is inferable from the 423-amino-acid sequence alone.",
    "reason": "The sequence identifies a methyltransferase but provides no substrate specificity, gene-cluster membership, or organism context. Distinguishing C from A requires knowing the specific annotation or the experimental paper's pathway classification, which is an item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The reference paper (PubMed:22447538) explicitly describes the pathway as producing 'a novel polyketide,' making choice A (Polyketide biosynthesis) a defensible answer. The UniProt annotation uses the broader term 'Secondary metabolite biosynthesis' (C), which encompasses polyketide biosynthesis. Since polyketide biosynthesis is a well-recognized subtype of secondary metabolite biosynthesis, both A and C are scientifically accurate descriptions of the pathway. The question's phrasing 'primary metabolic or signaling pathway' does not clearly indicate whether the broader or narrower classification is preferred, leaving both A and C defensible."
  },
  "important_caveats": [
    "The UniProt PATHWAY annotation (C) is backed by experimental evidence (ECO:0000269), but the underlying paper's title and content emphasize polyketide biosynthesis, creating genuine overlap between choices A and C.",
    "The sequence-match is confirmed (SHA-256 match between benchmark sequence and UniProt Q2TXQ9), so the annotation applies to the exact sequence presented.",
    "The entry was first publicly released in Swiss-Prot on 2025-04-09; depending on the author's data-construction date, this annotation may or may not have been available at benchmark creation.",
    "Choice B (antibiotic biosynthesis) is not supported by the evidence; the polyketide product is not described as an antibiotic."
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

**Accession:** `Q2TXQ9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 88. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.757390+00:00.  

```json
"Q2TXQ9"
```

Source SHA-256: `c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.757390+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22447538","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22447538","source":"PubMed"}],"value":"O-methyltransferase aoiF"}}}
```

Source SHA-256: `c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.757390+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22447538","source":"PubMed"}],"value":"Secondary metabolite biosynthesis"}]}
```

Source SHA-256: `c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.757390+00:00.  

```json
{"citation":{"authors":["Nakazawa T.","Ishiuchi K.","Praseuth A.","Noguchi H.","Hotta K.","Watanabe K."],"citationCrossReferences":[{"database":"PubMed","id":"22447538"},{"database":"DOI","id":"10.1002/cbic.201200107"}],"citationType":"journal article","firstPage":"855","id":"22447538","journal":"ChemBioChem","lastPage":"861","publicationDate":"2012","title":"Overexpressing transcriptional regulator in Aspergillus oryzae activates a silent biosynthetic pathway to produce a novel polyketide.","volume":"13"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","INDUCTION"]}
```

Source SHA-256: `c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 88 / 1.  
**Retrieved:** 2026-11-01T06:28:32.769835+00:00.  

```text
ID   AOIF_ASPOR              Reviewed;         423 AA.
AC   Q2TXQ9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   24-JAN-2006, sequence version 1.
DT   28-JAN-2026, entry version 88.
DE   RecName: Full=O-methyltransferase aoiF {ECO:0000303|PubMed:22447538};
DE            EC=2.1.1.- {ECO:0000269|PubMed:22447538};
GN   Name=aoiF {ECO:0000303|PubMed:22447538}; ORFNames=AO090010000047;
OS   Aspergillus oryzae (strain ATCC 42149 / RIB 40) (Yellow koji mold).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=510516;
```

Source SHA-256: `6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)  
**Locator:** `lines 32-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 88 / 1.  
**Retrieved:** 2026-11-01T06:28:32.769835+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND INDUCTION.
RX   PubMed=22447538; DOI=10.1002/cbic.201200107;
RA   Nakazawa T., Ishiuchi K., Praseuth A., Noguchi H., Hotta K., Watanabe K.;
RT   "Overexpressing transcriptional regulator in Aspergillus oryzae activates a
RT   silent biosynthetic pathway to produce a novel polyketide.";
RL   ChemBioChem 13:855-861(2012).
```

Source SHA-256: `6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)  
**Locator:** `lines 50-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 88 / 1.  
**Retrieved:** 2026-11-01T06:28:32.769835+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis.
CC       {ECO:0000269|PubMed:22447538}.
```

Source SHA-256: `6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
