# GO_cellular_component_0069

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0069.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — other organism cell membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MARFSSKNLTKLFQYLVLSLLSPVAFGNFNIEVDTRNKVLNDAAINFYGQNIGIITDGERRVFGITDGPLKEACSKVQGGKPGYVWVRSPTPANLYEIHNWRQVLRVLTAYDARIVGIEQKPEMVATQTYKNRSDHPAKVSGMITQSVSNTIENKWIEMNQFSITATVSCKVKAAEIGLSMGYERSWGKEDTNSTTTMLGQQTGFEVELPPGGNCTAVLSATKGSMKIDVGYRATLEGDCAVDFPNTWNGHHYWCYPIGLVQDVGNLKKHIDCRELITIGYYSDAHVTIENLGKKKNKKTKKPPRKTKMN

[Multiple Choices]
A. T=4 icosahedral viral capsid
B. nuclear periphery
C. NF-kappaB complex
D. other organism cell membrane
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

> The matched-sequence UniProt record annotates the protein as secreted and as localizing to the target cell membrane. The target-membrane annotation directly supports D; the separate GO cross-reference to “other organism cell membrane” is keyword-based rather than direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a strongly hydrophobic N-terminal segment consistent with a secretion signal, and its long globular mature region is more consistent with a secreted effector than with a nuclear protein, NF-kappaB subunit, or viral capsid protein. Transferable knowledge that secreted pore-forming toxins can bind target-cell membranes makes D a credible choice among these options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal peptide and toxin-like sequence architecture provide a meaningful, though not conclusive, basis for choosing a target-cell membrane over the nuclear and viral alternatives. A signal peptide alone would establish neither membrane targeting nor this exact GO annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein may be secreted before associating with a target membrane, but among the offered choices D is the one consistent with that target-cell interaction.


### Important caveats

