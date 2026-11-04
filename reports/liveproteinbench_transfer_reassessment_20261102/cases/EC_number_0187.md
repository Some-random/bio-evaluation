# EC_number_0187

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0187.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 5.1.1.24

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDRKVQVLDFIKINPAGNITILIDNFDIYDKNIPKLSEEIMKETNLYAEQVGFIKDSHLQMMGGEFCGNASRAFASLLAFRDKDFSKQKNYNITCSGESKVLDVDVRNDGAKNKFLAKIKMPKFLSLEEINVDEYKLGLVRFSGINHFIFNIKENKETSFENIIDLVKKYLSNEEYSAFGIMFFDSDNLSMKPYVYVKEVGSGVYENSCASGTTALGYYLKKCKNLDRAKIVQPNGWLEYIIENDEMYIDGPVEIIAEGKIYIGK

[Multiple Choices]
A. 5.1.3.14
B. 5.1.1.24
C. 1.14.14.154
D. 5.1.3.45
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

> The sequence-matched UniProt annotation assigns EC 5.1.1.24 and records the reaction L-histidine = D-histidine with experimental evidence cited to a 2024 study. This supports choice B, though the primary paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 265-residue sequence is compatible with a soluble, cofactor-independent racemase: it has cysteines that could support the acid/base chemistry used by some cofactor-independent amino-acid racemases, and it lacks an obvious PLP-binding signature. That gives a biologically meaningful, though not conclusive, basis for preferring the amino-acid racemase option B over the carbohydrate epimerase options (A and D) and the oxygenase (C).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence-based clues and transferable knowledge of cofactor-independent racemase mechanisms distinguish the offered classes probabilistically. They do not establish histidine as the substrate or prove this exact EC assignment, so the inference has limits; nevertheless, an exact target record is not required to make a meaningful choice among these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence-level inference or the sequence-matched experimental annotation.


### Important caveats

