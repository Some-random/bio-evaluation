# EC_number_0125

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0125.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.1.1.348

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNGREHRRGDEAARREARSILFQNQDRSIVLIDVPTSIEEAQASPEEVGCDAGPLRKRRRLISSEPPHLPFKTPEPKAGSGGLTESVSDLMIAAAATEALRVLQESYAGPFCLPRVTRPNPLKSAFVPKGSFFLHGTVSSERDRFAAEAPVFDLIVLDPPWPNRSARRKQRNYRVADSLGSIRETLSLIPIAAHLAPDGLLAVWITNKAGVVELLTGPRGLFAQWGLEQVDEWTWLKITTSGEPIVDVGSTWRKPWERILIARRRGSSRKPACRGRVLVSVPDLHSRKPNLRGLFEDVLVPSNKGLEIFARNLTAGWWSWGDEVLKFQQPEYWVES

[Multiple Choices]
A. 2.1.1.395
B. 2.1.1.348
C. 1.97.1.13
D. 2.4.2.14
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

> The sequence-matched UniProt record assigns EC 2.1.1.348 and describes the reaction as methylation of adenosine in mRNA to N6-methyladenosine. The annotation cites experimental evidence, although the cited papers were not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a DPPW motif in a compact soluble methyltransferase-like region, consistent with the conserved catalytic features of the MT-A70 family of m6A RNA methyltransferases. That family-level inference supports the mRNA methylation choice B over the oxidoreductase and phosphoribosyltransferase alternatives; it also provides a meaningful basis to prefer B over a different methyltransferase EC choice, though sequence motifs alone are not experimental proof of substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers a transferable family-level clue rather than only a generic indication of methyltransferase activity. The DPPW motif and domain context support an MT-A70-like m6A writer, which meaningfully distinguishes the offered EC 2.1.1.348 choice without requiring recall of this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based family inference favors B among the offered choices; no other option is comparably supported.


### Important caveats

