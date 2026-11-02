# pathway_0178

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSASTPTAPYLEDLVRNSLDQNLPWVVQKYGGTSVGKSLDNITKIVGSYIDNGSKVAIVCSARSTQTKSLGTTNLLLQASREALQPAMSSSGDGRSGSMSGTATPFYPKRVGSGFFGKDQSTSMTSSVSSLSQLESQLGRSGSPSPFQSSSSRSPPRSPATPSQDSSISQEPAFHATVDLIKKGHLEAARASLKGGPLRDELEEEIERDCESLRSFLYAAQIIDEISPRSQDSIVGTGERLACKIVAAALRDRGVDSELVVLDNIVDASMSAASEAVSVDAGDQGVAQLGQEFYDQLSFRLGERLRECGQRVPVVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLKASELQVWKEVDGIFTADPRKVPSARLVPIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCLSYPRSPATEMAGLQLQ

[Multiple Choices]
A. IMP biosynthesis via de novo pathway
B. spheroidene biosynthesis. .
C. oxylipin biosynthesis. .
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

> The exact supplied sequence matches a UniProt entry annotated as aspartokinase, with amino-acid biosynthesis pathways listed. The pathway annotations cite experimental evidence, although the cited paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clear general biological argument identifying which pathway this protein serves among the choices. Recognizing it as a particular enzyme would require protein-specific identification or homology information.


**Missing item-specific fact**

> The absent fact is that this sequence is an aspartokinase (HOM3), functioning in amino-acid biosynthesis.


**Reason**

> The key is supported by the sequence-matched annotation, but that annotation and the protein-specific functional identification are not supplied in the question. Generic sequence inspection does not meaningfully distinguish the pathway choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports amino-acid biosynthesis; no other listed pathway is indicated for this protein.


### Important caveats

