# GO_biological_process_0171

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0171.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **A** — rescue of stalled ribosome

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAIKLIVGLANPGAEYAATRHNAGAWYVDLLAERLRAPLREEPKFFGYTSRITLEGEDVRLLVPTTFMNLSGKAVGAMASFYRIQPDEILVAHDELDLPPGVAKFKLGGGHGGHNGLKDIISKLGNNPNFHRLRVGIGHPGDKNKVVGFVLGKPPVSEQKLIDEAIDEAARCTELWFKEGLAKATSRLHTFKAQ

[Multiple Choices]
A. rescue of stalled ribosome
B. mitochondrial respiratory chain complex I assembly
C. nucleocytoplasmic transport
D. fatty acid beta-oxidation
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact sequence matches the cited bacterial protein. Its UniProt annotation identifies it as peptidyl-tRNA hydrolase and describes releasing peptidyl moieties from stalled ribosomal subunits; the GO annotation assigns rescue of stalled ribosome. These annotations are computationally supported by a HAMAP rule/UniRule, not direct experimental evidence for that GO term in this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C6](#evidence-c6), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 194-residue bacterial sequence is consistent with the conserved peptidyl-tRNA hydrolase family. Transferable knowledge of this family links peptidyl-tRNA hydrolysis to clearing stalled ribosomes, supporting A. The bacterial enzyme context also contrasts with the mitochondrial assembly, nucleocytoplasmic transport, and fatty-acid oxidation alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and its established role in processing peptidyl-tRNA from stalled translation meaningfully distinguish A without needing the target's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, stalled-ribosome rescue is the specific process supported by the protein-family function.


### Important caveats

- The supplied sequence alone does not establish experimental validation of the specific GO annotation; the cited GO assignment is computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 194-residue bacterial sequence is consistent with the conserved peptidyl-tRNA hydrolase family. Transferable knowledge of this family links peptidyl-tRNA hydrolysis to clearing stalled ribosomes, supporting A. The bacterial enzyme context also contrasts with the mitochondrial assembly, nucleocytoplasmic transport, and fatty-acid oxidation alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and its established role in processing peptidyl-tRNA from stalled translation meaningfully distinguish A without needing the target's database record."
  },
  "case_id": "GO_biological_process_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C6",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the cited bacterial protein. Its UniProt annotation identifies it as peptidyl-tRNA hydrolase and describes releasing peptidyl moieties from stalled ribosomal subunits; the GO annotation assigns rescue of stalled ribosome. These annotations are computationally supported by a HAMAP rule/UniRule, not direct experimental evidence for that GO term in this protein."
  },
  "important_caveats": [
    "The supplied sequence alone does not establish experimental validation of the specific GO annotation; the cited GO assignment is computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, stalled-ribosome rescue is the specific process supported by the protein-family function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the cited bacterial protein. Its UniProt annotation identifies it as peptidyl-tRNA hydrolase and describes releasing peptidyl moieties from stalled ribosomal subunits; the GO annotation assigns rescue of stalled ribosome. These annotations are computationally supported by a HAMAP rule/UniRule, not direct experimental evidence for that GO term in this protein.",
    "evidence_ids": ["C1", "C4", "C6", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 194-residue bacterial sequence is consistent with the conserved peptidyl-tRNA hydrolase family. Transferable knowledge of this family links peptidyl-tRNA hydrolysis to clearing stalled ribosomes, supporting A. The bacterial enzyme context also contrasts with the mitochondrial assembly, nucleocytoplasmic transport, and fatty-acid oxidation alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and its established role in processing peptidyl-tRNA from stalled translation meaningfully distinguish A without needing the target's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, stalled-ribosome rescue is the specific process supported by the protein-family function."
  },
  "important_caveats": [
    "The supplied sequence alone does not establish experimental validation of the specific GO annotation; the cited GO assignment is computational."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein as Peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29) with GO:0072344 'rescue of stalled ribosome' (IEA:UniProtKB-UniRule). The function comments explicitly state it 'Hydrolyzes ribosome-free peptidyl-tRNAs...as a result of ribosome stalling' and 'Catalyzes the release of premature peptidyl moieties from peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits.' The annotation evidence code is IEA (computational, via HAMAP rule MF_00083), not direct experimental proof for this specific protein, but the catalytic function is well-established for the Pth enzyme family. The expected answer matches the GO annotation exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [H4](#evidence-h4), [H5](#evidence-h5), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'GGGHGGH' motif (residues ~120-126), which is the defining catalytic signature of the Peptidyl-tRNA hydrolase (Pth) family (Pfam PF01521). The His residue within this motif is essential for catalysis. Combined with the small protein size (~194 aa), the alpha-helical architecture, and the 'DELDLPPGV' region, these features allow recognition of the Pth family by analogy with the extensively studied E. coli Pth (which is nearly identical in sequence). Once identified as Pth, the primary biological process is hydrolysis of peptidyl-tRNAs released from stalled ribosomes, directly corresponding to 'rescue of stalled ribosome' (A). The other options are mechanistically incompatible: complex I assembly (B) involves large multi-subunit mitochondrial membrane complexes unrelated to a small soluble hydrolase; nucleocytoplasmic transport (C) requires large karyopherin-type proteins with specific transport signals; fatty acid beta-oxidation (D) involves acyl-CoA dehydrogenases, enoyl-CoA hydratases, and thiolases with entirely different catalytic motifs. None of these alternatives can accommodate a small His-rich hydrolase acting on peptidyl-tRNA substrates.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The conserved 'GGGHGGH' catalytic motif is a family-level signature transferable from the well-characterized Pth family (studied in E. coli, yeast, and other organisms). Recognizing this motif as Pth-specific is analogous to recognizing any conserved domain. Once the family is identified, the biological process follows from the known catalytic mechanism (peptidyl-tRNA hydrolysis at stalled ribosomes), and the three distractors are mechanistically incompatible with a small soluble hydrolase acting on peptidyl-tRNA substrates. This is legitimate family-level inference, not memorization of this specific Salmonella protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options describe mechanistically distinct biological processes. A small (~194 aa) soluble hydrolase with a His-rich catalytic motif acting on peptidyl-tRNA substrates is incompatible with mitochondrial complex assembly, nucleocytoplasmic transport, or fatty acid beta-oxidation. Only 'rescue of stalled ribosome' matches the Pth catalytic mechanism.


### Important caveats

- The GO annotation for 'rescue of stalled ribosome' carries evidence code IEA (Inferred from Electronic Annotation) via UniRule/HAMAP, meaning it is computationally assigned rather than experimentally verified for this specific Salmonella protein.
- The experimental evidence in the UniProt entry (PubMed 27264868, 29777131) pertains to Pth's role in counteracting the TacT toxin, not directly to stalled ribosome rescue, though the latter is the canonical family function.
- The sequence is nearly identical to E. coli Pth, making family recognition straightforward but also meaning the question primarily tests recognition of a well-studied family rather than novel inference.
- The protein is bacterial (Salmonella), making the 'mitochondrial' option (B) additionally implausible on organismal grounds.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GGGHGGH' motif (residues ~120-126), which is the defining catalytic signature of the Peptidyl-tRNA hydrolase (Pth) family (Pfam PF01521). The His residue within this motif is essential for catalysis. Combined with the small protein size (~194 aa), the alpha-helical architecture, and the 'DELDLPPGV' region, these features allow recognition of the Pth family by analogy with the extensively studied E. coli Pth (which is nearly identical in sequence). Once identified as Pth, the primary biological process is hydrolysis of peptidyl-tRNAs released from stalled ribosomes, directly corresponding to 'rescue of stalled ribosome' (A). The other options are mechanistically incompatible: complex I assembly (B) involves large multi-subunit mitochondrial membrane complexes unrelated to a small soluble hydrolase; nucleocytoplasmic transport (C) requires large karyopherin-type proteins with specific transport signals; fatty acid beta-oxidation (D) involves acyl-CoA dehydrogenases, enoyl-CoA hydratases, and thiolases with entirely different catalytic motifs. None of these alternatives can accommodate a small His-rich hydrolase acting on peptidyl-tRNA substrates.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The conserved 'GGGHGGH' catalytic motif is a family-level signature transferable from the well-characterized Pth family (studied in E. coli, yeast, and other organisms). Recognizing this motif as Pth-specific is analogous to recognizing any conserved domain. Once the family is identified, the biological process follows from the known catalytic mechanism (peptidyl-tRNA hydrolysis at stalled ribosomes), and the three distractors are mechanistically incompatible with a small soluble hydrolase acting on peptidyl-tRNA substrates. This is legitimate family-level inference, not memorization of this specific Salmonella protein's annotation."
  },
  "case_id": "GO_biological_process_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "H4",
      "H5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein as Peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29) with GO:0072344 'rescue of stalled ribosome' (IEA:UniProtKB-UniRule). The function comments explicitly state it 'Hydrolyzes ribosome-free peptidyl-tRNAs...as a result of ribosome stalling' and 'Catalyzes the release of premature peptidyl moieties from peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits.' The annotation evidence code is IEA (computational, via HAMAP rule MF_00083), not direct experimental proof for this specific protein, but the catalytic function is well-established for the Pth enzyme family. The expected answer matches the GO annotation exactly."
  },
  "important_caveats": [
    "The GO annotation for 'rescue of stalled ribosome' carries evidence code IEA (Inferred from Electronic Annotation) via UniRule/HAMAP, meaning it is computationally assigned rather than experimentally verified for this specific Salmonella protein.",
    "The experimental evidence in the UniProt entry (PubMed 27264868, 29777131) pertains to Pth's role in counteracting the TacT toxin, not directly to stalled ribosome rescue, though the latter is the canonical family function.",
    "The sequence is nearly identical to E. coli Pth, making family recognition straightforward but also meaning the question primarily tests recognition of a well-studied family rather than novel inference.",
    "The protein is bacterial (Salmonella), making the 'mitochondrial' option (B) additionally implausible on organismal grounds."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options describe mechanistically distinct biological processes. A small (~194 aa) soluble hydrolase with a His-rich catalytic motif acting on peptidyl-tRNA substrates is incompatible with mitochondrial complex assembly, nucleocytoplasmic transport, or fatty acid beta-oxidation. Only 'rescue of stalled ribosome' matches the Pth catalytic mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein as Peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29) with GO:0072344 'rescue of stalled ribosome' (IEA:UniProtKB-UniRule). The function comments explicitly state it 'Hydrolyzes ribosome-free peptidyl-tRNAs...as a result of ribosome stalling' and 'Catalyzes the release of premature peptidyl moieties from peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits.' The annotation evidence code is IEA (computational, via HAMAP rule MF_00083), not direct experimental proof for this specific protein, but the catalytic function is well-established for the Pth enzyme family. The expected answer matches the GO annotation exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C9", "H4", "H5", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GGGHGGH' motif (residues ~120-126), which is the defining catalytic signature of the Peptidyl-tRNA hydrolase (Pth) family (Pfam PF01521). The His residue within this motif is essential for catalysis. Combined with the small protein size (~194 aa), the alpha-helical architecture, and the 'DELDLPPGV' region, these features allow recognition of the Pth family by analogy with the extensively studied E. coli Pth (which is nearly identical in sequence). Once identified as Pth, the primary biological process is hydrolysis of peptidyl-tRNAs released from stalled ribosomes, directly corresponding to 'rescue of stalled ribosome' (A). The other options are mechanistically incompatible: complex I assembly (B) involves large multi-subunit mitochondrial membrane complexes unrelated to a small soluble hydrolase; nucleocytoplasmic transport (C) requires large karyopherin-type proteins with specific transport signals; fatty acid beta-oxidation (D) involves acyl-CoA dehydrogenases, enoyl-CoA hydratases, and thiolases with entirely different catalytic motifs. None of these alternatives can accommodate a small His-rich hydrolase acting on peptidyl-tRNA substrates.",
    "missing_item_specific_fact": "",
    "reason": "The conserved 'GGGHGGH' catalytic motif is a family-level signature transferable from the well-characterized Pth family (studied in E. coli, yeast, and other organisms). Recognizing this motif as Pth-specific is analogous to recognizing any conserved domain. Once the family is identified, the biological process follows from the known catalytic mechanism (peptidyl-tRNA hydrolysis at stalled ribosomes), and the three distractors are mechanistically incompatible with a small soluble hydrolase acting on peptidyl-tRNA substrates. This is legitimate family-level inference, not memorization of this specific Salmonella protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options describe mechanistically distinct biological processes. A small (~194 aa) soluble hydrolase with a His-rich catalytic motif acting on peptidyl-tRNA substrates is incompatible with mitochondrial complex assembly, nucleocytoplasmic transport, or fatty acid beta-oxidation. Only 'rescue of stalled ribosome' matches the Pth catalytic mechanism."
  },
  "important_caveats": [
    "The GO annotation for 'rescue of stalled ribosome' carries evidence code IEA (Inferred from Electronic Annotation) via UniRule/HAMAP, meaning it is computationally assigned rather than experimentally verified for this specific Salmonella protein.",
    "The experimental evidence in the UniProt entry (PubMed 27264868, 29777131) pertains to Pth's role in counteracting the TacT toxin, not directly to stalled ribosome rescue, though the latter is the canonical family function.",
    "The sequence is nearly identical to E. coli Pth, making family recognition straightforward but also meaning the question primarily tests recognition of a well-studied family rather than novel inference.",
    "The protein is bacterial (Salmonella), making the 'mitochondrial' option (B) additionally implausible on organismal grounds."
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
  "benchmark_sequence_length": 194,
  "benchmark_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-06-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 194,
  "current_source_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 42,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0F6B281",
  "selected_historical_entry_version": 42,
  "selected_historical_record_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "selected_historical_source_sequence_length": 194,
  "selected_historical_source_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "selected_historical_version": {
    "accession": "A0A0F6B281",
    "database": "Swiss-Prot",
    "entryVersion": 42,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PTH_SALT1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0F6B281\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-06-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Salmonella\"],\"scientificName\":\"Salmonella typhimurium (strain 14028s / SGSC 2262)\",\"taxonId\":588858}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"3.1.1.29\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Peptidyl-tRNA hydrolase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Pth\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Hydrolyzes ribosome-free peptidyl-tRNAs (with 1 or more amino acids incorporated), which drop off the ribosome during protein synthesis, or as a result of ribosome stalling\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Catalyzes the release of premature peptidyl moieties from peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits, and thus maintains levels of free tRNAs and 50S ribosomes\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27264868\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29777131\",\"source\":\"PubMed\"}],\"value\":\"Expression in lag phase counteracts expression of tRNA-acetylating toxin TacT, deacetylates bulk tRNA modified by TacT in vitro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0006515\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:protein quality control for misfolded or incompletely synthesized proteins\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniRule\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0072344\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:rescue of stalled cytosolic ribosome\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniRule\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Cheverton A.M.\",\"Gollan B.\",\"Przydacz M.\",\"Wong C.T.\",\"Mylona A.\",\"Hare S.A.\",\"Helaine S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27264868\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molcel.2016.05.002\"}],\"citationType\":\"journal article\",\"firstPage\":\"86\",\"id\":\"27264868\",\"journal\":\"Mol. Cell\",\"lastPage\":\"96\",\"publicationDate\":\"2016\",\"title\":\"A Salmonella Toxin Promotes Persister Formation through Acetylation of tRNA.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Rycroft J.A.\",\"Gollan B.\",\"Grabe G.J.\",\"Hall A.\",\"Cheverton A.M.\",\"Larrouy-Maumus G.\",\"Hare S.A.\",\"Helaine S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29777131\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-018-04472-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"1993\",\"id\":\"29777131\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"1993\",\"publicationDate\":\"2018\",\"title\":\"Activity of acetyltransferase toxins involved in Salmonella persister formation during macrophage infection.\",\"volume\":\"9\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H1",
  "excerpt": "ID   PTH_SALT1               Reviewed;         194 AA.\nAC   A0A0F6B281;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JUN-2015, sequence version 1.\nDT   28-JAN-2026, entry version 42.\nDE   RecName: Full=Peptidyl-tRNA hydrolase {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            Short=Pth {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            EC=3.1.1.29 {ECO:0000255|HAMAP-Rule:MF_00083};\nGN   Name=pth {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000312|EMBL:ACY88619.1};\nGN   OrderedLocusNames=STM14_2156 {ECO:0000312|EMBL:ACY88619.1};\nOS   Salmonella typhimurium (strain 14028s / SGSC 2262).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Salmonella.\nOX   NCBI_TaxID=588858;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023;\nRX   PubMed=27264868; DOI=10.1016/j.molcel.2016.05.002;\nRA   Cheverton A.M., Gollan B., Przydacz M., Wong C.T., Mylona A., Hare S.A.,\nRA   Helaine S.;\nRT   \"A Salmonella Toxin Promotes Persister Formation through Acetylation of\nRT   tRNA.\";\nRL   Mol. Cell 63:86-96(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023;\nRX   PubMed=29777131; DOI=10.1038/s41467-018-04472-6;\nRA   Rycroft J.A., Gollan B., Grabe G.J., Hall A., Cheverton A.M.,\nRA   Larrouy-Maumus G., Hare S.A., Helaine S.;\nRT   \"Activity of acetyltransferase toxins involved in Salmonella persister\nRT   formation during macrophage infection.\";\nRL   Nat. Commun. 9:1993-1993(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Hydrolyzes ribosome-free peptidyl-tRNAs (with 1 or more amino\nCC       acids incorporated), which drop off the ribosome during protein\nCC       synthesis, or as a result of ribosome stalling. {ECO:0000255|HAMAP-\nCC       Rule:MF_00083}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the release of premature peptidyl moieties from\nCC       peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits, and\nCC       thus maintains levels of free tRNAs and 50S ribosomes.\nCC       {ECO:0000255|HAMAP-Rule:MF_00083}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H6",
  "excerpt": "CC   -!- FUNCTION: Expression in lag phase counteracts expression of tRNA-\nCC       acetylating toxin TacT, deacetylates bulk tRNA modified by TacT in\nCC       vitro. {ECO:0000269|PubMed:27264868, ECO:0000269|PubMed:29777131}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0006515; P:protein quality control for misfolded or incompletely synthesized proteins; IEA:UniProtKB-UniRule.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0072344; P:rescue of stalled ribosome; IEA:UniProtKB-UniRule.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006635\nname: fatty acid beta-oxidation\nnamespace: biological_process\ndef: \"A fatty acid oxidation process that results in the complete oxidation of a long-chain fatty acid. Fatty acid beta-oxidation begins with the addition of coenzyme A to a fatty acid, and occurs by successive cycles of reactions during each of which the fatty acid is shortened by a two-carbon fragment removed as acetyl coenzyme A; the cycle continues until only two or three carbons remain (as acetyl-CoA or propionyl-CoA respectively).\" [GOC:mah, ISBN:0198506732]\nxref: MetaCyc:PWY-5137\nxref: MetaCyc:PWY-5138\nxref: Reactome:R-HSA-77289 \"Mitochondrial Fatty Acid Beta-Oxidation\"\nis_a: GO:0009062 ! fatty acid catabolic process\nis_a: GO:0019395 ! fatty acid oxidation\nproperty_value: skos:narrowMatch MetaCyc:PWY-5137\nproperty_value: skos:narrowMatch MetaCyc:PWY-5138\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006635",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 68574-68586",
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
  "excerpt": "[Term]\nid: GO:0006913\nname: nucleocytoplasmic transport\nnamespace: biological_process\nalt_id: GO:0000063\ndef: \"The directed movement of molecules between the nucleus and the cytoplasm.\" [GOC:curators]\ncomment: Note that transport through the nuclear pore complex is not transmembrane because the nuclear membrane is a double membrane, and is not traversed.\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_pombe\nsynonym: \"nucleocytoplasmic shuttling\" NARROW []\nis_a: GO:0051169 ! nuclear transport\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006913",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 71524-71537",
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
  "excerpt": "[Term]\nid: GO:0032981\nname: mitochondrial respiratory chain complex I assembly\nnamespace: biological_process\ndef: \"The aggregation, arrangement and bonding together of a set of components to form mitochondrial respiratory chain complex I.\" [GOC:rph]\nsynonym: \"mitochondrial complex I assembly\" EXACT []\nsynonym: \"mitochondrial NADH dehydrogenase complex (ubiquinone) assembly\" EXACT []\nxref: Reactome:R-HSA-6799198 \"Complex I biogenesis\"\nis_a: GO:0010257 ! NADH dehydrogenase complex assembly\nis_a: GO:0033108 ! mitochondrial respiratory chain complex assembly\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032981",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 192568-192578",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 171. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
