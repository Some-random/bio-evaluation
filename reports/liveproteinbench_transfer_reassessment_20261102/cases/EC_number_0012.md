# EC_number_0012

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0012.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.14.14.154

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSILWIVAYALLAFAASIALNLVYQFLYRTFNKSRPPLVFHWVPFIGSTIHYGMDPYNFFFSCREKYGDIFTFILLGRPTTVYLGTQGNEFILNGKLKDVNAEEVYSPLTTPVFGSDVVYDCPNSKLIEQKKFIKFGLSQAALEAHVPLIEKEVIDYLAQSPNFNGTAGTVDIASAMAEITIFTAGSTLQGEEVRSKLTTEFAVLYHDLDKGFTPINFMLPWAPLPHNKKRDAAHARMRAIYIDIINKRRKAGNAATGKPDMIENLMQCTYKNGQPLPDKEIAHIMITLLMAGQHSSSSIGSWIMLRLASQPAIVEELYQEQLANLERTANGSLPPLQFKDIENLPLHQNVIRETLRLHGSIHSLLRKVKNPLPVPGTPYIIPTSHVLLSAPGVTALSDEYFPNAMAWDPHRWETQAPEESKEDIVDYGYGAMSKGTSSPYLPFGAGRHRCIGEKFAYLNLTVIVATLVRHLRFHNLDGKKGVPGTDYTSLFSGPLKPTRVGWERRAAKSA

[Multiple Choices]
A. 1.14.14.126
B. 3.2.1.20
C. 1.1.1.336
D. 1.14.14.154
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

> The sequence-matched UniProt record assigns EC 1.14.14.154 and describes the protein as a sterol 14-alpha demethylase. The catalytic-activity annotations include the corresponding sterol demethylation reaction. These assignments are supported by transfer from homologs, rather than establishing direct experimental verification of this exact protein's activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal membrane anchor and conserved cytochrome P450 features, including the heme-binding cysteine region. More specifically, its length and sequence pattern are consistent with fungal CYP51 sterol 14-alpha-demethylases. Family-level knowledge links CYP51 enzymes to sterol 14-alpha demethylation (EC 1.14.14.154), distinguishing D from the glycosidase and dehydrogenase choices and the other P450 option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence supports a transferable family-level inference to CYP51 and its characteristic sterol-demethylation activity. The exact four-digit assignment is not certain from generic P450 features alone, but the more specific family pattern meaningfully distinguishes the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the sequence's CYP51-like features and associated sterol-demethylase activity.


### Important caveats

