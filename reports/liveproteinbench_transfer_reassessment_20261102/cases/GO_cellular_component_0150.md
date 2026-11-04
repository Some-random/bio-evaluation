# GO_cellular_component_0150

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0150.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTSSDSAMVNHTPSPWYKFGFKSFAEFNTYVTFVFLGMSIMMVASAVTSAPDFLTRYYVYATGDPDAVAETPLFWNNANTFYNAGTYVLQVLTELFSLTPFMRRIPLSVRLFVGLGIPFAELLLIIIVPAATIKSQHGAIAVIMVVACVGGFSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALLMSIIQIILKVSMGTSFHDILTMSRIYFGICIGIQLFAIFELAILRFNPFAQKYIAEYRAGAQRNAQNNESTLEETAPSMNEPAAGDIADLPATVDDKERALNEEEGDEVRAVTSEEFHVKRGAVLTATGDADKMVDLDQTGNITSTEQLLRASAASVFKRVYPMLVCVFLIYFTSLLTFPGVFFLVSTTSGWYMTVIVTLFNAGDFISRMVLMFRPLRPSPKVVVAGTLGRLIIIPFLVLCVRGIIRGEALPYVLITLLGLTNGYFGCMACIHCPRTTTLRYAGERSLAAMLSGISIMLGLCFGSNLSLAITLTH

[Multiple Choices]
A. host cell plasma membrane
B. plasma membrane
C. vacuolar membrane
D. microtubule
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

> For the sequence-matched protein, UniProt records cell-membrane localization with experimental evidence attributed to PubMed 20037157; its GO plasma-membrane annotation is computationally assigned. These support B, while the GO annotation’s evidence type should not be mistaken for experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The many hydrophobic stretches indicate a multipass membrane protein, and the sequence is consistent with the equilibrative nucleoside-transporter family. Transferable knowledge that such transporters commonly mediate nucleoside uptake across the cell surface makes plasma membrane (B) a credible choice over microtubule (D) or vacuolar membrane (C). Nothing in the input suggests localization on a host cell’s membrane (A).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a meaningful, though probabilistic, localization inference from membrane-protein topology and transporter-family patterns. It does not prove the localization experimentally or exclude every intracellular membrane possibility.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence and transporter-like features favor the cell surface among the offered choices; the host-cell qualifier distinguishes A from the protein’s own plasma membrane.


### Important caveats