- The evidence supports secretion and target-cell membrane localization, but the cited target-membrane annotation is curator-assigned rather than explicitly marked experimental.
- The original sequence alone cannot establish the precise GO annotation with certainty.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a strongly hydrophobic N-terminal segment consistent with a secretion signal, and its long globular mature region is more consistent with a secreted effector than with a nuclear protein, NF-kappaB subunit, or viral capsid protein. Transferable knowledge that secreted pore-forming toxins can bind target-cell membranes makes D a credible choice among these options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide and toxin-like sequence architecture provide a meaningful, though not conclusive, basis for choosing a target-cell membrane over the nuclear and viral alternatives. A signal peptide alone would establish neither membrane targeting nor this exact GO annotation."
  },
  "case_id": "GO_cellular_component_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates the protein as secreted and as localizing to the target cell membrane. The target-membrane annotation directly supports D; the separate GO cross-reference to “other organism cell membrane” is keyword-based rather than direct experimental evidence."
  },
  "important_caveats": [
    "The evidence supports secretion and target-cell membrane localization, but the cited target-membrane annotation is curator-assigned rather than explicitly marked experimental.",
    "The original sequence alone cannot establish the precise GO annotation with certainty."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may be secreted before associating with a target membrane, but among the offered choices D is the one consistent with that target-cell interaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates the protein as secreted and as localizing to the target cell membrane. The target-membrane annotation directly supports D; the separate GO cross-reference to “other organism cell membrane” is keyword-based rather than direct experimental evidence.",
    "evidence_ids": ["C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a strongly hydrophobic N-terminal segment consistent with a secretion signal, and its long globular mature region is more consistent with a secreted effector than with a nuclear protein, NF-kappaB subunit, or viral capsid protein. Transferable knowledge that secreted pore-forming toxins can bind target-cell membranes makes D a credible choice among these options.",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide and toxin-like sequence architecture provide a meaningful, though not conclusive, basis for choosing a target-cell membrane over the nuclear and viral alternatives. A signal peptide alone would establish neither membrane targeting nor this exact GO annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may be secreted before associating with a target membrane, but among the offered choices D is the one consistent with that target-cell interaction."
  },
  "important_caveats": [
    "The evidence supports secretion and target-cell membrane localization, but the cited target-membrane annotation is curator-assigned rather than explicitly marked experimental.",
    "The original sequence alone cannot establish the precise GO annotation with certainty."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXX1 annotates this protein with GO:0044218 'other organism cell membrane' (IEA:UniProtKB-KW) and lists subcellular location as 'Secreted' (ECO:0000269, experimental) and 'Target cell membrane' (ECO:0000305, sequence-based). The protein is an aerolysin-like pore-forming toxin from a caterpillar (Megalopyge opercularis) that acts on the membranes of other organisms (e.g., human skin). The experimental evidence supports secretion and membrane targeting; the specific GO:0044218 mapping follows from the keyword annotation for pore-forming toxins acting on foreign membranes. The concept is scientifically coherent: a secreted PFT from organism A targeting organism B's membrane maps to 'other organism cell membrane.'

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a clear signal peptide (MARFSSKNLTKLFQYLVLSLLSPVAFG, residues 1-25, with a hydrophobic core LTKLFQYLVLSLLSPVAFG), indicating a secreted protein. This eliminates nuclear periphery (B) and NF-kappaB complex (C), which require nuclear localization and Rel-homology domains respectively. The sequence contains characteristic aerolysin-family motifs: the 'DTG' dipeptide in 'IITDGERRVFGITDG' and the 'RPTPAN' region, consistent with the aerolysin-like pore-forming toxin superfamily (~300 aa, beta-barrel pore architecture). Aerolysin-family toxins are well-known membrane-pore formers. Since this is a eukaryotic (insect) toxin secreted to affect other organisms, the membrane it targets belongs to a foreign organism, matching 'other organism cell membrane' (D). Option A (T=4 icosahedral viral capsid) is excluded because the protein has a eukaryotic signal peptide, is not a structural capsid protein, and lacks the jelly-roll symmetry constraints of viral capsomers. Thus, family recognition (aerolysin PFT) plus signal-peptide logic plus toxin biology meaningfully distinguishes D from all other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can: (1) identify the signal peptide to infer secretion, eliminating B and C; (2) recognize aerolysin-family DTG and RPTPAN motifs to infer pore-forming/membrane-targeting function, eliminating A; (3) apply the general principle that a secreted toxin from one organism targeting membranes of another maps to 'other organism cell membrane.' This uses transferable knowledge of the aerolysin PFT family, signal peptide biology, and toxin mechanism without requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with a secreted protein bearing a eukaryotic signal peptide and aerolysin-like motifs. D is the only membrane-targeting option and is the natural GO term for a toxin acting on foreign cell membranes. No alternative among the four choices is defensible for this sequence.


### Important caveats

- The GO:0044218 annotation is IEA (Inferred from Electronic Annotation via UniProtKB keyword), not directly experimental. The experimental evidence supports 'Secreted' and 'Target cell membrane' (SL-0451); the 'other organism' qualifier is a logical consequence of the toxin context rather than a separately measured fact.
- The protein was first publicly released in UniProt on 2025-02-05 (entry version 1). The benchmark likely used a very recent annotation; the aerolysin-family recognition and signal-peptide logic are independent of the specific database entry.
- The reviewer-only evidence confirms sequence match to P0DXX1, but the model was not given the accession, organism name, or protein name—only the raw sequence and four GO options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a clear signal peptide (MARFSSKNLTKLFQYLVLSLLSPVAFG, residues 1-25, with a hydrophobic core LTKLFQYLVLSLLSPVAFG), indicating a secreted protein. This eliminates nuclear periphery (B) and NF-kappaB complex (C), which require nuclear localization and Rel-homology domains respectively. The sequence contains characteristic aerolysin-family motifs: the 'DTG' dipeptide in 'IITDGERRVFGITDG' and the 'RPTPAN' region, consistent with the aerolysin-like pore-forming toxin superfamily (~300 aa, beta-barrel pore architecture). Aerolysin-family toxins are well-known membrane-pore formers. Since this is a eukaryotic (insect) toxin secreted to affect other organisms, the membrane it targets belongs to a foreign organism, matching 'other organism cell membrane' (D). Option A (T=4 icosahedral viral capsid) is excluded because the protein has a eukaryotic signal peptide, is not a structural capsid protein, and lacks the jelly-roll symmetry constraints of viral capsomers. Thus, family recognition (aerolysin PFT) plus signal-peptide logic plus toxin biology meaningfully distinguishes D from all other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can: (1) identify the signal peptide to infer secretion, eliminating B and C; (2) recognize aerolysin-family DTG and RPTPAN motifs to infer pore-forming/membrane-targeting function, eliminating A; (3) apply the general principle that a secreted toxin from one organism targeting membranes of another maps to 'other organism cell membrane.' This uses transferable knowledge of the aerolysin PFT family, signal peptide biology, and toxin mechanism without requiring recall of this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXX1 annotates this protein with GO:0044218 'other organism cell membrane' (IEA:UniProtKB-KW) and lists subcellular location as 'Secreted' (ECO:0000269, experimental) and 'Target cell membrane' (ECO:0000305, sequence-based). The protein is an aerolysin-like pore-forming toxin from a caterpillar (Megalopyge opercularis) that acts on the membranes of other organisms (e.g., human skin). The experimental evidence supports secretion and membrane targeting; the specific GO:0044218 mapping follows from the keyword annotation for pore-forming toxins acting on foreign membranes. The concept is scientifically coherent: a secreted PFT from organism A targeting organism B's membrane maps to 'other organism cell membrane.'"
  },
  "important_caveats": [
    "The GO:0044218 annotation is IEA (Inferred from Electronic Annotation via UniProtKB keyword), not directly experimental. The experimental evidence supports 'Secreted' and 'Target cell membrane' (SL-0451); the 'other organism' qualifier is a logical consequence of the toxin context rather than a separately measured fact.",
    "The protein was first publicly released in UniProt on 2025-02-05 (entry version 1). The benchmark likely used a very recent annotation; the aerolysin-family recognition and signal-peptide logic are independent of the specific database entry.",
    "The reviewer-only evidence confirms sequence match to P0DXX1, but the model was not given the accession, organism name, or protein name—only the raw sequence and four GO options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a secreted protein bearing a eukaryotic signal peptide and aerolysin-like motifs. D is the only membrane-targeting option and is the natural GO term for a toxin acting on foreign cell membranes. No alternative among the four choices is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXX1 annotates this protein with GO:0044218 'other organism cell membrane' (IEA:UniProtKB-KW) and lists subcellular location as 'Secreted' (ECO:0000269, experimental) and 'Target cell membrane' (ECO:0000305, sequence-based). The protein is an aerolysin-like pore-forming toxin from a caterpillar (Megalopyge opercularis) that acts on the membranes of other organisms (e.g., human skin). The experimental evidence supports secretion and membrane targeting; the specific GO:0044218 mapping follows from the keyword annotation for pore-forming toxins acting on foreign membranes. The concept is scientifically coherent: a secreted PFT from organism A targeting organism B's membrane maps to 'other organism cell membrane.'",
    "evidence_ids": ["C5", "C6", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a clear signal peptide (MARFSSKNLTKLFQYLVLSLLSPVAFG, residues 1-25, with a hydrophobic core LTKLFQYLVLSLLSPVAFG), indicating a secreted protein. This eliminates nuclear periphery (B) and NF-kappaB complex (C), which require nuclear localization and Rel-homology domains respectively. The sequence contains characteristic aerolysin-family motifs: the 'DTG' dipeptide in 'IITDGERRVFGITDG' and the 'RPTPAN' region, consistent with the aerolysin-like pore-forming toxin superfamily (~300 aa, beta-barrel pore architecture). Aerolysin-family toxins are well-known membrane-pore formers. Since this is a eukaryotic (insect) toxin secreted to affect other organisms, the membrane it targets belongs to a foreign organism, matching 'other organism cell membrane' (D). Option A (T=4 icosahedral viral capsid) is excluded because the protein has a eukaryotic signal peptide, is not a structural capsid protein, and lacks the jelly-roll symmetry constraints of viral capsomers. Thus, family recognition (aerolysin PFT) plus signal-peptide logic plus toxin biology meaningfully distinguishes D from all other options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can: (1) identify the signal peptide to infer secretion, eliminating B and C; (2) recognize aerolysin-family DTG and RPTPAN motifs to infer pore-forming/membrane-targeting function, eliminating A; (3) apply the general principle that a secreted toxin from one organism targeting membranes of another maps to 'other organism cell membrane.' This uses transferable knowledge of the aerolysin PFT family, signal peptide biology, and toxin mechanism without requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a secreted protein bearing a eukaryotic signal peptide and aerolysin-like motifs. D is the only membrane-targeting option and is the natural GO term for a toxin acting on foreign cell membranes. No alternative among the four choices is defensible for this sequence."
  },
  "important_caveats": [
    "The GO:0044218 annotation is IEA (Inferred from Electronic Annotation via UniProtKB keyword), not directly experimental. The experimental evidence supports 'Secreted' and 'Target cell membrane' (SL-0451); the 'other organism' qualifier is a logical consequence of the toxin context rather than a separately measured fact.",
    "The protein was first publicly released in UniProt on 2025-02-05 (entry version 1). The benchmark likely used a very recent annotation; the aerolysin-family recognition and signal-peptide logic are independent of the specific database entry.",
    "The reviewer-only evidence confirms sequence match to P0DXX1, but the model was not given the accession, organism name, or protein name—only the raw sequence and four GO options."
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
  "benchmark_sequence_length": 310,
  "benchmark_sequence_sha256": "762364a55619850533adb77d6887a242b804a3ccb06c6831da30f7c577b3c14d",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ac064a4a53a978b82f076fcd40ca80db8fb662a5986e6b12e4d09c50ebf92455",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 310,
  "current_source_sequence_sha256": "762364a55619850533adb77d6887a242b804a3ccb06c6831da30f7c577b3c14d",
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
  "requested_accession": "P0DXX1",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "cc4914e79a75fdf864b4725d73cbbaa0b2f16de40bc89fbd59dcb5ab54fbf6b3",
  "selected_historical_source_sequence_length": 310,
  "selected_historical_source_sequence_sha256": "762364a55619850533adb77d6887a242b804a3ccb06c6831da30f7c577b3c14d",
  "selected_historical_version": {
    "accession": "P0DXX1",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TXU8F_MEGOP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXX1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:53.420710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac064a4a53a978b82f076fcd40ca80db8fb662a5986e6b12e4d09c50ebf92455",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXX1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:53.420710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac064a4a53a978b82f076fcd40ca80db8fb662a5986e6b12e4d09c50ebf92455",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXX1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Southern flannel moth\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Lepidoptera\",\"Glossata\",\"Ditrysia\",\"Zygaenoidea\",\"Megalopygidae\",\"Megalopyge\"],\"scientificName\":\"Megalopyge opercularis\",\"synonyms\":[\"Phalaena opercularis\"],\"taxonId\":1113279}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:53.420710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac064a4a53a978b82f076fcd40ca80db8fb662a5986e6b12e4d09c50ebf92455",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXX1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428925\",\"source\":\"PubMed\"}],\"value\":\"Aerolysin-like pore-forming toxin\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428925\",\"source\":\"PubMed\"}],\"value\":\"Megalysin\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428925\",\"source\":\"PubMed\"}],\"value\":\"U-megalopygitoxin(8)-Mo15\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428925\",\"source\":\"PubMed\"}],\"value\":\"U-MPTX(8)-Mo15\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WJJ70383.1\",\"source\":\"EMBL\"}],\"value\":\"U-MPTX.8-15\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:53.420710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac064a4a53a978b82f076fcd40ca80db8fb662a5986e6b12e4d09c50ebf92455",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXX1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428925\",\"source\":\"PubMed\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"37428925\",\"source\":\"PubMed\"}],\"id\":\"SL-0451\",\"value\":\"Target cell membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:53.420710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac064a4a53a978b82f076fcd40ca80db8fb662a5986e6b12e4d09c50ebf92455",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXX1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428925\",\"source\":\"PubMed\"}],\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/2",
  "retrieved_utc": "2026-11-02T04:29:53.420710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac064a4a53a978b82f076fcd40ca80db8fb662a5986e6b12e4d09c50ebf92455",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXX1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXX1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Walker A.A.\",\"Robinson S.D.\",\"Merritt D.J.\",\"Cardoso F.C.\",\"Goudarzi M.H.\",\"Mercedes R.S.\",\"Eagles D.A.\",\"Cooper P.\",\"Zdenek C.N.\",\"Fry B.G.\",\"Hall D.W.\",\"Vetter I.\",\"King G.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37428925\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.2305871120\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2305871120\",\"id\":\"37428925\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"e2305871120\",\"publicationDate\":\"2023\",\"title\":\"Horizontal gene transfer underlies the painful stings of asp caterpillars (Lepidoptera: Megalopygidae).\",\"volume\":\"120\"},\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Venom\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"MASS SPECTROMETRY\",\"3D-STRUCTURE MODELING\",\"RECOMBINANT EXPRESSION\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:53.420710+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ac064a4a53a978b82f076fcd40ca80db8fb662a5986e6b12e4d09c50ebf92455",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXX1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   TXU8F_MEGOP             Reviewed;         310 AA.\nAC   P0DXX1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=U-megalopygitoxin(8)-Mo15 {ECO:0000303|PubMed:37428925};\nDE            Short=U-MPTX(8)-Mo15 {ECO:0000303|PubMed:37428925};\nDE            Short=U-MPTX.8-15 {ECO:0000312|EMBL:WJJ70383.1};\nDE   AltName: Full=Aerolysin-like pore-forming toxin {ECO:0000303|PubMed:37428925};\nDE   AltName: Full=Megalysin {ECO:0000303|PubMed:37428925};\nDE   Flags: Precursor;\nOS   Megalopyge opercularis (Southern flannel moth) (Phalaena opercularis).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Lepidoptera; Glossata; Ditrysia; Zygaenoidea;\nOC   Megalopygidae; Megalopyge.\nOX   NCBI_TaxID=1113279;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.155077+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc4914e79a75fdf864b4725d73cbbaa0b2f16de40bc89fbd59dcb5ab54fbf6b3",
  "url": "https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], MASS SPECTROMETRY, 3D-STRUCTURE MODELING,\nRP   RECOMBINANT EXPRESSION, SUBCELLULAR LOCATION, TISSUE SPECIFICITY, AND\nRP   DEVELOPMENTAL STAGE.\nRC   TISSUE=Venom;\nRX   PubMed=37428925; DOI=10.1073/pnas.2305871120;\nRA   Walker A.A., Robinson S.D., Merritt D.J., Cardoso F.C., Goudarzi M.H.,\nRA   Mercedes R.S., Eagles D.A., Cooper P., Zdenek C.N., Fry B.G., Hall D.W.,\nRA   Vetter I., King G.F.;\nRT   \"Horizontal gene transfer underlies the painful stings of asp caterpillars\nRT   (Lepidoptera: Megalopygidae).\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 120:e2305871120-e2305871120(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.155077+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc4914e79a75fdf864b4725d73cbbaa0b2f16de40bc89fbd59dcb5ab54fbf6b3",
  "url": "https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:37428925}. Target\nCC       cell membrane {ECO:0000305|PubMed:37428925}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.155077+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc4914e79a75fdf864b4725d73cbbaa0b2f16de40bc89fbd59dcb5ab54fbf6b3",
  "url": "https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.155077+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc4914e79a75fdf864b4725d73cbbaa0b2f16de40bc89fbd59dcb5ab54fbf6b3",
  "url": "https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0044218; C:other organism cell membrane; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.155077+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc4914e79a75fdf864b4725d73cbbaa0b2f16de40bc89fbd59dcb5ab54fbf6b3",
  "url": "https://rest.uniprot.org/unisave/P0DXX1?format=txt&versions=3"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0034399\nname: nuclear periphery\nnamespace: cellular_component\ndef: \"The portion of the nuclear lumen proximal to the inner nuclear membrane.\" [GOC:krc, GOC:mah]\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0031981 ! nuclear lumen\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0034399",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 208650-208657",
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
  "excerpt": "[Term]\nid: GO:0039619\nname: T=4 icosahedral viral capsid\nnamespace: cellular_component\ndef: \"The protein coat that surrounds the infective nucleic acid in some virus particles where the subunits (capsomeres) are arranged to form an icosahedron with T=4 symmetry. The T=4 capsid is composed of 12 pentameric and 30 hexameric capsomeres.\" [VZ:808]\nxref: VZ:808 \"T=4 icosahedral capsid protein\"\nis_a: GO:0019030 ! icosahedral viral capsid\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0039619",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 232112-232119",
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
  "excerpt": "[Term]\nid: GO:0044218\nname: other organism cell membrane\nnamespace: cellular_component\nalt_id: GO:0044279\ndef: \"The cell membrane of a secondary organism with which the first organism is interacting.\" [GOC:jl]\nsynonym: \"foreign membrane\" RELATED []\nsynonym: \"other organism membrane\" BROAD []\nis_a: GO:0044217 ! other organism part\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044218",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 255298-255307",
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
  "excerpt": "[Term]\nid: GO:0071159\nname: NF-kappaB complex\nnamespace: cellular_component\ndef: \"A protein complex that consists of a homo- or heterodimer of members of a family of structurally related proteins that contain a conserved N-terminal region called the Rel homology domain (RHD). In the nucleus, NF-kappaB complexes act as transcription factors. In unstimulated cells, NF-kappaB dimers are sequestered in the cytoplasm by IkappaB monomers; signals that induce NF-kappaB activity cause degradation of IkappaB, allowing NF-kappaB dimers to translocate to the nucleus and induce gene expression.\" [ISBN:0849327946]\nis_a: GO:0140513 ! nuclear protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071159",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 374446-374452",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 69. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
