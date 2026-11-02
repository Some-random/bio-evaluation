# pathway_0014

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
MTLQPTAADVGAMYDQYTSLLTDVMAGFIHVGYWEDPSSEETMEVATERMTREVGARLSSSAGQHILDVGCGTGKSAVQIANTHGVQITGITVSKSQIEEAQALYGSAVQAGQVSYQFANAMDLPFADASFDGAYAIESLVHMDDRRTALQNIARVLRPGSRLAIADLCLDAHCPNPEALARFHELFQVPPMSSGEELQELLRETGFRVLEFTDIRDNVRPVCKFLEKKALSLEGEVGEKLLEIATSMATLKELGYAFITAERI

[Multiple Choices]
A. L-methionine biosynthesis via de novo pathway. .
B. Antifungal biosynthesis. .
C. tRNA modification
D. capsule polysaccharide biosynthesis. .
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

> The sequence exactly matches the UniProt record for a protein annotated as O-methyltransferase resE in the restricticin biosynthesis cluster, with the pathway listed as antifungal biosynthesis. The pathway annotation cites experimental evidence, though the underlying paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support an inference of a methyltransferase-like function, but that does not identify the specific biosynthetic pathway among the choices.


**Missing item-specific fact**

> The protein-specific association with restricticin/antifungal biosynthesis, established by annotation or experimental work, is absent from the input.


**Reason**

> Choosing B requires the specific pathway assignment for this protein; broad sequence-based functional inference does not distinguish it reliably from the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein record explicitly assigns the pathway to antifungal biosynthesis; no competing option is supported by the supplied sequence alone.


### Important caveats

