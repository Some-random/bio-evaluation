# pathway_0171

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0171.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPARKYKIHVPCTSANIGPGFDVCGIALSLSLSLVVTIPSVSSGAEPLPKIIYTGLDSDNVPLSPYKNLLTRVALYVLRANGITTFPPGVTIEARNEIPFGRGLGSSGAAVIAGVLLGDLLGNLSLPKSRLLDFALMVERHPDNVTAALMGGFVGSYLRELSPEDMSAASIPLAEVLPEYPPDAGPDWGKSPPQPPHGIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARSPPDPDLIYDAMGDRVHQPYRMTLIPGLPKILSTLTPTSHPGLLGICLSGAGPTILALATHNFEAIANEIERIFGDEQVLVDHKVLNIDEKGSWVEDITEA

[Multiple Choices]
A. L-histidine biosynthesis
B. Amino-acid biosynthesis
C. L-homoserine from L-aspartate: step 2/3. .
D. dTTP biosynthesis. .
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

> The historical UniProt record matching the supplied sequence annotates it in amino-acid biosynthesis, specifically threonine biosynthesis, and identifies the step as 4/5. That supports the broad choice B; choice C describes a different, earlier pathway segment.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a homoserine-kinase-family metabolic enzyme. Transferable knowledge of this family links homoserine phosphorylation to threonine biosynthesis, an amino-acid biosynthetic pathway. Thus B is meaningfully favored over histidine biosynthesis (A) and dTTP biosynthesis (D). Choice C refers to making homoserine from aspartate, an earlier pathway segment rather than the homoserine-kinase reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference and the known role of homoserine kinase distinguish the broad amino-acid-biosynthesis option from the alternatives; the exact target's database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the only offered choice that encompasses the relevant threonine-biosynthesis function; C names a different pathway segment.


### Important caveats

