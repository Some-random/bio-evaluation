# pathway_0155

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
MSLQPTATEVGTMYDQYTSLLTDVMAGFIHVGYWDDPEREDTIEVATERLTREIGERLSSVRGQRILDVGCGTGKSAVQIATAHDVHITGITVSNHQIELAQSQYESNTKAGQVNFLFANAMDLPFADASFDGAYAIESLVHMDDRRTALTNIARVLRPGSRLAIADLFLDAGCPNPEVLARFHELFQVPPMPSGDDLKALLHQTGFKVIEFTDIRDTSGLSANF

[Multiple Choices]
A. L-fucose degradation. .
B. Antifungal biosynthesis. .
C. chorismate biosynthesis
D. L-homoserine from L-aspartate: step 2/3. .
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

> The sequence matches the UniProt record for an O-methyltransferase in the restricticin biosynthesis cluster, which annotates its pathway as antifungal biosynthesis. The pathway annotation cites experimental evidence, although the underlying paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a methyltransferase, but that alone does not establish which specific biosynthetic pathway it serves.


**Missing item-specific fact**

> The protein's association with the restricticin/antifungal biosynthetic cluster and its pathway annotation.


**Reason**

> Distinguishing antifungal biosynthesis from the listed alternatives requires protein-specific pathway knowledge absent from the sequence and choices; recognizing the exact database entry would be lookup or memorization, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched, cited pathway annotation supports choice B; the supplied evidence does not identify another listed option as a pathway for this protein.


### Important caveats