- The cited database EC and catalytic activity annotations are based on evidence transferred from homologs; they should not be represented as direct experimental demonstration for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal membrane anchor and conserved cytochrome P450 features, including the heme-binding cysteine region. More specifically, its length and sequence pattern are consistent with fungal CYP51 sterol 14-alpha-demethylases. Family-level knowledge links CYP51 enzymes to sterol 14-alpha demethylation (EC 1.14.14.154), distinguishing D from the glycosidase and dehydrogenase choices and the other P450 option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports a transferable family-level inference to CYP51 and its characteristic sterol-demethylation activity. The exact four-digit assignment is not certain from generic P450 features alone, but the more specific family pattern meaningfully distinguishes the offered alternatives."
  },
  "case_id": "EC_number_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.14.14.154 and describes the protein as a sterol 14-alpha demethylase. The catalytic-activity annotations include the corresponding sterol demethylation reaction. These assignments are supported by transfer from homologs, rather than establishing direct experimental verification of this exact protein's activity."
  },
  "important_caveats": [
    "The cited database EC and catalytic activity annotations are based on evidence transferred from homologs; they should not be represented as direct experimental demonstration for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence's CYP51-like features and associated sterol-demethylase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.14.14.154 and describes the protein as a sterol 14-alpha demethylase. The catalytic-activity annotations include the corresponding sterol demethylation reaction. These assignments are supported by transfer from homologs, rather than establishing direct experimental verification of this exact protein's activity.",
    "evidence_ids": ["C4", "C5", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal membrane anchor and conserved cytochrome P450 features, including the heme-binding cysteine region. More specifically, its length and sequence pattern are consistent with fungal CYP51 sterol 14-alpha-demethylases. Family-level knowledge links CYP51 enzymes to sterol 14-alpha demethylation (EC 1.14.14.154), distinguishing D from the glycosidase and dehydrogenase choices and the other P450 option.",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports a transferable family-level inference to CYP51 and its characteristic sterol-demethylation activity. The exact four-digit assignment is not certain from generic P450 features alone, but the more specific family pattern meaningfully distinguishes the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence's CYP51-like features and associated sterol-demethylase activity."
  },
  "important_caveats": [
    "The cited database EC and catalytic activity annotations are based on evidence transferred from homologs; they should not be represented as direct experimental demonstration for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU9 (RESB_ASPSL) annotates this 511-aa protein as 'Sterol 14-alpha demethylase resB' with EC 1.14.14.154. The EC assignment carries evidence code ECO:0000250 (similarity to A0A0L1JEW4 and Q4WNT5), and the entry also cites experimental evidence from PubMed:39105744 for FUNCTION, CATALYTIC ACTIVITY, and PATHWAY. The listed catalytic activities (lanosterol → 4,4-dimethyl-5α-cholesta-8,14,24-trien-3β-ol + formate; eburicol → 14-demethyleburicol + formate) are the canonical three-step 14α-demethylation reaction of CYP51/sterol 14α-demethylase, matching EC 1.14.14.154. The annotation is primarily by similarity but corroborated by experimental pathway data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [C13](#evidence-c13), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H8](#evidence-h8), [H12](#evidence-h12).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Step 1 – P450 recognition: The sequence contains the canonical heme-binding motif 'FGAGRHRCIGE' (FxxGxRxCxG) near the C-terminus, a ~511-aa length typical of fungal microsomal P450s, and an N-terminal hydrophobic membrane-anchor region. This unambiguously identifies the protein as a cytochrome P450 monooxygenase (EC class 1.14.14.x), eliminating B (3.2.1.20, α-galactosidase – a glycoside hydrolase with a completely different TIM-barrel fold) and C (1.1.1.336, an NAD-dependent alcohol dehydrogenase – a Rossmann-fold oxidoreductase). Step 2 – CYP51 family identification: Among the remaining P450 choices (A: 1.14.14.126 vs D: 1.14.14.154), sterol 14α-demethylase (CYP51) is one of the most universally conserved P450 families across all eukaryotes and is the essential ergosterol-biosynthesis enzyme in fungi. Recognizable CYP51 features in this sequence include the I-helix region with the conserved 'AG' motif (visible as 'AGQHSSSSIGSWIMLRL'), the overall domain architecture matching known fungal CYP51 sequences (~500-550 aa, N-terminal ER anchor, conserved SRS substrate-binding pocket), and the characteristic 'IAG' tripeptide in the I-helix. EC 1.14.14.126 refers to a different, less common P450 substrate specificity. Transferable knowledge of fungal ergosterol biosynthesis pathways and the extreme conservation of CYP51 across fungi provides a credible basis for selecting 1.14.14.154 over 1.14.14.126.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P450 classification is directly readable from the heme-binding motif and overall architecture, eliminating B and C. Distinguishing between two P450 EC numbers (A vs D) is harder, but CYP51/sterol 14α-demethylase is the single most conserved and well-characterized P450 family in fungi, with well-documented sequence signatures (I-helix 'IAG', SRS residues, N-terminal ER anchor, ~511 aa length) that are transferable knowledge from studying CYP51 homologs across fungi. A knowledgeable model recognizing these CYP51 signatures can reasonably select 1.14.14.154 over the alternative P450 EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and C are clearly eliminated by P450 recognition. Between A and D, both are P450s, but the CYP51-specific sequence signatures and the dominance of sterol 14α-demethylase in fungal P450 biology make D the strongly preferred answer. EC 1.14.14.126 corresponds to a different substrate specificity and would not match the observed CYP51-like SRS architecture.


### Important caveats

- The UniProt EC annotation for P0DXU9 is primarily by similarity (ECO:0000250) to A0A0L1JEW4 and Q4WNT5, not from direct in-vitro enzyme kinetics on this exact protein, though the 2024 PubMed paper provides experimental pathway and catalytic activity evidence.
- Distinguishing between two specific 4-digit P450 EC numbers from sequence alone is inherently challenging; the argument relies on CYP51 family-level conservation rather than a single diagnostic residue unique to 1.14.14.154.
- EC 1.14.14.126 is a valid P450 EC number for a different substrate; its specific identity and substrate specificity would need to be checked to fully rule it out, but the CYP51 signatures in this sequence strongly favor 1.14.14.154.
- The reviewer-only UniProt accession and organism (Aspergillus sclerotiorum) were not available to the evaluated model; the reasoning above relies only on the sequence and general P450/CYP51 knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Step 1 – P450 recognition: The sequence contains the canonical heme-binding motif 'FGAGRHRCIGE' (FxxGxRxCxG) near the C-terminus, a ~511-aa length typical of fungal microsomal P450s, and an N-terminal hydrophobic membrane-anchor region. This unambiguously identifies the protein as a cytochrome P450 monooxygenase (EC class 1.14.14.x), eliminating B (3.2.1.20, α-galactosidase – a glycoside hydrolase with a completely different TIM-barrel fold) and C (1.1.1.336, an NAD-dependent alcohol dehydrogenase – a Rossmann-fold oxidoreductase). Step 2 – CYP51 family identification: Among the remaining P450 choices (A: 1.14.14.126 vs D: 1.14.14.154), sterol 14α-demethylase (CYP51) is one of the most universally conserved P450 families across all eukaryotes and is the essential ergosterol-biosynthesis enzyme in fungi. Recognizable CYP51 features in this sequence include the I-helix region with the conserved 'AG' motif (visible as 'AGQHSSSSIGSWIMLRL'), the overall domain architecture matching known fungal CYP51 sequences (~500-550 aa, N-terminal ER anchor, conserved SRS substrate-binding pocket), and the characteristic 'IAG' tripeptide in the I-helix. EC 1.14.14.126 refers to a different, less common P450 substrate specificity. Transferable knowledge of fungal ergosterol biosynthesis pathways and the extreme conservation of CYP51 across fungi provides a credible basis for selecting 1.14.14.154 over 1.14.14.126.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P450 classification is directly readable from the heme-binding motif and overall architecture, eliminating B and C. Distinguishing between two P450 EC numbers (A vs D) is harder, but CYP51/sterol 14α-demethylase is the single most conserved and well-characterized P450 family in fungi, with well-documented sequence signatures (I-helix 'IAG', SRS residues, N-terminal ER anchor, ~511 aa length) that are transferable knowledge from studying CYP51 homologs across fungi. A knowledgeable model recognizing these CYP51 signatures can reasonably select 1.14.14.154 over the alternative P450 EC number."
  },
  "case_id": "EC_number_0012",
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
    "reason": "The UniProt entry P0DXU9 (RESB_ASPSL) annotates this 511-aa protein as 'Sterol 14-alpha demethylase resB' with EC 1.14.14.154. The EC assignment carries evidence code ECO:0000250 (similarity to A0A0L1JEW4 and Q4WNT5), and the entry also cites experimental evidence from PubMed:39105744 for FUNCTION, CATALYTIC ACTIVITY, and PATHWAY. The listed catalytic activities (lanosterol → 4,4-dimethyl-5α-cholesta-8,14,24-trien-3β-ol + formate; eburicol → 14-demethyleburicol + formate) are the canonical three-step 14α-demethylation reaction of CYP51/sterol 14α-demethylase, matching EC 1.14.14.154. The annotation is primarily by similarity but corroborated by experimental pathway data."
  },
  "important_caveats": [
    "The UniProt EC annotation for P0DXU9 is primarily by similarity (ECO:0000250) to A0A0L1JEW4 and Q4WNT5, not from direct in-vitro enzyme kinetics on this exact protein, though the 2024 PubMed paper provides experimental pathway and catalytic activity evidence.",
    "Distinguishing between two specific 4-digit P450 EC numbers from sequence alone is inherently challenging; the argument relies on CYP51 family-level conservation rather than a single diagnostic residue unique to 1.14.14.154.",
    "EC 1.14.14.126 is a valid P450 EC number for a different substrate; its specific identity and substrate specificity would need to be checked to fully rule it out, but the CYP51 signatures in this sequence strongly favor 1.14.14.154.",
    "The reviewer-only UniProt accession and organism (Aspergillus sclerotiorum) were not available to the evaluated model; the reasoning above relies only on the sequence and general P450/CYP51 knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and C are clearly eliminated by P450 recognition. Between A and D, both are P450s, but the CYP51-specific sequence signatures and the dominance of sterol 14α-demethylase in fungal P450 biology make D the strongly preferred answer. EC 1.14.14.126 corresponds to a different substrate specificity and would not match the observed CYP51-like SRS architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU9 (RESB_ASPSL) annotates this 511-aa protein as 'Sterol 14-alpha demethylase resB' with EC 1.14.14.154. The EC assignment carries evidence code ECO:0000250 (similarity to A0A0L1JEW4 and Q4WNT5), and the entry also cites experimental evidence from PubMed:39105744 for FUNCTION, CATALYTIC ACTIVITY, and PATHWAY. The listed catalytic activities (lanosterol → 4,4-dimethyl-5α-cholesta-8,14,24-trien-3β-ol + formate; eburicol → 14-demethyleburicol + formate) are the canonical three-step 14α-demethylation reaction of CYP51/sterol 14α-demethylase, matching EC 1.14.14.154. The annotation is primarily by similarity but corroborated by experimental pathway data.",
    "evidence_ids": ["C4", "C5", "C9", "C13", "H1", "H2", "H4", "H8", "H12"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Step 1 – P450 recognition: The sequence contains the canonical heme-binding motif 'FGAGRHRCIGE' (FxxGxRxCxG) near the C-terminus, a ~511-aa length typical of fungal microsomal P450s, and an N-terminal hydrophobic membrane-anchor region. This unambiguously identifies the protein as a cytochrome P450 monooxygenase (EC class 1.14.14.x), eliminating B (3.2.1.20, α-galactosidase – a glycoside hydrolase with a completely different TIM-barrel fold) and C (1.1.1.336, an NAD-dependent alcohol dehydrogenase – a Rossmann-fold oxidoreductase). Step 2 – CYP51 family identification: Among the remaining P450 choices (A: 1.14.14.126 vs D: 1.14.14.154), sterol 14α-demethylase (CYP51) is one of the most universally conserved P450 families across all eukaryotes and is the essential ergosterol-biosynthesis enzyme in fungi. Recognizable CYP51 features in this sequence include the I-helix region with the conserved 'AG' motif (visible as 'AGQHSSSSIGSWIMLRL'), the overall domain architecture matching known fungal CYP51 sequences (~500-550 aa, N-terminal ER anchor, conserved SRS substrate-binding pocket), and the characteristic 'IAG' tripeptide in the I-helix. EC 1.14.14.126 refers to a different, less common P450 substrate specificity. Transferable knowledge of fungal ergosterol biosynthesis pathways and the extreme conservation of CYP51 across fungi provides a credible basis for selecting 1.14.14.154 over 1.14.14.126.",
    "missing_item_specific_fact": "",
    "reason": "The P450 classification is directly readable from the heme-binding motif and overall architecture, eliminating B and C. Distinguishing between two P450 EC numbers (A vs D) is harder, but CYP51/sterol 14α-demethylase is the single most conserved and well-characterized P450 family in fungi, with well-documented sequence signatures (I-helix 'IAG', SRS residues, N-terminal ER anchor, ~511 aa length) that are transferable knowledge from studying CYP51 homologs across fungi. A knowledgeable model recognizing these CYP51 signatures can reasonably select 1.14.14.154 over the alternative P450 EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and C are clearly eliminated by P450 recognition. Between A and D, both are P450s, but the CYP51-specific sequence signatures and the dominance of sterol 14α-demethylase in fungal P450 biology make D the strongly preferred answer. EC 1.14.14.126 corresponds to a different substrate specificity and would not match the observed CYP51-like SRS architecture."
  },
  "important_caveats": [
    "The UniProt EC annotation for P0DXU9 is primarily by similarity (ECO:0000250) to A0A0L1JEW4 and Q4WNT5, not from direct in-vitro enzyme kinetics on this exact protein, though the 2024 PubMed paper provides experimental pathway and catalytic activity evidence.",
    "Distinguishing between two specific 4-digit P450 EC numbers from sequence alone is inherently challenging; the argument relies on CYP51 family-level conservation rather than a single diagnostic residue unique to 1.14.14.154.",
    "EC 1.14.14.126 is a valid P450 EC number for a different substrate; its specific identity and substrate specificity would need to be checked to fully rule it out, but the CYP51 signatures in this sequence strongly favor 1.14.14.154.",
    "The reviewer-only UniProt accession and organism (Aspergillus sclerotiorum) were not available to the evaluated model; the reasoning above relies only on the sequence and general P450/CYP51 knowledge."
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
  "benchmark_sequence_length": 511,
  "benchmark_sequence_sha256": "a64d471b7671e38c6cea7bce97558a2ede1a3a938dacb056f2034f73583fb71d",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 511,
  "current_source_sequence_sha256": "a64d471b7671e38c6cea7bce97558a2ede1a3a938dacb056f2034f73583fb71d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXU9",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "selected_historical_source_sequence_length": 511,
  "selected_historical_source_sequence_sha256": "a64d471b7671e38c6cea7bce97558a2ede1a3a938dacb056f2034f73583fb71d",
  "selected_historical_version": {
    "accession": "P0DXU9",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RESB_ASPSL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus sclerotiorum\",\"taxonId\":138282}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase resB\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Ergosterol biosynthesis protein resB\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein B\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0L1JEW4\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.14.154\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Sterol 14-alpha demethylase resB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:54029\"}}],\"reaction\":{\"ecNumber\":\"1.14.14.154\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:54028\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138029\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138031\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:68061\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-methyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:68060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138029\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176901\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:68065\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:68064\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176901\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176902\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:68069\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"a 14alpha-formyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a Delta(14) steroid + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:68068\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:138031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:176902\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:25287\"}}],\"reaction\":{\"ecNumber\":\"1.14.14.154\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"name\":\"lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:25286\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16521\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17813\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75104\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"lanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-hydroxylanosterol + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75103\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16521\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166806\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75108\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-hydroxylanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-oxolanosterol + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75107\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166681\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166806\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/7",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75112\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-oxolanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75111\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17813\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:166681\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/8",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75440\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"name\":\"eburicol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = 14-demethyleburicol + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75439\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194330\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/9",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75428\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"eburicol + reduced [NADPH--hemoprotein reductase] + O2 = 32-hydroxyeburicol + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75427\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194328\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/10",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75432\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-hydroxyeburicol + reduced [NADPH--hemoprotein reductase] + O2 = 32-oxoeburicol + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75431\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194328\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194329\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/11",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:75436\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10614\",\"source\":\"UniProtKB\"}],\"name\":\"32-oxoeburicol + reduced [NADPH--hemoprotein reductase] + O2 = 14-demethyleburicol + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75435\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15740\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194329\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194330\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/12",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Lu Y.\",\"Li Y.\",\"Dou M.\",\"Liu D.\",\"Lin W.\",\"Fan A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39105744\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c04244\"}],\"citationType\":\"journal article\",\"firstPage\":\"18520\",\"id\":\"39105744\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"18527\",\"publicationDate\":\"2024\",\"title\":\"Discovery of a hybrid molecule with phytotoxic activity by genome mining, heterologous expression, and OSMAC strategy.\",\"volume\":\"72\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   RESB_ASPSL              Reviewed;         511 AA.\nAC   P0DXU9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Sterol 14-alpha demethylase resB {ECO:0000303|PubMed:39105744};\nDE            EC=1.14.14.154 {ECO:0000250|UniProtKB:A0A0L1JEW4};\nDE   AltName: Full=Cytochrome P450 monooxygenase resB {ECO:0000303|PubMed:39105744};\nDE   AltName: Full=Ergosterol biosynthesis protein resB {ECO:0000303|PubMed:39105744};\nDE   AltName: Full=Restricticin biosynthesis cluster protein B {ECO:0000303|PubMed:39105744};\nGN   Name=resB {ECO:0000303|PubMed:39105744};\nOS   Aspergillus sclerotiorum.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=138282;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Sterol 14-alpha demethylase resB {ECO:0000303|PubMed:39105744};\nDE            EC=1.14.14.154 {ECO:0000250|UniProtKB:A0A0L1JEW4};\nDE   AltName: Full=Cytochrome P450 monooxygenase resB {ECO:0000303|PubMed:39105744};\nDE   AltName: Full=Ergosterol biosynthesis protein resB {ECO:0000303|PubMed:39105744};\nDE   AltName: Full=Restricticin biosynthesis cluster protein B {ECO:0000303|PubMed:39105744};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRX   PubMed=39105744; DOI=10.1021/acs.jafc.4c04244;\nRA   Lu Y., Li Y., Dou M., Liu D., Lin W., Fan A.;\nRT   \"Discovery of a hybrid molecule with phytotoxic activity by genome mining,\nRT   heterologous expression, and OSMAC strategy.\";\nRL   J. Agric. Food Chem. 72:18520-18527(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein\nCC         reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized\nCC         [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);\nCC         Xref=Rhea:RHEA:54028, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,\nCC         ChEBI:CHEBI:138029, ChEBI:CHEBI:138031; EC=1.14.14.154;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:54029;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-methyl steroid + reduced [NADPH--hemoprotein\nCC         reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--\nCC         hemoprotein reductase] + H2O + H(+); Xref=Rhea:RHEA:68060, Rhea:RHEA-\nCC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:138029, ChEBI:CHEBI:176901;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:68061;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein\nCC         reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--\nCC         hemoprotein reductase] + 2 H2O + H(+); Xref=Rhea:RHEA:68064,\nCC         Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:176901, ChEBI:CHEBI:176902;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:68065;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 14alpha-formyl steroid + reduced [NADPH--hemoprotein\nCC         reductase] + O2 = a Delta(14) steroid + formate + oxidized [NADPH--\nCC         hemoprotein reductase] + H2O + 2 H(+); Xref=Rhea:RHEA:68068,\nCC         Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:138031,\nCC         ChEBI:CHEBI:176902; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:68069;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=lanosterol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 =\nCC         4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + 3\nCC         oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);\nCC         Xref=Rhea:RHEA:25286, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:16521, ChEBI:CHEBI:17813,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210; EC=1.14.14.154;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:25287;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=lanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-\nCC         hydroxylanosterol + oxidized [NADPH--hemoprotein reductase] + H2O +\nCC         H(+); Xref=Rhea:RHEA:75103, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:16521, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,\nCC         ChEBI:CHEBI:166806; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75104;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-hydroxylanosterol + reduced [NADPH--hemoprotein reductase]\nCC         + O2 = 32-oxolanosterol + oxidized [NADPH--hemoprotein reductase] + 2\nCC         H2O + H(+); Xref=Rhea:RHEA:75107, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:166681,\nCC         ChEBI:CHEBI:166806; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75108;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H11",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-oxolanosterol + reduced [NADPH--hemoprotein reductase] + O2\nCC         = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate +\nCC         oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+);\nCC         Xref=Rhea:RHEA:75111, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:15740, ChEBI:CHEBI:17813, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:166681;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75112;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H12",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=eburicol + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 =\nCC         14-demethyleburicol + formate + 3 oxidized [NADPH--hemoprotein\nCC         reductase] + 4 H2O + 4 H(+); Xref=Rhea:RHEA:75439, Rhea:RHEA-\nCC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:70315,\nCC         ChEBI:CHEBI:194330; Evidence={ECO:0000250|UniProtKB:Q4WNT5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75440;\nCC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H13",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=eburicol + reduced [NADPH--hemoprotein reductase] + O2 = 32-\nCC         hydroxyeburicol + oxidized [NADPH--hemoprotein reductase] + H2O +\nCC         H(+); Xref=Rhea:RHEA:75427, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:70315,\nCC         ChEBI:CHEBI:194328; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75428;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H14",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-hydroxyeburicol + reduced [NADPH--hemoprotein reductase] +\nCC         O2 = 32-oxoeburicol + oxidized [NADPH--hemoprotein reductase] + 2 H2O\nCC         + H(+); Xref=Rhea:RHEA:75431, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:194328,\nCC         ChEBI:CHEBI:194329; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75432;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H15",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=32-oxoeburicol + reduced [NADPH--hemoprotein reductase] + O2 =\nCC         14-demethyleburicol + formate + oxidized [NADPH--hemoprotein\nCC         reductase] + H2O + 2 H(+); Xref=Rhea:RHEA:75435, Rhea:RHEA-\nCC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:15740,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:194329,\nCC         ChEBI:CHEBI:194330; Evidence={ECO:0000250|UniProtKB:P10614};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:75436;\nCC         Evidence={ECO:0000250|UniProtKB:P10614};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-154",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
