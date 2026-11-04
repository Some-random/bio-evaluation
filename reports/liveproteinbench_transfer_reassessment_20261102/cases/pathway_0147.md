# pathway_0147

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0147.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSANTGKPARHYLISYPRTASNLLLKILALDSQPNFSSGGFDGGYFFMPADDILTDPRIRVRARSISDWTADERAQLKETFQACFEAQQRWLESAESQGQSVFVKEHTVFFADPTARSCLQFGPSATSEPAWTVEYAGGSTHSKLNITVLPDEFLLTWLPTFLIRHPALAFPSLYRTVIKREGKESAAADNFASLLTTVEWSRSLYDFYVQNRESLPCSPDQRLEWPIVLDADDIIAHPATVTLYCDKIGMDPRQLCFNWDQLKSEELSKIEPNQLAMRMSLYQSTGIDTSKSSRGINVDDEATKWRSEFGIAVADHIEKLVRGAMADYEYLRARRLRAD

[Multiple Choices]
A. Secondary metabolite biosynthesis. .
B. Alkaloid biosynthesis
C. pyruvate from D-glyceraldehyde 3-phosphate: step 2/5. .
D. ergot alkaloid biosynthesis. .
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record explicitly assigns the pathway as “Secondary metabolite biosynthesis,” citing a paper that reports function and pathway. This supports A as an annotation, though the excerpts do not independently establish the experimental basis or strength of that assignment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein’s specific association with the pyrrolopyrazine biosynthetic cluster and the pathway assignment for that cluster are not supplied by the sequence or choices.


**Reason**

> A sulfotransferase-like sequence could suggest modification of a metabolite, but that transferable clue does not meaningfully distinguish general secondary-metabolite biosynthesis from alkaloid biosynthesis, or identify an ergot-alkaloid pathway. Selecting the recorded pathway requires a target-specific pathway or cluster association.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Secondary-metabolite biosynthesis is a broad category that can include alkaloid biosynthesis. The choices do not say whether they are intended as mutually exclusive levels of pathway specificity; the supplied evidence supports A but does not resolve whether the more specific B label is also applicable.


### Important caveats

