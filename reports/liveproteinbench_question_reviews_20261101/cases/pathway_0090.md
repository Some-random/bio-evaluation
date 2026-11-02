# pathway_0090

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
MAGYLPEPLRMMVTNPAISDFTSDGPLPYALRQKFTGWPPPPAAADISLASQTVLVTGATSGVGLEAARQLAQLGPRLLILGARNLSKADGVKRQLEQDTPHVAVQVAKLDLEDLSSVDRFVDGLHASAIHLDLALLNAGFFANDDRMTPDGYSSLFQVNFLSTAYLAFRLLPLLQTTTTAPEASPQGPRLVLVTSEAHAWTTFPVPPEPAENSLPILSSFRQKESLGSADDQYYRAKLLLALIGKELSRRLTTMQMATSVVITTPGFCASNFFPDSVMTRLIQLISARSIQQGGALHVFAATAQGPQMHGAYLRDGKPTGLSKFAEGPQGQILQQRLWVEMEQFLAGRGYLLSSILKPSSPLQIDGPV

[Multiple Choices]
A. L-threonine biosynthesis
B. Glycolipid biosynthesis
C. Antifungal biosynthesis. .
D. tetrahydrofolate interconversion. .
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

> The exact sequence matches UniProt entry P9WEG6, annotated as short-chain dehydrogenase rstn4 and assigned to antifungal biosynthesis. The pathway annotation cites ECO:0000269 and PubMed 33857369, supporting the key, though the primary paper was not independently assessed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has features consistent with a short-chain dehydrogenase, but that enzyme-family inference does not identify its pathway; the sequence alone gives no clear basis to select antifungal biosynthesis over the listed alternatives.


**Missing item-specific fact**

> The protein-specific identification as rstn4 in a restricticin biosynthesis cluster and its pathway assignment.


**Reason**

> The supporting pathway annotation is linked to this exact protein and external literature. That item-specific fact is absent from the sequence and choices, and cannot be replaced by generic sequence-based enzyme-family reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports C, and the pathway labels are distinct. The issue is that the supplied input does not meaningfully distinguish the options, rather than that multiple options are supported.


### Important caveats

