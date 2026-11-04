# EC_number_0183

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0183.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 1.14.14.154

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSWPLIGAYALLAFVAIIALNVTYQFLFRLLNKTRPPLVFHWIPFIGSTIHYGMDPYGFFFSCREKYGDIFTFILLGRPTTVYLGTQGNEFILNGKLKDVNAEEVYSPLTTPVFGSDVVYDCPNSKLIEQKKFIKFGLSQTALEAHVPLIEKEVEDYLAMSPNFHGTSGEVDITAAMAEITIFTAGSALQGEEVRSKLTTEFAVLYHDLDKGFTPINFMLPWAPLPHNKKRDAAHARMRAIYIDIINKRRNAGDNVPEKLDMIGNLMQCTYKNGQPLPDKEIAHIMITLLMAGQHSSSSISSWIMLRLASQPAVVEELYQEQLANLERTGPNNSLAPLQYKDFDNLPLHQNVIRETLRLNSSIHSLMRKVKNPLPVPGTPYVIPTSHVLLSAPGVTALSDEYFPNAMAWDPHRWETQAPKENDKDDIVDYGYGAISKGTSSPYLPFGAGRHRCIGEKFAYLNLAVIVATMVRHLRFSNLDGQTGVPATDYSSLFSGPMKPARIRWERRAAKSG

[Multiple Choices]
A. 1.14.14.126
B. 1.14.14.154
C. 1.1.1.1
D. 3.4.21.90
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

> The sequence-matched UniProt entry assigns EC 1.14.14.154 to this protein and cites experimental evidence for that assignment. The historical entry also records the same EC number; the cited annotation supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the architecture and conserved heme-binding region expected of a cytochrome P450, including a hydrophobic N-terminal membrane anchor and a Cys-containing P450 heme-binding motif. Transferable knowledge of CYP51 sterol 14-alpha-demethylases identifies a plausible P450 family whose reaction is classified as EC 1.14.14.154, distinguishing B from the non-P450 choices and, with family recognition, from the other P450 option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and knowledge of related CYP51 enzymes provides a meaningful basis for choosing B. The P450 features alone are not uniquely diagnostic, so recognizing the CYP51 family is the important step; the exact enzyme assignment is not directly stated in the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives correspond to substantially different enzyme activities, and the CYP51-family inference supports B rather than the other listed choices.


### Important caveats