- The sequence clues are suggestive rather than diagnostic of histidine racemase activity.
- The cited annotation reports experimental evidence, but the underlying primary study was not independently checked.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 265-residue sequence is compatible with a soluble, cofactor-independent racemase: it has cysteines that could support the acid/base chemistry used by some cofactor-independent amino-acid racemases, and it lacks an obvious PLP-binding signature. That gives a biologically meaningful, though not conclusive, basis for preferring the amino-acid racemase option B over the carbohydrate epimerase options (A and D) and the oxygenase (C).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence-based clues and transferable knowledge of cofactor-independent racemase mechanisms distinguish the offered classes probabilistically. They do not establish histidine as the substrate or prove this exact EC assignment, so the inference has limits; nevertheless, an exact target record is not required to make a meaningful choice among these alternatives."
  },
  "case_id": "EC_number_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 5.1.1.24 and records the reaction L-histidine = D-histidine with experimental evidence cited to a 2024 study. This supports choice B, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence clues are suggestive rather than diagnostic of histidine racemase activity.",
    "The cited annotation reports experimental evidence, but the underlying primary study was not independently checked."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level inference or the sequence-matched experimental annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 5.1.1.24 and records the reaction L-histidine = D-histidine with experimental evidence cited to a 2024 study. This supports choice B, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 265-residue sequence is compatible with a soluble, cofactor-independent racemase: it has cysteines that could support the acid/base chemistry used by some cofactor-independent amino-acid racemases, and it lacks an obvious PLP-binding signature. That gives a biologically meaningful, though not conclusive, basis for preferring the amino-acid racemase option B over the carbohydrate epimerase options (A and D) and the oxygenase (C).",
    "missing_item_specific_fact": "",
    "reason": "The sequence-based clues and transferable knowledge of cofactor-independent racemase mechanisms distinguish the offered classes probabilistically. They do not establish histidine as the substrate or prove this exact EC assignment, so the inference has limits; nevertheless, an exact target record is not required to make a meaningful choice among these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level inference or the sequence-matched experimental annotation."
  },
  "important_caveats": [
    "The sequence clues are suggestive rather than diagnostic of histidine racemase activity.",
    "The cited annotation reports experimental evidence, but the underlying primary study was not independently checked."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8RI81 (HISR_FUSNN) is annotated as Histidine racemase with EC 5.1.1.24, supported by experimental evidence (ECO:0000269, PubMed:39424140, a 2024 JBC paper with X-ray crystallography at 2.5 Å, mutagenesis of Cys-67 and Cys-209, and catalytic activity assays confirming L-histidine = D-histidine). PDB structures 9CR1 and 9CR6 corroborate the structural and mechanistic assignment. The sequence in the question matches the entry exactly (265 aa, SHA256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (265 aa) contains conserved cysteine residues embedded in motifs such as 'GGEFCGNASRAF' (~Cys-67) and 'KCKNLDRAKIV' (~Cys-209), which are hallmark catalytic residues of the cofactor-independent amino acid racemase superfamily (EC 5.1.1.x; includes alanine racemase, cysteine racemase, and related enzymes). This cysteine-based catalytic mechanism is a well-known family-level feature transferable from other characterized racemases. Option C (1.14.14.154, a cytochrome P450) is eliminated because the sequence lacks the canonical heme-binding FxxGxxxCxG motif and is far too small (~265 aa vs. typical 400-550 aa P450s). Options A (5.1.3.14) and D (5.1.3.45) belong to the epimerase sub-class (5.1.3.x), which typically act on amino acid derivatives rather than free amino acids and often employ PLP-dependent or other non-cysteine mechanisms. The visible cysteine catalytic residues and the protein's size/architecture are consistent with the 5.1.1.x amino acid racemase class, of which only option B falls. The specific identification as histidine racemase is aided by the fact that B is the sole 5.1.1.x option among the four choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of the amino acid racemase superfamily (alanine racemase, cysteine racemase, etc.) can recognize the conserved catalytic cysteine residues and the ~265 aa size as hallmarks of EC 5.1.1.x. This family-level inference distinguishes option B from the epimerase options (A, D) and the P450 option (C) without needing to look up this specific protein's database annotation. The argument relies on transferable structural/mechanistic knowledge of related proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three distinct EC classes (5.1.3.x epimerases, 5.1.1.x amino acid racemase, 1.14.14.x P450), and the sequence features (cysteine motifs, absence of P450 signatures, size) provide a clear path to eliminate A, C, and D. Only B remains as a defensible choice.


### Important caveats

- The histidine racemase was only experimentally characterized in 2024 (PubMed:39424140). Prior to that, this enzyme's specific substrate preference (histidine vs. other amino acids) was unknown. However, the question only requires distinguishing among the four offered EC classes, not independently predicting the exact substrate.
- The cysteine-based racemase inference narrows the answer to the 5.1.1.x class. Distinguishing histidine racemase from, say, alanine racemase or cysteine racemase within 5.1.1.x would require more specific sequence knowledge, but no other 5.1.1.x option is offered.
- The annotation is based on a single experimental study (one PubMed reference, two PDB structures). While the evidence is solid, it is relatively recent and from a single laboratory.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (265 aa) contains conserved cysteine residues embedded in motifs such as 'GGEFCGNASRAF' (~Cys-67) and 'KCKNLDRAKIV' (~Cys-209), which are hallmark catalytic residues of the cofactor-independent amino acid racemase superfamily (EC 5.1.1.x; includes alanine racemase, cysteine racemase, and related enzymes). This cysteine-based catalytic mechanism is a well-known family-level feature transferable from other characterized racemases. Option C (1.14.14.154, a cytochrome P450) is eliminated because the sequence lacks the canonical heme-binding FxxGxxxCxG motif and is far too small (~265 aa vs. typical 400-550 aa P450s). Options A (5.1.3.14) and D (5.1.3.45) belong to the epimerase sub-class (5.1.3.x), which typically act on amino acid derivatives rather than free amino acids and often employ PLP-dependent or other non-cysteine mechanisms. The visible cysteine catalytic residues and the protein's size/architecture are consistent with the 5.1.1.x amino acid racemase class, of which only option B falls. The specific identification as histidine racemase is aided by the fact that B is the sole 5.1.1.x option among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the amino acid racemase superfamily (alanine racemase, cysteine racemase, etc.) can recognize the conserved catalytic cysteine residues and the ~265 aa size as hallmarks of EC 5.1.1.x. This family-level inference distinguishes option B from the epimerase options (A, D) and the P450 option (C) without needing to look up this specific protein's database annotation. The argument relies on transferable structural/mechanistic knowledge of related proteins."
  },
  "case_id": "EC_number_0187",
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
    "reason": "The UniProt entry Q8RI81 (HISR_FUSNN) is annotated as Histidine racemase with EC 5.1.1.24, supported by experimental evidence (ECO:0000269, PubMed:39424140, a 2024 JBC paper with X-ray crystallography at 2.5 Å, mutagenesis of Cys-67 and Cys-209, and catalytic activity assays confirming L-histidine = D-histidine). PDB structures 9CR1 and 9CR6 corroborate the structural and mechanistic assignment. The sequence in the question matches the entry exactly (265 aa, SHA256 match confirmed)."
  },
  "important_caveats": [
    "The histidine racemase was only experimentally characterized in 2024 (PubMed:39424140). Prior to that, this enzyme's specific substrate preference (histidine vs. other amino acids) was unknown. However, the question only requires distinguishing among the four offered EC classes, not independently predicting the exact substrate.",
    "The cysteine-based racemase inference narrows the answer to the 5.1.1.x class. Distinguishing histidine racemase from, say, alanine racemase or cysteine racemase within 5.1.1.x would require more specific sequence knowledge, but no other 5.1.1.x option is offered.",
    "The annotation is based on a single experimental study (one PubMed reference, two PDB structures). While the evidence is solid, it is relatively recent and from a single laboratory."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct EC classes (5.1.3.x epimerases, 5.1.1.x amino acid racemase, 1.14.14.x P450), and the sequence features (cysteine motifs, absence of P450 signatures, size) provide a clear path to eliminate A, C, and D. Only B remains as a defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8RI81 (HISR_FUSNN) is annotated as Histidine racemase with EC 5.1.1.24, supported by experimental evidence (ECO:0000269, PubMed:39424140, a 2024 JBC paper with X-ray crystallography at 2.5 Å, mutagenesis of Cys-67 and Cys-209, and catalytic activity assays confirming L-histidine = D-histidine). PDB structures 9CR1 and 9CR6 corroborate the structural and mechanistic assignment. The sequence in the question matches the entry exactly (265 aa, SHA256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (265 aa) contains conserved cysteine residues embedded in motifs such as 'GGEFCGNASRAF' (~Cys-67) and 'KCKNLDRAKIV' (~Cys-209), which are hallmark catalytic residues of the cofactor-independent amino acid racemase superfamily (EC 5.1.1.x; includes alanine racemase, cysteine racemase, and related enzymes). This cysteine-based catalytic mechanism is a well-known family-level feature transferable from other characterized racemases. Option C (1.14.14.154, a cytochrome P450) is eliminated because the sequence lacks the canonical heme-binding FxxGxxxCxG motif and is far too small (~265 aa vs. typical 400-550 aa P450s). Options A (5.1.3.14) and D (5.1.3.45) belong to the epimerase sub-class (5.1.3.x), which typically act on amino acid derivatives rather than free amino acids and often employ PLP-dependent or other non-cysteine mechanisms. The visible cysteine catalytic residues and the protein's size/architecture are consistent with the 5.1.1.x amino acid racemase class, of which only option B falls. The specific identification as histidine racemase is aided by the fact that B is the sole 5.1.1.x option among the four choices.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the amino acid racemase superfamily (alanine racemase, cysteine racemase, etc.) can recognize the conserved catalytic cysteine residues and the ~265 aa size as hallmarks of EC 5.1.1.x. This family-level inference distinguishes option B from the epimerase options (A, D) and the P450 option (C) without needing to look up this specific protein's database annotation. The argument relies on transferable structural/mechanistic knowledge of related proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct EC classes (5.1.3.x epimerases, 5.1.1.x amino acid racemase, 1.14.14.x P450), and the sequence features (cysteine motifs, absence of P450 signatures, size) provide a clear path to eliminate A, C, and D. Only B remains as a defensible choice."
  },
  "important_caveats": [
    "The histidine racemase was only experimentally characterized in 2024 (PubMed:39424140). Prior to that, this enzyme's specific substrate preference (histidine vs. other amino acids) was unknown. However, the question only requires distinguishing among the four offered EC classes, not independently predicting the exact substrate.",
    "The cysteine-based racemase inference narrows the answer to the 5.1.1.x class. Distinguishing histidine racemase from, say, alanine racemase or cysteine racemase within 5.1.1.x would require more specific sequence knowledge, but no other 5.1.1.x option is offered.",
    "The annotation is based on a single experimental study (one PubMed reference, two PDB structures). While the evidence is solid, it is relatively recent and from a single laboratory."
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
  "benchmark_sequence_length": 265,
  "benchmark_sequence_sha256": "366955426ff1f55c671654b2e899936080724ffe2dc1099a5aecf063554e039c",
  "current_entry_audit": {
    "entryVersion": 81,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 265,
  "current_source_sequence_sha256": "366955426ff1f55c671654b2e899936080724ffe2dc1099a5aecf063554e039c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 79,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8RI81",
  "selected_historical_entry_version": 79,
  "selected_historical_record_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "selected_historical_source_sequence_length": 265,
  "selected_historical_source_sequence_sha256": "366955426ff1f55c671654b2e899936080724ffe2dc1099a5aecf063554e039c",
  "selected_historical_version": {
    "accession": "Q8RI81",
    "database": "Swiss-Prot",
    "entryVersion": 79,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HISR_FUSNN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8RI81\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":81,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Fusobacteriati\",\"Fusobacteriota\",\"Fusobacteriia\",\"Fusobacteriales\",\"Fusobacteriaceae\",\"Fusobacterium\"],\"scientificName\":\"Fusobacterium nucleatum subsp. nucleatum (strain ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355)\",\"taxonId\":190304}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"5.1.1.24\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"Histidine racemase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.1.1.24\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"name\":\"L-histidine = D-histidine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:59188\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57595\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142967\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lamer T.\",\"Chen P.\",\"Venter M.J.\",\"van Belkum M.J.\",\"Wijewardane A.\",\"Wu C.\",\"Lemieux M.J.\",\"Vederas J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39424140\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107896\"}],\"citationType\":\"journal article\",\"firstPage\":\"107896\",\"id\":\"39424140\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107896\",\"publicationDate\":\"2024\",\"title\":\"Discovery, characterization, and structure of a cofactor-independent histidine racemase from the oral pathogen Fusobacterium nucleatum.\",\"volume\":\"300\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9CR1\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9CR6\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF CYS-67 AND CYS-209\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H1",
  "excerpt": "ID   HISR_FUSNN              Reviewed;         265 AA.\nAC   Q8RI81;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2002, sequence version 1.\nDT   28-JAN-2026, entry version 79.\nDE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};\nDE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};\nGN   Name=hisR {ECO:0000303|PubMed:39424140};\nGN   OrderedLocusNames=FN1732 {ECO:0000312|EMBL:AAL93847.1};\nOS   Fusobacterium nucleatum subsp. nucleatum (strain ATCC 25586 / DSM 15643 /\nOS   BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355).\nOC   Bacteria; Fusobacteriati; Fusobacteriota; Fusobacteriia; Fusobacteriales;\nOC   Fusobacteriaceae; Fusobacterium.\nOX   NCBI_TaxID=190304;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};\nDE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:9CR1, ECO:0007744|PDB:9CR6}\nRP   X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209,\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF CYS-67 AND CYS-209.\nRC   STRAIN=ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC\nRC   2640 / LMG 13131 / VPI 4355;\nRX   PubMed=39424140; DOI=10.1016/j.jbc.2024.107896;\nRA   Lamer T., Chen P., Venter M.J., van Belkum M.J., Wijewardane A., Wu C.,\nRA   Lemieux M.J., Vederas J.C.;\nRT   \"Discovery, characterization, and structure of a cofactor-independent\nRT   histidine racemase from the oral pathogen Fusobacterium nucleatum.\";\nRL   J. Biol. Chem. 300:107896-107896(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-histidine = D-histidine; Xref=Rhea:RHEA:59188,\nCC         ChEBI:CHEBI:57595, ChEBI:CHEBI:142967; EC=5.1.1.24;\nCC         Evidence={ECO:0000269|PubMed:39424140};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 187. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