- The reviewer-only database evidence supports the key but was not available to the evaluated model.
- The pathway annotation cites a publication with experimental evidence, but the primary study was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support an inference of a methyltransferase-like function, but that does not identify the specific biosynthetic pathway among the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific association with restricticin/antifungal biosynthesis, established by annotation or experimental work, is absent from the input.",
    "reason": "Choosing B requires the specific pathway assignment for this protein; broad sequence-based functional inference does not distinguish it reliably from the alternatives."
  },
  "case_id": "pathway_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record for a protein annotated as O-methyltransferase resE in the restricticin biosynthesis cluster, with the pathway listed as antifungal biosynthesis. The pathway annotation cites experimental evidence, though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The pathway annotation cites a publication with experimental evidence, but the primary study was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein record explicitly assigns the pathway to antifungal biosynthesis; no competing option is supported by the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record for a protein annotated as O-methyltransferase resE in the restricticin biosynthesis cluster, with the pathway listed as antifungal biosynthesis. The pathway annotation cites experimental evidence, though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support an inference of a methyltransferase-like function, but that does not identify the specific biosynthetic pathway among the choices.",
    "missing_item_specific_fact": "The protein-specific association with restricticin/antifungal biosynthesis, established by annotation or experimental work, is absent from the input.",
    "reason": "Choosing B requires the specific pathway assignment for this protein; broad sequence-based functional inference does not distinguish it reliably from the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein record explicitly assigns the pathway to antifungal biosynthesis; no competing option is supported by the supplied sequence alone."
  },
  "important_caveats": [
    "The reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The pathway annotation cites a publication with experimental evidence, but the primary study was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXV1 (RESE_ASPSL) for this exact 264-aa sequence carries a PATHWAY annotation of 'Antifungal biosynthesis' with evidence code ECO:0000269 (direct assay/experimental), citing PubMed:39105744 (Lu et al., 2024, J. Agric. Food Chem.). The protein is annotated as 'O-methyltransferase resE' / 'Restricticin biosynthesis cluster protein E' from Aspergillus sclerotiorum. The sequence match is exact (SHA-256 identical). The expected answer B directly corresponds to the database pathway annotation supported by experimental evidence.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could identify methyltransferase-like sequence motifs (e.g., the GCGTGK region suggestive of a SAM-binding Rossmann-like fold) and note the fungal origin, but the methyltransferase superfamily spans tRNA modification, secondary metabolite biosynthesis, lipid metabolism, and many other pathways. Distinguishing 'Antifungal biosynthesis' (a specific secondary metabolite cluster pathway) from 'tRNA modification' (C) or other methylation-dependent pathways requires knowing that this protein is resE in the restricticin biosynthetic gene cluster of A. sclerotiorum.


**Missing item-specific fact**

> The specific identity of this protein as resE, a member of the restricticin biosynthetic cluster, and the experimental demonstration (PubMed:39105744) that this cluster produces an antifungal/phytotoxic hybrid molecule. Without this protein-specific annotation or literature knowledge, the methyltransferase fold alone cannot distinguish antifungal secondary metabolite biosynthesis from tRNA modification or other methylation pathways.


**Reason**

> The sequence reveals a methyltransferase fold but does not encode pathway-specific information sufficient to select 'Antifungal biosynthesis' over 'tRNA modification' or other methyltransferase-associated pathways. Correct selection depends on recognizing this exact protein's role in the restricticin cluster, which is an item-specific database/literature fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> From sequence alone, the protein is identifiable as a SAM-dependent methyltransferase. Methyltransferases are prominent in tRNA modification pathways (option C), making C a superficially plausible alternative. Without knowing the restricticin cluster context, a model reasoning purely from sequence could not confidently eliminate C in favor of B. Option A (methionine biosynthesis) is less defensible because the sequence lacks hallmark features of Met biosynthesis enzymes (e.g., cobalamin-dependent methionine synthase domains, homoserine O-succinyltransferase motifs), and D (capsule polysaccharide biosynthesis) is poorly supported by methyltransferase fold features.


### Important caveats

- The UniProt pathway annotation uses ECO:0000269 (experimental/direct assay), lending stronger support than a purely computational annotation, but the underlying paper (Lu et al. 2024) describes a 'hybrid molecule with phytotoxic activity'—the categorization under 'Antifungal biosynthesis' reflects the biosynthetic cluster's function as characterized in that study.
- The entry was first public in February 2025; the author's data-construction snapshot is unknown. If the benchmark was constructed before this date, the annotation source may differ.
- The term 'Antifungal biosynthesis' is a UniProt-specific pathway category for secondary metabolite clusters with antifungal activity, not a standard KEGG/MetaCyc pathway name, which may affect general-knowledge reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could identify methyltransferase-like sequence motifs (e.g., the GCGTGK region suggestive of a SAM-binding Rossmann-like fold) and note the fungal origin, but the methyltransferase superfamily spans tRNA modification, secondary metabolite biosynthesis, lipid metabolism, and many other pathways. Distinguishing 'Antifungal biosynthesis' (a specific secondary metabolite cluster pathway) from 'tRNA modification' (C) or other methylation-dependent pathways requires knowing that this protein is resE in the restricticin biosynthetic gene cluster of A. sclerotiorum.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as resE, a member of the restricticin biosynthetic cluster, and the experimental demonstration (PubMed:39105744) that this cluster produces an antifungal/phytotoxic hybrid molecule. Without this protein-specific annotation or literature knowledge, the methyltransferase fold alone cannot distinguish antifungal secondary metabolite biosynthesis from tRNA modification or other methylation pathways.",
    "reason": "The sequence reveals a methyltransferase fold but does not encode pathway-specific information sufficient to select 'Antifungal biosynthesis' over 'tRNA modification' or other methyltransferase-associated pathways. Correct selection depends on recognizing this exact protein's role in the restricticin cluster, which is an item-specific database/literature fact."
  },
  "case_id": "pathway_0014",
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
    "reason": "The UniProt entry P0DXV1 (RESE_ASPSL) for this exact 264-aa sequence carries a PATHWAY annotation of 'Antifungal biosynthesis' with evidence code ECO:0000269 (direct assay/experimental), citing PubMed:39105744 (Lu et al., 2024, J. Agric. Food Chem.). The protein is annotated as 'O-methyltransferase resE' / 'Restricticin biosynthesis cluster protein E' from Aspergillus sclerotiorum. The sequence match is exact (SHA-256 identical). The expected answer B directly corresponds to the database pathway annotation supported by experimental evidence."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses ECO:0000269 (experimental/direct assay), lending stronger support than a purely computational annotation, but the underlying paper (Lu et al. 2024) describes a 'hybrid molecule with phytotoxic activity'—the categorization under 'Antifungal biosynthesis' reflects the biosynthetic cluster's function as characterized in that study.",
    "The entry was first public in February 2025; the author's data-construction snapshot is unknown. If the benchmark was constructed before this date, the annotation source may differ.",
    "The term 'Antifungal biosynthesis' is a UniProt-specific pathway category for secondary metabolite clusters with antifungal activity, not a standard KEGG/MetaCyc pathway name, which may affect general-knowledge reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "From sequence alone, the protein is identifiable as a SAM-dependent methyltransferase. Methyltransferases are prominent in tRNA modification pathways (option C), making C a superficially plausible alternative. Without knowing the restricticin cluster context, a model reasoning purely from sequence could not confidently eliminate C in favor of B. Option A (methionine biosynthesis) is less defensible because the sequence lacks hallmark features of Met biosynthesis enzymes (e.g., cobalamin-dependent methionine synthase domains, homoserine O-succinyltransferase motifs), and D (capsule polysaccharide biosynthesis) is poorly supported by methyltransferase fold features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXV1 (RESE_ASPSL) for this exact 264-aa sequence carries a PATHWAY annotation of 'Antifungal biosynthesis' with evidence code ECO:0000269 (direct assay/experimental), citing PubMed:39105744 (Lu et al., 2024, J. Agric. Food Chem.). The protein is annotated as 'O-methyltransferase resE' / 'Restricticin biosynthesis cluster protein E' from Aspergillus sclerotiorum. The sequence match is exact (SHA-256 identical). The expected answer B directly corresponds to the database pathway annotation supported by experimental evidence.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could identify methyltransferase-like sequence motifs (e.g., the GCGTGK region suggestive of a SAM-binding Rossmann-like fold) and note the fungal origin, but the methyltransferase superfamily spans tRNA modification, secondary metabolite biosynthesis, lipid metabolism, and many other pathways. Distinguishing 'Antifungal biosynthesis' (a specific secondary metabolite cluster pathway) from 'tRNA modification' (C) or other methylation-dependent pathways requires knowing that this protein is resE in the restricticin biosynthetic gene cluster of A. sclerotiorum.",
    "missing_item_specific_fact": "The specific identity of this protein as resE, a member of the restricticin biosynthetic cluster, and the experimental demonstration (PubMed:39105744) that this cluster produces an antifungal/phytotoxic hybrid molecule. Without this protein-specific annotation or literature knowledge, the methyltransferase fold alone cannot distinguish antifungal secondary metabolite biosynthesis from tRNA modification or other methylation pathways.",
    "reason": "The sequence reveals a methyltransferase fold but does not encode pathway-specific information sufficient to select 'Antifungal biosynthesis' over 'tRNA modification' or other methyltransferase-associated pathways. Correct selection depends on recognizing this exact protein's role in the restricticin cluster, which is an item-specific database/literature fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "From sequence alone, the protein is identifiable as a SAM-dependent methyltransferase. Methyltransferases are prominent in tRNA modification pathways (option C), making C a superficially plausible alternative. Without knowing the restricticin cluster context, a model reasoning purely from sequence could not confidently eliminate C in favor of B. Option A (methionine biosynthesis) is less defensible because the sequence lacks hallmark features of Met biosynthesis enzymes (e.g., cobalamin-dependent methionine synthase domains, homoserine O-succinyltransferase motifs), and D (capsule polysaccharide biosynthesis) is poorly supported by methyltransferase fold features."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses ECO:0000269 (experimental/direct assay), lending stronger support than a purely computational annotation, but the underlying paper (Lu et al. 2024) describes a 'hybrid molecule with phytotoxic activity'—the categorization under 'Antifungal biosynthesis' reflects the biosynthetic cluster's function as characterized in that study.",
    "The entry was first public in February 2025; the author's data-construction snapshot is unknown. If the benchmark was constructed before this date, the annotation source may differ.",
    "The term 'Antifungal biosynthesis' is a UniProt-specific pathway category for secondary metabolite clusters with antifungal activity, not a standard KEGG/MetaCyc pathway name, which may affect general-knowledge reasoning."
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

