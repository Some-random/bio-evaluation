# pathway_0187

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATDTAVTGAPETMQLRLASGNGPVTRTVLRTPLRDALPSEVPLIDISPIFSTSVADRKAVACKIHDAATNIGFFYIQNHRVPSRDTDMAYSASLDFFRQDMEAKMKADAKKGPFDSGYRGPGTQRVNPDEGADLRETYSILYDPMLDPTVPDPARIPEPASRFLHLGRAPFESTDTLPHFKDAFVRYFQACLALARALTRTFALSLDLPESAFDSKVQYPDASLEINFYPPISTGHAVSAPADPDTRVSIGSHTDFLLFTILWQDSNGGLQVLNREGQWIRASPVEGTFVVNIGDYLQRITNDKYVSTVHRAQNWSGRQRVSMPFFWGFGMHESCQVLESCCGEDGKSKYDEVRCVDWVSRRLGNLFDLSDKG

[Multiple Choices]
A. Pyrimidine metabolism
B. peptidoglycan degradation. .
C. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
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

> The supplied sequence exactly matches the UniProt entry annotated as ppzC, with the pathway “Secondary metabolite biosynthesis.” The annotation cites experimental evidence, including a 2024 study on enzymes in the PPZ cluster. This supports choice D for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features might suggest an enzyme family, but they do not establish this protein’s specific biosynthetic pathway. The pathway assignment depends on its role in the PPZ gene cluster.


**Missing item-specific fact**

> The protein-specific functional and pathway annotation linking ppzC to secondary-metabolite biosynthesis, including its PPZ-cluster context.


**Reason**

> That functional and pathway information is not supplied in the sequence or choices. Identifying the pathway requires an external annotation or equivalent protein-specific knowledge; family-level sequence inference alone does not distinguish D reliably.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports D, and none of the other options is comparably supported for this protein.


### Important caveats

