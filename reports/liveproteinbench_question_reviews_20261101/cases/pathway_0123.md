# pathway_0123

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELFFICGLVLFSTLSLISLFLLHNHSSARGYRLPPGRMGWPFIGESYEFLANGWKGYPEKFIFSRLAKYKPNQVFKTSILGEKVAVMCGATCNKFLFSNEGKLVNAWWPNSVNKIFPSSTQTSSKEEAKKMRKLLPTFFKPEALQRYIPIMDEIAIRHMEDEWEGKSKIEVFPLAKRYTFWLACRLFLSIDDPVHVAKFADPFNDIASGIISIPIDLPGTPFNRGIKASNVVRQELKTIIKQRKLDLSDNKASPTQDILSHMLLTPDEDGRYMNELDIADKILGLLIGGHDTASAACTFVVKFLAELPHIYDGVYKEQMEIAKSKKEGERLNWEDIQKMKYSWNVACEVMRLAPPLQGAFREALSDFMYAGFQIPKGWKLYWSANSTHRNPECFPEPEKFDPARFDGSGPAPYTYVPFGGGPRMCPGKEYARLEILVFMHNIVKRFKWEKLIPDETIVVNPMPTPAKGLPVRLRPHSKPVTVSA

[Multiple Choices]
A. L-threonine from L-aspartate: step 4/5. .
B. NAD(+) from nicotinamide D-ribonucleotide: step 1/1. .
C. chorismate biosynthesis
D. Secondary metabolite biosynthesis
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

> The exact sequence matches the UniProt record annotated as beta-amyrin 28-monooxygenase, with a pathway annotation of secondary metabolite and terpenoid biosynthesis. The pathway annotation cites ECO:0000269 evidence linked to a publication; this supports the key, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and sequence features are compatible with a membrane-associated cytochrome P450, which makes an oxidative metabolic role plausible. They do not establish this protein's particular substrate or pathway, and P450s participate in many different pathways.


**Missing item-specific fact**

> The protein-specific identification as beta-amyrin 28-monooxygenase and its experimentally linked role in terpenoid secondary-metabolite biosynthesis.


**Reason**

> The supplied sequence alone does not meaningfully distinguish the specific pathway choice from other possible roles of a plant P450. Selecting D requires the protein-specific functional annotation or equivalent external evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports D; the other choices describe distinct primary metabolic pathways and are not supported for this protein by the supplied sequence.


### Important caveats