**Accession:** `P0DXV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.952467+00:00.  

```json
"P0DXV1"
```

Source SHA-256: `28f2208ebdc3c58c28d8c0bd9978354bcb775822363a3845e9d7dffaefd695cd`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV1.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.952467+00:00.  

```json
{"lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Eurotiomycetes","Eurotiomycetidae","Eurotiales","Aspergillaceae","Aspergillus","Circumdati"],"scientificName":"Aspergillus sclerotiorum","taxonId":138282}
```

Source SHA-256: `28f2208ebdc3c58c28d8c0bd9978354bcb775822363a3845e9d7dffaefd695cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.952467+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein E"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"O-methyltransferase resE"}}}
```

Source SHA-256: `28f2208ebdc3c58c28d8c0bd9978354bcb775822363a3845e9d7dffaefd695cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.952467+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39105744","source":"PubMed"}],"value":"Antifungal biosynthesis"}]}
```

Source SHA-256: `28f2208ebdc3c58c28d8c0bd9978354bcb775822363a3845e9d7dffaefd695cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.952467+00:00.  

```json
{"citation":{"authors":["Lu Y.","Li Y.","Dou M.","Liu D.","Lin W.","Fan A."],"citationCrossReferences":[{"database":"PubMed","id":"39105744"},{"database":"DOI","id":"10.1021/acs.jafc.4c04244"}],"citationType":"journal article","firstPage":"18520","id":"39105744","journal":"J. Agric. Food Chem.","lastPage":"18527","publicationDate":"2024","title":"Discovery of a hybrid molecule with phytotoxic activity by genome mining, heterologous expression, and OSMAC strategy.","volume":"72"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","PATHWAY"]}
```

