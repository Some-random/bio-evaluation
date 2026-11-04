# EC_number_0083

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0083.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.4.1.391

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKPHNSEKYFVKNGQPHFLISGEVHYFRINPKLWRNHLQLLKQTGADTVSTYIPWDWHEIEEDDFDFEGKTHPARNLIRFIKLCKEENLDLIVKPGPYILAEYENQGLPSWLLKKLSKNAFALDENGNVISPDLVSYLSDEFLEYTFKWYDKVMPIISKHQKEHYGPITMMQLCNEIGVFQWLSGKSDYNPKVINLYKEFIIQRYKTIEKLNSVYSTNYNSFDDLKAPSGKIKLRSDYCAYFDFHLFFREYYNKYISILKNKIRSFGINIKLTHNIPGWIYGNASELPMLISTYSEIMKNHPDIIFGLDHIPEFVSFRNAHSDLACNKILEAMQPEAPVWAAEFQAGTREHHVKAYAKDLETFYIASLAHGIKGFNYYMFSQGINPEGKGFYGKTFYFQTALDAASNKLALYDSIKKVNRFIRKEQKDLLRTNVNSEICVGFYKPYFFTELISSQLLKEKKLNVEELGLYIDPRFLREEILFNGLLRGLQTLNYNYDVVDLENCDLKSLTAYKQLWITSAEFMDAETQNLLSEFVLNGGNLILYPAVPTLDNYLNRCEILKNNFGIEFITKDSSHKVSAFGIEDVFTAFSKKQIYNDTNSKPIAFTQENEICGIRKKIGKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQFVVRENNKSRYIFFLNYHNERKTFNYRKSSELKKKKSEEISIAPFSYKVIKENK

[Multiple Choices]
A. 2.4.1.261
B. 2.4.1.391
C. 3.2.1.8
D. 2.8.1.7
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence matches the reviewed UniProt entry, whose EC assignment is 2.4.1.391. The entry links the catalytic activity and EC number to experimental evidence from a characterization study, supporting choice B for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit recognition of a glycosyltransferase, which would favor choices A or B over the hydrolase and sulfurtransferase alternatives. But both A and B are glycosyltransferases, and no clear sequence feature in the supplied input establishes the particular substrate and linkage specificity that distinguishes EC 2.4.1.391 from EC 2.4.1.261.


**Missing item-specific fact**

> The experimentally characterized reaction or a sufficiently specific family/homology assignment for this exact protein that distinguishes the two glycosyltransferase EC choices.


**Reason**

> General enzyme-class recognition could narrow the options, but selecting the complete EC number requires distinguishing between two transferase annotations with specificity not established by the input. Recalling the exact protein's recorded annotation would supply that missing distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports the keyed EC number for the matched sequence; it does not establish another offered option as a defensible answer.


### Important caveats