- The sequence match is exact in both the current UniProt entry and the historical entry available by the stated cutoff.
- The UniProt pathway assignment cites experimental evidence, but the primary study was not independently retrieved or validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a short-chain dehydrogenase, but that enzyme-family inference does not identify its pathway; the sequence alone gives no clear basis to select antifungal biosynthesis over the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as rstn4 in a restricticin biosynthesis cluster and its pathway assignment.",
    "reason": "The supporting pathway annotation is linked to this exact protein and external literature. That item-specific fact is absent from the sequence and choices, and cannot be replaced by generic sequence-based enzyme-family reasoning."
  },
  "case_id": "pathway_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P9WEG6, annotated as short-chain dehydrogenase rstn4 and assigned to antifungal biosynthesis. The pathway annotation cites ECO:0000269 and PubMed 33857369, supporting the key, though the primary paper was not independently assessed here."
  },
  "important_caveats": [
    "The sequence match is exact in both the current UniProt entry and the historical entry available by the stated cutoff.",
    "The UniProt pathway assignment cites experimental evidence, but the primary study was not independently retrieved or validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C, and the pathway labels are distinct. The issue is that the supplied input does not meaningfully distinguish the options, rather than that multiple options are supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P9WEG6, annotated as short-chain dehydrogenase rstn4 and assigned to antifungal biosynthesis. The pathway annotation cites ECO:0000269 and PubMed 33857369, supporting the key, though the primary paper was not independently assessed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has features consistent with a short-chain dehydrogenase, but that enzyme-family inference does not identify its pathway; the sequence alone gives no clear basis to select antifungal biosynthesis over the listed alternatives.",
    "missing_item_specific_fact": "The protein-specific identification as rstn4 in a restricticin biosynthesis cluster and its pathway assignment.",
    "reason": "The supporting pathway annotation is linked to this exact protein and external literature. That item-specific fact is absent from the sequence and choices, and cannot be replaced by generic sequence-based enzyme-family reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C, and the pathway labels are distinct. The issue is that the supplied input does not meaningfully distinguish the options, rather than that multiple options are supported."
  },
  "important_caveats": [
    "The sequence match is exact in both the current UniProt entry and the historical entry available by the stated cutoff.",
    "The UniProt pathway assignment cites experimental evidence, but the primary study was not independently retrieved or validated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P9WEG6 (sequence matched, 369 AA) explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (experimental) from PubMed:33857369 (Liu et al., JACS 2021). The protein is named 'Short chain dehydrogenase rstn4' / 'Restricticin biosynthesis cluster protein 4' from Aspergillus nomiae, part of a biosynthetic gene cluster for a CYP51-inhibiting antifungal natural product. The sequence is confirmed as an SDR (Rossmann-fold NAD(P)-binding motif 'GATSGVGLEA' and catalytic tetrad region visible). The expected answer C is directly stated in the database annotation.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence clearly encodes a short-chain dehydrogenase/reductase (SDR): the N-terminal Rossmann-fold motif (GATSGVGLEA…GARNLSKADG) and the catalytic tetrad region (…TSEAHAWT…YXXXK-like) are recognizable. However, SDRs are ubiquitous across dozens of pathways—homoserine dehydrogenase in threonine biosynthesis (option A), lipid-modifying SDRs in glycolipid pathways (option B), and folate-metabolism SDRs (option D) all share this fold. Nothing in the 369-aa sequence uniquely encodes 'antifungal secondary-metabolite biosynthesis' as opposed to any other SDR-containing pathway.


**Missing item-specific fact**

> The specific biosynthetic gene cluster assignment (rstn4 within the restricticin BGC) and the experimental demonstration that this SDR participates in CYP51-inhibitor (antifungal) biosynthesis (PubMed:33857369). Without knowing the organism, the gene cluster context, or the product identity, the sequence alone cannot distinguish 'antifungal biosynthesis' from glycolipid biosynthesis or other SDR-associated pathways.


**Reason**

> Recognizing the SDR fold narrows the enzyme class but does not identify the pathway. The term 'Antifungal biosynthesis' is a project-specific annotation for a particular secondary-metabolite cluster, not a standard textbook pathway name. Selecting C over A, B, or D requires prior knowledge of this specific protein's role in the restricticin gene cluster, which is an item-specific database/experimental fact absent from the sequence input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Homoserine dehydrogenase (threonine biosynthesis, option A) is itself an SDR with a very similar fold; without additional context a model could reasonably assign an SDR to amino-acid biosynthesis. Similarly, SDRs participate in lipid/glycolipid modification (option B). The wording 'Antifungal biosynthesis' is non-standard and the trailing periods in options C and D add minor formatting noise but do not change the substantive ambiguity among SDR-associated pathways.


### Important caveats

- The UniProt annotation is experimental (ECO:0000269) but the pathway label 'Antifungal biosynthesis' is a project-level grouping, not a canonical KEGG/MetaCyc pathway name.
- The evaluated model was not given the organism name, gene cluster context, or accession; it received only the 369-aa sequence and four pathway labels.
- The entry was first public in Feb 2025; whether it was available in the author's source snapshot is unknown, though the sequence itself is unchanged since version 1.
- The trailing periods in options C and D are cosmetic and do not affect scientific content.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly encodes a short-chain dehydrogenase/reductase (SDR): the N-terminal Rossmann-fold motif (GATSGVGLEA…GARNLSKADG) and the catalytic tetrad region (…TSEAHAWT…YXXXK-like) are recognizable. However, SDRs are ubiquitous across dozens of pathways—homoserine dehydrogenase in threonine biosynthesis (option A), lipid-modifying SDRs in glycolipid pathways (option B), and folate-metabolism SDRs (option D) all share this fold. Nothing in the 369-aa sequence uniquely encodes 'antifungal secondary-metabolite biosynthesis' as opposed to any other SDR-containing pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific biosynthetic gene cluster assignment (rstn4 within the restricticin BGC) and the experimental demonstration that this SDR participates in CYP51-inhibitor (antifungal) biosynthesis (PubMed:33857369). Without knowing the organism, the gene cluster context, or the product identity, the sequence alone cannot distinguish 'antifungal biosynthesis' from glycolipid biosynthesis or other SDR-associated pathways.",
    "reason": "Recognizing the SDR fold narrows the enzyme class but does not identify the pathway. The term 'Antifungal biosynthesis' is a project-specific annotation for a particular secondary-metabolite cluster, not a standard textbook pathway name. Selecting C over A, B, or D requires prior knowledge of this specific protein's role in the restricticin gene cluster, which is an item-specific database/experimental fact absent from the sequence input."
  },
  "case_id": "pathway_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P9WEG6 (sequence matched, 369 AA) explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (experimental) from PubMed:33857369 (Liu et al., JACS 2021). The protein is named 'Short chain dehydrogenase rstn4' / 'Restricticin biosynthesis cluster protein 4' from Aspergillus nomiae, part of a biosynthetic gene cluster for a CYP51-inhibiting antifungal natural product. The sequence is confirmed as an SDR (Rossmann-fold NAD(P)-binding motif 'GATSGVGLEA' and catalytic tetrad region visible). The expected answer C is directly stated in the database annotation."
  },
  "important_caveats": [
    "The UniProt annotation is experimental (ECO:0000269) but the pathway label 'Antifungal biosynthesis' is a project-level grouping, not a canonical KEGG/MetaCyc pathway name.",
    "The evaluated model was not given the organism name, gene cluster context, or accession; it received only the 369-aa sequence and four pathway labels.",
    "The entry was first public in Feb 2025; whether it was available in the author's source snapshot is unknown, though the sequence itself is unchanged since version 1.",
    "The trailing periods in options C and D are cosmetic and do not affect scientific content."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Homoserine dehydrogenase (threonine biosynthesis, option A) is itself an SDR with a very similar fold; without additional context a model could reasonably assign an SDR to amino-acid biosynthesis. Similarly, SDRs participate in lipid/glycolipid modification (option B). The wording 'Antifungal biosynthesis' is non-standard and the trailing periods in options C and D add minor formatting noise but do not change the substantive ambiguity among SDR-associated pathways."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P9WEG6 (sequence matched, 369 AA) explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (experimental) from PubMed:33857369 (Liu et al., JACS 2021). The protein is named 'Short chain dehydrogenase rstn4' / 'Restricticin biosynthesis cluster protein 4' from Aspergillus nomiae, part of a biosynthetic gene cluster for a CYP51-inhibiting antifungal natural product. The sequence is confirmed as an SDR (Rossmann-fold NAD(P)-binding motif 'GATSGVGLEA' and catalytic tetrad region visible). The expected answer C is directly stated in the database annotation.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence clearly encodes a short-chain dehydrogenase/reductase (SDR): the N-terminal Rossmann-fold motif (GATSGVGLEA…GARNLSKADG) and the catalytic tetrad region (…TSEAHAWT…YXXXK-like) are recognizable. However, SDRs are ubiquitous across dozens of pathways—homoserine dehydrogenase in threonine biosynthesis (option A), lipid-modifying SDRs in glycolipid pathways (option B), and folate-metabolism SDRs (option D) all share this fold. Nothing in the 369-aa sequence uniquely encodes 'antifungal secondary-metabolite biosynthesis' as opposed to any other SDR-containing pathway.",
    "missing_item_specific_fact": "The specific biosynthetic gene cluster assignment (rstn4 within the restricticin BGC) and the experimental demonstration that this SDR participates in CYP51-inhibitor (antifungal) biosynthesis (PubMed:33857369). Without knowing the organism, the gene cluster context, or the product identity, the sequence alone cannot distinguish 'antifungal biosynthesis' from glycolipid biosynthesis or other SDR-associated pathways.",
    "reason": "Recognizing the SDR fold narrows the enzyme class but does not identify the pathway. The term 'Antifungal biosynthesis' is a project-specific annotation for a particular secondary-metabolite cluster, not a standard textbook pathway name. Selecting C over A, B, or D requires prior knowledge of this specific protein's role in the restricticin gene cluster, which is an item-specific database/experimental fact absent from the sequence input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Homoserine dehydrogenase (threonine biosynthesis, option A) is itself an SDR with a very similar fold; without additional context a model could reasonably assign an SDR to amino-acid biosynthesis. Similarly, SDRs participate in lipid/glycolipid modification (option B). The wording 'Antifungal biosynthesis' is non-standard and the trailing periods in options C and D add minor formatting noise but do not change the substantive ambiguity among SDR-associated pathways."
  },
  "important_caveats": [
    "The UniProt annotation is experimental (ECO:0000269) but the pathway label 'Antifungal biosynthesis' is a project-level grouping, not a canonical KEGG/MetaCyc pathway name.",
    "The evaluated model was not given the organism name, gene cluster context, or accession; it received only the 369-aa sequence and four pathway labels.",
    "The entry was first public in Feb 2025; whether it was available in the author's source snapshot is unknown, though the sequence itself is unchanged since version 1.",
    "The trailing periods in options C and D are cosmetic and do not affect scientific content."
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

**Accession:** `P9WEG6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.134193+00:00.  

```json
"P9WEG6"
```

Source SHA-256: `0fba683103f8b5ad991b939caaa7539457c1fa5b0a1cdcdff8183c7b2378f85a`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG6.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.134193+00:00.  

```json
{"lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Eurotiomycetes","Eurotiomycetidae","Eurotiales","Aspergillaceae","Aspergillus","Circumdati"],"scientificName":"Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 / M93)","taxonId":1509407}
```

Source SHA-256: `0fba683103f8b5ad991b939caaa7539457c1fa5b0a1cdcdff8183c7b2378f85a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.134193+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 4"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"1.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Short chain dehydrogenase rstn4"}}}
```

Source SHA-256: `0fba683103f8b5ad991b939caaa7539457c1fa5b0a1cdcdff8183c7b2378f85a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.134193+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"Antifungal biosynthesis"}]}
```

Source SHA-256: `0fba683103f8b5ad991b939caaa7539457c1fa5b0a1cdcdff8183c7b2378f85a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.134193+00:00.  