- The reviewer-only evidence is not information supplied to the evaluated model.
- The exact sequence match is established in both current and historical UniProt records; the author’s precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features might suggest an enzyme family, but they do not establish this protein’s specific biosynthetic pathway. The pathway assignment depends on its role in the PPZ gene cluster.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional and pathway annotation linking ppzC to secondary-metabolite biosynthesis, including its PPZ-cluster context.",
    "reason": "That functional and pathway information is not supplied in the sequence or choices. Identifying the pathway requires an external annotation or equivalent protein-specific knowledge; family-level sequence inference alone does not distinguish D reliably."
  },
  "case_id": "pathway_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as ppzC, with the pathway “Secondary metabolite biosynthesis.” The annotation cites experimental evidence, including a 2024 study on enzymes in the PPZ cluster. This supports choice D for this protein."
  },
  "important_caveats": [
    "The reviewer-only evidence is not information supplied to the evaluated model.",
    "The exact sequence match is established in both current and historical UniProt records; the author’s precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D, and none of the other options is comparably supported for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as ppzC, with the pathway “Secondary metabolite biosynthesis.” The annotation cites experimental evidence, including a 2024 study on enzymes in the PPZ cluster. This supports choice D for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features might suggest an enzyme family, but they do not establish this protein’s specific biosynthetic pathway. The pathway assignment depends on its role in the PPZ gene cluster.",
    "missing_item_specific_fact": "The protein-specific functional and pathway annotation linking ppzC to secondary-metabolite biosynthesis, including its PPZ-cluster context.",
    "reason": "That functional and pathway information is not supplied in the sequence or choices. Identifying the pathway requires an external annotation or equivalent protein-specific knowledge; family-level sequence inference alone does not distinguish D reliably."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D, and none of the other options is comparably supported for this protein."
  },
  "important_caveats": [
    "The reviewer-only evidence is not information supplied to the evaluated model.",
    "The exact sequence match is established in both current and historical UniProt records; the author’s precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry A0A455ZKR7 (PPZC_METMF) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:38578094). The protein is ppzC, a 2-oxoglutarate-Fe(II) type oxidoreductase (EC 1.14.11.-) in the pyrrolopyrazine biosynthetic gene cluster of Metarhizium majus. Pyrrolopyrazine/peramine is a fungal secondary metabolite. The sequence in the question matches the UniProt entry (374 aa, SHA-256 confirmed). The other options (pyrimidine metabolism, peptidoglycan degradation, chorismate biosynthesis step 7/7) are incompatible with this enzyme's identity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs consistent with a 2-oxoglutarate/Fe(II) oxygenase facial triad (e.g., 'IHDA' as HxD and 'HESC' as the distal His, separated by the long loops characteristic of the double-stranded β-helix fold). 2-OG oxygenases are overwhelmingly associated with secondary metabolite biosynthesis, particularly as tailoring enzymes in fungal NRPS/PKS gene clusters. The three distractors are incompatible with a 2-OG oxygenase: (B) peptidoglycan degradation involves lysozymes/amidases/transglycosylases with entirely different folds and is a bacterial cell-wall process irrelevant to a fungal protein; (A) pyrimidine metabolism enzymes (dihydroorotase, uridine phosphorylase, etc.) share no structural or mechanistic resemblance; (C) chorismate synthase (step 7/7 of the shikimate pathway) is an FMN-dependent enzyme with a completely different fold. By recognizing the 2-OG oxygenase architecture and eliminating mechanistically incompatible alternatives, 'Secondary metabolite biosynthesis' is the only viable pathway category.


**Missing item-specific fact**

> Exact identification as ppzC in the pyrrolopyrazine cluster requires database lookup, but the broader pathway category 'Secondary metabolite biosynthesis' is inferable from the enzyme class and elimination of incompatible alternatives.


**Reason**

> A knowledgeable model can recognize the 2-OG/Fe(II) oxygenase fold from the facial triad spacing and overall domain architecture, then apply the well-established general principle that this enzyme class is predominantly involved in secondary metabolite tailoring. The three distractors can be eliminated by mechanistic incompatibility without needing to know the specific protein identity. This constitutes a concrete biological reasoning chain rather than pure memorization of a database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mechanistically and taxonomically distinct. Only 'Secondary metabolite biosynthesis' is compatible with a 2-OG oxygenase in a fungal biosynthetic gene cluster. Minor trailing-period formatting artifacts in options B, C, and D ('. .') do not create substantive ambiguity.


### Important caveats

- The organism (Metarhizium majus, a fungus) is not stated in the question; identifying it as fungal strengthens the elimination of peptidoglycan degradation but is not strictly required since the enzyme fold itself is incompatible with peptidoglycan-degrading activity.
- The 2-OG oxygenase fold identification from raw sequence relies on recognizing the HxD/E...H facial triad with characteristic long intervening loops; this is expert-level but falls within general biochemistry knowledge.
- The UniProt pathway annotation 'Secondary metabolite biosynthesis' is a broad umbrella term; the specific sub-pathway (pyrrolopyrazine biosynthesis) is not among the options, so no finer-grained distinction is tested.
- All reviewer evidence is from the current and historical UniProt snapshots with confirmed sequence match; the author's source snapshot is unknown but the sequence has been unchanged since 2019.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs consistent with a 2-oxoglutarate/Fe(II) oxygenase facial triad (e.g., 'IHDA' as HxD and 'HESC' as the distal His, separated by the long loops characteristic of the double-stranded β-helix fold). 2-OG oxygenases are overwhelmingly associated with secondary metabolite biosynthesis, particularly as tailoring enzymes in fungal NRPS/PKS gene clusters. The three distractors are incompatible with a 2-OG oxygenase: (B) peptidoglycan degradation involves lysozymes/amidases/transglycosylases with entirely different folds and is a bacterial cell-wall process irrelevant to a fungal protein; (A) pyrimidine metabolism enzymes (dihydroorotase, uridine phosphorylase, etc.) share no structural or mechanistic resemblance; (C) chorismate synthase (step 7/7 of the shikimate pathway) is an FMN-dependent enzyme with a completely different fold. By recognizing the 2-OG oxygenase architecture and eliminating mechanistically incompatible alternatives, 'Secondary metabolite biosynthesis' is the only viable pathway category.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact identification as ppzC in the pyrrolopyrazine cluster requires database lookup, but the broader pathway category 'Secondary metabolite biosynthesis' is inferable from the enzyme class and elimination of incompatible alternatives.",
    "reason": "A knowledgeable model can recognize the 2-OG/Fe(II) oxygenase fold from the facial triad spacing and overall domain architecture, then apply the well-established general principle that this enzyme class is predominantly involved in secondary metabolite tailoring. The three distractors can be eliminated by mechanistic incompatibility without needing to know the specific protein identity. This constitutes a concrete biological reasoning chain rather than pure memorization of a database annotation."
  },
  "case_id": "pathway_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry A0A455ZKR7 (PPZC_METMF) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:38578094). The protein is ppzC, a 2-oxoglutarate-Fe(II) type oxidoreductase (EC 1.14.11.-) in the pyrrolopyrazine biosynthetic gene cluster of Metarhizium majus. Pyrrolopyrazine/peramine is a fungal secondary metabolite. The sequence in the question matches the UniProt entry (374 aa, SHA-256 confirmed). The other options (pyrimidine metabolism, peptidoglycan degradation, chorismate biosynthesis step 7/7) are incompatible with this enzyme's identity."
  },
  "important_caveats": [
    "The organism (Metarhizium majus, a fungus) is not stated in the question; identifying it as fungal strengthens the elimination of peptidoglycan degradation but is not strictly required since the enzyme fold itself is incompatible with peptidoglycan-degrading activity.",
    "The 2-OG oxygenase fold identification from raw sequence relies on recognizing the HxD/E...H facial triad with characteristic long intervening loops; this is expert-level but falls within general biochemistry knowledge.",
    "The UniProt pathway annotation 'Secondary metabolite biosynthesis' is a broad umbrella term; the specific sub-pathway (pyrrolopyrazine biosynthesis) is not among the options, so no finer-grained distinction is tested.",
    "All reviewer evidence is from the current and historical UniProt snapshots with confirmed sequence match; the author's source snapshot is unknown but the sequence has been unchanged since 2019."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mechanistically and taxonomically distinct. Only 'Secondary metabolite biosynthesis' is compatible with a 2-OG oxygenase in a fungal biosynthetic gene cluster. Minor trailing-period formatting artifacts in options B, C, and D ('. .') do not create substantive ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry A0A455ZKR7 (PPZC_METMF) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:38578094). The protein is ppzC, a 2-oxoglutarate-Fe(II) type oxidoreductase (EC 1.14.11.-) in the pyrrolopyrazine biosynthetic gene cluster of Metarhizium majus. Pyrrolopyrazine/peramine is a fungal secondary metabolite. The sequence in the question matches the UniProt entry (374 aa, SHA-256 confirmed). The other options (pyrimidine metabolism, peptidoglycan degradation, chorismate biosynthesis step 7/7) are incompatible with this enzyme's identity.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs consistent with a 2-oxoglutarate/Fe(II) oxygenase facial triad (e.g., 'IHDA' as HxD and 'HESC' as the distal His, separated by the long loops characteristic of the double-stranded β-helix fold). 2-OG oxygenases are overwhelmingly associated with secondary metabolite biosynthesis, particularly as tailoring enzymes in fungal NRPS/PKS gene clusters. The three distractors are incompatible with a 2-OG oxygenase: (B) peptidoglycan degradation involves lysozymes/amidases/transglycosylases with entirely different folds and is a bacterial cell-wall process irrelevant to a fungal protein; (A) pyrimidine metabolism enzymes (dihydroorotase, uridine phosphorylase, etc.) share no structural or mechanistic resemblance; (C) chorismate synthase (step 7/7 of the shikimate pathway) is an FMN-dependent enzyme with a completely different fold. By recognizing the 2-OG oxygenase architecture and eliminating mechanistically incompatible alternatives, 'Secondary metabolite biosynthesis' is the only viable pathway category.",
    "missing_item_specific_fact": "Exact identification as ppzC in the pyrrolopyrazine cluster requires database lookup, but the broader pathway category 'Secondary metabolite biosynthesis' is inferable from the enzyme class and elimination of incompatible alternatives.",
    "reason": "A knowledgeable model can recognize the 2-OG/Fe(II) oxygenase fold from the facial triad spacing and overall domain architecture, then apply the well-established general principle that this enzyme class is predominantly involved in secondary metabolite tailoring. The three distractors can be eliminated by mechanistic incompatibility without needing to know the specific protein identity. This constitutes a concrete biological reasoning chain rather than pure memorization of a database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mechanistically and taxonomically distinct. Only 'Secondary metabolite biosynthesis' is compatible with a 2-OG oxygenase in a fungal biosynthetic gene cluster. Minor trailing-period formatting artifacts in options B, C, and D ('. .') do not create substantive ambiguity."
  },
  "important_caveats": [
    "The organism (Metarhizium majus, a fungus) is not stated in the question; identifying it as fungal strengthens the elimination of peptidoglycan degradation but is not strictly required since the enzyme fold itself is incompatible with peptidoglycan-degrading activity.",
    "The 2-OG oxygenase fold identification from raw sequence relies on recognizing the HxD/E...H facial triad with characteristic long intervening loops; this is expert-level but falls within general biochemistry knowledge.",
    "The UniProt pathway annotation 'Secondary metabolite biosynthesis' is a broad umbrella term; the specific sub-pathway (pyrrolopyrazine biosynthesis) is not among the options, so no finer-grained distinction is tested.",
    "All reviewer evidence is from the current and historical UniProt snapshots with confirmed sequence match; the author's source snapshot is unknown but the sequence has been unchanged since 2019."
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

**Accession:** `A0A455ZKR7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
"A0A455ZKR7"
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"Pyrrolopyrazine biosynthesis cluster protein C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"value":"1.14.11.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"2-oxoglutarate-Fe(II) type oxidoreductase ppzC"}}}
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"value":"Secondary metabolite biosynthesis"}]}
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZKR7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.380201+00:00.  

```json
{"citation":{"authors":["Rothchild K.W.","Hagar M.","Berry D.","Ryan K.S."],"citationCrossReferences":[{"database":"PubMed","id":"38578094"},{"database":"DOI","id":"10.1021/jacs.4c01419"}],"citationType":"journal article","firstPage":"10263","id":"38578094","journal":"J. Am. Chem. Soc.","lastPage":"10267","publicationDate":"2024","title":"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.","volume":"146"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `6f69e81e503f1d4a9ac28a7bfbb2048904d8b6f1c7569c1f7d3c7190d601037a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:18.441147+00:00.  

```text
ID   PPZC_METMF              Reviewed;         374 AA.
AC   A0A455ZKR7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUN-2019, sequence version 1.
DT   28-JAN-2026, entry version 21.
DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzC {ECO:0000303|PubMed:30452111};
DE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};
DE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein C {ECO:0000303|PubMed:30452111};
GN   Name=ppzC;
OS   Metarhizium majus (strain ARSEF 297).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;
OC   Metarhizium majus.
OX   NCBI_TaxID=1276143;
```

Source SHA-256: `a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)  
**Locator:** `lines 24-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:18.441147+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=38578094; DOI=10.1021/jacs.4c01419;
RA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;
RT   "Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ
RT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.";
RL   J. Am. Chem. Soc. 146:10263-10267(2024).
```

Source SHA-256: `a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZKR7?format=txt&versions=21)  
**Locator:** `lines 63-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:25:18.441147+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis.
CC       {ECO:0000269|PubMed:38578094}.
```

Source SHA-256: `a07bd633297af25909c49dae08be64b07a7ca451f1bf6735c0a9d88a7ac8d4ca`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 187. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