- The experimental support is a database attribution to a cited publication, not an independent review of that study here.
- The GO plasma-membrane annotation is marked IEA:UniProtKB-SubCell, a computational annotation.
- The source entry matches the sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic stretches indicate a multipass membrane protein, and the sequence is consistent with the equilibrative nucleoside-transporter family. Transferable knowledge that such transporters commonly mediate nucleoside uptake across the cell surface makes plasma membrane (B) a credible choice over microtubule (D) or vacuolar membrane (C). Nothing in the input suggests localization on a host cell’s membrane (A).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a meaningful, though probabilistic, localization inference from membrane-protein topology and transporter-family patterns. It does not prove the localization experimentally or exclude every intracellular membrane possibility."
  },
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "For the sequence-matched protein, UniProt records cell-membrane localization with experimental evidence attributed to PubMed 20037157; its GO plasma-membrane annotation is computationally assigned. These support B, while the GO annotation’s evidence type should not be mistaken for experimental evidence."
  },
  "important_caveats": [
    "The experimental support is a database attribution to a cited publication, not an independent review of that study here.",
    "The GO plasma-membrane annotation is marked IEA:UniProtKB-SubCell, a computational annotation.",
    "The source entry matches the sequence, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and transporter-like features favor the cell surface among the offered choices; the host-cell qualifier distinguishes A from the protein’s own plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "For the sequence-matched protein, UniProt records cell-membrane localization with experimental evidence attributed to PubMed 20037157; its GO plasma-membrane annotation is computationally assigned. These support B, while the GO annotation’s evidence type should not be mistaken for experimental evidence.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The many hydrophobic stretches indicate a multipass membrane protein, and the sequence is consistent with the equilibrative nucleoside-transporter family. Transferable knowledge that such transporters commonly mediate nucleoside uptake across the cell surface makes plasma membrane (B) a credible choice over microtubule (D) or vacuolar membrane (C). Nothing in the input suggests localization on a host cell’s membrane (A).",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a meaningful, though probabilistic, localization inference from membrane-protein topology and transporter-family patterns. It does not prove the localization experimentally or exclude every intracellular membrane possibility."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and transporter-like features favor the cell surface among the offered choices; the host-cell qualifier distinguishes A from the protein’s own plasma membrane."
  },
  "important_caveats": [
    "The experimental support is a database attribution to a cited publication, not an independent review of that study here.",
    "The GO plasma-membrane annotation is marked IEA:UniProtKB-SubCell, a computational annotation.",
    "The source entry matches the sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein (Q9GTP4, Nucleoside transporter 2 from Crithidia fasciculata) as 'Cell membrane; Multi-pass membrane protein' with direct assay evidence (ECO:0000269, PubMed:20037157). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The protein's function as an equilibrative nucleoside transporter, experimentally characterized to mediate nucleoside uptake across the cell boundary, is consistent with plasma membrane localization. The sequence contains ~11 hydrophobic transmembrane segments consistent with multi-pass membrane topology.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> 1) The sequence displays ~11 long hydrophobic stretches (~20+ residues) separated by hydrophilic loops, clearly indicating a multi-pass membrane protein, which eliminates microtubule (D). 2) 'Host cell plasma membrane' (GO:0020002) is a GO term specifically in the goslim_virus subset, defined as 'The plasma membrane surrounding a host cell'—it applies to viral or viral-associated proteins in the context of host infection. A protein from a free-living unicellular protozoan (Crithidia) is the cell itself, not a virus infecting a host, so this term is inapplicable, eliminating A. 3) Equilibrative nucleoside transporters (ENT family) are universally characterized as plasma membrane proteins across organisms (human ENT1-4, bacterial ENT homologs, Leishmania/Trypanosoma nucleoside transporters), serving as the primary route for nucleoside/nucleobase uptake from the extracellular environment. In a unicellular organism, the plasma membrane is the primary interface for nutrient acquisition, making vacuolar membrane (C) a much less likely primary location for a nutrient uptake transporter. 4) The overall topology pattern (11 TMs, N-terminal cytoplasmic tail, alternating loops) is consistent with the well-studied ENT/MFS-type transporter architecture at the plasma membrane.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use: (a) sequence hydrophobicity analysis to confirm multi-pass membrane topology and exclude microtubule; (b) GO ontology knowledge that 'host cell plasma membrane' is a virus-specific term (goslim_virus subset) inapplicable to a free-living protozoan's own membrane; (c) family-level knowledge that equilibrative nucleoside transporters are plasma membrane proteins across diverse organisms; (d) the biological principle that nutrient uptake transporters in unicellular organisms localize to the plasma membrane rather than intracellular compartments. These transferable arguments meaningfully distinguish B from A, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A (host cell plasma membrane) is clearly distinguished from B (plasma membrane) by the GO ontology: GO:0020002 is a virus-specific term (goslim_virus subset) referring to the host's membrane during infection, not the organism's own membrane. Option D (microtubule) is eliminated by the obvious multi-pass membrane topology. Option C (vacuolar membrane) is disfavored by the well-established family-level pattern of nucleoside transporters localizing to the plasma membrane for extracellular nutrient uptake. The expected answer B is uniquely defensible.


### Important caveats

- The GO annotation for this protein is IEA (Inferred from Electronic Annotation) via UniProtKB-SubCell, but the underlying UniProt annotation has direct assay evidence (ECO:0000269) from a mutagenesis/subcellular localization study.
- The sequence does not explicitly state the organism name in the user input; however, the multi-pass membrane topology and transporter-like architecture are recognizable from the sequence alone.
- The distinction between 'plasma membrane' and 'host cell plasma membrane' relies on GO ontology structure knowledge (goslim_virus subset membership), which is standard bioinformatics knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "1) The sequence displays ~11 long hydrophobic stretches (~20+ residues) separated by hydrophilic loops, clearly indicating a multi-pass membrane protein, which eliminates microtubule (D). 2) 'Host cell plasma membrane' (GO:0020002) is a GO term specifically in the goslim_virus subset, defined as 'The plasma membrane surrounding a host cell'—it applies to viral or viral-associated proteins in the context of host infection. A protein from a free-living unicellular protozoan (Crithidia) is the cell itself, not a virus infecting a host, so this term is inapplicable, eliminating A. 3) Equilibrative nucleoside transporters (ENT family) are universally characterized as plasma membrane proteins across organisms (human ENT1-4, bacterial ENT homologs, Leishmania/Trypanosoma nucleoside transporters), serving as the primary route for nucleoside/nucleobase uptake from the extracellular environment. In a unicellular organism, the plasma membrane is the primary interface for nutrient acquisition, making vacuolar membrane (C) a much less likely primary location for a nutrient uptake transporter. 4) The overall topology pattern (11 TMs, N-terminal cytoplasmic tail, alternating loops) is consistent with the well-studied ENT/MFS-type transporter architecture at the plasma membrane.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (a) sequence hydrophobicity analysis to confirm multi-pass membrane topology and exclude microtubule; (b) GO ontology knowledge that 'host cell plasma membrane' is a virus-specific term (goslim_virus subset) inapplicable to a free-living protozoan's own membrane; (c) family-level knowledge that equilibrative nucleoside transporters are plasma membrane proteins across diverse organisms; (d) the biological principle that nutrient uptake transporters in unicellular organisms localize to the plasma membrane rather than intracellular compartments. These transferable arguments meaningfully distinguish B from A, C, and D."
  },
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (Q9GTP4, Nucleoside transporter 2 from Crithidia fasciculata) as 'Cell membrane; Multi-pass membrane protein' with direct assay evidence (ECO:0000269, PubMed:20037157). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The protein's function as an equilibrative nucleoside transporter, experimentally characterized to mediate nucleoside uptake across the cell boundary, is consistent with plasma membrane localization. The sequence contains ~11 hydrophobic transmembrane segments consistent with multi-pass membrane topology."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (Inferred from Electronic Annotation) via UniProtKB-SubCell, but the underlying UniProt annotation has direct assay evidence (ECO:0000269) from a mutagenesis/subcellular localization study.",
    "The sequence does not explicitly state the organism name in the user input; however, the multi-pass membrane topology and transporter-like architecture are recognizable from the sequence alone.",
    "The distinction between 'plasma membrane' and 'host cell plasma membrane' relies on GO ontology structure knowledge (goslim_virus subset membership), which is standard bioinformatics knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (host cell plasma membrane) is clearly distinguished from B (plasma membrane) by the GO ontology: GO:0020002 is a virus-specific term (goslim_virus subset) referring to the host's membrane during infection, not the organism's own membrane. Option D (microtubule) is eliminated by the obvious multi-pass membrane topology. Option C (vacuolar membrane) is disfavored by the well-established family-level pattern of nucleoside transporters localizing to the plasma membrane for extracellular nutrient uptake. The expected answer B is uniquely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (Q9GTP4, Nucleoside transporter 2 from Crithidia fasciculata) as 'Cell membrane; Multi-pass membrane protein' with direct assay evidence (ECO:0000269, PubMed:20037157). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The protein's function as an equilibrative nucleoside transporter, experimentally characterized to mediate nucleoside uptake across the cell boundary, is consistent with plasma membrane localization. The sequence contains ~11 hydrophobic transmembrane segments consistent with multi-pass membrane topology.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "1) The sequence displays ~11 long hydrophobic stretches (~20+ residues) separated by hydrophilic loops, clearly indicating a multi-pass membrane protein, which eliminates microtubule (D). 2) 'Host cell plasma membrane' (GO:0020002) is a GO term specifically in the goslim_virus subset, defined as 'The plasma membrane surrounding a host cell'—it applies to viral or viral-associated proteins in the context of host infection. A protein from a free-living unicellular protozoan (Crithidia) is the cell itself, not a virus infecting a host, so this term is inapplicable, eliminating A. 3) Equilibrative nucleoside transporters (ENT family) are universally characterized as plasma membrane proteins across organisms (human ENT1-4, bacterial ENT homologs, Leishmania/Trypanosoma nucleoside transporters), serving as the primary route for nucleoside/nucleobase uptake from the extracellular environment. In a unicellular organism, the plasma membrane is the primary interface for nutrient acquisition, making vacuolar membrane (C) a much less likely primary location for a nutrient uptake transporter. 4) The overall topology pattern (11 TMs, N-terminal cytoplasmic tail, alternating loops) is consistent with the well-studied ENT/MFS-type transporter architecture at the plasma membrane.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (a) sequence hydrophobicity analysis to confirm multi-pass membrane topology and exclude microtubule; (b) GO ontology knowledge that 'host cell plasma membrane' is a virus-specific term (goslim_virus subset) inapplicable to a free-living protozoan's own membrane; (c) family-level knowledge that equilibrative nucleoside transporters are plasma membrane proteins across diverse organisms; (d) the biological principle that nutrient uptake transporters in unicellular organisms localize to the plasma membrane rather than intracellular compartments. These transferable arguments meaningfully distinguish B from A, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (host cell plasma membrane) is clearly distinguished from B (plasma membrane) by the GO ontology: GO:0020002 is a virus-specific term (goslim_virus subset) referring to the host's membrane during infection, not the organism's own membrane. Option D (microtubule) is eliminated by the obvious multi-pass membrane topology. Option C (vacuolar membrane) is disfavored by the well-established family-level pattern of nucleoside transporters localizing to the plasma membrane for extracellular nutrient uptake. The expected answer B is uniquely defensible."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (Inferred from Electronic Annotation) via UniProtKB-SubCell, but the underlying UniProt annotation has direct assay evidence (ECO:0000269) from a mutagenesis/subcellular localization study.",
    "The sequence does not explicitly state the organism name in the user input; however, the multi-pass membrane topology and transporter-like architecture are recognizable from the sequence alone.",
    "The distinction between 'plasma membrane' and 'host cell plasma membrane' relies on GO ontology structure knowledge (goslim_virus subset membership), which is standard bioinformatics knowledge."
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
  "benchmark_sequence_length": 502,
  "benchmark_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "current_entry_audit": {
    "entryVersion": 55,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2001-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 502,
  "current_source_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9GTP4",
  "selected_historical_entry_version": 55,
  "selected_historical_record_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "selected_historical_source_sequence_length": 502,
  "selected_historical_source_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "selected_historical_version": {
    "accession": "Q9GTP4",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NT2_CRIFA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9GTP4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":55,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2001-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAG22611.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Crithidia\"],\"scientificName\":\"Crithidia fasciculata\",\"taxonId\":5656}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"value\":\"Equilibrative nucleoside transporter 2\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"value\":\"CfNT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu W.\",\"Arendt C.S.\",\"Gessford S.K.\",\"Ntaba D.\",\"Carter N.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15694482\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2004.11.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"15694482\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"12\",\"publicationDate\":\"2005\",\"title\":\"Identification and characterization of purine nucleoside transporters from Crithidia fasciculata.\",\"volume\":\"140\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20037157\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.074351\"}],\"citationType\":\"journal article\",\"firstPage\":\"6024\",\"id\":\"20037157\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"6035\",\"publicationDate\":\"2010\",\"title\":\"Role of transmembrane domain 4 in ligand permeation by Crithidia fasciculata equilibrative nucleoside transporter 2 (CfNT2).\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF VAL-89; HIS-138; GLY-139; ALA-140; ILE-141; ALA-142; VAL-143; ILE-144; MET-145; VAL-146; VAL-147; ALA-148; VAL-150; GLY-151; GLY-152; PHE-153; SER-154; LYS-155; ALA-156; LEU-157; ASP-159; SER-160; THR-162; ASN-163; ALA-164; LEU-165; VAL-166; GLY-167; PRO-168; PHE-169; PRO-170; THR-171 AND LYS-172\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H1",
  "excerpt": "ID   NT2_CRIFA               Reviewed;         502 AA.\nAC   Q9GTP4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2001, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=Nucleoside transporter 2 {ECO:0000303|PubMed:15694482};\nDE            Short=CfNT2 {ECO:0000303|PubMed:15694482, ECO:0000303|PubMed:20037157};\nDE   AltName: Full=Equilibrative nucleoside transporter 2 {ECO:0000303|PubMed:20037157};\nOS   Crithidia fasciculata.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Crithidia.\nOX   NCBI_TaxID=5656 {ECO:0000312|EMBL:AAG22611.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   INDUCTION.\nRX   PubMed=15694482; DOI=10.1016/j.molbiopara.2004.11.018;\nRA   Liu W., Arendt C.S., Gessford S.K., Ntaba D., Carter N.S., Ullman B.;\nRT   \"Identification and characterization of purine nucleoside transporters from\nRT   Crithidia fasciculata.\";\nRL   Mol. Biochem. Parasitol. 140:1-12(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, SUBCELLULAR LOCATION, AND MUTAGENESIS OF\nRP   VAL-89; HIS-138; GLY-139; ALA-140; ILE-141; ALA-142; VAL-143; ILE-144;\nRP   MET-145; VAL-146; VAL-147; ALA-148; VAL-150; GLY-151; GLY-152; PHE-153;\nRP   SER-154; LYS-155; ALA-156; LEU-157; ASP-159; SER-160; THR-162; ASN-163;\nRP   ALA-164; LEU-165; VAL-166; GLY-167; PRO-168; PHE-169; PRO-170; THR-171 AND\nRP   LYS-172.\nRX   PubMed=20037157; DOI=10.1074/jbc.m109.074351;\nRA   Arendt C.S., Ullman B.;\nRT   \"Role of transmembrane domain 4 in ligand permeation by Crithidia\nRT   fasciculata equilibrative nucleoside transporter 2 (CfNT2).\";\nRL   J. Biol. Chem. 285:6024-6035(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:20037157};\nCC       Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005774\nname: vacuolar membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the vacuole and separating its contents from the cytoplasm of the cell.\" [GOC:ai]\nis_a: GO:0098588 ! bounding membrane of organelle\nrelationship: part_of GO:0005773 ! vacuole\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005774",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59354-59361",
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
  "excerpt": "[Term]\nid: GO:0005874\nname: microtubule\nnamespace: cellular_component\ndef: \"Any of the long, generally straight, hollow tubes of internal diameter 12-15 nm and external diameter 24 nm found in a wide variety of eukaryotic cells; each consists (usually) of 13 protofilaments of polymeric tubulin, staggered in such a manner that the tubulin monomers are arranged in a helical pattern on the microtubular surface, and with the alpha/beta axes of the tubulin subunits parallel to the long axis of the tubule; exist in equilibrium with pool of tubulin monomers and can be rapidly assembled or disassembled in response to physiological stimuli; concerned with force generation, e.g. in the spindle.\" [ISBN:0879693568]\nsubset: goslim_metagenomics\nsynonym: \"microtubuli\" EXACT []\nsynonym: \"microtubulus\" EXACT []\nsynonym: \"neurotubule\" NARROW [NIF_Subcellular:sao248349196]\nxref: NIF_Subcellular:sao1846835077\nxref: Wikipedia:Microtubule\nis_a: GO:0099513 ! polymeric cytoskeletal fiber\nrelationship: part_of GO:0015630 ! microtubule cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005874",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60320-60333",
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
  "excerpt": "[Term]\nid: GO:0020002\nname: host cell plasma membrane\nnamespace: cellular_component\ndef: \"The plasma membrane surrounding a host cell.\" [GOC:mb]\nsubset: goslim_virus\nis_a: GO:0033644 ! host cell membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020002",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155120-155127",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 150. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