- The pathway excerpts are database annotations citing a paper; they are not themselves a direct experimental demonstration.
- The sequence-matched source identity and its annotations were reviewer-only, not original model inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein’s specific association with the pyrrolopyrazine biosynthetic cluster and the pathway assignment for that cluster are not supplied by the sequence or choices.",
    "reason": "A sulfotransferase-like sequence could suggest modification of a metabolite, but that transferable clue does not meaningfully distinguish general secondary-metabolite biosynthesis from alkaloid biosynthesis, or identify an ergot-alkaloid pathway. Selecting the recorded pathway requires a target-specific pathway or cluster association."
  },
  "case_id": "pathway_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record explicitly assigns the pathway as “Secondary metabolite biosynthesis,” citing a paper that reports function and pathway. This supports A as an annotation, though the excerpts do not independently establish the experimental basis or strength of that assignment."
  },
  "important_caveats": [
    "The pathway excerpts are database annotations citing a paper; they are not themselves a direct experimental demonstration.",
    "The sequence-matched source identity and its annotations were reviewer-only, not original model inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Secondary-metabolite biosynthesis is a broad category that can include alkaloid biosynthesis. The choices do not say whether they are intended as mutually exclusive levels of pathway specificity; the supplied evidence supports A but does not resolve whether the more specific B label is also applicable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record explicitly assigns the pathway as “Secondary metabolite biosynthesis,” citing a paper that reports function and pathway. This supports A as an annotation, though the excerpts do not independently establish the experimental basis or strength of that assignment.",
    "evidence_ids": ["C5", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein’s specific association with the pyrrolopyrazine biosynthetic cluster and the pathway assignment for that cluster are not supplied by the sequence or choices.",
    "reason": "A sulfotransferase-like sequence could suggest modification of a metabolite, but that transferable clue does not meaningfully distinguish general secondary-metabolite biosynthesis from alkaloid biosynthesis, or identify an ergot-alkaloid pathway. Selecting the recorded pathway requires a target-specific pathway or cluster association."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Secondary-metabolite biosynthesis is a broad category that can include alkaloid biosynthesis. The choices do not say whether they are intended as mutually exclusive levels of pathway specificity; the supplied evidence supports A but does not resolve whether the more specific B label is also applicable."
  },
  "important_caveats": [
    "The pathway excerpts are database annotations citing a paper; they are not themselves a direct experimental demonstration.",
    "The sequence-matched source identity and its annotations were reviewer-only, not original model inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A0A455ZLR3, Sulfotransferase ppzF from Metarhizium majus) explicitly states PATHWAY: Secondary metabolite biosynthesis, supported by evidence code ECO:0000305|PubMed:30452111. The protein is part of the pyrrolopyrazine biosynthesis gene cluster. The sequence matches the benchmark input exactly.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Options C and D can be partially eliminated by reasoning: C (pyruvate from G3P, glycolysis step) is incompatible with a fungal sulfotransferase, and D (ergot alkaloid biosynthesis) involves a very specific enzymatic cascade (LDMTS, C-8 prenyltransferase, etc.) in which sulfotransferases are not typical components. However, distinguishing A (Secondary metabolite biosynthesis) from B (Alkaloid biosynthesis) is not achievable by transferable knowledge: pyrrolopyrazine IS an alkaloid, so 'Alkaloid biosynthesis' is arguably equally or more accurate. The choice of 'Secondary metabolite biosynthesis' over 'Alkaloid biosynthesis' reflects UniProt's specific pathway-ontology annotation convention for this particular protein, not a biologically necessary distinction derivable from the sequence or general knowledge.


**Missing item-specific fact**

> The specific UniProt pathway-ontology term assigned to this protein ('Secondary metabolite biosynthesis' rather than 'Alkaloid biosynthesis'), which is a database annotation choice for this exact protein and not derivable from sequence features or general pathway knowledge, since pyrrolopyrazine is both a secondary metabolite and an alkaloid.


**Reason**

> While C and D can be reasonably excluded by general biological reasoning (sulfotransferases are not glycolytic enzymes; ergot alkaloid biosynthesis has a distinct enzymatic architecture), the A-vs-B distinction requires knowing the specific database annotation for this protein. Pyrrolopyrazine is an alkaloid, making B a defensible alternative. No sequence feature or family-level inference reliably forces the broader 'Secondary metabolite biosynthesis' term over the more specific 'Alkaloid biosynthesis' term without recalling this protein's UniProt record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Pyrrolopyrazine is both a secondary metabolite and an alkaloid. Option A ('Secondary metabolite biosynthesis') is the UniProt annotation, but option B ('Alkaloid biosynthesis') is biologically accurate since pyrrolopyrazine is structurally and biosynthetically an alkaloid. Without access to the specific UniProt pathway-ontology assignment, a knowledgeable model could reasonably select either A or B.


### Important caveats

- The UniProt pathway annotation uses 'Secondary metabolite biosynthesis' as a controlled-vocabulary term; this is a broad parent category in UniProt's pathway ontology, and the choice not to assign a more specific 'Alkaloid biosynthesis' term is an annotation convention rather than a biological exclusion.
- The PubMed reference (30452111, 2019) characterizing the pyrrolopyrazine cluster is the primary evidence for the pathway assignment; the annotation is based on gene-cluster context and functional characterization, not solely on sequence features of ppzF.
- The protein's sulfotransferase activity (EC 2.8.2.-) is consistent with secondary metabolism but does not by itself specify which secondary metabolite pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options C and D can be partially eliminated by reasoning: C (pyruvate from G3P, glycolysis step) is incompatible with a fungal sulfotransferase, and D (ergot alkaloid biosynthesis) involves a very specific enzymatic cascade (LDMTS, C-8 prenyltransferase, etc.) in which sulfotransferases are not typical components. However, distinguishing A (Secondary metabolite biosynthesis) from B (Alkaloid biosynthesis) is not achievable by transferable knowledge: pyrrolopyrazine IS an alkaloid, so 'Alkaloid biosynthesis' is arguably equally or more accurate. The choice of 'Secondary metabolite biosynthesis' over 'Alkaloid biosynthesis' reflects UniProt's specific pathway-ontology annotation convention for this particular protein, not a biologically necessary distinction derivable from the sequence or general knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt pathway-ontology term assigned to this protein ('Secondary metabolite biosynthesis' rather than 'Alkaloid biosynthesis'), which is a database annotation choice for this exact protein and not derivable from sequence features or general pathway knowledge, since pyrrolopyrazine is both a secondary metabolite and an alkaloid.",
    "reason": "While C and D can be reasonably excluded by general biological reasoning (sulfotransferases are not glycolytic enzymes; ergot alkaloid biosynthesis has a distinct enzymatic architecture), the A-vs-B distinction requires knowing the specific database annotation for this protein. Pyrrolopyrazine is an alkaloid, making B a defensible alternative. No sequence feature or family-level inference reliably forces the broader 'Secondary metabolite biosynthesis' term over the more specific 'Alkaloid biosynthesis' term without recalling this protein's UniProt record."
  },
  "case_id": "pathway_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A455ZLR3, Sulfotransferase ppzF from Metarhizium majus) explicitly states PATHWAY: Secondary metabolite biosynthesis, supported by evidence code ECO:0000305|PubMed:30452111. The protein is part of the pyrrolopyrazine biosynthesis gene cluster. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses 'Secondary metabolite biosynthesis' as a controlled-vocabulary term; this is a broad parent category in UniProt's pathway ontology, and the choice not to assign a more specific 'Alkaloid biosynthesis' term is an annotation convention rather than a biological exclusion.",
    "The PubMed reference (30452111, 2019) characterizing the pyrrolopyrazine cluster is the primary evidence for the pathway assignment; the annotation is based on gene-cluster context and functional characterization, not solely on sequence features of ppzF.",
    "The protein's sulfotransferase activity (EC 2.8.2.-) is consistent with secondary metabolism but does not by itself specify which secondary metabolite pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Pyrrolopyrazine is both a secondary metabolite and an alkaloid. Option A ('Secondary metabolite biosynthesis') is the UniProt annotation, but option B ('Alkaloid biosynthesis') is biologically accurate since pyrrolopyrazine is structurally and biosynthetically an alkaloid. Without access to the specific UniProt pathway-ontology assignment, a knowledgeable model could reasonably select either A or B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A455ZLR3, Sulfotransferase ppzF from Metarhizium majus) explicitly states PATHWAY: Secondary metabolite biosynthesis, supported by evidence code ECO:0000305|PubMed:30452111. The protein is part of the pyrrolopyrazine biosynthesis gene cluster. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Options C and D can be partially eliminated by reasoning: C (pyruvate from G3P, glycolysis step) is incompatible with a fungal sulfotransferase, and D (ergot alkaloid biosynthesis) involves a very specific enzymatic cascade (LDMTS, C-8 prenyltransferase, etc.) in which sulfotransferases are not typical components. However, distinguishing A (Secondary metabolite biosynthesis) from B (Alkaloid biosynthesis) is not achievable by transferable knowledge: pyrrolopyrazine IS an alkaloid, so 'Alkaloid biosynthesis' is arguably equally or more accurate. The choice of 'Secondary metabolite biosynthesis' over 'Alkaloid biosynthesis' reflects UniProt's specific pathway-ontology annotation convention for this particular protein, not a biologically necessary distinction derivable from the sequence or general knowledge.",
    "missing_item_specific_fact": "The specific UniProt pathway-ontology term assigned to this protein ('Secondary metabolite biosynthesis' rather than 'Alkaloid biosynthesis'), which is a database annotation choice for this exact protein and not derivable from sequence features or general pathway knowledge, since pyrrolopyrazine is both a secondary metabolite and an alkaloid.",
    "reason": "While C and D can be reasonably excluded by general biological reasoning (sulfotransferases are not glycolytic enzymes; ergot alkaloid biosynthesis has a distinct enzymatic architecture), the A-vs-B distinction requires knowing the specific database annotation for this protein. Pyrrolopyrazine is an alkaloid, making B a defensible alternative. No sequence feature or family-level inference reliably forces the broader 'Secondary metabolite biosynthesis' term over the more specific 'Alkaloid biosynthesis' term without recalling this protein's UniProt record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Pyrrolopyrazine is both a secondary metabolite and an alkaloid. Option A ('Secondary metabolite biosynthesis') is the UniProt annotation, but option B ('Alkaloid biosynthesis') is biologically accurate since pyrrolopyrazine is structurally and biosynthetically an alkaloid. Without access to the specific UniProt pathway-ontology assignment, a knowledgeable model could reasonably select either A or B."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses 'Secondary metabolite biosynthesis' as a controlled-vocabulary term; this is a broad parent category in UniProt's pathway ontology, and the choice not to assign a more specific 'Alkaloid biosynthesis' term is an annotation convention rather than a biological exclusion.",
    "The PubMed reference (30452111, 2019) characterizing the pyrrolopyrazine cluster is the primary evidence for the pathway assignment; the annotation is based on gene-cluster context and functional characterization, not solely on sequence features of ppzF.",
    "The protein's sulfotransferase activity (EC 2.8.2.-) is consistent with secondary metabolism but does not by itself specify which secondary metabolite pathway."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 340,
  "benchmark_sequence_sha256": "e316590a6f1ebb768b4cd2ae53d0b5fb1deefd8c6c5ffb22c77db65f75c3048a",
  "current_entry_audit": {
    "entryVersion": 11,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 340,
  "current_source_sequence_sha256": "e316590a6f1ebb768b4cd2ae53d0b5fb1deefd8c6c5ffb22c77db65f75c3048a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 10,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A455ZLR3",
  "selected_historical_entry_version": 10,
  "selected_historical_record_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "selected_historical_source_sequence_length": 340,
  "selected_historical_source_sequence_sha256": "e316590a6f1ebb768b4cd2ae53d0b5fb1deefd8c6c5ffb22c77db65f75c3048a",
  "selected_historical_version": {
    "accession": "A0A455ZLR3",
    "database": "Swiss-Prot",
    "entryVersion": 10,
    "firstRelease": "2025_02/2025_02",
    "firstReleaseDate": "23-Apr-2025",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PPZF_METMF",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZLR3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":11,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein F\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"2.8.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Sulfotransferase ppzF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H1",
  "excerpt": "ID   PPZF_METMF              Reviewed;         340 AA.\nAC   A0A455ZLR3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   09-APR-2025, entry version 10.\nDE   RecName: Full=Sulfotransferase ppzF {ECO:0000303|PubMed:30452111};\nDE            EC=2.8.2.- {ECO:0000305|PubMed:30452111};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein F {ECO:0000303|PubMed:30452111};\nGN   Name=ppzF {ECO:0000303|PubMed:30452111};\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:19.015576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:19.015576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000305|PubMed:30452111}.\nCC   ---------------------------------------------------------------------------\nCC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms\nCC   Distributed under the Creative Commons Attribution (CC BY 4.0) License\nCC   ---------------------------------------------------------------------------\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:19.015576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
