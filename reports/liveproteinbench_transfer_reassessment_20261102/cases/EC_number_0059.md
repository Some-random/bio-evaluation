# EC_number_0059

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0059.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 5.3.1.8

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLNDYLQWEKFILRGVEFPTRYRVDGDEVEITPSSRLYVSGMGGSGVVGDLIRDFSIVWNWDVEVTVVKDYFLRARDGLLIAVSYSGNTVETLYSVEYAKKRRIPTVAITTGGKLAQMGVPTIIIPKASAPRAALPQMLTAALHVVRKVYGIPIEIPEALEPPNDPLIHKLMEDFQKRPTIVAPETMRGVAYRVKNEFNENAKIEPSVEILPEAHHNWIEGSERPIVALTSPHIPREHQERVKATLEILGGTLYVVEMSTRGVLTFLREVGVASIKLAESRGVNPLATPRIEALKRRLQ

[Multiple Choices]
A. 5.3.1.8
B. 5.3.99.13
C. 1.1.1.195
D. 2.7.7.43
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

> The supplied sequence exactly matches the reviewed UniProt sequence, whose catalytic-activity annotation assigns EC 5.3.1.8 to conversion of D-mannose 6-phosphate to D-fructose 6-phosphate, with experimental evidence cited. Thus option A is a supported activity for this protein.

