# EC_number_0007

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0007.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 4.4.1.11

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIAVNSRNSLNADMTSLHPETLMVHGGMKGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHTLKDGDSAVYQRLWQPGVARFETALAGLEHAEEAVAFATGMAAMTAALLAAVSAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEADIASAIQDDTGLVIVETPANPSLDLVDLDSVVSAAGNVPVLVDNTFCTPVLQQPISHGAALVLHSATKYLGGHGDAMGGIIATNADWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLDAHPAISVVHYPGLKGQDPRGLLGRQMSGGGAMIAMELAGGFDAARSFVEHCNLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLADDLIAALDASRAAA

[Multiple Choices]
A. 4.3.1.24
B. 1.6.5.2
C. 3.2.2.5
D. 4.4.1.11
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

> The sequence-matched archived UniProt record assigns EC 4.4.1.11 to L-methionine gamma-lyase and cites experimental evidence. Its catalytic-activity annotation gives the corresponding L-methionine reaction. The record also lists EC 4.4.1.2 for homocysteine desulfhydrase activity, but that is not one of the choices.

Citations as saved: [H1](#evidence-h1), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a roughly 400-residue PLP-dependent amino-acid lyase, supporting a gamma-lyase-family inference. That meaningfully favors D over the oxidoreductase and nucleoside-hydrolase choices; the offered 4.3.1.24 alternative is an ammonia-lyase class, whereas the sequence's family-level features support a PLP-dependent sulfur-amino-acid lyase instead. This is a transferable family inference, not certainty about the exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family and cofactor-related sequence patterns provide a credible basis for distinguishing the methionine gamma-lyase choice from these alternatives, although sequence-only inference may not establish the exact EC annotation with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source record reports another catalytic activity, EC 4.4.1.2, but that EC is not offered; among the listed choices, only D matches the supported methionine gamma-lyase activity.


### Important caveats

- The source record is sequence-matched and its EC annotations cite experimental evidence, but the primary papers were not independently reviewed here.
- The answerability argument supports a family-level inference; it does not establish exact catalytic specificity from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a roughly 400-residue PLP-dependent amino-acid lyase, supporting a gamma-lyase-family inference. That meaningfully favors D over the oxidoreductase and nucleoside-hydrolase choices; the offered 4.3.1.24 alternative is an ammonia-lyase class, whereas the sequence's family-level features support a PLP-dependent sulfur-amino-acid lyase instead. This is a transferable family inference, not certainty about the exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family and cofactor-related sequence patterns provide a credible basis for distinguishing the methionine gamma-lyase choice from these alternatives, although sequence-only inference may not establish the exact EC annotation with certainty."
  },
  "case_id": "EC_number_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt record assigns EC 4.4.1.11 to L-methionine gamma-lyase and cites experimental evidence. Its catalytic-activity annotation gives the corresponding L-methionine reaction. The record also lists EC 4.4.1.2 for homocysteine desulfhydrase activity, but that is not one of the choices."
  },
  "important_caveats": [
    "The source record is sequence-matched and its EC annotations cite experimental evidence, but the primary papers were not independently reviewed here.",
    "The answerability argument supports a family-level inference; it does not establish exact catalytic specificity from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source record reports another catalytic activity, EC 4.4.1.2, but that EC is not offered; among the listed choices, only D matches the supported methionine gamma-lyase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt record assigns EC 4.4.1.11 to L-methionine gamma-lyase and cites experimental evidence. Its catalytic-activity annotation gives the corresponding L-methionine reaction. The record also lists EC 4.4.1.2 for homocysteine desulfhydrase activity, but that is not one of the choices.",
    "evidence_ids": ["H1", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a roughly 400-residue PLP-dependent amino-acid lyase, supporting a gamma-lyase-family inference. That meaningfully favors D over the oxidoreductase and nucleoside-hydrolase choices; the offered 4.3.1.24 alternative is an ammonia-lyase class, whereas the sequence's family-level features support a PLP-dependent sulfur-amino-acid lyase instead. This is a transferable family inference, not certainty about the exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Family and cofactor-related sequence patterns provide a credible basis for distinguishing the methionine gamma-lyase choice from these alternatives, although sequence-only inference may not establish the exact EC annotation with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source record reports another catalytic activity, EC 4.4.1.2, but that EC is not offered; among the listed choices, only D matches the supported methionine gamma-lyase activity."
  },
  "important_caveats": [
    "The source record is sequence-matched and its EC annotations cite experimental evidence, but the primary papers were not independently reviewed here.",
    "The answerability argument supports a family-level inference; it does not establish exact catalytic specificity from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2H1K3G9 (MEGL_BREAU) assigns EC 4.4.1.11 (L-methionine gamma-lyase) as the recommended name with experimental evidence (ECO:0000269) from two independent PubMed publications (9726878, 30940696). The catalytic reaction L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+) is explicitly annotated. The sequence in the benchmark matches the UniProt entry exactly (406 AA, SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options B (1.6.5.2, NADH:ubiquinone oxidoreductase) and C (3.2.2.5, adenosine deaminase) can be eliminated immediately: the sequence lacks transmembrane helices, FMN/NADH-binding Rossmann folds, or the TIM-barrel/cytochrome motifs expected of an oxidoreductase, and it lacks the zinc-binding or purine-recognition motifs of a glycosidase. The remaining challenge is distinguishing A (4.3.1.24, cystathionine gamma-lyase) from D (4.4.1.11, L-methionine gamma-lyase), both PLP-dependent fold-type I gamma-lyases. The sequence displays the characteristic fold-type I PLP architecture (the 'GGADTLIQHP' and 'GGSDHL' motifs near the C-terminal and mid-sequence regions, the conserved 'GG' dinucleotides flanking the active-site lysine region). Critically, the 'GGADTL' motif in the C-terminal half and the 'GGSDHL' motif in the N-terminal half are sequence signatures more commonly associated with methionine gamma-lyases than with cystathionine gamma-lyases in the fold-type I superfamily. CGL enzymes typically display a different active-site pocket architecture (shorter loop accommodating the beta-thioether of cystathionine vs. the longer gamma-thioether of methionine) reflected in distinct residue patterns around the PLP-binding lysine. The overall ~406-residue length and the specific arrangement of the 'VHYPGLKGQ' and 'GGADTLIQHP' segments match the known Brevibacterium-type MGL family pattern rather than the CGL pattern. This constitutes a family-level sequence-architecture inference transferable across PLP fold-type I enzymes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of B and C is straightforward from enzyme-class morphology. The A-vs-D distinction, while non-trivial, can be addressed by recognizing fold-type I PLP motifs and the specific 'GGADTL'/'GGSDHL' sequence signatures that are shared across MGL homologs (not unique to this single protein). A model familiar with PLP enzyme families can apply learned patterns from other MGL and CGL sequences to make a defensible probabilistic assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both 4.3.1.24 (CGL) and 4.4.1.11 (MGL) are PLP-dependent gamma-lyases in the same fold-type I superfamily. Without very close inspection of active-site residue patterns, a model might reasonably consider either. However, the specific 'GGADTL' and 'GGSDHL' motifs tilt the inference toward MGL. The distinction is real but narrow; a model unfamiliar with the subtle sequence differences between MGL and CGL could plausibly select A.


### Important caveats

- The UniProt entry also annotates EC 4.4.1.2 (homocysteine desulfhydrase) as a secondary activity, but this EC number is not among the offered choices, so it does not create ambiguity within the question.
- Distinguishing MGL from CGL by sequence alone is a genuinely difficult task even for experts; the reasoning argument relies on learned family-level motifs rather than a single unambiguous diagnostic residue.
- The reviewer-only evidence confirms the sequence match and experimental EC assignment, but the evaluated model had no access to this annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (1.6.5.2, NADH:ubiquinone oxidoreductase) and C (3.2.2.5, adenosine deaminase) can be eliminated immediately: the sequence lacks transmembrane helices, FMN/NADH-binding Rossmann folds, or the TIM-barrel/cytochrome motifs expected of an oxidoreductase, and it lacks the zinc-binding or purine-recognition motifs of a glycosidase. The remaining challenge is distinguishing A (4.3.1.24, cystathionine gamma-lyase) from D (4.4.1.11, L-methionine gamma-lyase), both PLP-dependent fold-type I gamma-lyases. The sequence displays the characteristic fold-type I PLP architecture (the 'GGADTLIQHP' and 'GGSDHL' motifs near the C-terminal and mid-sequence regions, the conserved 'GG' dinucleotides flanking the active-site lysine region). Critically, the 'GGADTL' motif in the C-terminal half and the 'GGSDHL' motif in the N-terminal half are sequence signatures more commonly associated with methionine gamma-lyases than with cystathionine gamma-lyases in the fold-type I superfamily. CGL enzymes typically display a different active-site pocket architecture (shorter loop accommodating the beta-thioether of cystathionine vs. the longer gamma-thioether of methionine) reflected in distinct residue patterns around the PLP-binding lysine. The overall ~406-residue length and the specific arrangement of the 'VHYPGLKGQ' and 'GGADTLIQHP' segments match the known Brevibacterium-type MGL family pattern rather than the CGL pattern. This constitutes a family-level sequence-architecture inference transferable across PLP fold-type I enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B and C is straightforward from enzyme-class morphology. The A-vs-D distinction, while non-trivial, can be addressed by recognizing fold-type I PLP motifs and the specific 'GGADTL'/'GGSDHL' sequence signatures that are shared across MGL homologs (not unique to this single protein). A model familiar with PLP enzyme families can apply learned patterns from other MGL and CGL sequences to make a defensible probabilistic assignment."
  },
  "case_id": "EC_number_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A2H1K3G9 (MEGL_BREAU) assigns EC 4.4.1.11 (L-methionine gamma-lyase) as the recommended name with experimental evidence (ECO:0000269) from two independent PubMed publications (9726878, 30940696). The catalytic reaction L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+) is explicitly annotated. The sequence in the benchmark matches the UniProt entry exactly (406 AA, SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt entry also annotates EC 4.4.1.2 (homocysteine desulfhydrase) as a secondary activity, but this EC number is not among the offered choices, so it does not create ambiguity within the question.",
    "Distinguishing MGL from CGL by sequence alone is a genuinely difficult task even for experts; the reasoning argument relies on learned family-level motifs rather than a single unambiguous diagnostic residue.",
    "The reviewer-only evidence confirms the sequence match and experimental EC assignment, but the evaluated model had no access to this annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both 4.3.1.24 (CGL) and 4.4.1.11 (MGL) are PLP-dependent gamma-lyases in the same fold-type I superfamily. Without very close inspection of active-site residue patterns, a model might reasonably consider either. However, the specific 'GGADTL' and 'GGSDHL' motifs tilt the inference toward MGL. The distinction is real but narrow; a model unfamiliar with the subtle sequence differences between MGL and CGL could plausibly select A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2H1K3G9 (MEGL_BREAU) assigns EC 4.4.1.11 (L-methionine gamma-lyase) as the recommended name with experimental evidence (ECO:0000269) from two independent PubMed publications (9726878, 30940696). The catalytic reaction L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+) is explicitly annotated. The sequence in the benchmark matches the UniProt entry exactly (406 AA, SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options B (1.6.5.2, NADH:ubiquinone oxidoreductase) and C (3.2.2.5, adenosine deaminase) can be eliminated immediately: the sequence lacks transmembrane helices, FMN/NADH-binding Rossmann folds, or the TIM-barrel/cytochrome motifs expected of an oxidoreductase, and it lacks the zinc-binding or purine-recognition motifs of a glycosidase. The remaining challenge is distinguishing A (4.3.1.24, cystathionine gamma-lyase) from D (4.4.1.11, L-methionine gamma-lyase), both PLP-dependent fold-type I gamma-lyases. The sequence displays the characteristic fold-type I PLP architecture (the 'GGADTLIQHP' and 'GGSDHL' motifs near the C-terminal and mid-sequence regions, the conserved 'GG' dinucleotides flanking the active-site lysine region). Critically, the 'GGADTL' motif in the C-terminal half and the 'GGSDHL' motif in the N-terminal half are sequence signatures more commonly associated with methionine gamma-lyases than with cystathionine gamma-lyases in the fold-type I superfamily. CGL enzymes typically display a different active-site pocket architecture (shorter loop accommodating the beta-thioether of cystathionine vs. the longer gamma-thioether of methionine) reflected in distinct residue patterns around the PLP-binding lysine. The overall ~406-residue length and the specific arrangement of the 'VHYPGLKGQ' and 'GGADTLIQHP' segments match the known Brevibacterium-type MGL family pattern rather than the CGL pattern. This constitutes a family-level sequence-architecture inference transferable across PLP fold-type I enzymes.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B and C is straightforward from enzyme-class morphology. The A-vs-D distinction, while non-trivial, can be addressed by recognizing fold-type I PLP motifs and the specific 'GGADTL'/'GGSDHL' sequence signatures that are shared across MGL homologs (not unique to this single protein). A model familiar with PLP enzyme families can apply learned patterns from other MGL and CGL sequences to make a defensible probabilistic assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both 4.3.1.24 (CGL) and 4.4.1.11 (MGL) are PLP-dependent gamma-lyases in the same fold-type I superfamily. Without very close inspection of active-site residue patterns, a model might reasonably consider either. However, the specific 'GGADTL' and 'GGSDHL' motifs tilt the inference toward MGL. The distinction is real but narrow; a model unfamiliar with the subtle sequence differences between MGL and CGL could plausibly select A."
  },
  "important_caveats": [
    "The UniProt entry also annotates EC 4.4.1.2 (homocysteine desulfhydrase) as a secondary activity, but this EC number is not among the offered choices, so it does not create ambiguity within the question.",
    "Distinguishing MGL from CGL by sequence alone is a genuinely difficult task even for experts; the reasoning argument relies on learned family-level motifs rather than a single unambiguous diagnostic residue.",
    "The reviewer-only evidence confirms the sequence match and experimental EC assignment, but the evaluated model had no access to this annotation."
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
  "benchmark_sequence_length": 406,
  "benchmark_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-01-31",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 406,
  "current_source_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2H1K3G9",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "selected_historical_source_sequence_length": 406,
  "selected_historical_source_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "selected_historical_version": {
    "accession": "A0A2H1K3G9",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MEGL_BREAU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2H1K3G9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-01-31\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Micrococcales\",\"Brevibacteriaceae\",\"Brevibacterium\"],\"scientificName\":\"Brevibacterium aurantiacum\",\"taxonId\":273384}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"4.4.1.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"Homocysteine desulfhydrase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"MGL-BL929\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"4.4.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"L-methionine gamma-lyase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"MGL\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23801\"}}],\"reaction\":{\"ecNumber\":\"4.4.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"name\":\"L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23800\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16007\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28938\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57844\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:14502\"}}],\"reaction\":{\"ecNumber\":\"4.4.1.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"name\":\"L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide + NH4(+) + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14501\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28938\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29919\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58199\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dias B.\",\"Weimer B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9726878\"},{\"database\":\"DOI\",\"id\":\"10.1128/aem.64.9.3327-3331.1998\"}],\"citationType\":\"journal article\",\"firstPage\":\"3327\",\"id\":\"9726878\",\"journal\":\"Appl. Environ. Microbiol.\",\"lastPage\":\"3331\",\"publicationDate\":\"1998\",\"title\":\"Purification and characterization of L-methionine gamma-lyase from brevibacterium linens BL2.\",\"volume\":\"64\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"BL2\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Machover D.\",\"Rossi L.\",\"Hamelin J.\",\"Desterke C.\",\"Goldschmidt E.\",\"Chadefaux-Vekemans B.\",\"Bonnarme P.\",\"Briozzo P.\",\"Kopecny D.\",\"Pierige F.\",\"Magnani M.\",\"Mollicone R.\",\"Haghighi-Rad F.\",\"Gaston-Mathe Y.\",\"Dairou J.\",\"Boucheix C.\",\"Saffroy R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30940696\"},{\"database\":\"DOI\",\"id\":\"10.1124/jpet.119.256537\"}],\"citationType\":\"journal article\",\"firstPage\":\"489\",\"id\":\"30940696\",\"journal\":\"J. Pharmacol. Exp. Ther.\",\"lastPage\":\"502\",\"publicationDate\":\"2019\",\"title\":\"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for Sustained L-Methionine Elimination.\",\"volume\":\"369\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB 8546 / KC\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   MEGL_BREAU              Reviewed;         406 AA.\nAC   A0A2H1K3G9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   31-JAN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=L-methionine gamma-lyase {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            Short=MGL {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            EC=4.4.1.11 {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000303|PubMed:30940696};\nDE            EC=4.4.1.2 {ECO:0000269|PubMed:30940696};\nDE   AltName: Full=MGL-BL929 {ECO:0000303|PubMed:30940696};\nGN   ORFNames=BAUR9175_03070 {ECO:0000312|EMBL:SMX94104.1},\nGN   BAUR920_03040 {ECO:0000312|EMBL:SMX97377.1},\nGN   BAURA63_02933 {ECO:0000312|EMBL:SMX94451.1},\nGN   BAURA86_00394 {ECO:0000312|EMBL:SMX72154.1};\nOS   Brevibacterium aurantiacum.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales;\nOC   Brevibacteriaceae; Brevibacterium.\nOX   NCBI_TaxID=273384;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-methionine gamma-lyase {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            Short=MGL {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            EC=4.4.1.11 {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000303|PubMed:30940696};\nDE            EC=4.4.1.2 {ECO:0000269|PubMed:30940696};\nDE   AltName: Full=MGL-BL929 {ECO:0000303|PubMed:30940696};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBSTRATE SPECIFICITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, ACTIVITY REGULATION, AND SUBUNIT.\nRC   STRAIN=BL2;\nRX   PubMed=9726878; DOI=10.1128/aem.64.9.3327-3331.1998;\nRA   Dias B., Weimer B.;\nRT   \"Purification and characterization of L-methionine gamma-lyase from\nRT   brevibacterium linens BL2.\";\nRL   Appl. Environ. Microbiol. 64:3327-3331(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBSTRATE SPECIFICITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND BIOTECHNOLOGY.\nRC   STRAIN=ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB\nRC   8546 / KC;\nRX   PubMed=30940696; DOI=10.1124/jpet.119.256537;\nRA   Machover D., Rossi L., Hamelin J., Desterke C., Goldschmidt E.,\nRA   Chadefaux-Vekemans B., Bonnarme P., Briozzo P., Kopecny D., Pierige F.,\nRA   Magnani M., Mollicone R., Haghighi-Rad F., Gaston-Mathe Y., Dairou J.,\nRA   Boucheix C., Saffroy R.;\nRT   \"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from\nRT   Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for\nRT   Sustained L-Methionine Elimination.\";\nRL   J. Pharmacol. Exp. Ther. 369:489-502(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+);\nCC         Xref=Rhea:RHEA:23800, ChEBI:CHEBI:15377, ChEBI:CHEBI:16007,\nCC         ChEBI:CHEBI:16763, ChEBI:CHEBI:28938, ChEBI:CHEBI:57844; EC=4.4.1.11;\nCC         Evidence={ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23801;\nCC         Evidence={ECO:0000269|PubMed:30940696};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide +\nCC         NH4(+) + H(+); Xref=Rhea:RHEA:14501, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16763, ChEBI:CHEBI:28938,\nCC         ChEBI:CHEBI:29919, ChEBI:CHEBI:58199; EC=4.4.1.2;\nCC         Evidence={ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14502;\nCC         Evidence={ECO:0000305|PubMed:30940696};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
