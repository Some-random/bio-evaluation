# EC_number_0082

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0082.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.3.1.312

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQIKPPYLLFIGDATDKLSIKMAQSLADWRAELCVGELSVNGCTVSTGLNQCSICEAAKLGAKTFVLGFANSGGVLDKKWLPIISEAIENGMNIVSGLHDKLTNFDELVSLSQKHNTNLLDIRHPSTAFATGKGYKRKGKRLLTVGTDCSVGKMYTSLSLEKAMKEQNIDVDFRATGQCGILISGSGVAIDCVIADFISGAAESLSPDAEETHWDIIEGQGSLSHPAFAGVSLGLLHGSQPDALVICHALNRTHMRGLLHTSFPSIETTIELNIAAAKLTNPDVQVVGISVNTSSVSIEQGNEICERLSQTFGVPCVDPLRDGVDSIVANLC

[Multiple Choices]
A. 2.3.1.193
B. 2.3.1.312
C. 2.1.1.393
D. 5.2.1.8
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

> The sequence-matched UniProt annotation assigns EC 2.3.1.312 and cites experimental evidence. The catalytic-activity record specifies acetylation of D-glutamate, which supports choice B. The cited study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Evidence that this protein specifically acetylates D-glutamate, or a sufficiently close characterized homolog establishing that substrate specificity, is not supplied in the original input.


**Reason**

> The sequence may suggest an enzyme, but no clear feature in the input distinguishes the D-glutamate acetyltransferase choice B from the other acetyltransferase choice A. Their distinction depends on substrate specificity, which is not reliably inferred from the broad enzyme class alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied experimental annotation supports B; lack of a clear sequence-only discriminator does not make another option an equally defensible actual EC assignment.


### Important caveats

