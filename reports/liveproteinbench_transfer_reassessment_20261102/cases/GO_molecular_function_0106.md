# GO_molecular_function_0106

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0106.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — toxin activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKFCLIFLLLALTALHVKGSPIPDEESEETEDAEQEEDAEEEEHAEEEAQEDGDQTQDTDQESDDGQEETANQGSDEQQEEDGSHGTDETDDEAAGSRTEDVESGGDEQNDGEENGSQENGEEVTGGEDDSHGAQDSEGGEEDAAAQEAGGKKSKGKGAKGGQGSNRAGSSSGGEESAAHTYQEVMRILNGIKINAKEPLKSRLVNGLQYLKVDTINRVENIQKFSRIEHCFGNLDHIVQLYAGDAVERNDYCKGTCIDMVSNEFRGQMEELTSRLYPCLQGGYY

[Multiple Choices]
A. toxin activity
B. hydrolase activity, acting on glycosyl bonds
C. NADP binding
D. structural constituent of cell wall
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

> The matched protein has an experimentally reported role in inhibiting host platelet aggregation by blocking VWF interaction with collagen (C5, H3), consistent with a host-active toxin function. The toxin GO annotation itself is keyword-inferred rather than direct experimental evidence (H5), so the evidence supports the key without showing that toxin activity was independently established as a GO term experimentally.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment suggests secretion, and the sequence does not show an obvious glycosidase or NADP-binding signature. But secretion and lack of those signatures do not establish toxin activity: many secreted proteins are not toxins, and the input gives no organism, target, or host-active function.


**Missing item-specific fact**

> This protein's host-active role—blocking VWF interaction with collagen and inhibiting platelet aggregation—which supplies the basis for its toxin classification.


**Reason**

> The sequence offers weak clues about secretion but no sufficiently specific transferable feature or recognizable family-level inference that distinguishes toxin activity from other secreted-protein functions. The decisive functional evidence is specific to this protein and absent from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source supports toxin activity; none of the other options is supported by the supplied functional evidence.


### Important caveats

