# GO_cellular_component_0135

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0135.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — nematocyst

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKPIFIVALLFSTCLVNAKPSIDDAEMKREPKPNIINPPCIGCYYQVGNECVYDKFKCGAVRKREPKPNIINPPCIGCYYQVGNECVYDKFKCGAV

[Multiple Choices]
A. endosome membrane
B. microtubule cytoskeleton
C. NF-kappaB p50/p65 complex
D. nematocyst
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

> The matched-sequence UniProt records annotate the protein as secreted and localized to a nematocyst, and the GO annotation also assigns nematocyst. This supports D, although the localization annotation is not itself direct experimental localization evidence; the cited study supports toxin identity and activity.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a secretion signal, and the short, cysteine-rich repeated peptide region is compatible with a secreted toxin peptide. Transferable knowledge that cnidarian nematocysts store and deliver toxins makes D a meaningful fit; the other choices describe an endosomal membrane, cytoskeletal structure, or transcription-factor complex and are poorly matched to a secreted toxin-like precursor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence features and general biology of toxin storage in nematocysts provide a credible probabilistic distinction among these alternatives without requiring the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, nematocyst is the clear fit for a likely secreted toxin-like peptide; the other options are not comparably supported by the sequence.


### Important caveats

- The sequence alone does not establish the organism or directly demonstrate localization to a nematocyst.
- The reviewer-only database localization annotation is curated, and its GO assignment is computationally inferred; the cited toxin evidence does not by itself prove the subcellular location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secretion signal, and the short, cysteine-rich repeated peptide region is compatible with a secreted toxin peptide. Transferable knowledge that cnidarian nematocysts store and deliver toxins makes D a meaningful fit; the other choices describe an endosomal membrane, cytoskeletal structure, or transcription-factor complex and are poorly matched to a secreted toxin-like precursor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and general biology of toxin storage in nematocysts provide a credible probabilistic distinction among these alternatives without requiring the exact protein's recorded annotation."
  },
  "case_id": "GO_cellular_component_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt records annotate the protein as secreted and localized to a nematocyst, and the GO annotation also assigns nematocyst. This supports D, although the localization annotation is not itself direct experimental localization evidence; the cited study supports toxin identity and activity."
  },
  "important_caveats": [
    "The sequence alone does not establish the organism or directly demonstrate localization to a nematocyst.",
    "The reviewer-only database localization annotation is curated, and its GO assignment is computationally inferred; the cited toxin evidence does not by itself prove the subcellular location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, nematocyst is the clear fit for a likely secreted toxin-like peptide; the other options are not comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt records annotate the protein as secreted and localized to a nematocyst, and the GO annotation also assigns nematocyst. This supports D, although the localization annotation is not itself direct experimental localization evidence; the cited study supports toxin identity and activity.",
    "evidence_ids": ["C5", "C7", "H3", "H5", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secretion signal, and the short, cysteine-rich repeated peptide region is compatible with a secreted toxin peptide. Transferable knowledge that cnidarian nematocysts store and deliver toxins makes D a meaningful fit; the other choices describe an endosomal membrane, cytoskeletal structure, or transcription-factor complex and are poorly matched to a secreted toxin-like precursor.",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and general biology of toxin storage in nematocysts provide a credible probabilistic distinction among these alternatives without requiring the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, nematocyst is the clear fit for a likely secreted toxin-like peptide; the other options are not comparably supported by the sequence."
  },
  "important_caveats": [
    "The sequence alone does not establish the organism or directly demonstrate localization to a nematocyst.",
    "The reviewer-only database localization annotation is curated, and its GO assignment is computationally inferred; the cited toxin evidence does not by itself prove the subcellular location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0P0UTQ7) annotates the subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, inferred from biological aspect of ancestor), and carries GO:0042151 (C:nematocyst). The sequence features—a cleavable N-terminal signal peptide (MKPIFIVALLFSTCLVNAK), small mature size (~78 aa), tandem repeat, and multiple cysteines forming a disulfide-rich knottin-like motif—are consistent with a cnidarian peptide toxin stored in nematocysts. The annotation evidence code is curatorial inference rather than direct experimental localization, but the sequence is highly consistent with the claim.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal signal peptide (hydrophobic core IFIVALLFSTCLV followed by a NA↓K cleavage site), indicating the protein is secreted. The mature portion is a small (~78 aa) cysteine-rich peptide with a tandem repeat motif and multiple disulfide-forming cysteines (CIGCYYQVGNECVYDKFKCGAV repeated twice), characteristic of small peptide toxins (e.g., knottin/ICK-type inhibitors). Crucially, there is NO transmembrane domain after the signal peptide, ruling out membrane-protein localization. Among the four choices: (B) microtubule cytoskeleton and (C) NF-kappaB p50/p65 complex are intracellular/cytoplasmic structures incompatible with a secreted small peptide; (A) endosome membrane requires a transmembrane anchor, which is absent. Only (D) nematocyst—a cnidarian stinging organelle that stores and delivers peptide toxins—is consistent with a small, secreted, disulfide-rich toxin. The tandem repeat and cysteine spacing pattern resembles known cnidarian toxins (e.g., stichodactylins, actinoporins), providing family-level transferable knowledge that distinguishes D from the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can reason from the signal peptide (→secreted, not intracellular), absence of transmembrane domain (→not a membrane protein), small cysteine-rich toxin-like architecture (→peptide toxin), and the nature of the four offered choices (three clearly intracellular/membrane-anchored, one a toxin-storage organelle) to select D without needing to look up this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (endosome membrane, microtubule cytoskeleton, NF-kappaB p50/p65 complex) are all intracellular structures or complexes that are clearly incompatible with a small secreted peptide toxin lacking transmembrane domains. Only nematocyst is a secreted toxin-storage organelle. No ambiguity among the offered choices.


### Important caveats

- The UniProt subcellular location annotation carries ECO:0000305 (inferred from biological aspect of ancestor), a curatorial inference rather than direct experimental localization of this specific peptide within the nematocyst.
- The GO:0042151 annotation is IEA (inferred from electronic annotation) derived from UniProtKB-SubCell, so it is not independently experimentally verified.
- The model does not receive organism identity from the input; however, the sequence features (small disulfide-rich peptide with signal peptide and tandem repeat) are sufficient to infer a toxin-like secreted peptide, and the choice set makes nematocyst the only viable compartment.
- The tandem repeat of the mature toxin domain is unusual and may reflect a specific toxin family feature, but the overall secreted-toxin logic independently supports the answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (hydrophobic core IFIVALLFSTCLV followed by a NA↓K cleavage site), indicating the protein is secreted. The mature portion is a small (~78 aa) cysteine-rich peptide with a tandem repeat motif and multiple disulfide-forming cysteines (CIGCYYQVGNECVYDKFKCGAV repeated twice), characteristic of small peptide toxins (e.g., knottin/ICK-type inhibitors). Crucially, there is NO transmembrane domain after the signal peptide, ruling out membrane-protein localization. Among the four choices: (B) microtubule cytoskeleton and (C) NF-kappaB p50/p65 complex are intracellular/cytoplasmic structures incompatible with a secreted small peptide; (A) endosome membrane requires a transmembrane anchor, which is absent. Only (D) nematocyst—a cnidarian stinging organelle that stores and delivers peptide toxins—is consistent with a small, secreted, disulfide-rich toxin. The tandem repeat and cysteine spacing pattern resembles known cnidarian toxins (e.g., stichodactylins, actinoporins), providing family-level transferable knowledge that distinguishes D from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can reason from the signal peptide (→secreted, not intracellular), absence of transmembrane domain (→not a membrane protein), small cysteine-rich toxin-like architecture (→peptide toxin), and the nature of the four offered choices (three clearly intracellular/membrane-anchored, one a toxin-storage organelle) to select D without needing to look up this exact protein's database entry."
  },
  "case_id": "GO_cellular_component_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0P0UTQ7) annotates the subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, inferred from biological aspect of ancestor), and carries GO:0042151 (C:nematocyst). The sequence features—a cleavable N-terminal signal peptide (MKPIFIVALLFSTCLVNAK), small mature size (~78 aa), tandem repeat, and multiple cysteines forming a disulfide-rich knottin-like motif—are consistent with a cnidarian peptide toxin stored in nematocysts. The annotation evidence code is curatorial inference rather than direct experimental localization, but the sequence is highly consistent with the claim."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation carries ECO:0000305 (inferred from biological aspect of ancestor), a curatorial inference rather than direct experimental localization of this specific peptide within the nematocyst.",
    "The GO:0042151 annotation is IEA (inferred from electronic annotation) derived from UniProtKB-SubCell, so it is not independently experimentally verified.",
    "The model does not receive organism identity from the input; however, the sequence features (small disulfide-rich peptide with signal peptide and tandem repeat) are sufficient to infer a toxin-like secreted peptide, and the choice set makes nematocyst the only viable compartment.",
    "The tandem repeat of the mature toxin domain is unusual and may reflect a specific toxin family feature, but the overall secreted-toxin logic independently supports the answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (endosome membrane, microtubule cytoskeleton, NF-kappaB p50/p65 complex) are all intracellular structures or complexes that are clearly incompatible with a small secreted peptide toxin lacking transmembrane domains. Only nematocyst is a secreted toxin-storage organelle. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0P0UTQ7) annotates the subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, inferred from biological aspect of ancestor), and carries GO:0042151 (C:nematocyst). The sequence features—a cleavable N-terminal signal peptide (MKPIFIVALLFSTCLVNAK), small mature size (~78 aa), tandem repeat, and multiple cysteines forming a disulfide-rich knottin-like motif—are consistent with a cnidarian peptide toxin stored in nematocysts. The annotation evidence code is curatorial inference rather than direct experimental localization, but the sequence is highly consistent with the claim.",
    "evidence_ids": ["C5", "C7", "H3", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (hydrophobic core IFIVALLFSTCLV followed by a NA↓K cleavage site), indicating the protein is secreted. The mature portion is a small (~78 aa) cysteine-rich peptide with a tandem repeat motif and multiple disulfide-forming cysteines (CIGCYYQVGNECVYDKFKCGAV repeated twice), characteristic of small peptide toxins (e.g., knottin/ICK-type inhibitors). Crucially, there is NO transmembrane domain after the signal peptide, ruling out membrane-protein localization. Among the four choices: (B) microtubule cytoskeleton and (C) NF-kappaB p50/p65 complex are intracellular/cytoplasmic structures incompatible with a secreted small peptide; (A) endosome membrane requires a transmembrane anchor, which is absent. Only (D) nematocyst—a cnidarian stinging organelle that stores and delivers peptide toxins—is consistent with a small, secreted, disulfide-rich toxin. The tandem repeat and cysteine spacing pattern resembles known cnidarian toxins (e.g., stichodactylins, actinoporins), providing family-level transferable knowledge that distinguishes D from the other options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can reason from the signal peptide (→secreted, not intracellular), absence of transmembrane domain (→not a membrane protein), small cysteine-rich toxin-like architecture (→peptide toxin), and the nature of the four offered choices (three clearly intracellular/membrane-anchored, one a toxin-storage organelle) to select D without needing to look up this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (endosome membrane, microtubule cytoskeleton, NF-kappaB p50/p65 complex) are all intracellular structures or complexes that are clearly incompatible with a small secreted peptide toxin lacking transmembrane domains. Only nematocyst is a secreted toxin-storage organelle. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation carries ECO:0000305 (inferred from biological aspect of ancestor), a curatorial inference rather than direct experimental localization of this specific peptide within the nematocyst.",
    "The GO:0042151 annotation is IEA (inferred from electronic annotation) derived from UniProtKB-SubCell, so it is not independently experimentally verified.",
    "The model does not receive organism identity from the input; however, the sequence features (small disulfide-rich peptide with signal peptide and tandem repeat) are sufficient to infer a toxin-like secreted peptide, and the choice set makes nematocyst the only viable compartment.",
    "The tandem repeat of the mature toxin domain is unusual and may reflect a specific toxin family feature, but the overall secreted-toxin logic independently supports the answer."
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
  "benchmark_sequence_length": 96,
  "benchmark_sequence_sha256": "46c2b3217737b877b04f7f087c6055144c1cba227728e230a747a825860d9ee0",
  "current_entry_audit": {
    "entryVersion": 9,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-01-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 96,
  "current_source_sequence_sha256": "46c2b3217737b877b04f7f087c6055144c1cba227728e230a747a825860d9ee0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 8,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0P0UTQ7",
  "selected_historical_entry_version": 8,
  "selected_historical_record_sha256": "7b38529a8265c44e6300a8d5f7dec9b2e6c0d79bfeff7fbb32de9c7c77031881",
  "selected_historical_source_sequence_length": 96,
  "selected_historical_source_sequence_sha256": "46c2b3217737b877b04f7f087c6055144c1cba227728e230a747a825860d9ee0",
  "selected_historical_version": {
    "accession": "A0A0P0UTQ7",
    "database": "Swiss-Prot",
    "entryVersion": 8,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "BBH2B_HETAU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0P0UTQ7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:18.589867+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":9,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-01-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:18.589867+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Banded sea anemone\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Cnidaria\",\"Anthozoa\",\"Hexacorallia\",\"Actiniaria\",\"Stichodactylidae\",\"Heteractis\"],\"scientificName\":\"Heteractis aurora\",\"synonyms\":[\"Actinia aurora\"],\"taxonId\":478399}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:18.589867+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39530114\",\"source\":\"PubMed\"}],\"value\":\"Hau III\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39530114\",\"source\":\"PubMed\"}],\"value\":\"U-stichotoxin-Hau2b\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39530114\",\"source\":\"PubMed\"}],\"value\":\"U-SHTX-Hau2b\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:18.589867+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0177\",\"value\":\"Nematocyst\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:18.589867+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:24:18.589867+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0042151\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nematocyst\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:24:18.589867+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Homma T.\",\"Ishida M.\",\"Nagashima Y.\",\"Shiomi K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39530114\"},{\"database\":\"DOI\",\"id\":\"10.1590/1678-9199-jvatitd-2024-0019\"}],\"citationType\":\"journal article\",\"firstPage\":\"e20240019\",\"id\":\"39530114\",\"journal\":\"J. Venom. Anim. Toxins Incl. Trop. Dis.\",\"lastPage\":\"e20240019\",\"publicationDate\":\"2024\",\"title\":\"Isolation and cDNA cloning of four peptide toxins from the sea anemone Heteractis aurora.\",\"volume\":\"30\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAS68534.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"PROTEIN SEQUENCE OF 34-58 AND 69-93\",\"MASS SPECTROMETRY\",\"TOXIC DOSE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:24:18.589867+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H1",
  "excerpt": "ID   BBH2B_HETAU             Reviewed;          96 AA.\nAC   A0A0P0UTQ7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-JAN-2016, sequence version 1.\nDT   28-JAN-2026, entry version 8.\nDE   RecName: Full=U-stichotoxin-Hau2b {ECO:0000303|PubMed:39530114};\nDE            Short=U-SHTX-Hau2b {ECO:0000303|PubMed:39530114};\nDE   AltName: Full=Hau III {ECO:0000303|PubMed:39530114};\nDE   Flags: Precursor;\nGN   Name=HAUTX3 {ECO:0000312|EMBL:BAS68534.1};\nOS   Heteractis aurora (Banded sea anemone) (Actinia aurora).\nOC   Eukaryota; Metazoa; Cnidaria; Anthozoa; Hexacorallia; Actiniaria;\nOC   Stichodactylidae; Heteractis.\nOX   NCBI_TaxID=478399;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:21.319533+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7b38529a8265c44e6300a8d5f7dec9b2e6c0d79bfeff7fbb32de9c7c77031881",
  "url": "https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAS68534.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], PROTEIN SEQUENCE OF 34-58 AND 69-93, MASS\nRP   SPECTROMETRY, AND TOXIC DOSE.\nRX   PubMed=39530114; DOI=10.1590/1678-9199-jvatitd-2024-0019;\nRA   Homma T., Ishida M., Nagashima Y., Shiomi K.;\nRT   \"Isolation and cDNA cloning of four peptide toxins from the sea anemone\nRT   Heteractis aurora.\";\nRL   J. Venom. Anim. Toxins Incl. Trop. Dis. 30:e20240019-e20240019(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:21.319533+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7b38529a8265c44e6300a8d5f7dec9b2e6c0d79bfeff7fbb32de9c7c77031881",
  "url": "https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305}. Nematocyst {ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:21.319533+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7b38529a8265c44e6300a8d5f7dec9b2e6c0d79bfeff7fbb32de9c7c77031881",
  "url": "https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:21.319533+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7b38529a8265c44e6300a8d5f7dec9b2e6c0d79bfeff7fbb32de9c7c77031881",
  "url": "https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0042151; C:nematocyst; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:21.319533+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7b38529a8265c44e6300a8d5f7dec9b2e6c0d79bfeff7fbb32de9c7c77031881",
  "url": "https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0010008\nname: endosome membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding an endosome.\" [GOC:mah]\nsynonym: \"endosomal membrane\" EXACT [NIF_Subcellular:sao978443756]\nxref: NIF_Subcellular:sao978443756\nis_a: GO:0030659 ! cytoplasmic vesicle membrane\nis_a: GO:0098588 ! bounding membrane of organelle\nrelationship: part_of GO:0005768 ! endosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0010008",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 101976-101986",
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
  "excerpt": "[Term]\nid: GO:0015630\nname: microtubule cytoskeleton\nnamespace: cellular_component\ndef: \"The part of the cytoskeleton (the internal framework of a cell) composed of microtubules and associated proteins.\" [GOC:jl, ISBN:0395825172]\nis_a: GO:0005856 ! cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015630",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 119409-119415",
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
  "excerpt": "[Term]\nid: GO:0035525\nname: NF-kappaB p50/p65 complex\nnamespace: cellular_component\ndef: \"A heterodimer of NF-kappa B p50 and p65 subunits.\" [GO:add, PMID:20393192, PMID:9299584]\ncomment: Note that the p50 subunit is encoded by NFKB1 gene in human and the p65 subunit is encoded by the RELA gene in human. Similar nomenclature is used in other vertebrate species. The p50 subunit has a precursor form p105 in some publications.\nsynonym: \"NF-kappa B1/p65 complex\" EXACT [PMID:9299584]\nsynonym: \"NF-kappa B1/RelA complex\" EXACT [PMID:9299584]\nsynonym: \"NF-kappa p105/p65 complex\" RELATED [PMID:9299584]\nsynonym: \"NF-kappa p105/RelA complex\" RELATED [PMID:9299584]\nsynonym: \"NF-kappa p50/RelA complex\" EXACT [PMID:9299584]\nis_a: GO:0071159 ! NF-kappaB complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035525",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 218851-218863",
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
  "excerpt": "[Term]\nid: GO:0042151\nname: nematocyst\nnamespace: cellular_component\ndef: \"An organelle found in cnidoblast (nematoblast) cells. When matured, these stinging organelles store toxins and can deliver them when the cnidocil (a short extension of the cnidocyst) is stimulated by a prey or another stimulus.\" [DOI:10.1139/z02-135, GOC:jl]\nsynonym: \"cnidocyst\" EXACT []\nxref: Wikipedia:Cnidocyte\nis_a: GO:0043232 ! intracellular membraneless organelle\nrelationship: part_of GO:0005938 ! cell cortex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042151",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 234754-234763",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 135. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
