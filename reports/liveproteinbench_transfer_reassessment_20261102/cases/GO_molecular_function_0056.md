# GO_molecular_function_0056

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0056.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — toxin activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MHALRSSVLALWLCLHVSVRAWMTYRSANGLDEYEPEDRIIFLGTKWCGNGNVAEGPEDLGPLKETDACCREHDMCPDLIAAGQSKHGLTNTASYTRLNCGCDEKFYNCLKNSAETGSGAVRFTYFTVLGTKCYRNEHPLICVKKGWFSCSKYELDKSQPKRYQWFDVSSNFAFPRMLT

[Multiple Choices]
A. phosphatidylcholine transfer activity
B. alpha-1,2-mannosyltransferase activity
C. acyltransferase activity, transferring groups other than amino-acyl groups
D. toxin activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches a venom-associated phospholipase A2 entry annotated with toxin activity. The annotation is computationally assigned, and the reported toxin-related effect is qualified as possible and partly based on an ortholog, so direct toxicity is not established conclusively. Still, the venom context and annotation support D among the offered choices. The reported catalytic reaction is hydrolysis, not acyl-group transfer, so it does not support C.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal peptide followed by a compact, cysteine-rich mature region consistent with secreted animal phospholipase A2 proteins, including venom PLA2s. Transferable knowledge of venom PLA2s makes toxin activity a credible choice. The other options describe phosphatidylcholine transport, glycan transfer, or acyl transfer; none fits a secreted PLA2-like sequence, and PLA2 hydrolysis is not acyltransferase activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and family-level pattern provide a meaningful, though probabilistic, basis for choosing D without needing the exact protein's database annotation. The sequence alone does not prove a toxin role, so the inference is not certain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The biochemical PLA2 activity itself is not offered. Of the listed choices, toxin activity is the defensible family-level role; the other options do not describe PLA2 hydrolysis.


### Important caveats

