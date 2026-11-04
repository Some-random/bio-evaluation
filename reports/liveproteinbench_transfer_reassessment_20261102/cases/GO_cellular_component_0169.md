# GO_cellular_component_0169

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0169.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDTAPDHREPQEQGESRKWYEMTASEFYVYVVAFMCGVSMMMPVNAVFSAPAYIMTYYRYAMQDPEAVPLYTNFWNNVMTYYNLIGIVTSLIMEPLTLLSWFRRIPMKVRLLGGLVILIVEIIVLMVVPARGTSEAGAVATICCTGFIGGFGKSIFESTTYGMFGAFPSSFTSTMMGGVGMSGVLTSLLQIIVKAALPDSYEGVKKQSKIYYGLDVGIQGMTFVALILLRFNSFAQNYFGDLGAVKSKVDAGKLSAEALCHTDEHPTHDKEGRNSSSGKEVPALGEVQTAAAKSEGPDAVEESSWPHEVEGPTSNEILVATAIFSTLRRVKWMFVACAFNFLITLFLFPGIAVGMFPDSKWFSTIAVFIFNVFDVLGRFSPSLKLMWPRSYKQRWIIVAASFARVIFVPLLLLHSYHYIPGEAYGYVMEVIFGFSNGYVGSMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRATY

[Multiple Choices]
A. lysosomal membrane
B. helical viral capsid
C. plasma membrane
D. histone acetyltransferase complex
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

> The exact sequence matches a UniProt record annotated to the cell membrane, with cited literature, and to plasma membrane by an electronic annotation. GO treats “cell membrane” as an exact synonym of “plasma membrane.” The sequence match supports applying these annotations to this protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has many hydrophobic segments consistent with a multipass membrane transporter, strongly favoring A or C over the viral capsid and histone acetyltransferase complex choices. Transferable knowledge of equilibrative nucleoside-transporter-like proteins provides a further basis for favoring the cell surface: these transporters commonly mediate nucleoside exchange across the plasma membrane, which distinguishes C from lysosomal membrane A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transporter-family pattern support a meaningful, probabilistic preference for plasma membrane among the offered choices. Multipass topology alone would not distinguish plasma from lysosomal membrane, and family-level tendencies do not prove this protein’s precise localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although generic membrane topology alone leaves A and C open, the transporter-family inference favors C; the provided annotations also support C.


### Important caveats