- The experimental support is conveyed through the database annotation's evidence link to a cited characterization study; the study itself was not independently reviewed here.
- The reviewer-only source evidence was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may permit recognition of a glycosyltransferase, which would favor choices A or B over the hydrolase and sulfurtransferase alternatives. But both A and B are glycosyltransferases, and no clear sequence feature in the supplied input establishes the particular substrate and linkage specificity that distinguishes EC 2.4.1.391 from EC 2.4.1.261.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally characterized reaction or a sufficiently specific family/homology assignment for this exact protein that distinguishes the two glycosyltransferase EC choices.",
    "reason": "General enzyme-class recognition could narrow the options, but selecting the complete EC number requires distinguishing between two transferase annotations with specificity not established by the input. Recalling the exact protein's recorded annotation would supply that missing distinction."
  },
  "case_id": "EC_number_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the reviewed UniProt entry, whose EC assignment is 2.4.1.391. The entry links the catalytic activity and EC number to experimental evidence from a characterization study, supporting choice B for this sequence."
  },
  "important_caveats": [
    "The experimental support is conveyed through the database annotation's evidence link to a cited characterization study; the study itself was not independently reviewed here.",
    "The reviewer-only source evidence was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports the keyed EC number for the matched sequence; it does not establish another offered option as a defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the reviewed UniProt entry, whose EC assignment is 2.4.1.391. The entry links the catalytic activity and EC number to experimental evidence from a characterization study, supporting choice B for this sequence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit recognition of a glycosyltransferase, which would favor choices A or B over the hydrolase and sulfurtransferase alternatives. But both A and B are glycosyltransferases, and no clear sequence feature in the supplied input establishes the particular substrate and linkage specificity that distinguishes EC 2.4.1.391 from EC 2.4.1.261.",
    "missing_item_specific_fact": "The experimentally characterized reaction or a sufficiently specific family/homology assignment for this exact protein that distinguishes the two glycosyltransferase EC choices.",
    "reason": "General enzyme-class recognition could narrow the options, but selecting the complete EC number requires distinguishing between two transferase annotations with specificity not established by the input. Recalling the exact protein's recorded annotation would supply that missing distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports the keyed EC number for the matched sequence; it does not establish another offered option as a defensible answer."
  },
  "important_caveats": [
    "The experimental support is conveyed through the database annotation's evidence link to a cited characterization study; the study itself was not independently reviewed here.",
    "The reviewer-only source evidence was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry I0AIT9 (sequence matched, 716 AA) is annotated with EC 2.4.1.391 (Beta-1,2-glucosyltransferase) supported by experimental evidence (ECO:0000269|PubMed:35065074). The enzyme was characterized by X-ray crystallography (PDB 7VKW-7VL6, 1.56 Å) in complexes with β-D-glucose, sophorose, and alternative substrates, along with biochemical characterization and mutagenesis of Glu-176 and Glu-343. The catalytic activity is defined as transferring a β-D-glucosyl unit to form a β-1,2-glucosidic linkage. This is strong experimental evidence, not mere computational annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence clearly encodes a glycosyltransferase rather than a hydrolase or sulfurtransferase, which eliminates options C (EC 3.2.1.8, endo-β-1,4-glucanase, a hydrolase with cellulase-type catalytic residues) and D (EC 2.8.1.7, thiosulfate sulfurtransferase, a rhodanese-fold enzyme with a conserved catalytic Cys). However, distinguishing A (EC 2.4.1.261) from B (EC 2.4.1.391) is the critical challenge. Both are EC 2.4.1.x 'other glycosyltransferases.' EC 2.4.1.391 was established in 2022 for an enzyme explicitly described as 'novel' in the primary publication, meaning it does not belong to a well-characterized glycosyltransferase family with established sequence-to-linkage-specificity relationships. The beta-1,2 linkage specificity is determined by active-site geometry that is not reliably predictable from primary sequence alone without prior knowledge of this specific enzyme's structure and mechanism. No conserved family motif in the sequence uniquely distinguishes a beta-1,2-glucosyltransferase from other EC 2.4.1.x transferases in a way that a knowledgeable model could apply without already knowing this protein's annotation.


**Missing item-specific fact**

> The specific annotation of this protein as EC 2.4.1.391 (beta-1,2-glucosyltransferase), established by experimental characterization in 2022. The enzyme is described as 'novel,' meaning it does not map to a pre-existing glycosyltransferase family whose members share predictable linkage specificity. Distinguishing EC 2.4.1.261 from EC 2.4.1.391 requires knowing which specific transfer reaction (donor, acceptor, linkage position) this particular sequence catalyzes, which is not derivable from general glycosyltransferase family knowledge.


**Reason**

> While the broad enzyme class (glycosyltransferase, EC 2.4.x) is identifiable from sequence features, the specific 4-digit EC number within EC 2.4.1.x requires knowledge of this exact protein's experimentally determined linkage specificity. The enzyme was characterized as 'novel' in 2022, indicating it does not belong to a family with transferable sequence-function rules that would allow prediction of the beta-1,2 linkage from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (2.4.1.261) and B (2.4.1.391) are glycosyltransferases (EC 2.4.1.x). Without knowing the specific linkage position (1,2 vs other) or the exact substrate specificity, a model relying on general glycosyltransferase knowledge could plausibly select either option. The distinction between these two EC numbers depends on very fine mechanistic details (beta-1,2 vs other linkages) that are not encoded in obvious sequence motifs shared across families.


### Important caveats

- EC 2.4.1.391 was established in 2022; models trained on earlier data may not have this EC number in their vocabulary at all.
- The primary publication describes the enzyme as 'novel,' confirming it does not fit established glycosyltransferase families with predictable sequence-function relationships.
- The elimination of options C and D is well-supported by general knowledge (hydrolase vs transferase; sulfurtransferase fold), but the A vs B distinction is the core difficulty.
- If EC 2.4.1.261 corresponds to a structurally very distinct enzyme (e.g., a phosphorylase or membrane-bound synthase with multi-TM architecture), its elimination might be feasible from sequence architecture, but this depends on the exact identity of 2.4.1.261 which is not provided in the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly encodes a glycosyltransferase rather than a hydrolase or sulfurtransferase, which eliminates options C (EC 3.2.1.8, endo-β-1,4-glucanase, a hydrolase with cellulase-type catalytic residues) and D (EC 2.8.1.7, thiosulfate sulfurtransferase, a rhodanese-fold enzyme with a conserved catalytic Cys). However, distinguishing A (EC 2.4.1.261) from B (EC 2.4.1.391) is the critical challenge. Both are EC 2.4.1.x 'other glycosyltransferases.' EC 2.4.1.391 was established in 2022 for an enzyme explicitly described as 'novel' in the primary publication, meaning it does not belong to a well-characterized glycosyltransferase family with established sequence-to-linkage-specificity relationships. The beta-1,2 linkage specificity is determined by active-site geometry that is not reliably predictable from primary sequence alone without prior knowledge of this specific enzyme's structure and mechanism. No conserved family motif in the sequence uniquely distinguishes a beta-1,2-glucosyltransferase from other EC 2.4.1.x transferases in a way that a knowledgeable model could apply without already knowing this protein's annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation of this protein as EC 2.4.1.391 (beta-1,2-glucosyltransferase), established by experimental characterization in 2022. The enzyme is described as 'novel,' meaning it does not map to a pre-existing glycosyltransferase family whose members share predictable linkage specificity. Distinguishing EC 2.4.1.261 from EC 2.4.1.391 requires knowing which specific transfer reaction (donor, acceptor, linkage position) this particular sequence catalyzes, which is not derivable from general glycosyltransferase family knowledge.",
    "reason": "While the broad enzyme class (glycosyltransferase, EC 2.4.x) is identifiable from sequence features, the specific 4-digit EC number within EC 2.4.1.x requires knowledge of this exact protein's experimentally determined linkage specificity. The enzyme was characterized as 'novel' in 2022, indicating it does not belong to a family with transferable sequence-function rules that would allow prediction of the beta-1,2 linkage from sequence alone."
  },
  "case_id": "EC_number_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry I0AIT9 (sequence matched, 716 AA) is annotated with EC 2.4.1.391 (Beta-1,2-glucosyltransferase) supported by experimental evidence (ECO:0000269|PubMed:35065074). The enzyme was characterized by X-ray crystallography (PDB 7VKW-7VL6, 1.56 Å) in complexes with β-D-glucose, sophorose, and alternative substrates, along with biochemical characterization and mutagenesis of Glu-176 and Glu-343. The catalytic activity is defined as transferring a β-D-glucosyl unit to form a β-1,2-glucosidic linkage. This is strong experimental evidence, not mere computational annotation."
  },
  "important_caveats": [
    "EC 2.4.1.391 was established in 2022; models trained on earlier data may not have this EC number in their vocabulary at all.",
    "The primary publication describes the enzyme as 'novel,' confirming it does not fit established glycosyltransferase families with predictable sequence-function relationships.",
    "The elimination of options C and D is well-supported by general knowledge (hydrolase vs transferase; sulfurtransferase fold), but the A vs B distinction is the core difficulty.",
    "If EC 2.4.1.261 corresponds to a structurally very distinct enzyme (e.g., a phosphorylase or membrane-bound synthase with multi-TM architecture), its elimination might be feasible from sequence architecture, but this depends on the exact identity of 2.4.1.261 which is not provided in the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (2.4.1.261) and B (2.4.1.391) are glycosyltransferases (EC 2.4.1.x). Without knowing the specific linkage position (1,2 vs other) or the exact substrate specificity, a model relying on general glycosyltransferase knowledge could plausibly select either option. The distinction between these two EC numbers depends on very fine mechanistic details (beta-1,2 vs other linkages) that are not encoded in obvious sequence motifs shared across families."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry I0AIT9 (sequence matched, 716 AA) is annotated with EC 2.4.1.391 (Beta-1,2-glucosyltransferase) supported by experimental evidence (ECO:0000269|PubMed:35065074). The enzyme was characterized by X-ray crystallography (PDB 7VKW-7VL6, 1.56 Å) in complexes with β-D-glucose, sophorose, and alternative substrates, along with biochemical characterization and mutagenesis of Glu-176 and Glu-343. The catalytic activity is defined as transferring a β-D-glucosyl unit to form a β-1,2-glucosidic linkage. This is strong experimental evidence, not mere computational annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence clearly encodes a glycosyltransferase rather than a hydrolase or sulfurtransferase, which eliminates options C (EC 3.2.1.8, endo-β-1,4-glucanase, a hydrolase with cellulase-type catalytic residues) and D (EC 2.8.1.7, thiosulfate sulfurtransferase, a rhodanese-fold enzyme with a conserved catalytic Cys). However, distinguishing A (EC 2.4.1.261) from B (EC 2.4.1.391) is the critical challenge. Both are EC 2.4.1.x 'other glycosyltransferases.' EC 2.4.1.391 was established in 2022 for an enzyme explicitly described as 'novel' in the primary publication, meaning it does not belong to a well-characterized glycosyltransferase family with established sequence-to-linkage-specificity relationships. The beta-1,2 linkage specificity is determined by active-site geometry that is not reliably predictable from primary sequence alone without prior knowledge of this specific enzyme's structure and mechanism. No conserved family motif in the sequence uniquely distinguishes a beta-1,2-glucosyltransferase from other EC 2.4.1.x transferases in a way that a knowledgeable model could apply without already knowing this protein's annotation.",
    "missing_item_specific_fact": "The specific annotation of this protein as EC 2.4.1.391 (beta-1,2-glucosyltransferase), established by experimental characterization in 2022. The enzyme is described as 'novel,' meaning it does not map to a pre-existing glycosyltransferase family whose members share predictable linkage specificity. Distinguishing EC 2.4.1.261 from EC 2.4.1.391 requires knowing which specific transfer reaction (donor, acceptor, linkage position) this particular sequence catalyzes, which is not derivable from general glycosyltransferase family knowledge.",
    "reason": "While the broad enzyme class (glycosyltransferase, EC 2.4.x) is identifiable from sequence features, the specific 4-digit EC number within EC 2.4.1.x requires knowledge of this exact protein's experimentally determined linkage specificity. The enzyme was characterized as 'novel' in 2022, indicating it does not belong to a family with transferable sequence-function rules that would allow prediction of the beta-1,2 linkage from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (2.4.1.261) and B (2.4.1.391) are glycosyltransferases (EC 2.4.1.x). Without knowing the specific linkage position (1,2 vs other) or the exact substrate specificity, a model relying on general glycosyltransferase knowledge could plausibly select either option. The distinction between these two EC numbers depends on very fine mechanistic details (beta-1,2 vs other linkages) that are not encoded in obvious sequence motifs shared across families."
  },
  "important_caveats": [
    "EC 2.4.1.391 was established in 2022; models trained on earlier data may not have this EC number in their vocabulary at all.",
    "The primary publication describes the enzyme as 'novel,' confirming it does not fit established glycosyltransferase families with predictable sequence-function relationships.",
    "The elimination of options C and D is well-supported by general knowledge (hydrolase vs transferase; sulfurtransferase fold), but the A vs B distinction is the core difficulty.",
    "If EC 2.4.1.261 corresponds to a structurally very distinct enzyme (e.g., a phosphorylase or membrane-bound synthase with multi-TM architecture), its elimination might be feasible from sequence architecture, but this depends on the exact identity of 2.4.1.261 which is not provided in the question."
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
  "benchmark_sequence_length": 716,
  "benchmark_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "current_entry_audit": {
    "entryVersion": 57,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-06-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 716,
  "current_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "I0AIT9",
  "selected_historical_entry_version": 55,
  "selected_historical_record_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "selected_historical_source_sequence_length": 716,
  "selected_historical_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "selected_historical_version": {
    "accession": "I0AIT9",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "B12GT_IGNAJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"I0AIT9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":57,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-06-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Ignavibacteriota\",\"Ignavibacteria\",\"Ignavibacteriales\",\"Ignavibacteriaceae\",\"Ignavibacterium\"],\"scientificName\":\"Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16)\",\"taxonId\":945713}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"IaSGT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.391\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.4.1.391\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"name\":\"a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:78691\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11881\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11882\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:27517\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35436\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229541\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Kobayashi K.\",\"Shimizu H.\",\"Tanaka N.\",\"Kuramochi K.\",\"Nakai H.\",\"Nakajima M.\",\"Taguchi H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35065074\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2022.101606\"}],\"citationType\":\"journal article\",\"firstPage\":\"101606\",\"id\":\"35065074\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"101606\",\"publicationDate\":\"2022\",\"title\":\"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.\",\"volume\":\"298\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKW\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL0\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL1\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL3\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL4\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL6\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF GLU-176 AND GLU-343\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H1",
  "excerpt": "ID   B12GT_IGNAJ             Reviewed;         716 AA.\nAC   I0AIT9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-JUN-2012, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};\nDE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};\nGN   OrderedLocusNames=IALB_1185 {ECO:0000312|EMBL:AFH48896.1};\nOS   Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 /\nOS   Mat9-16).\nOC   Bacteria; Pseudomonadati; Ignavibacteriota; Ignavibacteria;\nOC   Ignavibacteriales; Ignavibacteriaceae; Ignavibacterium.\nOX   NCBI_TaxID=945713;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};\nDE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7VKW, ECO:0007744|PDB:7VKX, ECO:0007744|PDB:7VKY, ECO:0007744|PDB:7VKZ, ECO:0007744|PDB:7VL0, ECO:0007744|PDB:7VL1, ECO:0007744|PDB:7VL2, ECO:0007744|PDB:7VL3, ECO:0007744|PDB:7VL4, ECO:0007744|PDB:7VL5, ECO:0007744|PDB:7VL6}\nRP   X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE;\nRP   SOPHOROSE AND ALTERNATIVE SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF\nRP   GLU-176 AND GLU-343.\nRC   STRAIN=DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16;\nRX   PubMed=35065074; DOI=10.1016/j.jbc.2022.101606;\nRA   Kobayashi K., Shimizu H., Tanaka N., Kuramochi K., Nakai H., Nakajima M.,\nRA   Taguchi H.;\nRT   \"Characterization and structural analyses of a novel glycosyltransferase\nRT   acting on the beta-1,2-glucosidic linkages.\";\nRL   J. Biol. Chem. 298:101606-101606(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-\nCC         glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1);\nCC         Xref=Rhea:RHEA:78691, Rhea:RHEA-COMP:11881, Rhea:RHEA-COMP:11882,\nCC         ChEBI:CHEBI:27517, ChEBI:CHEBI:35436, ChEBI:CHEBI:229541;\nCC         EC=2.4.1.391; Evidence={ECO:0000269|PubMed:35065074};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 83. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