- The supplied annotations include computational evidence, and the reported toxin-related effect is qualified rather than an unambiguous direct demonstration of toxicity.
- The source-specific venom context was reviewer-only; the answerability judgment relies on transferable sequence and family knowledge, not that record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide followed by a compact, cysteine-rich mature region consistent with secreted animal phospholipase A2 proteins, including venom PLA2s. Transferable knowledge of venom PLA2s makes toxin activity a credible choice. The other options describe phosphatidylcholine transport, glycan transfer, or acyl transfer; none fits a secreted PLA2-like sequence, and PLA2 hydrolysis is not acyltransferase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level pattern provide a meaningful, though probabilistic, basis for choosing D without needing the exact protein's database annotation. The sequence alone does not prove a toxin role, so the inference is not certain."
  },
  "case_id": "GO_molecular_function_0056",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a venom-associated phospholipase A2 entry annotated with toxin activity. The annotation is computationally assigned, and the reported toxin-related effect is qualified as possible and partly based on an ortholog, so direct toxicity is not established conclusively. Still, the venom context and annotation support D among the offered choices. The reported catalytic reaction is hydrolysis, not acyl-group transfer, so it does not support C."
  },
  "important_caveats": [
    "The supplied annotations include computational evidence, and the reported toxin-related effect is qualified rather than an unambiguous direct demonstration of toxicity.",
    "The source-specific venom context was reviewer-only; the answerability judgment relies on transferable sequence and family knowledge, not that record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The biochemical PLA2 activity itself is not offered. Of the listed choices, toxin activity is the defensible family-level role; the other options do not describe PLA2 hydrolysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a venom-associated phospholipase A2 entry annotated with toxin activity. The annotation is computationally assigned, and the reported toxin-related effect is qualified as possible and partly based on an ortholog, so direct toxicity is not established conclusively. Still, the venom context and annotation support D among the offered choices. The reported catalytic reaction is hydrolysis, not acyl-group transfer, so it does not support C.",
    "evidence_ids": ["H2", "H3", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide followed by a compact, cysteine-rich mature region consistent with secreted animal phospholipase A2 proteins, including venom PLA2s. Transferable knowledge of venom PLA2s makes toxin activity a credible choice. The other options describe phosphatidylcholine transport, glycan transfer, or acyl transfer; none fits a secreted PLA2-like sequence, and PLA2 hydrolysis is not acyltransferase activity.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level pattern provide a meaningful, though probabilistic, basis for choosing D without needing the exact protein's database annotation. The sequence alone does not prove a toxin role, so the inference is not certain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The biochemical PLA2 activity itself is not offered. Of the listed choices, toxin activity is the defensible family-level role; the other options do not describe PLA2 hydrolysis."
  },
  "important_caveats": [
    "The supplied annotations include computational evidence, and the reported toxin-related effect is qualified rather than an unambiguous direct demonstration of toxicity.",
    "The source-specific venom context was reviewer-only; the answerability judgment relies on transferable sequence and family knowledge, not that record."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (P0DXZ6) annotates this protein with GO:0090729 (toxin activity, IEA:UniProtKB-KW) in addition to GO:0004623 (phospholipase A2 activity, IEA:UniProtKB-EC). The FUNCTION comment describes toxic effects: potentiating DRG activation, cell lysis, and pain behaviors. Among the four offered options, D is the only one actually annotated on this protein. Options A (phosphatidylcholine transfer), B (mannosyltransferase), and C (acyltransferase) are all mechanistically incompatible with a PLA2 hydrolase (EC 3.1.1.4). While the enzymatic activity (phospholipase A2) could be argued as more 'primary,' it is not among the choices, making D the best available answer.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H6](#evidence-h6), [H7](#evidence-h7), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmark PLA2 features: a signal peptide (MHALRSSVLALWLCLHVSVRAW), the conserved 'GTKWCG' and 'GTKCY' motifs, extensive cysteine pattern (~12 Cys forming disulfides typical of the ~140-residue mature PLA2 fold), and overall length (~179 aa precursor). Recognizing PLA2 from these features, a model can eliminate: (A) phosphatidylcholine transfer requires a lipid-binding pocket domain (e.g., START, PC-TP fold) for shuttling intact PC—PLA2 hydrolyzes PC, it does not transfer it; (B) alpha-1,2-mannosyltransferase is a glycosyltransferase with entirely different catalytic motifs and fold—no sequence resemblance; (C) acyltransferase (EC 2.3.1.-) transfers an acyl group to an acceptor molecule, whereas PLA2 is a hydrolase (EC 3.1.1.4) using water to cleave the ester bond—mechanistically distinct. This leaves D (toxin activity, GO:0090729), whose GO definition explicitly includes venom toxins (snake venom example). Venom PLA2s from Hymenoptera and other venomous animals are well-established examples of toxin activity in GO. The elimination is firm: A, B, C are mechanistically incompatible with any PLA2, regardless of whether the model can confirm venom origin from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the PLA2 fold from conserved sequence motifs (GTKWCG, cysteine spacing, signal peptide, length) combined with knowledge that PLA2 is a hydrolase (not a transferase or lipid-transfer protein) allows definitive elimination of A, B, and C. The GO definition of toxin activity explicitly encompasses venom proteins like PLA2. This is a family-level inference using transferable knowledge of PLA2 catalytic mechanism and GO annotation conventions for venom proteins, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are mechanistically incompatible with a PLA2 (hydrolase, not transferase; hydrolyzes PC, does not transfer it; not a glycosyltransferase). Only D is both annotated on the protein and mechanistically plausible for a venom PLA2. No ambiguity among the offered choices.


### Important caveats

- The primary enzymatic molecular function (phospholipase A2 activity, GO:0004623) is not offered as an option; the question forces selection among alternatives, making D the best available answer despite the enzyme activity being arguably more 'primary.'
- The toxin activity annotation uses IEA:UniProtKB-KW (keyword-based inference), not direct experimental evidence of toxic mechanism for this specific protein; the FUNCTION comment notes effects are inferred from the orthologous A. mellifera PLA2.
- The GO term GO:0015070 (obsolete toxin activity) was replaced by GO:0090729; the option text 'toxin activity' maps to both, but the current valid term is GO:0090729.
- The sequence alone does not unambiguously reveal the organism (Xylocopa aruana) or that this is specifically a venom-gland PLA2 rather than another secreted PLA2; however, the elimination of A, B, C does not require knowing the organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmark PLA2 features: a signal peptide (MHALRSSVLALWLCLHVSVRAW), the conserved 'GTKWCG' and 'GTKCY' motifs, extensive cysteine pattern (~12 Cys forming disulfides typical of the ~140-residue mature PLA2 fold), and overall length (~179 aa precursor). Recognizing PLA2 from these features, a model can eliminate: (A) phosphatidylcholine transfer requires a lipid-binding pocket domain (e.g., START, PC-TP fold) for shuttling intact PC—PLA2 hydrolyzes PC, it does not transfer it; (B) alpha-1,2-mannosyltransferase is a glycosyltransferase with entirely different catalytic motifs and fold—no sequence resemblance; (C) acyltransferase (EC 2.3.1.-) transfers an acyl group to an acceptor molecule, whereas PLA2 is a hydrolase (EC 3.1.1.4) using water to cleave the ester bond—mechanistically distinct. This leaves D (toxin activity, GO:0090729), whose GO definition explicitly includes venom toxins (snake venom example). Venom PLA2s from Hymenoptera and other venomous animals are well-established examples of toxin activity in GO. The elimination is firm: A, B, C are mechanistically incompatible with any PLA2, regardless of whether the model can confirm venom origin from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PLA2 fold from conserved sequence motifs (GTKWCG, cysteine spacing, signal peptide, length) combined with knowledge that PLA2 is a hydrolase (not a transferase or lipid-transfer protein) allows definitive elimination of A, B, and C. The GO definition of toxin activity explicitly encompasses venom proteins like PLA2. This is a family-level inference using transferable knowledge of PLA2 catalytic mechanism and GO annotation conventions for venom proteins, not a lookup of this specific protein's record."
  },
  "case_id": "GO_molecular_function_0056",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H6",
      "H7",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXZ6) annotates this protein with GO:0090729 (toxin activity, IEA:UniProtKB-KW) in addition to GO:0004623 (phospholipase A2 activity, IEA:UniProtKB-EC). The FUNCTION comment describes toxic effects: potentiating DRG activation, cell lysis, and pain behaviors. Among the four offered options, D is the only one actually annotated on this protein. Options A (phosphatidylcholine transfer), B (mannosyltransferase), and C (acyltransferase) are all mechanistically incompatible with a PLA2 hydrolase (EC 3.1.1.4). While the enzymatic activity (phospholipase A2) could be argued as more 'primary,' it is not among the choices, making D the best available answer."
  },
  "important_caveats": [
    "The primary enzymatic molecular function (phospholipase A2 activity, GO:0004623) is not offered as an option; the question forces selection among alternatives, making D the best available answer despite the enzyme activity being arguably more 'primary.'",
    "The toxin activity annotation uses IEA:UniProtKB-KW (keyword-based inference), not direct experimental evidence of toxic mechanism for this specific protein; the FUNCTION comment notes effects are inferred from the orthologous A. mellifera PLA2.",
    "The GO term GO:0015070 (obsolete toxin activity) was replaced by GO:0090729; the option text 'toxin activity' maps to both, but the current valid term is GO:0090729.",
    "The sequence alone does not unambiguously reveal the organism (Xylocopa aruana) or that this is specifically a venom-gland PLA2 rather than another secreted PLA2; however, the elimination of A, B, C does not require knowing the organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are mechanistically incompatible with a PLA2 (hydrolase, not transferase; hydrolyzes PC, does not transfer it; not a glycosyltransferase). Only D is both annotated on the protein and mechanistically plausible for a venom PLA2. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXZ6) annotates this protein with GO:0090729 (toxin activity, IEA:UniProtKB-KW) in addition to GO:0004623 (phospholipase A2 activity, IEA:UniProtKB-EC). The FUNCTION comment describes toxic effects: potentiating DRG activation, cell lysis, and pain behaviors. Among the four offered options, D is the only one actually annotated on this protein. Options A (phosphatidylcholine transfer), B (mannosyltransferase), and C (acyltransferase) are all mechanistically incompatible with a PLA2 hydrolase (EC 3.1.1.4). While the enzymatic activity (phospholipase A2) could be argued as more 'primary,' it is not among the choices, making D the best available answer.",
    "evidence_ids": ["C5", "C7", "H3", "H6", "H7", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmark PLA2 features: a signal peptide (MHALRSSVLALWLCLHVSVRAW), the conserved 'GTKWCG' and 'GTKCY' motifs, extensive cysteine pattern (~12 Cys forming disulfides typical of the ~140-residue mature PLA2 fold), and overall length (~179 aa precursor). Recognizing PLA2 from these features, a model can eliminate: (A) phosphatidylcholine transfer requires a lipid-binding pocket domain (e.g., START, PC-TP fold) for shuttling intact PC—PLA2 hydrolyzes PC, it does not transfer it; (B) alpha-1,2-mannosyltransferase is a glycosyltransferase with entirely different catalytic motifs and fold—no sequence resemblance; (C) acyltransferase (EC 2.3.1.-) transfers an acyl group to an acceptor molecule, whereas PLA2 is a hydrolase (EC 3.1.1.4) using water to cleave the ester bond—mechanistically distinct. This leaves D (toxin activity, GO:0090729), whose GO definition explicitly includes venom toxins (snake venom example). Venom PLA2s from Hymenoptera and other venomous animals are well-established examples of toxin activity in GO. The elimination is firm: A, B, C are mechanistically incompatible with any PLA2, regardless of whether the model can confirm venom origin from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PLA2 fold from conserved sequence motifs (GTKWCG, cysteine spacing, signal peptide, length) combined with knowledge that PLA2 is a hydrolase (not a transferase or lipid-transfer protein) allows definitive elimination of A, B, and C. The GO definition of toxin activity explicitly encompasses venom proteins like PLA2. This is a family-level inference using transferable knowledge of PLA2 catalytic mechanism and GO annotation conventions for venom proteins, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are mechanistically incompatible with a PLA2 (hydrolase, not transferase; hydrolyzes PC, does not transfer it; not a glycosyltransferase). Only D is both annotated on the protein and mechanistically plausible for a venom PLA2. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The primary enzymatic molecular function (phospholipase A2 activity, GO:0004623) is not offered as an option; the question forces selection among alternatives, making D the best available answer despite the enzyme activity being arguably more 'primary.'",
    "The toxin activity annotation uses IEA:UniProtKB-KW (keyword-based inference), not direct experimental evidence of toxic mechanism for this specific protein; the FUNCTION comment notes effects are inferred from the orthologous A. mellifera PLA2.",
    "The GO term GO:0015070 (obsolete toxin activity) was replaced by GO:0090729; the option text 'toxin activity' maps to both, but the current valid term is GO:0090729.",
    "The sequence alone does not unambiguously reveal the organism (Xylocopa aruana) or that this is specifically a venom-gland PLA2 rather than another secreted PLA2; however, the elimination of A, B, C does not require knowing the organism."
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
  "benchmark_sequence_length": 179,
  "benchmark_sequence_sha256": "50594be59aa7852dcdccd4fd13825b239fed46dff2ce31a488ef868edb881b3b",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 179,
  "current_source_sequence_sha256": "50594be59aa7852dcdccd4fd13825b239fed46dff2ce31a488ef868edb881b3b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXZ6",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "selected_historical_source_sequence_length": 179,
  "selected_historical_source_sequence_sha256": "50594be59aa7852dcdccd4fd13825b239fed46dff2ce31a488ef868edb881b3b",
  "selected_historical_version": {
    "accession": "P0DXZ6",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PA2_XYLAR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXZ6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Great carpenter bee\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Hymenoptera\",\"Apocrita\",\"Aculeata\",\"Apoidea\",\"Anthophila\",\"Apidae\",\"Xylocopa\",\"Koptortosoma\"],\"scientificName\":\"Xylocopa aruana\",\"taxonId\":135674}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Phosphatidylcholine 2-acylhydrolase\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00630\",\"source\":\"UniProtKB\"}],\"value\":\"3.1.1.4\"}],\"fullName\":{\"value\":\"Phospholipase A2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PA2\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36550366\",\"source\":\"PubMed\"}],\"value\":\"PLA2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36550366\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"May potentiate Xylotoxin(1)-Xa1a DRG activation and cell lysis, since the orthologous A.mellifera PA2 potentiates Xylotoxin(1)-Xa1a DRG activation and cell lysis. In vivo, intraplantar injection in mice may potentiate spontaneous pain behaviors and paw swelling caused by Xylotoxin(1)-Xa1a, since the orthologous A.mellifera PA2 shows this effect (PubMed:36550366). PLA2 catalyzes the calcium-dependent hydrolysis of the 2-acyl groups in 3-sn-phosphoglycerides (Probable)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.1.1.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10035\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:15801\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28868\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57643\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58168\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004623\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:A2-type glycerophospholipase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-EC\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Shi N.\",\"Szanto T.G.\",\"He J.\",\"Schroeder C.I.\",\"Walker A.A.\",\"Deuis J.R.\",\"Vetter I.\",\"Panyi G.\",\"King G.F.\",\"Robinson S.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36550366\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41598-022-26867-8\"}],\"citationType\":\"journal article\",\"firstPage\":\"22168\",\"id\":\"36550366\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"22168\",\"publicationDate\":\"2022\",\"title\":\"Venom composition and pain-causing toxins of the Australian great carpenter bee Xylocopa aruana.\",\"volume\":\"12\"},\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Venom\"},{\"type\":\"TISSUE\",\"value\":\"Venom gland\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"IDENTIFICATION BY MASS SPECTROMETRY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:59.679483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   PA2_XYLAR               Reviewed;         179 AA.\nAC   P0DXZ6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Phospholipase A2;\nDE            Short=PA2 {ECO:0000305};\nDE            Short=PLA2 {ECO:0000303|PubMed:36550366};\nDE            EC=3.1.1.4 {ECO:0000250|UniProtKB:P00630};\nDE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;\nDE   Flags: Precursor;\nOS   Xylocopa aruana (Great carpenter bee).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Hymenoptera; Apocrita; Aculeata; Apoidea;\nOC   Anthophila; Apidae; Xylocopa; Koptortosoma.\nOX   NCBI_TaxID=135674;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], IDENTIFICATION BY MASS SPECTROMETRY, AND\nRP   SUBCELLULAR LOCATION.\nRC   TISSUE=Venom, and Venom gland;\nRX   PubMed=36550366; DOI=10.1038/s41598-022-26867-8;\nRA   Shi N., Szanto T.G., He J., Schroeder C.I., Walker A.A., Deuis J.R.,\nRA   Vetter I., Panyi G., King G.F., Robinson S.D.;\nRT   \"Venom composition and pain-causing toxins of the Australian great\nRT   carpenter bee Xylocopa aruana.\";\nRL   Sci. Rep. 12:22168-22168(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: May potentiate Xylotoxin(1)-Xa1a DRG activation and cell\nCC       lysis, since the orthologous A.mellifera PA2 potentiates Xylotoxin(1)-\nCC       Xa1a DRG activation and cell lysis. In vivo, intraplantar injection in\nCC       mice may potentiate spontaneous pain behaviors and paw swelling caused\nCC       by Xylotoxin(1)-Xa1a, since the orthologous A.mellifera PA2 shows this\nCC       effect (PubMed:36550366). PLA2 catalyzes the calcium-dependent\nCC       hydrolysis of the 2-acyl groups in 3-sn-phosphoglycerides (Probable).\nCC       {ECO:0000269|PubMed:36550366, ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-\nCC         glycero-3-phosphocholine + a fatty acid + H(+); Xref=Rhea:RHEA:15801,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:28868,\nCC         ChEBI:CHEBI:57643, ChEBI:CHEBI:58168; EC=3.1.1.4;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10035};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0004623; F:phospholipase A2 activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0090729; F:toxin activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:01.445083+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a",
  "url": "https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000026\nname: alpha-1,2-mannosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a mannose residue to an oligosaccharide, forming an alpha-(1->2) linkage.\" [GOC:mcc, PMID:10521541]\nxref: Reactome:R-HSA-446187 \"ALG11 transfers the fourth and fifth Man to the N-glycan precursor\"\nxref: Reactome:R-HSA-446215 \"ALG9 transfers Man to N-glycan precursor (GlcNAc)2 (Man)6 (PP-Dol)1\"\nxref: Reactome:R-HSA-446216 \"ALG9 transfers Man to N-glycan precursor (GlcNAc)2 (Man)8 (PP-Dol)1\"\nxref: Reactome:R-HSA-4551297 \"Defective ALG11 does not transfer Man to the N-glycan precursor\"\nxref: Reactome:R-HSA-4720478 \"Defective ALG9 does not add the seventh mannose to the N-glycan precursor\"\nxref: Reactome:R-HSA-9035514 \"Defective ALG9 does not add the last mannose to the N-glycan precursor\"\nis_a: GO:0000030 ! mannosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000026",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 282-294",
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
  "excerpt": "[Term]\nid: GO:0015070\nname: obsolete toxin activity\nnamespace: molecular_function\ndef: \"OBSOLETE. Acts as to cause injury to other living organisms.\" [GOC:jl]\ncomment: This term was made obsolete because it represents a classification of molecules and not a molecular function.\nsynonym: \"toxin activity\" EXACT []\nis_obsolete: true\nconsider: GO:0090729\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015070",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 114261-114270",
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
  "excerpt": "[Term]\nid: GO:0016747\nname: acyltransferase activity, transferring groups other than amino-acyl groups\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of an acyl group, other than amino-acyl, from one compound (donor) to another (acceptor).\" [EC:2.3.1.-]\nsynonym: \"transferase activity, transferring acyl groups other than amino-acyl groups\" EXACT []\nsynonym: \"transferase activity, transferring groups other than amino-acyl groups\" RELATED [EC:2.3.1.-]\nxref: EC:2.3.1.-\nxref: Reactome:R-HSA-9859163 \"DBT transfers BCAA to CoA\"\nxref: Reactome:R-HSA-9865115 \"DBT loss-of-function mutants don't synthesize BCAA-CoA\"\nis_a: GO:0016746 ! acyltransferase activity\nproperty_value: skos:exactMatch EC:2.3.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016747",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129733-129745",
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
  "excerpt": "[Term]\nid: GO:0090729\nname: toxin activity\nnamespace: molecular_function\nalt_id: GO:0050827\ndef: \"Interacting selectively with one or more biological molecules in another (target) organism, initiating pathogenesis (leading to an abnormal, generally detrimental state) in the target organism. The activity should refer to an evolved function of the active gene product, i.e. one that was selected for. Examples include the activity of botulinum toxin, and snake venom.\" [GOC:pt]\nsubset: goslim_generic\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsynonym: \"toxin receptor binding\" EXACT []\nxref: Wikipedia:Toxin\nis_a: GO:0003674 ! molecular_function\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0090729",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 401379-401391",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0120019\nname: phosphatidylcholine transfer activity\nnamespace: molecular_function\ndef: \"Removes phosphatidylcholine from a membrane or a monolayer lipid particle, transports it through the aqueous phase while protected in a hydrophobic pocket, and brings it to an acceptor membrane or lipid particle.\" [GOC:krc, PMID:20823909, PMID:24220498, PMID:25797198]\nsynonym: \"intermembrane phosphatidylcholine transfer activity\" NARROW []\nsynonym: \"phosphatidylcholine carrier activity\" EXACT []\nxref: Reactome:R-HSA-1483087 \"PI is exchanged with PC by PITPNB\"\nxref: Reactome:R-HSA-1483211 \"PC:PITPNB is transported from the Golgi membrane to the ER membrane\"\nxref: Reactome:R-HSA-1483219 \"PC is exchanged with PI by PITPNB\"\nxref: Reactome:R-HSA-9956308 \"STARD7 transports PC from ER membrane to mitochondrial outer membrane\"\nis_a: GO:0120014 ! phospholipid transfer activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0120019",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 432286-432298",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 56. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
