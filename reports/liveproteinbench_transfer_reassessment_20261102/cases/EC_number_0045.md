# EC_number_0045

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0045.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 4.2.1.70

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKTDFSHDLLRFSDEVKEALHSGKPVVALESTVIAHGLPYPENVATARKIEAAVRAEGAIPATIGIENGRFLIGMSDADLERFGSTRGIPKASSRDIPVILAQGGMGATTVASSLVAADLAGIPFFASAGIGGVHRGAERSMDISADLIQFTRSRVAVVCAGAKSILDLGLTLEYLETQCVPIISYQSDDFPAFYCRSSGFHSPHRLDDATVIARSIDMHWKLGNQSSVLITHPIHEEDAIGTDEVESIIREAAVQAEHEGIRGPGATPYLMRAVAKATEGKTVKANMSVLISTAALAGKLACAHIDYLRQQNQA

[Multiple Choices]
A. 4.2.1.18
B. 3.1.1.29
C. 4.2.1.70
D. 4.1.1.129
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

> The matched-sequence UniProt annotation assigns EC 4.2.1.70 and the reaction consistent with that EC. The assignment is supported by a HAMAP computational rule, not by experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 316-residue sequence can be recognized by homology and conserved sequence patterns as belonging to the bacterial PsuG/IndA-like enzyme family. Transferable knowledge of that family’s function points to pseudouridine-5'-phosphate glycosidase activity, corresponding to EC 4.2.1.70 (C); the other choices describe different enzyme activities.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition provides a meaningful basis for choosing among these substantially different EC alternatives without needing the exact protein’s recorded annotation. This is a homology-based inference, not a guarantee of experimentally verified activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify distinct EC activities, and the sequence-family inference favors C.


### Important caveats