- A generic P450 motif by itself does not establish CYP51 identity; the inference depends on broader family recognition or comparison with related proteins.
- The source annotation cites experimental evidence, but the underlying paper was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the architecture and conserved heme-binding region expected of a cytochrome P450, including a hydrophobic N-terminal membrane anchor and a Cys-containing P450 heme-binding motif. Transferable knowledge of CYP51 sterol 14-alpha-demethylases identifies a plausible P450 family whose reaction is classified as EC 1.14.14.154, distinguishing B from the non-P450 choices and, with family recognition, from the other P450 option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and knowledge of related CYP51 enzymes provides a meaningful basis for choosing B. The P450 features alone are not uniquely diagnostic, so recognizing the CYP51 family is the important step; the exact enzyme assignment is not directly stated in the input."
  },
  "case_id": "EC_number_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 1.14.14.154 to this protein and cites experimental evidence for that assignment. The historical entry also records the same EC number; the cited annotation supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "A generic P450 motif by itself does not establish CYP51 identity; the inference depends on broader family recognition or comparison with related proteins.",
    "The source annotation cites experimental evidence, but the underlying paper was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives correspond to substantially different enzyme activities, and the CYP51-family inference supports B rather than the other listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 1.14.14.154 to this protein and cites experimental evidence for that assignment. The historical entry also records the same EC number; the cited annotation supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the architecture and conserved heme-binding region expected of a cytochrome P450, including a hydrophobic N-terminal membrane anchor and a Cys-containing P450 heme-binding motif. Transferable knowledge of CYP51 sterol 14-alpha-demethylases identifies a plausible P450 family whose reaction is classified as EC 1.14.14.154, distinguishing B from the non-P450 choices and, with family recognition, from the other P450 option.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and knowledge of related CYP51 enzymes provides a meaningful basis for choosing B. The P450 features alone are not uniquely diagnostic, so recognizing the CYP51 family is the important step; the exact enzyme assignment is not directly stated in the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives correspond to substantially different enzyme activities, and the CYP51-family inference supports B rather than the other listed choices."
  },
  "important_caveats": [
    "A generic P450 motif by itself does not establish CYP51 identity; the inference depends on broader family recognition or comparison with related proteins.",
    "The source annotation cites experimental evidence, but the underlying paper was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0L1JEW4 (RSTN2_ASPN3) explicitly assigns EC 1.14.14.154 as the recommended EC number, with evidence code ECO:0000269 (direct experimental evidence) from PubMed:33857369. The recommended name is 'Sterol 14-alpha demethylase rstn2' and multiple catalytic activity entries (lanosterol and eburicol 14α-demethylation) are annotated under EC 1.14.14.154. The sequence in the benchmark matches the UniProt sequence exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [C13](#evidence-c13), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H8](#evidence-h8), [H12](#evidence-h12).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif 'GRHRCIGEK' (FxxGxxxCxG pattern with the invariant Cys coordinating heme iron), confirming membership in the P450 superfamily (EC class 1.14.14.x). This immediately eliminates C (1.1.1.1, alcohol dehydrogenase) and D (3.4.21.90, serine protease), which belong to entirely different enzyme classes. The protein is ~513 aa with an N-terminal hydrophobic transmembrane anchor, consistent with microsomal fungal P450s. Among the remaining P450 options, CYP51 (sterol 14α-demethylase) is one of the most extensively characterized P450 families in fungi, involved in ergosterol biosynthesis. The substrate-binding pocket of CYP51 is adapted for the steroid/sterol nucleus, and the overall architecture (length, TM anchor, active-site geometry) is well-known from numerous fungal CYP51 homologs (e.g., yeast ERG11, Candida CYP51). A model recognizing CYP51-family features—such as the acidic pocket residues, the I-helix region, and the sterol-adapted substrate channel—can favor 1.14.14.154 (fungal sterol 14α-demethylase) over 1.14.14.126, which would correspond to a P450 acting on a different substrate class. The family-level inference from well-characterized CYP51 homologs provides a credible basis for selecting B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P450 identification via the heme-binding motif is unambiguous from the sequence. The CYP51/sterol-demethylase family is among the best-studied P450 families, and its sequence and structural signatures are transferable knowledge from many characterized homologs. Distinguishing 1.14.14.154 from 1.14.14.126 relies on recognizing CYP51-specific active-site features (steroid-binding pocket, conserved SRS residues) versus a P450 acting on a non-steroid substrate. This is a defensible family-level inference, though the A-vs-B distinction is finer than the C/D eliminations.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly incompatible with a P450. The distinction between A (1.14.14.126) and B (1.14.14.154) is fine-grained, but CYP51-family recognition provides a credible basis for selecting B. Without independent confirmation of what EC 1.14.14.126 specifically catalyzes, there is a minor residual uncertainty, but it does not rise to the level of genuine ambiguity between the offered choices.


### Important caveats

- The distinction between EC 1.14.14.126 and 1.14.14.154 is fine-grained; both are P450s (1.14.14.x). The argument relies on recognizing CYP51/sterol-demethylase family features and assuming 1.14.14.126 corresponds to a P450 with a different substrate specificity.
- The UniProt annotation for EC 1.14.14.154 carries experimental evidence (ECO:0000269, PubMed:33857369) for the recommended name, but the detailed catalytic reaction annotations are largely by similarity (ECO:0000250) to Q4WNT5 and P10614.
- The reviewer-only evidence confirms the sequence matches UniProt A0A0L1JEW4 exactly, but this accession and organism identity were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'GRHRCIGEK' (FxxGxxxCxG pattern with the invariant Cys coordinating heme iron), confirming membership in the P450 superfamily (EC class 1.14.14.x). This immediately eliminates C (1.1.1.1, alcohol dehydrogenase) and D (3.4.21.90, serine protease), which belong to entirely different enzyme classes. The protein is ~513 aa with an N-terminal hydrophobic transmembrane anchor, consistent with microsomal fungal P450s. Among the remaining P450 options, CYP51 (sterol 14α-demethylase) is one of the most extensively characterized P450 families in fungi, involved in ergosterol biosynthesis. The substrate-binding pocket of CYP51 is adapted for the steroid/sterol nucleus, and the overall architecture (length, TM anchor, active-site geometry) is well-known from numerous fungal CYP51 homologs (e.g., yeast ERG11, Candida CYP51). A model recognizing CYP51-family features—such as the acidic pocket residues, the I-helix region, and the sterol-adapted substrate channel—can favor 1.14.14.154 (fungal sterol 14α-demethylase) over 1.14.14.126, which would correspond to a P450 acting on a different substrate class. The family-level inference from well-characterized CYP51 homologs provides a credible basis for selecting B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P450 identification via the heme-binding motif is unambiguous from the sequence. The CYP51/sterol-demethylase family is among the best-studied P450 families, and its sequence and structural signatures are transferable knowledge from many characterized homologs. Distinguishing 1.14.14.154 from 1.14.14.126 relies on recognizing CYP51-specific active-site features (steroid-binding pocket, conserved SRS residues) versus a P450 acting on a non-steroid substrate. This is a defensible family-level inference, though the A-vs-B distinction is finer than the C/D eliminations."
  },
  "case_id": "EC_number_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "C13",
      "H1",
      "H2",
      "H4",
      "H8",
      "H12"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0L1JEW4 (RSTN2_ASPN3) explicitly assigns EC 1.14.14.154 as the recommended EC number, with evidence code ECO:0000269 (direct experimental evidence) from PubMed:33857369. The recommended name is 'Sterol 14-alpha demethylase rstn2' and multiple catalytic activity entries (lanosterol and eburicol 14α-demethylation) are annotated under EC 1.14.14.154. The sequence in the benchmark matches the UniProt sequence exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The distinction between EC 1.14.14.126 and 1.14.14.154 is fine-grained; both are P450s (1.14.14.x). The argument relies on recognizing CYP51/sterol-demethylase family features and assuming 1.14.14.126 corresponds to a P450 with a different substrate specificity.",
    "The UniProt annotation for EC 1.14.14.154 carries experimental evidence (ECO:0000269, PubMed:33857369) for the recommended name, but the detailed catalytic reaction annotations are largely by similarity (ECO:0000250) to Q4WNT5 and P10614.",
    "The reviewer-only evidence confirms the sequence matches UniProt A0A0L1JEW4 exactly, but this accession and organism identity were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with a P450. The distinction between A (1.14.14.126) and B (1.14.14.154) is fine-grained, but CYP51-family recognition provides a credible basis for selecting B. Without independent confirmation of what EC 1.14.14.126 specifically catalyzes, there is a minor residual uncertainty, but it does not rise to the level of genuine ambiguity between the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0L1JEW4 (RSTN2_ASPN3) explicitly assigns EC 1.14.14.154 as the recommended EC number, with evidence code ECO:0000269 (direct experimental evidence) from PubMed:33857369. The recommended name is 'Sterol 14-alpha demethylase rstn2' and multiple catalytic activity entries (lanosterol and eburicol 14α-demethylation) are annotated under EC 1.14.14.154. The sequence in the benchmark matches the UniProt sequence exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C9", "C13", "H1", "H2", "H4", "H8", "H12"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'GRHRCIGEK' (FxxGxxxCxG pattern with the invariant Cys coordinating heme iron), confirming membership in the P450 superfamily (EC class 1.14.14.x). This immediately eliminates C (1.1.1.1, alcohol dehydrogenase) and D (3.4.21.90, serine protease), which belong to entirely different enzyme classes. The protein is ~513 aa with an N-terminal hydrophobic transmembrane anchor, consistent with microsomal fungal P450s. Among the remaining P450 options, CYP51 (sterol 14α-demethylase) is one of the most extensively characterized P450 families in fungi, involved in ergosterol biosynthesis. The substrate-binding pocket of CYP51 is adapted for the steroid/sterol nucleus, and the overall architecture (length, TM anchor, active-site geometry) is well-known from numerous fungal CYP51 homologs (e.g., yeast ERG11, Candida CYP51). A model recognizing CYP51-family features—such as the acidic pocket residues, the I-helix region, and the sterol-adapted substrate channel—can favor 1.14.14.154 (fungal sterol 14α-demethylase) over 1.14.14.126, which would correspond to a P450 acting on a different substrate class. The family-level inference from well-characterized CYP51 homologs provides a credible basis for selecting B.",
    "missing_item_specific_fact": "",
    "reason": "The P450 identification via the heme-binding motif is unambiguous from the sequence. The CYP51/sterol-demethylase family is among the best-studied P450 families, and its sequence and structural signatures are transferable knowledge from many characterized homologs. Distinguishing 1.14.14.154 from 1.14.14.126 relies on recognizing CYP51-specific active-site features (steroid-binding pocket, conserved SRS residues) versus a P450 acting on a non-steroid substrate. This is a defensible family-level inference, though the A-vs-B distinction is finer than the C/D eliminations."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with a P450. The distinction between A (1.14.14.126) and B (1.14.14.154) is fine-grained, but CYP51-family recognition provides a credible basis for selecting B. Without independent confirmation of what EC 1.14.14.126 specifically catalyzes, there is a minor residual uncertainty, but it does not rise to the level of genuine ambiguity between the offered choices."
  },
  "important_caveats": [
    "The distinction between EC 1.14.14.126 and 1.14.14.154 is fine-grained; both are P450s (1.14.14.x). The argument relies on recognizing CYP51/sterol-demethylase family features and assuming 1.14.14.126 corresponds to a P450 with a different substrate specificity.",
    "The UniProt annotation for EC 1.14.14.154 carries experimental evidence (ECO:0000269, PubMed:33857369) for the recommended name, but the detailed catalytic reaction annotations are largely by similarity (ECO:0000250) to Q4WNT5 and P10614.",
    "The reviewer-only evidence confirms the sequence matches UniProt A0A0L1JEW4 exactly, but this accession and organism identity were not available to the evaluated model."
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
  "benchmark_sequence_length": 513,
  "benchmark_sequence_sha256": "19c16af699d50913a7bf4f55defbf96b0893917eaeb57b66b0dc53dd081e1b3c",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-11-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 513,
  "current_source_sequence_sha256": "19c16af699d50913a7bf4f55defbf96b0893917eaeb57b66b0dc53dd081e1b3c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0L1JEW4",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "selected_historical_source_sequence_length": 513,
  "selected_historical_source_sequence_sha256": "19c16af699d50913a7bf4f55defbf96b0893917eaeb57b66b0dc53dd081e1b3c",
  "selected_historical_version": {
    "accession": "A0A0L1JEW4",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RSTN2_ASPN3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0L1JEW4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-11-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 / M93)\",\"taxonId\":1509407}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase rstn2\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Ergosterol biosynthesis protein rstn2\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein 2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.154\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Sterol 14-alpha demethylase rstn2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:54029\"}}],\"reaction\":{\"ecNumber\":\"1.14.14.154\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:54028\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138029\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138031\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:68061\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-methyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:68060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138029\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176901\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:68065\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:68064\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176901\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176902\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:68069\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-formyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a Delta(14) steroid + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:68068\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176902\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:25287\"}}],\"reaction\":{\"ecNumber\":\"1.14.14.154\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"name\":\"lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:25286\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16521\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17813\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75104\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"lanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-hydroxylanosterol + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75103\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16521\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166806\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75108\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-hydroxylanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-oxolanosterol + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75107\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166681\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166806\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/7",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75112\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-oxolanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75111\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17813\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166681\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/8",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75440\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"name\":\"eburicol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 14-demethyleburicol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75439\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194330\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/9",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75428\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"eburicol + reduced [NADPH--hemoprotein reductase] + O2 = 32-hydroxyeburicol + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75427\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194328\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/10",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75432\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-hydroxyeburicol + reduced [NADPH--hemoprotein reductase] + O2 = 32-oxoeburicol + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75431\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194328\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194329\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/11",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75436\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-oxoeburicol + reduced [NADPH--hemoprotein reductase] + O2 = 14-demethyleburicol + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75435\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194329\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194330\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/12",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   RSTN2_ASPN3             Reviewed;         513 AA.\nAC   A0A0L1JEW4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-NOV-2015, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Sterol 14-alpha demethylase rstn2 {ECO:0000303|PubMed:33857369};\nDE            EC=1.14.14.154 {ECO:0000269|PubMed:33857369};\nDE   AltName: Full=Cytochrome P450 monooxygenase rstn2 {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Ergosterol biosynthesis protein rstn2 {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Restricticin biosynthesis cluster protein 2 {ECO:0000303|PubMed:33857369};\nGN   Name=rstn2 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001443;\nOS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /\nOS   M93).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=1509407;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Sterol 14-alpha demethylase rstn2 {ECO:0000303|PubMed:33857369};\nDE            EC=1.14.14.154 {ECO:0000269|PubMed:33857369};\nDE   AltName: Full=Cytochrome P450 monooxygenase rstn2 {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Ergosterol biosynthesis protein rstn2 {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Restricticin biosynthesis cluster protein 2 {ECO:0000303|PubMed:33857369};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein\nCC         reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized\nCC         [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);\nCC         Xref=Rhea:RHEA:54028, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,\nCC         ChEBI:CHEBI:138029, ChEBI:CHEBI:138031; EC=1.14.14.154;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:54029;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-methyl steroid + reduced [NADPH--hemoprotein\nCC         reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--\nCC         hemoprotein reductase] + H2O + H(+); Xref=Rhea:RHEA:68060, Rhea:RHEA-\nCC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:138029, ChEBI:CHEBI:176901;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:68061;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein\nCC         reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--\nCC         hemoprotein reductase] + 2 H2O + H(+); Xref=Rhea:RHEA:68064,\nCC         Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:176901, ChEBI:CHEBI:176902;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:68065;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-formyl steroid + reduced [NADPH--hemoprotein\nCC         reductase] + O2 = a Delta(14) steroid + formate + oxidized [NADPH--\nCC         hemoprotein reductase] + H2O + 2 H(+); Xref=Rhea:RHEA:68068,\nCC         Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:138031,\nCC         ChEBI:CHEBI:176902; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:68069;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 =\nCC         4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3\nCC         oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);\nCC         Xref=Rhea:RHEA:25286, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:16521, ChEBI:CHEBI:17813,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210; EC=1.14.14.154;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:25287;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=lanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-\nCC         hydroxylanosterol + oxidized [NADPH--hemoprotein reductase] + H2O +\nCC         H(+); Xref=Rhea:RHEA:75103, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:16521, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,\nCC         ChEBI:CHEBI:166806; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75104;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-hydroxylanosterol + reduced [NADPH--hemoprotein reductase]\nCC         + O2 = 32-oxolanosterol + oxidized [NADPH--hemoprotein reductase] + 2\nCC         H2O + H(+); Xref=Rhea:RHEA:75107, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:166681,\nCC         ChEBI:CHEBI:166806; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75108;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H11",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-oxolanosterol + reduced [NADPH--hemoprotein reductase] + O2\nCC         = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate +\nCC         oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+);\nCC         Xref=Rhea:RHEA:75111, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:17813, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:166681;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75112;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H12",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=eburicol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 =\nCC         14-demethyleburicol + formate + 3 oxidized [NADPH--hemoprotein\nCC         reductase] + 4 H2O + 4 H(+); Xref=Rhea:RHEA:75439, Rhea:RHEA-\nCC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:70315,\nCC         ChEBI:CHEBI:194330; Evidence={ECO:0000250|UniProtKB:Q4WNT5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75440;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H13",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=eburicol + reduced [NADPH--hemoprotein reductase] + O2 = 32-\nCC         hydroxyeburicol + oxidized [NADPH--hemoprotein reductase] + H2O +\nCC         H(+); Xref=Rhea:RHEA:75427, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:70315,\nCC         ChEBI:CHEBI:194328; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75428;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 135-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H14",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-hydroxyeburicol + reduced [NADPH--hemoprotein reductase] +\nCC         O2 = 32-oxoeburicol + oxidized [NADPH--hemoprotein reductase] + 2 H2O\nCC         + H(+); Xref=Rhea:RHEA:75431, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:194328,\nCC         ChEBI:CHEBI:194329; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75432;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H15",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-oxoeburicol + reduced [NADPH--hemoprotein reductase] + O2 =\nCC         14-demethyleburicol + formate + oxidized [NADPH--hemoprotein\nCC         reductase] + H2O + 2 H(+); Xref=Rhea:RHEA:75435, Rhea:RHEA-\nCC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:194329,\nCC         ChEBI:CHEBI:194330; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75436;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 183. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
