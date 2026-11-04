# GO_cellular_component_0023

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0023.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — mitochondrion

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNGNQIKQLKKLYRHILNEASKFENINYNVYFSNKAKEKFREFCSDTNFESEKLKTFQNECWDYLNMLKRQTIIHNLYHVDKPLVNK

[Multiple Choices]
A. mitochondrial [2Fe-2S] assembly complex
B. cytoplasm
C. virion component
D. mitochondrion
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

> The sequence-matched UniProt record reports mitochondrial localization with experimental evidence (ECO:0000269), and includes a mitochondrion GO annotation with IDA evidence. This supports choice D.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short sequence contains an LYR motif in a small, largely helical protein, consistent with the transferable Isd11/LYRM4 protein family. Isd11-family proteins participate in mitochondrial iron-sulfur-cluster biogenesis, which supports mitochondrion over cytoplasm or virion component without needing the exact protein's database record.


**Missing item-specific fact**

> Exact membership of this protein in the particular mitochondrial &#91;2Fe-2S&#93; assembly complex would be needed to resolve whether A is intended instead of the broader compartment D.


**Reason**

> Family-level inference meaningfully supports mitochondrial localization, but does not by itself establish the exact complex membership implied by A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> D is the supported organelle location. A may also be defensible because Isd11/LYRM4-family proteins participate in mitochondrial iron-sulfur assembly complexes; the question does not clarify whether it wants the organelle or a protein complex in which the protein resides.


### Important caveats

