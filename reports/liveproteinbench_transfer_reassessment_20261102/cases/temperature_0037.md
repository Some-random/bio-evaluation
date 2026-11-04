# temperature_0037

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0037.txt)

**Task:** `temperature`  
**Expected answer:** **B** — 37-42

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. 26-37
B. 37-42
C. 22-33
D. 40-54
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation reports an optimum temperature between 37 and 42 °C, matching choice B. The annotation attributes this result to experimental evidence from cited studies.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence or family-level knowledge might support a broad expectation of moderate-temperature function, but that does not meaningfully distinguish these nearby temperature intervals or establish the measured optimum.


**Missing item-specific fact**

> The experimentally reported optimum temperature for this exact protein, 37–42 °C, is absent from the input.


**Reason**

> The exact interval depends on a protein-specific experimental measurement. General sequence patterns and transferable family knowledge may suggest a broad thermal category, but do not provide a credible basis for selecting this narrow range over the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Interpreting the choices as the optimal temperature range, B is supported. The prompt's wording also mentions stability and function, while the evidence reports activity over a broader range; it does not establish another option as the optimum.


### Important caveats

- The cited experimental evidence is represented here through UniProt annotations; the primary studies were not independently reviewed.
- The annotation also reports relatively constant activity from 37 to 56 °C, which is a broader activity observation, not the reported optimum.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence or family-level knowledge might support a broad expectation of moderate-temperature function, but that does not meaningfully distinguish these nearby temperature intervals or establish the measured optimum.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally reported optimum temperature for this exact protein, 37–42 °C, is absent from the input.",
    "reason": "The exact interval depends on a protein-specific experimental measurement. General sequence patterns and transferable family knowledge may suggest a broad thermal category, but do not provide a credible basis for selecting this narrow range over the alternatives."
  },
  "case_id": "temperature_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature between 37 and 42 °C, matching choice B. The annotation attributes this result to experimental evidence from cited studies."
  },
  "important_caveats": [
    "The cited experimental evidence is represented here through UniProt annotations; the primary studies were not independently reviewed.",
    "The annotation also reports relatively constant activity from 37 to 56 °C, which is a broader activity observation, not the reported optimum."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Interpreting the choices as the optimal temperature range, B is supported. The prompt's wording also mentions stability and function, while the evidence reports activity over a broader range; it does not establish another option as the optimum."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports an optimum temperature between 37 and 42 °C, matching choice B. The annotation attributes this result to experimental evidence from cited studies.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence or family-level knowledge might support a broad expectation of moderate-temperature function, but that does not meaningfully distinguish these nearby temperature intervals or establish the measured optimum.",
    "missing_item_specific_fact": "The experimentally reported optimum temperature for this exact protein, 37–42 °C, is absent from the input.",
    "reason": "The exact interval depends on a protein-specific experimental measurement. General sequence patterns and transferable family knowledge may suggest a broad thermal category, but do not provide a credible basis for selecting this narrow range over the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Interpreting the choices as the optimal temperature range, B is supported. The prompt's wording also mentions stability and function, while the evidence reports activity over a broader range; it does not establish another option as the optimum."
  },
  "important_caveats": [
    "The cited experimental evidence is represented here through UniProt annotations; the primary studies were not independently reviewed.",
    "The annotation also reports relatively constant activity from 37 to 56 °C, which is a broader activity observation, not the reported optimum."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for Q9RHD7 (WbpO, UDP-N-acetyl-D-glucosamine 6-dehydrogenase from Pseudomonas aeruginosa) explicitly states: 'Optimum temperature is between 37 and 42 degrees Celsius (PubMed:18065759).' This is direct experimental evidence (ECO:0000269). The sequence matches the benchmark exactly (422 aa, SHA256 confirmed). The organism P. aeruginosa is a mesophilic human pathogen with optimal growth at 37°C, fully consistent with the 37-42°C range.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C3](#evidence-c3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a Rossmann-fold NAD-dependent dehydrogenase (GXGXXG motif at positions 8-13: GLGYVGLP). Sequence composition analysis shows moderate densities of charged residues (D, E, K, R) forming potential salt bridges, moderate proline content, and a hydrophobic core without extreme stabilization features. These features are inconsistent with cold-adaptation (which would show very high glycine, low proline, reduced salt bridges → rules out C: 22-33) and inconsistent with thermophilic adaptation (which would show very high charged-residue density, elevated proline, reduced thermolabile residues → rules out D: 40-54). For the A vs B distinction: statistical patterns from mesophilic bacterial enzymes (learned from many homologs) show optima clustering near the organism's growth temperature, canonically 37°C for mesophiles. Option B (37-42) places the optimum AT 37°C, consistent with a standard mesophilic optimum, while option A (26-37) implies the optimum is below 37°C, more characteristic of psychrotolerant or soil mesophiles. The moderate salt-bridge density and absence of cold-adaptation signatures (no extreme glycine enrichment, no proline depletion) favor a canonical 37°C-centered optimum, making B more probable than A. Additionally, the enzyme's broad activity range (37-56°C per experimental data) is consistent with a mesophile that tolerates mild heat stress, aligning with the 37-42 optimum rather than a lower-centered range.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The general mesophilic classification (ruling out C and D) is strongly supported by sequence composition. The A vs B distinction relies on the statistical regularity that canonical mesophilic bacterial enzymes have optima at ~37°C rather than below it, which is transferable knowledge from many homologous dehydrogenases. However, the specific 42°C upper bound is organism-specific (P. aeruginosa's known 42°C growth tolerance) and not strictly derivable from sequence alone, introducing some uncertainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (26-37) and B (37-42) represent mesophilic ranges. Without organism identification, a model might reasonably assign a mesophilic enzyme to either range. The distinction depends on whether the optimum is centered at 37°C (B) or shifted lower (A), which is a subtle discrimination that general sequence composition alone does not definitively resolve.


### Important caveats

- The specific 42°C upper bound in the correct answer is an experimental measurement from PubMed:18065759 and is organism-specific (P. aeruginosa's thermal tolerance).
- The A vs B distinction is the hardest part of this question; general mesophilic reasoning favors B but does not exclude A with certainty.
- The UniProt annotation for this entry was first publicly released in 2025-02-05; the author's source snapshot timing is unknown.
- The sequence is 422 amino acids matching Q9RHD7 exactly; no organism name or accession was provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a Rossmann-fold NAD-dependent dehydrogenase (GXGXXG motif at positions 8-13: GLGYVGLP). Sequence composition analysis shows moderate densities of charged residues (D, E, K, R) forming potential salt bridges, moderate proline content, and a hydrophobic core without extreme stabilization features. These features are inconsistent with cold-adaptation (which would show very high glycine, low proline, reduced salt bridges → rules out C: 22-33) and inconsistent with thermophilic adaptation (which would show very high charged-residue density, elevated proline, reduced thermolabile residues → rules out D: 40-54). For the A vs B distinction: statistical patterns from mesophilic bacterial enzymes (learned from many homologs) show optima clustering near the organism's growth temperature, canonically 37°C for mesophiles. Option B (37-42) places the optimum AT 37°C, consistent with a standard mesophilic optimum, while option A (26-37) implies the optimum is below 37°C, more characteristic of psychrotolerant or soil mesophiles. The moderate salt-bridge density and absence of cold-adaptation signatures (no extreme glycine enrichment, no proline depletion) favor a canonical 37°C-centered optimum, making B more probable than A. Additionally, the enzyme's broad activity range (37-56°C per experimental data) is consistent with a mesophile that tolerates mild heat stress, aligning with the 37-42 optimum rather than a lower-centered range.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The general mesophilic classification (ruling out C and D) is strongly supported by sequence composition. The A vs B distinction relies on the statistical regularity that canonical mesophilic bacterial enzymes have optima at ~37°C rather than below it, which is transferable knowledge from many homologous dehydrogenases. However, the specific 42°C upper bound is organism-specific (P. aeruginosa's known 42°C growth tolerance) and not strictly derivable from sequence alone, introducing some uncertainty."
  },
  "case_id": "temperature_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for Q9RHD7 (WbpO, UDP-N-acetyl-D-glucosamine 6-dehydrogenase from Pseudomonas aeruginosa) explicitly states: 'Optimum temperature is between 37 and 42 degrees Celsius (PubMed:18065759).' This is direct experimental evidence (ECO:0000269). The sequence matches the benchmark exactly (422 aa, SHA256 confirmed). The organism P. aeruginosa is a mesophilic human pathogen with optimal growth at 37°C, fully consistent with the 37-42°C range."
  },
  "important_caveats": [
    "The specific 42°C upper bound in the correct answer is an experimental measurement from PubMed:18065759 and is organism-specific (P. aeruginosa's thermal tolerance).",
    "The A vs B distinction is the hardest part of this question; general mesophilic reasoning favors B but does not exclude A with certainty.",
    "The UniProt annotation for this entry was first publicly released in 2025-02-05; the author's source snapshot timing is unknown.",
    "The sequence is 422 amino acids matching Q9RHD7 exactly; no organism name or accession was provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (26-37) and B (37-42) represent mesophilic ranges. Without organism identification, a model might reasonably assign a mesophilic enzyme to either range. The distinction depends on whether the optimum is centered at 37°C (B) or shifted lower (A), which is a subtle discrimination that general sequence composition alone does not definitively resolve."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"temperature_0037","expected_answer_check":{"judgment":"supported","reason":"The UniProt entry for Q9RHD7 (WbpO, UDP-N-acetyl-D-glucosamine 6-dehydrogenase from Pseudomonas aeruginosa) explicitly states: 'Optimum temperature is between 37 and 42 degrees Celsius (PubMed:18065759).' This is direct experimental evidence (ECO:0000269). The sequence matches the benchmark exactly (422 aa, SHA256 confirmed). The organism P. aeruginosa is a mesophilic human pathogen with optimal growth at 37°C, fully consistent with the 37-42°C range.","evidence_ids":["C5","H6","C3"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The sequence encodes a Rossmann-fold NAD-dependent dehydrogenase (GXGXXG motif at positions 8-13: GLGYVGLP). Sequence composition analysis shows moderate densities of charged residues (D, E, K, R) forming potential salt bridges, moderate proline content, and a hydrophobic core without extreme stabilization features. These features are inconsistent with cold-adaptation (which would show very high glycine, low proline, reduced salt bridges → rules out C: 22-33) and inconsistent with thermophilic adaptation (which would show very high charged-residue density, elevated proline, reduced thermolabile residues → rules out D: 40-54). For the A vs B distinction: statistical patterns from mesophilic bacterial enzymes (learned from many homologs) show optima clustering near the organism's growth temperature, canonically 37°C for mesophiles. Option B (37-42) places the optimum AT 37°C, consistent with a standard mesophilic optimum, while option A (26-37) implies the optimum is below 37°C, more characteristic of psychrotolerant or soil mesophiles. The moderate salt-bridge density and absence of cold-adaptation signatures (no extreme glycine enrichment, no proline depletion) favor a canonical 37°C-centered optimum, making B more probable than A. Additionally, the enzyme's broad activity range (37-56°C per experimental data) is consistent with a mesophile that tolerates mild heat stress, aligning with the 37-42 optimum rather than a lower-centered range.","missing_item_specific_fact":"","reason":"The general mesophilic classification (ruling out C and D) is strongly supported by sequence composition. The A vs B distinction relies on the statistical regularity that canonical mesophilic bacterial enzymes have optima at ~37°C rather than below it, which is transferable knowledge from many homologous dehydrogenases. However, the specific 42°C upper bound is organism-specific (P. aeruginosa's known 42°C growth tolerance) and not strictly derivable from sequence alone, introducing some uncertainty."},"question_ambiguity":{"multiple_defensible_options":["A","B"],"reason":"Both A (26-37) and B (37-42) represent mesophilic ranges. Without organism identification, a model might reasonably assign a mesophilic enzyme to either range. The distinction depends on whether the optimum is centered at 37°C (B) or shifted lower (A), which is a subtle discrimination that general sequence composition alone does not definitively resolve."},"important_caveats":["The specific 42°C upper bound in the correct answer is an experimental measurement from PubMed:18065759 and is organism-specific (P. aeruginosa's thermal tolerance).","The A vs B distinction is the hardest part of this question; general mesophilic reasoning favors B but does not exclude A with certainty.","The UniProt annotation for this entry was first publicly released in 2025-02-05; the author's source snapshot timing is unknown.","The sequence is 422 amino acids matching Q9RHD7 exactly; no organism name or accession was provided to the evaluated model."]}
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
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"michaelisConstants\":[{\"constant\":0.047,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"substrate\":\"UDP-GlcNAc\",\"unit\":\"mM\"},{\"constant\":22.2,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10931835\",\"source\":\"PubMed\"}],\"substrate\":\"UDP-GlcNAc (refolded enzyme, in the presence of NAD(+))\",\"unit\":\"mM\"},{\"constant\":0.27,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"substrate\":\"UDP-GalNAc\",\"unit\":\"mM\"},{\"constant\":7.79,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10931835\",\"source\":\"PubMed\"}],\"substrate\":\"UDP-GalNAc (refolded enzyme, in the presence of NAD(+))\",\"unit\":\"mM\"},{\"constant\":0.23,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"substrate\":\"NAD(+)\",\"unit\":\"mM\"},{\"constant\":0.65,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10931835\",\"source\":\"PubMed\"}],\"substrate\":\"NAD(+) (refolded enzyme)\",\"unit\":\"mM\"},{\"constant\":3.7,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"substrate\":\"NADP(+)\",\"unit\":\"mM\"},{\"constant\":0.44,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10931835\",\"source\":\"PubMed\"}],\"substrate\":\"NADP(+) (refolded enzyme)\",\"unit\":\"mM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10931835\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"kcat is 110 min(-1) with UDP-GlcNAc as substrate. kcat is 0.69 min(-1) with UDP-GalNAc as substrate. kcat is 110 min(-1) with NAD(+) as substrate. kcat is 0.71 min(-1) with NADP(+) as substrate (PubMed:18065759). kcat is 5.5 min(-1) with UDP-GlcNAc as substrate (refolded enzyme, in the presence of NAD(+)). kcat is 47.8 min(-1) with UDP-GalNAc as substrate (refolded enzyme, in the presence of NAD(+)). kcat is 26.8 min(-1) with NAD(+) as substrate (refolded enzyme). kcat is 16.9 min(-1) with NADP(+) as substrate (refolded enzyme) (PubMed:10931835).\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10931835\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 8.5.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10931835\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"Activity is relatively constant over a wide temperature range from 37 to 56 degrees Celsius (PubMed:10931835). Optimum temperature is between 37 and 42 degrees Celsius (PubMed:18065759).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
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
  "excerpt": "{\"citation\":{\"authors\":[\"Zhao X.\",\"Creuzenet C.\",\"Belanger M.\",\"Egbosimba E.\",\"Li J.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10931835\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m004191200\"}],\"citationType\":\"journal article\",\"firstPage\":\"33252\",\"id\":\"10931835\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"33259\",\"publicationDate\":\"2000\",\"title\":\"WbpO, a UDP-N-acetyl-D-galactosamine dehydrogenase from Pseudomonas aeruginosa serotype O6.\",\"volume\":\"275\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
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
  "excerpt": "RN   [4]\nRP   FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=Serotype O6;\nRX   PubMed=10931835; DOI=10.1074/jbc.m004191200;\nRA   Zhao X., Creuzenet C., Belanger M., Egbosimba E., Li J., Lam J.S.;\nRT   \"WbpO, a UDP-N-acetyl-D-galactosamine dehydrogenase from Pseudomonas\nRT   aeruginosa serotype O6.\";\nRL   J. Biol. Chem. 275:33252-33259(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
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

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H6",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=0.047 mM for UDP-GlcNAc {ECO:0000269|PubMed:18065759};\nCC         KM=22.2 mM for UDP-GlcNAc (refolded enzyme, in the presence of\nCC         NAD(+)) {ECO:0000269|PubMed:10931835};\nCC         KM=0.27 mM for UDP-GalNAc {ECO:0000269|PubMed:18065759};\nCC         KM=7.79 mM for UDP-GalNAc (refolded enzyme, in the presence of\nCC         NAD(+)) {ECO:0000269|PubMed:10931835};\nCC         KM=0.23 mM for NAD(+) {ECO:0000269|PubMed:18065759};\nCC         KM=0.65 mM for NAD(+) (refolded enzyme)\nCC         {ECO:0000269|PubMed:10931835};\nCC         KM=3.7 mM for NADP(+) {ECO:0000269|PubMed:18065759};\nCC         KM=0.44 mM for NADP(+) (refolded enzyme)\nCC         {ECO:0000269|PubMed:10931835};\nCC         Note=kcat is 110 min(-1) with UDP-GlcNAc as substrate. kcat is 0.69\nCC         min(-1) with UDP-GalNAc as substrate. kcat is 110 min(-1) with NAD(+)\nCC         as substrate. kcat is 0.71 min(-1) with NADP(+) as substrate\nCC         (PubMed:18065759). kcat is 5.5 min(-1) with UDP-GlcNAc as substrate\nCC         (refolded enzyme, in the presence of NAD(+)). kcat is 47.8 min(-1)\nCC         with UDP-GalNAc as substrate (refolded enzyme, in the presence of\nCC         NAD(+)). kcat is 26.8 min(-1) with NAD(+) as substrate (refolded\nCC         enzyme). kcat is 16.9 min(-1) with NADP(+) as substrate (refolded\nCC         enzyme) (PubMed:10931835). {ECO:0000269|PubMed:10931835,\nCC         ECO:0000269|PubMed:18065759};\nCC       pH dependence:\nCC         Optimum pH is 8.5. {ECO:0000269|PubMed:10931835,\nCC         ECO:0000269|PubMed:18065759};\nCC       Temperature dependence:\nCC         Activity is relatively constant over a wide temperature range from 37\nCC         to 56 degrees Celsius (PubMed:10931835). Optimum temperature is\nCC         between 37 and 42 degrees Celsius (PubMed:18065759).\nCC         {ECO:0000269|PubMed:10931835, ECO:0000269|PubMed:18065759};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
