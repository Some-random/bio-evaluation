# EC_number_0001

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0001.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 4.4.1.11

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNSMHPETLMVHGGMDGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHALKDGDSAVYQRLWQPGVARFETALAELEHADEAVAFATGMAAMTAALLAAVNAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEAEIASAIQDDTGLVIVETPANPSLDLVDLDSVVAAAGTVPVLVDNTFCTPVLQQPIRHGAALVLHSATKYLGGHGDAMGGIIATNSDWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLAAHPAITAVHYPGLNGQDPRGLLGRQMSGGGAMIALELAGGFDAARSFVEHCSLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLEDDLIAALDASRAAA

[Multiple Choices]
A. 4.3.1.24
B. 4.2.1.70
C. 4.4.1.11
D. 2.7.13.3
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

> The sequence-matched UniProt record assigns EC 4.4.1.11 and describes the L-methionine gamma-lyase reaction, supporting choice C. However, the annotation is transferred from a homolog (ECO:0000250), not evidence of a direct experimental assay of this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a pyridoxal-phosphate-dependent amino-acid lyase family, and transferable family-level sequence recognition can favor a methionine gamma-lyase over the offered alternatives, including the kinase option. That makes C a meaningful inference from the sequence and choices, though closely related lyases can have overlapping activities and sequence alone may not establish every substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-based inference from sequence patterns can distinguish the offered MGL choice without recalling this exact protein's database record. The precise enzyme assignment remains less certain than an experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C among the offered choices is supported as the MGL EC number. The source also annotates EC 4.4.1.2 as an alternative activity, but that number is not an offered option.


### Important caveats

