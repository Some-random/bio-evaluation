# EC_number_0182: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0182.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 3.4.21.62

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | no saved label | no saved label | output error (invalid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MVLTRRAALLLCPWVIQLVIKRTLAGDILPNEGKKEKDDVHKIISELRFLQKVETILESSNMSVSDVEADANAYNPDRDAPKEELQKLQDQQETPSKQPNNLRNSPQKRAEKKESPGKNKKSLRLIVSENHATSPSFFEESLLQEDVVSFIQSKGKLSNLKNLKSMIIDLNSDMTDEELAEYISLLERKGALIESDKLVGADDVSLASVKDAVRRGESSVNWGKLRSTMLEVPSGESPPSHAASSGSPFDDDDDLLSEAALHREEAHLAGSKTTKGYKFNDEYRNLQWGLDLARLDETQDLINANRVSVTKICVIDSGIDYNHPDLRNNIDVNVKELHGRKGVDDDSNGVVDDVYGANFVNNSGDPMDDNYHGTHVSGIISAVGNNGIGIVGVDGHSKLVICKALDQHKLGRLGDMFKCIDYCISRQAHMINGSFSFDEYSNIFNASVEHLRSLGILFFVSASNCAHDKLSKPDIAKCDLAVNHRYPPILSKTHNNVIAVANLKRDLDESYSLSVNSFYSNIYCQLAAPGTNIYSTTPMNNYRKLNGTSMASPHVAAIASIVRSINPNLTYLQIVEILRNAIVKLPSLTERVSWGGYVDILRAVNLAIDSKAAPYIKSHSWFRWKQGSRR

[Multiple Choices]
A. 3.4.13.22
B. 1.1.1.195
C. 3.4.21.62
D. 1.97.1.13
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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the 630-aa Plasmodium vivax SUB1 sequence in the cited UniProt records. Those records annotate it as EC 3.4.21.62, with catalytic-activity evidence attributed to publications (ECO:0000269).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a large precursor containing a subtilisin-like serine protease domain, which supports a serine endopeptidase interpretation and makes the non-protease options poor fits.


**Missing item-specific fact**

> Identifying the exact EC subtype 3.4.21.62 requires the protein-specific SUB1 annotation or catalytic characterization; the sequence and choices alone do not establish that precise EC assignment.


**Reason**

> Sequence reasoning can support the broad enzyme class and may favor C over the dipeptidase option, but the requested complete EC number is more specific than those general features establish.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports C for this sequence. The uncertainty concerns whether the input alone supports the exact subtype, not conflicting evidence for another listed option.


### Important caveats

- The sequence match and EC annotation are established from reviewer-only database evidence, which was not supplied to the evaluated model.
- The UniProt annotation cites experimental evidence codes, but the underlying primary studies were not independently reviewed here.
- The author's exact source snapshot is unknown; the sequence matches both the current entry and the retrieved historical entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large precursor containing a subtilisin-like serine protease domain, which supports a serine endopeptidase interpretation and makes the non-protease options poor fits.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying the exact EC subtype 3.4.21.62 requires the protein-specific SUB1 annotation or catalytic characterization; the sequence and choices alone do not establish that precise EC assignment.",
    "reason": "Sequence reasoning can support the broad enzyme class and may favor C over the dipeptidase option, but the requested complete EC number is more specific than those general features establish."
  },
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 630-aa Plasmodium vivax SUB1 sequence in the cited UniProt records. Those records annotate it as EC 3.4.21.62, with catalytic-activity evidence attributed to publications (ECO:0000269)."
  },
  "important_caveats": [
    "The sequence match and EC annotation are established from reviewer-only database evidence, which was not supplied to the evaluated model.",
    "The UniProt annotation cites experimental evidence codes, but the underlying primary studies were not independently reviewed here.",
    "The author's exact source snapshot is unknown; the sequence matches both the current entry and the retrieved historical entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C for this sequence. The uncertainty concerns whether the input alone supports the exact subtype, not conflicting evidence for another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 630-aa Plasmodium vivax SUB1 sequence in the cited UniProt records. Those records annotate it as EC 3.4.21.62, with catalytic-activity evidence attributed to publications (ECO:0000269).",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a large precursor containing a subtilisin-like serine protease domain, which supports a serine endopeptidase interpretation and makes the non-protease options poor fits.",
    "missing_item_specific_fact": "Identifying the exact EC subtype 3.4.21.62 requires the protein-specific SUB1 annotation or catalytic characterization; the sequence and choices alone do not establish that precise EC assignment.",
    "reason": "Sequence reasoning can support the broad enzyme class and may favor C over the dipeptidase option, but the requested complete EC number is more specific than those general features establish."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C for this sequence. The uncertainty concerns whether the input alone supports the exact subtype, not conflicting evidence for another listed option."
  },
  "important_caveats": [
    "The sequence match and EC annotation are established from reviewer-only database evidence, which was not supplied to the evaluated model.",
    "The UniProt annotation cites experimental evidence codes, but the underlying primary studies were not independently reviewed here.",
    "The author's exact source snapshot is unknown; the sequence matches both the current entry and the retrieved historical entry."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E6Y8B9 (SUB1_PLAVI, Plasmodium vivax) assigns EC 3.4.21.62 with evidence code ECO:0000269 (experimental) supported by five independent publications including X-ray crystallography studies (PDB: 4TR2, 8COY, 8COZ, 8QKE, 8QKG). The catalytic activity is described as 'Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.' The sequence matches exactly (630 AA, SHA256 confirmed). The EC assignment is experimentally validated.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could reason that the sequence is unlikely to be an oxidoreductase (eliminating B: 1.1.1.195 and D: 1.97.1.13) based on the absence of cofactor-binding motifs and the presence of protease-like features. Subtilisin-family (S8) features such as the HGR motif (His of catalytic triad) and DSG motif (Asp of catalytic triad) are present in the sequence, which could narrow the choice to 3.4.21.x over 3.4.13.x (S11 D-Ala-D-Ala carboxypeptidase). However, the specific 4th digit '62' cannot be derived from general biological reasoning; it is a database-assigned identifier for this particular enzyme.


**Missing item-specific fact**

> The exact 4-digit EC number 3.4.21.62 is a database-assigned identifier that cannot be derived from sequence by general biological reasoning. While the sequence contains some subtilisin-like motifs (HGR, DSG), Plasmodium SUB1 is a highly divergent subtilisin, and the canonical GDSGS catalytic serine motif is not clearly identifiable in the sequence. Assigning the specific number .62 rather than any other 3.4.21.x entry requires knowing the exact enzyme identity from UniProt or literature.


**Reason**

> The constrained choices (only one 3.4.21.x option) partially mitigate the lookup burden, as identifying subtilisin-like features would lead to C. However, the Plasmodium SUB1 sequence is divergent from canonical subtilisins, making motif-based identification uncertain without prior knowledge of this specific protein. The final 4-digit assignment is fundamentally a database fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the four choices, only C (3.4.21.62) is consistent with a subtilisin-like serine endopeptidase. Options B and D are oxidoreductases (EC class 1), clearly incompatible with a protease. Option A (3.4.13.22) is a D-Ala-D-Ala carboxypeptidase (S11 family) with different structural motifs. No other option is defensible for this sequence.


### Important caveats

- The UniProt annotation for EC 3.4.21.62 is supported by experimental evidence (ECO:0000269) from five publications, not merely computational prediction.
- Plasmodium vivax SUB1 is a divergent subtilisin; canonical subtilisin motifs (e.g., GDSGS) may be modified, making sequence-based identification harder than for well-studied subtilisins.
- The reviewer identified the accession E6Y8B9 from dataset image-path metadata; this was not available to the evaluated model.
- The first public date of the UniProt entry is 2025-04-09, meaning the annotation was relatively recent at the time of benchmark construction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could reason that the sequence is unlikely to be an oxidoreductase (eliminating B: 1.1.1.195 and D: 1.97.1.13) based on the absence of cofactor-binding motifs and the presence of protease-like features. Subtilisin-family (S8) features such as the HGR motif (His of catalytic triad) and DSG motif (Asp of catalytic triad) are present in the sequence, which could narrow the choice to 3.4.21.x over 3.4.13.x (S11 D-Ala-D-Ala carboxypeptidase). However, the specific 4th digit '62' cannot be derived from general biological reasoning; it is a database-assigned identifier for this particular enzyme.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact 4-digit EC number 3.4.21.62 is a database-assigned identifier that cannot be derived from sequence by general biological reasoning. While the sequence contains some subtilisin-like motifs (HGR, DSG), Plasmodium SUB1 is a highly divergent subtilisin, and the canonical GDSGS catalytic serine motif is not clearly identifiable in the sequence. Assigning the specific number .62 rather than any other 3.4.21.x entry requires knowing the exact enzyme identity from UniProt or literature.",
    "reason": "The constrained choices (only one 3.4.21.x option) partially mitigate the lookup burden, as identifying subtilisin-like features would lead to C. However, the Plasmodium SUB1 sequence is divergent from canonical subtilisins, making motif-based identification uncertain without prior knowledge of this specific protein. The final 4-digit assignment is fundamentally a database fact."
  },
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H1",
      "H2",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E6Y8B9 (SUB1_PLAVI, Plasmodium vivax) assigns EC 3.4.21.62 with evidence code ECO:0000269 (experimental) supported by five independent publications including X-ray crystallography studies (PDB: 4TR2, 8COY, 8COZ, 8QKE, 8QKG). The catalytic activity is described as 'Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.' The sequence matches exactly (630 AA, SHA256 confirmed). The EC assignment is experimentally validated."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.4.21.62 is supported by experimental evidence (ECO:0000269) from five publications, not merely computational prediction.",
    "Plasmodium vivax SUB1 is a divergent subtilisin; canonical subtilisin motifs (e.g., GDSGS) may be modified, making sequence-based identification harder than for well-studied subtilisins.",
    "The reviewer identified the accession E6Y8B9 from dataset image-path metadata; this was not available to the evaluated model.",
    "The first public date of the UniProt entry is 2025-04-09, meaning the annotation was relatively recent at the time of benchmark construction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four choices, only C (3.4.21.62) is consistent with a subtilisin-like serine endopeptidase. Options B and D are oxidoreductases (EC class 1), clearly incompatible with a protease. Option A (3.4.13.22) is a D-Ala-D-Ala carboxypeptidase (S11 family) with different structural motifs. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E6Y8B9 (SUB1_PLAVI, Plasmodium vivax) assigns EC 3.4.21.62 with evidence code ECO:0000269 (experimental) supported by five independent publications including X-ray crystallography studies (PDB: 4TR2, 8COY, 8COZ, 8QKE, 8QKG). The catalytic activity is described as 'Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.' The sequence matches exactly (630 AA, SHA256 confirmed). The EC assignment is experimentally validated.",
    "evidence_ids": ["C4", "C5", "C8", "H1", "H2", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could reason that the sequence is unlikely to be an oxidoreductase (eliminating B: 1.1.1.195 and D: 1.97.1.13) based on the absence of cofactor-binding motifs and the presence of protease-like features. Subtilisin-family (S8) features such as the HGR motif (His of catalytic triad) and DSG motif (Asp of catalytic triad) are present in the sequence, which could narrow the choice to 3.4.21.x over 3.4.13.x (S11 D-Ala-D-Ala carboxypeptidase). However, the specific 4th digit '62' cannot be derived from general biological reasoning; it is a database-assigned identifier for this particular enzyme.",
    "missing_item_specific_fact": "The exact 4-digit EC number 3.4.21.62 is a database-assigned identifier that cannot be derived from sequence by general biological reasoning. While the sequence contains some subtilisin-like motifs (HGR, DSG), Plasmodium SUB1 is a highly divergent subtilisin, and the canonical GDSGS catalytic serine motif is not clearly identifiable in the sequence. Assigning the specific number .62 rather than any other 3.4.21.x entry requires knowing the exact enzyme identity from UniProt or literature.",
    "reason": "The constrained choices (only one 3.4.21.x option) partially mitigate the lookup burden, as identifying subtilisin-like features would lead to C. However, the Plasmodium SUB1 sequence is divergent from canonical subtilisins, making motif-based identification uncertain without prior knowledge of this specific protein. The final 4-digit assignment is fundamentally a database fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four choices, only C (3.4.21.62) is consistent with a subtilisin-like serine endopeptidase. Options B and D are oxidoreductases (EC class 1), clearly incompatible with a protease. Option A (3.4.13.22) is a D-Ala-D-Ala carboxypeptidase (S11 family) with different structural motifs. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.4.21.62 is supported by experimental evidence (ECO:0000269) from five publications, not merely computational prediction.",
    "Plasmodium vivax SUB1 is a divergent subtilisin; canonical subtilisin motifs (e.g., GDSGS) may be modified, making sequence-based identification harder than for well-studied subtilisins.",
    "The reviewer identified the accession E6Y8B9 from dataset image-path metadata; this was not available to the evaluated model.",
    "The first public date of the UniProt entry is 2025-04-09, meaning the annotation was relatively recent at the time of benchmark construction."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the reviewed UniProt sequence. Its annotation assigns EC 3.4.21.62, and the catalytic-activity annotation is supported by evidence coded ECO:0000269, indicating experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the architecture of a secreted precursor with a long prodomain followed by a subtilisin-like catalytic region. Recognition of the subtilase family and its serine-protease function supports a peptide-bond hydrolase, distinguishing choice C from the dehydrogenase and oxidoreductase choices and the peptidase with a different EC class.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of subtilase-family sequences and functions gives a meaningful basis for choosing C among these alternatives. The exact EC subtype may require finer family knowledge, but the offered choices make the family-level inference discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C is consistent with the sequence's apparent subtilase precursor and serine-protease function among the offered alternatives.


### Important caveats

- Sequence-based family recognition supports the choice but is not, by itself, direct experimental confirmation of the exact EC subtype.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the architecture of a secreted precursor with a long prodomain followed by a subtilisin-like catalytic region. Recognition of the subtilase family and its serine-protease function supports a peptide-bond hydrolase, distinguishing choice C from the dehydrogenase and oxidoreductase choices and the peptidase with a different EC class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of subtilase-family sequences and functions gives a meaningful basis for choosing C among these alternatives. The exact EC subtype may require finer family knowledge, but the offered choices make the family-level inference discriminating."
  },
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence. Its annotation assigns EC 3.4.21.62, and the catalytic-activity annotation is supported by evidence coded ECO:0000269, indicating experimental evidence."
  },
  "important_caveats": [
    "Sequence-based family recognition supports the choice but is not, by itself, direct experimental confirmation of the exact EC subtype."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C is consistent with the sequence's apparent subtilase precursor and serine-protease function among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence. Its annotation assigns EC 3.4.21.62, and the catalytic-activity annotation is supported by evidence coded ECO:0000269, indicating experimental evidence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the architecture of a secreted precursor with a long prodomain followed by a subtilisin-like catalytic region. Recognition of the subtilase family and its serine-protease function supports a peptide-bond hydrolase, distinguishing choice C from the dehydrogenase and oxidoreductase choices and the peptidase with a different EC class.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of subtilase-family sequences and functions gives a meaningful basis for choosing C among these alternatives. The exact EC subtype may require finer family knowledge, but the offered choices make the family-level inference discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C is consistent with the sequence's apparent subtilase precursor and serine-protease function among the offered alternatives."
  },
  "important_caveats": [
    "Sequence-based family recognition supports the choice but is not, by itself, direct experimental confirmation of the exact EC subtype."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

No visible final review text was saved. Internal model reasoning is not a substitute for a visible review and is not published. The final-content extraction failed because the saved final content was not text.

**Saved parsed visible review:** `null`.

**Exact saved visible final text:** empty string (`""`). No visible final is synthesized from private reasoning.

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "E6Y8B9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "26d75cef4b12afe63e95e1e558255f990bc3a1fb29980dad1ff271270e9bc1c3",
  "benchmark_sequence_length": 630,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 80,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-03-08",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "current_source_sequence_sha256": "26d75cef4b12afe63e95e1e558255f990bc3a1fb29980dad1ff271270e9bc1c3",
  "current_source_sequence_length": 630,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 78,
  "selected_historical_version": {
    "accession": "E6Y8B9",
    "database": "Swiss-Prot",
    "entryVersion": 78,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SUB1_PLAVI",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "selected_historical_source_sequence_sha256": "26d75cef4b12afe63e95e1e558255f990bc3a1fb29980dad1ff271270e9bc1c3",
  "selected_historical_source_sequence_length": 630,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 78,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"E6Y8B9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":80,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-03-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ACT76164.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Plasmodium\"],\"scientificName\":\"Plasmodium vivax\",\"taxonId\":5855}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"PvS1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25204226\",\"source\":\"PubMed\"}],\"value\":\"PvSUB1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"SUB1 protease\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25204226\",\"source\":\"PubMed\"}],\"value\":\"Subtilase SUB1\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"3.4.21.62\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"Subtilisin-like protease 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.4.21.62\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Bouillon A.\",\"Giganti D.\",\"Benedet C.\",\"Gorgette O.\",\"Petres S.\",\"Crublet E.\",\"Girard-Blanc C.\",\"Witkowski B.\",\"Menard D.\",\"Nilges M.\",\"Mercereau-Puijalon O.\",\"Stoven V.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23653352\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m113.456764\"}],\"citationType\":\"journal article\",\"firstPage\":\"18561\",\"id\":\"23653352\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"18573\",\"publicationDate\":\"2013\",\"title\":\"In Silico screening on the three-dimensional model of the Plasmodium vivax SUB1 protease leads to the validation of a novel anti-parasite compound.\",\"volume\":\"288\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"DEVELOPMENTAL STAGE\",\"PROTEOLYTIC CLEAVAGE\",\"CLEAVAGE SITES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Martinez M.\",\"Bouillon A.\",\"Brule S.\",\"Raynal B.\",\"Haouz A.\",\"Alzari P.M.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38386597\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00198-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0019824\",\"id\":\"38386597\",\"journal\":\"MBio\",\"lastPage\":\"e0019824\",\"publicationDate\":\"2024\",\"title\":\"Prodomain-driven enzyme dimerization: a pH-dependent autoinhibition mechanism that controls Plasmodium Sub1 activity before merozoite egress.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Giganti D.\",\"Bouillon A.\",\"Tawk L.\",\"Robert F.\",\"Martinez M.\",\"Crublet E.\",\"Weber P.\",\"Girard-Blanc C.\",\"Petres S.\",\"Haouz A.\",\"Hernandez J.F.\",\"Mercereau-Puijalon O.\",\"Alzari P.M.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25204226\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms5833\"}],\"citationType\":\"journal article\",\"firstPage\":\"4833\",\"id\":\"25204226\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"4833\",\"publicationDate\":\"2014\",\"title\":\"A novel Plasmodium-specific prodomain fold regulates the malaria drug target SUB1 subtilase.\",\"volume\":\"5\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"}],\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) OF 26-630 IN COMPLEX WITH CALCIUM\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"SUBUNIT\",\"PROTEOLYTIC CLEAVAGE\",\"CLEAVAGE SITE\",\"DISULFIDE BONDS\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/references/5",
  "excerpt": "{\"citation\":{\"authors\":[\"Martinez M.\",\"Batista F.A.\",\"Maurel M.\",\"Bouillon A.\",\"Ortega Varga L.\",\"Wehenkel A.M.\",\"Le Chevalier-Sontag L.\",\"Blondel A.\",\"Haouz A.\",\"Hernandez J.F.\",\"Alzari P.M.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37428845\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2059798323004710\"}],\"citationType\":\"journal article\",\"firstPage\":\"721\",\"id\":\"37428845\",\"journal\":\"Acta Crystallogr. D Struct. Biol.\",\"lastPage\":\"734\",\"publicationDate\":\"2023\",\"title\":\"3D structures of the Plasmodium vivax subtilisin-like drug target SUB1 reveal conformational changes to accommodate a substrate-derived alpha-ketoamide inhibitor.\",\"volume\":\"79\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.44 ANGSTROMS) OF 273-617 IN COMPLEX WITH CA(2+) AND PEPTIDE INHIBITOR\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PROTEOLYTIC CLEAVAGE\",\"GLYCOSYLATION\",\"GLYCOSYLATION AT ASN-546\",\"DISULFIDE BONDS\",\"MUTAGENESIS OF ASN-361; ASN-432 AND ASN-445\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "json_pointer": "/references/6",
  "excerpt": "{\"citation\":{\"authors\":[\"Legru A.\",\"Batista F.A.\",\"Puszko A.K.\",\"Bouillon A.\",\"Maurel M.\",\"Martinez M.\",\"Ejjoummany A.\",\"Ortega Varga L.\",\"Adler P.\",\"Mechaly A.\",\"Hadjadj M.\",\"Sosnowski P.\",\"Hopfgartner G.\",\"Alzari P.M.\",\"Blondel A.\",\"Haouz A.\",\"Barale J.C.\",\"Hernandez J.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38503166\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ejmech.2024.116308\"}],\"citationType\":\"journal article\",\"firstPage\":\"116308\",\"id\":\"38503166\",\"journal\":\"Eur. J. Med. Chem.\",\"lastPage\":\"116308\",\"publicationDate\":\"2024\",\"title\":\"Insights from structure-activity relationships and the binding mode of peptidic alpha-ketoamide inhibitors of the malaria drug target subtilisin-like SUB1.\",\"volume\":\"269\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"referenceNumber\":7,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.50 ANGSTROMS) OF 26-630 IN COMPLEX WITH CA(2+) AND PEPTIDE INHIBITORS\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"GLYCOSYLATION AT ASN-546\",\"DISULFIDE BONDS\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "source_locator": "lines 1-20",
  "excerpt": "ID   SUB1_PLAVI              Reviewed;         630 AA.\nAC   E6Y8B9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-MAR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 78.\nDE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597, ECO:0000269|PubMed:38503166};\nDE   AltName: Full=PvS1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE   AltName: Full=PvSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:25204226};\nDE   AltName: Full=SUB1 protease {ECO:0000303|PubMed:38503166};\nDE   AltName: Full=Subtilase SUB1 {ECO:0000303|PubMed:25204226};\nDE   Flags: Precursor;\nGN   Name=sub1 {ECO:0000312|EMBL:ACT76164.1};\nGN   ORFNames=PVC01_100035100 {ECO:0000312|EMBL:SCO73277.1},\nGN   PVT01_100029100 {ECO:0000312|EMBL:SCO67822.1},\nGN   PVW1_100050600 {ECO:0000312|EMBL:CAG9475055.1};\nOS   Plasmodium vivax.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).\nOX   NCBI_TaxID=5855 {ECO:0000312|EMBL:ACT76164.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 78,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "source_locator": "lines 6-12",
  "excerpt": "DE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597, ECO:0000269|PubMed:38503166};\nDE   AltName: Full=PvS1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE   AltName: Full=PvSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:25204226};\nDE   AltName: Full=SUB1 protease {ECO:0000303|PubMed:38503166};\nDE   AltName: Full=Subtilase SUB1 {ECO:0000303|PubMed:25204226};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 78,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "source_locator": "lines 32-41",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, SUBUNIT, DEVELOPMENTAL STAGE, PROTEOLYTIC CLEAVAGE, AND\nRP   CLEAVAGE SITES.\nRX   PubMed=23653352; DOI=10.1074/jbc.m113.456764;\nRA   Bouillon A., Giganti D., Benedet C., Gorgette O., Petres S., Crublet E.,\nRA   Girard-Blanc C., Witkowski B., Menard D., Nilges M., Mercereau-Puijalon O.,\nRA   Stoven V., Barale J.C.;\nRT   \"In Silico screening on the three-dimensional model of the Plasmodium vivax\nRT   SUB1 protease leads to the validation of a novel anti-parasite compound.\";\nRL   J. Biol. Chem. 288:18561-18573(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 78,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "source_locator": "lines 42-49",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRX   PubMed=38386597; DOI=10.1128/mbio.00198-24;\nRA   Martinez M., Bouillon A., Brule S., Raynal B., Haouz A., Alzari P.M.,\nRA   Barale J.C.;\nRT   \"Prodomain-driven enzyme dimerization: a pH-dependent autoinhibition\nRT   mechanism that controls Plasmodium Sub1 activity before merozoite egress.\";\nRL   MBio 15:e0019824-e0019824(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 78,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "source_locator": "lines 50-60",
  "excerpt": "RN   [5] {ECO:0007744|PDB:4TR2}\nRP   X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) OF 26-630 IN COMPLEX WITH CALCIUM,\nRP   CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, SUBUNIT, PROTEOLYTIC\nRP   CLEAVAGE, CLEAVAGE SITE, AND DISULFIDE BONDS.\nRX   PubMed=25204226; DOI=10.1038/ncomms5833;\nRA   Giganti D., Bouillon A., Tawk L., Robert F., Martinez M., Crublet E.,\nRA   Weber P., Girard-Blanc C., Petres S., Haouz A., Hernandez J.F.,\nRA   Mercereau-Puijalon O., Alzari P.M., Barale J.C.;\nRT   \"A novel Plasmodium-specific prodomain fold regulates the malaria drug\nRT   target SUB1 subtilase.\";\nRL   Nat. Commun. 5:4833-4833(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 78,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "source_locator": "lines 61-73",
  "excerpt": "RN   [6] {ECO:0007744|PDB:8COY, ECO:0007744|PDB:8COZ}\nRP   X-RAY CRYSTALLOGRAPHY (1.44 ANGSTROMS) OF 273-617 IN COMPLEX WITH CA(2+)\nRP   AND PEPTIDE INHIBITOR, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PROTEOLYTIC\nRP   CLEAVAGE, GLYCOSYLATION, GLYCOSYLATION AT ASN-546, DISULFIDE BONDS, AND\nRP   MUTAGENESIS OF ASN-361; ASN-432 AND ASN-445.\nRX   PubMed=37428845; DOI=10.1107/s2059798323004710;\nRA   Martinez M., Batista F.A., Maurel M., Bouillon A., Ortega Varga L.,\nRA   Wehenkel A.M., Le Chevalier-Sontag L., Blondel A., Haouz A.,\nRA   Hernandez J.F., Alzari P.M., Barale J.C.;\nRT   \"3D structures of the Plasmodium vivax subtilisin-like drug target SUB1\nRT   reveal conformational changes to accommodate a substrate-derived alpha-\nRT   ketoamide inhibitor.\";\nRL   Acta Crystallogr. D Struct. Biol. 79:721-734(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 78,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "source_locator": "lines 74-86",
  "excerpt": "RN   [7] {ECO:0007744|PDB:8QKE, ECO:0007744|PDB:8QKG}\nRP   X-RAY CRYSTALLOGRAPHY (1.50 ANGSTROMS) OF 26-630 IN COMPLEX WITH CA(2+) AND\nRP   PEPTIDE INHIBITORS, CATALYTIC ACTIVITY, ACTIVITY REGULATION, GLYCOSYLATION\nRP   AT ASN-546, AND DISULFIDE BONDS.\nRX   PubMed=38503166; DOI=10.1016/j.ejmech.2024.116308;\nRA   Legru A., Batista F.A., Puszko A.K., Bouillon A., Maurel M., Martinez M.,\nRA   Ejjoummany A., Ortega Varga L., Adler P., Mechaly A., Hadjadj M.,\nRA   Sosnowski P., Hopfgartner G., Alzari P.M., Blondel A., Haouz A.,\nRA   Barale J.C., Hernandez J.F.;\nRT   \"Insights from structure-activity relationships and the binding mode of\nRT   peptidic alpha-ketoamide inhibitors of the malaria drug target subtilisin-\nRT   like SUB1.\";\nRL   Eur. J. Med. Chem. 269:116308-116308(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 78,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "source_locator": "lines 91-97",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of proteins with broad specificity for peptide\nCC         bonds, and a preference for a large uncharged residue in P1.\nCC         Hydrolyzes peptide amides.; EC=3.4.21.62;\nCC         Evidence={ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226,\nCC         ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597,\nCC         ECO:0000269|PubMed:38503166};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 78,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 182. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
