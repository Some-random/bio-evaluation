# GO_cellular_component_0067

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0067.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — Ndc80 complex

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAAPGLPQPGSLSTLAGYPSSTYSSQNSPFFPSADRGGRMTLEEIKRDFTKHKLECPDTMWREPQPEQVQGLYSFAIESIFGLTVNDVRIEEVTGDVRSCLPSIDSLQFLSQDGRLHAKAIGNLRFIRLCQRLNRVLGLPEFSRETFASPTASGVQRFASAVCMLLRLRESLCRQFESQIQQRASLQQSLQKLSQNAQLVEQELLRFRAERQTQQPLAQRQKQQQSELEEELRQRHSELGALMEEFKERQAVHGRLELELGDLVLELMNLKQEREELHDQVVHSPEKLMERRDELRVQQKHLDAQLQELENLAASQQKLLLAFAKAVKKAKKAMEILSAHRDQVLAPHLGFRSDMRTREKLFRELGEQKEQLSKAVQDLQAEREELARQLEDQERKKDEEETELRGHLARAKREVEERKKALADQQDMTAAFLREAEKLEEKLAEQKQRHKLLVDAIEEEIQKVYAAFLTYVSQMQFIRSQMPLSLDLSQSASFLAEHSEKTHRGSPLACEREENDDFLASLLAESSPSSLGEEKENLPQSRPTAAADAERRLADFSPEKGRKRLSCLDEETEEEARMHERERESDRLFPAAREPREDGDFPMYGHAE

[Multiple Choices]
A. nuclear pore
B. periplasmic space
C. Ndc80 complex
D. tRNA methyltransferase complex
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

> The matching-sequence UniProt record identifies the protein as NUF2 and assigns it to the Ndc80 complex by IEA:InterPro. Experimental evidence reports co-localization with NDC80 at the kinetochore, supporting the expected cellular-component choice, though co-localization alone does not prove direct complex membership.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a long, eukaryotic protein with an N-terminal structured region and an extensive central coiled-coil-like region, an architecture characteristic of NUF2/NDC80-family kinetochore proteins that form the coiled-coil Ndc80 complex. That family-level pattern distinguishes C from the periplasmic-space and tRNA-methyltransferase alternatives; it is also a better fit than a nuclear-pore assignment among these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of NUF2/NDC80-family architecture and kinetochore-complex organization provides a meaningful basis for selecting C without recalling this exact protein's database record. Sequence architecture alone is not definitive, but the alternatives make the family-level inference useful.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence and its family-level features.


### Important caveats