- The GO plasma-membrane annotation is electronic, while the UniProt cell-membrane annotation cites publications; the excerpts do not independently establish the experimental methods or strength of localization evidence.
- The original input does not provide the protein name, organism, or localization annotation; the answerability argument relies on transferable sequence-family and functional patterns, not those reviewer-only facts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many hydrophobic segments consistent with a multipass membrane transporter, strongly favoring A or C over the viral capsid and histone acetyltransferase complex choices. Transferable knowledge of equilibrative nucleoside-transporter-like proteins provides a further basis for favoring the cell surface: these transporters commonly mediate nucleoside exchange across the plasma membrane, which distinguishes C from lysosomal membrane A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transporter-family pattern support a meaningful, probabilistic preference for plasma membrane among the offered choices. Multipass topology alone would not distinguish plasma from lysosomal membrane, and family-level tendencies do not prove this protein’s precise localization."
  },
  "case_id": "GO_cellular_component_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to the cell membrane, with cited literature, and to plasma membrane by an electronic annotation. GO treats “cell membrane” as an exact synonym of “plasma membrane.” The sequence match supports applying these annotations to this protein."
  },
  "important_caveats": [
    "The GO plasma-membrane annotation is electronic, while the UniProt cell-membrane annotation cites publications; the excerpts do not independently establish the experimental methods or strength of localization evidence.",
    "The original input does not provide the protein name, organism, or localization annotation; the answerability argument relies on transferable sequence-family and functional patterns, not those reviewer-only facts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although generic membrane topology alone leaves A and C open, the transporter-family inference favors C; the provided annotations also support C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to the cell membrane, with cited literature, and to plasma membrane by an electronic annotation. GO treats “cell membrane” as an exact synonym of “plasma membrane.” The sequence match supports applying these annotations to this protein.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has many hydrophobic segments consistent with a multipass membrane transporter, strongly favoring A or C over the viral capsid and histone acetyltransferase complex choices. Transferable knowledge of equilibrative nucleoside-transporter-like proteins provides a further basis for favoring the cell surface: these transporters commonly mediate nucleoside exchange across the plasma membrane, which distinguishes C from lysosomal membrane A.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transporter-family pattern support a meaningful, probabilistic preference for plasma membrane among the offered choices. Multipass topology alone would not distinguish plasma from lysosomal membrane, and family-level tendencies do not prove this protein’s precise localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although generic membrane topology alone leaves A and C open, the transporter-family inference favors C; the provided annotations also support C."
  },
  "important_caveats": [
    "The GO plasma-membrane annotation is electronic, while the UniProt cell-membrane annotation cites publications; the excerpts do not independently establish the experimental methods or strength of localization evidence.",
    "The original input does not provide the protein name, organism, or localization annotation; the answerability argument relies on transferable sequence-family and functional patterns, not those reviewer-only facts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for O76343 (Nucleoside transporter 1.1, LdNT1.1) explicitly annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' based on experimental evidence from two PubMed publications (9707568, 12835315). The GO annotation GO:0005886 (plasma membrane) is assigned with evidence code IEA:UniProtKB-SubCell. The GO ontology confirms 'cell membrane' is an EXACT synonym of 'plasma membrane' (GO:0005886). The sequence matches the benchmark exactly (491 AA, SHA256 match). The expected answer C is well-supported by curator-inferred annotations backed by functional transporter studies.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays 11-12 hydrophobic transmembrane segments separated by short hydrophilic loops, characteristic of the ENT/NBT (equilibrative nucleoside/nucleobase transporter) superfamily. Key motifs such as 'GFIGGFG' and the overall 1+7+3 TM topology are hallmarks of this family. Across all characterized organisms (mammals, Drosophila, trypanosomatids), ENT/NBT family members are plasma membrane proteins that mediate nucleoside/nucleobase uptake from the extracellular environment. This family-level knowledge distinguishes C (plasma membrane) from A (lysosomal membrane): lysosomal membrane transporters belong to entirely different families (e.g., SLC, MFS) with distinct topologies. Options B (helical viral capsid) and D (histone acetyltransferase complex) are trivially excluded: the sequence is a large multi-pass membrane protein with no capsid self-assembly motifs and no acetyltransferase (GNAT) fold or nuclear localization signal. The argument relies on recognizing a well-known transporter family and the general principle that extracellular nutrient uptake transporters reside at the plasma membrane.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the multi-pass TM architecture as belonging to the ENT/NBT transporter superfamily from conserved sequence motifs and topology. Family-level knowledge establishes that these are plasma membrane nutrient-uptake transporters. This distinguishes C from A without needing the specific UniProt annotation for this exact protein. B and D are eliminated by basic structural/functional reasoning (membrane protein vs. capsid or nuclear complex).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span very different cellular compartments (lysosomal membrane, viral capsid, plasma membrane, nuclear protein complex). The sequence is unambiguously a multi-pass membrane transporter, eliminating B and D immediately. The ENT/NBT family assignment and the general principle that extracellular nucleoside uptake occurs at the plasma membrane cleanly favor C over A. No genuine ambiguity exists among the offered alternatives.


### Important caveats

- The GO annotation evidence code is IEA (inferred from electronic annotation), but the underlying UniProt 'Cell membrane' annotation carries ECO:0000305 (curator inference from publication), supported by functional transporter studies in Xenopus oocytes and transport-deficient mutant rescue.
- The protein is from Leishmania donovani, a protozoan where the lysosomal role is largely served by glycosomes; however, the ENT family argument for plasma membrane localization holds universally across eukaryotes.
- The reviewer-only evidence confirms sequence identity (O76343, 491 AA, SHA256 match) but this was not available to the evaluated model; the reasoning relies solely on sequence features and transferable family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays 11-12 hydrophobic transmembrane segments separated by short hydrophilic loops, characteristic of the ENT/NBT (equilibrative nucleoside/nucleobase transporter) superfamily. Key motifs such as 'GFIGGFG' and the overall 1+7+3 TM topology are hallmarks of this family. Across all characterized organisms (mammals, Drosophila, trypanosomatids), ENT/NBT family members are plasma membrane proteins that mediate nucleoside/nucleobase uptake from the extracellular environment. This family-level knowledge distinguishes C (plasma membrane) from A (lysosomal membrane): lysosomal membrane transporters belong to entirely different families (e.g., SLC, MFS) with distinct topologies. Options B (helical viral capsid) and D (histone acetyltransferase complex) are trivially excluded: the sequence is a large multi-pass membrane protein with no capsid self-assembly motifs and no acetyltransferase (GNAT) fold or nuclear localization signal. The argument relies on recognizing a well-known transporter family and the general principle that extracellular nutrient uptake transporters reside at the plasma membrane.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the multi-pass TM architecture as belonging to the ENT/NBT transporter superfamily from conserved sequence motifs and topology. Family-level knowledge establishes that these are plasma membrane nutrient-uptake transporters. This distinguishes C from A without needing the specific UniProt annotation for this exact protein. B and D are eliminated by basic structural/functional reasoning (membrane protein vs. capsid or nuclear complex)."
  },
  "case_id": "GO_cellular_component_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for O76343 (Nucleoside transporter 1.1, LdNT1.1) explicitly annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' based on experimental evidence from two PubMed publications (9707568, 12835315). The GO annotation GO:0005886 (plasma membrane) is assigned with evidence code IEA:UniProtKB-SubCell. The GO ontology confirms 'cell membrane' is an EXACT synonym of 'plasma membrane' (GO:0005886). The sequence matches the benchmark exactly (491 AA, SHA256 match). The expected answer C is well-supported by curator-inferred annotations backed by functional transporter studies."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA (inferred from electronic annotation), but the underlying UniProt 'Cell membrane' annotation carries ECO:0000305 (curator inference from publication), supported by functional transporter studies in Xenopus oocytes and transport-deficient mutant rescue.",
    "The protein is from Leishmania donovani, a protozoan where the lysosomal role is largely served by glycosomes; however, the ENT family argument for plasma membrane localization holds universally across eukaryotes.",
    "The reviewer-only evidence confirms sequence identity (O76343, 491 AA, SHA256 match) but this was not available to the evaluated model; the reasoning relies solely on sequence features and transferable family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different cellular compartments (lysosomal membrane, viral capsid, plasma membrane, nuclear protein complex). The sequence is unambiguously a multi-pass membrane transporter, eliminating B and D immediately. The ENT/NBT family assignment and the general principle that extracellular nucleoside uptake occurs at the plasma membrane cleanly favor C over A. No genuine ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for O76343 (Nucleoside transporter 1.1, LdNT1.1) explicitly annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' based on experimental evidence from two PubMed publications (9707568, 12835315). The GO annotation GO:0005886 (plasma membrane) is assigned with evidence code IEA:UniProtKB-SubCell. The GO ontology confirms 'cell membrane' is an EXACT synonym of 'plasma membrane' (GO:0005886). The sequence matches the benchmark exactly (491 AA, SHA256 match). The expected answer C is well-supported by curator-inferred annotations backed by functional transporter studies.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays 11-12 hydrophobic transmembrane segments separated by short hydrophilic loops, characteristic of the ENT/NBT (equilibrative nucleoside/nucleobase transporter) superfamily. Key motifs such as 'GFIGGFG' and the overall 1+7+3 TM topology are hallmarks of this family. Across all characterized organisms (mammals, Drosophila, trypanosomatids), ENT/NBT family members are plasma membrane proteins that mediate nucleoside/nucleobase uptake from the extracellular environment. This family-level knowledge distinguishes C (plasma membrane) from A (lysosomal membrane): lysosomal membrane transporters belong to entirely different families (e.g., SLC, MFS) with distinct topologies. Options B (helical viral capsid) and D (histone acetyltransferase complex) are trivially excluded: the sequence is a large multi-pass membrane protein with no capsid self-assembly motifs and no acetyltransferase (GNAT) fold or nuclear localization signal. The argument relies on recognizing a well-known transporter family and the general principle that extracellular nutrient uptake transporters reside at the plasma membrane.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the multi-pass TM architecture as belonging to the ENT/NBT transporter superfamily from conserved sequence motifs and topology. Family-level knowledge establishes that these are plasma membrane nutrient-uptake transporters. This distinguishes C from A without needing the specific UniProt annotation for this exact protein. B and D are eliminated by basic structural/functional reasoning (membrane protein vs. capsid or nuclear complex)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different cellular compartments (lysosomal membrane, viral capsid, plasma membrane, nuclear protein complex). The sequence is unambiguously a multi-pass membrane transporter, eliminating B and D immediately. The ENT/NBT family assignment and the general principle that extracellular nucleoside uptake occurs at the plasma membrane cleanly favor C over A. No genuine ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA (inferred from electronic annotation), but the underlying UniProt 'Cell membrane' annotation carries ECO:0000305 (curator inference from publication), supported by functional transporter studies in Xenopus oocytes and transport-deficient mutant rescue.",
    "The protein is from Leishmania donovani, a protozoan where the lysosomal role is largely served by glycosomes; however, the ENT family argument for plasma membrane localization holds universally across eukaryotes.",
    "The reviewer-only evidence confirms sequence identity (O76343, 491 AA, SHA256 match) but this was not available to the evaluated model; the reasoning relies solely on sequence features and transferable family knowledge."
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
  "benchmark_sequence_length": 491,
  "benchmark_sequence_sha256": "d64970eec213a81b1bb8c504a7b46c7621212ff726e7abba5ac1e9cf9ffc63c5",
  "current_entry_audit": {
    "entryVersion": 72,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-11-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 491,
  "current_source_sequence_sha256": "d64970eec213a81b1bb8c504a7b46c7621212ff726e7abba5ac1e9cf9ffc63c5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 70,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O76343",
  "selected_historical_entry_version": 70,
  "selected_historical_record_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "selected_historical_source_sequence_length": 491,
  "selected_historical_source_sequence_sha256": "d64970eec213a81b1bb8c504a7b46c7621212ff726e7abba5ac1e9cf9ffc63c5",
  "selected_historical_version": {
    "accession": "O76343",
    "database": "Swiss-Prot",
    "entryVersion": 70,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NT11_LEIDO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O76343\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":72,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-11-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32597.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Leishmania\"],\"scientificName\":\"Leishmania donovani\",\"taxonId\":5661}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"12835315\",\"source\":\"PubMed\"}],\"value\":\"Equilibrative nucleoside transporter 1.1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 1.1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"value\":\"LdNT1.1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"12835315\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Vasudevan G.\",\"Carter N.S.\",\"Drew M.E.\",\"Beverley S.M.\",\"Sanchez M.A.\",\"Seyfang A.\",\"Ullman B.\",\"Landfear S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9707568\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.95.17.9873\"}],\"citationType\":\"journal article\",\"firstPage\":\"9873\",\"id\":\"9707568\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"9878\",\"publicationDate\":\"1998\",\"title\":\"Cloning of Leishmania nucleoside transporter genes by rescue of a transport-deficient mutant.\",\"volume\":\"95\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32597.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32597.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"1S\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Stein A.\",\"Vaseduvan G.\",\"Carter N.S.\",\"Ullman B.\",\"Landfear S.M.\",\"Kavanaugh M.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12835315\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m306188200\"}],\"citationType\":\"journal article\",\"firstPage\":\"35127\",\"id\":\"12835315\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"35134\",\"publicationDate\":\"2003\",\"title\":\"Equilibrative nucleoside transporter family members from Leishmania donovani are electrogenic proton symporters.\",\"volume\":\"278\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:29:17.225994+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5",
  "url": "https://rest.uniprot.org/uniprotkb/O76343.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H1",
  "excerpt": "ID   NT11_LEIDO              Reviewed;         491 AA.\nAC   O76343;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-NOV-1998, sequence version 1.\nDT   28-JAN-2026, entry version 70.\nDE   RecName: Full=Nucleoside transporter 1.1 {ECO:0000303|PubMed:9707568};\nDE            Short=LdNT1.1 {ECO:0000303|PubMed:9707568};\nDE   AltName: Full=Equilibrative nucleoside transporter 1.1 {ECO:0000303|PubMed:12835315};\nGN   Name=NT1.1 {ECO:0000303|PubMed:9707568};\nGN   ORFNames=CGC20_30430 {ECO:0000312|EMBL:TPP53190.1},\nGN   LdCL_150017900 {ECO:0000312|EMBL:AYU77538.1},\nGN   LDHU3_15.1550 {ECO:0000312|EMBL:CAC5428821.1};\nOS   Leishmania donovani.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Leishmania.\nOX   NCBI_TaxID=5661 {ECO:0000312|EMBL:AAC32597.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAC32597.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, TRANSPORTER ACTIVITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=1S {ECO:0000312|EMBL:AAC32597.1};\nRX   PubMed=9707568; DOI=10.1073/pnas.95.17.9873;\nRA   Vasudevan G., Carter N.S., Drew M.E., Beverley S.M., Sanchez M.A.,\nRA   Seyfang A., Ullman B., Landfear S.M.;\nRT   \"Cloning of Leishmania nucleoside transporter genes by rescue of a\nRT   transport-deficient mutant.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 95:9873-9878(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, AND TRANSPORTER ACTIVITY.\nRX   PubMed=12835315; DOI=10.1074/jbc.m306188200;\nRA   Stein A., Vaseduvan G., Carter N.S., Ullman B., Landfear S.M.,\nRA   Kavanaugh M.P.;\nRT   \"Equilibrative nucleoside transporter family members from Leishmania\nRT   donovani are electrogenic proton symporters.\";\nRL   J. Biol. Chem. 278:35127-35134(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:12835315,\nCC       ECO:0000305|PubMed:9707568}; Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:19.110797+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c",
  "url": "https://rest.uniprot.org/unisave/O76343?format=txt&versions=70"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000123\nname: histone acetyltransferase complex\nnamespace: cellular_component\ndef: \"A protein complex that possesses histone acetyltransferase activity.\" [GOC:mah]\ncomment: Note that this term represents a protein complex, not a function; the activity possessed by this complex is mentioned in the definition for the purpose of describing and distinguishing the complex. The function of this complex is represented by the molecular function term 'histone acetyltransferase activity ; GO:0004402'.\nsynonym: \"histone acetylase complex\" EXACT []\nis_a: GO:0031248 ! protein acetyltransferase complex\nrelationship: part_of GO:0000785 ! chromatin\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000123",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1242-1251",
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
  "excerpt": "[Term]\nid: GO:0005765\nname: lysosomal membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the lysosome and separating its contents from the cell cytoplasm.\" [GOC:ai]\nsynonym: \"lysosome membrane\" EXACT []\nis_a: GO:0098852 ! lytic vacuole membrane\nrelationship: part_of GO:0005764 ! lysosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005765",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59259-59267",
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
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
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
  "excerpt": "[Term]\nid: GO:0019029\nname: helical viral capsid\nnamespace: cellular_component\ndef: \"The protein coat that surrounds the infective nucleic acid in some virus particles; the subunits are arranged to form a protein helix with the genetic material contained within. Tobacco mosaic virus has such a capsid structure.\" [ISBN:071673706X, UniProtKB-KW:KW-1139, VZ:885]\nis_a: GO:0019028 ! viral capsid\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019029",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 144666-144672",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 169. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