Citations as saved: [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a compact sugar-phosphate isomerase family protein. Family-level recognition and transferable knowledge of phosphosugar isomerases provide a meaningful basis for an intramolecular isomerase classification (EC 5.3), rather than the oxidoreductase or transferase choices. Among the two isomerase options, EC 5.3.99.13 is a different isomerase class; EC 5.3.1.8 is the phosphomannose-isomerase activity compatible with this family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference can distinguish the offered phosphosugar-isomerase choice from the unrelated enzyme classes; exact experimental characterization of this protein is not necessary to make that distinction. The sequence alone may not establish every activity of a bifunctional enzyme.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A among the offered choices is supported as an activity for this protein. The protein is also annotated with EC 5.3.1.9, but that number is not offered.


### Important caveats

- The evidence annotates the protein as bifunctional, with both EC 5.3.1.8 and EC 5.3.1.9 activities; the single-answer choices omit the latter.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a compact sugar-phosphate isomerase family protein. Family-level recognition and transferable knowledge of phosphosugar isomerases provide a meaningful basis for an intramolecular isomerase classification (EC 5.3), rather than the oxidoreductase or transferase choices. Among the two isomerase options, EC 5.3.99.13 is a different isomerase class; EC 5.3.1.8 is the phosphomannose-isomerase activity compatible with this family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the offered phosphosugar-isomerase choice from the unrelated enzyme classes; exact experimental characterization of this protein is not necessary to make that distinction. The sequence alone may not establish every activity of a bifunctional enzyme."
  },
  "case_id": "EC_number_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence, whose catalytic-activity annotation assigns EC 5.3.1.8 to conversion of D-mannose 6-phosphate to D-fructose 6-phosphate, with experimental evidence cited. Thus option A is a supported activity for this protein."
  },
  "important_caveats": [
    "The evidence annotates the protein as bifunctional, with both EC 5.3.1.8 and EC 5.3.1.9 activities; the single-answer choices omit the latter."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the offered choices is supported as an activity for this protein. The protein is also annotated with EC 5.3.1.9, but that number is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence, whose catalytic-activity annotation assigns EC 5.3.1.8 to conversion of D-mannose 6-phosphate to D-fructose 6-phosphate, with experimental evidence cited. Thus option A is a supported activity for this protein.",
    "evidence_ids": ["C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a compact sugar-phosphate isomerase family protein. Family-level recognition and transferable knowledge of phosphosugar isomerases provide a meaningful basis for an intramolecular isomerase classification (EC 5.3), rather than the oxidoreductase or transferase choices. Among the two isomerase options, EC 5.3.99.13 is a different isomerase class; EC 5.3.1.8 is the phosphomannose-isomerase activity compatible with this family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the offered phosphosugar-isomerase choice from the unrelated enzyme classes; exact experimental characterization of this protein is not necessary to make that distinction. The sequence alone may not establish every activity of a bifunctional enzyme."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the offered choices is supported as an activity for this protein. The protein is also annotated with EC 5.3.1.9, but that number is not offered."
  },
  "important_caveats": [
    "The evidence annotates the protein as bifunctional, with both EC 5.3.1.8 and EC 5.3.1.9 activities; the single-answer choices omit the latter."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A3MTR6 (PGMI_PYRCJ) is experimentally annotated (ECO:0000269, PubMed 39208883) as a bifunctional phosphoglucose/phosphomannose isomerase with both EC 5.3.1.8 (mannose-6-phosphate isomerase) and EC 5.3.1.9 (glucose-6-phosphate isomerase) activities. The author's key of 5.3.1.8 is one of the two experimentally confirmed EC numbers. Since 5.3.1.9 is not among the offered choices, A (5.3.1.8) is the correct answer from the available options.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical P-loop/glycine-rich motif 'GMGGSGVVGDL' and an 'SGNT' motif in the active-site region, together with an overall ~300-aa architecture characteristic of the phosphoglucose/phosphomannose isomerase (PGI/PMI) superfamily. This family catalyzes aldose-ketose isomerization of phosphorylated sugars and is classified under EC 5.3.1.x (isomerases of carbohydrates). Among the four choices: C (1.1.1.195, an oxidoreductase) is excluded because the sequence lacks NAD(P)-binding Rossmann motifs and dehydrogenase catalytic residues; D (2.7.7.43, a nucleotidyltransferase) is excluded because the sequence lacks nucleotidyltransferase motifs; B (5.3.99.13, an isomerase transposing C=C bonds) is excluded because the PGI/PMI fold and active-site architecture are incompatible with C=C bond transposition chemistry. Only A (5.3.1.8) falls within the 5.3.1.x carbohydrate-isomerase class that matches the identified PGI/PMI family fold. Recognizing the P-loop and SGNT motifs as hallmarks of the PGI/PMI family is transferable knowledge from homologous proteins in bacteria, archaea, and eukaryotes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P-loop motif (GMGGSGVVGDL), the SGNT active-site motif, and the overall ~300-aa PGI/PMI architecture are sequence features shared across the PGI/PMI superfamily. A model familiar with this family can assign the protein to EC 5.3.1.x and, among the offered choices, select A as the only 5.3.1.x option. No target-specific annotation or memorization of this exact protein's record is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the enzyme is bifunctional (5.3.1.8 and 5.3.1.9), only 5.3.1.8 appears among the four choices. The other options belong to clearly different enzyme classes (oxidoreductase, nucleotidyltransferase, or a different isomerase subclass), so no ambiguity exists among the provided alternatives.


### Important caveats

- The enzyme is experimentally confirmed as bifunctional (both 5.3.1.8 and 5.3.1.9). The question only offers 5.3.1.8, so the bifunctional aspect does not create ambiguity among the given choices.
- The P-loop motif is found in many enzyme families; its assignment to PGI/PMI specifically relies on the combination with the SGNT motif, overall fold architecture, and sequence length, which together are diagnostic of the PGI/PMI superfamily.
- EC 5.3.99.13 is a very obscure entry; a model unfamiliar with its exact definition might find it harder to rule out, but the PGI/PMI family architecture is incompatible with C=C bond transposition chemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical P-loop/glycine-rich motif 'GMGGSGVVGDL' and an 'SGNT' motif in the active-site region, together with an overall ~300-aa architecture characteristic of the phosphoglucose/phosphomannose isomerase (PGI/PMI) superfamily. This family catalyzes aldose-ketose isomerization of phosphorylated sugars and is classified under EC 5.3.1.x (isomerases of carbohydrates). Among the four choices: C (1.1.1.195, an oxidoreductase) is excluded because the sequence lacks NAD(P)-binding Rossmann motifs and dehydrogenase catalytic residues; D (2.7.7.43, a nucleotidyltransferase) is excluded because the sequence lacks nucleotidyltransferase motifs; B (5.3.99.13, an isomerase transposing C=C bonds) is excluded because the PGI/PMI fold and active-site architecture are incompatible with C=C bond transposition chemistry. Only A (5.3.1.8) falls within the 5.3.1.x carbohydrate-isomerase class that matches the identified PGI/PMI family fold. Recognizing the P-loop and SGNT motifs as hallmarks of the PGI/PMI family is transferable knowledge from homologous proteins in bacteria, archaea, and eukaryotes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif (GMGGSGVVGDL), the SGNT active-site motif, and the overall ~300-aa PGI/PMI architecture are sequence features shared across the PGI/PMI superfamily. A model familiar with this family can assign the protein to EC 5.3.1.x and, among the offered choices, select A as the only 5.3.1.x option. No target-specific annotation or memorization of this exact protein's record is required."
  },
  "case_id": "EC_number_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A3MTR6 (PGMI_PYRCJ) is experimentally annotated (ECO:0000269, PubMed 39208883) as a bifunctional phosphoglucose/phosphomannose isomerase with both EC 5.3.1.8 (mannose-6-phosphate isomerase) and EC 5.3.1.9 (glucose-6-phosphate isomerase) activities. The author's key of 5.3.1.8 is one of the two experimentally confirmed EC numbers. Since 5.3.1.9 is not among the offered choices, A (5.3.1.8) is the correct answer from the available options."
  },
  "important_caveats": [
    "The enzyme is experimentally confirmed as bifunctional (both 5.3.1.8 and 5.3.1.9). The question only offers 5.3.1.8, so the bifunctional aspect does not create ambiguity among the given choices.",
    "The P-loop motif is found in many enzyme families; its assignment to PGI/PMI specifically relies on the combination with the SGNT motif, overall fold architecture, and sequence length, which together are diagnostic of the PGI/PMI superfamily.",
    "EC 5.3.99.13 is a very obscure entry; a model unfamiliar with its exact definition might find it harder to rule out, but the PGI/PMI family architecture is incompatible with C=C bond transposition chemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the enzyme is bifunctional (5.3.1.8 and 5.3.1.9), only 5.3.1.8 appears among the four choices. The other options belong to clearly different enzyme classes (oxidoreductase, nucleotidyltransferase, or a different isomerase subclass), so no ambiguity exists among the provided alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A3MTR6 (PGMI_PYRCJ) is experimentally annotated (ECO:0000269, PubMed 39208883) as a bifunctional phosphoglucose/phosphomannose isomerase with both EC 5.3.1.8 (mannose-6-phosphate isomerase) and EC 5.3.1.9 (glucose-6-phosphate isomerase) activities. The author's key of 5.3.1.8 is one of the two experimentally confirmed EC numbers. Since 5.3.1.9 is not among the offered choices, A (5.3.1.8) is the correct answer from the available options.",
    "evidence_ids": ["C4", "C6", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical P-loop/glycine-rich motif 'GMGGSGVVGDL' and an 'SGNT' motif in the active-site region, together with an overall ~300-aa architecture characteristic of the phosphoglucose/phosphomannose isomerase (PGI/PMI) superfamily. This family catalyzes aldose-ketose isomerization of phosphorylated sugars and is classified under EC 5.3.1.x (isomerases of carbohydrates). Among the four choices: C (1.1.1.195, an oxidoreductase) is excluded because the sequence lacks NAD(P)-binding Rossmann motifs and dehydrogenase catalytic residues; D (2.7.7.43, a nucleotidyltransferase) is excluded because the sequence lacks nucleotidyltransferase motifs; B (5.3.99.13, an isomerase transposing C=C bonds) is excluded because the PGI/PMI fold and active-site architecture are incompatible with C=C bond transposition chemistry. Only A (5.3.1.8) falls within the 5.3.1.x carbohydrate-isomerase class that matches the identified PGI/PMI family fold. Recognizing the P-loop and SGNT motifs as hallmarks of the PGI/PMI family is transferable knowledge from homologous proteins in bacteria, archaea, and eukaryotes.",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif (GMGGSGVVGDL), the SGNT active-site motif, and the overall ~300-aa PGI/PMI architecture are sequence features shared across the PGI/PMI superfamily. A model familiar with this family can assign the protein to EC 5.3.1.x and, among the offered choices, select A as the only 5.3.1.x option. No target-specific annotation or memorization of this exact protein's record is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the enzyme is bifunctional (5.3.1.8 and 5.3.1.9), only 5.3.1.8 appears among the four choices. The other options belong to clearly different enzyme classes (oxidoreductase, nucleotidyltransferase, or a different isomerase subclass), so no ambiguity exists among the provided alternatives."
  },
  "important_caveats": [
    "The enzyme is experimentally confirmed as bifunctional (both 5.3.1.8 and 5.3.1.9). The question only offers 5.3.1.8, so the bifunctional aspect does not create ambiguity among the given choices.",
    "The P-loop motif is found in many enzyme families; its assignment to PGI/PMI specifically relies on the combination with the SGNT motif, overall fold architecture, and sequence length, which together are diagnostic of the PGI/PMI superfamily.",
    "EC 5.3.99.13 is a very obscure entry; a model unfamiliar with its exact definition might find it harder to rule out, but the PGI/PMI family architecture is incompatible with C=C bond transposition chemistry."
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
  "benchmark_sequence_length": 299,
  "benchmark_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "current_entry_audit": {
    "entryVersion": 75,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-04-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 299,
  "current_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A3MTR6",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "selected_historical_source_sequence_length": 299,
  "selected_historical_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "selected_historical_version": {
    "accession": "A3MTR6",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PGMI_PYRCJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A3MTR6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":75,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-04-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Thermoproteota\",\"Thermoprotei\",\"Thermoproteales\",\"Thermoproteaceae\",\"Pyrobaculum\"],\"scientificName\":\"Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1)\",\"taxonId\":410359}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Glucose-6-phosphate isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"GPI\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Mannose-6-phosphate isomerase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.8\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional phosphoglucose/phosphomannose isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Bifunctional PGI/PMI\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.3.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"name\":\"alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:11816\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57634\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58225\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.3.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"name\":\"D-mannose 6-phosphate = D-fructose 6-phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:12356\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58735\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Maqsood A.\",\"Shakir N.A.\",\"Aslam M.\",\"Rahman M.\",\"Rashid N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39208883\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2024.135127\"}],\"citationType\":\"journal article\",\"firstPage\":\"135127\",\"id\":\"39208883\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"135127\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional investigations of Pcal_0606, a bifunctional phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\",\"volume\":\"279\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 21063 / JCM 11548 / VA1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   PGMI_PYRCJ              Reviewed;         299 AA.\nAC   A3MTR6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-APR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=Bifunctional phosphoglucose/phosphomannose isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=Bifunctional PGI/PMI {ECO:0000305};\nDE            EC=5.3.1.8 {ECO:0000269|PubMed:39208883};\nDE            EC=5.3.1.9 {ECO:0000269|PubMed:39208883};\nDE   AltName: Full=Glucose-6-phosphate isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=GPI {ECO:0000305};\nDE   AltName: Full=Mannose-6-phosphate isomerase {ECO:0000305};\nGN   OrderedLocusNames=Pcal_0606 {ECO:0000312|EMBL:ABO08033.1};\nOS   Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1).\nOC   Archaea; Thermoproteota; Thermoprotei; Thermoproteales; Thermoproteaceae;\nOC   Pyrobaculum.\nOX   NCBI_TaxID=410359;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Bifunctional phosphoglucose/phosphomannose isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=Bifunctional PGI/PMI {ECO:0000305};\nDE            EC=5.3.1.8 {ECO:0000269|PubMed:39208883};\nDE            EC=5.3.1.9 {ECO:0000269|PubMed:39208883};\nDE   AltName: Full=Glucose-6-phosphate isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=GPI {ECO:0000305};\nDE   AltName: Full=Mannose-6-phosphate isomerase {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 21063 / JCM 11548 / VA1;\nRX   PubMed=39208883; DOI=10.1016/j.ijbiomac.2024.135127;\nRA   Maqsood A., Shakir N.A., Aslam M., Rahman M., Rashid N.;\nRT   \"Structural and functional investigations of Pcal_0606, a bifunctional\nRT   phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\";\nRL   Int. J. Biol. Macromol. 279:135127-135127(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate;\nCC         Xref=Rhea:RHEA:11816, ChEBI:CHEBI:57634, ChEBI:CHEBI:58225;\nCC         EC=5.3.1.9; Evidence={ECO:0000269|PubMed:39208883};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-mannose 6-phosphate = D-fructose 6-phosphate;\nCC         Xref=Rhea:RHEA:12356, ChEBI:CHEBI:58735, ChEBI:CHEBI:61527;\nCC         EC=5.3.1.8; Evidence={ECO:0000269|PubMed:39208883};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 59. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
