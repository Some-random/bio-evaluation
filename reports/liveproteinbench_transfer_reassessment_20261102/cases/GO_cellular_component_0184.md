# GO_cellular_component_0184

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0184.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — cell outer membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIALTERTERVRPQRVEQNLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGGAREVQFFTDEDGERNLVALEKKGGIWRRSASEADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLIYDSLYFHGQQVAAGDILAAEVVKGGTRHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. protein-DNA complex
B. nuclear pore nuclear basket
C. cell outer membrane
D. chromosome
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

> The supplied sequence matches the annotated protein. Its UniProt record assigns cell outer membrane, including a GO annotation with IDA evidence; the accompanying localization note is qualified as probable for the mature protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic N-terminal segment consistent with an export signal or membrane-targeting region, followed by a long globular enzyme-like region. Transferable knowledge of bacterial proteins makes an envelope-associated protein substantially more plausible than a nuclear pore basket, chromosome, or protein-DNA complex. This favors C among the offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The N-terminal targeting feature and the stark contrast between an exported bacterial-type protein and the nuclear/DNA-related alternatives provide a meaningful inference without needing the exact database annotation. The sequence alone does not establish outer membrane rather than another envelope destination, but that limitation does not make the offered alternatives equally plausible.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports export or membrane association, whereas the other choices describe nuclear or DNA-associated locations. No alternative is comparably supported by the input.


### Important caveats

