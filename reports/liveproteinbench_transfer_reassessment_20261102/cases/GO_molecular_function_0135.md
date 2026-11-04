# GO_molecular_function_0135

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0135.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — protein folding chaperone

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MANILENQLFTAAKTIEQQLDQQLDRLDNLDSDDLKVLREQRLREMKDLNNKKQEWLRNGHGTYTELADEKEFFEMSKKSPNIVCHFYRDSTERCKIVDMHLKILAAKHVEAKFCKVNAEKTPFLTQRLRIKVIPTIALVKDSKTKDFIVGFTDLGNCDDFATEMLEWRIAHSGAIDYKGDLMQPPDVKRKPFINRPQKTIRGGYDSDDSDIDLDD

[Multiple Choices]
A. glycosaminoglycan binding
B. histone deacetylase activity
C. protein folding chaperone
D. peptide binding
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

> The sequence-matched historical record annotates this protein with protein folding chaperone activity (H5), supporting choice C as a GO annotation. This is a FlyBase NAS annotation, not direct experimental evidence for chaperone activity; the record also reports experimentally supported thioredoxin redox activity, so the annotation does not establish that chaperoning is its exclusive or primary activity.

Citations as saved: [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 216-residue sequence is consistent with a phosducin-like protein family member, whose family-level association with protein folding/co-chaperone functions provides a transferable basis for choosing C. The sequence also lacks the characteristic catalytic signatures expected of histone deacetylases, while glycosaminoglycan binding is a less fitting prediction for this compact intracellular-looking protein. This is a probabilistic family inference, not proof of the exact GO annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition and the offered alternatives give a meaningful basis for selecting the chaperone option without needing the exact protein's database entry. The experimentally reported redox function is an important limitation, but it is not among the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence indicates an additional redox activity, but no second offered option is comparably supported as the best choice among the listed alternatives.


### Important caveats

- The chaperone annotation is NAS:FlyBase and should not be presented as direct experimental confirmation.
- The source also reports experimentally supported thioredoxin redox activity; the word “primary” is therefore not established as an exclusive ranking of functions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 216-residue sequence is consistent with a phosducin-like protein family member, whose family-level association with protein folding/co-chaperone functions provides a transferable basis for choosing C. The sequence also lacks the characteristic catalytic signatures expected of histone deacetylases, while glycosaminoglycan binding is a less fitting prediction for this compact intracellular-looking protein. This is a probabilistic family inference, not proof of the exact GO annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the offered alternatives give a meaningful basis for selecting the chaperone option without needing the exact protein's database entry. The experimentally reported redox function is an important limitation, but it is not among the choices."
  },
  "case_id": "GO_molecular_function_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical record annotates this protein with protein folding chaperone activity (H5), supporting choice C as a GO annotation. This is a FlyBase NAS annotation, not direct experimental evidence for chaperone activity; the record also reports experimentally supported thioredoxin redox activity, so the annotation does not establish that chaperoning is its exclusive or primary activity."
  },
  "important_caveats": [
    "The chaperone annotation is NAS:FlyBase and should not be presented as direct experimental confirmation.",
    "The source also reports experimentally supported thioredoxin redox activity; the word “primary” is therefore not established as an exclusive ranking of functions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence indicates an additional redox activity, but no second offered option is comparably supported as the best choice among the listed alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical record annotates this protein with protein folding chaperone activity (H5), supporting choice C as a GO annotation. This is a FlyBase NAS annotation, not direct experimental evidence for chaperone activity; the record also reports experimentally supported thioredoxin redox activity, so the annotation does not establish that chaperoning is its exclusive or primary activity.",
    "evidence_ids": ["H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 216-residue sequence is consistent with a phosducin-like protein family member, whose family-level association with protein folding/co-chaperone functions provides a transferable basis for choosing C. The sequence also lacks the characteristic catalytic signatures expected of histone deacetylases, while glycosaminoglycan binding is a less fitting prediction for this compact intracellular-looking protein. This is a probabilistic family inference, not proof of the exact GO annotation.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the offered alternatives give a meaningful basis for selecting the chaperone option without needing the exact protein's database entry. The experimentally reported redox function is an important limitation, but it is not among the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence indicates an additional redox activity, but no second offered option is comparably supported as the best choice among the listed alternatives."
  },
  "important_caveats": [
    "The chaperone annotation is NAS:FlyBase and should not be presented as direct experimental confirmation.",
    "The source also reports experimentally supported thioredoxin redox activity; the word “primary” is therefore not established as an exclusive ranking of functions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for Q9VGV8 (Phosducin-like protein 3, Drosophila melanogaster) carries GO:0044183 'protein folding chaperone' with NAS:FlyBase evidence (C7/H5). This is the only option among A–D that has any GO annotation for this protein. However, the primary experimentally verified molecular function (IDA:FlyBase, GO:0047134) is protein-disulfide reductase &#91;NAD(P)H&#93; activity (EC 1.8.1.9, thioredoxin-disulfide reductase), which is not offered as a choice. The chaperone annotation is NAS (non-traceable author statement), weaker than the IDA redox annotation. Among the four offered alternatives, C is the only one with any annotation for this protein, so the key is supported within the constrained option set, though it represents a secondary or ancillary function rather than the primary catalytic activity.

Citations as saved: [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C5](#evidence-c5), [H5](#evidence-h5), [H6](#evidence-h6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 216-aa sequence displays a coiled-coil-like N-terminal region followed by a thioredoxin-like fold (containing a CxxC-like redox motif visible around residues ~100–115: 'CHFYRDSTERCK'), consistent with the Phosducin-like protein (PhLP) family architecture. PhLP2 is a well-characterized subunit of the CCT/TRiC chaperonin complex and is a canonical chaperone. PhLP3, as a family member sharing the thioredoxin-like fold and overall domain organization, has been described in the literature as possessing chaperone-like properties. A model recognizing the PhLP family from these sequence features can transfer the chaperone association from PhLP2 to PhLP3. Meanwhile, the other options can be eliminated: (A) glycosaminoglycan binding requires basic/clustered motifs or specific carbohydrate-recognition domains absent here; (B) histone deacetylase activity requires Zn²⁺-binding catalytic motifs (H-x₁₁-H-D-x₃-H) or NAD⁺-binding motifs (for sirtuins), none of which are present; (D) peptide binding implies specific peptide-recognition domains (MHC, SH3, PDZ, etc.) not found in this sequence. Among the four choices, C is the only one with a plausible biological connection via family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PhLP family–chaperone link is well-established transferable knowledge (PhLP2 = CCT-β). The sequence's thioredoxin-like fold and coiled-coil architecture are recognizable family signatures. The elimination of A, B, and D relies on the absence of characteristic catalytic or binding motifs, which is standard sequence analysis. While the primary experimentally verified function is redox (not offered as a choice), the chaperone annotation and family context make C the most defensible answer among the four options without requiring recall of this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (glycosaminoglycan binding), B (histone deacetylase activity), and D (peptide binding) are clearly incompatible with the sequence and family context. C (protein folding chaperone) is the only option with any GO annotation for this protein and is supported by PhLP family knowledge. Although the primary experimental function is thioredoxin-disulfide reductase (not offered), among the four choices only C has a biological basis, so no genuine ambiguity exists within the provided alternatives.


### Important caveats

- The primary experimentally verified molecular function (IDA evidence, EC 1.8.1.9) is thioredoxin-disulfide reductase / protein-disulfide reductase activity, which is not among the offered choices. The chaperone annotation (GO:0044183) carries only NAS:FlyBase evidence, weaker than the IDA redox annotation.
- The PhLP3 chaperone annotation may reflect a secondary or context-dependent role (e.g., during spermiogenesis) rather than the primary catalytic activity.
- The sequence's thioredoxin-like fold could lead a knowledgeable model to predict redox activity as the primary function; the chaperone answer depends on recognizing the PhLP family and its chaperone associations rather than the fold's canonical enzymatic role.
- The GO term 'peptide binding' (D) is a broad binding category; a model might briefly consider it since chaperones do bind protein substrates, but the GO definition of GO:0044183 specifically includes 'assist the protein folding process,' making C more precise for a chaperone than the generic D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 216-aa sequence displays a coiled-coil-like N-terminal region followed by a thioredoxin-like fold (containing a CxxC-like redox motif visible around residues ~100–115: 'CHFYRDSTERCK'), consistent with the Phosducin-like protein (PhLP) family architecture. PhLP2 is a well-characterized subunit of the CCT/TRiC chaperonin complex and is a canonical chaperone. PhLP3, as a family member sharing the thioredoxin-like fold and overall domain organization, has been described in the literature as possessing chaperone-like properties. A model recognizing the PhLP family from these sequence features can transfer the chaperone association from PhLP2 to PhLP3. Meanwhile, the other options can be eliminated: (A) glycosaminoglycan binding requires basic/clustered motifs or specific carbohydrate-recognition domains absent here; (B) histone deacetylase activity requires Zn²⁺-binding catalytic motifs (H-x₁₁-H-D-x₃-H) or NAD⁺-binding motifs (for sirtuins), none of which are present; (D) peptide binding implies specific peptide-recognition domains (MHC, SH3, PDZ, etc.) not found in this sequence. Among the four choices, C is the only one with a plausible biological connection via family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PhLP family–chaperone link is well-established transferable knowledge (PhLP2 = CCT-β). The sequence's thioredoxin-like fold and coiled-coil architecture are recognizable family signatures. The elimination of A, B, and D relies on the absence of characteristic catalytic or binding motifs, which is standard sequence analysis. While the primary experimentally verified function is redox (not offered as a choice), the chaperone annotation and family context make C the most defensible answer among the four options without requiring recall of this exact protein's database record."
  },
  "case_id": "GO_molecular_function_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C8",
      "C9",
      "C5",
      "H5",
      "H6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for Q9VGV8 (Phosducin-like protein 3, Drosophila melanogaster) carries GO:0044183 'protein folding chaperone' with NAS:FlyBase evidence (C7/H5). This is the only option among A–D that has any GO annotation for this protein. However, the primary experimentally verified molecular function (IDA:FlyBase, GO:0047134) is protein-disulfide reductase [NAD(P)H] activity (EC 1.8.1.9, thioredoxin-disulfide reductase), which is not offered as a choice. The chaperone annotation is NAS (non-traceable author statement), weaker than the IDA redox annotation. Among the four offered alternatives, C is the only one with any annotation for this protein, so the key is supported within the constrained option set, though it represents a secondary or ancillary function rather than the primary catalytic activity."
  },
  "important_caveats": [
    "The primary experimentally verified molecular function (IDA evidence, EC 1.8.1.9) is thioredoxin-disulfide reductase / protein-disulfide reductase activity, which is not among the offered choices. The chaperone annotation (GO:0044183) carries only NAS:FlyBase evidence, weaker than the IDA redox annotation.",
    "The PhLP3 chaperone annotation may reflect a secondary or context-dependent role (e.g., during spermiogenesis) rather than the primary catalytic activity.",
    "The sequence's thioredoxin-like fold could lead a knowledgeable model to predict redox activity as the primary function; the chaperone answer depends on recognizing the PhLP family and its chaperone associations rather than the fold's canonical enzymatic role.",
    "The GO term 'peptide binding' (D) is a broad binding category; a model might briefly consider it since chaperones do bind protein substrates, but the GO definition of GO:0044183 specifically includes 'assist the protein folding process,' making C more precise for a chaperone than the generic D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (glycosaminoglycan binding), B (histone deacetylase activity), and D (peptide binding) are clearly incompatible with the sequence and family context. C (protein folding chaperone) is the only option with any GO annotation for this protein and is supported by PhLP family knowledge. Although the primary experimental function is thioredoxin-disulfide reductase (not offered), among the four choices only C has a biological basis, so no genuine ambiguity exists within the provided alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for Q9VGV8 (Phosducin-like protein 3, Drosophila melanogaster) carries GO:0044183 'protein folding chaperone' with NAS:FlyBase evidence (C7/H5). This is the only option among A–D that has any GO annotation for this protein. However, the primary experimentally verified molecular function (IDA:FlyBase, GO:0047134) is protein-disulfide reductase [NAD(P)H] activity (EC 1.8.1.9, thioredoxin-disulfide reductase), which is not offered as a choice. The chaperone annotation is NAS (non-traceable author statement), weaker than the IDA redox annotation. Among the four offered alternatives, C is the only one with any annotation for this protein, so the key is supported within the constrained option set, though it represents a secondary or ancillary function rather than the primary catalytic activity.",
    "evidence_ids": ["C7", "C8", "C9", "C5", "H5", "H6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 216-aa sequence displays a coiled-coil-like N-terminal region followed by a thioredoxin-like fold (containing a CxxC-like redox motif visible around residues ~100–115: 'CHFYRDSTERCK'), consistent with the Phosducin-like protein (PhLP) family architecture. PhLP2 is a well-characterized subunit of the CCT/TRiC chaperonin complex and is a canonical chaperone. PhLP3, as a family member sharing the thioredoxin-like fold and overall domain organization, has been described in the literature as possessing chaperone-like properties. A model recognizing the PhLP family from these sequence features can transfer the chaperone association from PhLP2 to PhLP3. Meanwhile, the other options can be eliminated: (A) glycosaminoglycan binding requires basic/clustered motifs or specific carbohydrate-recognition domains absent here; (B) histone deacetylase activity requires Zn²⁺-binding catalytic motifs (H-x₁₁-H-D-x₃-H) or NAD⁺-binding motifs (for sirtuins), none of which are present; (D) peptide binding implies specific peptide-recognition domains (MHC, SH3, PDZ, etc.) not found in this sequence. Among the four choices, C is the only one with a plausible biological connection via family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "The PhLP family–chaperone link is well-established transferable knowledge (PhLP2 = CCT-β). The sequence's thioredoxin-like fold and coiled-coil architecture are recognizable family signatures. The elimination of A, B, and D relies on the absence of characteristic catalytic or binding motifs, which is standard sequence analysis. While the primary experimentally verified function is redox (not offered as a choice), the chaperone annotation and family context make C the most defensible answer among the four options without requiring recall of this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (glycosaminoglycan binding), B (histone deacetylase activity), and D (peptide binding) are clearly incompatible with the sequence and family context. C (protein folding chaperone) is the only option with any GO annotation for this protein and is supported by PhLP family knowledge. Although the primary experimental function is thioredoxin-disulfide reductase (not offered), among the four choices only C has a biological basis, so no genuine ambiguity exists within the provided alternatives."
  },
  "important_caveats": [
    "The primary experimentally verified molecular function (IDA evidence, EC 1.8.1.9) is thioredoxin-disulfide reductase / protein-disulfide reductase activity, which is not among the offered choices. The chaperone annotation (GO:0044183) carries only NAS:FlyBase evidence, weaker than the IDA redox annotation.",
    "The PhLP3 chaperone annotation may reflect a secondary or context-dependent role (e.g., during spermiogenesis) rather than the primary catalytic activity.",
    "The sequence's thioredoxin-like fold could lead a knowledgeable model to predict redox activity as the primary function; the chaperone answer depends on recognizing the PhLP family and its chaperone associations rather than the fold's canonical enzymatic role.",
    "The GO term 'peptide binding' (D) is a broad binding category; a model might briefly consider it since chaperones do bind protein substrates, but the GO definition of GO:0044183 specifically includes 'assist the protein folding process,' making C more precise for a chaperone than the generic D."
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
  "benchmark_sequence_length": 216,
  "benchmark_sequence_sha256": "c25c23004437d39c2d205acb8e99a590ca09b0fcb126425b294296e18fe712ce",
  "current_entry_audit": {
    "entryVersion": 207,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 216,
  "current_source_sequence_sha256": "c25c23004437d39c2d205acb8e99a590ca09b0fcb126425b294296e18fe712ce",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 205,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VGV8",
  "selected_historical_entry_version": 205,
  "selected_historical_record_sha256": "ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00",
  "selected_historical_source_sequence_length": 216,
  "selected_historical_source_sequence_sha256": "c25c23004437d39c2d205acb8e99a590ca09b0fcb126425b294296e18fe712ce",
  "selected_historical_version": {
    "accession": "Q9VGV8",
    "database": "Swiss-Prot",
    "entryVersion": 205,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PHLP3_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VGV8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":207,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39480878\",\"source\":\"PubMed\"}],\"value\":\"1.8.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0037843\",\"source\":\"FlyBase\"}],\"value\":\"Phosducin-like protein 3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39480878\",\"source\":\"PubMed\"}],\"value\":\"Has redox activity with thioredoxin (PubMed:39480878). Required for male fertility and maturation of sperm past the canoe stage during spermiogenesis (PubMed:39480878)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.8.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39480878\",\"source\":\"PubMed\"}],\"name\":\"[thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20345\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10698\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10700\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29950\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:50058\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39480878\",\"source\":\"PubMed\"}],\"id\":\"GO:0044183\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:protein folding chaperone\"},{\"key\":\"GoEvidenceType\",\"value\":\"NAS:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/31",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39480878\",\"source\":\"PubMed\"}],\"id\":\"GO:0047134\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:protein-disulfide reductase [NAD(P)H] activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/32",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004791\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:thioredoxin-disulfide reductase (NADPH) activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-EC\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/33",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Petit C.\",\"Kojak E.\",\"Webster S.\",\"Marra M.\",\"Sweeney B.\",\"Chaikin C.\",\"Jemc J.C.\",\"Kanzok S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39480878\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0306676\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0306676\",\"id\":\"39480878\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e0306676\",\"publicationDate\":\"2024\",\"title\":\"The evolutionarily conserved PhLP3 is essential for sperm development in Drosophila melanogaster.\",\"volume\":\"19\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:29.511607+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGV8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)

```json
{
  "entry_version": 205,
  "evidence_id": "H1",
  "excerpt": "ID   PHLP3_DROME             Reviewed;         216 AA.\nAC   Q9VGV8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 205.\nDE   RecName: Full=Phosducin-like protein 3 {ECO:0000312|FlyBase:FBgn0037843};\nDE            EC=1.8.1.9 {ECO:0000269|PubMed:39480878};\nGN   Name=PhLP3 {ECO:0000312|FlyBase:FBgn0037843};\nGN   ORFNames=CG4511 {ECO:0000312|FlyBase:FBgn0037843};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.609437+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00",
  "url": "https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)

```json
{
  "entry_version": 205,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, TISSUE\nRP   SPECIFICITY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39480878; DOI=10.1371/journal.pone.0306676;\nRA   Petit C., Kojak E., Webster S., Marra M., Sweeney B., Chaikin C.,\nRA   Jemc J.C., Kanzok S.M.;\nRT   \"The evolutionarily conserved PhLP3 is essential for sperm development in\nRT   Drosophila melanogaster.\";\nRL   PLoS ONE 19:e0306676-e0306676(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.609437+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00",
  "url": "https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)

```json
{
  "entry_version": 205,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Has redox activity with thioredoxin (PubMed:39480878).\nCC       Required for male fertility and maturation of sperm past the canoe\nCC       stage during spermiogenesis (PubMed:39480878).\nCC       {ECO:0000269|PubMed:39480878}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.609437+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00",
  "url": "https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)

```json
{
  "entry_version": 205,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=[thioredoxin]-dithiol + NADP(+) = [thioredoxin]-disulfide +\nCC         NADPH + H(+); Xref=Rhea:RHEA:20345, Rhea:RHEA-COMP:10698, Rhea:RHEA-\nCC         COMP:10700, ChEBI:CHEBI:15378, ChEBI:CHEBI:29950, ChEBI:CHEBI:50058,\nCC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.8.1.9;\nCC         Evidence={ECO:0000269|PubMed:39480878};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.609437+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00",
  "url": "https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)

```json
{
  "entry_version": 205,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0044183; F:protein folding chaperone; NAS:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.609437+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00",
  "url": "https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)

```json
{
  "entry_version": 205,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0047134; F:protein-disulfide reductase [NAD(P)H] activity; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.609437+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-146",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00",
  "url": "https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)

```json
{
  "entry_version": 205,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0004791; F:thioredoxin-disulfide reductase (NADPH) activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.609437+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 147-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00",
  "url": "https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004407\nname: histone deacetylase activity\nnamespace: molecular_function\ndef: \"Removal of an acetyl group from a lysine residue in a histone.\" [PMID:24691964, PMID:9893272]\ncomment: Histone deacytylase (HDAC) enzymes are divided into four classes: the Class I Rpd3-like proteins (in human: HDAC1, HDAC2, HDAC3, and HDAC8); the Class II Hda1-like proteins (in human: HDAC4, HDAC5, HDAC6, HDAC7, HDAC9, and HDAC10); the Class III Sir2-like proteins (in human: SIRT1, SIRT2, SIRT3, SIRT4, SIRT5, SIRT6, and SIRT7); and the Class IV protein (HDAC11 in human). Except for Class III enzymes, the mechanism is a metal-dependent hydrolysis of the acetylated substrate. The Class III HDACs use NAD+ as a reactant to deacetylate acetyl lysine residues of protein substrates forming nicotinamide, the deacetylated product, and the metabolite 2'-O-acetyl-ADP-ribose. Therefore, Class III are classified as transferases (EC:2) and others are hydrolases (EC:3).\nsynonym: \"histone deacetylase activity (NAD-independent)\" EXACT []\nxref: Reactome:R-HSA-2545203 \"Deacetylation of cleaved cohesin\"\nxref: Reactome:R-HSA-2545253 \"Deacetylation of cohesin\"\nxref: Reactome:R-HSA-3769447 \"HDAC1:2-containing complex deacetylate histones\"\nxref: Reactome:R-HSA-3777129 \"HDAC3 containing complexes deacetylate histone\"\nxref: Reactome:R-HSA-3782637 \"HDAC8 deacetylates histones\"\nxref: Reactome:R-HSA-3782655 \"HDAC10 deacetylates histone\"\nxref: Reactome:R-HSA-427514 \"eNoSC deacetylates histone H3\"\nxref: Reactome:R-HSA-433672 \"NoRC:HDAC:DNMT deacetylates histone H4 and methylates histone H3\"\nxref: Reactome:R-HSA-6805650 \"MTA2-NuRD complex deacetylates TP53\"\nis_a: GO:0033558 ! protein lysine deacetylase activity\nis_a: GO:0140993 ! histone modifying activity\nproperty_value: skos:broadMatch EC:2.3.1.-\nproperty_value: skos:broadMatch EC:3.5.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004407",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 41440-41460",
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
  "excerpt": "[Term]\nid: GO:0005539\nname: glycosaminoglycan binding\nnamespace: molecular_function\ndef: \"Binding to a glycan (polysaccharide) containing a substantial proportion of aminomonosaccharide residues.\" [GOC:jl, ISBN:0198506732]\nsubset: goslim_chembl\nis_a: GO:0097367 ! carbohydrate derivative binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005539",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 57150-57157",
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
  "excerpt": "[Term]\nid: GO:0042277\nname: peptide binding\nnamespace: molecular_function\ndef: \"Binding to a peptide, an organic compound comprising two or more amino acids linked by peptide bonds.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_pir\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042277",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 235888-235896",
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
  "excerpt": "[Term]\nid: GO:0044183\nname: protein folding chaperone\nnamespace: molecular_function\ndef: \"Binding to a protein or a protein-containing complex to assist the protein folding process.\" [GOC:mtg_cambridge_2009]\ncomment: Note that a protein folding chaperone binds an unfolded protein to fold it. Do not confuse with unfolded protein holdase activity, which binds an unfolded protein and keeps it unfolded to deliver it to its final destination.\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_prokaryote\nsynonym: \"chaperone activity\" BROAD []\nsynonym: \"protein binding involved in protein folding\" EXACT []\nxref: Reactome:R-HSA-9018785 \"RHOBTB2 binds GTP\"\nxref: Reactome:R-HSA-9855212 \"SDHA binds to SDHB\"\nxref: Reactome:R-HSA-9865893 \"MT-CYB is translated\"\nxref: Reactome:R-HSA-9866253 \"apo-UQCRFS1 binds LYRM7\"\nis_a: GO:0003674 ! molecular_function\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044183",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 255011-255028",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 135. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