- The database record and sequence match support the expected answer, but the primary study was not independently examined.
- Reviewer-only accession and annotation information was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a methyltransferase, but that alone does not establish which specific biosynthetic pathway it serves.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's association with the restricticin/antifungal biosynthetic cluster and its pathway annotation.",
    "reason": "Distinguishing antifungal biosynthesis from the listed alternatives requires protein-specific pathway knowledge absent from the sequence and choices; recognizing the exact database entry would be lookup or memorization, not sequence-based reasoning."
  },
  "case_id": "pathway_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record for an O-methyltransferase in the restricticin biosynthesis cluster, which annotates its pathway as antifungal biosynthesis. The pathway annotation cites experimental evidence, although the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The database record and sequence match support the expected answer, but the primary study was not independently examined.",
    "Reviewer-only accession and annotation information was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched, cited pathway annotation supports choice B; the supplied evidence does not identify another listed option as a pathway for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record for an O-methyltransferase in the restricticin biosynthesis cluster, which annotates its pathway as antifungal biosynthesis. The pathway annotation cites experimental evidence, although the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a methyltransferase, but that alone does not establish which specific biosynthetic pathway it serves.",
    "missing_item_specific_fact": "The protein's association with the restricticin/antifungal biosynthetic cluster and its pathway annotation.",
    "reason": "Distinguishing antifungal biosynthesis from the listed alternatives requires protein-specific pathway knowledge absent from the sequence and choices; recognizing the exact database entry would be lookup or memorization, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched, cited pathway annotation supports choice B; the supplied evidence does not identify another listed option as a pathway for this protein."
  },
  "important_caveats": [
    "The database record and sequence match support the expected answer, but the primary study was not independently examined.",
    "Reviewer-only accession and annotation information was not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0L1JF88 (RSTN1_ASPN3) matches the supplied 225-aa sequence exactly (SHA256 confirmed). The entry carries an explicit PATHWAY annotation 'Antifungal biosynthesis' with evidence code ECO:0000269 (inferred from direct assay) from PubMed 33857369 (Liu et al., JACS 2021). The protein is annotated as O-methyltransferase rstn1 / Restricticin biosynthesis cluster protein 1 (EC 2.1.1.-), a component of the restricticin biosynthetic gene cluster in Aspergillus nomiae. Choice B matches the curated pathway annotation precisely.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a 'GCGTGKSAV' motif (GxGxG) characteristic of Rossmann-fold methyltransferases, which could narrow the enzymatic class. However, methyltransferases participate in dozens of pathways. None of the four pathway choices can be uniquely inferred from the sequence alone: the motif does not encode information about restricticin biosynthesis, antifungal secondary metabolism, or the specific biosynthetic gene cluster. Distinguishing 'Antifungal biosynthesis' from 'L-fucose degradation' or 'chorismate biosynthesis' requires knowing that this particular methyltransferase (Rstn1) is a member of the restricticin BGC in Aspergillus nomiae.


**Missing item-specific fact**

> The specific identity of this protein as Rstn1, a methyltransferase within the restricticin (an antifungal CYP51-inhibitor) biosynthetic gene cluster of Aspergillus nomiae, as characterized experimentally in Liu et al. 2021 (JACS 143:6043-6047). Without this protein-specific annotation, the sequence provides no pathway-level discriminant among the four choices.


**Reason**

> General biological knowledge can identify the protein as a methyltransferase from the GCGTGKSAV motif, but cannot assign it to 'Antifungal biosynthesis' rather than any other pathway. The correct answer depends on recalling or looking up the specific UniProt/functional annotation of this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the specific UniProt annotation, only B is correct. The other three choices (L-fucose degradation, chorismate biosynthesis, L-homoserine from L-aspartate step 2/3) describe primary metabolic pathways whose canonical enzymes (kinases, dehydrogenases, aldolases, dehydratases) are mechanistically and structurally distinct from an O-methyltransferase of this size and fold. No other option is defensible once the protein's true identity is known.


### Important caveats

- The pathway annotation 'Antifungal biosynthesis' is a UniProt-curated category applied to secondary-metabolite BGCs producing antifungal compounds; it is not a standard KEGG or MetaCyc pathway name, which may confuse models expecting canonical pathway nomenclature.
- The evidence code ECO:0000269 indicates experimental support (direct assay from the 2021 JACS paper), not purely computational transfer.
- The evaluated model receives only the raw sequence and four choices; the UniProt accession, organism, and gene name are absent from the input.
- The entry was first released in Swiss-Prot on 2025-02-05; whether the benchmark authors had access to this annotation at construction time is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a 'GCGTGKSAV' motif (GxGxG) characteristic of Rossmann-fold methyltransferases, which could narrow the enzymatic class. However, methyltransferases participate in dozens of pathways. None of the four pathway choices can be uniquely inferred from the sequence alone: the motif does not encode information about restricticin biosynthesis, antifungal secondary metabolism, or the specific biosynthetic gene cluster. Distinguishing 'Antifungal biosynthesis' from 'L-fucose degradation' or 'chorismate biosynthesis' requires knowing that this particular methyltransferase (Rstn1) is a member of the restricticin BGC in Aspergillus nomiae.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as Rstn1, a methyltransferase within the restricticin (an antifungal CYP51-inhibitor) biosynthetic gene cluster of Aspergillus nomiae, as characterized experimentally in Liu et al. 2021 (JACS 143:6043-6047). Without this protein-specific annotation, the sequence provides no pathway-level discriminant among the four choices.",
    "reason": "General biological knowledge can identify the protein as a methyltransferase from the GCGTGKSAV motif, but cannot assign it to 'Antifungal biosynthesis' rather than any other pathway. The correct answer depends on recalling or looking up the specific UniProt/functional annotation of this particular protein."
  },
  "case_id": "pathway_0155",
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
    "reason": "UniProt entry A0A0L1JF88 (RSTN1_ASPN3) matches the supplied 225-aa sequence exactly (SHA256 confirmed). The entry carries an explicit PATHWAY annotation 'Antifungal biosynthesis' with evidence code ECO:0000269 (inferred from direct assay) from PubMed 33857369 (Liu et al., JACS 2021). The protein is annotated as O-methyltransferase rstn1 / Restricticin biosynthesis cluster protein 1 (EC 2.1.1.-), a component of the restricticin biosynthetic gene cluster in Aspergillus nomiae. Choice B matches the curated pathway annotation precisely."
  },
  "important_caveats": [
    "The pathway annotation 'Antifungal biosynthesis' is a UniProt-curated category applied to secondary-metabolite BGCs producing antifungal compounds; it is not a standard KEGG or MetaCyc pathway name, which may confuse models expecting canonical pathway nomenclature.",
    "The evidence code ECO:0000269 indicates experimental support (direct assay from the 2021 JACS paper), not purely computational transfer.",
    "The evaluated model receives only the raw sequence and four choices; the UniProt accession, organism, and gene name are absent from the input.",
    "The entry was first released in Swiss-Prot on 2025-02-05; whether the benchmark authors had access to this annotation at construction time is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the specific UniProt annotation, only B is correct. The other three choices (L-fucose degradation, chorismate biosynthesis, L-homoserine from L-aspartate step 2/3) describe primary metabolic pathways whose canonical enzymes (kinases, dehydrogenases, aldolases, dehydratases) are mechanistically and structurally distinct from an O-methyltransferase of this size and fold. No other option is defensible once the protein's true identity is known."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0L1JF88 (RSTN1_ASPN3) matches the supplied 225-aa sequence exactly (SHA256 confirmed). The entry carries an explicit PATHWAY annotation 'Antifungal biosynthesis' with evidence code ECO:0000269 (inferred from direct assay) from PubMed 33857369 (Liu et al., JACS 2021). The protein is annotated as O-methyltransferase rstn1 / Restricticin biosynthesis cluster protein 1 (EC 2.1.1.-), a component of the restricticin biosynthetic gene cluster in Aspergillus nomiae. Choice B matches the curated pathway annotation precisely.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a 'GCGTGKSAV' motif (GxGxG) characteristic of Rossmann-fold methyltransferases, which could narrow the enzymatic class. However, methyltransferases participate in dozens of pathways. None of the four pathway choices can be uniquely inferred from the sequence alone: the motif does not encode information about restricticin biosynthesis, antifungal secondary metabolism, or the specific biosynthetic gene cluster. Distinguishing 'Antifungal biosynthesis' from 'L-fucose degradation' or 'chorismate biosynthesis' requires knowing that this particular methyltransferase (Rstn1) is a member of the restricticin BGC in Aspergillus nomiae.",
    "missing_item_specific_fact": "The specific identity of this protein as Rstn1, a methyltransferase within the restricticin (an antifungal CYP51-inhibitor) biosynthetic gene cluster of Aspergillus nomiae, as characterized experimentally in Liu et al. 2021 (JACS 143:6043-6047). Without this protein-specific annotation, the sequence provides no pathway-level discriminant among the four choices.",
    "reason": "General biological knowledge can identify the protein as a methyltransferase from the GCGTGKSAV motif, but cannot assign it to 'Antifungal biosynthesis' rather than any other pathway. The correct answer depends on recalling or looking up the specific UniProt/functional annotation of this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the specific UniProt annotation, only B is correct. The other three choices (L-fucose degradation, chorismate biosynthesis, L-homoserine from L-aspartate step 2/3) describe primary metabolic pathways whose canonical enzymes (kinases, dehydrogenases, aldolases, dehydratases) are mechanistically and structurally distinct from an O-methyltransferase of this size and fold. No other option is defensible once the protein's true identity is known."
  },
  "important_caveats": [
    "The pathway annotation 'Antifungal biosynthesis' is a UniProt-curated category applied to secondary-metabolite BGCs producing antifungal compounds; it is not a standard KEGG or MetaCyc pathway name, which may confuse models expecting canonical pathway nomenclature.",
    "The evidence code ECO:0000269 indicates experimental support (direct assay from the 2021 JACS paper), not purely computational transfer.",
    "The evaluated model receives only the raw sequence and four choices; the UniProt accession, organism, and gene name are absent from the input.",
    "The entry was first released in Swiss-Prot on 2025-02-05; whether the benchmark authors had access to this annotation at construction time is unknown."
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

**Accession:** `A0A0L1JF88` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 23. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF88.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:15.624587+00:00.  

```json
"A0A0L1JF88"
```

Source SHA-256: `dda8c813658a8c709826544ad5ddbd2ae972d7bfe23bb0ae87e41d05627a6d20`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF88.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:15.624587+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"O-methyltransferase rstn1"}}}
```

Source SHA-256: `dda8c813658a8c709826544ad5ddbd2ae972d7bfe23bb0ae87e41d05627a6d20`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF88.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:15.624587+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"Antifungal biosynthesis"}]}
```

