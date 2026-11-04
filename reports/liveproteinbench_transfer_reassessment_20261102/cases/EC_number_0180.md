# EC_number_0180

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0180.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 1.1.1.136

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. 1.1.1.136
B. 1.1.1.336
C. 3.6.1.5
D. 3.2.1.31
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

> The sequence-matched UniProt entry assigns EC 1.1.1.136 and gives the corresponding UDP-N-acetylglucosamine oxidation reaction with ECO:0000269 experimental evidence. This supports choice A for the supplied protein, though it is evidence reported in the database rather than an independent review of the primary experiment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the length and glycine-rich N-terminal dinucleotide-binding pattern expected of an NAD-dependent sugar-nucleotide dehydrogenase, along with a plausible conserved catalytic cysteine region. Transferable family/profile knowledge can narrow this to the UDP-sugar dehydrogenase alternatives and, by recognizing the UDP-GlcNAc 6-dehydrogenase family rather than merely the broad fold, favor A. The motifs alone are not a direct assay of substrate specificity, so this is a sequence-family inference, not proof.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A credible family-level sequence inference can meaningfully distinguish the offered enzyme class and favor A; the choices include unrelated hydrolase activities that do not fit the dehydrogenase-like sequence. Exact substrate specificity is the difficult distinction, but transferable homolog-family recognition provides a basis for it without requiring the recorded annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based family inference favors A over the alternatives; no second choice is comparably supported by the supplied sequence.


### Important caveats

