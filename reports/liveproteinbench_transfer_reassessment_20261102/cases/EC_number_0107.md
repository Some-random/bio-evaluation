# EC_number_0107

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0107.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.3.1.319

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATKRKVIITCAPTGAIHTPSMSPYLPVTPQQIGDAALAAAKEGAAIIHLHARDPDDGHPTQDPAVFQEFLPRIKAECDAVINLTTGGSPHMTVAERLKPAHHFQPEVASLNMGSMNFGLYPMLERFKELKYDWERKHLENSRDLVFKNTFADIEYILTSCGANGTRFEFECYDISHLYNLAHFVDRGLAKPPFFVQSVFGLLGGIGAHPEDLAHMRRTADRLFGKDYVWSILGAGRNQIPLASIGVAQGSNARVGLEDSLWIEPGKLAESSAAQVRKIRQVIEGLSLDIATPAEAREMLQLKGAANTNF

[Multiple Choices]
A. 2.3.1.322
B. 2.3.1.319
C. 3.6.1.5
D. 6.3.5.1
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

> The sequence-matched UniProt annotation assigns EC 2.3.1.319 and gives the corresponding catalytic reaction, with experimental evidence cited to a publication. This supports choice B, though the cited primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad acyltransferase-class inference, favoring choices A or B over the different EC classes in C and D. But that does not distinguish A from B, which share EC 2.3.1 and differ in their specific enzyme assignments.


**Missing item-specific fact**

> Whether this protein has the substrate and product specificity assigned to EC 2.3.1.319 rather than the specificity represented by EC 2.3.1.322; the input provides no clear transferable feature that resolves that distinction.


**Reason**

> General class-level sequence or mechanism clues do not establish the precise catalytic activity needed to choose between the two closely related acyltransferase options. Distinguishing them would require a validated family-to-function mapping or reaction-specific evidence for this protein, neither of which is supplied in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched source evidence supports B as the assigned EC number. The difficulty of deriving that assignment from the sequence alone does not make another option equally correct.


### Important caveats

