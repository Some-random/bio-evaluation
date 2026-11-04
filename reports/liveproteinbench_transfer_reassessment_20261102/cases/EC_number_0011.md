# EC_number_0011

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0011.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.37

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPLITNIYTADPSAHVFNGKLYIYPSHDRETDIQFNDNGDQYDMADYHVFSLDSLDPPSEVTDHGVVLKVEDIPWVSKQLWAPDAATKDGKYYLYFPARDKEGIFRIGVAVSDKPEGPFTPDPEPIKGSYSIDPAVFVDDDGSAYMYFGGLWGGQLQCYQKGNNIFDAEWSGPKEPSGSGAKALGPRVAKLTDDMRQFAEEVREIVILAPETGEPLAADDHDRRFFEAAWMHKYNGKYYFSYSTGDTHYLVYAVGDSPYGPFTYGGRILEPVLGWTTHHSIVEFQGRWWLFHHDCELSKGVDHLRSVKVKEIWYDKDGKIVTEKPE

[Multiple Choices]
A. 3.2.1.37
B. 3.2.1.18
C. 2.7.1.39
D. 2.7.2.4
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

> The sequence-matched UniProt record assigns EC 3.2.1.37 and describes the corresponding xylan-hydrolysis reaction, citing experimental evidence from a publication. This supports choice A, though the primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 327-aa sequence is consistent with a fungal GH43 carbohydrate-active enzyme: GH43 family knowledge, including its characteristic acidic catalytic features and typical role in plant-cell-wall sugar hydrolysis, favors a beta-xylosidase over the offered alternatives. In particular, this family-level inference distinguishes it from the kinase choices and from the distinct sialidase family represented by EC 3.2.1.18.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use transferable sequence-family patterns to favor beta-xylosidase EC 3.2.1.37 among these choices without retrieving this protein's record. The sequence alone may not establish every substrate-specific activity with certainty, but the family inference meaningfully distinguishes the offered options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The record also assigns an unoffered arabinofuranosidase activity, but among the provided choices only A is supported.


### Important caveats