- A Rossmann-like motif and catalytic-region pattern support a dehydrogenase-family inference but do not by themselves establish the exact substrate.
- The reviewer evidence is sequence-matched database annotation with an experimental evidence code; it was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the length and glycine-rich N-terminal dinucleotide-binding pattern expected of an NAD-dependent sugar-nucleotide dehydrogenase, along with a plausible conserved catalytic cysteine region. Transferable family/profile knowledge can narrow this to the UDP-sugar dehydrogenase alternatives and, by recognizing the UDP-GlcNAc 6-dehydrogenase family rather than merely the broad fold, favor A. The motifs alone are not a direct assay of substrate specificity, so this is a sequence-family inference, not proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A credible family-level sequence inference can meaningfully distinguish the offered enzyme class and favor A; the choices include unrelated hydrolase activities that do not fit the dehydrogenase-like sequence. Exact substrate specificity is the difficult distinction, but transferable homolog-family recognition provides a basis for it without requiring the recorded annotation for this exact protein."
  },
  "case_id": "EC_number_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 1.1.1.136 and gives the corresponding UDP-N-acetylglucosamine oxidation reaction with ECO:0000269 experimental evidence. This supports choice A for the supplied protein, though it is evidence reported in the database rather than an independent review of the primary experiment."
  },
  "important_caveats": [
    "A Rossmann-like motif and catalytic-region pattern support a dehydrogenase-family inference but do not by themselves establish the exact substrate.",
    "The reviewer evidence is sequence-matched database annotation with an experimental evidence code; it was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors A over the alternatives; no second choice is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 1.1.1.136 and gives the corresponding UDP-N-acetylglucosamine oxidation reaction with ECO:0000269 experimental evidence. This supports choice A for the supplied protein, though it is evidence reported in the database rather than an independent review of the primary experiment.",
    "evidence_ids": ["C4", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the length and glycine-rich N-terminal dinucleotide-binding pattern expected of an NAD-dependent sugar-nucleotide dehydrogenase, along with a plausible conserved catalytic cysteine region. Transferable family/profile knowledge can narrow this to the UDP-sugar dehydrogenase alternatives and, by recognizing the UDP-GlcNAc 6-dehydrogenase family rather than merely the broad fold, favor A. The motifs alone are not a direct assay of substrate specificity, so this is a sequence-family inference, not proof.",
    "missing_item_specific_fact": "",
    "reason": "A credible family-level sequence inference can meaningfully distinguish the offered enzyme class and favor A; the choices include unrelated hydrolase activities that do not fit the dehydrogenase-like sequence. Exact substrate specificity is the difficult distinction, but transferable homolog-family recognition provides a basis for it without requiring the recorded annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference favors A over the alternatives; no second choice is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "A Rossmann-like motif and catalytic-region pattern support a dehydrogenase-family inference but do not by themselves establish the exact substrate.",
    "The reviewer evidence is sequence-matched database annotation with an experimental evidence code; it was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9RHD7 (WBPO_PSEAI) exactly matches the supplied 422-aa sequence (SHA256 confirmed). EC 1.1.1.136 (UDP-N-acetyl-D-glucosamine 6-dehydrogenase) is annotated with experimental evidence code ECO:0000269 from PubMed 18065759 (Miller et al., JBC 2008), which directly demonstrated the catalytic activity. Both current and historical (entry version 111) records confirm this annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region 'VAVVGLGYVGLPLAVEFG' contains the canonical GxGxxG Rossmann-fold motif (GLGYVGLP), a hallmark of NAD(P)-dependent oxidoreductases, immediately eliminating hydrolase options C (EC 3.6.1.5) and D (EC 3.2.1.31). Within EC 1.1.1.x, the sequence displays multiple motifs diagnostic of the UDP-sugar 6-dehydrogenase (UGDH/WbpO) superfamily: the 'GAYDGIILAVAHSEFKN' segment, the 'GTP' region, and the overall ~420-aa architecture with two domains (NAD-binding + substrate-binding) are characteristic of this family. EC 1.1.1.136 (UDP-GlcNAc 6-dehydrogenase) is a well-known member of this family (alongside EC 1.1.1.22 UDP-Glc 6-dehydrogenase). EC 1.1.1.336 is either not a recognized EC number or does not belong to the UDP-sugar dehydrogenase family; it does not share the diagnostic UGDH-family motifs. Thus, recognizing the Rossmann fold plus UGDH-family sequence signatures from general knowledge of UDP-sugar dehydrogenases across multiple organisms meaningfully distinguishes A from B, C, and D without needing the specific database annotation of this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold GxGxxG motif at the N-terminus is a universally recognized feature of NAD-dependent oxidoreductases, clearly separating EC 1.x.x.x from EC 3.x.x.x choices. The UDP-sugar 6-dehydrogenase family motifs (GAY, GTP, overall domain architecture) are well-documented across homologs (E. coli Ugd, Neisseria, Pseudomonas WbpO family members). EC 1.1.1.136 is the established EC number for UDP-GlcNAc 6-dehydrogenase within this family, while EC 1.1.1.336 is not a recognized member of this superfamily. A knowledgeable model using family-level sequence pattern recognition can meaningfully select A over B, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Rossmann fold eliminates C and D. The UGDH-family motifs point specifically to EC 1.1.1.136 rather than the obscure or non-standard EC 1.1.1.336. No other option shares the diagnostic family features.


### Important caveats

- The distinction between EC 1.1.1.136 (UDP-GlcNAc 6-dehydrogenase) and EC 1.1.1.22 (UDP-Glc 6-dehydrogenase) within the same family would require more specific substrate-binding-site analysis, but EC 1.1.1.22 is not among the choices, so this does not create ambiguity here.
- EC 1.1.1.336 could not be confidently identified as a valid, well-characterized EC number in the UDP-sugar dehydrogenase family; if it were a valid but unrelated dehydrogenase, the family-motif argument still distinguishes it from the UGDH/WbpO fold.
- The experimental evidence (PubMed 18065759) provides direct enzymatic characterization, strengthening the annotation beyond computational inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'VAVVGLGYVGLPLAVEFG' contains the canonical GxGxxG Rossmann-fold motif (GLGYVGLP), a hallmark of NAD(P)-dependent oxidoreductases, immediately eliminating hydrolase options C (EC 3.6.1.5) and D (EC 3.2.1.31). Within EC 1.1.1.x, the sequence displays multiple motifs diagnostic of the UDP-sugar 6-dehydrogenase (UGDH/WbpO) superfamily: the 'GAYDGIILAVAHSEFKN' segment, the 'GTP' region, and the overall ~420-aa architecture with two domains (NAD-binding + substrate-binding) are characteristic of this family. EC 1.1.1.136 (UDP-GlcNAc 6-dehydrogenase) is a well-known member of this family (alongside EC 1.1.1.22 UDP-Glc 6-dehydrogenase). EC 1.1.1.336 is either not a recognized EC number or does not belong to the UDP-sugar dehydrogenase family; it does not share the diagnostic UGDH-family motifs. Thus, recognizing the Rossmann fold plus UGDH-family sequence signatures from general knowledge of UDP-sugar dehydrogenases across multiple organisms meaningfully distinguishes A from B, C, and D without needing the specific database annotation of this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold GxGxxG motif at the N-terminus is a universally recognized feature of NAD-dependent oxidoreductases, clearly separating EC 1.x.x.x from EC 3.x.x.x choices. The UDP-sugar 6-dehydrogenase family motifs (GAY, GTP, overall domain architecture) are well-documented across homologs (E. coli Ugd, Neisseria, Pseudomonas WbpO family members). EC 1.1.1.136 is the established EC number for UDP-GlcNAc 6-dehydrogenase within this family, while EC 1.1.1.336 is not a recognized member of this superfamily. A knowledgeable model using family-level sequence pattern recognition can meaningfully select A over B, C, and D."
  },
  "case_id": "EC_number_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9RHD7 (WBPO_PSEAI) exactly matches the supplied 422-aa sequence (SHA256 confirmed). EC 1.1.1.136 (UDP-N-acetyl-D-glucosamine 6-dehydrogenase) is annotated with experimental evidence code ECO:0000269 from PubMed 18065759 (Miller et al., JBC 2008), which directly demonstrated the catalytic activity. Both current and historical (entry version 111) records confirm this annotation."
  },
  "important_caveats": [
    "The distinction between EC 1.1.1.136 (UDP-GlcNAc 6-dehydrogenase) and EC 1.1.1.22 (UDP-Glc 6-dehydrogenase) within the same family would require more specific substrate-binding-site analysis, but EC 1.1.1.22 is not among the choices, so this does not create ambiguity here.",
    "EC 1.1.1.336 could not be confidently identified as a valid, well-characterized EC number in the UDP-sugar dehydrogenase family; if it were a valid but unrelated dehydrogenase, the family-motif argument still distinguishes it from the UGDH/WbpO fold.",
    "The experimental evidence (PubMed 18065759) provides direct enzymatic characterization, strengthening the annotation beyond computational inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann fold eliminates C and D. The UGDH-family motifs point specifically to EC 1.1.1.136 rather than the obscure or non-standard EC 1.1.1.336. No other option shares the diagnostic family features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9RHD7 (WBPO_PSEAI) exactly matches the supplied 422-aa sequence (SHA256 confirmed). EC 1.1.1.136 (UDP-N-acetyl-D-glucosamine 6-dehydrogenase) is annotated with experimental evidence code ECO:0000269 from PubMed 18065759 (Miller et al., JBC 2008), which directly demonstrated the catalytic activity. Both current and historical (entry version 111) records confirm this annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region 'VAVVGLGYVGLPLAVEFG' contains the canonical GxGxxG Rossmann-fold motif (GLGYVGLP), a hallmark of NAD(P)-dependent oxidoreductases, immediately eliminating hydrolase options C (EC 3.6.1.5) and D (EC 3.2.1.31). Within EC 1.1.1.x, the sequence displays multiple motifs diagnostic of the UDP-sugar 6-dehydrogenase (UGDH/WbpO) superfamily: the 'GAYDGIILAVAHSEFKN' segment, the 'GTP' region, and the overall ~420-aa architecture with two domains (NAD-binding + substrate-binding) are characteristic of this family. EC 1.1.1.136 (UDP-GlcNAc 6-dehydrogenase) is a well-known member of this family (alongside EC 1.1.1.22 UDP-Glc 6-dehydrogenase). EC 1.1.1.336 is either not a recognized EC number or does not belong to the UDP-sugar dehydrogenase family; it does not share the diagnostic UGDH-family motifs. Thus, recognizing the Rossmann fold plus UGDH-family sequence signatures from general knowledge of UDP-sugar dehydrogenases across multiple organisms meaningfully distinguishes A from B, C, and D without needing the specific database annotation of this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold GxGxxG motif at the N-terminus is a universally recognized feature of NAD-dependent oxidoreductases, clearly separating EC 1.x.x.x from EC 3.x.x.x choices. The UDP-sugar 6-dehydrogenase family motifs (GAY, GTP, overall domain architecture) are well-documented across homologs (E. coli Ugd, Neisseria, Pseudomonas WbpO family members). EC 1.1.1.136 is the established EC number for UDP-GlcNAc 6-dehydrogenase within this family, while EC 1.1.1.336 is not a recognized member of this superfamily. A knowledgeable model using family-level sequence pattern recognition can meaningfully select A over B, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann fold eliminates C and D. The UGDH-family motifs point specifically to EC 1.1.1.136 rather than the obscure or non-standard EC 1.1.1.336. No other option shares the diagnostic family features."
  },
  "important_caveats": [
    "The distinction between EC 1.1.1.136 (UDP-GlcNAc 6-dehydrogenase) and EC 1.1.1.22 (UDP-Glc 6-dehydrogenase) within the same family would require more specific substrate-binding-site analysis, but EC 1.1.1.22 is not among the choices, so this does not create ambiguity here.",
    "EC 1.1.1.336 could not be confidently identified as a valid, well-characterized EC number in the UDP-sugar dehydrogenase family; if it were a valid but unrelated dehydrogenase, the family-motif argument still distinguishes it from the UGDH/WbpO fold.",
    "The experimental evidence (PubMed 18065759) provides direct enzymatic characterization, strengthening the annotation beyond computational inference."
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
  "benchmark_sequence_length": 422,
  "benchmark_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "current_entry_audit": {
    "entryVersion": 113,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 422,
  "current_source_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 111,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9RHD7",
  "selected_historical_entry_version": 111,
  "selected_historical_record_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "selected_historical_source_sequence_length": 422,
  "selected_historical_source_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "selected_historical_version": {
    "accession": "Q9RHD7",
    "database": "Swiss-Prot",
    "entryVersion": 111,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "WBPO_PSEAI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9RHD7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":113,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa\",\"taxonId\":287}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.136\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-D-glucosamine 6-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-GlcNAc 6-dehydrogenase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13326\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.136\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13325\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65040\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Miller W.L.\",\"Matewish M.J.\",\"McNally D.J.\",\"Ishiyama N.\",\"Anderson E.M.\",\"Brewer D.\",\"Brisson J.R.\",\"Berghuis A.M.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18065759\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m708894200\"}],\"citationType\":\"journal article\",\"firstPage\":\"3507\",\"id\":\"18065759\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"3518\",\"publicationDate\":\"2008\",\"title\":\"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.\",\"volume\":\"283\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"PAK / Serotype O6\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H1",
  "excerpt": "ID   WBPO_PSEAI              Reviewed;         422 AA.\nAC   Q9RHD7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 111.\nDE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000305};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000305};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:18065759};\nGN   Name=wbpO {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};\nGN   ORFNames=CAZ10_03215 {ECO:0000312|EMBL:OTI64803.1};\nOS   Pseudomonas aeruginosa.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=287;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000305};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000305};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:18065759};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAF23997.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 33354 / Serotype O6;\nRX   PubMed=10627048; DOI=10.1099/00221287-145-12-3505;\nRA   Belanger M., Burrows L.L., Lam J.S.;\nRT   \"Functional analysis of genes responsible for the synthesis of the B-band O\nRT   antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.\";\nRL   Microbiology 145:3505-3521(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H4",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:AAM27816.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=Serotype O6;\nRX   PubMed=12057956; DOI=10.1128/jb.184.13.3614-3622.2002;\nRA   Raymond C.K., Sims E.H., Kas A., Spencer D.H., Kutyavin T.V., Ivey R.G.,\nRA   Zhou Y., Kaul R., Clendenning J.B., Olson M.V.;\nRT   \"Genetic variation at the O-antigen biosynthetic locus in Pseudomonas\nRT   aeruginosa.\";\nRL   J. Bacteriol. 184:3614-3622(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H5",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=PAK / Serotype O6;\nRX   PubMed=18065759; DOI=10.1074/jbc.m708894200;\nRA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,\nRA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;\nRT   \"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-\nRT   antigen biosynthesis enzyme WbpO.\";\nRL   J. Biol. Chem. 283:3507-3518(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-\nCC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);\nCC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,\nCC         ChEBI:CHEBI:65040; EC=1.1.1.136;\nCC         Evidence={ECO:0000269|PubMed:18065759};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;\nCC         Evidence={ECO:0000269|PubMed:18065759};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 180. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