- The direct GO complex annotation is computational (IEA:InterPro); the cited experimental evidence supports kinetochore localization and co-localization with NDC80, not necessarily direct physical interaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long, eukaryotic protein with an N-terminal structured region and an extensive central coiled-coil-like region, an architecture characteristic of NUF2/NDC80-family kinetochore proteins that form the coiled-coil Ndc80 complex. That family-level pattern distinguishes C from the periplasmic-space and tRNA-methyltransferase alternatives; it is also a better fit than a nuclear-pore assignment among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of NUF2/NDC80-family architecture and kinetochore-complex organization provides a meaningful basis for selecting C without recalling this exact protein's database record. Sequence architecture alone is not definitive, but the alternatives make the family-level inference useful."
  },
  "case_id": "GO_cellular_component_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matching-sequence UniProt record identifies the protein as NUF2 and assigns it to the Ndc80 complex by IEA:InterPro. Experimental evidence reports co-localization with NDC80 at the kinetochore, supporting the expected cellular-component choice, though co-localization alone does not prove direct complex membership."
  },
  "important_caveats": [
    "The direct GO complex annotation is computational (IEA:InterPro); the cited experimental evidence supports kinetochore localization and co-localization with NDC80, not necessarily direct physical interaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence and its family-level features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matching-sequence UniProt record identifies the protein as NUF2 and assigns it to the Ndc80 complex by IEA:InterPro. Experimental evidence reports co-localization with NDC80 at the kinetochore, supporting the expected cellular-component choice, though co-localization alone does not prove direct complex membership.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a long, eukaryotic protein with an N-terminal structured region and an extensive central coiled-coil-like region, an architecture characteristic of NUF2/NDC80-family kinetochore proteins that form the coiled-coil Ndc80 complex. That family-level pattern distinguishes C from the periplasmic-space and tRNA-methyltransferase alternatives; it is also a better fit than a nuclear-pore assignment among these choices.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of NUF2/NDC80-family architecture and kinetochore-complex organization provides a meaningful basis for selecting C without recalling this exact protein's database record. Sequence architecture alone is not definitive, but the alternatives make the family-level inference useful."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence and its family-level features."
  },
  "important_caveats": [
    "The direct GO complex annotation is computational (IEA:InterPro); the cited experimental evidence supports kinetochore localization and co-localization with NDC80, not necessarily direct physical interaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry identifies this protein as Kinetochore protein NUF2 (TgNuf2) from Toxoplasma gondii. Experimental evidence (PubMed:24015880, ECO:0000269) demonstrates co-localization with NDC80 at the kinetochore throughout the cell cycle. The GO annotation GO:0031262 (Ndc80 complex) is present, though via IEA:InterPro (computational domain inference). The GO term definition for Ndc80 complex explicitly includes the synonym 'Nuf2-Ndc80 complex,' confirming NUF2 as a core component. The answer C is well-supported by both the family-level role of NUF2 in the Ndc80 complex and the experimental co-localization data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several elimination steps are available from general biology: (1) Periplasmic space (B) is a prokaryotic/fungal compartment and is incompatible with a eukaryotic protein lacking signal peptides or transmembrane domains. (2) tRNA methyltransferase complex (D) requires catalytic methyltransferase domains (Rossmann-fold, AdoMet-binding motifs), which are absent from this predominantly coiled-coil sequence. (3) Between nuclear pore (A) and Ndc80 complex (C): the sequence is dominated by a very long central coiled-coil (~350+ residues of heptad-repeat hydrophobic pattern) without FG-repeats, beta-propeller motifs, or other nucleoporin-specific features. NUF2 family proteins across eukaryotes (yeast Nuf2, human NUF2, etc.) are characterized by exactly this architecture: a long coiled-coil mediating interaction with NDC80/HEC1, flanked by less structured N- and C-terminal regions. A model familiar with NUF2 homologs from model organisms can recognize this coiled-coil-dominated architecture as consistent with NUF2 and thus the Ndc80 complex, while nuclear pore proteins typically display FG-repeats, beta-propellers, or multiple short coiled-coils interspersed with other domains. The inference is probabilistic but meaningfully distinguishes C from A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The coiled-coil architecture, absence of FG-repeats or nucleoporin-specific domains, and knowledge of the NUF2 protein family (conserved coiled-coil component of the Ndc80 complex across eukaryotes) provide a transferable inference path. The elimination of B (prokaryotic term) and D (no catalytic domains) is straightforward. The A-vs-C distinction relies on recognizing the NUF2-family coiled-coil pattern, which is legitimate family-level knowledge transferable from homologs in yeast, human, and other organisms.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly eliminable. The A-vs-C distinction, while not airtight from sequence alone, is meaningfully resolved by the coiled-coil architecture matching the well-characterized NUF2 family and the absence of nucleoporin-specific features. No other option is genuinely defensible.


### Important caveats

- The GO:0031262 annotation is IEA:InterPro (computational domain match), not direct experimental evidence for complex membership, though the subcellular localization evidence (PubMed:24015880) experimentally confirms kinetochore co-localization with NDC80.
- The sequence is from Toxoplasma gondii, an apicomplexan; NUF2 family recognition relies on conservation with model-organism homologs.
- The coiled-coil argument is probabilistic: some nucleoporins also contain coiled-coil regions, though they typically have additional distinguishing features (FG-repeats, specific domains) absent here.
- The protein is 608 residues, consistent with known NUF2 family lengths across eukaryotes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several elimination steps are available from general biology: (1) Periplasmic space (B) is a prokaryotic/fungal compartment and is incompatible with a eukaryotic protein lacking signal peptides or transmembrane domains. (2) tRNA methyltransferase complex (D) requires catalytic methyltransferase domains (Rossmann-fold, AdoMet-binding motifs), which are absent from this predominantly coiled-coil sequence. (3) Between nuclear pore (A) and Ndc80 complex (C): the sequence is dominated by a very long central coiled-coil (~350+ residues of heptad-repeat hydrophobic pattern) without FG-repeats, beta-propeller motifs, or other nucleoporin-specific features. NUF2 family proteins across eukaryotes (yeast Nuf2, human NUF2, etc.) are characterized by exactly this architecture: a long coiled-coil mediating interaction with NDC80/HEC1, flanked by less structured N- and C-terminal regions. A model familiar with NUF2 homologs from model organisms can recognize this coiled-coil-dominated architecture as consistent with NUF2 and thus the Ndc80 complex, while nuclear pore proteins typically display FG-repeats, beta-propellers, or multiple short coiled-coils interspersed with other domains. The inference is probabilistic but meaningfully distinguishes C from A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The coiled-coil architecture, absence of FG-repeats or nucleoporin-specific domains, and knowledge of the NUF2 protein family (conserved coiled-coil component of the Ndc80 complex across eukaryotes) provide a transferable inference path. The elimination of B (prokaryotic term) and D (no catalytic domains) is straightforward. The A-vs-C distinction relies on recognizing the NUF2-family coiled-coil pattern, which is legitimate family-level knowledge transferable from homologs in yeast, human, and other organisms."
  },
  "case_id": "GO_cellular_component_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry identifies this protein as Kinetochore protein NUF2 (TgNuf2) from Toxoplasma gondii. Experimental evidence (PubMed:24015880, ECO:0000269) demonstrates co-localization with NDC80 at the kinetochore throughout the cell cycle. The GO annotation GO:0031262 (Ndc80 complex) is present, though via IEA:InterPro (computational domain inference). The GO term definition for Ndc80 complex explicitly includes the synonym 'Nuf2-Ndc80 complex,' confirming NUF2 as a core component. The answer C is well-supported by both the family-level role of NUF2 in the Ndc80 complex and the experimental co-localization data."
  },
  "important_caveats": [
    "The GO:0031262 annotation is IEA:InterPro (computational domain match), not direct experimental evidence for complex membership, though the subcellular localization evidence (PubMed:24015880) experimentally confirms kinetochore co-localization with NDC80.",
    "The sequence is from Toxoplasma gondii, an apicomplexan; NUF2 family recognition relies on conservation with model-organism homologs.",
    "The coiled-coil argument is probabilistic: some nucleoporins also contain coiled-coil regions, though they typically have additional distinguishing features (FG-repeats, specific domains) absent here.",
    "The protein is 608 residues, consistent with known NUF2 family lengths across eukaryotes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly eliminable. The A-vs-C distinction, while not airtight from sequence alone, is meaningfully resolved by the coiled-coil architecture matching the well-characterized NUF2 family and the absence of nucleoporin-specific features. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry identifies this protein as Kinetochore protein NUF2 (TgNuf2) from Toxoplasma gondii. Experimental evidence (PubMed:24015880, ECO:0000269) demonstrates co-localization with NDC80 at the kinetochore throughout the cell cycle. The GO annotation GO:0031262 (Ndc80 complex) is present, though via IEA:InterPro (computational domain inference). The GO term definition for Ndc80 complex explicitly includes the synonym 'Nuf2-Ndc80 complex,' confirming NUF2 as a core component. The answer C is well-supported by both the family-level role of NUF2 in the Ndc80 complex and the experimental co-localization data.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several elimination steps are available from general biology: (1) Periplasmic space (B) is a prokaryotic/fungal compartment and is incompatible with a eukaryotic protein lacking signal peptides or transmembrane domains. (2) tRNA methyltransferase complex (D) requires catalytic methyltransferase domains (Rossmann-fold, AdoMet-binding motifs), which are absent from this predominantly coiled-coil sequence. (3) Between nuclear pore (A) and Ndc80 complex (C): the sequence is dominated by a very long central coiled-coil (~350+ residues of heptad-repeat hydrophobic pattern) without FG-repeats, beta-propeller motifs, or other nucleoporin-specific features. NUF2 family proteins across eukaryotes (yeast Nuf2, human NUF2, etc.) are characterized by exactly this architecture: a long coiled-coil mediating interaction with NDC80/HEC1, flanked by less structured N- and C-terminal regions. A model familiar with NUF2 homologs from model organisms can recognize this coiled-coil-dominated architecture as consistent with NUF2 and thus the Ndc80 complex, while nuclear pore proteins typically display FG-repeats, beta-propellers, or multiple short coiled-coils interspersed with other domains. The inference is probabilistic but meaningfully distinguishes C from A.",
    "missing_item_specific_fact": "",
    "reason": "The coiled-coil architecture, absence of FG-repeats or nucleoporin-specific domains, and knowledge of the NUF2 protein family (conserved coiled-coil component of the Ndc80 complex across eukaryotes) provide a transferable inference path. The elimination of B (prokaryotic term) and D (no catalytic domains) is straightforward. The A-vs-C distinction relies on recognizing the NUF2-family coiled-coil pattern, which is legitimate family-level knowledge transferable from homologs in yeast, human, and other organisms."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly eliminable. The A-vs-C distinction, while not airtight from sequence alone, is meaningfully resolved by the coiled-coil architecture matching the well-characterized NUF2 family and the absence of nucleoporin-specific features. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The GO:0031262 annotation is IEA:InterPro (computational domain match), not direct experimental evidence for complex membership, though the subcellular localization evidence (PubMed:24015880) experimentally confirms kinetochore co-localization with NDC80.",
    "The sequence is from Toxoplasma gondii, an apicomplexan; NUF2 family recognition relies on conservation with model-organism homologs.",
    "The coiled-coil argument is probabilistic: some nucleoporins also contain coiled-coil regions, though they typically have additional distinguishing features (FG-repeats, specific domains) absent here.",
    "The protein is 608 residues, consistent with known NUF2 family lengths across eukaryotes."
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
  "benchmark_sequence_length": 608,
  "benchmark_sequence_sha256": "b48650b65c0b00cace28156b972d9d6ce15cf53c7a1780904ed25f8cf8773472",
  "current_entry_audit": {
    "entryVersion": 41,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-10-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 608,
  "current_source_sequence_sha256": "b48650b65c0b00cace28156b972d9d6ce15cf53c7a1780904ed25f8cf8773472",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 39,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "S8EV69",
  "selected_historical_entry_version": 39,
  "selected_historical_record_sha256": "665a5d577c22b6c288b850d0d50c4d6f885ae6321f4d7320b54fc9362f20bc3a",
  "selected_historical_source_sequence_length": 608,
  "selected_historical_source_sequence_sha256": "b48650b65c0b00cace28156b972d9d6ce15cf53c7a1780904ed25f8cf8773472",
  "selected_historical_version": {
    "accession": "S8EV69",
    "database": "Swiss-Prot",
    "entryVersion": 39,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NUF2_TOXGM",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"S8EV69\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:58.410089+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17",
  "url": "https://rest.uniprot.org/uniprotkb/S8EV69.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":41,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-10-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:58.410089+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17",
  "url": "https://rest.uniprot.org/uniprotkb/S8EV69.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001529\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii (strain ATCC 50611 / Me49)\",\"taxonId\":508771}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:58.410089+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17",
  "url": "https://rest.uniprot.org/uniprotkb/S8EV69.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Kinetochore protein NUF2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24015880\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30865554\",\"source\":\"PubMed\"}],\"value\":\"TgNuf2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:58.410089+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17",
  "url": "https://rest.uniprot.org/uniprotkb/S8EV69.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24015880\",\"source\":\"PubMed\"}],\"value\":\"Co-localizes with NDC80 throughout the cell cycle\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24015880\",\"source\":\"PubMed\"}],\"id\":\"SL-0149\",\"value\":\"Chromosome, centromere, kinetochore\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:58.410089+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17",
  "url": "https://rest.uniprot.org/uniprotkb/S8EV69.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031262\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:Ndc80 complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:33:58.410089+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17",
  "url": "https://rest.uniprot.org/uniprotkb/S8EV69.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Farrell M.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24015880\"},{\"database\":\"DOI\",\"id\":\"10.1111/cmi.12185\"}],\"citationType\":\"journal article\",\"firstPage\":\"78\",\"id\":\"24015880\",\"journal\":\"Cell. Microbiol.\",\"lastPage\":\"94\",\"publicationDate\":\"2014\",\"title\":\"The Toxoplasma gondii kinetochore is required for centrosome association with the centrocone (spindle pole).\",\"volume\":\"16\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"REGION REQUIRED FOR NUCLEAR LOCALIZATION\",\"MUTAGENESIS OF 121-ILE--ARG-125\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:33:58.410089+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17",
  "url": "https://rest.uniprot.org/uniprotkb/S8EV69.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EV69.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Chen C.T.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30865554\"},{\"database\":\"DOI\",\"id\":\"10.1091/mbc.e18-10-0608\"}],\"citationType\":\"journal article\",\"firstPage\":\"1160\",\"id\":\"30865554\",\"journal\":\"Mol. Biol. Cell\",\"lastPage\":\"1169\",\"publicationDate\":\"2019\",\"title\":\"TgCep250 is dynamically processed through the division cycle and is essential for structural integrity of the Toxoplasma centrosome.\",\"volume\":\"30\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:58.410089+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "21d863f6ce77eb34e9be9d1b3d4aeabfd4e7421da314d69e1c53d0322926db17",
  "url": "https://rest.uniprot.org/uniprotkb/S8EV69.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H1",
  "excerpt": "ID   NUF2_TOXGM              Reviewed;         608 AA.\nAC   S8EV69;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-OCT-2013, sequence version 1.\nDT   28-JAN-2026, entry version 39.\nDE   RecName: Full=Kinetochore protein NUF2 {ECO:0000305};\nDE            Short=TgNuf2 {ECO:0000303|PubMed:24015880, ECO:0000303|PubMed:30865554};\nGN   Name=NUF2 {ECO:0000305};\nGN   ORFNames=TGME49_309380 {ECO:0000312|EMBL:EPT26282.1};\nOS   Toxoplasma gondii (strain ATCC 50611 / Me49).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=508771 {ECO:0000312|Proteomes:UP000001529};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:00.721786+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "665a5d577c22b6c288b850d0d50c4d6f885ae6321f4d7320b54fc9362f20bc3a",
  "url": "https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, REGION REQUIRED FOR\nRP   NUCLEAR LOCALIZATION, AND MUTAGENESIS OF 121-ILE--ARG-125.\nRX   PubMed=24015880; DOI=10.1111/cmi.12185;\nRA   Farrell M., Gubbels M.J.;\nRT   \"The Toxoplasma gondii kinetochore is required for centrosome association\nRT   with the centrocone (spindle pole).\";\nRL   Cell. Microbiol. 16:78-94(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:00.721786+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "665a5d577c22b6c288b850d0d50c4d6f885ae6321f4d7320b54fc9362f20bc3a",
  "url": "https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30865554; DOI=10.1091/mbc.e18-10-0608;\nRA   Chen C.T., Gubbels M.J.;\nRT   \"TgCep250 is dynamically processed through the division cycle and is\nRT   essential for structural integrity of the Toxoplasma centrosome.\";\nRL   Mol. Biol. Cell 30:1160-1169(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:00.721786+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "665a5d577c22b6c288b850d0d50c4d6f885ae6321f4d7320b54fc9362f20bc3a",
  "url": "https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Chromosome, centromere, kinetochore\nCC       {ECO:0000269|PubMed:24015880}. Note=Co-localizes with NDC80 throughout\nCC       the cell cycle. {ECO:0000269|PubMed:24015880}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:00.721786+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "665a5d577c22b6c288b850d0d50c4d6f885ae6321f4d7320b54fc9362f20bc3a",
  "url": "https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0031262; C:Ndc80 complex; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:00.721786+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "665a5d577c22b6c288b850d0d50c4d6f885ae6321f4d7320b54fc9362f20bc3a",
  "url": "https://rest.uniprot.org/unisave/S8EV69?format=txt&versions=39"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005643\nname: nuclear pore\nnamespace: cellular_component\nalt_id: GO:0005644\ndef: \"A protein complex providing a discrete opening in the nuclear envelope of a eukaryotic cell, where the inner and outer nuclear membranes are joined.\" [ISBN:0198547684]\nsubset: goslim_pir\nsynonym: \"NPC\" EXACT []\nsynonym: \"nuclear pore complex\" EXACT []\nsynonym: \"nuclear pore membrane protein\" NARROW []\nsynonym: \"nucleopore\" EXACT [GOC:al, PMID:7603572]\nxref: NIF_Subcellular:sao220861693\nxref: Wikipedia:Nuclear_pore\nis_a: GO:0140513 ! nuclear protein-containing complex\nrelationship: part_of GO:0005635 ! nuclear envelope\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005643",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58104-58119",
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
  "excerpt": "[Term]\nid: GO:0031262\nname: Ndc80 complex\nnamespace: cellular_component\ndef: \"An essential outer kinetochore complex involved in the attachment of microtubule ends to the chromosomes during mitosis.\" [GOC:vw, PMID:28502666, PMID:34810257]\nsynonym: \"Nuf2-Ndc80 complex\" EXACT []\nis_a: GO:0032991 ! protein-containing complex\nrelationship: part_of GO:0000940 ! outer kinetochore\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031262",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 174616-174624",
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
  "excerpt": "[Term]\nid: GO:0042597\nname: periplasmic space\nnamespace: cellular_component\nalt_id: GO:0005620\ndef: \"The region between the inner (cytoplasmic) and outer membrane (Gram-negative Bacteria) or cytoplasmic membrane and cell wall (Fungi and Gram-positive Bacteria).\" [GOC:curators, GOC:md]\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsynonym: \"periplasm\" EXACT []\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005576 ! extracellular region\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042597",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 238998-239011",
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
  "excerpt": "[Term]\nid: GO:0043527\nname: tRNA methyltransferase complex\nnamespace: cellular_component\ndef: \"A multimeric protein complex involved in the methylation of specific nucleotides in tRNA.\" [GOC:jl, PMID:24904644, PMID:9851972]\nsubset: goslim_pir\nis_a: GO:0034708 ! methyltransferase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043527",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 248215-248222",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
