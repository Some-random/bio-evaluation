# GO_molecular_function_0015

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0015.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — exo-alpha-sialidase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEPSKLFTISDNATFAPGPVINVADKKTFRTCFRILVLSVQAVTLILVIVNLGELVRMINDQGLSNQLSSITDKIRESANMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTSKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYISTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. exo-alpha-sialidase activity
B. ribosome binding
C. zinc ion transmembrane transporter activity
D. misfolded protein binding
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

> The sequence-matched UniProt record assigns hemagglutinin-neuraminidase and EC 3.2.1.18, and describes hydrolysis of terminal sialic-acid linkages, supporting exo-alpha-sialidase activity. The function evidence is transferred by similarity rather than direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a short N-terminal hydrophobic membrane anchor followed by a long globular ectodomain, a pattern compatible with viral hemagglutinin-neuraminidase proteins. Transferable knowledge of this protein family connects its neuraminidase activity to sialic-acid cleavage, making A a meaningful choice over ribosome binding, zinc transport, or misfolded-protein binding. This is a family-level inference, not a claim of certainty from architecture alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence architecture and recognizable viral glycoprotein-family pattern provide a credible basis for choosing A without needing this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, sialidase activity is the plausible function for a hemagglutinin-neuraminidase-like sequence; the alternatives describe unrelated activities.


### Important caveats