- The reviewer-only annotation is computationally supported by HAMAP; the excerpts do not establish independent experimental validation.
- The source sequence matches the input, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 316-residue sequence can be recognized by homology and conserved sequence patterns as belonging to the bacterial PsuG/IndA-like enzyme family. Transferable knowledge of that family’s function points to pseudouridine-5'-phosphate glycosidase activity, corresponding to EC 4.2.1.70 (C); the other choices describe different enzyme activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a meaningful basis for choosing among these substantially different EC alternatives without needing the exact protein’s recorded annotation. This is a homology-based inference, not a guarantee of experimentally verified activity."
  },
  "case_id": "EC_number_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 4.2.1.70 and the reaction consistent with that EC. The assignment is supported by a HAMAP computational rule, not by experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only annotation is computationally supported by HAMAP; the excerpts do not establish independent experimental validation.",
    "The source sequence matches the input, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC activities, and the sequence-family inference favors C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 4.2.1.70 and the reaction consistent with that EC. The assignment is supported by a HAMAP computational rule, not by experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 316-residue sequence can be recognized by homology and conserved sequence patterns as belonging to the bacterial PsuG/IndA-like enzyme family. Transferable knowledge of that family’s function points to pseudouridine-5'-phosphate glycosidase activity, corresponding to EC 4.2.1.70 (C); the other choices describe different enzyme activities.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a meaningful basis for choosing among these substantially different EC alternatives without needing the exact protein’s recorded annotation. This is a homology-based inference, not a guarantee of experimentally verified activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC activities, and the sequence-family inference favors C."
  },
  "important_caveats": [
    "The reviewer-only annotation is computationally supported by HAMAP; the excerpts do not establish independent experimental validation.",
    "The source sequence matches the input, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9L393 (PSUG_DICD3) is annotated with EC 4.2.1.70 (Pseudouridine-5'-phosphate glycosidase) based on HAMAP-Rule MF_01876 (evidence code ECO:0000255, computational/probabilistic annotation). The benchmark sequence (316 aa) matches the UniProt sequence exactly. The catalytic reaction (D-ribose 5-phosphate + uracil = psi-UMP + H2O) is consistent with EC 4.2.1.70. The annotation is computational rather than experimentally validated, but it is the authoritative database assignment and supports the expected answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two prominent Rossmann-fold motifs: 'GGMGAT' (GxGxxG at ~position 105) and 'AGIGGVHRG' (~position 130), which are hallmarks of nucleotide/small-molecule binding domains. This architecture is consistent with PsiMP glycosidase (EC 4.2.1.70), which binds the nucleotide sugar psi-UMP and ribose-5-phosphate. In contrast: (1) EC 3.1.1.29 (carboxylesterase) requires an alpha/beta-hydrolase fold with a GxSxG nucleophile motif and Ser-His-Asp triad, neither of which is present; (2) EC 4.1.1.129 (4-hydroxyphenylpyruvate dioxygenase) requires a 2-His-1-carboxylate iron-binding facial triad and a specific HPPD fold, absent here; (3) EC 4.2.1.18 (DNA AP-site lyase) enzymes (e.g., EndoIII/Nth, Fpg) belong to the HhH-GPD or zinc-finger superfamily with DNA-binding motifs (helix-hairpin-helix, zinc finger), not Rossmann folds, and typically show higher positive-charge density for DNA interaction. The prominent Rossmann-fold architecture and absence of DNA-binding or alpha/beta-hydrolase features provide a transferable structural argument favoring 4.2.1.70 over the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use Rossmann-fold motif recognition (transferable from many nucleotide-binding proteins), the absence of alpha/beta-hydrolase features (to rule out 3.1.1.29), the absence of iron-binding triads (to rule out 4.1.1.129), and the absence of HhH/DNA-binding motifs typical of AP lyases (to rule out 4.2.1.18). The 4.2.1.18 vs 4.2.1.70 distinction is the most challenging but is addressed by the Rossmann-fold vs. HhH-GPD architectural difference, which is well-established transferable structural biology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different EC classes (3, 4.1, 4.2) and two sub-classes within 4.2 (4.2.1.18 vs 4.2.1.70). The Rossmann-fold architecture and absence of DNA-binding or hydrolase features provide a reasonable basis to select 4.2.1.70. While the 4.2.1.18 vs 4.2.1.70 distinction is narrow, the structural arguments are sufficiently differentiating.


### Important caveats

- The UniProt annotation for EC 4.2.1.70 is based on HAMAP-Rule MF_01876 (ECO:0000255), a computational/probabilistic assignment, not direct experimental enzymology.
- The distinction between EC 4.2.1.18 and EC 4.2.1.70 is the most challenging aspect; while Rossmann-fold architecture argues against AP lyase, some AP lyase subfamilies have diverse architectures, so the argument is probabilistic rather than definitive.
- The protein is IndA/psuG from Dickeya dadantii, involved in indigoidine biosynthesis; this specific biological context was not provided in the original input and would further confirm the answer but is not required for the structural reasoning argument.
- The source annotation was first integrated into Swiss-Prot on 2025-02-05; the author's data-construction date is unknown, so the annotation may or may not have been available at construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two prominent Rossmann-fold motifs: 'GGMGAT' (GxGxxG at ~position 105) and 'AGIGGVHRG' (~position 130), which are hallmarks of nucleotide/small-molecule binding domains. This architecture is consistent with PsiMP glycosidase (EC 4.2.1.70), which binds the nucleotide sugar psi-UMP and ribose-5-phosphate. In contrast: (1) EC 3.1.1.29 (carboxylesterase) requires an alpha/beta-hydrolase fold with a GxSxG nucleophile motif and Ser-His-Asp triad, neither of which is present; (2) EC 4.1.1.129 (4-hydroxyphenylpyruvate dioxygenase) requires a 2-His-1-carboxylate iron-binding facial triad and a specific HPPD fold, absent here; (3) EC 4.2.1.18 (DNA AP-site lyase) enzymes (e.g., EndoIII/Nth, Fpg) belong to the HhH-GPD or zinc-finger superfamily with DNA-binding motifs (helix-hairpin-helix, zinc finger), not Rossmann folds, and typically show higher positive-charge density for DNA interaction. The prominent Rossmann-fold architecture and absence of DNA-binding or alpha/beta-hydrolase features provide a transferable structural argument favoring 4.2.1.70 over the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use Rossmann-fold motif recognition (transferable from many nucleotide-binding proteins), the absence of alpha/beta-hydrolase features (to rule out 3.1.1.29), the absence of iron-binding triads (to rule out 4.1.1.129), and the absence of HhH/DNA-binding motifs typical of AP lyases (to rule out 4.2.1.18). The 4.2.1.18 vs 4.2.1.70 distinction is the most challenging but is addressed by the Rossmann-fold vs. HhH-GPD architectural difference, which is well-established transferable structural biology knowledge."
  },
  "case_id": "EC_number_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9L393 (PSUG_DICD3) is annotated with EC 4.2.1.70 (Pseudouridine-5'-phosphate glycosidase) based on HAMAP-Rule MF_01876 (evidence code ECO:0000255, computational/probabilistic annotation). The benchmark sequence (316 aa) matches the UniProt sequence exactly. The catalytic reaction (D-ribose 5-phosphate + uracil = psi-UMP + H2O) is consistent with EC 4.2.1.70. The annotation is computational rather than experimentally validated, but it is the authoritative database assignment and supports the expected answer."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.2.1.70 is based on HAMAP-Rule MF_01876 (ECO:0000255), a computational/probabilistic assignment, not direct experimental enzymology.",
    "The distinction between EC 4.2.1.18 and EC 4.2.1.70 is the most challenging aspect; while Rossmann-fold architecture argues against AP lyase, some AP lyase subfamilies have diverse architectures, so the argument is probabilistic rather than definitive.",
    "The protein is IndA/psuG from Dickeya dadantii, involved in indigoidine biosynthesis; this specific biological context was not provided in the original input and would further confirm the answer but is not required for the structural reasoning argument.",
    "The source annotation was first integrated into Swiss-Prot on 2025-02-05; the author's data-construction date is unknown, so the annotation may or may not have been available at construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC classes (3, 4.1, 4.2) and two sub-classes within 4.2 (4.2.1.18 vs 4.2.1.70). The Rossmann-fold architecture and absence of DNA-binding or hydrolase features provide a reasonable basis to select 4.2.1.70. While the 4.2.1.18 vs 4.2.1.70 distinction is narrow, the structural arguments are sufficiently differentiating."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9L393 (PSUG_DICD3) is annotated with EC 4.2.1.70 (Pseudouridine-5'-phosphate glycosidase) based on HAMAP-Rule MF_01876 (evidence code ECO:0000255, computational/probabilistic annotation). The benchmark sequence (316 aa) matches the UniProt sequence exactly. The catalytic reaction (D-ribose 5-phosphate + uracil = psi-UMP + H2O) is consistent with EC 4.2.1.70. The annotation is computational rather than experimentally validated, but it is the authoritative database assignment and supports the expected answer.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two prominent Rossmann-fold motifs: 'GGMGAT' (GxGxxG at ~position 105) and 'AGIGGVHRG' (~position 130), which are hallmarks of nucleotide/small-molecule binding domains. This architecture is consistent with PsiMP glycosidase (EC 4.2.1.70), which binds the nucleotide sugar psi-UMP and ribose-5-phosphate. In contrast: (1) EC 3.1.1.29 (carboxylesterase) requires an alpha/beta-hydrolase fold with a GxSxG nucleophile motif and Ser-His-Asp triad, neither of which is present; (2) EC 4.1.1.129 (4-hydroxyphenylpyruvate dioxygenase) requires a 2-His-1-carboxylate iron-binding facial triad and a specific HPPD fold, absent here; (3) EC 4.2.1.18 (DNA AP-site lyase) enzymes (e.g., EndoIII/Nth, Fpg) belong to the HhH-GPD or zinc-finger superfamily with DNA-binding motifs (helix-hairpin-helix, zinc finger), not Rossmann folds, and typically show higher positive-charge density for DNA interaction. The prominent Rossmann-fold architecture and absence of DNA-binding or alpha/beta-hydrolase features provide a transferable structural argument favoring 4.2.1.70 over the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use Rossmann-fold motif recognition (transferable from many nucleotide-binding proteins), the absence of alpha/beta-hydrolase features (to rule out 3.1.1.29), the absence of iron-binding triads (to rule out 4.1.1.129), and the absence of HhH/DNA-binding motifs typical of AP lyases (to rule out 4.2.1.18). The 4.2.1.18 vs 4.2.1.70 distinction is the most challenging but is addressed by the Rossmann-fold vs. HhH-GPD architectural difference, which is well-established transferable structural biology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC classes (3, 4.1, 4.2) and two sub-classes within 4.2 (4.2.1.18 vs 4.2.1.70). The Rossmann-fold architecture and absence of DNA-binding or hydrolase features provide a reasonable basis to select 4.2.1.70. While the 4.2.1.18 vs 4.2.1.70 distinction is narrow, the structural arguments are sufficiently differentiating."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.2.1.70 is based on HAMAP-Rule MF_01876 (ECO:0000255), a computational/probabilistic assignment, not direct experimental enzymology.",
    "The distinction between EC 4.2.1.18 and EC 4.2.1.70 is the most challenging aspect; while Rossmann-fold architecture argues against AP lyase, some AP lyase subfamilies have diverse architectures, so the argument is probabilistic rather than definitive.",
    "The protein is IndA/psuG from Dickeya dadantii, involved in indigoidine biosynthesis; this specific biological context was not provided in the original input and would further confirm the answer but is not required for the structural reasoning argument.",
    "The source annotation was first integrated into Swiss-Prot on 2025-02-05; the author's data-construction date is unknown, so the annotation may or may not have been available at construction time."
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
  "benchmark_sequence_length": 316,
  "benchmark_sequence_sha256": "79ec54a1b9a163f1fff48088a706f31d4fafb5f1834f53349d86da2f5110f685",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 316,
  "current_source_sequence_sha256": "79ec54a1b9a163f1fff48088a706f31d4fafb5f1834f53349d86da2f5110f685",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9L393",
  "selected_historical_entry_version": 67,
  "selected_historical_record_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "selected_historical_source_sequence_length": 316,
  "selected_historical_source_sequence_sha256": "79ec54a1b9a163f1fff48088a706f31d4fafb5f1834f53349d86da2f5110f685",
  "selected_historical_version": {
    "accession": "Q9L393",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PSUG_DICD3",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9L393\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Erwinia chrysanthemi (strain 3937)\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Pectobacteriaceae\",\"Dickeya\"],\"scientificName\":\"Dickeya dadantii (strain 3937)\",\"taxonId\":198628}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"4.2.1.70\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Pseudouridine-5'-phosphate glycosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"value\":\"PsiMP glycosidase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"4.2.1.70\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01876\",\"source\":\"HAMAP-Rule\"}],\"name\":\"D-ribose 5-phosphate + uracil = psi-UMP + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:18337\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17568\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58380\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:78346\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:05.918269+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L393.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H1",
  "excerpt": "ID   PSUG_DICD3              Reviewed;         316 AA.\nAC   Q9L393; E0SMH8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Pseudouridine-5'-phosphate glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            Short=PsiMP glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            EC=4.2.1.70 {ECO:0000255|HAMAP-Rule:MF_01876};\nGN   Name=indA {ECO:0000303|PubMed:11790734};\nGN   Synonyms=psuG {ECO:0000255|HAMAP-Rule:MF_01876};\nGN   OrderedLocusNames=Dda3937_00974 {ECO:0000312|EMBL:ADN00617.1};\nOS   Dickeya dadantii (strain 3937) (Erwinia chrysanthemi (strain 3937)).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Pectobacteriaceae; Dickeya.\nOX   NCBI_TaxID=198628;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Pseudouridine-5'-phosphate glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            Short=PsiMP glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};\nDE            EC=4.2.1.70 {ECO:0000255|HAMAP-Rule:MF_01876};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB87988.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, INDUCTION, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=3937;\nRX   PubMed=11790734; DOI=10.1128/jb.184.3.654-665.2002;\nRA   Reverchon S., Rouanet C., Expert D., Nasser W.;\nRT   \"Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi\nRT   and role of this blue pigment in pathogenicity.\";\nRL   J. Bacteriol. 184:654-665(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-ribose 5-phosphate + uracil = psi-UMP + H2O;\nCC         Xref=Rhea:RHEA:18337, ChEBI:CHEBI:15377, ChEBI:CHEBI:17568,\nCC         ChEBI:CHEBI:58380, ChEBI:CHEBI:78346; EC=4.2.1.70;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_01876};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.935581+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea",
  "url": "https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
