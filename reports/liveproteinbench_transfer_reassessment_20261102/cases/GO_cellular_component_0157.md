# GO_cellular_component_0157

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0157.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKNQFAVLLVALVLLQLFSQSEAFWSTLLSIGKSLLGKRGLRNFDLEQMDDTYEPELSEADLRYLQDLLR

[Multiple Choices]
A. ATAC complex
B. aggresome
C. membrane
D. spindle
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation lists both secretion and target cell membrane, supporting the keyed membrane choice among the offered options. This is a database annotation citing literature, not independent experimental verification here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The strongly hydrophobic N-terminal segment is characteristic of a secretion signal, while the remaining short peptide has both basic and hydrophobic residues, a pattern compatible with a secreted, membrane-active peptide. That makes membrane more plausible than the offered intracellular complex, aggregate, or spindle choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a credible transferable basis for favoring membrane among these alternatives, although a signal peptide alone does not prove that a protein remains membrane-localized rather than being secreted.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence and biological pattern support membrane over the other listed choices; no second offered option is comparably defensible.


### Important caveats

- The source annotation also describes the protein as secreted, and an extracellular-region GO annotation is present. The exact distinction between secretion and target-membrane association is not established by sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic N-terminal segment is characteristic of a secretion signal, while the remaining short peptide has both basic and hydrophobic residues, a pattern compatible with a secreted, membrane-active peptide. That makes membrane more plausible than the offered intracellular complex, aggregate, or spindle choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a credible transferable basis for favoring membrane among these alternatives, although a signal peptide alone does not prove that a protein remains membrane-localized rather than being secreted."
  },
  "case_id": "GO_cellular_component_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists both secretion and target cell membrane, supporting the keyed membrane choice among the offered options. This is a database annotation citing literature, not independent experimental verification here."
  },
  "important_caveats": [
    "The source annotation also describes the protein as secreted, and an extracellular-region GO annotation is present. The exact distinction between secretion and target-membrane association is not established by sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and biological pattern support membrane over the other listed choices; no second offered option is comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists both secretion and target cell membrane, supporting the keyed membrane choice among the offered options. This is a database annotation citing literature, not independent experimental verification here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The strongly hydrophobic N-terminal segment is characteristic of a secretion signal, while the remaining short peptide has both basic and hydrophobic residues, a pattern compatible with a secreted, membrane-active peptide. That makes membrane more plausible than the offered intracellular complex, aggregate, or spindle choices.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a credible transferable basis for favoring membrane among these alternatives, although a signal peptide alone does not prove that a protein remains membrane-localized rather than being secreted."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and biological pattern support membrane over the other listed choices; no second offered option is comparably defensible."
  },
  "important_caveats": [
    "The source annotation also describes the protein as secreted, and an extracellular-region GO annotation is present. The exact distinction between secretion and target-membrane association is not established by sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DRH3 annotates this protein's subcellular location as 'Secreted' and 'Target cell membrane' (ECO:0000305, PubMed:25659089). The GO annotation includes GO:0044218 (other organism cell membrane), which is a child of GO:0016020 (membrane). Among the four offered choices, 'membrane' (GO:0016020) is directly supported by the 'Target cell membrane' annotation and the GO:0044218 cross-reference. The evidence codes are ECO:0000305 (author statement based on a single publication) and IEA (inferred from electronic annotation), so this is annotation-level support rather than direct experimental localization, but it is consistent and supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence MKNQFAVLLVALVLLQLFSQS is a canonical signal peptide: ~20 hydrophobic residues at the extreme N-terminus, characteristic of proteins entering the ER/Golgi secretory pathway. This single feature immediately excludes all three intracellular options: ATAC complex (A) is a nuclear chromatin-remodeling complex, spindle (D) is a cytoplasmic microtubule structure during mitosis, and aggresome (B) is a cytoplasmic inclusion body of misfolded proteins. A protein with a cleavable signal peptide is routed to the secretory pathway and ends up extracellular or membrane-associated, never in these intracellular compartments. Additionally, the mature peptide (residues ~21–70) is amphipathic with alternating hydrophobic (W, F, L, I) and charged (K, R, D, E) residues, a hallmark of antimicrobial peptides that interact with and disrupt target membranes. Together, the signal peptide and amphipathic mature domain strongly and specifically point to 'membrane' (C) over the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal peptide alone provides a decisive, transferable inference: proteins with N-terminal signal peptides are secreted or membrane-associated and cannot reside in the ATAC complex, spindle, or aggresome. The amphipathic character of the mature peptide further supports membrane targeting. No knowledge of this specific protein's database record is needed; the reasoning relies on general signal-peptide biology and antimicrobial-peptide family characteristics learned from many other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only 'membrane' is consistent with a protein bearing a cleavable signal peptide and an amphipathic mature domain. The protein is also annotated as 'Secreted' / 'extracellular region,' but that option is not offered, so no ambiguity arises among the given alternatives. The three distractors (ATAC complex, aggresome, spindle) are all strictly intracellular structures incompatible with a secreted peptide.


### Important caveats

- The UniProt subcellular-location annotation uses ECO:0000305 (author statement from a single transcriptome paper, PubMed:25659089), which is an inference from the venom-gland mRNA source rather than direct subcellular fractionation or imaging.
- The GO 'membrane' annotation (GO:0044218, other organism cell membrane) is IEA:UniProtKB-KW, i.e., a keyword-derived electronic annotation, not an independent experimental localization.
- The protein is also annotated as 'Secreted' / extracellular region (GO:0005576, IEA). 'Membrane' and 'extracellular' are not mutually exclusive for an antimicrobial peptide that is secreted and then binds target-cell membranes, but 'extracellular region' was not offered as a choice.
- The reviewer-only evidence identifies this as P0DRH3 (Antimicrobial peptide VpCT1, Mesomexovis punctatus); this identity was not provided to the evaluated model and is not needed for the reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence MKNQFAVLLVALVLLQLFSQS is a canonical signal peptide: ~20 hydrophobic residues at the extreme N-terminus, characteristic of proteins entering the ER/Golgi secretory pathway. This single feature immediately excludes all three intracellular options: ATAC complex (A) is a nuclear chromatin-remodeling complex, spindle (D) is a cytoplasmic microtubule structure during mitosis, and aggresome (B) is a cytoplasmic inclusion body of misfolded proteins. A protein with a cleavable signal peptide is routed to the secretory pathway and ends up extracellular or membrane-associated, never in these intracellular compartments. Additionally, the mature peptide (residues ~21–70) is amphipathic with alternating hydrophobic (W, F, L, I) and charged (K, R, D, E) residues, a hallmark of antimicrobial peptides that interact with and disrupt target membranes. Together, the signal peptide and amphipathic mature domain strongly and specifically point to 'membrane' (C) over the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide alone provides a decisive, transferable inference: proteins with N-terminal signal peptides are secreted or membrane-associated and cannot reside in the ATAC complex, spindle, or aggresome. The amphipathic character of the mature peptide further supports membrane targeting. No knowledge of this specific protein's database record is needed; the reasoning relies on general signal-peptide biology and antimicrobial-peptide family characteristics learned from many other proteins."
  },
  "case_id": "GO_cellular_component_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DRH3 annotates this protein's subcellular location as 'Secreted' and 'Target cell membrane' (ECO:0000305, PubMed:25659089). The GO annotation includes GO:0044218 (other organism cell membrane), which is a child of GO:0016020 (membrane). Among the four offered choices, 'membrane' (GO:0016020) is directly supported by the 'Target cell membrane' annotation and the GO:0044218 cross-reference. The evidence codes are ECO:0000305 (author statement based on a single publication) and IEA (inferred from electronic annotation), so this is annotation-level support rather than direct experimental localization, but it is consistent and supported."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation uses ECO:0000305 (author statement from a single transcriptome paper, PubMed:25659089), which is an inference from the venom-gland mRNA source rather than direct subcellular fractionation or imaging.",
    "The GO 'membrane' annotation (GO:0044218, other organism cell membrane) is IEA:UniProtKB-KW, i.e., a keyword-derived electronic annotation, not an independent experimental localization.",
    "The protein is also annotated as 'Secreted' / extracellular region (GO:0005576, IEA). 'Membrane' and 'extracellular' are not mutually exclusive for an antimicrobial peptide that is secreted and then binds target-cell membranes, but 'extracellular region' was not offered as a choice.",
    "The reviewer-only evidence identifies this as P0DRH3 (Antimicrobial peptide VpCT1, Mesomexovis punctatus); this identity was not provided to the evaluated model and is not needed for the reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only 'membrane' is consistent with a protein bearing a cleavable signal peptide and an amphipathic mature domain. The protein is also annotated as 'Secreted' / 'extracellular region,' but that option is not offered, so no ambiguity arises among the given alternatives. The three distractors (ATAC complex, aggresome, spindle) are all strictly intracellular structures incompatible with a secreted peptide."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DRH3 annotates this protein's subcellular location as 'Secreted' and 'Target cell membrane' (ECO:0000305, PubMed:25659089). The GO annotation includes GO:0044218 (other organism cell membrane), which is a child of GO:0016020 (membrane). Among the four offered choices, 'membrane' (GO:0016020) is directly supported by the 'Target cell membrane' annotation and the GO:0044218 cross-reference. The evidence codes are ECO:0000305 (author statement based on a single publication) and IEA (inferred from electronic annotation), so this is annotation-level support rather than direct experimental localization, but it is consistent and supported.",
    "evidence_ids": ["C5", "C6", "H4", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence MKNQFAVLLVALVLLQLFSQS is a canonical signal peptide: ~20 hydrophobic residues at the extreme N-terminus, characteristic of proteins entering the ER/Golgi secretory pathway. This single feature immediately excludes all three intracellular options: ATAC complex (A) is a nuclear chromatin-remodeling complex, spindle (D) is a cytoplasmic microtubule structure during mitosis, and aggresome (B) is a cytoplasmic inclusion body of misfolded proteins. A protein with a cleavable signal peptide is routed to the secretory pathway and ends up extracellular or membrane-associated, never in these intracellular compartments. Additionally, the mature peptide (residues ~21–70) is amphipathic with alternating hydrophobic (W, F, L, I) and charged (K, R, D, E) residues, a hallmark of antimicrobial peptides that interact with and disrupt target membranes. Together, the signal peptide and amphipathic mature domain strongly and specifically point to 'membrane' (C) over the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide alone provides a decisive, transferable inference: proteins with N-terminal signal peptides are secreted or membrane-associated and cannot reside in the ATAC complex, spindle, or aggresome. The amphipathic character of the mature peptide further supports membrane targeting. No knowledge of this specific protein's database record is needed; the reasoning relies on general signal-peptide biology and antimicrobial-peptide family characteristics learned from many other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only 'membrane' is consistent with a protein bearing a cleavable signal peptide and an amphipathic mature domain. The protein is also annotated as 'Secreted' / 'extracellular region,' but that option is not offered, so no ambiguity arises among the given alternatives. The three distractors (ATAC complex, aggresome, spindle) are all strictly intracellular structures incompatible with a secreted peptide."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation uses ECO:0000305 (author statement from a single transcriptome paper, PubMed:25659089), which is an inference from the venom-gland mRNA source rather than direct subcellular fractionation or imaging.",
    "The GO 'membrane' annotation (GO:0044218, other organism cell membrane) is IEA:UniProtKB-KW, i.e., a keyword-derived electronic annotation, not an independent experimental localization.",
    "The protein is also annotated as 'Secreted' / extracellular region (GO:0005576, IEA). 'Membrane' and 'extracellular' are not mutually exclusive for an antimicrobial peptide that is secreted and then binds target-cell membranes, but 'extracellular region' was not offered as a choice.",
    "The reviewer-only evidence identifies this as P0DRH3 (Antimicrobial peptide VpCT1, Mesomexovis punctatus); this identity was not provided to the evaluated model and is not needed for the reasoning."
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
  "benchmark_sequence_length": 70,
  "benchmark_sequence_sha256": "e15f84c34405c3f85caa57570ea9f16a0c3523e8a7ef26e22cf25e063f692fba",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ab8a44c22785bc63fea0f6c0194c712c58188fcce571c235f3891d6f69005c56",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 70,
  "current_source_sequence_sha256": "e15f84c34405c3f85caa57570ea9f16a0c3523e8a7ef26e22cf25e063f692fba",
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
  "requested_accession": "P0DRH3",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "f19fddaf53179d74f41dad45e23f9d00464335ce3cf0a21eef48979ff0e94aa4",
  "selected_historical_source_sequence_length": 70,
  "selected_historical_source_sequence_sha256": "e15f84c34405c3f85caa57570ea9f16a0c3523e8a7ef26e22cf25e063f692fba",
  "selected_historical_version": {
    "accession": "P0DRH3",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NDBT1_MESPU",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DRH3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:14.792819+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab8a44c22785bc63fea0f6c0194c712c58188fcce571c235f3891d6f69005c56",
  "url": "https://rest.uniprot.org/uniprotkb/P0DRH3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:14.792819+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab8a44c22785bc63fea0f6c0194c712c58188fcce571c235f3891d6f69005c56",
  "url": "https://rest.uniprot.org/uniprotkb/P0DRH3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Scorpion\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Chelicerata\",\"Arachnida\",\"Scorpiones\",\"Iurida\",\"Chactoidea\",\"Vaejovidae\",\"Mesomexovis\"],\"scientificName\":\"Mesomexovis punctatus\",\"synonyms\":[\"Vaejovis punctatus\"],\"taxonId\":1532993}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:14.792819+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab8a44c22785bc63fea0f6c0194c712c58188fcce571c235f3891d6f69005c56",
  "url": "https://rest.uniprot.org/uniprotkb/P0DRH3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33862164\",\"source\":\"PubMed\"}],\"value\":\"Antimicrobial peptide VpCT1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:14.792819+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab8a44c22785bc63fea0f6c0194c712c58188fcce571c235f3891d6f69005c56",
  "url": "https://rest.uniprot.org/uniprotkb/P0DRH3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"25659089\",\"source\":\"PubMed\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"25659089\",\"source\":\"PubMed\"}],\"id\":\"SL-0451\",\"value\":\"Target cell membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:14.792819+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab8a44c22785bc63fea0f6c0194c712c58188fcce571c235f3891d6f69005c56",
  "url": "https://rest.uniprot.org/uniprotkb/P0DRH3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-01T06:25:14.792819+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab8a44c22785bc63fea0f6c0194c712c58188fcce571c235f3891d6f69005c56",
  "url": "https://rest.uniprot.org/uniprotkb/P0DRH3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Quintero-Hernandez V.\",\"Ramirez-Carreto S.\",\"Romero-Gutierrez M.T.\",\"Valdez-Velazquez L.L.\",\"Becerril B.\",\"Possani L.D.\",\"Ortiz E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25659089\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0117188\"}],\"citationType\":\"journal article\",\"firstPage\":\"E0117188\",\"id\":\"25659089\",\"journal\":\"PLoS ONE\",\"lastPage\":\"E0117188\",\"publicationDate\":\"2015\",\"title\":\"Transcriptome analysis of scorpion species belonging to the Vaejovis genus.\",\"volume\":\"10\"},\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Venom gland\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"PROBABLE AMIDATION AT LEU-36\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:14.792819+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab8a44c22785bc63fea0f6c0194c712c58188fcce571c235f3891d6f69005c56",
  "url": "https://rest.uniprot.org/uniprotkb/P0DRH3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DRH3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Jimenez-Vargas J.M.\",\"Ramirez-Carreto S.\",\"Corzo G.\",\"Possani L.D.\",\"Becerril B.\",\"Ortiz E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33862164\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.peptides.2021.170553\"}],\"citationType\":\"journal article\",\"firstPage\":\"170553\",\"id\":\"33862164\",\"journal\":\"Peptides\",\"lastPage\":\"170553\",\"publicationDate\":\"2021\",\"title\":\"Structural and functional characterization of NDBP-4 family antimicrobial peptides from the scorpion Mesomexovis variegatus.\",\"volume\":\"141\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SYNTHESIS OF 24-36\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:14.792819+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab8a44c22785bc63fea0f6c0194c712c58188fcce571c235f3891d6f69005c56",
  "url": "https://rest.uniprot.org/uniprotkb/P0DRH3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   NDBT1_MESPU             Reviewed;          70 AA.\nAC   P0DRH3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Antimicrobial peptide VpCT1 {ECO:0000303|PubMed:33862164};\nDE   Flags: Precursor;\nOS   Mesomexovis punctatus (Scorpion) (Vaejovis punctatus).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Chelicerata; Arachnida;\nOC   Scorpiones; Iurida; Chactoidea; Vaejovidae; Mesomexovis.\nOX   NCBI_TaxID=1532993;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:18.944778+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f19fddaf53179d74f41dad45e23f9d00464335ce3cf0a21eef48979ff0e94aa4",
  "url": "https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], AND PROBABLE AMIDATION AT LEU-36.\nRC   TISSUE=Venom gland;\nRX   PubMed=25659089; DOI=10.1371/journal.pone.0117188;\nRA   Quintero-Hernandez V., Ramirez-Carreto S., Romero-Gutierrez M.T.,\nRA   Valdez-Velazquez L.L., Becerril B., Possani L.D., Ortiz E.;\nRT   \"Transcriptome analysis of scorpion species belonging to the Vaejovis\nRT   genus.\";\nRL   PLoS ONE 10:E0117188-E0117188(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:18.944778+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 12-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f19fddaf53179d74f41dad45e23f9d00464335ce3cf0a21eef48979ff0e94aa4",
  "url": "https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND SYNTHESIS OF 24-36.\nRX   PubMed=33862164; DOI=10.1016/j.peptides.2021.170553;\nRA   Jimenez-Vargas J.M., Ramirez-Carreto S., Corzo G., Possani L.D.,\nRA   Becerril B., Ortiz E.;\nRT   \"Structural and functional characterization of NDBP-4 family antimicrobial\nRT   peptides from the scorpion Mesomexovis variegatus.\";\nRL   Peptides 141:170553-170553(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:18.944778+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f19fddaf53179d74f41dad45e23f9d00464335ce3cf0a21eef48979ff0e94aa4",
  "url": "https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:25659089}. Target\nCC       cell membrane {ECO:0000305|PubMed:25659089}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:18.944778+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f19fddaf53179d74f41dad45e23f9d00464335ce3cf0a21eef48979ff0e94aa4",
  "url": "https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:18.944778+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f19fddaf53179d74f41dad45e23f9d00464335ce3cf0a21eef48979ff0e94aa4",
  "url": "https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0044218; C:other organism cell membrane; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:18.944778+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f19fddaf53179d74f41dad45e23f9d00464335ce3cf0a21eef48979ff0e94aa4",
  "url": "https://rest.uniprot.org/unisave/P0DRH3?format=txt&versions=3"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005819\nname: spindle\nnamespace: cellular_component\ndef: \"The array of microtubules and associated molecules that forms between opposite poles of a eukaryotic cell during mitosis or meiosis and serves to move the duplicated chromosomes apart.\" [ISBN:0198547684]\nxref: Wikipedia:Spindle_apparatus\nis_a: GO:0043232 ! intracellular membraneless organelle\nrelationship: part_of GO:0015630 ! microtubule cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005819",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59855-59863",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0016020\nname: membrane\nnamespace: cellular_component\nalt_id: GO:0016021\nalt_id: GO:0098589\nalt_id: GO:0098805\ndef: \"A lipid bilayer along with all the proteins and protein complexes embedded in it and attached to it.\" [GOC:dos, GOC:mah, ISBN:0815316194]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_yeast\nsynonym: \"integral component of membrane\" NARROW []\nsynonym: \"integral to membrane\" NARROW []\nsynonym: \"membrane region\" NARROW []\nsynonym: \"region of membrane\" NARROW []\nsynonym: \"transmembrane\" RELATED [GOC:mah]\nsynonym: \"whole membrane\" NARROW []\nxref: Wikipedia:Biological_membrane\nxref: Wikipedia:Transmembrane_protein\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016020",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 122626-122650",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0016235\nname: aggresome\nnamespace: cellular_component\ndef: \"An inclusion body formed by dynein-dependent retrograde transport of an aggregated protein on microtubules.\" [PMID:11121744]\nxref: Wikipedia:Aggresome\nis_a: GO:0016234 ! inclusion body\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016235",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 124908-124915",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0140672\nname: ATAC complex\nnamespace: cellular_component\ndef: \"A chromatin remodeling complex that regulates transcription via acetylation primarily of nucleosomal histones H3 and possibly H4. Shares the histone acetylation (HAT) module of GCN5/PCAF-ADA2-ADA3-SGF29 (or orthologs) with the related SAGA complex (GO:0000124). Contains HAT subunits GCN5 or PCAF in a mutually exclusive manner. In addition to the HAT module contains DR1/NC2B, KAT14, MBIP, WDR5, YEATS2 and ZZZ3 or orthologs. Also regulates the activity of non-histone targets and orchestrates mitotic progression by regulating Cyclin A degradation through acetylation.\" [GOC:bhm, PMID:19936620, PMID:20562830, PMID:28966424]\nsynonym: \"Ada two A containing complex\" EXACT []\nsynonym: \"Ada Two-A containing complex\" EXACT []\nsynonym: \"Ada-Two-A-containing complex\" EXACT []\nsynonym: \"ADA2A-containing complex\" EXACT []\nsynonym: \"G-ATAC complex\" EXACT []\nsynonym: \"KAT2A-containing ATAC complex\" EXACT []\nsynonym: \"KAT2B-containing ATAC complex\" EXACT []\nis_a: GO:0070461 ! SAGA-type complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140672",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 442360-442373",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 157. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