- The supporting annotation is homology-transferred, not direct experimental evidence for this exact protein.
- The sequence-matched record also annotates EC 4.4.1.2, so the protein may have an additional relevant activity not represented among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a pyridoxal-phosphate-dependent amino-acid lyase family, and transferable family-level sequence recognition can favor a methionine gamma-lyase over the offered alternatives, including the kinase option. That makes C a meaningful inference from the sequence and choices, though closely related lyases can have overlapping activities and sequence alone may not establish every substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-based inference from sequence patterns can distinguish the offered MGL choice without recalling this exact protein's database record. The precise enzyme assignment remains less certain than an experimental characterization."
  },
  "case_id": "EC_number_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 4.4.1.11 and describes the L-methionine gamma-lyase reaction, supporting choice C. However, the annotation is transferred from a homolog (ECO:0000250), not evidence of a direct experimental assay of this protein."
  },
  "important_caveats": [
    "The supporting annotation is homology-transferred, not direct experimental evidence for this exact protein.",
    "The sequence-matched record also annotates EC 4.4.1.2, so the protein may have an additional relevant activity not represented among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the offered choices is supported as the MGL EC number. The source also annotates EC 4.4.1.2 as an alternative activity, but that number is not an offered option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 4.4.1.11 and describes the L-methionine gamma-lyase reaction, supporting choice C. However, the annotation is transferred from a homolog (ECO:0000250), not evidence of a direct experimental assay of this protein.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a pyridoxal-phosphate-dependent amino-acid lyase family, and transferable family-level sequence recognition can favor a methionine gamma-lyase over the offered alternatives, including the kinase option. That makes C a meaningful inference from the sequence and choices, though closely related lyases can have overlapping activities and sequence alone may not establish every substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "A family-based inference from sequence patterns can distinguish the offered MGL choice without recalling this exact protein's database record. The precise enzyme assignment remains less certain than an experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the offered choices is supported as the MGL EC number. The source also annotates EC 4.4.1.2 as an alternative activity, but that number is not an offered option."
  },
  "important_caveats": [
    "The supporting annotation is homology-transferred, not direct experimental evidence for this exact protein.",
    "The sequence-matched record also annotates EC 4.4.1.2, so the protein may have an additional relevant activity not represented among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1H1YBL2 (sequence matched, 393 aa) assigns the recommended name L-methionine gamma-lyase with EC 4.4.1.11 (evidence C4, C5, H2, H3). The annotation is computational (ECO:0000250, similarity-based transfer from A0A2H1K3G9), not experimentally verified, but it is the current database annotation and is consistent with the expected answer C. The alternative EC 4.4.1.2 (homocysteine desulfhydrase) is listed only as an alternative name, not the primary assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple 'GG' motifs (e.g., GGDSYEW, GGSDHLLE, GGHGDAMGG, GGGAMIALE, GGFDAARSF) and 'T' and 'H' motifs characteristic of fold-type II pyridoxal-5'-phosphate (PLP)-dependent enzymes. This immediately eliminates EC 4.2.1.70 (hydroxycinnamoyl-CoA hydratase-lyase, not PLP-dependent, different fold) and EC 2.7.13.3 (glutamate-ammonia ligase, a completely different enzyme class and fold). Between the remaining two PLP fold-type II gamma-lyases (4.3.1.24 cystathionine gamma-lyase vs 4.4.1.11 L-methionine gamma-lyase), the distinction rests on whether the enzyme is a C-N lyase (EC 4.3) or C-S lyase (EC 4.4). Within the fold-type II superfamily, MGL and CGL form distinct phylogenetic subfamilies with characteristic differences in active-site residue spacing, the 'GG' motif arrangement, and overall sequence architecture. A model trained on characterized homologs (e.g., E. coli MetC for MGL, E. coli MetI for CGL) can recognize the subfamily membership pattern from the specific motif spacing, conserved residues, and ~393-aa length more typical of bacterial MGL. The EC class-level distinction (4.3 C-N lyase vs 4.4 C-S lyase) reflects the active-site geometry visible in the sequence pattern, favoring C-S lyase (4.4.1.11).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PLP fold-type II motifs are directly observable in the input sequence and eliminate options B and D. The A vs C distinction, while subtle, can be approached through family-level pattern recognition: the specific GG/T/H motif spacing, sequence length, and conserved residue architecture are transferable features learned from characterized MGL and CGL homologs in other organisms. This is probabilistic subfamily assignment, not first-principles proof, but it provides a meaningful basis for distinguishing the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A"
]
```

> Cystathionine gamma-lyase (4.3.1.24) and L-methionine gamma-lyase (4.4.1.11) are closely related fold-type II PLP enzymes that in some organisms share overlapping substrate specificities. Without experimental kinetics, a model could argue for A based on general fold-type II gamma-lyase similarity. However, the specific sequence pattern and the EC-class-level distinction (C-N vs C-S lyase) favor C, making A a weaker but not entirely implausible alternative.


### Important caveats

- The UniProt annotation for EC 4.4.1.11 is purely computational (ECO:0000250, similarity transfer from A0A2H1K3G9), not experimentally validated. The 'ground truth' is itself a database inference.
- The distinction between EC 4.3.1.24 and 4.4.1.11 is genuinely subtle at the sequence level; the reasoning argument is probabilistic subfamily assignment rather than a definitive structural proof.
- The organism (Brevibacterium sandarakinum) is not provided in the model input, so organism-specific metabolic context (Brevibacterium's known role in methionine metabolism) cannot be used as an original input.
- The alternative EC 4.4.1.2 (homocysteine desulfhydrase) is also annotated for this protein but is not among the answer choices, so it does not create additional ambiguity within the given options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple 'GG' motifs (e.g., GGDSYEW, GGSDHLLE, GGHGDAMGG, GGGAMIALE, GGFDAARSF) and 'T' and 'H' motifs characteristic of fold-type II pyridoxal-5'-phosphate (PLP)-dependent enzymes. This immediately eliminates EC 4.2.1.70 (hydroxycinnamoyl-CoA hydratase-lyase, not PLP-dependent, different fold) and EC 2.7.13.3 (glutamate-ammonia ligase, a completely different enzyme class and fold). Between the remaining two PLP fold-type II gamma-lyases (4.3.1.24 cystathionine gamma-lyase vs 4.4.1.11 L-methionine gamma-lyase), the distinction rests on whether the enzyme is a C-N lyase (EC 4.3) or C-S lyase (EC 4.4). Within the fold-type II superfamily, MGL and CGL form distinct phylogenetic subfamilies with characteristic differences in active-site residue spacing, the 'GG' motif arrangement, and overall sequence architecture. A model trained on characterized homologs (e.g., E. coli MetC for MGL, E. coli MetI for CGL) can recognize the subfamily membership pattern from the specific motif spacing, conserved residues, and ~393-aa length more typical of bacterial MGL. The EC class-level distinction (4.3 C-N lyase vs 4.4 C-S lyase) reflects the active-site geometry visible in the sequence pattern, favoring C-S lyase (4.4.1.11).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PLP fold-type II motifs are directly observable in the input sequence and eliminate options B and D. The A vs C distinction, while subtle, can be approached through family-level pattern recognition: the specific GG/T/H motif spacing, sequence length, and conserved residue architecture are transferable features learned from characterized MGL and CGL homologs in other organisms. This is probabilistic subfamily assignment, not first-principles proof, but it provides a meaningful basis for distinguishing the offered alternatives."
  },
  "case_id": "EC_number_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1H1YBL2 (sequence matched, 393 aa) assigns the recommended name L-methionine gamma-lyase with EC 4.4.1.11 (evidence C4, C5, H2, H3). The annotation is computational (ECO:0000250, similarity-based transfer from A0A2H1K3G9), not experimentally verified, but it is the current database annotation and is consistent with the expected answer C. The alternative EC 4.4.1.2 (homocysteine desulfhydrase) is listed only as an alternative name, not the primary assignment."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.4.1.11 is purely computational (ECO:0000250, similarity transfer from A0A2H1K3G9), not experimentally validated. The 'ground truth' is itself a database inference.",
    "The distinction between EC 4.3.1.24 and 4.4.1.11 is genuinely subtle at the sequence level; the reasoning argument is probabilistic subfamily assignment rather than a definitive structural proof.",
    "The organism (Brevibacterium sandarakinum) is not provided in the model input, so organism-specific metabolic context (Brevibacterium's known role in methionine metabolism) cannot be used as an original input.",
    "The alternative EC 4.4.1.2 (homocysteine desulfhydrase) is also annotated for this protein but is not among the answer choices, so it does not create additional ambiguity within the given options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A"
    ],
    "reason": "Cystathionine gamma-lyase (4.3.1.24) and L-methionine gamma-lyase (4.4.1.11) are closely related fold-type II PLP enzymes that in some organisms share overlapping substrate specificities. Without experimental kinetics, a model could argue for A based on general fold-type II gamma-lyase similarity. However, the specific sequence pattern and the EC-class-level distinction (C-N vs C-S lyase) favor C, making A a weaker but not entirely implausible alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1H1YBL2 (sequence matched, 393 aa) assigns the recommended name L-methionine gamma-lyase with EC 4.4.1.11 (evidence C4, C5, H2, H3). The annotation is computational (ECO:0000250, similarity-based transfer from A0A2H1K3G9), not experimentally verified, but it is the current database annotation and is consistent with the expected answer C. The alternative EC 4.4.1.2 (homocysteine desulfhydrase) is listed only as an alternative name, not the primary assignment.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple 'GG' motifs (e.g., GGDSYEW, GGSDHLLE, GGHGDAMGG, GGGAMIALE, GGFDAARSF) and 'T' and 'H' motifs characteristic of fold-type II pyridoxal-5'-phosphate (PLP)-dependent enzymes. This immediately eliminates EC 4.2.1.70 (hydroxycinnamoyl-CoA hydratase-lyase, not PLP-dependent, different fold) and EC 2.7.13.3 (glutamate-ammonia ligase, a completely different enzyme class and fold). Between the remaining two PLP fold-type II gamma-lyases (4.3.1.24 cystathionine gamma-lyase vs 4.4.1.11 L-methionine gamma-lyase), the distinction rests on whether the enzyme is a C-N lyase (EC 4.3) or C-S lyase (EC 4.4). Within the fold-type II superfamily, MGL and CGL form distinct phylogenetic subfamilies with characteristic differences in active-site residue spacing, the 'GG' motif arrangement, and overall sequence architecture. A model trained on characterized homologs (e.g., E. coli MetC for MGL, E. coli MetI for CGL) can recognize the subfamily membership pattern from the specific motif spacing, conserved residues, and ~393-aa length more typical of bacterial MGL. The EC class-level distinction (4.3 C-N lyase vs 4.4 C-S lyase) reflects the active-site geometry visible in the sequence pattern, favoring C-S lyase (4.4.1.11).",
    "missing_item_specific_fact": "",
    "reason": "The PLP fold-type II motifs are directly observable in the input sequence and eliminate options B and D. The A vs C distinction, while subtle, can be approached through family-level pattern recognition: the specific GG/T/H motif spacing, sequence length, and conserved residue architecture are transferable features learned from characterized MGL and CGL homologs in other organisms. This is probabilistic subfamily assignment, not first-principles proof, but it provides a meaningful basis for distinguishing the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A"],
    "reason": "Cystathionine gamma-lyase (4.3.1.24) and L-methionine gamma-lyase (4.4.1.11) are closely related fold-type II PLP enzymes that in some organisms share overlapping substrate specificities. Without experimental kinetics, a model could argue for A based on general fold-type II gamma-lyase similarity. However, the specific sequence pattern and the EC-class-level distinction (C-N vs C-S lyase) favor C, making A a weaker but not entirely implausible alternative."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.4.1.11 is purely computational (ECO:0000250, similarity transfer from A0A2H1K3G9), not experimentally validated. The 'ground truth' is itself a database inference.",
    "The distinction between EC 4.3.1.24 and 4.4.1.11 is genuinely subtle at the sequence level; the reasoning argument is probabilistic subfamily assignment rather than a definitive structural proof.",
    "The organism (Brevibacterium sandarakinum) is not provided in the model input, so organism-specific metabolic context (Brevibacterium's known role in methionine metabolism) cannot be used as an original input.",
    "The alternative EC 4.4.1.2 (homocysteine desulfhydrase) is also annotated for this protein but is not among the answer choices, so it does not create additional ambiguity within the given options."
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
  "benchmark_sequence_length": 393,
  "benchmark_sequence_sha256": "d62ef1248b2c7e60f020a849ac08272c51994b6267c0d401825afaddef80c605",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-01-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 393,
  "current_source_sequence_sha256": "d62ef1248b2c7e60f020a849ac08272c51994b6267c0d401825afaddef80c605",
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
  "requested_accession": "A0A1H1YBL2",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2",
  "selected_historical_source_sequence_length": 393,
  "selected_historical_source_sequence_sha256": "d62ef1248b2c7e60f020a849ac08272c51994b6267c0d401825afaddef80c605",
  "selected_historical_version": {
    "accession": "A0A1H1YBL2",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MEGL_BRESA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1H1YBL2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-01-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Micrococcales\",\"Brevibacteriaceae\",\"Brevibacterium\"],\"scientificName\":\"Brevibacterium sandarakinum\",\"taxonId\":629680}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"4.4.1.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"Homocysteine desulfhydrase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"4.4.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"L-methionine gamma-lyase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"MGL\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23801\"}}],\"reaction\":{\"ecNumber\":\"4.4.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"name\":\"L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23800\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16007\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28938\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57844\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:14502\"}}],\"reaction\":{\"ecNumber\":\"4.4.1.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"name\":\"L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide + NH4(+) + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14501\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28938\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29919\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58199\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   MEGL_BRESA              Reviewed;         393 AA.\nAC   A0A1H1YBL2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JAN-2017, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=L-methionine gamma-lyase {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            Short=MGL {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            EC=4.4.1.11 {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            EC=4.4.1.2 {ECO:0000250|UniProtKB:A0A2H1K3G9};\nGN   ORFNames=SAMN04489751_4033 {ECO:0000312|EMBL:SDT18406.1};\nOS   Brevibacterium sandarakinum.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales;\nOC   Brevibacteriaceae; Brevibacterium.\nOX   NCBI_TaxID=629680;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.341815+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2",
  "url": "https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-methionine gamma-lyase {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            Short=MGL {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            EC=4.4.1.11 {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            EC=4.4.1.2 {ECO:0000250|UniProtKB:A0A2H1K3G9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.341815+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2",
  "url": "https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+);\nCC         Xref=Rhea:RHEA:23800, ChEBI:CHEBI:15377, ChEBI:CHEBI:16007,\nCC         ChEBI:CHEBI:16763, ChEBI:CHEBI:28938, ChEBI:CHEBI:57844; EC=4.4.1.11;\nCC         Evidence={ECO:0000250|UniProtKB:A0A2H1K3G9};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23801;\nCC         Evidence={ECO:0000250|UniProtKB:A0A2H1K3G9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.341815+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2",
  "url": "https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide +\nCC         NH4(+) + H(+); Xref=Rhea:RHEA:14501, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16763, ChEBI:CHEBI:28938,\nCC         ChEBI:CHEBI:29919, ChEBI:CHEBI:58199; EC=4.4.1.2;\nCC         Evidence={ECO:0000250|UniProtKB:A0A2H1K3G9};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14502;\nCC         Evidence={ECO:0000250|UniProtKB:A0A2H1K3G9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.341815+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2",
  "url": "https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
