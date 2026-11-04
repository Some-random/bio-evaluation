# GO_cellular_component_0084

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0084.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — nucleus

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAKTPIPFTTLNDLPDVILSNIIAAVSDTRSRNATALVCHKWLVLERSTRTSLTLRGNIRDLFMLPTCFRSITYLDLSLISPWGHPLLASRATDAPDNDSALIAHLLRHTFPSVTSLTLYARDPNTIQFLPAQWAHTLKHIKLVRWHQRAQLASGDELNLLFIGTPQITSLDLSNFYCWTDDVPPALQSNPNVACNLTRFNLLNASFPEGFKTDEIKVITKCCPNLKEFKVACMFDPRYIGFIGDEALVCLATNCPKLSVLHLADTSVLSNCRGDPNDEGFTVEDAQFSVSTLIEVFSGLSLLEELVFDVCNNVRDSGPALEILKTKCPKLRSLKLGQFHGISMPIESKLDGVALCQGLLSLSIRSVGDLDDMGLIGIGRGCSRLTKFEIECCKKITMRGMRTLASLLRKSLVDVTISCCKNLGASSSLKALEPIQDRIQRLHIDCVWDTVEEFENLDGVEYGFDLNEASGGEASSNPAGFGDTFGSMDDDLMNNRNKRCKYSYDLNSVYVENNGHGNGFCGRTWDRLQYLSLWIGVGELLTPLAAAGLQDCPKLEEIKIKVEGDCRLWSKPSERAFGLSTLIQYPKLVKMHLDCGDIIGYAHTAPSGQMDLSLWERFYLMGIRHLNLRELDYWPPQDRDVNQRSLSLPAAGLLQECVTLRKLFIHGTAHEHFMMFLLRIPNLRDVQLREDYYPAPENDMSTEMRADSLSRFEVALNRRQICD

[Multiple Choices]
A. nucleus
B. glutamatergic synapse
C. membrane
D. microneme
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

> The sequence-matched UniProt record reports experimentally supported nuclear localization and a nuclear GO annotation. It also reports cytoplasmic localization, so the evidence supports nucleus as a location but does not establish that it is exclusive or quantitatively primary.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an F-box/LRR-like architecture characteristic of intracellular SCF ubiquitin-ligase substrate receptors. Such proteins are soluble signaling regulators that can access the nucleus and cytoplasm; the sequence lacks an obvious transmembrane segment or secretory signal. This makes nucleus a credible choice over membrane, the neuron-specific glutamatergic synapse, or the apicomplexan microneme. This is a family-level probabilistic inference, not proof of this protein's localization.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable recognition of the F-box/LRR protein architecture meaningfully distinguishes the nuclear option from the offered alternatives, even though the sequence alone cannot establish the exact localization or its relative prominence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports both nuclear and cytoplasmic localization, but cytoplasm is not an offered choice. Among the listed alternatives, nucleus is the supported and most plausible option.


### Important caveats

