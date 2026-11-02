# pathway_0010

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Antifungal biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLHLTPLIFLSLAMAAAVGVWGVFTWNGGFDEMDGIVASHQSTGILGLQHCPDLDRGLMSMVAFNLPVVGRNPIFPAGRRFMVQFLANVAVIPVILNTEGARAEPGSLVRYSTTWGLFSQMATSAVMCPLYGFWFVRQSGAKQTEGGTLRPLPPNKWVVPSSVLIGYGIPALLSFDPFQWGLDLQIRGILAFTLYPLCISLTARLMRKVSKKRGRSLSPEWNSTISYVAVGVVGMVSHLWYLGTGLTGYPLSGDAVSSVAGPTEVGRAAQLVLLFLQIDYVITFAAMLLLAWHELTRHQLVRSWRAAGTLAVGWLFLGPGATLAAAWALREQWLSRPRGVRGEIKQKPK

[Multiple Choices]
A. polypeptide chain elongation. .
B. Antifungal biosynthesis. .
C. tetrahydrofolate interconversion. .
D. Purine metabolism
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

> The exact sequence matches UniProt entry P9WEG7, which annotates the protein as terpene cyclase rstn5 / a restricticin-biosynthesis cluster protein and assigns it to antifungal biosynthesis. The pathway annotation cites ECO:0000269 evidence linked to a 2021 publication, supporting choice B, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic, consistent with a membrane-associated protein, but that feature does not distinguish antifungal biosynthesis from the listed alternatives.


**Missing item-specific fact**

> Identifying this protein as rstn5 in the restricticin biosynthesis cluster, or equivalent protein-specific functional evidence, is needed to select antifungal biosynthesis.


**Reason**

> The sequence and choices provide no meaningful general biological basis for identifying this specific pathway; the distinguishing fact is an external, protein-specific annotation or functional result.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence assigns the matched protein to antifungal biosynthesis, and no competing choice is supported by the evidence.


### Important caveats