- Reviewer-only accession and database evidence were not supplied to the evaluated model.
- The pathway annotation is database evidence citing a publication; the underlying primary study was not independently examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and sequence features are compatible with a membrane-associated cytochrome P450, which makes an oxidative metabolic role plausible. They do not establish this protein's particular substrate or pathway, and P450s participate in many different pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as beta-amyrin 28-monooxygenase and its experimentally linked role in terpenoid secondary-metabolite biosynthesis.",
    "reason": "The supplied sequence alone does not meaningfully distinguish the specific pathway choice from other possible roles of a plant P450. Selecting D requires the protein-specific functional annotation or equivalent external evidence."
  },
  "case_id": "pathway_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record annotated as beta-amyrin 28-monooxygenase, with a pathway annotation of secondary metabolite and terpenoid biosynthesis. The pathway annotation cites ECO:0000269 evidence linked to a publication; this supports the key, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only accession and database evidence were not supplied to the evaluated model.",
    "The pathway annotation is database evidence citing a publication; the underlying primary study was not independently examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D; the other choices describe distinct primary metabolic pathways and are not supported for this protein by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record annotated as beta-amyrin 28-monooxygenase, with a pathway annotation of secondary metabolite and terpenoid biosynthesis. The pathway annotation cites ECO:0000269 evidence linked to a publication; this supports the key, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and sequence features are compatible with a membrane-associated cytochrome P450, which makes an oxidative metabolic role plausible. They do not establish this protein's particular substrate or pathway, and P450s participate in many different pathways.",
    "missing_item_specific_fact": "The protein-specific identification as beta-amyrin 28-monooxygenase and its experimentally linked role in terpenoid secondary-metabolite biosynthesis.",
    "reason": "The supplied sequence alone does not meaningfully distinguish the specific pathway choice from other possible roles of a plant P450. Selecting D requires the protein-specific functional annotation or equivalent external evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D; the other choices describe distinct primary metabolic pathways and are not supported for this protein by the supplied sequence."
  },
  "important_caveats": [
    "Reviewer-only accession and database evidence were not supplied to the evaluated model.",
    "The pathway annotation is database evidence citing a publication; the underlying primary study was not independently examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAW1NEA3 explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is Beta-amyrin 28-monooxygenase CYP716A378 (EC 1.14.14.126), a cytochrome P450 catalyzing a step in saponin (triterpenoid) biosynthesis in Saponaria officinalis. The expected answer D 'Secondary metabolite biosynthesis' matches the UniProt PATHWAY annotation exactly.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif FxxGxRxCxG (visible as 'FGGGPRMCPG' near the C-terminus) plus the conserved KFK/FKW region, identifying it as a P450. Among the four options, A (threonine synthase, a PLP-dependent enzyme), B (NAD synthetase, an adenylyltransferase), and C (shikimate-pathway enzymes such as DAHP synthase and DHQ synthase) all describe primary metabolic enzymes that are NOT cytochrome P450s. Option D (secondary metabolite biosynthesis) is the only pathway among the choices that characteristically employs cytochrome P450 monooxygenases in plants (terpenoid, phenylpropanoid, and alkaloid pathways). Thus, identifying the P450 fold from the sequence and recognizing that the other three options involve non-P450 primary-metabolic enzymes provides a concrete biological argument to select D.


**Missing item-specific fact**

> None strictly required. Precise family assignment (CYP716 → triterpenoid-specific) would strengthen the answer, but the broader P450-vs-non-P450 logic already eliminates A, B, and C.


**Reason**

> The heme-binding signature is extractable from the raw sequence, and the biological fact that plant P450s are hallmarks of secondary metabolism while threonine synthase, NAD synthetase, and shikimate-pathway enzymes are not P450s constitutes a general-knowledge reasoning chain that distinguishes D from the distractors without needing to memorize this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe pathways whose enzymatic steps are well-characterized non-P450 enzymes (PLP-dependent, adenylyltransferase, and shikimate-pathway enzymes respectively). Only D is compatible with a cytochrome P450. No other option is defensible once the P450 identity is recognized.


### Important caveats

- The UniProt annotation is experimental (ECO:0000269) based on a 2025 Nat. Chem. Biol. paper; the pathway assignment is well-supported.
- The organism name (Saponaria officinalis, soapwort) is not provided in the model input, so reasoning must rely on sequence-derived features (P450 motif, signal peptide, ER-targeting) rather than organism context.
- While the CYP716 family is triterpenoid-specific, the broader P450→secondary-metabolism logic suffices to eliminate the three primary-metabolism distractors without family-level precision.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning argument stands independently on sequence features and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif FxxGxRxCxG (visible as 'FGGGPRMCPG' near the C-terminus) plus the conserved KFK/FKW region, identifying it as a P450. Among the four options, A (threonine synthase, a PLP-dependent enzyme), B (NAD synthetase, an adenylyltransferase), and C (shikimate-pathway enzymes such as DAHP synthase and DHQ synthase) all describe primary metabolic enzymes that are NOT cytochrome P450s. Option D (secondary metabolite biosynthesis) is the only pathway among the choices that characteristically employs cytochrome P450 monooxygenases in plants (terpenoid, phenylpropanoid, and alkaloid pathways). Thus, identifying the P450 fold from the sequence and recognizing that the other three options involve non-P450 primary-metabolic enzymes provides a concrete biological argument to select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Precise family assignment (CYP716 → triterpenoid-specific) would strengthen the answer, but the broader P450-vs-non-P450 logic already eliminates A, B, and C.",
    "reason": "The heme-binding signature is extractable from the raw sequence, and the biological fact that plant P450s are hallmarks of secondary metabolism while threonine synthase, NAD synthetase, and shikimate-pathway enzymes are not P450s constitutes a general-knowledge reasoning chain that distinguishes D from the distractors without needing to memorize this specific UniProt entry."
  },
  "case_id": "pathway_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C6",
      "H3",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1NEA3 explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is Beta-amyrin 28-monooxygenase CYP716A378 (EC 1.14.14.126), a cytochrome P450 catalyzing a step in saponin (triterpenoid) biosynthesis in Saponaria officinalis. The expected answer D 'Secondary metabolite biosynthesis' matches the UniProt PATHWAY annotation exactly."
  },
  "important_caveats": [
    "The UniProt annotation is experimental (ECO:0000269) based on a 2025 Nat. Chem. Biol. paper; the pathway assignment is well-supported.",
    "The organism name (Saponaria officinalis, soapwort) is not provided in the model input, so reasoning must rely on sequence-derived features (P450 motif, signal peptide, ER-targeting) rather than organism context.",
    "While the CYP716 family is triterpenoid-specific, the broader P450→secondary-metabolism logic suffices to eliminate the three primary-metabolism distractors without family-level precision.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning argument stands independently on sequence features and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe pathways whose enzymatic steps are well-characterized non-P450 enzymes (PLP-dependent, adenylyltransferase, and shikimate-pathway enzymes respectively). Only D is compatible with a cytochrome P450. No other option is defensible once the P450 identity is recognized."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1NEA3 explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is Beta-amyrin 28-monooxygenase CYP716A378 (EC 1.14.14.126), a cytochrome P450 catalyzing a step in saponin (triterpenoid) biosynthesis in Saponaria officinalis. The expected answer D 'Secondary metabolite biosynthesis' matches the UniProt PATHWAY annotation exactly.",
    "evidence_ids": ["C5", "C4", "C6", "H3", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif FxxGxRxCxG (visible as 'FGGGPRMCPG' near the C-terminus) plus the conserved KFK/FKW region, identifying it as a P450. Among the four options, A (threonine synthase, a PLP-dependent enzyme), B (NAD synthetase, an adenylyltransferase), and C (shikimate-pathway enzymes such as DAHP synthase and DHQ synthase) all describe primary metabolic enzymes that are NOT cytochrome P450s. Option D (secondary metabolite biosynthesis) is the only pathway among the choices that characteristically employs cytochrome P450 monooxygenases in plants (terpenoid, phenylpropanoid, and alkaloid pathways). Thus, identifying the P450 fold from the sequence and recognizing that the other three options involve non-P450 primary-metabolic enzymes provides a concrete biological argument to select D.",
    "missing_item_specific_fact": "None strictly required. Precise family assignment (CYP716 → triterpenoid-specific) would strengthen the answer, but the broader P450-vs-non-P450 logic already eliminates A, B, and C.",
    "reason": "The heme-binding signature is extractable from the raw sequence, and the biological fact that plant P450s are hallmarks of secondary metabolism while threonine synthase, NAD synthetase, and shikimate-pathway enzymes are not P450s constitutes a general-knowledge reasoning chain that distinguishes D from the distractors without needing to memorize this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe pathways whose enzymatic steps are well-characterized non-P450 enzymes (PLP-dependent, adenylyltransferase, and shikimate-pathway enzymes respectively). Only D is compatible with a cytochrome P450. No other option is defensible once the P450 identity is recognized."
  },
  "important_caveats": [
    "The UniProt annotation is experimental (ECO:0000269) based on a 2025 Nat. Chem. Biol. paper; the pathway assignment is well-supported.",
    "The organism name (Saponaria officinalis, soapwort) is not provided in the model input, so reasoning must rely on sequence-derived features (P450 motif, signal peptide, ER-targeting) rather than organism context.",
    "While the CYP716 family is triterpenoid-specific, the broader P450→secondary-metabolism logic suffices to eliminate the three primary-metabolism distractors without family-level precision.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning argument stands independently on sequence features and general biology."
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

**Accession:** `A0AAW1NEA3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
"A0AAW1NEA3"
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"Cytochrome P450 716A378"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoCYP716A378"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"1.14.14.126"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Beta-amyrin 28-monooxygenase CYP716A378"}}}
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48148.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.561544+00:00.  

```text
ID   C7168_SAPOF             Reviewed;         485 AA.
AC   A0AAW1NEA3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A378 {ECO:0000305};
DE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};
DE   AltName: Full=Cytochrome P450 716A378 {ECO:0000303|PubMed:39043959};
DE            Short=SoCYP716A378 {ECO:0000303|PubMed:39043959};
GN   Name=CYP716A378 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11003497m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_01G137900 {ECO:0000312|EMBL:KAK9757076.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)  
**Locator:** `lines 55-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.561544+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