- The reviewer-only record supports the key and matches the sequence, but its annotation is not itself an independent examination of the cited primary study.
- The exact pathway assignment is more specific than the offered correct choice, which is the broad category amino-acid biosynthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a homoserine-kinase-family metabolic enzyme. Transferable knowledge of this family links homoserine phosphorylation to threonine biosynthesis, an amino-acid biosynthetic pathway. Thus B is meaningfully favored over histidine biosynthesis (A) and dTTP biosynthesis (D). Choice C refers to making homoserine from aspartate, an earlier pathway segment rather than the homoserine-kinase reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference and the known role of homoserine kinase distinguish the broad amino-acid-biosynthesis option from the alternatives; the exact target's database record is not necessary."
  },
  "case_id": "pathway_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The historical UniProt record matching the supplied sequence annotates it in amino-acid biosynthesis, specifically threonine biosynthesis, and identifies the step as 4/5. That supports the broad choice B; choice C describes a different, earlier pathway segment."
  },
  "important_caveats": [
    "The reviewer-only record supports the key and matches the sequence, but its annotation is not itself an independent examination of the cited primary study.",
    "The exact pathway assignment is more specific than the offered correct choice, which is the broad category amino-acid biosynthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only offered choice that encompasses the relevant threonine-biosynthesis function; C names a different pathway segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The historical UniProt record matching the supplied sequence annotates it in amino-acid biosynthesis, specifically threonine biosynthesis, and identifies the step as 4/5. That supports the broad choice B; choice C describes a different, earlier pathway segment.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a homoserine-kinase-family metabolic enzyme. Transferable knowledge of this family links homoserine phosphorylation to threonine biosynthesis, an amino-acid biosynthetic pathway. Thus B is meaningfully favored over histidine biosynthesis (A) and dTTP biosynthesis (D). Choice C refers to making homoserine from aspartate, an earlier pathway segment rather than the homoserine-kinase reaction.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference and the known role of homoserine kinase distinguish the broad amino-acid-biosynthesis option from the alternatives; the exact target's database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only offered choice that encompasses the relevant threonine-biosynthesis function; C names a different pathway segment."
  },
  "important_caveats": [
    "The reviewer-only record supports the key and matches the sequence, but its annotation is not itself an independent examination of the cited primary study.",
    "The exact pathway assignment is more specific than the offered correct choice, which is the broad category amino-acid biosynthesis."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for J9VU26 (Homoserine kinase, EC 2.7.1.39) states the pathway as 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 4/5.' Option B ('Amino-acid biosynthesis') is the top-level pathway category from this annotation. The sequence matches the UniProt entry exactly. The annotation is experimentally supported (ECO:0000269, PubMed:18757810, Kingsbury & McCusker 2008).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains kinase-like motifs (e.g., the conserved kinase domain region 'GIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARSPPDPDLIYDAMGDRVHQPYRMTLIPGLPKILSTLTPTSHPGLLGICLSGAGPTILALATHNFEAIANEIERIFGDEQVLVDHKVLNIDEKGSWVEDITEA'). A model recognizing this as a kinase acting on an amino-acid intermediate can apply the general biochemical principle: a kinase that phosphorylates homoserine (consuming it as substrate) is NOT in the pathway that produces homoserine from aspartate (option C: 'L-homoserine from L-aspartate: step 2/3'), but rather in a downstream pathway. The phosphorylation of homoserine to O-phospho-homoserine is part of threonine biosynthesis, which falls under the broad category 'Amino-acid biosynthesis' (option B). Options A (histidine) and D (dTTP) are eliminated because the kinase context and amino-acid substrate specificity are inconsistent with purine/nucleotide or histidine pathways. Thus, from general knowledge of kinase biochemistry and amino-acid pathway logic, B is distinguishable from C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The inference relies on the general principle that a kinase acting on a metabolite as substrate is in a downstream pathway, not in the pathway producing that metabolite. This is transferable biochemical knowledge applicable to any homoserine kinase, not specific to this protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C ('L-homoserine from L-aspartate: step 2/3') refers to the pathway producing homoserine (catalyzed by aspartate semialdehyde dehydrogenase/homoserine dehydrogenase), which is biochemically distinct from and upstream of homoserine kinase activity. Option B is the correct broad pathway category. No other option is defensible.


### Important caveats

- The author's answer B ('Amino-acid biosynthesis') is the top-level UniProt pathway category. The more specific annotation is 'L-threonine biosynthesis; L-threonine from L-aspartate: step 4/5,' which is not offered as an option.
- Option C is a near-miss distractor that names homoserine but refers to the wrong pathway direction (producing homoserine rather than consuming it via phosphorylation).
- The UniProt EC assignment (2.7.1.39) is based on similarity (ECO:0000250, source P17423), while the pathway annotation is experimentally supported (ECO:0000269, PubMed:18757810).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains kinase-like motifs (e.g., the conserved kinase domain region 'GIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARSPPDPDLIYDAMGDRVHQPYRMTLIPGLPKILSTLTPTSHPGLLGICLSGAGPTILALATHNFEAIANEIERIFGDEQVLVDHKVLNIDEKGSWVEDITEA'). A model recognizing this as a kinase acting on an amino-acid intermediate can apply the general biochemical principle: a kinase that phosphorylates homoserine (consuming it as substrate) is NOT in the pathway that produces homoserine from aspartate (option C: 'L-homoserine from L-aspartate: step 2/3'), but rather in a downstream pathway. The phosphorylation of homoserine to O-phospho-homoserine is part of threonine biosynthesis, which falls under the broad category 'Amino-acid biosynthesis' (option B). Options A (histidine) and D (dTTP) are eliminated because the kinase context and amino-acid substrate specificity are inconsistent with purine/nucleotide or histidine pathways. Thus, from general knowledge of kinase biochemistry and amino-acid pathway logic, B is distinguishable from C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on the general principle that a kinase acting on a metabolite as substrate is in a downstream pathway, not in the pathway producing that metabolite. This is transferable biochemical knowledge applicable to any homoserine kinase, not specific to this protein's database record."
  },
  "case_id": "pathway_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for J9VU26 (Homoserine kinase, EC 2.7.1.39) states the pathway as 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 4/5.' Option B ('Amino-acid biosynthesis') is the top-level pathway category from this annotation. The sequence matches the UniProt entry exactly. The annotation is experimentally supported (ECO:0000269, PubMed:18757810, Kingsbury & McCusker 2008)."
  },
  "important_caveats": [
    "The author's answer B ('Amino-acid biosynthesis') is the top-level UniProt pathway category. The more specific annotation is 'L-threonine biosynthesis; L-threonine from L-aspartate: step 4/5,' which is not offered as an option.",
    "Option C is a near-miss distractor that names homoserine but refers to the wrong pathway direction (producing homoserine rather than consuming it via phosphorylation).",
    "The UniProt EC assignment (2.7.1.39) is based on similarity (ECO:0000250, source P17423), while the pathway annotation is experimentally supported (ECO:0000269, PubMed:18757810)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C ('L-homoserine from L-aspartate: step 2/3') refers to the pathway producing homoserine (catalyzed by aspartate semialdehyde dehydrogenase/homoserine dehydrogenase), which is biochemically distinct from and upstream of homoserine kinase activity. Option B is the correct broad pathway category. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for J9VU26 (Homoserine kinase, EC 2.7.1.39) states the pathway as 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 4/5.' Option B ('Amino-acid biosynthesis') is the top-level pathway category from this annotation. The sequence matches the UniProt entry exactly. The annotation is experimentally supported (ECO:0000269, PubMed:18757810, Kingsbury & McCusker 2008).",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains kinase-like motifs (e.g., the conserved kinase domain region 'GIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARSPPDPDLIYDAMGDRVHQPYRMTLIPGLPKILSTLTPTSHPGLLGICLSGAGPTILALATHNFEAIANEIERIFGDEQVLVDHKVLNIDEKGSWVEDITEA'). A model recognizing this as a kinase acting on an amino-acid intermediate can apply the general biochemical principle: a kinase that phosphorylates homoserine (consuming it as substrate) is NOT in the pathway that produces homoserine from aspartate (option C: 'L-homoserine from L-aspartate: step 2/3'), but rather in a downstream pathway. The phosphorylation of homoserine to O-phospho-homoserine is part of threonine biosynthesis, which falls under the broad category 'Amino-acid biosynthesis' (option B). Options A (histidine) and D (dTTP) are eliminated because the kinase context and amino-acid substrate specificity are inconsistent with purine/nucleotide or histidine pathways. Thus, from general knowledge of kinase biochemistry and amino-acid pathway logic, B is distinguishable from C.",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on the general principle that a kinase acting on a metabolite as substrate is in a downstream pathway, not in the pathway producing that metabolite. This is transferable biochemical knowledge applicable to any homoserine kinase, not specific to this protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C ('L-homoserine from L-aspartate: step 2/3') refers to the pathway producing homoserine (catalyzed by aspartate semialdehyde dehydrogenase/homoserine dehydrogenase), which is biochemically distinct from and upstream of homoserine kinase activity. Option B is the correct broad pathway category. No other option is defensible."
  },
  "important_caveats": [
    "The author's answer B ('Amino-acid biosynthesis') is the top-level UniProt pathway category. The more specific annotation is 'L-threonine biosynthesis; L-threonine from L-aspartate: step 4/5,' which is not offered as an option.",
    "Option C is a near-miss distractor that names homoserine but refers to the wrong pathway direction (producing homoserine rather than consuming it via phosphorylation).",
    "The UniProt EC assignment (2.7.1.39) is based on similarity (ECO:0000250, source P17423), while the pathway annotation is experimentally supported (ECO:0000269, PubMed:18757810)."
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
  "benchmark_sequence_length": 357,
  "benchmark_sequence_sha256": "0d5b6ca56754f8b7a34530cb0993479508f4e035318ede70547b7393e120e776",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 357,
  "current_source_sequence_sha256": "0d5b6ca56754f8b7a34530cb0993479508f4e035318ede70547b7393e120e776",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VU26",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "selected_historical_source_sequence_length": 357,
  "selected_historical_source_sequence_sha256": "0d5b6ca56754f8b7a34530cb0993479508f4e035318ede70547b7393e120e776",
  "selected_historical_version": {
    "accession": "J9VU26",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "KHSE_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VU26\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17423\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.1.39\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Homoserine kinase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HK\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HSK\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18757810\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 4/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Kingsbury J.M.\",\"McCusker J.H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18757810\"},{\"database\":\"DOI\",\"id\":\"10.1099/mic.0.2008/019729-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"2767\",\"id\":\"18757810\",\"journal\":\"Microbiology\",\"lastPage\":\"2775\",\"publicationDate\":\"2008\",\"title\":\"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\",\"volume\":\"154\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ACC85591.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   KHSE_CRYN9              Reviewed;         357 AA.\nAC   J9VU26; B2MVI2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Homoserine kinase {ECO:0000305};\nDE            Short=HK {ECO:0000305};\nDE            Short=HSK {ECO:0000305};\nDE            EC=2.7.1.39 {ECO:0000250|UniProtKB:P17423};\nGN   Name=THR1 {ECO:0000303|PubMed:18757810};\nGN   ORFNames=CNAG_04156 {ECO:0000312|EMBL:AFR96886.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ACC85591.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;\nRA   Kingsbury J.M., McCusker J.H.;\nRT   \"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\";\nRL   Microbiology 154:2767-2775(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 4/5. {ECO:0000269|PubMed:18757810}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 171. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
