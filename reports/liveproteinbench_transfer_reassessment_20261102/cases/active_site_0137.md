# active_site_0137

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0137.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 258 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. Position 413 (Proton donor)
B. Position 258 (Nucleophile)
C. Position 52 (Proton acceptor; for glutaminase activity)
D. Position 366 (For beta-ketoacyl synthase activity)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates residue 258 as the nucleophile. That annotation is transferred from a homolog, so it supports the expected answer but is not direct experimental validation of this residue in the supplied protein.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conserved Cys-containing motif consistent with NAD-dependent UDP-sugar dehydrogenases. In this enzyme family, a catalytic cysteine acts as the nucleophile during oxidation of the sugar substrate. This makes the nucleophile choice at position 258 meaningfully more plausible than the alternatives referring to glutaminase or beta-ketoacyl synthase activity, or a proton donor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level catalytic knowledge and the sequence motif provide a credible basis for selecting the nucleophile option without recalling this protein's exact database annotation. Assigning the precise position is supported by the motif's location in the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered functional descriptions distinguish the conserved catalytic nucleophile from the unrelated activity descriptions and the proton-donor alternative.


### Important caveats

- The available site annotation is evidence transferred from a homolog rather than direct experimental verification for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conserved Cys-containing motif consistent with NAD-dependent UDP-sugar dehydrogenases. In this enzyme family, a catalytic cysteine acts as the nucleophile during oxidation of the sugar substrate. This makes the nucleophile choice at position 258 meaningfully more plausible than the alternatives referring to glutaminase or beta-ketoacyl synthase activity, or a proton donor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic knowledge and the sequence motif provide a credible basis for selecting the nucleophile option without recalling this protein's exact database annotation. Assigning the precise position is supported by the motif's location in the supplied sequence."
  },
  "case_id": "active_site_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 258 as the nucleophile. That annotation is transferred from a homolog, so it supports the expected answer but is not direct experimental validation of this residue in the supplied protein."
  },
  "important_caveats": [
    "The available site annotation is evidence transferred from a homolog rather than direct experimental verification for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered functional descriptions distinguish the conserved catalytic nucleophile from the unrelated activity descriptions and the proton-donor alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 258 as the nucleophile. That annotation is transferred from a homolog, so it supports the expected answer but is not direct experimental validation of this residue in the supplied protein.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conserved Cys-containing motif consistent with NAD-dependent UDP-sugar dehydrogenases. In this enzyme family, a catalytic cysteine acts as the nucleophile during oxidation of the sugar substrate. This makes the nucleophile choice at position 258 meaningfully more plausible than the alternatives referring to glutaminase or beta-ketoacyl synthase activity, or a proton donor.",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic knowledge and the sequence motif provide a credible basis for selecting the nucleophile option without recalling this protein's exact database annotation. Assigning the precise position is supported by the motif's location in the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered functional descriptions distinguish the conserved catalytic nucleophile from the unrelated activity descriptions and the proton-donor alternative."
  },
  "important_caveats": [
    "The available site annotation is evidence transferred from a homolog rather than direct experimental verification for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5/H5) explicitly lists position 258 as 'Nucleophile' with evidence code ECO:0000250 (by similarity to Q0P8H3). Counting the provided sequence confirms position 258 is Cysteine, which is consistent with the 'GLVGGHCIGVDPYY' motif where Cys serves as the nucleophilic catalytic residue in this dehydrogenase subfamily. The annotation is computational (transferred by similarity), not direct experimental evidence for this specific protein, but it is internally consistent with the sequence context.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal 'GLGYVGLP' motif is a canonical GxxGxxG Rossmann fold for NAD+ binding, identifying this as an NAD-dependent dehydrogenase. The 'GLVGGHCIGVDPYY' region contains the 'GHC' (Gly-His-Cys) catalytic motif, a well-characterized nucleophilic catalytic arrangement in multiple dehydrogenase subfamilies where Cys is activated by His as a general base. Position 258 corresponds to the C in 'GHC'. Distractors are eliminable: (A) Position 413 is Leucine, which cannot function as a proton donor; (C) references 'glutaminase activity,' incompatible with a dehydrogenase bearing a Rossmann fold; (D) references 'beta-ketoacyl synthase activity,' also incompatible. A knowledgeable model recognizing the Rossmann fold and the GHC nucleophilic motif from other dehydrogenases (e.g., 3-hydroxyacyl-CoA dehydrogenases, certain UDP-sugar dehydrogenases) can identify Cys-258 as the nucleophile and reject the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GHC catalytic motif is directly visible in the supplied sequence, the Rossmann fold identifies the enzyme class, and the distractors are eliminated by both residue chemistry (Leu cannot be a proton donor) and family-level enzyme classification (glutaminase and beta-ketoacyl synthase activities are inconsistent with the sequence architecture). Transferable knowledge of dehydrogenase catalytic motifs suffices to distinguish B from the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D reference enzyme activities (glutaminase, beta-ketoacyl synthase) that are incompatible with the sequence's Rossmann-fold dehydrogenase architecture. Option A assigns 'proton donor' to position 413, which is Leucine—a chemically impossible proton donor. Only B is consistent with both the sequence features and the enzyme family.


### Important caveats

- The UniProt annotation for position 258 uses evidence code ECO:0000250 (inferred by similarity to Q0P8H3), meaning it is computational transfer rather than direct experimental verification for this specific protein.
- The nucleophile at position 258 is Cysteine (not Serine), which is less common than the canonical SDR Ser-Tyr-Lys-Asn tetrad but is a recognized variant in certain dehydrogenase subfamilies with a GHC motif.
- The reviewer-only evidence confirms sequence match and annotation, but the model was not given the UniProt entry or organism identity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal 'GLGYVGLP' motif is a canonical GxxGxxG Rossmann fold for NAD+ binding, identifying this as an NAD-dependent dehydrogenase. The 'GLVGGHCIGVDPYY' region contains the 'GHC' (Gly-His-Cys) catalytic motif, a well-characterized nucleophilic catalytic arrangement in multiple dehydrogenase subfamilies where Cys is activated by His as a general base. Position 258 corresponds to the C in 'GHC'. Distractors are eliminable: (A) Position 413 is Leucine, which cannot function as a proton donor; (C) references 'glutaminase activity,' incompatible with a dehydrogenase bearing a Rossmann fold; (D) references 'beta-ketoacyl synthase activity,' also incompatible. A knowledgeable model recognizing the Rossmann fold and the GHC nucleophilic motif from other dehydrogenases (e.g., 3-hydroxyacyl-CoA dehydrogenases, certain UDP-sugar dehydrogenases) can identify Cys-258 as the nucleophile and reject the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GHC catalytic motif is directly visible in the supplied sequence, the Rossmann fold identifies the enzyme class, and the distractors are eliminated by both residue chemistry (Leu cannot be a proton donor) and family-level enzyme classification (glutaminase and beta-ketoacyl synthase activities are inconsistent with the sequence architecture). Transferable knowledge of dehydrogenase catalytic motifs suffices to distinguish B from the alternatives."
  },
  "case_id": "active_site_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H5) explicitly lists position 258 as 'Nucleophile' with evidence code ECO:0000250 (by similarity to Q0P8H3). Counting the provided sequence confirms position 258 is Cysteine, which is consistent with the 'GLVGGHCIGVDPYY' motif where Cys serves as the nucleophilic catalytic residue in this dehydrogenase subfamily. The annotation is computational (transferred by similarity), not direct experimental evidence for this specific protein, but it is internally consistent with the sequence context."
  },
  "important_caveats": [
    "The UniProt annotation for position 258 uses evidence code ECO:0000250 (inferred by similarity to Q0P8H3), meaning it is computational transfer rather than direct experimental verification for this specific protein.",
    "The nucleophile at position 258 is Cysteine (not Serine), which is less common than the canonical SDR Ser-Tyr-Lys-Asn tetrad but is a recognized variant in certain dehydrogenase subfamilies with a GHC motif.",
    "The reviewer-only evidence confirms sequence match and annotation, but the model was not given the UniProt entry or organism identity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D reference enzyme activities (glutaminase, beta-ketoacyl synthase) that are incompatible with the sequence's Rossmann-fold dehydrogenase architecture. Option A assigns 'proton donor' to position 413, which is Leucine—a chemically impossible proton donor. Only B is consistent with both the sequence features and the enzyme family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H5) explicitly lists position 258 as 'Nucleophile' with evidence code ECO:0000250 (by similarity to Q0P8H3). Counting the provided sequence confirms position 258 is Cysteine, which is consistent with the 'GLVGGHCIGVDPYY' motif where Cys serves as the nucleophilic catalytic residue in this dehydrogenase subfamily. The annotation is computational (transferred by similarity), not direct experimental evidence for this specific protein, but it is internally consistent with the sequence context.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal 'GLGYVGLP' motif is a canonical GxxGxxG Rossmann fold for NAD+ binding, identifying this as an NAD-dependent dehydrogenase. The 'GLVGGHCIGVDPYY' region contains the 'GHC' (Gly-His-Cys) catalytic motif, a well-characterized nucleophilic catalytic arrangement in multiple dehydrogenase subfamilies where Cys is activated by His as a general base. Position 258 corresponds to the C in 'GHC'. Distractors are eliminable: (A) Position 413 is Leucine, which cannot function as a proton donor; (C) references 'glutaminase activity,' incompatible with a dehydrogenase bearing a Rossmann fold; (D) references 'beta-ketoacyl synthase activity,' also incompatible. A knowledgeable model recognizing the Rossmann fold and the GHC nucleophilic motif from other dehydrogenases (e.g., 3-hydroxyacyl-CoA dehydrogenases, certain UDP-sugar dehydrogenases) can identify Cys-258 as the nucleophile and reject the other options.",
    "missing_item_specific_fact": "",
    "reason": "The GHC catalytic motif is directly visible in the supplied sequence, the Rossmann fold identifies the enzyme class, and the distractors are eliminated by both residue chemistry (Leu cannot be a proton donor) and family-level enzyme classification (glutaminase and beta-ketoacyl synthase activities are inconsistent with the sequence architecture). Transferable knowledge of dehydrogenase catalytic motifs suffices to distinguish B from the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D reference enzyme activities (glutaminase, beta-ketoacyl synthase) that are incompatible with the sequence's Rossmann-fold dehydrogenase architecture. Option A assigns 'proton donor' to position 413, which is Leucine—a chemically impossible proton donor. Only B is consistent with both the sequence features and the enzyme family."
  },
  "important_caveats": [
    "The UniProt annotation for position 258 uses evidence code ECO:0000250 (inferred by similarity to Q0P8H3), meaning it is computational transfer rather than direct experimental verification for this specific protein.",
    "The nucleophile at position 258 is Cysteine (not Serine), which is less common than the canonical SDR Ser-Tyr-Lys-Asn tetrad but is a recognized variant in certain dehydrogenase subfamilies with a GHC motif.",
    "The reviewer-only evidence confirms sequence match and annotation, but the model was not given the UniProt entry or organism identity."
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
  "benchmark_sequence_length": 422,
  "benchmark_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "current_entry_audit": {
    "entryVersion": 113,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 422,
  "current_source_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 111,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9RHD7",
  "selected_historical_entry_version": 111,
  "selected_historical_record_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "selected_historical_source_sequence_length": 422,
  "selected_historical_source_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "selected_historical_version": {
    "accession": "Q9RHD7",
    "database": "Swiss-Prot",
    "entryVersion": 111,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "WBPO_PSEAI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9RHD7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":113,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa\",\"taxonId\":287}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.136\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-D-glucosamine 6-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-GlcNAc 6-dehydrogenase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":258},\"start\":{\"modifier\":\"EXACT\",\"value\":258}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":14},\"start\":{\"modifier\":\"EXACT\",\"value\":14}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":32},\"start\":{\"modifier\":\"EXACT\",\"value\":32}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":37},\"start\":{\"modifier\":\"EXACT\",\"value\":37}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":83},\"start\":{\"modifier\":\"EXACT\",\"value\":83}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":118},\"start\":{\"modifier\":\"EXACT\",\"value\":118}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0P8H3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":329},\"start\":{\"modifier\":\"EXACT\",\"value\":329}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Miller W.L.\",\"Matewish M.J.\",\"McNally D.J.\",\"Ishiyama N.\",\"Anderson E.M.\",\"Brewer D.\",\"Brisson J.R.\",\"Berghuis A.M.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18065759\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m708894200\"}],\"citationType\":\"journal article\",\"firstPage\":\"3507\",\"id\":\"18065759\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"3518\",\"publicationDate\":\"2008\",\"title\":\"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.\",\"volume\":\"283\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"PAK / Serotype O6\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H1",
  "excerpt": "ID   WBPO_PSEAI              Reviewed;         422 AA.\nAC   Q9RHD7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 111.\nDE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000305};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000305};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:18065759};\nGN   Name=wbpO {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};\nGN   ORFNames=CAZ10_03215 {ECO:0000312|EMBL:OTI64803.1};\nOS   Pseudomonas aeruginosa.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=287;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAF23997.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 33354 / Serotype O6;\nRX   PubMed=10627048; DOI=10.1099/00221287-145-12-3505;\nRA   Belanger M., Burrows L.L., Lam J.S.;\nRT   \"Functional analysis of genes responsible for the synthesis of the B-band O\nRT   antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.\";\nRL   Microbiology 145:3505-3521(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:AAM27816.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=Serotype O6;\nRX   PubMed=12057956; DOI=10.1128/jb.184.13.3614-3622.2002;\nRA   Raymond C.K., Sims E.H., Kas A., Spencer D.H., Kutyavin T.V., Ivey R.G.,\nRA   Zhou Y., Kaul R., Clendenning J.B., Olson M.V.;\nRT   \"Genetic variation at the O-antigen biosynthetic locus in Pseudomonas\nRT   aeruginosa.\";\nRL   J. Bacteriol. 184:3614-3622(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H4",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=PAK / Serotype O6;\nRX   PubMed=18065759; DOI=10.1074/jbc.m708894200;\nRA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,\nRA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;\nRT   \"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-\nRT   antigen biosynthesis enzyme WbpO.\";\nRL   J. Biol. Chem. 283:3507-3518(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        258\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 177-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         14\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-183",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         32\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 184-187",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         37\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 188-191",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         83\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 192-195",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         118\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 196-199",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         329\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q0P8H3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 200-203",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 137. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