- The toxin GO annotation is IEA-based; the cited experimental function is platelet-aggregation inhibition, not a direct experimental assignment of the toxin GO term.
- The sequence matches the reviewed UniProt entry, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment suggests secretion, and the sequence does not show an obvious glycosidase or NADP-binding signature. But secretion and lack of those signatures do not establish toxin activity: many secreted proteins are not toxins, and the input gives no organism, target, or host-active function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "This protein's host-active role—blocking VWF interaction with collagen and inhibiting platelet aggregation—which supplies the basis for its toxin classification.",
    "reason": "The sequence offers weak clues about secretion but no sufficiently specific transferable feature or recognizable family-level inference that distinguishes toxin activity from other secreted-protein functions. The decisive functional evidence is specific to this protein and absent from the original input."
  },
  "case_id": "GO_molecular_function_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched protein has an experimentally reported role in inhibiting host platelet aggregation by blocking VWF interaction with collagen (C5, H3), consistent with a host-active toxin function. The toxin GO annotation itself is keyword-inferred rather than direct experimental evidence (H5), so the evidence supports the key without showing that toxin activity was independently established as a GO term experimentally."
  },
  "important_caveats": [
    "The toxin GO annotation is IEA-based; the cited experimental function is platelet-aggregation inhibition, not a direct experimental assignment of the toxin GO term.",
    "The sequence matches the reviewed UniProt entry, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source supports toxin activity; none of the other options is supported by the supplied functional evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein has an experimentally reported role in inhibiting host platelet aggregation by blocking VWF interaction with collagen (C5, H3), consistent with a host-active toxin function. The toxin GO annotation itself is keyword-inferred rather than direct experimental evidence (H5), so the evidence supports the key without showing that toxin activity was independently established as a GO term experimentally.",
    "evidence_ids": ["C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment suggests secretion, and the sequence does not show an obvious glycosidase or NADP-binding signature. But secretion and lack of those signatures do not establish toxin activity: many secreted proteins are not toxins, and the input gives no organism, target, or host-active function.",
    "missing_item_specific_fact": "This protein's host-active role—blocking VWF interaction with collagen and inhibiting platelet aggregation—which supplies the basis for its toxin classification.",
    "reason": "The sequence offers weak clues about secretion but no sufficiently specific transferable feature or recognizable family-level inference that distinguishes toxin activity from other secreted-protein functions. The decisive functional evidence is specific to this protein and absent from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source supports toxin activity; none of the other options is supported by the supplied functional evidence."
  },
  "important_caveats": [
    "The toxin GO annotation is IEA-based; the cited experimental function is platelet-aggregation inhibition, not a direct experimental assignment of the toxin GO term.",
    "The sequence matches the reviewed UniProt entry, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry D1FQ14 (Simplagrin, an Aegyptin-like protein from Simulium nigrimanum) carries GO:0090729 (toxin activity) as an IEA:UniProtKB-KW annotation (evidence_id H5), triggered by the 'Toxin' keyword. The GO:0090729 definition ('Interacting selectively with one or more biological molecules in another target organism, initiating pathogenesis/detrimental state') is applicable to a salivary gland protein that inhibits host platelet aggregation by blocking VWF-collagen interaction (experimental function per IDA evidence, H3/C5). However, the annotation is electronic (IEA) rather than experimentally validated (the IDA annotation is for collagen binding, GO:0005518). Among the four offered choices, only 'toxin activity' has any annotation in the record; the other three have none. The key is thus supported by the database annotation, albeit with weaker evidence than the primary experimental function.

Citations as saved: [H5](#evidence-h5), [H3](#evidence-h3), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence shows a clear N-terminal signal peptide (MKKFCLIFLLLALTALH), a long acidic region (abundant D/E residues), and a C-terminal structured domain with conserved cysteines (CKGTCIDM...CFPCLQ) typical of secreted insect proteins. (1) A secreted protein from an animal eliminates D (structural constituent of cell wall, which applies to plant/fungal/bacterial cell walls). (2) No Rossmann-fold or glycine-rich loop motifs are present, eliminating C (NADP binding). (3) No glycosidase catalytic motifs (e.g., conserved Glu/Asp pairs, TIM-barrel, or GH-family signatures) are present, eliminating B (hydrolase acting on glycosyl bonds). (4) The combination of signal peptide + acidic secreted region + cysteine-rich C-terminal domain matches the well-characterized pattern of salivary gland anti-hemostatic proteins from blood-feeding arthropods (e.g., Aegyptin from Aedes aegypti, Anophelin, tick anti-coagulants). These proteins interact with host hemostatic molecules (collagen, VWF, thrombin) to inhibit clotting during feeding, and in the GO framework such host-targeting salivary factors are classified under 'toxin activity' (GO:0090729: interacting with molecules in another organism to cause a detrimental state). This family-level inference from other blood-feeding arthropod salivary proteins meaningfully distinguishes A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of B, C, and D follows from standard sequence-feature analysis (signal peptide, absence of catalytic motifs, organism type). The positive identification of A relies on recognizing the salivary gland anti-hemostatic protein pattern common across blood-feeding arthropods (mosquitoes, ticks, black flies), which is transferable knowledge learned from homologous proteins like Aegyptin. The model does not need to recall this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only 'toxin activity' has any annotation in the UniProt record. The other three (hydrolase on glycosyl bonds, NADP binding, structural constituent of cell wall) are clearly incompatible with the sequence features and organism context. The primary experimental annotation (collagen binding, GO:0005518) is not offered as a choice, so no ambiguity arises among the provided alternatives.


### Important caveats

- The 'toxin activity' annotation is IEA (electronic, keyword-derived), not experimentally validated. The experimental (IDA) annotation is 'collagen binding,' which is not among the choices.
- The GO:0090729 definition requires 'initiating pathogenesis' or a 'detrimental state'; whether anti-hemostatic feeding strategy strictly qualifies as pathogenesis is a matter of interpretive judgment, though UniProt's keyword assignment treats it as such.
- The reviewer-only evidence identifies this as Simulium nigrimanum (black fly) protein Simpagrin/Aegyptin-like protein; this organism identity was not provided to the evaluated model. The model must infer insect origin from sequence features alone.
- The benchmark sequence matches the UniProt canonical sequence (286 AA, SHA256 confirmed) across both current and historical (v15) snapshots.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows a clear N-terminal signal peptide (MKKFCLIFLLLALTALH), a long acidic region (abundant D/E residues), and a C-terminal structured domain with conserved cysteines (CKGTCIDM...CFPCLQ) typical of secreted insect proteins. (1) A secreted protein from an animal eliminates D (structural constituent of cell wall, which applies to plant/fungal/bacterial cell walls). (2) No Rossmann-fold or glycine-rich loop motifs are present, eliminating C (NADP binding). (3) No glycosidase catalytic motifs (e.g., conserved Glu/Asp pairs, TIM-barrel, or GH-family signatures) are present, eliminating B (hydrolase acting on glycosyl bonds). (4) The combination of signal peptide + acidic secreted region + cysteine-rich C-terminal domain matches the well-characterized pattern of salivary gland anti-hemostatic proteins from blood-feeding arthropods (e.g., Aegyptin from Aedes aegypti, Anophelin, tick anti-coagulants). These proteins interact with host hemostatic molecules (collagen, VWF, thrombin) to inhibit clotting during feeding, and in the GO framework such host-targeting salivary factors are classified under 'toxin activity' (GO:0090729: interacting with molecules in another organism to cause a detrimental state). This family-level inference from other blood-feeding arthropod salivary proteins meaningfully distinguishes A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B, C, and D follows from standard sequence-feature analysis (signal peptide, absence of catalytic motifs, organism type). The positive identification of A relies on recognizing the salivary gland anti-hemostatic protein pattern common across blood-feeding arthropods (mosquitoes, ticks, black flies), which is transferable knowledge learned from homologous proteins like Aegyptin. The model does not need to recall this specific protein's database entry."
  },
  "case_id": "GO_molecular_function_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H3",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry D1FQ14 (Simplagrin, an Aegyptin-like protein from Simulium nigrimanum) carries GO:0090729 (toxin activity) as an IEA:UniProtKB-KW annotation (evidence_id H5), triggered by the 'Toxin' keyword. The GO:0090729 definition ('Interacting selectively with one or more biological molecules in another target organism, initiating pathogenesis/detrimental state') is applicable to a salivary gland protein that inhibits host platelet aggregation by blocking VWF-collagen interaction (experimental function per IDA evidence, H3/C5). However, the annotation is electronic (IEA) rather than experimentally validated (the IDA annotation is for collagen binding, GO:0005518). Among the four offered choices, only 'toxin activity' has any annotation in the record; the other three have none. The key is thus supported by the database annotation, albeit with weaker evidence than the primary experimental function."
  },
  "important_caveats": [
    "The 'toxin activity' annotation is IEA (electronic, keyword-derived), not experimentally validated. The experimental (IDA) annotation is 'collagen binding,' which is not among the choices.",
    "The GO:0090729 definition requires 'initiating pathogenesis' or a 'detrimental state'; whether anti-hemostatic feeding strategy strictly qualifies as pathogenesis is a matter of interpretive judgment, though UniProt's keyword assignment treats it as such.",
    "The reviewer-only evidence identifies this as Simulium nigrimanum (black fly) protein Simpagrin/Aegyptin-like protein; this organism identity was not provided to the evaluated model. The model must infer insect origin from sequence features alone.",
    "The benchmark sequence matches the UniProt canonical sequence (286 AA, SHA256 confirmed) across both current and historical (v15) snapshots."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'toxin activity' has any annotation in the UniProt record. The other three (hydrolase on glycosyl bonds, NADP binding, structural constituent of cell wall) are clearly incompatible with the sequence features and organism context. The primary experimental annotation (collagen binding, GO:0005518) is not offered as a choice, so no ambiguity arises among the provided alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry D1FQ14 (Simplagrin, an Aegyptin-like protein from Simulium nigrimanum) carries GO:0090729 (toxin activity) as an IEA:UniProtKB-KW annotation (evidence_id H5), triggered by the 'Toxin' keyword. The GO:0090729 definition ('Interacting selectively with one or more biological molecules in another target organism, initiating pathogenesis/detrimental state') is applicable to a salivary gland protein that inhibits host platelet aggregation by blocking VWF-collagen interaction (experimental function per IDA evidence, H3/C5). However, the annotation is electronic (IEA) rather than experimentally validated (the IDA annotation is for collagen binding, GO:0005518). Among the four offered choices, only 'toxin activity' has any annotation in the record; the other three have none. The key is thus supported by the database annotation, albeit with weaker evidence than the primary experimental function.",
    "evidence_ids": ["H5", "H3", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence shows a clear N-terminal signal peptide (MKKFCLIFLLLALTALH), a long acidic region (abundant D/E residues), and a C-terminal structured domain with conserved cysteines (CKGTCIDM...CFPCLQ) typical of secreted insect proteins. (1) A secreted protein from an animal eliminates D (structural constituent of cell wall, which applies to plant/fungal/bacterial cell walls). (2) No Rossmann-fold or glycine-rich loop motifs are present, eliminating C (NADP binding). (3) No glycosidase catalytic motifs (e.g., conserved Glu/Asp pairs, TIM-barrel, or GH-family signatures) are present, eliminating B (hydrolase acting on glycosyl bonds). (4) The combination of signal peptide + acidic secreted region + cysteine-rich C-terminal domain matches the well-characterized pattern of salivary gland anti-hemostatic proteins from blood-feeding arthropods (e.g., Aegyptin from Aedes aegypti, Anophelin, tick anti-coagulants). These proteins interact with host hemostatic molecules (collagen, VWF, thrombin) to inhibit clotting during feeding, and in the GO framework such host-targeting salivary factors are classified under 'toxin activity' (GO:0090729: interacting with molecules in another organism to cause a detrimental state). This family-level inference from other blood-feeding arthropod salivary proteins meaningfully distinguishes A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of B, C, and D follows from standard sequence-feature analysis (signal peptide, absence of catalytic motifs, organism type). The positive identification of A relies on recognizing the salivary gland anti-hemostatic protein pattern common across blood-feeding arthropods (mosquitoes, ticks, black flies), which is transferable knowledge learned from homologous proteins like Aegyptin. The model does not need to recall this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'toxin activity' has any annotation in the UniProt record. The other three (hydrolase on glycosyl bonds, NADP binding, structural constituent of cell wall) are clearly incompatible with the sequence features and organism context. The primary experimental annotation (collagen binding, GO:0005518) is not offered as a choice, so no ambiguity arises among the provided alternatives."
  },
  "important_caveats": [
    "The 'toxin activity' annotation is IEA (electronic, keyword-derived), not experimentally validated. The experimental (IDA) annotation is 'collagen binding,' which is not among the choices.",
    "The GO:0090729 definition requires 'initiating pathogenesis' or a 'detrimental state'; whether anti-hemostatic feeding strategy strictly qualifies as pathogenesis is a matter of interpretive judgment, though UniProt's keyword assignment treats it as such.",
    "The reviewer-only evidence identifies this as Simulium nigrimanum (black fly) protein Simpagrin/Aegyptin-like protein; this organism identity was not provided to the evaluated model. The model must infer insect origin from sequence features alone.",
    "The benchmark sequence matches the UniProt canonical sequence (286 AA, SHA256 confirmed) across both current and historical (v15) snapshots."
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
  "benchmark_sequence_length": 286,
  "benchmark_sequence_sha256": "c6b04aca6b77a300ece42f879e4e7416e0160e8a2e8105428c5cd707da8513d3",
  "current_entry_audit": {
    "entryVersion": 16,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-01-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "88c0577c4777ed337897699494ad0e6578b90fb06807269837ca558a7146d64d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 286,
  "current_source_sequence_sha256": "c6b04aca6b77a300ece42f879e4e7416e0160e8a2e8105428c5cd707da8513d3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 15,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D1FQ14",
  "selected_historical_entry_version": 15,
  "selected_historical_record_sha256": "8de32b2186869d34be804dc22af75b84f48c919a9b3d61df9d07a5f111d47c98",
  "selected_historical_source_sequence_length": 286,
  "selected_historical_source_sequence_sha256": "c6b04aca6b77a300ece42f879e4e7416e0160e8a2e8105428c5cd707da8513d3",
  "selected_historical_version": {
    "accession": "D1FQ14",
    "database": "Swiss-Prot",
    "entryVersion": 15,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "ALL3_SIMNI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1FQ14.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D1FQ14\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:01.644581+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "88c0577c4777ed337897699494ad0e6578b90fb06807269837ca558a7146d64d",
  "url": "https://rest.uniprot.org/uniprotkb/D1FQ14.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1FQ14.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":16,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-01-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:01.644581+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "88c0577c4777ed337897699494ad0e6578b90fb06807269837ca558a7146d64d",
  "url": "https://rest.uniprot.org/uniprotkb/D1FQ14.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1FQ14.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Black fly\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Chironomoidea\",\"Simuliidae\",\"Simulium\"],\"scientificName\":\"Simulium nigrimanum\",\"taxonId\":683695}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:01.644581+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "88c0577c4777ed337897699494ad0e6578b90fb06807269837ca558a7146d64d",
  "url": "https://rest.uniprot.org/uniprotkb/D1FQ14.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1FQ14.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24921659\",\"source\":\"PubMed\"}],\"value\":\"Aegyptin-like protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24921659\",\"source\":\"PubMed\"}],\"value\":\"Sim-50\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24921659\",\"source\":\"PubMed\"}],\"value\":\"Simplagrin\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:01.644581+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "88c0577c4777ed337897699494ad0e6578b90fb06807269837ca558a7146d64d",
  "url": "https://rest.uniprot.org/uniprotkb/D1FQ14.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1FQ14.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24921659\",\"source\":\"PubMed\"}],\"value\":\"Inhibits host platelet aggregation induced by low concentrations of collagen via blocking the von Willebrand Factor (VWF) interaction with collagen\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:01.644581+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "88c0577c4777ed337897699494ad0e6578b90fb06807269837ca558a7146d64d",
  "url": "https://rest.uniprot.org/uniprotkb/D1FQ14.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1FQ14.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"24921659\",\"source\":\"PubMed\"}],\"id\":\"GO:0005518\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:collagen binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-01T06:25:01.644581+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "88c0577c4777ed337897699494ad0e6578b90fb06807269837ca558a7146d64d",
  "url": "https://rest.uniprot.org/uniprotkb/D1FQ14.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D1FQ14.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Chagas A.C.\",\"McPhie P.\",\"San H.\",\"Narum D.\",\"Reiter K.\",\"Tokomasu F.\",\"Brayner F.A.\",\"Alves L.C.\",\"Ribeiro J.M.\",\"Calvo E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24921659\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pntd.0002947\"}],\"citationType\":\"journal article\",\"firstPage\":\"e2947\",\"id\":\"24921659\",\"journal\":\"PLoS Negl. Trop. Dis.\",\"lastPage\":\"e2947\",\"publicationDate\":\"2014\",\"title\":\"Simplagrin, a platelet aggregation inhibitor from Simulium nigrimanum salivary glands specifically binds to the Von Willebrand factor receptor in collagen and inhibits carotid thrombus formation in vivo.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"INTERACTION WITH HOST COLLAGEN\",\"GLYCOSYLATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:01.644581+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "88c0577c4777ed337897699494ad0e6578b90fb06807269837ca558a7146d64d",
  "url": "https://rest.uniprot.org/uniprotkb/D1FQ14.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H1",
  "excerpt": "ID   ALL3_SIMNI              Reviewed;         286 AA.\nAC   D1FQ14; D1FQ13; D1FQ20; D1FQ21;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-JAN-2010, sequence version 1.\nDT   28-JAN-2026, entry version 15.\nDE   RecName: Full=Simplagrin {ECO:0000303|PubMed:24921659};\nDE   AltName: Full=Aegyptin-like protein {ECO:0000303|PubMed:24921659};\nDE   AltName: Full=Sim-50 {ECO:0000303|PubMed:24921659};\nDE   Flags: Precursor;\nOS   Simulium nigrimanum (Black fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Chironomoidea; Simuliidae;\nOC   Simulium.\nOX   NCBI_TaxID=683695;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.014509+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8de32b2186869d34be804dc22af75b84f48c919a9b3d61df9d07a5f111d47c98",
  "url": "https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBUNIT, INTERACTION WITH HOST COLLAGEN, AND GLYCOSYLATION.\nRX   PubMed=24921659; DOI=10.1371/journal.pntd.0002947;\nRA   Chagas A.C., McPhie P., San H., Narum D., Reiter K., Tokomasu F.,\nRA   Brayner F.A., Alves L.C., Ribeiro J.M., Calvo E.;\nRT   \"Simplagrin, a platelet aggregation inhibitor from Simulium nigrimanum\nRT   salivary glands specifically binds to the Von Willebrand factor receptor in\nRT   collagen and inhibits carotid thrombus formation in vivo.\";\nRL   PLoS Negl. Trop. Dis. 8:e2947-e2947(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.014509+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8de32b2186869d34be804dc22af75b84f48c919a9b3d61df9d07a5f111d47c98",
  "url": "https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Inhibits host platelet aggregation induced by low\nCC       concentrations of collagen via blocking the von Willebrand Factor (VWF)\nCC       interaction with collagen. {ECO:0000269|PubMed:24921659}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.014509+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8de32b2186869d34be804dc22af75b84f48c919a9b3d61df9d07a5f111d47c98",
  "url": "https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005518; F:collagen binding; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.014509+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8de32b2186869d34be804dc22af75b84f48c919a9b3d61df9d07a5f111d47c98",
  "url": "https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0090729; F:toxin activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.014509+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8de32b2186869d34be804dc22af75b84f48c919a9b3d61df9d07a5f111d47c98",
  "url": "https://rest.uniprot.org/unisave/D1FQ14?format=txt&versions=15"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005199\nname: structural constituent of cell wall\nnamespace: molecular_function\ndef: \"The action of a molecule that contributes to the structural integrity of a cell wall.\" [GOC:mah]\nis_a: GO:0005198 ! structural molecule activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005199",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 54695-54701",
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
  "excerpt": "[Term]\nid: GO:0016798\nname: hydrolase activity, acting on glycosyl bonds\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of any glycosyl bond.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_yeast\nsynonym: \"glycosidase activity\" EXACT []\nsynonym: \"glycosylase\" NARROW []\nsynonym: \"N-glycosylase\" NARROW []\nxref: EC:3.2.-.-\nxref: Reactome:R-HSA-1793176 \"DS is cleaved from its proteoglycan\"\nxref: Reactome:R-HSA-2065233 \"CS is cleaved from its proteoglycan\"\nxref: Reactome:R-HSA-5333609 \"MeSebGalNac is hydrolysed to MeSeH and bGalNac\"\nis_a: GO:0016787 ! hydrolase activity\nproperty_value: skos:exactMatch EC:3.2.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016798",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130290-130307",
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
  "excerpt": "[Term]\nid: GO:0050661\nname: NADP binding\nnamespace: molecular_function\ndef: \"Binding to nicotinamide-adenine dinucleotide phosphate, a coenzyme involved in many redox and biosynthetic reactions; binding may be to either the oxidized form, NADP+, or the reduced form, NADPH.\" [GOC:ai]\nsynonym: \"NADP or NADPH binding\" RELATED [GOC:mah]\nsynonym: \"NADP+ or NADPH binding\" RELATED []\nsynonym: \"nicotinamide adenine dinucleotide phosphate binding\" EXACT []\nis_a: GO:0030554 ! adenyl nucleotide binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0050661",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 318403-318412",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