- The cited localization evidence is experimental in the sequence-matched source record, but the author's exact source snapshot is unknown.
- The family-based inference supports mitochondrial localization; it does not independently prove membership in the specific complex named in A.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short sequence contains an LYR motif in a small, largely helical protein, consistent with the transferable Isd11/LYRM4 protein family. Isd11-family proteins participate in mitochondrial iron-sulfur-cluster biogenesis, which supports mitochondrion over cytoplasm or virion component without needing the exact protein's database record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact membership of this protein in the particular mitochondrial [2Fe-2S] assembly complex would be needed to resolve whether A is intended instead of the broader compartment D.",
    "reason": "Family-level inference meaningfully supports mitochondrial localization, but does not by itself establish the exact complex membership implied by A."
  },
  "case_id": "GO_cellular_component_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports mitochondrial localization with experimental evidence (ECO:0000269), and includes a mitochondrion GO annotation with IDA evidence. This supports choice D."
  },
  "important_caveats": [
    "The cited localization evidence is experimental in the sequence-matched source record, but the author's exact source snapshot is unknown.",
    "The family-based inference supports mitochondrial localization; it does not independently prove membership in the specific complex named in A."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "D is the supported organelle location. A may also be defensible because Isd11/LYRM4-family proteins participate in mitochondrial iron-sulfur assembly complexes; the question does not clarify whether it wants the organelle or a protein complex in which the protein resides."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports mitochondrial localization with experimental evidence (ECO:0000269), and includes a mitochondrion GO annotation with IDA evidence. This supports choice D.",
    "evidence_ids": ["C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short sequence contains an LYR motif in a small, largely helical protein, consistent with the transferable Isd11/LYRM4 protein family. Isd11-family proteins participate in mitochondrial iron-sulfur-cluster biogenesis, which supports mitochondrion over cytoplasm or virion component without needing the exact protein's database record.",
    "missing_item_specific_fact": "Exact membership of this protein in the particular mitochondrial [2Fe-2S] assembly complex would be needed to resolve whether A is intended instead of the broader compartment D.",
    "reason": "Family-level inference meaningfully supports mitochondrial localization, but does not by itself establish the exact complex membership implied by A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "D is the supported organelle location. A may also be defensible because Isd11/LYRM4-family proteins participate in mitochondrial iron-sulfur assembly complexes; the question does not clarify whether it wants the organelle or a protein complex in which the protein resides."
  },
  "important_caveats": [
    "The cited localization evidence is experimental in the sequence-matched source record, but the author's exact source snapshot is unknown.",
    "The family-based inference supports mitochondrial localization; it does not independently prove membership in the specific complex named in A."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IEK7 (PfIsd11) carries an experimental subcellular location annotation 'Mitochondrion' with evidence code ECO:0000269 (PubMed:24086138, Gisselberg et al. 2013, PLoS Pathog) and a direct GO annotation GO:0005739 C:mitochondrion with IDA:GeneDB evidence (evidence codes ECO:0000314). The 2021 paper (PubMed:34032321) further confirms the protein as part of the ISC scaffold complex in the Plasmodium falciparum mitochondrion. Option A (mitochondrial &#91;2Fe-2S&#93; assembly complex, GO:0099128) is NOT annotated for this protein; the protein is annotated to the parent term GO:1990221 (L-cysteine desulfurase complex) only via IBA inference. Option D is the experimentally supported primary location.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H4](#evidence-h4), [H6](#evidence-h6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 87-aa sequence contains the conserved CSD and CWD motifs (…CSDTNFESEKLKTFQNECWDYLNMLKRQ…), which are hallmark &#91;2Fe-2S&#93; cluster-binding motifs of Isd11-family scaffold proteins identified across eukaryotic homologs (yeast Isd11, human ISD11, bacterial NfsA-associated scaffolds). Recognizing these motifs allows a model to infer involvement in the ISC (iron-sulfur cluster) biogenesis pathway, whose core machinery is located in the mitochondrial matrix in eukaryotes. This points to mitochondrial localization (D). To distinguish D from A, the model can note that the sequence is very small (~87 aa) and scaffold-like, consistent with the Isd11 scaffold role rather than membership in the multi-subunit &#91;2Fe-2S&#93; assembly complex (GO:0099128, defined in the GO ontology as containing ISCU, NFS1, LYRM4, NDUFAB1, FXN in humans). The scaffold protein interacts with but is not a defined component of that specific complex. Additionally, the task asks for the 'primary Cellular Component,' which in standard GO annotation practice refers to the compartment (mitochondrion) rather than a specific multi-protein complex nested within it. Option C (virion component) is eliminable because the sequence lacks viral structural protein features, and B (cytoplasm) is less consistent with the Fe-S cluster scaffold motifs that are hallmarks of the mitochondrial ISC pathway.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The CSD/CWD Fe-S cluster-binding motifs are transferable features recognized across Isd11 homologs in yeast, humans, and bacteria. Their presence in this short scaffold-like protein supports inference of mitochondrial ISC pathway involvement. The distinction between the general compartment (mitochondrion, D) and the specific &#91;2Fe-2S&#93; assembly complex (A) can be reasoned from the protein's small scaffold-like architecture and the known composition of the &#91;2Fe-2S&#93; assembly complex. The 'primary cellular component' framing further favors the compartment-level answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> A model recognizing Fe-S cluster motifs could plausibly select either D (mitochondrion) or A (mitochondrial &#91;2Fe-2S&#93; assembly complex), since both are mitochondrial and related to Fe-S cluster biogenesis. The distinction requires knowing that Isd11 is the scaffold protein and not a defined member of the &#91;2Fe-2S&#93; assembly complex (GO:0099128), or interpreting 'primary cellular component' as the compartment rather than a specific complex. This makes A a somewhat tempting distractor, though the experimental annotation and GO term definitions favor D.


### Important caveats

- The organism (Plasmodium falciparum) and protein name (Isd11) are not provided in the original input; the model must infer mitochondrial localization from sequence features alone.
- Plasmodium mitochondrial targeting sequences are atypical (often not canonical amphipathic N-terminal presequences), so standard MTS predictors may not flag this sequence; the CSD/CWD motifs are the more reliable transferable signal.
- The GO annotation GO:1990221 (L-cysteine desulfurase complex) is present via IBA inference, which is a weaker evidence type than the IDA/ECO:0000269 experimental annotation for GO:0005739 (mitochondrion).
- The reviewer-only evidence confirms the sequence matches Q8IEK7 exactly (SHA-256 match), but this accession and organism were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 87-aa sequence contains the conserved CSD and CWD motifs (…CSDTNFESEKLKTFQNECWDYLNMLKRQ…), which are hallmark [2Fe-2S] cluster-binding motifs of Isd11-family scaffold proteins identified across eukaryotic homologs (yeast Isd11, human ISD11, bacterial NfsA-associated scaffolds). Recognizing these motifs allows a model to infer involvement in the ISC (iron-sulfur cluster) biogenesis pathway, whose core machinery is located in the mitochondrial matrix in eukaryotes. This points to mitochondrial localization (D). To distinguish D from A, the model can note that the sequence is very small (~87 aa) and scaffold-like, consistent with the Isd11 scaffold role rather than membership in the multi-subunit [2Fe-2S] assembly complex (GO:0099128, defined in the GO ontology as containing ISCU, NFS1, LYRM4, NDUFAB1, FXN in humans). The scaffold protein interacts with but is not a defined component of that specific complex. Additionally, the task asks for the 'primary Cellular Component,' which in standard GO annotation practice refers to the compartment (mitochondrion) rather than a specific multi-protein complex nested within it. Option C (virion component) is eliminable because the sequence lacks viral structural protein features, and B (cytoplasm) is less consistent with the Fe-S cluster scaffold motifs that are hallmarks of the mitochondrial ISC pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The CSD/CWD Fe-S cluster-binding motifs are transferable features recognized across Isd11 homologs in yeast, humans, and bacteria. Their presence in this short scaffold-like protein supports inference of mitochondrial ISC pathway involvement. The distinction between the general compartment (mitochondrion, D) and the specific [2Fe-2S] assembly complex (A) can be reasoned from the protein's small scaffold-like architecture and the known composition of the [2Fe-2S] assembly complex. The 'primary cellular component' framing further favors the compartment-level answer."
  },
  "case_id": "GO_cellular_component_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "C9",
      "H4",
      "H6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IEK7 (PfIsd11) carries an experimental subcellular location annotation 'Mitochondrion' with evidence code ECO:0000269 (PubMed:24086138, Gisselberg et al. 2013, PLoS Pathog) and a direct GO annotation GO:0005739 C:mitochondrion with IDA:GeneDB evidence (evidence codes ECO:0000314). The 2021 paper (PubMed:34032321) further confirms the protein as part of the ISC scaffold complex in the Plasmodium falciparum mitochondrion. Option A (mitochondrial [2Fe-2S] assembly complex, GO:0099128) is NOT annotated for this protein; the protein is annotated to the parent term GO:1990221 (L-cysteine desulfurase complex) only via IBA inference. Option D is the experimentally supported primary location."
  },
  "important_caveats": [
    "The organism (Plasmodium falciparum) and protein name (Isd11) are not provided in the original input; the model must infer mitochondrial localization from sequence features alone.",
    "Plasmodium mitochondrial targeting sequences are atypical (often not canonical amphipathic N-terminal presequences), so standard MTS predictors may not flag this sequence; the CSD/CWD motifs are the more reliable transferable signal.",
    "The GO annotation GO:1990221 (L-cysteine desulfurase complex) is present via IBA inference, which is a weaker evidence type than the IDA/ECO:0000269 experimental annotation for GO:0005739 (mitochondrion).",
    "The reviewer-only evidence confirms the sequence matches Q8IEK7 exactly (SHA-256 match), but this accession and organism were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "A model recognizing Fe-S cluster motifs could plausibly select either D (mitochondrion) or A (mitochondrial [2Fe-2S] assembly complex), since both are mitochondrial and related to Fe-S cluster biogenesis. The distinction requires knowing that Isd11 is the scaffold protein and not a defined member of the [2Fe-2S] assembly complex (GO:0099128), or interpreting 'primary cellular component' as the compartment rather than a specific complex. This makes A a somewhat tempting distractor, though the experimental annotation and GO term definitions favor D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IEK7 (PfIsd11) carries an experimental subcellular location annotation 'Mitochondrion' with evidence code ECO:0000269 (PubMed:24086138, Gisselberg et al. 2013, PLoS Pathog) and a direct GO annotation GO:0005739 C:mitochondrion with IDA:GeneDB evidence (evidence codes ECO:0000314). The 2021 paper (PubMed:34032321) further confirms the protein as part of the ISC scaffold complex in the Plasmodium falciparum mitochondrion. Option A (mitochondrial [2Fe-2S] assembly complex, GO:0099128) is NOT annotated for this protein; the protein is annotated to the parent term GO:1990221 (L-cysteine desulfurase complex) only via IBA inference. Option D is the experimentally supported primary location.",
    "evidence_ids": ["C5", "C7", "C8", "C9", "H4", "H6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 87-aa sequence contains the conserved CSD and CWD motifs (…CSDTNFESEKLKTFQNECWDYLNMLKRQ…), which are hallmark [2Fe-2S] cluster-binding motifs of Isd11-family scaffold proteins identified across eukaryotic homologs (yeast Isd11, human ISD11, bacterial NfsA-associated scaffolds). Recognizing these motifs allows a model to infer involvement in the ISC (iron-sulfur cluster) biogenesis pathway, whose core machinery is located in the mitochondrial matrix in eukaryotes. This points to mitochondrial localization (D). To distinguish D from A, the model can note that the sequence is very small (~87 aa) and scaffold-like, consistent with the Isd11 scaffold role rather than membership in the multi-subunit [2Fe-2S] assembly complex (GO:0099128, defined in the GO ontology as containing ISCU, NFS1, LYRM4, NDUFAB1, FXN in humans). The scaffold protein interacts with but is not a defined component of that specific complex. Additionally, the task asks for the 'primary Cellular Component,' which in standard GO annotation practice refers to the compartment (mitochondrion) rather than a specific multi-protein complex nested within it. Option C (virion component) is eliminable because the sequence lacks viral structural protein features, and B (cytoplasm) is less consistent with the Fe-S cluster scaffold motifs that are hallmarks of the mitochondrial ISC pathway.",
    "missing_item_specific_fact": "",
    "reason": "The CSD/CWD Fe-S cluster-binding motifs are transferable features recognized across Isd11 homologs in yeast, humans, and bacteria. Their presence in this short scaffold-like protein supports inference of mitochondrial ISC pathway involvement. The distinction between the general compartment (mitochondrion, D) and the specific [2Fe-2S] assembly complex (A) can be reasoned from the protein's small scaffold-like architecture and the known composition of the [2Fe-2S] assembly complex. The 'primary cellular component' framing further favors the compartment-level answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "A model recognizing Fe-S cluster motifs could plausibly select either D (mitochondrion) or A (mitochondrial [2Fe-2S] assembly complex), since both are mitochondrial and related to Fe-S cluster biogenesis. The distinction requires knowing that Isd11 is the scaffold protein and not a defined member of the [2Fe-2S] assembly complex (GO:0099128), or interpreting 'primary cellular component' as the compartment rather than a specific complex. This makes A a somewhat tempting distractor, though the experimental annotation and GO term definitions favor D."
  },
  "important_caveats": [
    "The organism (Plasmodium falciparum) and protein name (Isd11) are not provided in the original input; the model must infer mitochondrial localization from sequence features alone.",
    "Plasmodium mitochondrial targeting sequences are atypical (often not canonical amphipathic N-terminal presequences), so standard MTS predictors may not flag this sequence; the CSD/CWD motifs are the more reliable transferable signal.",
    "The GO annotation GO:1990221 (L-cysteine desulfurase complex) is present via IBA inference, which is a weaker evidence type than the IDA/ECO:0000269 experimental annotation for GO:0005739 (mitochondrion).",
    "The reviewer-only evidence confirms the sequence matches Q8IEK7 exactly (SHA-256 match), but this accession and organism were not available to the evaluated model."
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
  "benchmark_sequence_length": 87,
  "benchmark_sequence_sha256": "815f42c3144ae2ea2c1a076fe6c0c288030a0dd499a0d2862408f97a7437882f",
  "current_entry_audit": {
    "entryVersion": 87,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 87,
  "current_source_sequence_sha256": "815f42c3144ae2ea2c1a076fe6c0c288030a0dd499a0d2862408f97a7437882f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 85,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IEK7",
  "selected_historical_entry_version": 85,
  "selected_historical_record_sha256": "18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d",
  "selected_historical_source_sequence_length": 87,
  "selected_historical_source_sequence_sha256": "815f42c3144ae2ea2c1a076fe6c0c288030a0dd499a0d2862408f97a7437882f",
  "selected_historical_version": {
    "accession": "Q8IEK7",
    "database": "Swiss-Prot",
    "entryVersion": 85,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ISD11_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IEK7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:24.795774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IEK7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":87,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:24.795774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IEK7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:24.795774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IEK7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Protein Isd11\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"PfIsd11\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:24.795774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IEK7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24086138\",\"source\":\"PubMed\"}],\"id\":\"SL-0173\",\"value\":\"Mitochondrion\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:24.795774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IEK7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:1990221\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:L-cysteine desulfurase complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-01T06:25:24.795774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IEK7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"24086138\",\"source\":\"PubMed\"}],\"id\":\"GO:0005739\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrion\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/21",
  "retrieved_utc": "2026-11-01T06:25:24.795774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IEK7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Gisselberg J.E.\",\"Dellibovi-Ragheb T.A.\",\"Matthews K.A.\",\"Bosch G.\",\"Prigge S.T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24086138\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1003655\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1003655\",\"id\":\"24086138\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1003655\",\"publicationDate\":\"2013\",\"title\":\"The suf iron-sulfur cluster synthesis pathway is required for apicoplast maintenance in malaria parasites.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:24.795774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IEK7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Sadik M.\",\"Afsar M.\",\"Ramachandran R.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34032321\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14735\"}],\"citationType\":\"journal article\",\"firstPage\":\"606\",\"id\":\"34032321\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"623\",\"publicationDate\":\"2021\",\"title\":\"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH ISCS\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:24.795774+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IEK7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H1",
  "excerpt": "ID   ISD11_PLAF7             Reviewed;          87 AA.\nAC   Q8IEK7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 85.\nDE   RecName: Full=Protein Isd11 {ECO:0000305};\nDE            Short=PfIsd11 {ECO:0000303|PubMed:34032321};\nGN   Name=Isd11 {ECO:0000303|PubMed:24086138, ECO:0000303|PubMed:34032321};\nGN   ORFNames=PF3D7_1311000 {ECO:0000312|EMBL:CAD52245.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:39.775629+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d",
  "url": "https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=24086138; DOI=10.1371/journal.ppat.1003655;\nRA   Gisselberg J.E., Dellibovi-Ragheb T.A., Matthews K.A., Bosch G.,\nRA   Prigge S.T.;\nRT   \"The suf iron-sulfur cluster synthesis pathway is required for apicoplast\nRT   maintenance in malaria parasites.\";\nRL   PLoS Pathog. 9:e1003655-e1003655(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:39.775629+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d",
  "url": "https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND INTERACTION WITH ISCS.\nRX   PubMed=34032321; DOI=10.1111/mmi.14735;\nRA   Sadik M., Afsar M., Ramachandran R., Habib S.;\nRT   \"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the\nRT   Plasmodium falciparum mitochondrion.\";\nRL   Mol. Microbiol. 116:606-623(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:39.775629+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d",
  "url": "https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:24086138}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:39.775629+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d",
  "url": "https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:1990221; C:L-cysteine desulfurase complex; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:39.775629+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d",
  "url": "https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005739; C:mitochondrion; IDA:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:39.775629+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d",
  "url": "https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005737\nname: cytoplasm\nnamespace: cellular_component\ndef: \"The contents of a cell excluding the plasma membrane and nucleus, but including other subcellular structures.\" [ISBN:0198547684]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nxref: Wikipedia:Cytoplasm\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005622 ! intracellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005737",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58957-58974",
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
  "excerpt": "[Term]\nid: GO:0005739\nname: mitochondrion\nnamespace: cellular_component\ndef: \"A semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration.\" [GOC:giardia, ISBN:0198506732]\ncomment: Some anaerobic or microaerophilic organisms (e.g. Entamoeba histolytica, Giardia intestinalis and several Microsporidia species) do not have mitochondria, and contain mitochondrion-related organelles (MROs) instead, called mitosomes or hydrogenosomes, very likely derived from mitochondria. To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"mitochondria\" EXACT []\nxref: NIF_Subcellular:sao1860313010\nxref: Wikipedia:Mitochondrion\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005739",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58975-58998",
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
  "excerpt": "[Term]\nid: GO:0005829\nname: cytosol\nnamespace: cellular_component\ndef: \"The part of the cytoplasm that does not contain organelles but which does contain other particulate matter, such as protein complexes.\" [GOC:hjd, GOC:jl]\nsubset: goslim_agr\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_plant\nxref: NIF_Subcellular:sao101633890\nxref: Wikipedia:Cytosol\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005829",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59936-59953",
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
  "excerpt": "[Term]\nid: GO:0044423\nname: virion component\nnamespace: cellular_component\nalt_id: GO:0019012\ndef: \"Any constituent part of a virion, a complete fully infectious extracellular virus particle.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"complete virus particle\" RELATED []\nsynonym: \"virion\" RELATED []\nsynonym: \"virion part\" EXACT []\nxref: Wikipedia:Virus\nis_a: GO:0005575 ! cellular_component\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044423",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 257048-257062",
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
  "excerpt": "[Term]\nid: GO:0099128\nname: mitochondrial [2Fe-2S] assembly complex\nnamespace: cellular_component\ndef: \"A protein complex capable of forming 2Fe-2S clusters in mitochondria. In humans it consists of ISCU, NFS1, LYRM4, NDUFAB1 and FXN.\" [PMID:31101807, PMID:34660592]\nsynonym: \"mitochondrial iron-sulfur cluster assembly complex\" RELATED []\nsynonym: \"mitochondrial ISCU complex\" EXACT []\nis_a: GO:0098798 ! mitochondrial protein-containing complex\nis_a: GO:1990221 ! L-cysteine desulfurase complex\nis_a: GO:1990229 ! iron-sulfur cluster assembly complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0099128",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 413997-414007",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:1990221\nname: L-cysteine desulfurase complex\nnamespace: cellular_component\ndef: \"A protein complex capable of cysteine desulfurase activity decomposing L-cysteine to L-alanine and sulfur. It belongs to a ubiquitous family of pyridoxal 5-phosphate (PLP)-dependent enzymes.\" [GOC:bhm, PMID:11827487]\nsynonym: \"IscS\" NARROW [GOC:bhm, GOC:dph]\nsynonym: \"NifS\" NARROW [GOC:bhm, GOC:dph]\nsynonym: \"SufS complex\" NARROW []\nis_a: GO:1990228 ! sulfurtransferase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990221",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 550305-550314",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO7",
  "excerpt": "[Term]\nid: GO:1990228\nname: sulfurtransferase complex\nnamespace: cellular_component\ndef: \"A protein complex capable of catalyzing the transfer of sulfur atoms from one compound (donor) to another (acceptor).\" [GOC:bhm, PMID:17350958]\nsynonym: \"SufE complex\" NARROW [GOC:bhm]\nsynonym: \"SufE dimer\" NARROW [GOC:bhm]\nsynonym: \"sulfur transfer complex\" EXACT [GOC:bhm]\nsynonym: \"ThiF-ThiS complex\" RELATED [GOC:bhm]\nis_a: GO:1990234 ! transferase complex\nrelationship: part_of GO:0005829 ! cytosol\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990228",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 550367-550378",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