- The source annotates both nucleus and cytoplasm; it does not demonstrate that nuclear localization is quantitatively primary.
- Reviewer-only annotations support the key but were not available as input for the transferability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an F-box/LRR-like architecture characteristic of intracellular SCF ubiquitin-ligase substrate receptors. Such proteins are soluble signaling regulators that can access the nucleus and cytoplasm; the sequence lacks an obvious transmembrane segment or secretory signal. This makes nucleus a credible choice over membrane, the neuron-specific glutamatergic synapse, or the apicomplexan microneme. This is a family-level probabilistic inference, not proof of this protein's localization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of the F-box/LRR protein architecture meaningfully distinguishes the nuclear option from the offered alternatives, even though the sequence alone cannot establish the exact localization or its relative prominence."
  },
  "case_id": "GO_cellular_component_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimentally supported nuclear localization and a nuclear GO annotation. It also reports cytoplasmic localization, so the evidence supports nucleus as a location but does not establish that it is exclusive or quantitatively primary."
  },
  "important_caveats": [
    "The source annotates both nucleus and cytoplasm; it does not demonstrate that nuclear localization is quantitatively primary.",
    "Reviewer-only annotations support the key but were not available as input for the transferability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports both nuclear and cytoplasmic localization, but cytoplasm is not an offered choice. Among the listed alternatives, nucleus is the supported and most plausible option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimentally supported nuclear localization and a nuclear GO annotation. It also reports cytoplasmic localization, so the evidence supports nucleus as a location but does not establish that it is exclusive or quantitatively primary.",
    "evidence_ids": ["C5", "C7", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an F-box/LRR-like architecture characteristic of intracellular SCF ubiquitin-ligase substrate receptors. Such proteins are soluble signaling regulators that can access the nucleus and cytoplasm; the sequence lacks an obvious transmembrane segment or secretory signal. This makes nucleus a credible choice over membrane, the neuron-specific glutamatergic synapse, or the apicomplexan microneme. This is a family-level probabilistic inference, not proof of this protein's localization.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of the F-box/LRR protein architecture meaningfully distinguishes the nuclear option from the offered alternatives, even though the sequence alone cannot establish the exact localization or its relative prominence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports both nuclear and cytoplasmic localization, but cytoplasm is not an offered choice. Among the listed alternatives, nucleus is the supported and most plausible option."
  },
  "important_caveats": [
    "The source annotates both nucleus and cytoplasm; it does not demonstrate that nuclear localization is quantitatively primary.",
    "Reviewer-only annotations support the key but were not available as input for the transferability judgment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (I1SSI6, PhMAX2B) annotates subcellular location as both Nucleus and Cytoplasm with experimental evidence (ECO:0000269, PubMed:38513014). GO annotations include GO:0005634 (nucleus, IDA) and GO:0005737 (cytoplasm, IDA), plus GO:0019005 (SCF ubiquitin ligase complex, IEA). Nucleus is listed first in the subcellular location comment and is the primary functional compartment for SCF-mediated ubiquitin ligase activity. Among the four offered choices (nucleus, glutamatergic synapse, membrane, microneme), nucleus is the only one supported by the annotation. Cytoplasm is also annotated but is not among the options, so the expected answer of nucleus is well-supported.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a clear F-box + LRR (leucine-rich repeat) architecture: an F-box motif near the N-terminus followed by numerous LxxLxLxxNxL repeat patterns spanning the C-terminal region. This architecture is the hallmark of FBXL proteins, which serve as substrate-recognition subunits of SCF (Skp1-Cullin1-F-box) E3 ubiquitin ligase complexes. SCF complexes are predominantly nuclear, especially in plants, where F-box proteins such as MAX2 (D3 in rice, AtMAX2 in Arabidopsis), GID2, and COI1 function in nuclear hormone-signaling pathways (strigolactone, gibberellin, jasmonate) by ubiquitinating transcription factors and signaling regulators. A knowledgeable model can recognize the F-box+LRR family signature from the sequence and infer nuclear localization from the well-established SCF complex biology. The other options are readily eliminable: glutamatergic synapse is a neuronal structure absent from plants; microneme is specific to apicomplexan parasites (Plasmodium, Toxoplasma); membrane localization is inconsistent with the soluble F-box+LRR architecture and the absence of transmembrane helices in the sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The F-box+LRR domain architecture is directly recognizable from the sequence itself. The nuclear localization of SCF ubiquitin ligase components, particularly plant F-box signaling proteins, is a well-established family-level pattern transferable from homologs (AtMAX2, OsD3, GID2, COI1). The three distractor options are eliminable through basic biological reasoning: synapses are neuronal, micronemes are apicomplexan-specific, and no transmembrane domains are present. This constitutes a concrete, credible inference from sequence features and transferable family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt annotation lists both nucleus and cytoplasm, cytoplasm is not among the offered choices. Among the four options (nucleus, glutamatergic synapse, membrane, microneme), only nucleus is biologically plausible for a plant F-box+LRR SCF component. The other three options are clearly eliminable: glutamatergic synapse is a neuronal term inapplicable to plants, microneme is restricted to apicomplexan parasites, and membrane lacks supporting evidence (no transmembrane domains, F-box proteins are soluble). No ambiguity among the offered alternatives.


### Important caveats

- The UniProt annotation lists both Nucleus and Cytoplasm as experimental subcellular locations; however, cytoplasm is not among the answer choices, so this does not create ambiguity among the offered options.
- The SCF ubiquitin ligase complex annotation (GO:0019005) is IEA (inferred by electronic annotation via TreeGrafter), not experimental, but the nuclear and cytoplasmic GO terms are IDA (Inferred from Direct Assay) from PubMed:38513014.
- The protein was identified as PhMAX2B from Petunia hybrida via reviewer-only UniProt accession I1SSI6; the evaluated model received only the sequence without organism or name information.
- The F-box+LRR architecture and SCF nuclear localization inference rely on family-level knowledge from homologs (AtMAX2, OsD3, etc.) and general SCF biology, not on a target-specific database lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a clear F-box + LRR (leucine-rich repeat) architecture: an F-box motif near the N-terminus followed by numerous LxxLxLxxNxL repeat patterns spanning the C-terminal region. This architecture is the hallmark of FBXL proteins, which serve as substrate-recognition subunits of SCF (Skp1-Cullin1-F-box) E3 ubiquitin ligase complexes. SCF complexes are predominantly nuclear, especially in plants, where F-box proteins such as MAX2 (D3 in rice, AtMAX2 in Arabidopsis), GID2, and COI1 function in nuclear hormone-signaling pathways (strigolactone, gibberellin, jasmonate) by ubiquitinating transcription factors and signaling regulators. A knowledgeable model can recognize the F-box+LRR family signature from the sequence and infer nuclear localization from the well-established SCF complex biology. The other options are readily eliminable: glutamatergic synapse is a neuronal structure absent from plants; microneme is specific to apicomplexan parasites (Plasmodium, Toxoplasma); membrane localization is inconsistent with the soluble F-box+LRR architecture and the absence of transmembrane helices in the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The F-box+LRR domain architecture is directly recognizable from the sequence itself. The nuclear localization of SCF ubiquitin ligase components, particularly plant F-box signaling proteins, is a well-established family-level pattern transferable from homologs (AtMAX2, OsD3, GID2, COI1). The three distractor options are eliminable through basic biological reasoning: synapses are neuronal, micronemes are apicomplexan-specific, and no transmembrane domains are present. This constitutes a concrete, credible inference from sequence features and transferable family knowledge."
  },
  "case_id": "GO_cellular_component_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "H4",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (I1SSI6, PhMAX2B) annotates subcellular location as both Nucleus and Cytoplasm with experimental evidence (ECO:0000269, PubMed:38513014). GO annotations include GO:0005634 (nucleus, IDA) and GO:0005737 (cytoplasm, IDA), plus GO:0019005 (SCF ubiquitin ligase complex, IEA). Nucleus is listed first in the subcellular location comment and is the primary functional compartment for SCF-mediated ubiquitin ligase activity. Among the four offered choices (nucleus, glutamatergic synapse, membrane, microneme), nucleus is the only one supported by the annotation. Cytoplasm is also annotated but is not among the options, so the expected answer of nucleus is well-supported."
  },
  "important_caveats": [
    "The UniProt annotation lists both Nucleus and Cytoplasm as experimental subcellular locations; however, cytoplasm is not among the answer choices, so this does not create ambiguity among the offered options.",
    "The SCF ubiquitin ligase complex annotation (GO:0019005) is IEA (inferred by electronic annotation via TreeGrafter), not experimental, but the nuclear and cytoplasmic GO terms are IDA (Inferred from Direct Assay) from PubMed:38513014.",
    "The protein was identified as PhMAX2B from Petunia hybrida via reviewer-only UniProt accession I1SSI6; the evaluated model received only the sequence without organism or name information.",
    "The F-box+LRR architecture and SCF nuclear localization inference rely on family-level knowledge from homologs (AtMAX2, OsD3, etc.) and general SCF biology, not on a target-specific database lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt annotation lists both nucleus and cytoplasm, cytoplasm is not among the offered choices. Among the four options (nucleus, glutamatergic synapse, membrane, microneme), only nucleus is biologically plausible for a plant F-box+LRR SCF component. The other three options are clearly eliminable: glutamatergic synapse is a neuronal term inapplicable to plants, microneme is restricted to apicomplexan parasites, and membrane lacks supporting evidence (no transmembrane domains, F-box proteins are soluble). No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (I1SSI6, PhMAX2B) annotates subcellular location as both Nucleus and Cytoplasm with experimental evidence (ECO:0000269, PubMed:38513014). GO annotations include GO:0005634 (nucleus, IDA) and GO:0005737 (cytoplasm, IDA), plus GO:0019005 (SCF ubiquitin ligase complex, IEA). Nucleus is listed first in the subcellular location comment and is the primary functional compartment for SCF-mediated ubiquitin ligase activity. Among the four offered choices (nucleus, glutamatergic synapse, membrane, microneme), nucleus is the only one supported by the annotation. Cytoplasm is also annotated but is not among the options, so the expected answer of nucleus is well-supported.",
    "evidence_ids": ["C5", "C7", "C8", "H4", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a clear F-box + LRR (leucine-rich repeat) architecture: an F-box motif near the N-terminus followed by numerous LxxLxLxxNxL repeat patterns spanning the C-terminal region. This architecture is the hallmark of FBXL proteins, which serve as substrate-recognition subunits of SCF (Skp1-Cullin1-F-box) E3 ubiquitin ligase complexes. SCF complexes are predominantly nuclear, especially in plants, where F-box proteins such as MAX2 (D3 in rice, AtMAX2 in Arabidopsis), GID2, and COI1 function in nuclear hormone-signaling pathways (strigolactone, gibberellin, jasmonate) by ubiquitinating transcription factors and signaling regulators. A knowledgeable model can recognize the F-box+LRR family signature from the sequence and infer nuclear localization from the well-established SCF complex biology. The other options are readily eliminable: glutamatergic synapse is a neuronal structure absent from plants; microneme is specific to apicomplexan parasites (Plasmodium, Toxoplasma); membrane localization is inconsistent with the soluble F-box+LRR architecture and the absence of transmembrane helices in the sequence.",
    "missing_item_specific_fact": "",
    "reason": "The F-box+LRR domain architecture is directly recognizable from the sequence itself. The nuclear localization of SCF ubiquitin ligase components, particularly plant F-box signaling proteins, is a well-established family-level pattern transferable from homologs (AtMAX2, OsD3, GID2, COI1). The three distractor options are eliminable through basic biological reasoning: synapses are neuronal, micronemes are apicomplexan-specific, and no transmembrane domains are present. This constitutes a concrete, credible inference from sequence features and transferable family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt annotation lists both nucleus and cytoplasm, cytoplasm is not among the offered choices. Among the four options (nucleus, glutamatergic synapse, membrane, microneme), only nucleus is biologically plausible for a plant F-box+LRR SCF component. The other three options are clearly eliminable: glutamatergic synapse is a neuronal term inapplicable to plants, microneme is restricted to apicomplexan parasites, and membrane lacks supporting evidence (no transmembrane domains, F-box proteins are soluble). No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The UniProt annotation lists both Nucleus and Cytoplasm as experimental subcellular locations; however, cytoplasm is not among the answer choices, so this does not create ambiguity among the offered options.",
    "The SCF ubiquitin ligase complex annotation (GO:0019005) is IEA (inferred by electronic annotation via TreeGrafter), not experimental, but the nuclear and cytoplasmic GO terms are IDA (Inferred from Direct Assay) from PubMed:38513014.",
    "The protein was identified as PhMAX2B from Petunia hybrida via reviewer-only UniProt accession I1SSI6; the evaluated model received only the sequence without organism or name information.",
    "The F-box+LRR architecture and SCF nuclear localization inference rely on family-level knowledge from homologs (AtMAX2, OsD3, etc.) and general SCF biology, not on a target-specific database lookup."
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
  "benchmark_sequence_length": 723,
  "benchmark_sequence_sha256": "c74acfde3f9c8733df57dd9dc981d1d7f7f596b3f3b501c3898547160276b089",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2012-07-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 723,
  "current_source_sequence_sha256": "c74acfde3f9c8733df57dd9dc981d1d7f7f596b3f3b501c3898547160276b089",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 20,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "I1SSI6",
  "selected_historical_entry_version": 20,
  "selected_historical_record_sha256": "a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab",
  "selected_historical_source_sequence_length": 723,
  "selected_historical_source_sequence_sha256": "c74acfde3f9c8733df57dd9dc981d1d7f7f596b3f3b501c3898547160276b089",
  "selected_historical_version": {
    "accession": "I1SSI6",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MAX2B_PETHY",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"I1SSI6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2012-07-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Petunia\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Solanales\",\"Solanaceae\",\"Petunioideae\",\"Petunia\"],\"scientificName\":\"Petunia hybrida\",\"taxonId\":4102}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22645562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38513014\",\"source\":\"PubMed\"}],\"value\":\"F-box protein MAX2 homolog B\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22645562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38513014\",\"source\":\"PubMed\"}],\"value\":\"PhMAX2B\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38513014\",\"source\":\"PubMed\"}],\"id\":\"SL-0191\",\"value\":\"Nucleus\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38513014\",\"source\":\"PubMed\"}],\"id\":\"SL-0086\",\"value\":\"Cytoplasm\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38513014\",\"source\":\"PubMed\"}],\"id\":\"GO:0005737\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38513014\",\"source\":\"PubMed\"}],\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0019005\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:SCF ubiquitin ligase complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Drummond R.S.M.\",\"Sheehan H.\",\"Simons J.L.\",\"Martinez-Sanchez N.M.\",\"Turner R.M.\",\"Putterill J.\",\"Snowden K.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22645562\"},{\"database\":\"DOI\",\"id\":\"10.3389/fpls.2011.00115\"}],\"citationType\":\"journal article\",\"firstPage\":\"115\",\"id\":\"22645562\",\"journal\":\"Front. Plant Sci.\",\"lastPage\":\"115\",\"publicationDate\":\"2011\",\"title\":\"The expression of Petunia strigolactone pathway genes is altered as part of the endogenous developmental program.\",\"volume\":\"2\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Violet 26\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"TISSUE SPECIFICITY\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Stirling S.A.\",\"Guercio A.M.\",\"Partrick R.M.\",\"Huang X.-Q.\",\"Bergman M.E.\",\"Dwivedi V.\",\"Kortbeek R.W.J.\",\"Liu Y.-K.\",\"Sun F.\",\"Tao W.A.\",\"Li Y.\",\"Boachon B.\",\"Shabek N.\",\"Dudareva N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38513014\"},{\"database\":\"DOI\",\"id\":\"10.1126/science.adl4685\"}],\"citationType\":\"journal article\",\"firstPage\":\"1318\",\"id\":\"38513014\",\"journal\":\"Science\",\"lastPage\":\"1325\",\"publicationDate\":\"2024\",\"title\":\"Volatile communication in plants relies on a KAI2-mediated signaling pathway.\",\"volume\":\"383\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Mitchell\"}],\"referenceNumber\":2,\"referencePositions\":[\"TISSUE SPECIFICITY\",\"SUBCELLULAR LOCATION\",\"INTERACTION WITH KAI2IA\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:51.337813+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636",
  "url": "https://rest.uniprot.org/uniprotkb/I1SSI6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H1",
  "excerpt": "ID   MAX2B_PETHY             Reviewed;         723 AA.\nAC   I1SSI6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-JUL-2012, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=F-box protein MAX2 homolog B {ECO:0000303|PubMed:22645562, ECO:0000303|PubMed:38513014};\nDE            Short=PhMAX2B {ECO:0000303|PubMed:22645562, ECO:0000303|PubMed:38513014};\nGN   Name=MAX2B {ECO:0000303|PubMed:38513014};\nOS   Petunia hybrida (Petunia).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Solanales; Solanaceae; Petunioideae; Petunia.\nOX   NCBI_TaxID=4102;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.521456+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab",
  "url": "https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], TISSUE SPECIFICITY, AND DEVELOPMENTAL\nRP   STAGE.\nRC   STRAIN=cv. Violet 26;\nRX   PubMed=22645562; DOI=10.3389/fpls.2011.00115;\nRA   Drummond R.S.M., Sheehan H., Simons J.L., Martinez-Sanchez N.M.,\nRA   Turner R.M., Putterill J., Snowden K.C.;\nRT   \"The expression of Petunia strigolactone pathway genes is altered as part\nRT   of the endogenous developmental program.\";\nRL   Front. Plant Sci. 2:115-115(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.521456+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab",
  "url": "https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   TISSUE SPECIFICITY, SUBCELLULAR LOCATION, AND INTERACTION WITH KAI2IA.\nRC   STRAIN=cv. Mitchell;\nRX   PubMed=38513014; DOI=10.1126/science.adl4685;\nRA   Stirling S.A., Guercio A.M., Partrick R.M., Huang X.-Q., Bergman M.E.,\nRA   Dwivedi V., Kortbeek R.W.J., Liu Y.-K., Sun F., Tao W.A., Li Y.,\nRA   Boachon B., Shabek N., Dudareva N.;\nRT   \"Volatile communication in plants relies on a KAI2-mediated signaling\nRT   pathway.\";\nRL   Science 383:1318-1325(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.521456+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab",
  "url": "https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:38513014}. Cytoplasm\nCC       {ECO:0000269|PubMed:38513014}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.521456+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab",
  "url": "https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.521456+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab",
  "url": "https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.521456+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab",
  "url": "https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0019005; C:SCF ubiquitin ligase complex; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:53.521456+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab",
  "url": "https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005634\nname: nucleus\nnamespace: cellular_component\ndef: \"A membrane-bounded organelle of eukaryotic cells in which chromosomes are housed and replicated. In most cells, the nucleus contains all of the cell's chromosomes except the organellar chromosomes, and is the site of RNA synthesis and processing. In some species, or in specialized cell types, RNA metabolism or DNA replication may be absent.\" [GOC:curators]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"cell nucleus\" EXACT []\nsynonym: \"horsetail nucleus\" NARROW [GOC:al, GOC:mah, GOC:vw, PMID:15030757]\nxref: NIF_Subcellular:sao1702920020\nxref: Wikipedia:Cell_nucleus\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005634",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58002-58025",
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
  "excerpt": "[Term]\nid: GO:0016020\nname: membrane\nnamespace: cellular_component\nalt_id: GO:0016021\nalt_id: GO:0098589\nalt_id: GO:0098805\ndef: \"A lipid bilayer along with all the proteins and protein complexes embedded in it and attached to it.\" [GOC:dos, GOC:mah, ISBN:0815316194]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_yeast\nsynonym: \"integral component of membrane\" NARROW []\nsynonym: \"integral to membrane\" NARROW []\nsynonym: \"membrane region\" NARROW []\nsynonym: \"region of membrane\" NARROW []\nsynonym: \"transmembrane\" RELATED [GOC:mah]\nsynonym: \"whole membrane\" NARROW []\nxref: Wikipedia:Biological_membrane\nxref: Wikipedia:Transmembrane_protein\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016020",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 122626-122650",
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
  "excerpt": "[Term]\nid: GO:0020009\nname: microneme\nnamespace: cellular_component\ndef: \"A small, elongated secretory organelle that forms part of the apical complex, located along the main axis of an apicomplexan parasite cell within the extreme apical region and at the periphery under the inner membrane complex. Of the specialized secretory compartments identified in apicomplexans, micronemes discharge their contents first, during initial contact of the parasite's apical pole with the host cell surface. Micronemal proteins function during parasite attachment and penetration into the target cell.\" [ISBN:0521664470, PMID:11801218]\nsynonym: \"sarconeme\" RELATED []\nxref: Wikipedia:Microneme\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0020007 ! apical complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020009",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155191-155200",
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
  "excerpt": "[Term]\nid: GO:0098978\nname: glutamatergic synapse\nnamespace: cellular_component\ndef: \"A synapse that uses glutamate as a neurotransmitter.\" [GOC:dos]\nsubset: goslim_synapse\nis_a: GO:0045202 ! synapse\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098978",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 412689-412696",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
