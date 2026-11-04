# EC_number_0003

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0003.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 1.14.13.247

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTANPTSIHQRLDRRLSGFSLEQPFYTSPEVYALDLQHIFYKQWLYAVPVCQLAKAGSYTTLRVGAYEVVIVRSRDGEVRAFHNSCRHRGSLICKARQGQVAKLVCPYHQWTYELDGKLIWANDMGPDFDASKYGLKPVNLRNLDGLIYICLSDTPPDFQTFAQLARPYLEVHDLKDAKVAFTSTIIEKGNWKLVWENNRECYHCSSNHPALCRSFPLDPEVAGVQADGGVSKKLQAHFDRCEAAGTPAQFVLAGDGQYRLARMPLQEKALSYTMDGKAAVSRHLGRVAPPDAGTLLMFHYPSTWNHFLPDHSLTFRVMPISPTETEVTTTWLVHKDAVEGVDYDLKRLTEVWIATNDEDREIVETNQQGILSPAYVPGPYSPGQESGVMQFVDWYAASLERALAPRQVAAE

[Multiple Choices]
A. 1.14.13.238
B. 1.14.13.247
C. 2.7.11.24
D. 3.2.2.5
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

> The sequence-matched UniProt record assigns EC 1.14.13.247 and reports the corresponding L-proline betaine demethylation reactions, citing experimental evidence (ECO:0000269). The archived record also contains this assignment before the stated historical cutoff.