Source SHA-256: `28f2208ebdc3c58c28d8c0bd9978354bcb775822363a3845e9d7dffaefd695cd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV1?format=txt&versions=4)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.445708+00:00.  

```text
ID   RESE_ASPSL              Reviewed;         264 AA.
AC   P0DXV1;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=O-methyltransferase resE {ECO:0000303|PubMed:39105744};
DE            EC=2.1.1.- {ECO:0000305|PubMed:39105744};
DE   AltName: Full=Restricticin biosynthesis cluster protein E {ECO:0000303|PubMed:39105744};
GN   Name=resE {ECO:0000303|PubMed:39105744};
OS   Aspergillus sclerotiorum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=138282;
```

Source SHA-256: `cd2e82952af8d3844a3a9c286440d6c646ca7af305696f06813c85a3b4406cf2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV1?format=txt&versions=4)  
**Locator:** `lines 15-21`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.445708+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.
RX   PubMed=39105744; DOI=10.1021/acs.jafc.4c04244;
RA   Lu Y., Li Y., Dou M., Liu D., Lin W., Fan A.;
RT   "Discovery of a hybrid molecule with phytotoxic activity by genome mining,
RT   heterologous expression, and OSMAC strategy.";
RL   J. Agric. Food Chem. 72:18520-18527(2024).
```

Source SHA-256: `cd2e82952af8d3844a3a9c286440d6c646ca7af305696f06813c85a3b4406cf2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV1?format=txt&versions=4)  
**Locator:** `lines 48-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.445708+00:00.  

```text
CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000269|PubMed:39105744}.
```

Source SHA-256: `cd2e82952af8d3844a3a9c286440d6c646ca7af305696f06813c85a3b4406cf2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