- The sequence match and UniProt annotations are reviewer-only evidence, not information provided to the evaluated model.
- The pathway annotation cites experimental evidence, but the cited primary publication was not independently assessed; the author's exact data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic, consistent with a membrane-associated protein, but that feature does not distinguish antifungal biosynthesis from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this protein as rstn5 in the restricticin biosynthesis cluster, or equivalent protein-specific functional evidence, is needed to select antifungal biosynthesis.",
    "reason": "The sequence and choices provide no meaningful general biological basis for identifying this specific pathway; the distinguishing fact is an external, protein-specific annotation or functional result."
  },
  "case_id": "pathway_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P9WEG7, which annotates the protein as terpene cyclase rstn5 / a restricticin-biosynthesis cluster protein and assigns it to antifungal biosynthesis. The pathway annotation cites ECO:0000269 evidence linked to a 2021 publication, supporting choice B, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match and UniProt annotations are reviewer-only evidence, not information provided to the evaluated model.",
    "The pathway annotation cites experimental evidence, but the cited primary publication was not independently assessed; the author's exact data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence assigns the matched protein to antifungal biosynthesis, and no competing choice is supported by the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P9WEG7, which annotates the protein as terpene cyclase rstn5 / a restricticin-biosynthesis cluster protein and assigns it to antifungal biosynthesis. The pathway annotation cites ECO:0000269 evidence linked to a 2021 publication, supporting choice B, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic, consistent with a membrane-associated protein, but that feature does not distinguish antifungal biosynthesis from the listed alternatives.",
    "missing_item_specific_fact": "Identifying this protein as rstn5 in the restricticin biosynthesis cluster, or equivalent protein-specific functional evidence, is needed to select antifungal biosynthesis.",
    "reason": "The sequence and choices provide no meaningful general biological basis for identifying this specific pathway; the distinguishing fact is an external, protein-specific annotation or functional result."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence assigns the matched protein to antifungal biosynthesis, and no competing choice is supported by the evidence."
  },
  "important_caveats": [
    "The sequence match and UniProt annotations are reviewer-only evidence, not information provided to the evaluated model.",
    "The pathway annotation cites experimental evidence, but the cited primary publication was not independently assessed; the author's exact data-source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P9WEG7 (sequence matched exactly, 349 AA) annotates this protein as 'Terpene cyclase rstn5' / 'Restricticin biosynthesis cluster protein 5' with PATHWAY: 'Antifungal biosynthesis' (ECO:0000269, experimental evidence from PubMed:33857369, a 2021 JACS paper on genome mining of CYP51-inhibitor biosynthetic gene clusters). The EC number 5.4.99.- (isomerase/cyclase) is consistent with a terpene cyclase. The antifungal designation derives from the biological activity of the product (restricticin inhibits CYP51, a fungal enzyme). The sequence match is exact in both current and historical (v2) records.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Elimination is partially possible: the N-terminal signal peptide and multiple hydrophobic TM-like segments make this incompatible with soluble translation machinery (A), folate-metabolizing enzymes (C), or purine-pathway enzymes (D). However, positively arriving at the pathway name 'Antifungal biosynthesis' requires knowing that this specific terpene cyclase (rstn5) belongs to the restricticin biosynthetic gene cluster and that UniProt assigns the pathway label 'Antifungal biosynthesis' rather than the more generic 'terpene biosynthesis' or 'secondary metabolite biosynthesis.' The DDxxD/NDxxD terpene-cyclase motifs are not unambiguously identifiable in this 349-aa sequence by casual inspection.


**Missing item-specific fact**

> The specific UniProt pathway annotation 'Antifungal biosynthesis' for this terpene cyclase, which is a database-specific naming choice tied to the restricticin biosynthetic cluster (rstn5) and its CYP51-inhibitor product. Without this annotation, a reasoning model would more naturally propose 'terpene biosynthesis' or 'secondary metabolism' rather than the exact label 'Antifungal biosynthesis.'


**Reason**

> While general biological knowledge permits elimination of A, C, and D (the sequence clearly is not a ribosomal/elongation factor, folate enzyme, or purine enzyme), the positive identification of the specific pathway label 'Antifungal biosynthesis' depends on the UniProt annotation of this particular terpene cyclase. The pathway name is an annotation convention, not a self-evident deduction from sequence features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors A (polypeptide chain elongation), C (tetrahydrofolate interconversion), and D (purine metabolism) are clearly incompatible with a membrane-associated terpene cyclase from a fungal secondary-metabolite gene cluster. No other option is defensible for this sequence.


### Important caveats

- The evidence code ECO:0000269 indicates experimental evidence, but the underlying experiment (2021 JACS paper) primarily involved genome mining, heterologous expression, and chemical characterization; the 'antifungal' label reflects the product's biological activity rather than a dedicated antifungal-pathway assay.
- The pathway name 'Antifungal biosynthesis' is a UniProt-specific annotation convention; the same enzyme could reasonably be placed under 'terpene biosynthesis' or 'natural product biosynthesis' in other databases.
- The UniProt entry was first public in Feb 2025; the author's source snapshot is unknown, but the sequence matches both current (v4) and historical (v2) records.
- The terpene cyclase DDxxD/NDxxD motifs are not clearly identifiable by simple pattern matching in this sequence, making positive enzymatic classification from sequence alone difficult.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Elimination is partially possible: the N-terminal signal peptide and multiple hydrophobic TM-like segments make this incompatible with soluble translation machinery (A), folate-metabolizing enzymes (C), or purine-pathway enzymes (D). However, positively arriving at the pathway name 'Antifungal biosynthesis' requires knowing that this specific terpene cyclase (rstn5) belongs to the restricticin biosynthetic gene cluster and that UniProt assigns the pathway label 'Antifungal biosynthesis' rather than the more generic 'terpene biosynthesis' or 'secondary metabolite biosynthesis.' The DDxxD/NDxxD terpene-cyclase motifs are not unambiguously identifiable in this 349-aa sequence by casual inspection.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt pathway annotation 'Antifungal biosynthesis' for this terpene cyclase, which is a database-specific naming choice tied to the restricticin biosynthetic cluster (rstn5) and its CYP51-inhibitor product. Without this annotation, a reasoning model would more naturally propose 'terpene biosynthesis' or 'secondary metabolism' rather than the exact label 'Antifungal biosynthesis.'",
    "reason": "While general biological knowledge permits elimination of A, C, and D (the sequence clearly is not a ribosomal/elongation factor, folate enzyme, or purine enzyme), the positive identification of the specific pathway label 'Antifungal biosynthesis' depends on the UniProt annotation of this particular terpene cyclase. The pathway name is an annotation convention, not a self-evident deduction from sequence features alone."
  },
  "case_id": "pathway_0010",
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
    "reason": "UniProt entry P9WEG7 (sequence matched exactly, 349 AA) annotates this protein as 'Terpene cyclase rstn5' / 'Restricticin biosynthesis cluster protein 5' with PATHWAY: 'Antifungal biosynthesis' (ECO:0000269, experimental evidence from PubMed:33857369, a 2021 JACS paper on genome mining of CYP51-inhibitor biosynthetic gene clusters). The EC number 5.4.99.- (isomerase/cyclase) is consistent with a terpene cyclase. The antifungal designation derives from the biological activity of the product (restricticin inhibits CYP51, a fungal enzyme). The sequence match is exact in both current and historical (v2) records."
  },
  "important_caveats": [
    "The evidence code ECO:0000269 indicates experimental evidence, but the underlying experiment (2021 JACS paper) primarily involved genome mining, heterologous expression, and chemical characterization; the 'antifungal' label reflects the product's biological activity rather than a dedicated antifungal-pathway assay.",
    "The pathway name 'Antifungal biosynthesis' is a UniProt-specific annotation convention; the same enzyme could reasonably be placed under 'terpene biosynthesis' or 'natural product biosynthesis' in other databases.",
    "The UniProt entry was first public in Feb 2025; the author's source snapshot is unknown, but the sequence matches both current (v4) and historical (v2) records.",
    "The terpene cyclase DDxxD/NDxxD motifs are not clearly identifiable by simple pattern matching in this sequence, making positive enzymatic classification from sequence alone difficult."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors A (polypeptide chain elongation), C (tetrahydrofolate interconversion), and D (purine metabolism) are clearly incompatible with a membrane-associated terpene cyclase from a fungal secondary-metabolite gene cluster. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P9WEG7 (sequence matched exactly, 349 AA) annotates this protein as 'Terpene cyclase rstn5' / 'Restricticin biosynthesis cluster protein 5' with PATHWAY: 'Antifungal biosynthesis' (ECO:0000269, experimental evidence from PubMed:33857369, a 2021 JACS paper on genome mining of CYP51-inhibitor biosynthetic gene clusters). The EC number 5.4.99.- (isomerase/cyclase) is consistent with a terpene cyclase. The antifungal designation derives from the biological activity of the product (restricticin inhibits CYP51, a fungal enzyme). The sequence match is exact in both current and historical (v2) records.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Elimination is partially possible: the N-terminal signal peptide and multiple hydrophobic TM-like segments make this incompatible with soluble translation machinery (A), folate-metabolizing enzymes (C), or purine-pathway enzymes (D). However, positively arriving at the pathway name 'Antifungal biosynthesis' requires knowing that this specific terpene cyclase (rstn5) belongs to the restricticin biosynthetic gene cluster and that UniProt assigns the pathway label 'Antifungal biosynthesis' rather than the more generic 'terpene biosynthesis' or 'secondary metabolite biosynthesis.' The DDxxD/NDxxD terpene-cyclase motifs are not unambiguously identifiable in this 349-aa sequence by casual inspection.",
    "missing_item_specific_fact": "The specific UniProt pathway annotation 'Antifungal biosynthesis' for this terpene cyclase, which is a database-specific naming choice tied to the restricticin biosynthetic cluster (rstn5) and its CYP51-inhibitor product. Without this annotation, a reasoning model would more naturally propose 'terpene biosynthesis' or 'secondary metabolism' rather than the exact label 'Antifungal biosynthesis.'",
    "reason": "While general biological knowledge permits elimination of A, C, and D (the sequence clearly is not a ribosomal/elongation factor, folate enzyme, or purine enzyme), the positive identification of the specific pathway label 'Antifungal biosynthesis' depends on the UniProt annotation of this particular terpene cyclase. The pathway name is an annotation convention, not a self-evident deduction from sequence features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors A (polypeptide chain elongation), C (tetrahydrofolate interconversion), and D (purine metabolism) are clearly incompatible with a membrane-associated terpene cyclase from a fungal secondary-metabolite gene cluster. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The evidence code ECO:0000269 indicates experimental evidence, but the underlying experiment (2021 JACS paper) primarily involved genome mining, heterologous expression, and chemical characterization; the 'antifungal' label reflects the product's biological activity rather than a dedicated antifungal-pathway assay.",
    "The pathway name 'Antifungal biosynthesis' is a UniProt-specific annotation convention; the same enzyme could reasonably be placed under 'terpene biosynthesis' or 'natural product biosynthesis' in other databases.",
    "The UniProt entry was first public in Feb 2025; the author's source snapshot is unknown, but the sequence matches both current (v4) and historical (v2) records.",
    "The terpene cyclase DDxxD/NDxxD motifs are not clearly identifiable by simple pattern matching in this sequence, making positive enzymatic classification from sequence alone difficult."
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

**Accession:** `P9WEG7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
"P9WEG7"
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Eurotiomycetes","Eurotiomycetidae","Eurotiales","Aspergillaceae","Aspergillus","Circumdati"],"scientificName":"Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 / M93)","taxonId":1509407}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 5"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"5.4.99.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Terpene cyclase rstn5"}}}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"Antifungal biosynthesis"}]}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:17.512806+00:00.  

```json
{"citation":{"authors":["Liu N.","Abramyan E.D.","Cheng W.","Perlatti B.","Harvey C.J.B.","Bills G.F.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33857369"},{"database":"DOI","id":"10.1021/jacs.1c01516"}],"citationType":"journal article","firstPage":"6043","id":"33857369","journal":"J. Am. Chem. Soc.","lastPage":"6047","publicationDate":"2021","title":"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.","volume":"143"},"referenceNumber":2,"referencePositions":["FUNCTION","PATHWAY"]}
```

Source SHA-256: `cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
ID   RSTN5_ASPN3             Reviewed;         349 AA.
AC   P9WEG7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   09-APR-2025, entry version 2.
DE   RecName: Full=Terpene cyclase rstn5 {ECO:0000303|PubMed:33857369};
DE            EC=5.4.99.- {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 5 {ECO:0000303|PubMed:33857369};
GN   Name=rstn5 {ECO:0000303|PubMed:33857369};
OS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /
OS   M93).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=1509407;
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

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

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)  
**Locator:** `lines 47-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:21.947384+00:00.  

```text
CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000269|PubMed:33857369}.
```

Source SHA-256: `20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