- A signal peptide or hydrophobic N-terminus alone does not prove outer-membrane localization.
- The source describes mature-protein association with the outer membrane as probable; the GO assignment is recorded with IDA evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with an export signal or membrane-targeting region, followed by a long globular enzyme-like region. Transferable knowledge of bacterial proteins makes an envelope-associated protein substantially more plausible than a nuclear pore basket, chromosome, or protein-DNA complex. This favors C among the offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal targeting feature and the stark contrast between an exported bacterial-type protein and the nuclear/DNA-related alternatives provide a meaningful inference without needing the exact database annotation. The sequence alone does not establish outer membrane rather than another envelope destination, but that limitation does not make the offered alternatives equally plausible."
  },
  "case_id": "GO_cellular_component_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein. Its UniProt record assigns cell outer membrane, including a GO annotation with IDA evidence; the accompanying localization note is qualified as probable for the mature protein."
  },
  "important_caveats": [
    "A signal peptide or hydrophobic N-terminus alone does not prove outer-membrane localization.",
    "The source describes mature-protein association with the outer membrane as probable; the GO assignment is recorded with IDA evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports export or membrane association, whereas the other choices describe nuclear or DNA-associated locations. No alternative is comparably supported by the input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein. Its UniProt record assigns cell outer membrane, including a GO annotation with IDA evidence; the accompanying localization note is qualified as probable for the mature protein.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with an export signal or membrane-targeting region, followed by a long globular enzyme-like region. Transferable knowledge of bacterial proteins makes an envelope-associated protein substantially more plausible than a nuclear pore basket, chromosome, or protein-DNA complex. This favors C among the offered choices.",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal targeting feature and the stark contrast between an exported bacterial-type protein and the nuclear/DNA-related alternatives provide a meaningful inference without needing the exact database annotation. The sequence alone does not establish outer membrane rather than another envelope destination, but that limitation does not make the offered alternatives equally plausible."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports export or membrane association, whereas the other choices describe nuclear or DNA-associated locations. No alternative is comparably supported by the input."
  },
  "important_caveats": [
    "A signal peptide or hydrophobic N-terminus alone does not prove outer-membrane localization.",
    "The source describes mature-protein association with the outer membrane as probable; the GO assignment is recorded with IDA evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E0N688 (MPG_NEIM3) annotates the subcellular location as 'Cell outer membrane' (GO:0009279) with evidence from PubMed:22046377 (crystal structure paper, PDB:3SLU). The annotation notes a probable signal/transmembrane region in the N-terminus and that the mature protein is probably associated with the cell outer membrane. The GO cross-reference carries evidence code IDA (direct assay) in the current entry. The sequence matches the benchmark exactly (430 aa, SHA256 confirmed). The annotation is supported by experimental structural evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus 'MAVFPLSAKHRKYALRALAVSIILVSAAYIAL' contains a hydrophobic stretch with an 'SAA' motif near position 28-30, which is a classic bacterial lipobox pattern (&#91;L/I/V&#93;&#91;A/T&#93;&#91;G/S&#93;&#91;A/S/L&#93;A/C) found in Gram-negative bacterial lipoproteins/outer membrane proteins. The 'GGGGG' and 'GG' repeats are common in bacterial surface proteins. The 'HANG' motif (~position 310) is a zinc metalloprotease catalytic motif (HxH), identifying this as a bacterial metalloprotease. From transferable knowledge: (1) The absence of any eukaryotic targeting signals (no NLS clusters, no mitochondrial transit peptide) and the presence of bacterial-type signal peptide strongly indicate a prokaryotic protein, which eliminates B (nuclear pore nuclear basket is exclusively eukaryotic). (2) The protein is a metalloprotease with no DNA-binding motifs (no HTH, zinc finger, or leucine zipper), eliminating A (protein-DNA complex) and D (chromosome). (3) In Gram-negative bacteria, proteins with N-terminal signal peptides/lipoboxes are exported to the periplasm or outer membrane. Among the four choices, only C (cell outer membrane) is compatible with a bacterial membrane-targeted protein. The reasoning chain—recognize bacterial signal peptide → eliminate eukaryotic structures → eliminate DNA-binding options → select the only bacterial membrane option—is well-supported by transferable knowledge of protein targeting and cell biology.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can distinguish C from A, B, and D using: (a) recognition of the N-terminal lipobox/signal peptide as a bacterial export signal, (b) recognition that nuclear pore nuclear basket is exclusively eukaryotic, (c) recognition that a metalloprotease lacks DNA-binding motifs, and (d) the general principle that Gram-negative bacterial proteins with signal peptides localize to outer membrane or periplasm. The other three options are all nuclear/eukaryotic structures incompatible with a bacterial secreted protein. This is a concrete, multi-step inference from sequence features and general biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (protein-DNA complex, nuclear pore nuclear basket, chromosome) are all nuclear/eukaryotic structures that are clearly incompatible with a bacterial protein bearing an N-terminal signal peptide and metalloprotease motifs. Only C (cell outer membrane) is compatible with the sequence features. No ambiguity exists among the offered choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (curator inference) for the subcellular location, supported by the crystal structure paper (PubMed:22046377). The word 'probably' in the annotation note indicates some uncertainty, but the GO annotation is recorded as IDA in the current entry.
- The organism identity (Neisseria meningitidis) is reviewer-only information. However, the bacterial nature of the protein can be inferred from sequence features (lipobox, GG repeats, metalloprotease motifs) without knowing the exact species.
- The historical entry (v51) uses IEA evidence for the GO term, while the current entry (v53) shows IDA. The benchmark was likely constructed from the current or near-current annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus 'MAVFPLSAKHRKYALRALAVSIILVSAAYIAL' contains a hydrophobic stretch with an 'SAA' motif near position 28-30, which is a classic bacterial lipobox pattern ([L/I/V][A/T][G/S][A/S/L]A/C) found in Gram-negative bacterial lipoproteins/outer membrane proteins. The 'GGGGG' and 'GG' repeats are common in bacterial surface proteins. The 'HANG' motif (~position 310) is a zinc metalloprotease catalytic motif (HxH), identifying this as a bacterial metalloprotease. From transferable knowledge: (1) The absence of any eukaryotic targeting signals (no NLS clusters, no mitochondrial transit peptide) and the presence of bacterial-type signal peptide strongly indicate a prokaryotic protein, which eliminates B (nuclear pore nuclear basket is exclusively eukaryotic). (2) The protein is a metalloprotease with no DNA-binding motifs (no HTH, zinc finger, or leucine zipper), eliminating A (protein-DNA complex) and D (chromosome). (3) In Gram-negative bacteria, proteins with N-terminal signal peptides/lipoboxes are exported to the periplasm or outer membrane. Among the four choices, only C (cell outer membrane) is compatible with a bacterial membrane-targeted protein. The reasoning chain—recognize bacterial signal peptide → eliminate eukaryotic structures → eliminate DNA-binding options → select the only bacterial membrane option—is well-supported by transferable knowledge of protein targeting and cell biology.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish C from A, B, and D using: (a) recognition of the N-terminal lipobox/signal peptide as a bacterial export signal, (b) recognition that nuclear pore nuclear basket is exclusively eukaryotic, (c) recognition that a metalloprotease lacks DNA-binding motifs, and (d) the general principle that Gram-negative bacterial proteins with signal peptides localize to outer membrane or periplasm. The other three options are all nuclear/eukaryotic structures incompatible with a bacterial secreted protein. This is a concrete, multi-step inference from sequence features and general biology."
  },
  "case_id": "GO_cellular_component_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E0N688 (MPG_NEIM3) annotates the subcellular location as 'Cell outer membrane' (GO:0009279) with evidence from PubMed:22046377 (crystal structure paper, PDB:3SLU). The annotation notes a probable signal/transmembrane region in the N-terminus and that the mature protein is probably associated with the cell outer membrane. The GO cross-reference carries evidence code IDA (direct assay) in the current entry. The sequence matches the benchmark exactly (430 aa, SHA256 confirmed). The annotation is supported by experimental structural evidence."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (curator inference) for the subcellular location, supported by the crystal structure paper (PubMed:22046377). The word 'probably' in the annotation note indicates some uncertainty, but the GO annotation is recorded as IDA in the current entry.",
    "The organism identity (Neisseria meningitidis) is reviewer-only information. However, the bacterial nature of the protein can be inferred from sequence features (lipobox, GG repeats, metalloprotease motifs) without knowing the exact species.",
    "The historical entry (v51) uses IEA evidence for the GO term, while the current entry (v53) shows IDA. The benchmark was likely constructed from the current or near-current annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (protein-DNA complex, nuclear pore nuclear basket, chromosome) are all nuclear/eukaryotic structures that are clearly incompatible with a bacterial protein bearing an N-terminal signal peptide and metalloprotease motifs. Only C (cell outer membrane) is compatible with the sequence features. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E0N688 (MPG_NEIM3) annotates the subcellular location as 'Cell outer membrane' (GO:0009279) with evidence from PubMed:22046377 (crystal structure paper, PDB:3SLU). The annotation notes a probable signal/transmembrane region in the N-terminus and that the mature protein is probably associated with the cell outer membrane. The GO cross-reference carries evidence code IDA (direct assay) in the current entry. The sequence matches the benchmark exactly (430 aa, SHA256 confirmed). The annotation is supported by experimental structural evidence.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus 'MAVFPLSAKHRKYALRALAVSIILVSAAYIAL' contains a hydrophobic stretch with an 'SAA' motif near position 28-30, which is a classic bacterial lipobox pattern ([L/I/V][A/T][G/S][A/S/L]A/C) found in Gram-negative bacterial lipoproteins/outer membrane proteins. The 'GGGGG' and 'GG' repeats are common in bacterial surface proteins. The 'HANG' motif (~position 310) is a zinc metalloprotease catalytic motif (HxH), identifying this as a bacterial metalloprotease. From transferable knowledge: (1) The absence of any eukaryotic targeting signals (no NLS clusters, no mitochondrial transit peptide) and the presence of bacterial-type signal peptide strongly indicate a prokaryotic protein, which eliminates B (nuclear pore nuclear basket is exclusively eukaryotic). (2) The protein is a metalloprotease with no DNA-binding motifs (no HTH, zinc finger, or leucine zipper), eliminating A (protein-DNA complex) and D (chromosome). (3) In Gram-negative bacteria, proteins with N-terminal signal peptides/lipoboxes are exported to the periplasm or outer membrane. Among the four choices, only C (cell outer membrane) is compatible with a bacterial membrane-targeted protein. The reasoning chain—recognize bacterial signal peptide → eliminate eukaryotic structures → eliminate DNA-binding options → select the only bacterial membrane option—is well-supported by transferable knowledge of protein targeting and cell biology.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish C from A, B, and D using: (a) recognition of the N-terminal lipobox/signal peptide as a bacterial export signal, (b) recognition that nuclear pore nuclear basket is exclusively eukaryotic, (c) recognition that a metalloprotease lacks DNA-binding motifs, and (d) the general principle that Gram-negative bacterial proteins with signal peptides localize to outer membrane or periplasm. The other three options are all nuclear/eukaryotic structures incompatible with a bacterial secreted protein. This is a concrete, multi-step inference from sequence features and general biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (protein-DNA complex, nuclear pore nuclear basket, chromosome) are all nuclear/eukaryotic structures that are clearly incompatible with a bacterial protein bearing an N-terminal signal peptide and metalloprotease motifs. Only C (cell outer membrane) is compatible with the sequence features. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (curator inference) for the subcellular location, supported by the crystal structure paper (PubMed:22046377). The word 'probably' in the annotation note indicates some uncertainty, but the GO annotation is recorded as IDA in the current entry.",
    "The organism identity (Neisseria meningitidis) is reviewer-only information. However, the bacterial nature of the protein can be inferred from sequence features (lipobox, GG repeats, metalloprotease motifs) without knowing the exact species.",
    "The historical entry (v51) uses IEA evidence for the GO term, while the current entry (v53) shows IDA. The benchmark was likely constructed from the current or near-current annotation."
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
  "benchmark_sequence_length": 430,
  "benchmark_sequence_sha256": "3e75444ef73a59ea32e1df8dd911f094a963233fecca96f1fb511d7b05e30d56",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 430,
  "current_source_sequence_sha256": "3e75444ef73a59ea32e1df8dd911f094a963233fecca96f1fb511d7b05e30d56",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E0N688",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "selected_historical_source_sequence_length": 430,
  "selected_historical_source_sequence_sha256": "3e75444ef73a59ea32e1df8dd911f094a963233fecca96f1fb511d7b05e30d56",
  "selected_historical_version": {
    "accession": "E0N688",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MPG_NEIM3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E0N688\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Neisseriales\",\"Neisseriaceae\",\"Neisseria\"],\"scientificName\":\"Neisseria meningitidis serogroup B (strain ATCC 13091 / M2091)\",\"taxonId\":862513}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"Metalloprotease active against peptidoglycan\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"Outer membrane protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"OMP\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc metallopeptidase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc metalloprotease\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"Zinc-dependent metallopeptidase\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.17.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DD-carboxypeptidase/endopeptidase Mpg\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"There is a signal or a transmembrane region in the N-terminus of the pre-protein (Probable). Mature protein is probably associated with the cell outer membrane (PubMed:22046377)\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"id\":\"SL-0040\",\"value\":\"Cell outer membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"id\":\"GO:0009279\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cell outer membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang X.\",\"Yang X.\",\"Yang C.\",\"Wu Z.\",\"Xu H.\",\"Shen Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22046377\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0026845\"}],\"citationType\":\"journal article\",\"firstPage\":\"e26845\",\"id\":\"22046377\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e26845\",\"publicationDate\":\"2011\",\"title\":\"Crystal structure of outer membrane protein NMB0315 from Neisseria meningitidis.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3SLU\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 13091 / M2091\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL\",\"COFACTOR\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"PTM\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   MPG_NEIM3               Reviewed;         430 AA.\nAC   E0N688;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2010, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};\nDE            EC=3.4.17.- {ECO:0000250|UniProtKB:Q5F676};\nDE            EC=3.4.24.- {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Outer membrane protein {ECO:0000303|PubMed:22046377};\nDE            Short=OMP {ECO:0000303|PubMed:22046377};\nDE   AltName: Full=Zinc metallopeptidase {ECO:0000305};\nDE   AltName: Full=Zinc metalloprotease {ECO:0000305};\nDE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000303|PubMed:22046377};\nDE   Flags: Precursor;\nGN   ORFNames=HMPREF0602_0018 {ECO:0000312|EMBL:EFM05396.1};\nOS   Neisseria meningitidis serogroup B (strain ATCC 13091 / M2091).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;\nOC   Neisseriaceae; Neisseria.\nOX   NCBI_TaxID=862513;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:3SLU}\nRP   X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL,\nRP   COFACTOR, SUBUNIT, SUBCELLULAR LOCATION, AND PTM.\nRC   STRAIN=ATCC 13091 / M2091 {ECO:0000303|PubMed:22046377};\nRX   PubMed=22046377; DOI=10.1371/journal.pone.0026845;\nRA   Wang X., Yang X., Yang C., Wu Z., Xu H., Shen Y.;\nRT   \"Crystal structure of outer membrane protein NMB0315 from Neisseria\nRT   meningitidis.\";\nRL   PLoS ONE 6:e26845-e26845(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell outer membrane\nCC       {ECO:0000305|PubMed:22046377}. Note=There is a signal or a\nCC       transmembrane region in the N-terminus of the pre-protein (Probable).\nCC       Mature protein is probably associated with the cell outer membrane\nCC       (PubMed:22046377). {ECO:0000305|PubMed:22046377}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0009279; C:cell outer membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005694\nname: chromosome\nnamespace: cellular_component\ndef: \"A structure composed of a very long molecule of DNA and associated proteins (e.g. histones) that carries hereditary information.\" [ISBN:0198547684]\ncomment: Chromosomes include parts that are not part of the chromatin. Examples include the kinetochore.\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"chromatid\" RELATED []\nsynonym: \"interphase chromosome\" NARROW []\nsynonym: \"prophase chromosome\" NARROW []\nxref: Wikipedia:Chromosome\nis_a: GO:0043232 ! intracellular membraneless organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005694",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58583-58605",
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
  "excerpt": "[Term]\nid: GO:0009279\nname: cell outer membrane\nnamespace: cellular_component\ndef: \"A lipid bilayer that forms the outermost membrane of the cell envelope; enriched in polysaccharide and protein; the outer leaflet of the membrane contains specific lipopolysaccharide structures.\" [GOC:md, GOC:mtg_sensu, ISBN:0135712254]\ncomment: To annotate the plasma (cytoplasmic) membrane, see instead GO:0005886.\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsynonym: \"outer membrane of cell\" EXACT []\nis_a: GO:0019867 ! outer membrane\nis_a: GO:0030312 ! external encapsulating structure\nrelationship: part_of GO:0030313 ! cell envelope\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009279",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 94785-94797",
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
  "excerpt": "[Term]\nid: GO:0032993\nname: protein-DNA complex\nnamespace: cellular_component\ndef: \"A macromolecular complex containing both protein and DNA molecules.\" [GOC:mah]\ncomment: Note that this term is intended to classify complexes that have DNA as one of the members of the complex, that is, the complex does not exist if DNA is not present. Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here.\nsubset: goslim_pir\nsynonym: \"DNA-protein complex\" EXACT [GOC:mah]\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032993",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 192695-192704",
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
  "excerpt": "[Term]\nid: GO:0044615\nname: nuclear pore nuclear basket\nnamespace: cellular_component\ndef: \"A filamentous, cage-like assembly on the nuclear face of the nuclear pore complex (NPC). In S. cerevisiae, Mlp1p and Mlp2p are two major components of the NPC nuclear basket. In vertebrates, Tpr is a major component.\" [GOC:dgf, PMID:18046406, PMID:19524430, PMID:20947011, PMID:22419078]\nis_a: GO:0140513 ! nuclear protein-containing complex\nrelationship: part_of GO:0005643 ! nuclear pore\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044615",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 258897-258904",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