Citations as saved: [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has features consistent with a Rieske-type oxygenase, which makes the monooxygenase choices A or B more plausible than the kinase or hydrolase choices. But A and B are both in EC class 1.14.13; that broad family-level inference does not establish which substrate and reaction this protein performs.


**Missing item-specific fact**

> The protein's substrate specificity and catalytic reaction—specifically whether it demethylates L-proline betaine as assigned to EC 1.14.13.247—are needed to distinguish B from A.


**Reason**

> Transferable sequence and family knowledge can narrow the choices to the oxygenase options, but the supplied sequence alone offers no sufficiently discriminating basis for choosing between them. The exact substrate activity is the relevant missing fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The EC number is determined by the enzyme's reaction, and the evidence supports B. The difficulty of inferring the specific reaction from this input does not make two EC assignments equally defensible.


### Important caveats

- The cited UniProt annotation attributes the catalytic activity to experimental evidence, but the primary paper was not independently retrieved or assessed here.
- The archived record matches the supplied sequence and predates the stated cutoff; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a Rieske-type oxygenase, which makes the monooxygenase choices A or B more plausible than the kinase or hydrolase choices. But A and B are both in EC class 1.14.13; that broad family-level inference does not establish which substrate and reaction this protein performs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate specificity and catalytic reaction—specifically whether it demethylates L-proline betaine as assigned to EC 1.14.13.247—are needed to distinguish B from A.",
    "reason": "Transferable sequence and family knowledge can narrow the choices to the oxygenase options, but the supplied sequence alone offers no sufficiently discriminating basis for choosing between them. The exact substrate activity is the relevant missing fact."
  },
  "case_id": "EC_number_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.14.13.247 and reports the corresponding L-proline betaine demethylation reactions, citing experimental evidence (ECO:0000269). The archived record also contains this assignment before the stated historical cutoff."
  },
  "important_caveats": [
    "The cited UniProt annotation attributes the catalytic activity to experimental evidence, but the primary paper was not independently retrieved or assessed here.",
    "The archived record matches the supplied sequence and predates the stated cutoff; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC number is determined by the enzyme's reaction, and the evidence supports B. The difficulty of inferring the specific reaction from this input does not make two EC assignments equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.14.13.247 and reports the corresponding L-proline betaine demethylation reactions, citing experimental evidence (ECO:0000269). The archived record also contains this assignment before the stated historical cutoff.",
    "evidence_ids": ["H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has features consistent with a Rieske-type oxygenase, which makes the monooxygenase choices A or B more plausible than the kinase or hydrolase choices. But A and B are both in EC class 1.14.13; that broad family-level inference does not establish which substrate and reaction this protein performs.",
    "missing_item_specific_fact": "The protein's substrate specificity and catalytic reaction—specifically whether it demethylates L-proline betaine as assigned to EC 1.14.13.247—are needed to distinguish B from A.",
    "reason": "Transferable sequence and family knowledge can narrow the choices to the oxygenase options, but the supplied sequence alone offers no sufficiently discriminating basis for choosing between them. The exact substrate activity is the relevant missing fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC number is determined by the enzyme's reaction, and the evidence supports B. The difficulty of inferring the specific reaction from this input does not make two EC assignments equally defensible."
  },
  "important_caveats": [
    "The cited UniProt annotation attributes the catalytic activity to experimental evidence, but the primary paper was not independently retrieved or assessed here.",
    "The archived record matches the supplied sequence and predates the stated cutoff; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q92ZP9 (sequence matched) assigns EC 1.14.13.247 to Stachydrine N-demethylase with experimental evidence (ECO:0000269|PubMed:22224443). X-ray crystallography structures (PDB 3VCA, 3VCP at 1.59 Å) confirm the Rieske-type &#91;2Fe-2S&#93; and mononuclear iron active site, and the catalytic reaction (L-proline betaine + NAD(P)H + O2 → N-methyl-L-proline + formaldehyde + NAD(P)+ + H2O) is experimentally validated. The historical record (entry version 138) carries the same EC assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple Rieske-type &#91;2Fe-2S&#93; cluster motifs (Cys-Tyr-His-Cys at 'CYHCSS', and 'FHNSCRHRGSLICK' / 'WENNRECYHCSS' regions) along with a putative mononuclear non-heme iron site ('FTSTIIEK' region). It lacks FAD/FMN Rossmann-fold motifs (GxGxxG), cytochrome P450 heme-binding motifs (FxxGxxxCxG), protein kinase catalytic motifs (VAIK, HRD, DFG), and glycosidase motifs. This immediately eliminates C (2.7.11.24, a protein kinase) and D (3.2.2.5, an N-glycosyl hydrolase). The Rieske-type cofactor architecture identifies the enzyme as a Rieske-type monooxygenase within EC 1.14.13.x. Among the remaining 1.14.13.x choices, the specific domain architecture—two Rieske motifs flanking a mononuclear iron site in a compact ~412-aa protein—is characteristic of the Rieske-type quaternary-ammonium demethylase family (e.g., the stachydrine/proline-betaine catabolic enzymes studied by Daughtry et al. 2012). EC 1.14.13.247 is the Rieske-type stachydrine N-demethylase; EC 1.14.13.238 corresponds to a different specific monooxygenase reaction. The combination of Rieske-type cofactor recognition, absence of other cofactor motifs, and family-level sequence architecture provides a meaningful transferable basis to favor B over A, though the exact 4th-digit assignment carries some residual uncertainty if both candidate EC numbers were Rieske-type.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the clearly visible Rieske-type Cys-His motifs to identify the enzyme as a Rieske-type &#91;2Fe-2S&#93; monooxygenase, eliminating the kinase (C) and glycosidase (D) options outright. The Rieske-type architecture and compact domain organization are transferable family-level features shared with other Rieske-type oxygenases, which meaningfully narrows the 1.14.13.x alternatives. The distinction between 1.14.13.238 and 1.14.13.247 at the 4th digit is the weakest link, but the overall reasoning path from sequence features to a Rieske-type demethylase is supported by general biochemistry and enzyme-family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly eliminated by the absence of kinase and glycosidase motifs. Between A and B, the Rieske-type architecture and family-level sequence features favor B. While the 4th-digit distinction between two 1.14.13.x numbers is the most challenging step, the sequence does not contain features suggesting a different monooxygenase subclass, and the overall evidence points more strongly to B.


### Important caveats

- The distinction between EC 1.14.13.238 and 1.14.13.247 at the 4th digit is the least certain step; if both were Rieske-type enzymes, the 4th-digit assignment would lean more on specific substrate knowledge or database lookup.
- The reviewer-only evidence confirms the EC assignment experimentally (X-ray crystallography, PubMed 22224443), but this was not available to the evaluated model.
- The protein's organism identity (Sinorhizobium/Rhizobium meliloti) is not provided in the original input and was inferred only from the reviewer's accession match; the model must work from sequence features alone.
- The EC number 1.14.13.247 was relatively recently assigned (entry first released 2025-04-09 in current form), so a model's training data may or may not include this specific EC-to-sequence mapping.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple Rieske-type [2Fe-2S] cluster motifs (Cys-Tyr-His-Cys at 'CYHCSS', and 'FHNSCRHRGSLICK' / 'WENNRECYHCSS' regions) along with a putative mononuclear non-heme iron site ('FTSTIIEK' region). It lacks FAD/FMN Rossmann-fold motifs (GxGxxG), cytochrome P450 heme-binding motifs (FxxGxxxCxG), protein kinase catalytic motifs (VAIK, HRD, DFG), and glycosidase motifs. This immediately eliminates C (2.7.11.24, a protein kinase) and D (3.2.2.5, an N-glycosyl hydrolase). The Rieske-type cofactor architecture identifies the enzyme as a Rieske-type monooxygenase within EC 1.14.13.x. Among the remaining 1.14.13.x choices, the specific domain architecture—two Rieske motifs flanking a mononuclear iron site in a compact ~412-aa protein—is characteristic of the Rieske-type quaternary-ammonium demethylase family (e.g., the stachydrine/proline-betaine catabolic enzymes studied by Daughtry et al. 2012). EC 1.14.13.247 is the Rieske-type stachydrine N-demethylase; EC 1.14.13.238 corresponds to a different specific monooxygenase reaction. The combination of Rieske-type cofactor recognition, absence of other cofactor motifs, and family-level sequence architecture provides a meaningful transferable basis to favor B over A, though the exact 4th-digit assignment carries some residual uncertainty if both candidate EC numbers were Rieske-type.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the clearly visible Rieske-type Cys-His motifs to identify the enzyme as a Rieske-type [2Fe-2S] monooxygenase, eliminating the kinase (C) and glycosidase (D) options outright. The Rieske-type architecture and compact domain organization are transferable family-level features shared with other Rieske-type oxygenases, which meaningfully narrows the 1.14.13.x alternatives. The distinction between 1.14.13.238 and 1.14.13.247 at the 4th digit is the weakest link, but the overall reasoning path from sequence features to a Rieske-type demethylase is supported by general biochemistry and enzyme-family knowledge."
  },
  "case_id": "EC_number_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q92ZP9 (sequence matched) assigns EC 1.14.13.247 to Stachydrine N-demethylase with experimental evidence (ECO:0000269|PubMed:22224443). X-ray crystallography structures (PDB 3VCA, 3VCP at 1.59 Å) confirm the Rieske-type [2Fe-2S] and mononuclear iron active site, and the catalytic reaction (L-proline betaine + NAD(P)H + O2 → N-methyl-L-proline + formaldehyde + NAD(P)+ + H2O) is experimentally validated. The historical record (entry version 138) carries the same EC assignment."
  },
  "important_caveats": [
    "The distinction between EC 1.14.13.238 and 1.14.13.247 at the 4th digit is the least certain step; if both were Rieske-type enzymes, the 4th-digit assignment would lean more on specific substrate knowledge or database lookup.",
    "The reviewer-only evidence confirms the EC assignment experimentally (X-ray crystallography, PubMed 22224443), but this was not available to the evaluated model.",
    "The protein's organism identity (Sinorhizobium/Rhizobium meliloti) is not provided in the original input and was inferred only from the reviewer's accession match; the model must work from sequence features alone.",
    "The EC number 1.14.13.247 was relatively recently assigned (entry first released 2025-04-09 in current form), so a model's training data may or may not include this specific EC-to-sequence mapping."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminated by the absence of kinase and glycosidase motifs. Between A and B, the Rieske-type architecture and family-level sequence features favor B. While the 4th-digit distinction between two 1.14.13.x numbers is the most challenging step, the sequence does not contain features suggesting a different monooxygenase subclass, and the overall evidence points more strongly to B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q92ZP9 (sequence matched) assigns EC 1.14.13.247 to Stachydrine N-demethylase with experimental evidence (ECO:0000269|PubMed:22224443). X-ray crystallography structures (PDB 3VCA, 3VCP at 1.59 Å) confirm the Rieske-type [2Fe-2S] and mononuclear iron active site, and the catalytic reaction (L-proline betaine + NAD(P)H + O2 → N-methyl-L-proline + formaldehyde + NAD(P)+ + H2O) is experimentally validated. The historical record (entry version 138) carries the same EC assignment.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple Rieske-type [2Fe-2S] cluster motifs (Cys-Tyr-His-Cys at 'CYHCSS', and 'FHNSCRHRGSLICK' / 'WENNRECYHCSS' regions) along with a putative mononuclear non-heme iron site ('FTSTIIEK' region). It lacks FAD/FMN Rossmann-fold motifs (GxGxxG), cytochrome P450 heme-binding motifs (FxxGxxxCxG), protein kinase catalytic motifs (VAIK, HRD, DFG), and glycosidase motifs. This immediately eliminates C (2.7.11.24, a protein kinase) and D (3.2.2.5, an N-glycosyl hydrolase). The Rieske-type cofactor architecture identifies the enzyme as a Rieske-type monooxygenase within EC 1.14.13.x. Among the remaining 1.14.13.x choices, the specific domain architecture—two Rieske motifs flanking a mononuclear iron site in a compact ~412-aa protein—is characteristic of the Rieske-type quaternary-ammonium demethylase family (e.g., the stachydrine/proline-betaine catabolic enzymes studied by Daughtry et al. 2012). EC 1.14.13.247 is the Rieske-type stachydrine N-demethylase; EC 1.14.13.238 corresponds to a different specific monooxygenase reaction. The combination of Rieske-type cofactor recognition, absence of other cofactor motifs, and family-level sequence architecture provides a meaningful transferable basis to favor B over A, though the exact 4th-digit assignment carries some residual uncertainty if both candidate EC numbers were Rieske-type.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the clearly visible Rieske-type Cys-His motifs to identify the enzyme as a Rieske-type [2Fe-2S] monooxygenase, eliminating the kinase (C) and glycosidase (D) options outright. The Rieske-type architecture and compact domain organization are transferable family-level features shared with other Rieske-type oxygenases, which meaningfully narrows the 1.14.13.x alternatives. The distinction between 1.14.13.238 and 1.14.13.247 at the 4th digit is the weakest link, but the overall reasoning path from sequence features to a Rieske-type demethylase is supported by general biochemistry and enzyme-family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminated by the absence of kinase and glycosidase motifs. Between A and B, the Rieske-type architecture and family-level sequence features favor B. While the 4th-digit distinction between two 1.14.13.x numbers is the most challenging step, the sequence does not contain features suggesting a different monooxygenase subclass, and the overall evidence points more strongly to B."
  },
  "important_caveats": [
    "The distinction between EC 1.14.13.238 and 1.14.13.247 at the 4th digit is the least certain step; if both were Rieske-type enzymes, the 4th-digit assignment would lean more on specific substrate knowledge or database lookup.",
    "The reviewer-only evidence confirms the EC assignment experimentally (X-ray crystallography, PubMed 22224443), but this was not available to the evaluated model.",
    "The protein's organism identity (Sinorhizobium/Rhizobium meliloti) is not provided in the original input and was inferred only from the reviewer's accession match; the model must work from sequence features alone.",
    "The EC number 1.14.13.247 was relatively recently assigned (entry first released 2025-04-09 in current form), so a model's training data may or may not include this specific EC-to-sequence mapping."
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
  "benchmark_sequence_length": 412,
  "benchmark_sequence_sha256": "02696bd07c892515185be2809c4d39876ddd67459e5b8f8988a93fdc7960d8ea",
  "current_entry_audit": {
    "entryVersion": 140,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-12-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 412,
  "current_source_sequence_sha256": "02696bd07c892515185be2809c4d39876ddd67459e5b8f8988a93fdc7960d8ea",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 138,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q92ZP9",
  "selected_historical_entry_version": 138,
  "selected_historical_record_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "selected_historical_source_sequence_length": 412,
  "selected_historical_source_sequence_sha256": "02696bd07c892515185be2809c4d39876ddd67459e5b8f8988a93fdc7960d8ea",
  "selected_historical_version": {
    "accession": "Q92ZP9",
    "database": "Swiss-Prot",
    "entryVersion": 138,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "STC2_RHIME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q92ZP9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":140,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-12-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ensifer meliloti\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Alphaproteobacteria\",\"Hyphomicrobiales\",\"Rhizobiaceae\",\"Sinorhizobium/Ensifer group\",\"Sinorhizobium\"],\"scientificName\":\"Rhizobium meliloti (strain 1021)\",\"synonyms\":[\"Sinorhizobium meliloti\"],\"taxonId\":266834}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22224443\",\"source\":\"PubMed\"}],\"value\":\"Rieske-type mononuclear non-heme enzyme\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22224443\",\"source\":\"PubMed\"}],\"value\":\"1.14.13.247\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Stachydrine N-demethylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.14.13.247\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22224443\",\"source\":\"PubMed\"}],\"name\":\"L-proline betaine + NADH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NAD(+) + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:61616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16842\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35280\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:133743\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.14.13.247\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22224443\",\"source\":\"PubMed\"}],\"name\":\"L-proline betaine + NADPH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NADP(+) + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19357\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16842\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35280\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:133743\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Daughtry K.D.\",\"Xiao Y.\",\"Stoner-Ma D.\",\"Cho E.\",\"Orville A.M.\",\"Liu P.\",\"Allen K.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22224443\"},{\"database\":\"DOI\",\"id\":\"10.1021/ja2111898\"}],\"citationType\":\"journal article\",\"firstPage\":\"2823\",\"id\":\"22224443\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"2834\",\"publicationDate\":\"2012\",\"title\":\"Quaternary ammonium oxidative demethylation: X-ray crystallographic, resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type demethylase.\",\"volume\":\"134\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3VCA\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3VCP\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"1021\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.59 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR (2FE-2S)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"REACTION MECHANISM\",\"COFACTOR\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H1",
  "excerpt": "ID   STC2_RHIME              Reviewed;         412 AA.\nAC   Q92ZP9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-DEC-2001, sequence version 1.\nDT   28-JAN-2026, entry version 138.\nDE   RecName: Full=Stachydrine N-demethylase {ECO:0000305};\nDE            EC=1.14.13.247 {ECO:0000269|PubMed:22224443};\nDE   AltName: Full=Rieske-type mononuclear non-heme enzyme {ECO:0000303|PubMed:22224443};\nGN   Name=stc2 {ECO:0000303|PubMed:10689197};\nGN   OrderedLocusNames=RA0400 {ECO:0000305};\nGN   ORFNames=SMa0751 {ECO:0000312|EMBL:AAK65058.1};\nOS   Rhizobium meliloti (strain 1021) (Ensifer meliloti) (Sinorhizobium\nOS   meliloti).\nOG   Plasmid pSymA (megaplasmid 1).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;\nOC   Hyphomicrobiales; Rhizobiaceae; Sinorhizobium/Ensifer group; Sinorhizobium.\nOX   NCBI_TaxID=266834;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Stachydrine N-demethylase {ECO:0000305};\nDE            EC=1.14.13.247 {ECO:0000269|PubMed:22224443};\nDE   AltName: Full=Rieske-type mononuclear non-heme enzyme {ECO:0000303|PubMed:22224443};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=Sm2011 / Rm2011 / 2011;\nRX   PubMed=10689197; DOI=10.1016/s0378-1119(99)00554-5;\nRA   Burnet M.W., Goldmann A., Message B., Drong R., El Amrani A., Loreau O.,\nRA   Slightom J., Tepfer D.;\nRT   \"The stachydrine catabolism region in Sinorhizobium meliloti encodes a\nRT   multi-enzyme complex similar to the xenobiotic degrading systems in other\nRT   bacteria.\";\nRL   Gene 244:151-161(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:3VCA, ECO:0007744|PDB:3VCP}\nRP   X-RAY CRYSTALLOGRAPHY (1.59 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR\nRP   (2FE-2S), FUNCTION, CATALYTIC ACTIVITY, REACTION MECHANISM, COFACTOR, AND\nRP   SUBUNIT.\nRC   STRAIN=1021;\nRX   PubMed=22224443; DOI=10.1021/ja2111898;\nRA   Daughtry K.D., Xiao Y., Stoner-Ma D., Cho E., Orville A.M., Liu P.,\nRA   Allen K.N.;\nRT   \"Quaternary ammonium oxidative demethylation: X-ray crystallographic,\nRT   resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type\nRT   demethylase.\";\nRL   J. Am. Chem. Soc. 134:2823-2834(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-proline betaine + NADH + O2 + H(+) = N-methyl-L-proline +\nCC         formaldehyde + NAD(+) + H2O; Xref=Rhea:RHEA:61616, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:16842,\nCC         ChEBI:CHEBI:35280, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945,\nCC         ChEBI:CHEBI:133743; EC=1.14.13.247;\nCC         Evidence={ECO:0000269|PubMed:22224443};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-proline betaine + NADPH + O2 + H(+) = N-methyl-L-proline +\nCC         formaldehyde + NADP(+) + H2O; Xref=Rhea:RHEA:19357,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:16842, ChEBI:CHEBI:35280, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:133743; EC=1.14.13.247;\nCC         Evidence={ECO:0000269|PubMed:22224443};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