- The reviewer-only record is an annotation with experimental evidence cited; the underlying publication was not independently examined.
- The enzyme is annotated with an additional EC activity that is not among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 327-aa sequence is consistent with a fungal GH43 carbohydrate-active enzyme: GH43 family knowledge, including its characteristic acidic catalytic features and typical role in plant-cell-wall sugar hydrolysis, favors a beta-xylosidase over the offered alternatives. In particular, this family-level inference distinguishes it from the kinase choices and from the distinct sialidase family represented by EC 3.2.1.18.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use transferable sequence-family patterns to favor beta-xylosidase EC 3.2.1.37 among these choices without retrieving this protein's record. The sequence alone may not establish every substrate-specific activity with certainty, but the family inference meaningfully distinguishes the offered options."
  },
  "case_id": "EC_number_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.1.37 and describes the corresponding xylan-hydrolysis reaction, citing experimental evidence from a publication. This supports choice A, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only record is an annotation with experimental evidence cited; the underlying publication was not independently examined.",
    "The enzyme is annotated with an additional EC activity that is not among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also assigns an unoffered arabinofuranosidase activity, but among the provided choices only A is supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.1.37 and describes the corresponding xylan-hydrolysis reaction, citing experimental evidence from a publication. This supports choice A, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 327-aa sequence is consistent with a fungal GH43 carbohydrate-active enzyme: GH43 family knowledge, including its characteristic acidic catalytic features and typical role in plant-cell-wall sugar hydrolysis, favors a beta-xylosidase over the offered alternatives. In particular, this family-level inference distinguishes it from the kinase choices and from the distinct sialidase family represented by EC 3.2.1.18.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use transferable sequence-family patterns to favor beta-xylosidase EC 3.2.1.37 among these choices without retrieving this protein's record. The sequence alone may not establish every substrate-specific activity with certainty, but the family inference meaningfully distinguishes the offered options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also assigns an unoffered arabinofuranosidase activity, but among the provided choices only A is supported."
  },
  "important_caveats": [
    "The reviewer-only record is an annotation with experimental evidence cited; the underlying publication was not independently examined.",
    "The enzyme is annotated with an additional EC activity that is not among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry V9TNS0 annotates EC 3.2.1.37 (beta-xylosidase) with experimental evidence (ECO:0000269, PubMed:24262572). The catalytic activity comment states 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini' with EC=3.2.1.37. The sequence matches the benchmark input exactly (SHA-256 confirmed). The protein also carries a secondary EC 3.2.1.55 annotation, but that EC is not among the offered choices, so the expected answer A is the correct and only valid choice.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~327 aa) contains multiple D and H residues in patterns consistent with the GH43 catalytic dyad (DxxH…HxxD), multiple aromatic residues (W, Y, F) typical of carbohydrate-binding enzymes, and a small size characteristic of glycoside hydrolase families. This eliminates kinases (C: 2.7.1.39, D: 2.7.2.4) which require ATP-binding motifs (Walker A/B) and catalytic aspartates absent here. For the glycoside hydrolase choices: GH43 enzymes are inverting glycosidases. EC 3.2.1.18 (alpha-L-arabinofuranosidase) is conventionally assigned to GH51-family enzymes using a retaining mechanism, whereas GH43 arabinofuranosidases receive EC 3.2.1.55 (inverting). Thus 3.2.1.18 is mechanistically inconsistent with a GH43 enzyme, while 3.2.1.37 (beta-xylosidase) is the standard primary EC for GH43 xylan-acting exoglucanases. A model with knowledge of GH43 catalytic mechanism and EC classification conventions can therefore eliminate B, C, and D, leaving A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition of GH43 (catalytic dyad motifs, size, aromatic content) combined with the mechanistic EC classification convention (inverting GH43 → 3.2.1.37/3.2.1.55; retaining GH51 → 3.2.1.18) provides a concrete, transferable inference that distinguishes A from B, C, and D without requiring knowledge of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is bifunctional (EC 3.2.1.37 and 3.2.1.55), but 3.2.1.55 is not among the offered choices. Among the four options, only 3.2.1.37 is mechanistically and annotationally consistent with a GH43 enzyme. 3.2.1.18 is mechanistically wrong (retaining vs inverting), and 2.7.1.39/2.7.2.4 are kinases incompatible with the sequence. No ambiguity among the presented alternatives.


### Important caveats

- The protein is annotated as bifunctional (EC 3.2.1.37 and 3.2.1.55); the question only offers 3.2.1.37 among the choices, avoiding ambiguity.
- The GH43 catalytic dyad identification from raw sequence requires pattern recognition of DxxH/HxxD motifs, which is a learned family-level skill but not trivially obvious from a single sequence glance.
- The EC 3.2.1.18 vs 3.2.1.55 distinction is based on IUBMB convention linking mechanism to EC number assignment; this is a well-established classification principle across glycoside hydrolase families.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~327 aa) contains multiple D and H residues in patterns consistent with the GH43 catalytic dyad (DxxH…HxxD), multiple aromatic residues (W, Y, F) typical of carbohydrate-binding enzymes, and a small size characteristic of glycoside hydrolase families. This eliminates kinases (C: 2.7.1.39, D: 2.7.2.4) which require ATP-binding motifs (Walker A/B) and catalytic aspartates absent here. For the glycoside hydrolase choices: GH43 enzymes are inverting glycosidases. EC 3.2.1.18 (alpha-L-arabinofuranosidase) is conventionally assigned to GH51-family enzymes using a retaining mechanism, whereas GH43 arabinofuranosidases receive EC 3.2.1.55 (inverting). Thus 3.2.1.18 is mechanistically inconsistent with a GH43 enzyme, while 3.2.1.37 (beta-xylosidase) is the standard primary EC for GH43 xylan-acting exoglucanases. A model with knowledge of GH43 catalytic mechanism and EC classification conventions can therefore eliminate B, C, and D, leaving A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of GH43 (catalytic dyad motifs, size, aromatic content) combined with the mechanistic EC classification convention (inverting GH43 → 3.2.1.37/3.2.1.55; retaining GH51 → 3.2.1.18) provides a concrete, transferable inference that distinguishes A from B, C, and D without requiring knowledge of this specific protein's database annotation."
  },
  "case_id": "EC_number_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry V9TNS0 annotates EC 3.2.1.37 (beta-xylosidase) with experimental evidence (ECO:0000269, PubMed:24262572). The catalytic activity comment states 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini' with EC=3.2.1.37. The sequence matches the benchmark input exactly (SHA-256 confirmed). The protein also carries a secondary EC 3.2.1.55 annotation, but that EC is not among the offered choices, so the expected answer A is the correct and only valid choice."
  },
  "important_caveats": [
    "The protein is annotated as bifunctional (EC 3.2.1.37 and 3.2.1.55); the question only offers 3.2.1.37 among the choices, avoiding ambiguity.",
    "The GH43 catalytic dyad identification from raw sequence requires pattern recognition of DxxH/HxxD motifs, which is a learned family-level skill but not trivially obvious from a single sequence glance.",
    "The EC 3.2.1.18 vs 3.2.1.55 distinction is based on IUBMB convention linking mechanism to EC number assignment; this is a well-established classification principle across glycoside hydrolase families."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (EC 3.2.1.37 and 3.2.1.55), but 3.2.1.55 is not among the offered choices. Among the four options, only 3.2.1.37 is mechanistically and annotationally consistent with a GH43 enzyme. 3.2.1.18 is mechanistically wrong (retaining vs inverting), and 2.7.1.39/2.7.2.4 are kinases incompatible with the sequence. No ambiguity among the presented alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry V9TNS0 annotates EC 3.2.1.37 (beta-xylosidase) with experimental evidence (ECO:0000269, PubMed:24262572). The catalytic activity comment states 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini' with EC=3.2.1.37. The sequence matches the benchmark input exactly (SHA-256 confirmed). The protein also carries a secondary EC 3.2.1.55 annotation, but that EC is not among the offered choices, so the expected answer A is the correct and only valid choice.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~327 aa) contains multiple D and H residues in patterns consistent with the GH43 catalytic dyad (DxxH…HxxD), multiple aromatic residues (W, Y, F) typical of carbohydrate-binding enzymes, and a small size characteristic of glycoside hydrolase families. This eliminates kinases (C: 2.7.1.39, D: 2.7.2.4) which require ATP-binding motifs (Walker A/B) and catalytic aspartates absent here. For the glycoside hydrolase choices: GH43 enzymes are inverting glycosidases. EC 3.2.1.18 (alpha-L-arabinofuranosidase) is conventionally assigned to GH51-family enzymes using a retaining mechanism, whereas GH43 arabinofuranosidases receive EC 3.2.1.55 (inverting). Thus 3.2.1.18 is mechanistically inconsistent with a GH43 enzyme, while 3.2.1.37 (beta-xylosidase) is the standard primary EC for GH43 xylan-acting exoglucanases. A model with knowledge of GH43 catalytic mechanism and EC classification conventions can therefore eliminate B, C, and D, leaving A.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of GH43 (catalytic dyad motifs, size, aromatic content) combined with the mechanistic EC classification convention (inverting GH43 → 3.2.1.37/3.2.1.55; retaining GH51 → 3.2.1.18) provides a concrete, transferable inference that distinguishes A from B, C, and D without requiring knowledge of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (EC 3.2.1.37 and 3.2.1.55), but 3.2.1.55 is not among the offered choices. Among the four options, only 3.2.1.37 is mechanistically and annotationally consistent with a GH43 enzyme. 3.2.1.18 is mechanistically wrong (retaining vs inverting), and 2.7.1.39/2.7.2.4 are kinases incompatible with the sequence. No ambiguity among the presented alternatives."
  },
  "important_caveats": [
    "The protein is annotated as bifunctional (EC 3.2.1.37 and 3.2.1.55); the question only offers 3.2.1.37 among the choices, avoiding ambiguity.",
    "The GH43 catalytic dyad identification from raw sequence requires pattern recognition of DxxH/HxxD motifs, which is a learned family-level skill but not trivially obvious from a single sequence glance.",
    "The EC 3.2.1.18 vs 3.2.1.55 distinction is based on IUBMB convention linking mechanism to EC number assignment; this is a well-established classification principle across glycoside hydrolase families."
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
  "benchmark_sequence_length": 327,
  "benchmark_sequence_sha256": "50d3469575943c69659937ec94d1f84b72a59b8d874475defb7b29759a02ee84",
  "current_entry_audit": {
    "entryVersion": 23,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 327,
  "current_source_sequence_sha256": "50d3469575943c69659937ec94d1f84b72a59b8d874475defb7b29759a02ee84",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "V9TNS0",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "selected_historical_source_sequence_length": 327,
  "selected_historical_source_sequence_sha256": "50d3469575943c69659937ec94d1f84b72a59b8d874475defb7b29759a02ee84",
  "selected_historical_version": {
    "accession": "V9TNS0",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XY43A_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"V9TNS0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":23,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"includes\":[{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"1,4-beta-D-xylan xylohydrolase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylan 1,4-beta-xylosidase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.37\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Beta-xylosidase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.55\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Alpha-L-arabinofuranosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Arabinosidase\"}]}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylosidase/arabinosidase 43A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.37\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.55\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.\",\"Shi P.\",\"Huang H.\",\"Luo H.\",\"Wang Y.\",\"Zhang W.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24262572\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.foodchem.2013.10.062\"}],\"citationType\":\"journal article\",\"firstPage\":\"381\",\"id\":\"24262572\",\"journal\":\"Food Chem.\",\"lastPage\":\"387\",\"publicationDate\":\"2014\",\"title\":\"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and one GH11 xylanase from Humicola insolens and their synergy in the degradation of xylan.\",\"volume\":\"148\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   XY43A_HUMIN             Reviewed;         327 AA.\nAC   V9TNS0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=Xylosidase/arabinosidase 43A {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};\nDE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};\nDE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};\nDE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};\nGN   Name=XylL43A {ECO:0000303|PubMed:24262572};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Xylosidase/arabinosidase 43A {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};\nDE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};\nDE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};\nDE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   SUBCELLULAR LOCATION, AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=24262572; DOI=10.1016/j.foodchem.2013.10.062;\nRA   Yang X., Shi P., Huang H., Luo H., Wang Y., Zhang W., Yao B.;\nRT   \"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and\nRT   one GH11 xylanase from Humicola insolens and their synergy in the\nRT   degradation of xylan.\";\nRL   Food Chem. 148:381-387(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-\nCC         xylose residues from the non-reducing termini.; EC=3.2.1.37;\nCC         Evidence={ECO:0000269|PubMed:24262572};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside\nCC         residues in alpha-L-arabinosides.; EC=3.2.1.55;\nCC         Evidence={ECO:0000269|PubMed:24262572};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