- The supporting source is a sequence-matched database record citing experimental evidence; the cited paper was not independently checked.
- The reviewer-only source identity and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Evidence that this protein specifically acetylates D-glutamate, or a sufficiently close characterized homolog establishing that substrate specificity, is not supplied in the original input.",
    "reason": "The sequence may suggest an enzyme, but no clear feature in the input distinguishes the D-glutamate acetyltransferase choice B from the other acetyltransferase choice A. Their distinction depends on substrate specificity, which is not reliably inferred from the broad enzyme class alone."
  },
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.312 and cites experimental evidence. The catalytic-activity record specifies acetylation of D-glutamate, which supports choice B. The cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The supporting source is a sequence-matched database record citing experimental evidence; the cited paper was not independently checked.",
    "The reviewer-only source identity and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental annotation supports B; lack of a clear sequence-only discriminator does not make another option an equally defensible actual EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.312 and cites experimental evidence. The catalytic-activity record specifies acetylation of D-glutamate, which supports choice B. The cited study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Evidence that this protein specifically acetylates D-glutamate, or a sufficiently close characterized homolog establishing that substrate specificity, is not supplied in the original input.",
    "reason": "The sequence may suggest an enzyme, but no clear feature in the input distinguishes the D-glutamate acetyltransferase choice B from the other acetyltransferase choice A. Their distinction depends on substrate specificity, which is not reliably inferred from the broad enzyme class alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental annotation supports B; lack of a clear sequence-only discriminator does not make another option an equally defensible actual EC assignment."
  },
  "important_caveats": [
    "The supporting source is a sequence-matched database record citing experimental evidence; the cited paper was not independently checked.",
    "The reviewer-only source identity and annotations were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXZ1 annotates this 332-aa protein as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally validated. The benchmark sequence matches the source sequence exactly (SHA-256 confirmed). The historical Swiss-Prot record (entry version 3) also carries EC 2.3.1.312.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Transferable knowledge can narrow the EC class: the sequence contains a GNAT (GCN5-related N-acetyltransferase) fold motif ('GFANSGG' near the N-terminus, acetyl-CoA-binding region features), which is characteristic of acyltransferases (EC 2.3.x), not methyltransferases (EC 2.1.x) or isomerases (EC 5.2.x). This reliably eliminates C (2.1.1.393, methyltransferase) and D (5.2.1.8, cis-trans isomerase). However, both remaining options A (2.3.1.193) and B (2.3.1.312) fall within EC 2.3.1.x (acyltransferases transferring groups other than amino-acyl groups). Distinguishing between these two specific four-digit EC numbers requires knowing the exact substrate specificity of the enzyme (e.g., D-glutamate vs. whatever substrate 2.3.1.193 acts on). While GNAT subfamily classification can indicate the general substrate class, the precise assignment to EC 2.3.1.312 versus 2.3.1.193 depends on experimentally determined substrate specificity and active-site residue configurations that are not reliably extractable from the raw sequence alone without already knowing this protein's annotation.


**Missing item-specific fact**

> The experimentally determined substrate specificity of this particular GNAT-fold protein (i.e., that it specifically acetylates D-glutamate, D-aspartate, and D-glutamine rather than the substrate of EC 2.3.1.193), which is established only through the in vitro enzymatic assays reported in PubMed:36690779.


**Reason**

> The GNAT fold and acyltransferase motifs allow elimination of the methyltransferase (C) and isomerase (D) options through family-level inference. However, the final distinction between 2.3.1.193 and 2.3.1.312 requires knowledge of the exact substrate specificity, which is an experimental measurement specific to this protein and not derivable from sequence homology or general GNAT-family knowledge alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (2.3.1.x acyltransferase, 2.1.1.x methyltransferase, 5.2.1.x isomerase), so there is no ambiguity in the question format. The difficulty lies in distinguishing the two 2.3.1.x options, not in ambiguous wording.


### Important caveats

- The UniProt entry was first published on 2025-04-09 and the Swiss-Prot review (entry version 3) was released in 2026_01. The author's source snapshot is unknown; if the question was constructed before the Swiss-Prot annotation, the EC number may have been derived from the primary publication directly.
- EC 2.3.1.193 is a valid but obscure EC number; its exact substrate identity was not independently verified in this review. The argument for lookup dependence assumes that 2.3.1.193 and 2.3.1.312 cannot be distinguished by GNAT subfamily features alone, which may be refined with more detailed active-site analysis.
- The reviewer-only evidence confirms sequence match and experimental evidence code (ECO:0000269), but the evaluated model had access only to the raw sequence and the four EC number choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Transferable knowledge can narrow the EC class: the sequence contains a GNAT (GCN5-related N-acetyltransferase) fold motif ('GFANSGG' near the N-terminus, acetyl-CoA-binding region features), which is characteristic of acyltransferases (EC 2.3.x), not methyltransferases (EC 2.1.x) or isomerases (EC 5.2.x). This reliably eliminates C (2.1.1.393, methyltransferase) and D (5.2.1.8, cis-trans isomerase). However, both remaining options A (2.3.1.193) and B (2.3.1.312) fall within EC 2.3.1.x (acyltransferases transferring groups other than amino-acyl groups). Distinguishing between these two specific four-digit EC numbers requires knowing the exact substrate specificity of the enzyme (e.g., D-glutamate vs. whatever substrate 2.3.1.193 acts on). While GNAT subfamily classification can indicate the general substrate class, the precise assignment to EC 2.3.1.312 versus 2.3.1.193 depends on experimentally determined substrate specificity and active-site residue configurations that are not reliably extractable from the raw sequence alone without already knowing this protein's annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined substrate specificity of this particular GNAT-fold protein (i.e., that it specifically acetylates D-glutamate, D-aspartate, and D-glutamine rather than the substrate of EC 2.3.1.193), which is established only through the in vitro enzymatic assays reported in PubMed:36690779.",
    "reason": "The GNAT fold and acyltransferase motifs allow elimination of the methyltransferase (C) and isomerase (D) options through family-level inference. However, the final distinction between 2.3.1.193 and 2.3.1.312 requires knowledge of the exact substrate specificity, which is an experimental measurement specific to this protein and not derivable from sequence homology or general GNAT-family knowledge alone."
  },
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 annotates this 332-aa protein as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally validated. The benchmark sequence matches the source sequence exactly (SHA-256 confirmed). The historical Swiss-Prot record (entry version 3) also carries EC 2.3.1.312."
  },
  "important_caveats": [
    "The UniProt entry was first published on 2025-04-09 and the Swiss-Prot review (entry version 3) was released in 2026_01. The author's source snapshot is unknown; if the question was constructed before the Swiss-Prot annotation, the EC number may have been derived from the primary publication directly.",
    "EC 2.3.1.193 is a valid but obscure EC number; its exact substrate identity was not independently verified in this review. The argument for lookup dependence assumes that 2.3.1.193 and 2.3.1.312 cannot be distinguished by GNAT subfamily features alone, which may be refined with more detailed active-site analysis.",
    "The reviewer-only evidence confirms sequence match and experimental evidence code (ECO:0000269), but the evaluated model had access only to the raw sequence and the four EC number choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (2.3.1.x acyltransferase, 2.1.1.x methyltransferase, 5.2.1.x isomerase), so there is no ambiguity in the question format. The difficulty lies in distinguishing the two 2.3.1.x options, not in ambiguous wording."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 annotates this 332-aa protein as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269, PubMed:36690779, ISME J. 2023). The catalytic reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally validated. The benchmark sequence matches the source sequence exactly (SHA-256 confirmed). The historical Swiss-Prot record (entry version 3) also carries EC 2.3.1.312.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Transferable knowledge can narrow the EC class: the sequence contains a GNAT (GCN5-related N-acetyltransferase) fold motif ('GFANSGG' near the N-terminus, acetyl-CoA-binding region features), which is characteristic of acyltransferases (EC 2.3.x), not methyltransferases (EC 2.1.x) or isomerases (EC 5.2.x). This reliably eliminates C (2.1.1.393, methyltransferase) and D (5.2.1.8, cis-trans isomerase). However, both remaining options A (2.3.1.193) and B (2.3.1.312) fall within EC 2.3.1.x (acyltransferases transferring groups other than amino-acyl groups). Distinguishing between these two specific four-digit EC numbers requires knowing the exact substrate specificity of the enzyme (e.g., D-glutamate vs. whatever substrate 2.3.1.193 acts on). While GNAT subfamily classification can indicate the general substrate class, the precise assignment to EC 2.3.1.312 versus 2.3.1.193 depends on experimentally determined substrate specificity and active-site residue configurations that are not reliably extractable from the raw sequence alone without already knowing this protein's annotation.",
    "missing_item_specific_fact": "The experimentally determined substrate specificity of this particular GNAT-fold protein (i.e., that it specifically acetylates D-glutamate, D-aspartate, and D-glutamine rather than the substrate of EC 2.3.1.193), which is established only through the in vitro enzymatic assays reported in PubMed:36690779.",
    "reason": "The GNAT fold and acyltransferase motifs allow elimination of the methyltransferase (C) and isomerase (D) options through family-level inference. However, the final distinction between 2.3.1.193 and 2.3.1.312 requires knowledge of the exact substrate specificity, which is an experimental measurement specific to this protein and not derivable from sequence homology or general GNAT-family knowledge alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (2.3.1.x acyltransferase, 2.1.1.x methyltransferase, 5.2.1.x isomerase), so there is no ambiguity in the question format. The difficulty lies in distinguishing the two 2.3.1.x options, not in ambiguous wording."
  },
  "important_caveats": [
    "The UniProt entry was first published on 2025-04-09 and the Swiss-Prot review (entry version 3) was released in 2026_01. The author's source snapshot is unknown; if the question was constructed before the Swiss-Prot annotation, the EC number may have been derived from the primary publication directly.",
    "EC 2.3.1.193 is a valid but obscure EC number; its exact substrate identity was not independently verified in this review. The argument for lookup dependence assumes that 2.3.1.193 and 2.3.1.312 cannot be distinguished by GNAT subfamily features alone, which may be refined with more detailed active-site analysis.",
    "The reviewer-only evidence confirms sequence match and experimental evidence code (ECO:0000269), but the evaluated model had access only to the raw sequence and the four EC number choices."
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
  "benchmark_sequence_length": 332,
  "benchmark_sequence_sha256": "d233fd888471e43669f332aeb0b2fac44fb59ce5fab9d43f3919864cdb20c35d",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 332,
  "current_source_sequence_sha256": "d233fd888471e43669f332aeb0b2fac44fb59ce5fab9d43f3919864cdb20c35d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXZ1",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "selected_historical_source_sequence_length": 332,
  "selected_historical_source_sequence_sha256": "d233fd888471e43669f332aeb0b2fac44fb59ce5fab9d43f3919864cdb20c35d",
  "selected_historical_version": {
    "accession": "P0DXZ1",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DGCN_PSEAS",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXZ1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Alteromonadales\",\"Pseudoalteromonadaceae\",\"Pseudoalteromonas\"],\"scientificName\":\"Pseudoalteromonas sp\",\"taxonId\":53249}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.312\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"D-glutamate N-acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:76496\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76495\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29986\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:195260\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76551\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29990\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:195274\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76547\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58000\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:143880\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Yu Y.\",\"Wang P.\",\"Cao H.Y.\",\"Teng Z.J.\",\"Zhu Y.\",\"Wang M.\",\"McMinn A.\",\"Chen Y.\",\"Xiang H.\",\"Zhang Y.Z.\",\"Chen X.L.\",\"Zhang Y.Q.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36690779\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41396-023-01364-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"36690779\",\"journal\":\"ISME J.\",\"lastPage\":\"548\",\"publicationDate\":\"2023\",\"title\":\"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.\",\"volume\":\"17\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CF6-2\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   DGCN_PSEAS              Reviewed;         332 AA.\nAC   P0DXZ1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\nGN   Name=dgcN {ECO:0000303|PubMed:36690779};\nOS   Pseudoalteromonas sp.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Alteromonadales; Pseudoalteromonadaceae; Pseudoalteromonas.\nOX   NCBI_TaxID=53249;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, INDUCTION,\nRP   AND DISRUPTION PHENOTYPE.\nRC   STRAIN=CF6-2;\nRX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;\nRA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,\nRA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;\nRT   \"Novel D-glutamate catabolic pathway in marine Proteobacteria and\nRT   halophilic archaea.\";\nRL   ISME J. 17:537-548(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 13-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+);\nCC         Xref=Rhea:RHEA:76495, ChEBI:CHEBI:15378, ChEBI:CHEBI:29986,\nCC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195260;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76496;\nCC         Evidence={ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+);\nCC         Xref=Rhea:RHEA:76551, ChEBI:CHEBI:15378, ChEBI:CHEBI:29990,\nCC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195274;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+);\nCC         Xref=Rhea:RHEA:76547, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:58000, ChEBI:CHEBI:143880;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