Source SHA-256: `dda8c813658a8c709826544ad5ddbd2ae972d7bfe23bb0ae87e41d05627a6d20`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF88.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:15.624587+00:00.  

```json
{"citation":{"authors":["Liu N.","Abramyan E.D.","Cheng W.","Perlatti B.","Harvey C.J.B.","Bills G.F.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33857369"},{"database":"DOI","id":"10.1021/jacs.1c01516"}],"citationType":"journal article","firstPage":"6043","id":"33857369","journal":"J. Am. Chem. Soc.","lastPage":"6047","publicationDate":"2021","title":"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.","volume":"143"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `dda8c813658a8c709826544ad5ddbd2ae972d7bfe23bb0ae87e41d05627a6d20`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF88?format=txt&versions=23)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:17.437797+00:00.  

```text
ID   RSTN1_ASPN3             Reviewed;         225 AA.
AC   A0A0L1JF88;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-NOV-2015, sequence version 1.
DT   28-JAN-2026, entry version 23.
DE   RecName: Full=O-methyltransferase rstn1 {ECO:0000303|PubMed:33857369};
DE            EC=2.1.1.- {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};
GN   Name=rstn1 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001442;
OS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /
OS   M93).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=1509407;
```

Source SHA-256: `79e66fc3e8c4ef26bf02567903ff65dcc83c5c855359b04ab315caa7a97c6612`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF88?format=txt&versions=23)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:17.437797+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RX   PubMed=33857369; DOI=10.1021/jacs.1c01516;
RA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,
RA   Tang Y.;
RT   "Targeted genome mining reveals the biosynthetic gene clusters of natural
RT   product CYP51 inhibitors.";
RL   J. Am. Chem. Soc. 143:6043-6047(2021).
```

Source SHA-256: `79e66fc3e8c4ef26bf02567903ff65dcc83c5c855359b04ab315caa7a97c6612`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF88?format=txt&versions=23)  
**Locator:** `lines 60-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:24:17.437797+00:00.  

```text
CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000269|PubMed:33857369}.
```

Source SHA-256: `79e66fc3e8c4ef26bf02567903ff65dcc83c5c855359b04ab315caa7a97c6612`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 155. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