- The family inference is probabilistic; a motif by itself does not establish the complete EC reaction.
- The reviewer-only source links the annotation to experimental evidence, but the cited primary studies were not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a DPPW motif in a compact soluble methyltransferase-like region, consistent with the conserved catalytic features of the MT-A70 family of m6A RNA methyltransferases. That family-level inference supports the mRNA methylation choice B over the oxidoreductase and phosphoribosyltransferase alternatives; it also provides a meaningful basis to prefer B over a different methyltransferase EC choice, though sequence motifs alone are not experimental proof of substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a transferable family-level clue rather than only a generic indication of methyltransferase activity. The DPPW motif and domain context support an MT-A70-like m6A writer, which meaningfully distinguishes the offered EC 2.1.1.348 choice without requiring recall of this exact protein's database record."
  },
  "case_id": "EC_number_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.1.1.348 and describes the reaction as methylation of adenosine in mRNA to N6-methyladenosine. The annotation cites experimental evidence, although the cited papers were not independently reviewed here."
  },
  "important_caveats": [
    "The family inference is probabilistic; a motif by itself does not establish the complete EC reaction.",
    "The reviewer-only source links the annotation to experimental evidence, but the cited primary studies were not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors B among the offered choices; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.1.1.348 and describes the reaction as methylation of adenosine in mRNA to N6-methyladenosine. The annotation cites experimental evidence, although the cited papers were not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a DPPW motif in a compact soluble methyltransferase-like region, consistent with the conserved catalytic features of the MT-A70 family of m6A RNA methyltransferases. That family-level inference supports the mRNA methylation choice B over the oxidoreductase and phosphoribosyltransferase alternatives; it also provides a meaningful basis to prefer B over a different methyltransferase EC choice, though sequence motifs alone are not experimental proof of substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a transferable family-level clue rather than only a generic indication of methyltransferase activity. The DPPW motif and domain context support an MT-A70-like m6A writer, which meaningfully distinguishes the offered EC 2.1.1.348 choice without requiring recall of this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors B among the offered choices; no other option is comparably supported."
  },
  "important_caveats": [
    "The family inference is probabilistic; a motif by itself does not establish the complete EC reaction.",
    "The reviewer-only source links the annotation to experimental evidence, but the cited primary studies were not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9P5CQV5 annotates this protein as N6-methyladenosine RNA methyltransferase MTA1 with EC 2.1.1.348, supported by experimental evidence (ECO:0000269) from two independent publications (PubMed:39159278, PubMed:39611846). The catalytic activity is confirmed as: adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+. The sequence in the question matches the UniProt entry exactly (SHA-256 verified).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly diagnostic 'DPPW' catalytic motif (in the stretch 'DLIVLDPPWPNRS'), which is the hallmark of the METTL3/METTL14-type m6A RNA methyltransferase family. This motif is well-characterized across eukaryotes (human METTL3, yeast Met3/Met14, and fungal homologs) as the catalytic center for transferring a methyl group from SAM to the N6 position of adenosine in mRNA. This immediately eliminates EC 1.97.1.13 (oxidoreductase, EC class 1) and EC 2.4.2.14 (glycosyltransferase, EC class 2.4), which are entirely different enzyme classes. Between the two remaining methyltransferase options (A: 2.1.1.395 and B: 2.1.1.348), the DPPW motif specifically identifies the protein as an mRNA m6A writer (EC 2.1.1.348) rather than other 2.1.1.x methyltransferases that act on different substrates or use different catalytic architectures. The overall Rossmann-fold MTase domain organization and the fungal context (fungal m6A writers are METTL3 homologs) further support this assignment.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DPPW catalytic motif is a well-known, transferable family-level signature of m6A RNA methyltransferases learned from studying METTL3/METTL14 across multiple organisms. Its presence in the sequence meaningfully distinguishes EC 2.1.1.348 from the non-methyltransferase options (C, D) and from other methyltransferase options (A). While distinguishing 2.1.1.348 from 2.1.1.395 at the finest level has some residual uncertainty, the DPPW motif and MTase fold architecture provide a strong, concrete basis for selecting B over the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly eliminated by EC class (not methyltransferases). Option A (2.1.1.395) is a different methyltransferase that would not carry the DPPW m6A-writer signature. The DPPW motif and overall domain architecture make B the most defensible answer among the four choices.


### Important caveats

- The exact identity of EC 2.1.1.395 was not independently verified from first principles; the argument relies on the DPPW motif being specific to m6A writers rather than other 2.1.1.x methyltransferases.
- The UniProt annotation is based on experimental evidence from two 2024-2025 publications, which postdate many training cutoffs; however, the DPPW motif knowledge is well-established from earlier METTL3 studies.
- The protein is a fungal m6A writer homolog; its exact substrate specificity (mRNA vs. other RNA) was experimentally confirmed but the DPPW motif alone strongly implies mRNA m6A activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly diagnostic 'DPPW' catalytic motif (in the stretch 'DLIVLDPPWPNRS'), which is the hallmark of the METTL3/METTL14-type m6A RNA methyltransferase family. This motif is well-characterized across eukaryotes (human METTL3, yeast Met3/Met14, and fungal homologs) as the catalytic center for transferring a methyl group from SAM to the N6 position of adenosine in mRNA. This immediately eliminates EC 1.97.1.13 (oxidoreductase, EC class 1) and EC 2.4.2.14 (glycosyltransferase, EC class 2.4), which are entirely different enzyme classes. Between the two remaining methyltransferase options (A: 2.1.1.395 and B: 2.1.1.348), the DPPW motif specifically identifies the protein as an mRNA m6A writer (EC 2.1.1.348) rather than other 2.1.1.x methyltransferases that act on different substrates or use different catalytic architectures. The overall Rossmann-fold MTase domain organization and the fungal context (fungal m6A writers are METTL3 homologs) further support this assignment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DPPW catalytic motif is a well-known, transferable family-level signature of m6A RNA methyltransferases learned from studying METTL3/METTL14 across multiple organisms. Its presence in the sequence meaningfully distinguishes EC 2.1.1.348 from the non-methyltransferase options (C, D) and from other methyltransferase options (A). While distinguishing 2.1.1.348 from 2.1.1.395 at the finest level has some residual uncertainty, the DPPW motif and MTase fold architecture provide a strong, concrete basis for selecting B over the offered alternatives."
  },
  "case_id": "EC_number_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9P5CQV5 annotates this protein as N6-methyladenosine RNA methyltransferase MTA1 with EC 2.1.1.348, supported by experimental evidence (ECO:0000269) from two independent publications (PubMed:39159278, PubMed:39611846). The catalytic activity is confirmed as: adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+. The sequence in the question matches the UniProt entry exactly (SHA-256 verified)."
  },
  "important_caveats": [
    "The exact identity of EC 2.1.1.395 was not independently verified from first principles; the argument relies on the DPPW motif being specific to m6A writers rather than other 2.1.1.x methyltransferases.",
    "The UniProt annotation is based on experimental evidence from two 2024-2025 publications, which postdate many training cutoffs; however, the DPPW motif knowledge is well-established from earlier METTL3 studies.",
    "The protein is a fungal m6A writer homolog; its exact substrate specificity (mRNA vs. other RNA) was experimentally confirmed but the DPPW motif alone strongly implies mRNA m6A activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminated by EC class (not methyltransferases). Option A (2.1.1.395) is a different methyltransferase that would not carry the DPPW m6A-writer signature. The DPPW motif and overall domain architecture make B the most defensible answer among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9P5CQV5 annotates this protein as N6-methyladenosine RNA methyltransferase MTA1 with EC 2.1.1.348, supported by experimental evidence (ECO:0000269) from two independent publications (PubMed:39159278, PubMed:39611846). The catalytic activity is confirmed as: adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+. The sequence in the question matches the UniProt entry exactly (SHA-256 verified).",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly diagnostic 'DPPW' catalytic motif (in the stretch 'DLIVLDPPWPNRS'), which is the hallmark of the METTL3/METTL14-type m6A RNA methyltransferase family. This motif is well-characterized across eukaryotes (human METTL3, yeast Met3/Met14, and fungal homologs) as the catalytic center for transferring a methyl group from SAM to the N6 position of adenosine in mRNA. This immediately eliminates EC 1.97.1.13 (oxidoreductase, EC class 1) and EC 2.4.2.14 (glycosyltransferase, EC class 2.4), which are entirely different enzyme classes. Between the two remaining methyltransferase options (A: 2.1.1.395 and B: 2.1.1.348), the DPPW motif specifically identifies the protein as an mRNA m6A writer (EC 2.1.1.348) rather than other 2.1.1.x methyltransferases that act on different substrates or use different catalytic architectures. The overall Rossmann-fold MTase domain organization and the fungal context (fungal m6A writers are METTL3 homologs) further support this assignment.",
    "missing_item_specific_fact": "",
    "reason": "The DPPW catalytic motif is a well-known, transferable family-level signature of m6A RNA methyltransferases learned from studying METTL3/METTL14 across multiple organisms. Its presence in the sequence meaningfully distinguishes EC 2.1.1.348 from the non-methyltransferase options (C, D) and from other methyltransferase options (A). While distinguishing 2.1.1.348 from 2.1.1.395 at the finest level has some residual uncertainty, the DPPW motif and MTase fold architecture provide a strong, concrete basis for selecting B over the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminated by EC class (not methyltransferases). Option A (2.1.1.395) is a different methyltransferase that would not carry the DPPW m6A-writer signature. The DPPW motif and overall domain architecture make B the most defensible answer among the four choices."
  },
  "important_caveats": [
    "The exact identity of EC 2.1.1.395 was not independently verified from first principles; the argument relies on the DPPW motif being specific to m6A writers rather than other 2.1.1.x methyltransferases.",
    "The UniProt annotation is based on experimental evidence from two 2024-2025 publications, which postdate many training cutoffs; however, the DPPW motif knowledge is well-established from earlier METTL3 studies.",
    "The protein is a fungal m6A writer homolog; its exact substrate specificity (mRNA vs. other RNA) was experimentally confirmed but the DPPW motif alone strongly implies mRNA m6A activity."
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
  "benchmark_sequence_length": 336,
  "benchmark_sequence_sha256": "514940bbe527a4a17e21aaafc90f528777bc2a32248e3127fe0393ba01d916a9",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-09-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 336,
  "current_source_sequence_sha256": "514940bbe527a4a17e21aaafc90f528777bc2a32248e3127fe0393ba01d916a9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9P5CQV5",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc",
  "selected_historical_source_sequence_length": 336,
  "selected_historical_source_sequence_sha256": "514940bbe527a4a17e21aaafc90f528777bc2a32248e3127fe0393ba01d916a9",
  "selected_historical_version": {
    "accession": "A0A9P5CQV5",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MTA1_CRYP1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9P5CQV5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:17.608993+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-09-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:17.608993+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Diaporthales\",\"Cryphonectriaceae\",\"Cryphonectria-Endothia species complex\",\"Cryphonectria\"],\"scientificName\":\"Cryphonectria parasitica (strain ATCC 38755 / EP155)\",\"taxonId\":660469}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:17.608993+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39159278\",\"source\":\"PubMed\"}],\"value\":\"M6A writer MTA1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39159278\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.348\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39159278\",\"source\":\"PubMed\"}],\"value\":\"N6-methyladenosine RNA methyltransferase MTA1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:17.608993+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39159278\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39611846\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:55585\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.348\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39159278\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39611846\",\"source\":\"PubMed\"}],\"name\":\"an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:55584\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:12414\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:12417\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74411\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74449\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:17.608993+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhao L.\",\"Wei X.\",\"Chen F.\",\"Yuan L.\",\"Chen B.\",\"Li R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39159278\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1012476\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1012476\",\"id\":\"39159278\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1012476\",\"publicationDate\":\"2024\",\"title\":\"N6-methyladenosine RNA methyltransferase CpMTA1 mediates CpAphA mRNA stability through a YTHDF1-dependent m6A modification in the chestnut blight fungus.\",\"volume\":\"20\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:26:17.608993+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhao L.\",\"Wei X.\",\"Chen F.\",\"Chen B.\",\"Li R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39611846\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.01844-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0184424\",\"id\":\"39611846\",\"journal\":\"MBio\",\"lastPage\":\"e0184424\",\"publicationDate\":\"2025\",\"title\":\"m6A demethylase CpALKBH regulates CpZap1 mRNA stability to modulate the development and virulence of chestnut blight fungus.\",\"volume\":\"16\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF ASP-158 AND TRP-161\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:26:17.608993+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   MTA1_CRYP1              Reviewed;         336 AA.\nAC   A0A9P5CQV5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-SEP-2023, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:39159278};\nDE            EC=2.1.1.348 {ECO:0000269|PubMed:39159278};\nDE   AltName: Full=M6A writer MTA1 {ECO:0000303|PubMed:39159278};\nGN   Name=MTA1 {ECO:0000303|PubMed:39159278}; ORFNames=M406DRAFT_288717;\nOS   Cryphonectria parasitica (strain ATCC 38755 / EP155).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Diaporthales; Cryphonectriaceae;\nOC   Cryphonectria-Endothia species complex; Cryphonectria.\nOX   NCBI_TaxID=660469;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.443513+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc",
  "url": "https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:39159278};\nDE            EC=2.1.1.348 {ECO:0000269|PubMed:39159278};\nDE   AltName: Full=M6A writer MTA1 {ECO:0000303|PubMed:39159278};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.443513+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc",
  "url": "https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39159278; DOI=10.1371/journal.ppat.1012476;\nRA   Zhao L., Wei X., Chen F., Yuan L., Chen B., Li R.;\nRT   \"N6-methyladenosine RNA methyltransferase CpMTA1 mediates CpAphA mRNA\nRT   stability through a YTHDF1-dependent m6A modification in the chestnut\nRT   blight fungus.\";\nRL   PLoS Pathog. 20:e1012476-e1012476(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.443513+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc",
  "url": "https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H4",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, DISRUPTION PHENOTYPE, SUBCELLULAR LOCATION,\nRP   AND MUTAGENESIS OF ASP-158 AND TRP-161.\nRX   PubMed=39611846; DOI=10.1128/mbio.01844-24;\nRA   Zhao L., Wei X., Chen F., Chen B., Li R.;\nRT   \"m6A demethylase CpALKBH regulates CpZap1 mRNA stability to modulate the\nRT   development and virulence of chestnut blight fungus.\";\nRL   MBio 16:e0184424-e0184424(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.443513+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc",
  "url": "https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-\nCC         methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:55584, Rhea:RHEA-COMP:12414, Rhea:RHEA-COMP:12417,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:74411, ChEBI:CHEBI:74449; EC=2.1.1.348;\nCC         Evidence={ECO:0000269|PubMed:39159278, ECO:0000269|PubMed:39611846};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:55585;\nCC         Evidence={ECO:0000269|PubMed:39159278, ECO:0000269|PubMed:39611846};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.443513+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc",
  "url": "https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 125. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