- The supplied functional annotations are similarity-based, so they support the expected answer but should not be described as direct experimental confirmation for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a short N-terminal hydrophobic membrane anchor followed by a long globular ectodomain, a pattern compatible with viral hemagglutinin-neuraminidase proteins. Transferable knowledge of this protein family connects its neuraminidase activity to sialic-acid cleavage, making A a meaningful choice over ribosome binding, zinc transport, or misfolded-protein binding. This is a family-level inference, not a claim of certainty from architecture alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and recognizable viral glycoprotein-family pattern provide a credible basis for choosing A without needing this exact protein's database annotation."
  },
  "case_id": "GO_molecular_function_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7",
      "C8",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns hemagglutinin-neuraminidase and EC 3.2.1.18, and describes hydrolysis of terminal sialic-acid linkages, supporting exo-alpha-sialidase activity. The function evidence is transferred by similarity rather than direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied functional annotations are similarity-based, so they support the expected answer but should not be described as direct experimental confirmation for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, sialidase activity is the plausible function for a hemagglutinin-neuraminidase-like sequence; the alternatives describe unrelated activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns hemagglutinin-neuraminidase and EC 3.2.1.18, and describes hydrolysis of terminal sialic-acid linkages, supporting exo-alpha-sialidase activity. The function evidence is transferred by similarity rather than direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C7", "C8", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a short N-terminal hydrophobic membrane anchor followed by a long globular ectodomain, a pattern compatible with viral hemagglutinin-neuraminidase proteins. Transferable knowledge of this protein family connects its neuraminidase activity to sialic-acid cleavage, making A a meaningful choice over ribosome binding, zinc transport, or misfolded-protein binding. This is a family-level inference, not a claim of certainty from architecture alone.",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and recognizable viral glycoprotein-family pattern provide a credible basis for choosing A without needing this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, sialidase activity is the plausible function for a hemagglutinin-neuraminidase-like sequence; the alternatives describe unrelated activities."
  },
  "important_caveats": [
    "The supplied functional annotations are similarity-based, so they support the expected answer but should not be described as direct experimental confirmation for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5SC51 (Hemagglutinin-neuraminidase, Mumps virus) is annotated with EC 3.2.1.18 and GO:0004308 (exo-alpha-sialidase activity). The catalytic activity is described as hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)-glycosidic linkages of terminal sialic acid residues. The GO annotation evidence code is ISS (Inferred from Sequence Similarity, based on related paramyxovirus HN proteins like Q9WAF5), which is a well-established computational inference for this protein family. The function comment confirms neuraminidase activity ensures efficient viral spread by dissociating virions from sialic acid-containing glycoproteins.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmark features of a paramyxovirus-type surface glycoprotein: (1) N-terminal hydrophobic signal peptide followed by a type I membrane protein topology (extracellular domain, single transmembrane helix near C-terminus), (2) multiple N-glycosylation sequons (NxS/T motifs), (3) cysteine-rich regions consistent with viral envelope glycoprotein disulfide bonding, (4) total length ~582 aa consistent with paramyxovirus HN proteins. Transferable knowledge from the paramyxovirus HN family (NDV HN, measles HN, parainfluenza HN, mumps HN) establishes that these proteins possess neuraminidase (sialidase, EC 3.2.1.18) activity in addition to hemagglutination. The catalytic R-Y-K triad and conserved active-site motifs (e.g., the 'WATLVPGVGSGIYFENKLIFPAYGG' region) are recognizable family signatures. Among the four options: ribosome binding (B) is a function of ribosomal/translation proteins, not viral envelope glycoproteins; zinc ion transmembrane transporter (C) requires specific ZIP/ZnT motifs and multi-pass topology incompatible with a type I viral glycoprotein; misfolded protein binding (D) is a chaperone function (HSP70/90 family). Exo-alpha-sialidase activity (A) is the only molecular function consistent with a sialic-acid-interacting viral surface glycoprotein, a well-known family-level property shared across multiple viral families (paramyxovirus HN, influenza NA, coronavirus HE).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence topology, length, glycosylation pattern, and cysteine distribution allow recognition as a paramyxovirus-type surface glycoprotein. Family-level knowledge that paramyxovirus HN proteins possess neuraminidase/sialidase activity (EC 3.2.1.18) is well-established across multiple characterized members (NDV, measles, parainfluenza). The three distractors (ribosome binding, zinc transporter, misfolded protein binding) are mechanistically incompatible with a viral envelope glycoprotein, making A the only viable choice through elimination and family-level functional assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (ribosome binding, zinc ion transmembrane transporter, misfolded protein binding) describe functions of entirely different protein classes (ribosomal proteins, metal transporters, molecular chaperones) that are mechanistically and topologically incompatible with a viral surface glycoprotein. Only exo-alpha-sialidase activity is consistent with the identified protein class.


### Important caveats

- The GO annotation for this protein carries evidence code ISS (Inferred from Sequence Similarity), meaning the sialidase assignment is transferred from characterized homologs (e.g., NDV HN Q9WAF5) rather than directly measured for this exact mumps HN variant.
- The reviewer-only evidence confirms the protein is Mumps virus HN (Q5SC51), but this identification was not provided to the evaluated model; the reasoning must rely on sequence-level family recognition.
- The sequence contains features consistent with paramyxovirus HN proteins, but absolute certainty of family assignment from sequence alone without BLAST/homology tools would require careful motif analysis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmark features of a paramyxovirus-type surface glycoprotein: (1) N-terminal hydrophobic signal peptide followed by a type I membrane protein topology (extracellular domain, single transmembrane helix near C-terminus), (2) multiple N-glycosylation sequons (NxS/T motifs), (3) cysteine-rich regions consistent with viral envelope glycoprotein disulfide bonding, (4) total length ~582 aa consistent with paramyxovirus HN proteins. Transferable knowledge from the paramyxovirus HN family (NDV HN, measles HN, parainfluenza HN, mumps HN) establishes that these proteins possess neuraminidase (sialidase, EC 3.2.1.18) activity in addition to hemagglutination. The catalytic R-Y-K triad and conserved active-site motifs (e.g., the 'WATLVPGVGSGIYFENKLIFPAYGG' region) are recognizable family signatures. Among the four options: ribosome binding (B) is a function of ribosomal/translation proteins, not viral envelope glycoproteins; zinc ion transmembrane transporter (C) requires specific ZIP/ZnT motifs and multi-pass topology incompatible with a type I viral glycoprotein; misfolded protein binding (D) is a chaperone function (HSP70/90 family). Exo-alpha-sialidase activity (A) is the only molecular function consistent with a sialic-acid-interacting viral surface glycoprotein, a well-known family-level property shared across multiple viral families (paramyxovirus HN, influenza NA, coronavirus HE).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence topology, length, glycosylation pattern, and cysteine distribution allow recognition as a paramyxovirus-type surface glycoprotein. Family-level knowledge that paramyxovirus HN proteins possess neuraminidase/sialidase activity (EC 3.2.1.18) is well-established across multiple characterized members (NDV, measles, parainfluenza). The three distractors (ribosome binding, zinc transporter, misfolded protein binding) are mechanistically incompatible with a viral envelope glycoprotein, making A the only viable choice through elimination and family-level functional assignment."
  },
  "case_id": "GO_molecular_function_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5SC51 (Hemagglutinin-neuraminidase, Mumps virus) is annotated with EC 3.2.1.18 and GO:0004308 (exo-alpha-sialidase activity). The catalytic activity is described as hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)-glycosidic linkages of terminal sialic acid residues. The GO annotation evidence code is ISS (Inferred from Sequence Similarity, based on related paramyxovirus HN proteins like Q9WAF5), which is a well-established computational inference for this protein family. The function comment confirms neuraminidase activity ensures efficient viral spread by dissociating virions from sialic acid-containing glycoproteins."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code ISS (Inferred from Sequence Similarity), meaning the sialidase assignment is transferred from characterized homologs (e.g., NDV HN Q9WAF5) rather than directly measured for this exact mumps HN variant.",
    "The reviewer-only evidence confirms the protein is Mumps virus HN (Q5SC51), but this identification was not provided to the evaluated model; the reasoning must rely on sequence-level family recognition.",
    "The sequence contains features consistent with paramyxovirus HN proteins, but absolute certainty of family assignment from sequence alone without BLAST/homology tools would require careful motif analysis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (ribosome binding, zinc ion transmembrane transporter, misfolded protein binding) describe functions of entirely different protein classes (ribosomal proteins, metal transporters, molecular chaperones) that are mechanistically and topologically incompatible with a viral surface glycoprotein. Only exo-alpha-sialidase activity is consistent with the identified protein class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5SC51 (Hemagglutinin-neuraminidase, Mumps virus) is annotated with EC 3.2.1.18 and GO:0004308 (exo-alpha-sialidase activity). The catalytic activity is described as hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)-glycosidic linkages of terminal sialic acid residues. The GO annotation evidence code is ISS (Inferred from Sequence Similarity, based on related paramyxovirus HN proteins like Q9WAF5), which is a well-established computational inference for this protein family. The function comment confirms neuraminidase activity ensures efficient viral spread by dissociating virions from sialic acid-containing glycoproteins.",
    "evidence_ids": ["C4", "C6", "C7", "C8", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmark features of a paramyxovirus-type surface glycoprotein: (1) N-terminal hydrophobic signal peptide followed by a type I membrane protein topology (extracellular domain, single transmembrane helix near C-terminus), (2) multiple N-glycosylation sequons (NxS/T motifs), (3) cysteine-rich regions consistent with viral envelope glycoprotein disulfide bonding, (4) total length ~582 aa consistent with paramyxovirus HN proteins. Transferable knowledge from the paramyxovirus HN family (NDV HN, measles HN, parainfluenza HN, mumps HN) establishes that these proteins possess neuraminidase (sialidase, EC 3.2.1.18) activity in addition to hemagglutination. The catalytic R-Y-K triad and conserved active-site motifs (e.g., the 'WATLVPGVGSGIYFENKLIFPAYGG' region) are recognizable family signatures. Among the four options: ribosome binding (B) is a function of ribosomal/translation proteins, not viral envelope glycoproteins; zinc ion transmembrane transporter (C) requires specific ZIP/ZnT motifs and multi-pass topology incompatible with a type I viral glycoprotein; misfolded protein binding (D) is a chaperone function (HSP70/90 family). Exo-alpha-sialidase activity (A) is the only molecular function consistent with a sialic-acid-interacting viral surface glycoprotein, a well-known family-level property shared across multiple viral families (paramyxovirus HN, influenza NA, coronavirus HE).",
    "missing_item_specific_fact": "",
    "reason": "The sequence topology, length, glycosylation pattern, and cysteine distribution allow recognition as a paramyxovirus-type surface glycoprotein. Family-level knowledge that paramyxovirus HN proteins possess neuraminidase/sialidase activity (EC 3.2.1.18) is well-established across multiple characterized members (NDV, measles, parainfluenza). The three distractors (ribosome binding, zinc transporter, misfolded protein binding) are mechanistically incompatible with a viral envelope glycoprotein, making A the only viable choice through elimination and family-level functional assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (ribosome binding, zinc ion transmembrane transporter, misfolded protein binding) describe functions of entirely different protein classes (ribosomal proteins, metal transporters, molecular chaperones) that are mechanistically and topologically incompatible with a viral surface glycoprotein. Only exo-alpha-sialidase activity is consistent with the identified protein class."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code ISS (Inferred from Sequence Similarity), meaning the sialidase assignment is transferred from characterized homologs (e.g., NDV HN Q9WAF5) rather than directly measured for this exact mumps HN variant.",
    "The reviewer-only evidence confirms the protein is Mumps virus HN (Q5SC51), but this identification was not provided to the evaluated model; the reasoning must rely on sequence-level family recognition.",
    "The sequence contains features consistent with paramyxovirus HN proteins, but absolute certainty of family assignment from sequence alone without BLAST/homology tools would require careful motif analysis."
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
  "benchmark_sequence_length": 582,
  "benchmark_sequence_sha256": "e96cff28d63a847ba629b286f3a32c333c53ea1cb31fc62f1e0624df41dc039e",
  "current_entry_audit": {
    "entryVersion": 107,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-12-21",
    "sequenceVersion": 1
  },
  "current_record_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 582,
  "current_source_sequence_sha256": "e96cff28d63a847ba629b286f3a32c333c53ea1cb31fc62f1e0624df41dc039e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 105,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5SC51",
  "selected_historical_entry_version": 105,
  "selected_historical_record_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "selected_historical_source_sequence_length": 582,
  "selected_historical_source_sequence_sha256": "e96cff28d63a847ba629b286f3a32c333c53ea1cb31fc62f1e0624df41dc039e",
  "selected_historical_version": {
    "accession": "Q5SC51",
    "database": "Swiss-Prot",
    "entryVersion": 105,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HN_MUMPZ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5SC51\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":107,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-12-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype N (strain L-Zagreb vaccine)\",\"taxonId\":301186}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9WAF5\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.18\"}],\"fullName\":{\"value\":\"Hemagglutinin-neuraminidase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q786F2\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9WAF5\",\"source\":\"UniProtKB\"}],\"value\":\"Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection (By similarity). Binding of HN protein to the receptor induces a conformational change that allows the F protein to trigger virion/cell membranes fusion (By similarity). Binds to the glycan motifs sialyl Lewis (SLe) and GM2 ganglioside (GM2-glycan) (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q91UL0\",\"source\":\"UniProtKB\"}],\"value\":\"Neuraminidase activity ensures the efficient spread of the virus by dissociating the mature virions from the neuraminic acid containing glycoproteins\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9WAF5\",\"source\":\"UniProtKB\"}],\"name\":\"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004308\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:exo-alpha-sialidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0046789\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:host cell surface receptor binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0042802\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:identical protein binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:31:29.846842+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC51.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H1",
  "excerpt": "ID   HN_MUMPZ                Reviewed;         582 AA.\nAC   Q5SC51;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-DEC-2004, sequence version 1.\nDT   28-JAN-2026, entry version 105.\nDE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000250|UniProtKB:Q9WAF5};\nGN   Name=HN;\nOS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=301186;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H2",
  "excerpt": "CC   -!- FUNCTION: Attaches the virus to alpha-2,3-linked sialic acid-containing\nCC       cell receptors and thereby initiating infection (By similarity).\nCC       Binding of HN protein to the receptor induces a conformational change\nCC       that allows the F protein to trigger virion/cell membranes fusion (By\nCC       similarity). Binds to the glycan motifs sialyl Lewis (SLe) and GM2\nCC       ganglioside (GM2-glycan) (By similarity).\nCC       {ECO:0000250|UniProtKB:Q786F2, ECO:0000250|UniProtKB:Q9WAF5}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Neuraminidase activity ensures the efficient spread of the\nCC       virus by dissociating the mature virions from the neuraminic acid\nCC       containing glycoproteins. {ECO:0000250|UniProtKB:Q91UL0}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-\nCC         (2->8)- glycosidic linkages of terminal sialic acid residues in\nCC         oligosaccharides, glycoproteins, glycolipids, colominic acid and\nCC         synthetic substrates.; EC=3.2.1.18;\nCC         Evidence={ECO:0000250|UniProtKB:Q9WAF5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0004308; F:exo-alpha-sialidase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0046789; F:host cell surface receptor binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0042802; F:identical protein binding; IEA:UniProtKB-ARBA.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:32.054381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb",
  "url": "https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004308\nname: exo-alpha-sialidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)-glycosidic linkages of terminal sialic residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.\" [EC:3.2.1.18]\nsynonym: \"acetylneuraminidase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"acetylneuraminyl hydrolase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"alpha-neuraminidase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"N-acylneuraminate glycohydrolase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"neuraminidase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"sialidase activity\" RELATED [EC:3.2.1.18]\nxref: EC:3.2.1.18\nxref: MetaCyc:3.2.1.18-RXN\nxref: Reactome:R-HSA-1605723 \"NEU2 cleaves GM3 to form LacCer (cytosol)\"\nxref: Reactome:R-HSA-1605724 \"NEU1,4 hydrolyze PSAP(195-273):GM3:PE\"\nxref: Reactome:R-HSA-1605768 \"NEU3 cleaves GM3 to form LacCer (plasma membrane)\"\nxref: Reactome:R-HSA-168870 \"Neuraminidase enzymatic release from sialic acid\"\nxref: Reactome:R-HSA-4084994 \"NEU3 hydrolyzes Neu5Ac from glycoconjugates\"\nxref: Reactome:R-HSA-4084999 \"NEU1 hydrolyses Neu5Ac from glycoconjugates\"\nxref: Reactome:R-HSA-4085029 \"NEU2 hydrolyzes Neu5Ac from glycoconjugates\"\nxref: Reactome:R-HSA-4341669 \"Defective NEU1 does not hydrolyse Neu5Ac from glycoconjugates\"\nxref: Reactome:R-HSA-9638120 \"NEU4 hydrolyses Neu5Ac from glycoconjugates\"\nis_a: GO:0016997 ! alpha-sialidase activity\nproperty_value: skos:exactMatch EC:3.2.1.18\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004308",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 39493-39517",
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
  "excerpt": "[Term]\nid: GO:0005385\nname: zinc ion transmembrane transporter activity\nnamespace: molecular_function\ndef: \"Enables the transfer of zinc (Zn) ions from one side of a membrane to the other.\" [GOC:dgf]\nsynonym: \"cobalt, zinc uptake permease activity\" RELATED []\nsynonym: \"zinc, cadmium uptake permease activity\" RELATED []\nsynonym: \"zinc, cadmium, cobalt, nickel, lead-efflux ATPase activity\" RELATED []\nsynonym: \"zinc, iron permease activity\" NARROW []\nxref: MetaCyc:RXN0-12\nxref: Reactome:R-HSA-435366 \"ZnT1 mediates the efflux of zinc from the cell\"\nxref: Reactome:R-HSA-435375 \"ZnT2 facilitates zinc vesicular sequestration\"\nxref: Reactome:R-HSA-437084 \"ZnT3 transports zinc into synaptic vesicles\"\nxref: Reactome:R-HSA-437085 \"ZnT5 transports zinc into secretory granules in pancreatic beta cells\"\nxref: Reactome:R-HSA-437136 \"SLC30A8 transports Zn2+ from cytosol to secretory granule\"\nxref: Reactome:R-HSA-437139 \"ZnT8 transports zinc into the Golgi apparatus\"\nxref: Reactome:R-HSA-442317 \"ZIP6 and ZIP14 mediate zinc influx into cells\"\nxref: Reactome:R-HSA-442345 \"hZIP10 mediates zinc influx into cells\"\nxref: Reactome:R-HSA-442387 \"ZIP8 mediates zinc influx into cells\"\nxref: Reactome:R-HSA-442393 \"ZIP7 mediates zinc efflux from the endoplasmic reticulum\"\nxref: Reactome:R-HSA-442405 \"hZIP5 mediates zinc uptake by cells\"\nxref: Reactome:R-HSA-442422 \"SLC39A1-4 transports Zn2+ from extracellular region to cytosol\"\nxref: Reactome:R-HSA-5654125 \"Defective SLC39A4 does not transport Zn2+ from extracellular region to cytosol\"\nxref: Reactome:R-HSA-9820566 \"ZnT5 transports zinc into the golgi apparatus\"\nxref: Reactome:R-HSA-9928035 \"ZnuABC transports Zn2+ to cytosol\"\nis_a: GO:0046915 ! transition metal ion transmembrane transporter activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005385",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 56286-56312",
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
  "excerpt": "[Term]\nid: GO:0043022\nname: ribosome binding\nnamespace: molecular_function\nalt_id: GO:0030376\ndef: \"Binding to a ribosome.\" [GOC:curators]\nsynonym: \"ribosome receptor activity\" NARROW []\nis_a: GO:0043021 ! ribonucleoprotein complex binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043022",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 243239-243247",
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
  "excerpt": "[Term]\nid: GO:0051787\nname: misfolded protein binding\nnamespace: molecular_function\ndef: \"Binding to a misfolded protein.\" [GOC:ai]\nxref: Reactome:R-HSA-5324632 \"Dissociation of cytosolic HSF1:HSP90:HDAC6:PTGES3 upon sensing protein aggregates\"\nis_a: GO:0005515 ! protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051787",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 330727-330734",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 15. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