```json
{"citation":{"authors":["Liu N.","Abramyan E.D.","Cheng W.","Perlatti B.","Harvey C.J.B.","Bills G.F.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33857369"},{"database":"DOI","id":"10.1021/jacs.1c01516"}],"citationType":"journal article","firstPage":"6043","id":"33857369","journal":"J. Am. Chem. Soc.","lastPage":"6047","publicationDate":"2021","title":"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.","volume":"143"},"referenceNumber":2,"referencePositions":["FUNCTION","PATHWAY"]}
```

Source SHA-256: `0fba683103f8b5ad991b939caaa7539457c1fa5b0a1cdcdff8183c7b2378f85a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG6?format=txt&versions=3)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:28:24.829652+00:00.  

```text
ID   RSTN4_ASPN3             Reviewed;         369 AA.
AC   P9WEG6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=Short chain dehydrogenase rstn4 {ECO:0000303|PubMed:33857369};
DE            EC=1.1.1.- {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 4 {ECO:0000303|PubMed:33857369};
GN   Name=rstn4 {ECO:0000303|PubMed:33857369};
OS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /
OS   M93).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=1509407;
```

Source SHA-256: `ff8c1b64817125a79245574591c776cf54dc0454d7c5b3122875fb82a7084649`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG6?format=txt&versions=3)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:28:24.829652+00:00.  

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

Source SHA-256: `ff8c1b64817125a79245574591c776cf54dc0454d7c5b3122875fb82a7084649`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG6?format=txt&versions=3)  
**Locator:** `lines 47-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:28:24.829652+00:00.  

```text
CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000269|PubMed:33857369}.
```

Source SHA-256: `ff8c1b64817125a79245574591c776cf54dc0454d7c5b3122875fb82a7084649`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 90. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