- The cited pathway annotation carries an experimental-evidence code, but the underlying primary study was not independently validated here.
- The reviewer-only accession and annotation were absent from the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a clear general biological argument identifying which pathway this protein serves among the choices. Recognizing it as a particular enzyme would require protein-specific identification or homology information.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The absent fact is that this sequence is an aspartokinase (HOM3), functioning in amino-acid biosynthesis.",
    "reason": "The key is supported by the sequence-matched annotation, but that annotation and the protein-specific functional identification are not supplied in the question. Generic sequence inspection does not meaningfully distinguish the pathway choices."
  },
  "case_id": "pathway_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a UniProt entry annotated as aspartokinase, with amino-acid biosynthesis pathways listed. The pathway annotations cite experimental evidence, although the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The cited pathway annotation carries an experimental-evidence code, but the underlying primary study was not independently validated here.",
    "The reviewer-only accession and annotation were absent from the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports amino-acid biosynthesis; no other listed pathway is indicated for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a UniProt entry annotated as aspartokinase, with amino-acid biosynthesis pathways listed. The pathway annotations cite experimental evidence, although the cited paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clear general biological argument identifying which pathway this protein serves among the choices. Recognizing it as a particular enzyme would require protein-specific identification or homology information.",
    "missing_item_specific_fact": "The absent fact is that this sequence is an aspartokinase (HOM3), functioning in amino-acid biosynthesis.",
    "reason": "The key is supported by the sequence-matched annotation, but that annotation and the protein-specific functional identification are not supplied in the question. Generic sequence inspection does not meaningfully distinguish the pathway choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports amino-acid biosynthesis; no other listed pathway is indicated for this protein."
  },
  "important_caveats": [
    "The cited pathway annotation carries an experimental-evidence code, but the underlying primary study was not independently validated here.",
    "The reviewer-only accession and annotation were absent from the evaluated model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9VS37 (sequence matched exactly, 615 aa) identifies this protein as Aspartokinase (EC 2.7.2.4, gene HOM3). Two pathway annotations, both with ECO:0000269 (direct assay) evidence from PubMed:18757810, state: 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 1/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 1/5.' The expected answer 'Amino-acid biosynthesis' directly matches the annotated pathway category.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable amino acid kinase (PF00696) catalytic domain motif ('GGTSVGKSLDNITKIVGSYIDNGSKVAIVC') and a C-terminal ACT/regulatory domain pattern ('PIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCL'). The amino acid kinase superfamily is involved exclusively in amino acid biosynthesis pathways (aspartokinase, homoserine kinase, threonine kinase, etc.). This distinguishes the protein from IMP biosynthesis enzymes (purine biosynthesis enzymes are not amino acid kinases), spheroidene biosynthesis (carotenoid desaturases/cyclases), and oxylipin biosynthesis (lipoxygenases). Recognizing the amino acid kinase domain family from its conserved motif and connecting it to amino acid biosynthesis is a legitimate reasoning task based on general protein domain biology.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The amino acid kinase catalytic motif is sufficiently distinctive from protein kinase, lipid kinase, and other enzyme families to allow reasoning from sequence to the amino acid biosynthesis pathway. The regulatory ACT domain further supports an amino acid biosynthetic enzyme. None of the other three options (IMP biosynthesis, spheroidene biosynthesis, oxylipin biosynthesis) involve amino acid kinases. This is a domain-family recognition task rather than memorization of a single protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct metabolic pathway classes. The amino acid kinase domain pattern is incompatible with IMP biosynthesis (purine enzymes), spheroidene biosynthesis (carotenoid enzymes), and oxylipin biosynthesis (lipoxygenases). Only option D is consistent with the identified enzyme family.


### Important caveats

- The pathway annotation is supported by direct assay evidence (ECO:0000269) from a 2008 study on Cryptococcus neoformans threonine biosynthetic genes, not solely by computational transfer.
- The EC number assignment (2.7.2.4) carries ECO:0000250 (similarity to P10869), but the pathway assignment itself is based on direct experimental evidence.
- The sequence is from a fungal organism (Cryptococcus neoformans); the reasoning about amino acid kinase domain recognition applies across kingdoms.
- The reviewer-only accession and annotation were not available to the evaluated model; the reasoning argument relies solely on the provided sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable amino acid kinase (PF00696) catalytic domain motif ('GGTSVGKSLDNITKIVGSYIDNGSKVAIVC') and a C-terminal ACT/regulatory domain pattern ('PIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCL'). The amino acid kinase superfamily is involved exclusively in amino acid biosynthesis pathways (aspartokinase, homoserine kinase, threonine kinase, etc.). This distinguishes the protein from IMP biosynthesis enzymes (purine biosynthesis enzymes are not amino acid kinases), spheroidene biosynthesis (carotenoid desaturases/cyclases), and oxylipin biosynthesis (lipoxygenases). Recognizing the amino acid kinase domain family from its conserved motif and connecting it to amino acid biosynthesis is a legitimate reasoning task based on general protein domain biology.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The amino acid kinase catalytic motif is sufficiently distinctive from protein kinase, lipid kinase, and other enzyme families to allow reasoning from sequence to the amino acid biosynthesis pathway. The regulatory ACT domain further supports an amino acid biosynthetic enzyme. None of the other three options (IMP biosynthesis, spheroidene biosynthesis, oxylipin biosynthesis) involve amino acid kinases. This is a domain-family recognition task rather than memorization of a single protein's annotation."
  },
  "case_id": "pathway_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry J9VS37 (sequence matched exactly, 615 aa) identifies this protein as Aspartokinase (EC 2.7.2.4, gene HOM3). Two pathway annotations, both with ECO:0000269 (direct assay) evidence from PubMed:18757810, state: 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 1/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 1/5.' The expected answer 'Amino-acid biosynthesis' directly matches the annotated pathway category."
  },
  "important_caveats": [
    "The pathway annotation is supported by direct assay evidence (ECO:0000269) from a 2008 study on Cryptococcus neoformans threonine biosynthetic genes, not solely by computational transfer.",
    "The EC number assignment (2.7.2.4) carries ECO:0000250 (similarity to P10869), but the pathway assignment itself is based on direct experimental evidence.",
    "The sequence is from a fungal organism (Cryptococcus neoformans); the reasoning about amino acid kinase domain recognition applies across kingdoms.",
    "The reviewer-only accession and annotation were not available to the evaluated model; the reasoning argument relies solely on the provided sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct metabolic pathway classes. The amino acid kinase domain pattern is incompatible with IMP biosynthesis (purine enzymes), spheroidene biosynthesis (carotenoid enzymes), and oxylipin biosynthesis (lipoxygenases). Only option D is consistent with the identified enzyme family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9VS37 (sequence matched exactly, 615 aa) identifies this protein as Aspartokinase (EC 2.7.2.4, gene HOM3). Two pathway annotations, both with ECO:0000269 (direct assay) evidence from PubMed:18757810, state: 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 1/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 1/5.' The expected answer 'Amino-acid biosynthesis' directly matches the annotated pathway category.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable amino acid kinase (PF00696) catalytic domain motif ('GGTSVGKSLDNITKIVGSYIDNGSKVAIVC') and a C-terminal ACT/regulatory domain pattern ('PIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCL'). The amino acid kinase superfamily is involved exclusively in amino acid biosynthesis pathways (aspartokinase, homoserine kinase, threonine kinase, etc.). This distinguishes the protein from IMP biosynthesis enzymes (purine biosynthesis enzymes are not amino acid kinases), spheroidene biosynthesis (carotenoid desaturases/cyclases), and oxylipin biosynthesis (lipoxygenases). Recognizing the amino acid kinase domain family from its conserved motif and connecting it to amino acid biosynthesis is a legitimate reasoning task based on general protein domain biology.",
    "missing_item_specific_fact": "",
    "reason": "The amino acid kinase catalytic motif is sufficiently distinctive from protein kinase, lipid kinase, and other enzyme families to allow reasoning from sequence to the amino acid biosynthesis pathway. The regulatory ACT domain further supports an amino acid biosynthetic enzyme. None of the other three options (IMP biosynthesis, spheroidene biosynthesis, oxylipin biosynthesis) involve amino acid kinases. This is a domain-family recognition task rather than memorization of a single protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct metabolic pathway classes. The amino acid kinase domain pattern is incompatible with IMP biosynthesis (purine enzymes), spheroidene biosynthesis (carotenoid enzymes), and oxylipin biosynthesis (lipoxygenases). Only option D is consistent with the identified enzyme family."
  },
  "important_caveats": [
    "The pathway annotation is supported by direct assay evidence (ECO:0000269) from a 2008 study on Cryptococcus neoformans threonine biosynthetic genes, not solely by computational transfer.",
    "The EC number assignment (2.7.2.4) carries ECO:0000250 (similarity to P10869), but the pathway assignment itself is based on direct experimental evidence.",
    "The sequence is from a fungal organism (Cryptococcus neoformans); the reasoning about amino acid kinase domain recognition applies across kingdoms.",
    "The reviewer-only accession and annotation were not available to the evaluated model; the reasoning argument relies solely on the provided sequence."
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

**Accession:** `J9VS37` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 66. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"2.7.2.4"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartokinase"}}}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18757810","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 1/3"}]}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18757810","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 1/5"}]}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"citation":{"authors":["Kingsbury J.M.","McCusker J.H."],"citationCrossReferences":[{"database":"PubMed","id":"18757810"},{"database":"DOI","id":"10.1099/mic.0.2008/019729-0"}],"citationType":"journal article","firstPage":"2767","id":"18757810","journal":"Microbiology","lastPage":"2775","publicationDate":"2008","title":"Threonine biosynthetic genes are essential in Cryptococcus neoformans.","volume":"154"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
ID   AK_CRYN9                Reviewed;         615 AA.
AC   J9VS37;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-NOV-2012, sequence version 1.
DT   28-JAN-2026, entry version 66.
DE   RecName: Full=Aspartokinase {ECO:0000305};
DE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};
GN   Name=HOM3 {ECO:0000303|PubMed:18757810};
GN   ORFNames=CNAG_04347 {ECO:0000312|EMBL:AFR97078.1};
OS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)
OS   (Cryptococcus neoformans var. grubii serotype A).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 35-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.
RX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;
RA   Kingsbury J.M., McCusker J.H.;
RT   "Threonine biosynthetic genes are essential in Cryptococcus neoformans.";
RL   Microbiology 154:2767-2775(2008).
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 52-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo
CC       pathway; L-homoserine from L-aspartate: step 1/3.
CC       {ECO:0000269|PubMed:18757810}.
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 55-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine
CC       from L-aspartate: step 1/5. {ECO:0000269|PubMed:18757810}.
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 178. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