- The sequence-match and experimental-evidence attribution come from reviewer-only source material, not from the original model input.
- The source cites experimental evidence for the reaction, but the primary publication was not independently checked.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad acyltransferase-class inference, favoring choices A or B over the different EC classes in C and D. But that does not distinguish A from B, which share EC 2.3.1 and differ in their specific enzyme assignments.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this protein has the substrate and product specificity assigned to EC 2.3.1.319 rather than the specificity represented by EC 2.3.1.322; the input provides no clear transferable feature that resolves that distinction.",
    "reason": "General class-level sequence or mechanism clues do not establish the precise catalytic activity needed to choose between the two closely related acyltransferase options. Distinguishing them would require a validated family-to-function mapping or reaction-specific evidence for this protein, neither of which is supplied in the original input."
  },
  "case_id": "EC_number_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.319 and gives the corresponding catalytic reaction, with experimental evidence cited to a publication. This supports choice B, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence-match and experimental-evidence attribution come from reviewer-only source material, not from the original model input.",
    "The source cites experimental evidence for the reaction, but the primary publication was not independently checked."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched source evidence supports B as the assigned EC number. The difficulty of deriving that assignment from the sequence alone does not make another option equally correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.319 and gives the corresponding catalytic reaction, with experimental evidence cited to a publication. This supports choice B, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad acyltransferase-class inference, favoring choices A or B over the different EC classes in C and D. But that does not distinguish A from B, which share EC 2.3.1 and differ in their specific enzyme assignments.",
    "missing_item_specific_fact": "Whether this protein has the substrate and product specificity assigned to EC 2.3.1.319 rather than the specificity represented by EC 2.3.1.322; the input provides no clear transferable feature that resolves that distinction.",
    "reason": "General class-level sequence or mechanism clues do not establish the precise catalytic activity needed to choose between the two closely related acyltransferase options. Distinguishing them would require a validated family-to-function mapping or reaction-specific evidence for this protein, neither of which is supplied in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched source evidence supports B as the assigned EC number. The difficulty of deriving that assignment from the sequence alone does not make another option equally correct."
  },
  "important_caveats": [
    "The sequence-match and experimental-evidence attribution come from reviewer-only source material, not from the original model input.",
    "The source cites experimental evidence for the reaction, but the primary publication was not independently checked."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The expected answer B (EC 2.3.1.319, 3,5-dioxohexanoate:acetyl-CoA acetone transferase) is supported by experimental evidence (ECO:0000269) from Bastard et al. 2014 (PubMed:24240508, Nat. Chem. Biol. 10:42-49). The UniProt entry B1G5Y9 (DOHCE_PARG4) records the catalytic reaction: 3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate, with the sequence matching the benchmark input (310 AA, SHA256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable CoA-transferase motifs (e.g., 'CAPTGAIH', 'GGIGAHPED', 'GAGRNQIPLASIG') that would allow a knowledgeable model to assign the protein to EC class 2.3.1 (acyltransferases transferring groups other than aminoacyl), thereby eliminating C (3.6.1.5, a hydrolase on acid anhydrides) and D (6.3.5.1, a ligase). However, distinguishing EC 2.3.1.319 (3,5-dioxohexanoate + acetyl-CoA → acetoacetyl-CoA + acetoacetate) from EC 2.3.1.322 requires knowing the specific substrate identity of this enzyme. The Bastard et al. 2014 paper that characterized this enzyme explicitly demonstrated 'hidden functional diversity' within this CoA-transferase family—closely related sequences catalyze different substrate-specific reactions. No generalizable sequence motif within this family reliably predicts the exact 4-digit EC number. The distinction between .319 and .322 is a specific experimental measurement of substrate specificity not recoverable from sequence features shared across the family.


**Missing item-specific fact**

> The specific substrate specificity of this exact protein (whether it transfers CoA to 3,5-dioxohexanoate &#91;2.3.1.319&#93; or to the substrate of EC 2.3.1.322) cannot be predicted from the sequence alone within this enzyme family, as the family exhibits hidden functional diversity. The experimental characterization (PubMed:24240508) of the specific reaction catalyzed by this protein is the necessary distinguishing fact.


**Reason**

> While family-level assignment to EC 2.3.1 is reasoning-supported via conserved CoA-transferase motifs, the fine-grained distinction between EC 2.3.1.319 and EC 2.3.1.322 requires knowledge of the specific substrate specificity determined experimentally for this protein or its immediate characterized homologs. The very paper that assigned this EC number demonstrated that sequence similarity within this family does not predict substrate specificity, making the 4th-digit distinction effectively lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (2.3.1.322) and B (2.3.1.319) are CoA-transferases (EC 2.3.1.xxxx) within the same enzyme superfamily. From sequence alone, a model can confidently assign EC class 2.3.1 but cannot reliably distinguish the specific 4-digit number between these two closely related entries without knowing the experimentally determined substrate specificity. C and D are clearly eliminable as they belong to different EC top-level classes (hydrolase and ligase respectively).


### Important caveats

- The EC 2.3.1.319 assignment is based on experimental evidence (ECO:0000269), not computational prediction.
- The Bastard et al. 2014 paper specifically demonstrated that this enzyme family harbors hidden functional diversity, meaning sequence-based prediction of the exact 4-digit EC number is inherently unreliable within this family.
- The reviewer-only evidence confirms sequence match (SHA256 identical, 310 AA) between the benchmark input and UniProt B1G5Y9.
- The distinction between EC 2.3.1.319 and 2.3.1.322 is at the level of specific substrate identity, not enzyme class or mechanism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable CoA-transferase motifs (e.g., 'CAPTGAIH', 'GGIGAHPED', 'GAGRNQIPLASIG') that would allow a knowledgeable model to assign the protein to EC class 2.3.1 (acyltransferases transferring groups other than aminoacyl), thereby eliminating C (3.6.1.5, a hydrolase on acid anhydrides) and D (6.3.5.1, a ligase). However, distinguishing EC 2.3.1.319 (3,5-dioxohexanoate + acetyl-CoA → acetoacetyl-CoA + acetoacetate) from EC 2.3.1.322 requires knowing the specific substrate identity of this enzyme. The Bastard et al. 2014 paper that characterized this enzyme explicitly demonstrated 'hidden functional diversity' within this CoA-transferase family—closely related sequences catalyze different substrate-specific reactions. No generalizable sequence motif within this family reliably predicts the exact 4-digit EC number. The distinction between .319 and .322 is a specific experimental measurement of substrate specificity not recoverable from sequence features shared across the family.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this exact protein (whether it transfers CoA to 3,5-dioxohexanoate [2.3.1.319] or to the substrate of EC 2.3.1.322) cannot be predicted from the sequence alone within this enzyme family, as the family exhibits hidden functional diversity. The experimental characterization (PubMed:24240508) of the specific reaction catalyzed by this protein is the necessary distinguishing fact.",
    "reason": "While family-level assignment to EC 2.3.1 is reasoning-supported via conserved CoA-transferase motifs, the fine-grained distinction between EC 2.3.1.319 and EC 2.3.1.322 requires knowledge of the specific substrate specificity determined experimentally for this protein or its immediate characterized homologs. The very paper that assigned this EC number demonstrated that sequence similarity within this family does not predict substrate specificity, making the 4th-digit distinction effectively lookup-dependent."
  },
  "case_id": "EC_number_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The expected answer B (EC 2.3.1.319, 3,5-dioxohexanoate:acetyl-CoA acetone transferase) is supported by experimental evidence (ECO:0000269) from Bastard et al. 2014 (PubMed:24240508, Nat. Chem. Biol. 10:42-49). The UniProt entry B1G5Y9 (DOHCE_PARG4) records the catalytic reaction: 3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate, with the sequence matching the benchmark input (310 AA, SHA256 identical)."
  },
  "important_caveats": [
    "The EC 2.3.1.319 assignment is based on experimental evidence (ECO:0000269), not computational prediction.",
    "The Bastard et al. 2014 paper specifically demonstrated that this enzyme family harbors hidden functional diversity, meaning sequence-based prediction of the exact 4-digit EC number is inherently unreliable within this family.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical, 310 AA) between the benchmark input and UniProt B1G5Y9.",
    "The distinction between EC 2.3.1.319 and 2.3.1.322 is at the level of specific substrate identity, not enzyme class or mechanism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (2.3.1.322) and B (2.3.1.319) are CoA-transferases (EC 2.3.1.xxxx) within the same enzyme superfamily. From sequence alone, a model can confidently assign EC class 2.3.1 but cannot reliably distinguish the specific 4-digit number between these two closely related entries without knowing the experimentally determined substrate specificity. C and D are clearly eliminable as they belong to different EC top-level classes (hydrolase and ligase respectively)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The expected answer B (EC 2.3.1.319, 3,5-dioxohexanoate:acetyl-CoA acetone transferase) is supported by experimental evidence (ECO:0000269) from Bastard et al. 2014 (PubMed:24240508, Nat. Chem. Biol. 10:42-49). The UniProt entry B1G5Y9 (DOHCE_PARG4) records the catalytic reaction: 3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate, with the sequence matching the benchmark input (310 AA, SHA256 identical).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable CoA-transferase motifs (e.g., 'CAPTGAIH', 'GGIGAHPED', 'GAGRNQIPLASIG') that would allow a knowledgeable model to assign the protein to EC class 2.3.1 (acyltransferases transferring groups other than aminoacyl), thereby eliminating C (3.6.1.5, a hydrolase on acid anhydrides) and D (6.3.5.1, a ligase). However, distinguishing EC 2.3.1.319 (3,5-dioxohexanoate + acetyl-CoA → acetoacetyl-CoA + acetoacetate) from EC 2.3.1.322 requires knowing the specific substrate identity of this enzyme. The Bastard et al. 2014 paper that characterized this enzyme explicitly demonstrated 'hidden functional diversity' within this CoA-transferase family—closely related sequences catalyze different substrate-specific reactions. No generalizable sequence motif within this family reliably predicts the exact 4-digit EC number. The distinction between .319 and .322 is a specific experimental measurement of substrate specificity not recoverable from sequence features shared across the family.",
    "missing_item_specific_fact": "The specific substrate specificity of this exact protein (whether it transfers CoA to 3,5-dioxohexanoate [2.3.1.319] or to the substrate of EC 2.3.1.322) cannot be predicted from the sequence alone within this enzyme family, as the family exhibits hidden functional diversity. The experimental characterization (PubMed:24240508) of the specific reaction catalyzed by this protein is the necessary distinguishing fact.",
    "reason": "While family-level assignment to EC 2.3.1 is reasoning-supported via conserved CoA-transferase motifs, the fine-grained distinction between EC 2.3.1.319 and EC 2.3.1.322 requires knowledge of the specific substrate specificity determined experimentally for this protein or its immediate characterized homologs. The very paper that assigned this EC number demonstrated that sequence similarity within this family does not predict substrate specificity, making the 4th-digit distinction effectively lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (2.3.1.322) and B (2.3.1.319) are CoA-transferases (EC 2.3.1.xxxx) within the same enzyme superfamily. From sequence alone, a model can confidently assign EC class 2.3.1 but cannot reliably distinguish the specific 4-digit number between these two closely related entries without knowing the experimentally determined substrate specificity. C and D are clearly eliminable as they belong to different EC top-level classes (hydrolase and ligase respectively)."
  },
  "important_caveats": [
    "The EC 2.3.1.319 assignment is based on experimental evidence (ECO:0000269), not computational prediction.",
    "The Bastard et al. 2014 paper specifically demonstrated that this enzyme family harbors hidden functional diversity, meaning sequence-based prediction of the exact 4-digit EC number is inherently unreliable within this family.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical, 310 AA) between the benchmark input and UniProt B1G5Y9.",
    "The distinction between EC 2.3.1.319 and 2.3.1.322 is at the level of specific substrate identity, not enzyme class or mechanism."
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
  "benchmark_sequence_length": 310,
  "benchmark_sequence_sha256": "669119f3660e25802e4d9d5d3abdcf25e9feb3666a00e1d4a9a294493841e494",
  "current_entry_audit": {
    "entryVersion": 44,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-04-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 310,
  "current_source_sequence_sha256": "669119f3660e25802e4d9d5d3abdcf25e9feb3666a00e1d4a9a294493841e494",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 43,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B1G5Y9",
  "selected_historical_entry_version": 43,
  "selected_historical_record_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "selected_historical_source_sequence_length": 310,
  "selected_historical_source_sequence_sha256": "669119f3660e25802e4d9d5d3abdcf25e9feb3666a00e1d4a9a294493841e494",
  "selected_historical_version": {
    "accession": "B1G5Y9",
    "database": "Swiss-Prot",
    "entryVersion": 43,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "DOHCE_PARG4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B1G5Y9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":44,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-04-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Burkholderiaceae\",\"Paraburkholderia\"],\"scientificName\":\"Paraburkholderia graminis (strain ATCC 700544 / DSM 17151 / LMG 18924 / NCIMB 13744 / C4D1M)\",\"taxonId\":396598}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3,5-dioxohexanoate cleavage enzyme\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"BKACE_274\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.319\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3,5-dioxohexanoate:acetyl-CoA acetone transferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.319\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"name\":\"3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79655\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57286\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57814\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bastard K.\",\"Smith A.A.\",\"Vergne-Vaxelaire C.\",\"Perret A.\",\"Zaparucha A.\",\"De Melo-Minardi R.\",\"Mariage A.\",\"Boutard M.\",\"Debard A.\",\"Lechaplais C.\",\"Pelle C.\",\"Pellouin V.\",\"Perchat N.\",\"Petit J.L.\",\"Kreimeyer A.\",\"Medigue C.\",\"Weissenbach J.\",\"Artiguenave F.\",\"De Berardinis V.\",\"Vallenet D.\",\"Salanoubat M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24240508\"},{\"database\":\"DOI\",\"id\":\"10.1038/nchembio.1387\"}],\"citationType\":\"journal article\",\"firstPage\":\"42\",\"id\":\"24240508\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"49\",\"publicationDate\":\"2014\",\"title\":\"Revealing the hidden functional diversity of an enzyme family.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:00.301562+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb",
  "url": "https://rest.uniprot.org/uniprotkb/B1G5Y9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H1",
  "excerpt": "ID   DOHCE_PARG4             Reviewed;         310 AA.\nAC   B1G5Y9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-APR-2008, sequence version 1.\nDT   28-JAN-2026, entry version 43.\nDE   RecName: Full=3,5-dioxohexanoate:acetyl-CoA acetone transferase {ECO:0000305};\nDE            EC=2.3.1.319 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3,5-dioxohexanoate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_274 {ECO:0000303|PubMed:24240508};\nGN   Name=kce_3 {ECO:0000312|EMBL:CAB3715113.1};\nGN   ORFNames=BgramDRAFT_4880 {ECO:0000312|EMBL:EDT08458.1},\nGN   R8871_04389 {ECO:0000312|EMBL:CAB3715113.1};\nOS   Paraburkholderia graminis (strain ATCC 700544 / DSM 17151 / LMG 18924 /\nOS   NCIMB 13744 / C4D1M).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Burkholderiaceae; Paraburkholderia.\nOX   NCBI_TaxID=396598;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.999580+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "url": "https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=3,5-dioxohexanoate:acetyl-CoA acetone transferase {ECO:0000305};\nDE            EC=2.3.1.319 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3,5-dioxohexanoate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_274 {ECO:0000303|PubMed:24240508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.999580+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "url": "https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=24240508; DOI=10.1038/nchembio.1387;\nRA   Bastard K., Smith A.A., Vergne-Vaxelaire C., Perret A., Zaparucha A.,\nRA   De Melo-Minardi R., Mariage A., Boutard M., Debard A., Lechaplais C.,\nRA   Pelle C., Pellouin V., Perchat N., Petit J.L., Kreimeyer A., Medigue C.,\nRA   Weissenbach J., Artiguenave F., De Berardinis V., Vallenet D.,\nRA   Salanoubat M.;\nRT   \"Revealing the hidden functional diversity of an enzyme family.\";\nRL   Nat. Chem. Biol. 10:42-49(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.999580+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "url": "https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)

```json
{
  "entry_version": 43,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA +\nCC         acetoacetate; Xref=Rhea:RHEA:79655, ChEBI:CHEBI:13705,\nCC         ChEBI:CHEBI:57286, ChEBI:CHEBI:57288, ChEBI:CHEBI:57814;\nCC         EC=2.3.1.319; Evidence={ECO:0000269|PubMed:24240508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:50.999580+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94",
  "url": "https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
