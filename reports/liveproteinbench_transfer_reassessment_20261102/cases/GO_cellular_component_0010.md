# GO_cellular_component_0010

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0010.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — cytosolic small ribosomal subunit

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATVYDVPGDLLVERVAKALKEVPEIKPPEWAPFVKTGRHKERLPEQEDWWYYRVASVFRKVYIDGPVGIERLRTWYGGRKNRGHAPEHFYKAGGSIIRKALQQLEAAGFVQKVPGEGRIVTPKGQSFLDKIATELKKELEEQIPELKKY

[Multiple Choices]
A. ATP-binding cassette (ABC) transporter complex
B. checkpoint clamp complex
C. transcription regulator complex
D. cytosolic small ribosomal subunit
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

> The exact sequence matches a UniProt entry annotated as small ribosomal subunit protein eS19 by a HAMAP computational rule, with a GO annotation to the cytosolic small ribosomal subunit supported by IBA. This supports D, though the supplied evidence is computational/inferred rather than direct experimental localization evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 150-residue sequence is a compact, basic protein consistent with the conserved archaeal eS19 small-ribosomal-protein family. Family-level recognition from its sequence provides a meaningful route to D: ABC transporter complexes require characteristic membrane/transport components, while checkpoint clamps are PCNA-like clamp proteins rather than this ribosomal-protein family. The inference is probabilistic, not a direct localization measurement.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable recognition of a conserved ribosomal-protein family meaningfully distinguishes D among these choices; recalling the exact protein's database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level inference favors the cytosolic small ribosomal subunit over the offered alternatives.


### Important caveats

- The sequence-matched annotation uses computational HAMAP and IBA evidence; the excerpts do not establish experimental localization.
- The exact historical ontology snapshot is unknown, but the offered D term is supported in the cited records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 150-residue sequence is a compact, basic protein consistent with the conserved archaeal eS19 small-ribosomal-protein family. Family-level recognition from its sequence provides a meaningful route to D: ABC transporter complexes require characteristic membrane/transport components, while checkpoint clamps are PCNA-like clamp proteins rather than this ribosomal-protein family. The inference is probabilistic, not a direct localization measurement.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of a conserved ribosomal-protein family meaningfully distinguishes D among these choices; recalling the exact protein's database record is not necessary."
  },
  "case_id": "GO_cellular_component_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as small ribosomal subunit protein eS19 by a HAMAP computational rule, with a GO annotation to the cytosolic small ribosomal subunit supported by IBA. This supports D, though the supplied evidence is computational/inferred rather than direct experimental localization evidence."
  },
  "important_caveats": [
    "The sequence-matched annotation uses computational HAMAP and IBA evidence; the excerpts do not establish experimental localization.",
    "The exact historical ontology snapshot is unknown, but the offered D term is supported in the cited records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference favors the cytosolic small ribosomal subunit over the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as small ribosomal subunit protein eS19 by a HAMAP computational rule, with a GO annotation to the cytosolic small ribosomal subunit supported by IBA. This supports D, though the supplied evidence is computational/inferred rather than direct experimental localization evidence.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 150-residue sequence is a compact, basic protein consistent with the conserved archaeal eS19 small-ribosomal-protein family. Family-level recognition from its sequence provides a meaningful route to D: ABC transporter complexes require characteristic membrane/transport components, while checkpoint clamps are PCNA-like clamp proteins rather than this ribosomal-protein family. The inference is probabilistic, not a direct localization measurement.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of a conserved ribosomal-protein family meaningfully distinguishes D among these choices; recalling the exact protein's database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference favors the cytosolic small ribosomal subunit over the offered alternatives."
  },
  "important_caveats": [
    "The sequence-matched annotation uses computational HAMAP and IBA evidence; the excerpts do not establish experimental localization.",
    "The exact historical ontology snapshot is unknown, but the offered D term is supported in the cited records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry Q5JGN5 is annotated as 'Small ribosomal subunit protein eS19' (HAMAP rule MF_01474) and carries GO:0022627 'cytosolic small ribosomal subunit' (evidence C4, C5, H1, H2). The GO term text matches option D exactly. The annotation evidence code is IBA:GO_Central (computational transfer by biological aspect), and the protein name is assigned by HAMAP family rule, so the support is computational/family-based rather than experimentally validated. Nevertheless, the annotation directly supports the expected answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 150-aa sequence provides several transferable discriminators. (1) Size: ABC transporter subunits (option A) require transmembrane domains and nucleotide-binding domains (Walker A/B motifs) and are typically 400–1500+ aa; checkpoint clamp complex subunits (option B, e.g. Rad9/Rad1/Hus1) are PCNA-like folds of 500–700+ aa. A 150-aa protein is far too small for either, eliminating A and B. (2) Basic character: The sequence is strongly basic (high K/R density, e.g. 'RKALQQLEAAGFVQK', 'RIVTPKGQSFLDKIATELKKELEEQIPELKKY'), which is the hallmark of ribosomal proteins that electrostatically contact rRNA. Transcription regulators (option C) tend to carry specific DNA-binding motifs (helix-turn-helix, zinc fingers, winged-helix) and generally show less extreme net positive charge. (3) Absence of identifiable transmembrane helices, Walker A/B motifs, or DNA-binding domain signatures in a 150-aa basic protein is most consistent with a small ribosomal subunit protein fold (e.g. beta-ribbon or SH3-like fold common in small-subunit proteins). These family-level features—small size, extreme basicity, lack of transporter or DNA-binding motifs—meaningfully favor D over A, B, and C without requiring prior knowledge of this exact protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence length, net basic charge, and absence of transporter or DNA-binding motifs allow a knowledgeable model to eliminate A and B by size, and to favor D over C based on the ribosomal-protein-like basic composition and lack of transcription-factor motifs. This is a legitimate family-level inference from general protein biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are excluded by the small protein size. Option C is less consistent given the extreme basic character and absence of recognizable DNA-binding motifs. Option D is the most consistent with all observed features. No two options are equally defensible.


### Important caveats

- The GO annotation (GO:0022627) is supported by IBA:GO_Central (computational transfer), not direct experimental evidence; the protein name comes from HAMAP family rule MF_01474.
- The organism is an archaeon (Thermococcus kodakarensis); the GO term 'cytosolic small ribosomal subunit' includes archaeal small subunit proteins as a narrow synonym ('prokaryotic small ribosomal subunit').
- Distinguishing D from C relies on probabilistic family-level reasoning (basic character, absence of DNA-binding motifs) rather than a definitive structural proof; some small archaeal transcription regulators exist, though their sequence signatures differ.
- The reviewer-only accession Q5JGN5 and organism identity were not available to the evaluated model; the reasoning above uses only the sequence and general protein knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 150-aa sequence provides several transferable discriminators. (1) Size: ABC transporter subunits (option A) require transmembrane domains and nucleotide-binding domains (Walker A/B motifs) and are typically 400–1500+ aa; checkpoint clamp complex subunits (option B, e.g. Rad9/Rad1/Hus1) are PCNA-like folds of 500–700+ aa. A 150-aa protein is far too small for either, eliminating A and B. (2) Basic character: The sequence is strongly basic (high K/R density, e.g. 'RKALQQLEAAGFVQK', 'RIVTPKGQSFLDKIATELKKELEEQIPELKKY'), which is the hallmark of ribosomal proteins that electrostatically contact rRNA. Transcription regulators (option C) tend to carry specific DNA-binding motifs (helix-turn-helix, zinc fingers, winged-helix) and generally show less extreme net positive charge. (3) Absence of identifiable transmembrane helices, Walker A/B motifs, or DNA-binding domain signatures in a 150-aa basic protein is most consistent with a small ribosomal subunit protein fold (e.g. beta-ribbon or SH3-like fold common in small-subunit proteins). These family-level features—small size, extreme basicity, lack of transporter or DNA-binding motifs—meaningfully favor D over A, B, and C without requiring prior knowledge of this exact protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence length, net basic charge, and absence of transporter or DNA-binding motifs allow a knowledgeable model to eliminate A and B by size, and to favor D over C based on the ribosomal-protein-like basic composition and lack of transcription-factor motifs. This is a legitimate family-level inference from general protein biology."
  },
  "case_id": "GO_cellular_component_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry Q5JGN5 is annotated as 'Small ribosomal subunit protein eS19' (HAMAP rule MF_01474) and carries GO:0022627 'cytosolic small ribosomal subunit' (evidence C4, C5, H1, H2). The GO term text matches option D exactly. The annotation evidence code is IBA:GO_Central (computational transfer by biological aspect), and the protein name is assigned by HAMAP family rule, so the support is computational/family-based rather than experimentally validated. Nevertheless, the annotation directly supports the expected answer."
  },
  "important_caveats": [
    "The GO annotation (GO:0022627) is supported by IBA:GO_Central (computational transfer), not direct experimental evidence; the protein name comes from HAMAP family rule MF_01474.",
    "The organism is an archaeon (Thermococcus kodakarensis); the GO term 'cytosolic small ribosomal subunit' includes archaeal small subunit proteins as a narrow synonym ('prokaryotic small ribosomal subunit').",
    "Distinguishing D from C relies on probabilistic family-level reasoning (basic character, absence of DNA-binding motifs) rather than a definitive structural proof; some small archaeal transcription regulators exist, though their sequence signatures differ.",
    "The reviewer-only accession Q5JGN5 and organism identity were not available to the evaluated model; the reasoning above uses only the sequence and general protein knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are excluded by the small protein size. Option C is less consistent given the extreme basic character and absence of recognizable DNA-binding motifs. Option D is the most consistent with all observed features. No two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry Q5JGN5 is annotated as 'Small ribosomal subunit protein eS19' (HAMAP rule MF_01474) and carries GO:0022627 'cytosolic small ribosomal subunit' (evidence C4, C5, H1, H2). The GO term text matches option D exactly. The annotation evidence code is IBA:GO_Central (computational transfer by biological aspect), and the protein name is assigned by HAMAP family rule, so the support is computational/family-based rather than experimentally validated. Nevertheless, the annotation directly supports the expected answer.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 150-aa sequence provides several transferable discriminators. (1) Size: ABC transporter subunits (option A) require transmembrane domains and nucleotide-binding domains (Walker A/B motifs) and are typically 400–1500+ aa; checkpoint clamp complex subunits (option B, e.g. Rad9/Rad1/Hus1) are PCNA-like folds of 500–700+ aa. A 150-aa protein is far too small for either, eliminating A and B. (2) Basic character: The sequence is strongly basic (high K/R density, e.g. 'RKALQQLEAAGFVQK', 'RIVTPKGQSFLDKIATELKKELEEQIPELKKY'), which is the hallmark of ribosomal proteins that electrostatically contact rRNA. Transcription regulators (option C) tend to carry specific DNA-binding motifs (helix-turn-helix, zinc fingers, winged-helix) and generally show less extreme net positive charge. (3) Absence of identifiable transmembrane helices, Walker A/B motifs, or DNA-binding domain signatures in a 150-aa basic protein is most consistent with a small ribosomal subunit protein fold (e.g. beta-ribbon or SH3-like fold common in small-subunit proteins). These family-level features—small size, extreme basicity, lack of transporter or DNA-binding motifs—meaningfully favor D over A, B, and C without requiring prior knowledge of this exact protein's record.",
    "missing_item_specific_fact": "",
    "reason": "The sequence length, net basic charge, and absence of transporter or DNA-binding motifs allow a knowledgeable model to eliminate A and B by size, and to favor D over C based on the ribosomal-protein-like basic composition and lack of transcription-factor motifs. This is a legitimate family-level inference from general protein biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are excluded by the small protein size. Option C is less consistent given the extreme basic character and absence of recognizable DNA-binding motifs. Option D is the most consistent with all observed features. No two options are equally defensible."
  },
  "important_caveats": [
    "The GO annotation (GO:0022627) is supported by IBA:GO_Central (computational transfer), not direct experimental evidence; the protein name comes from HAMAP family rule MF_01474.",
    "The organism is an archaeon (Thermococcus kodakarensis); the GO term 'cytosolic small ribosomal subunit' includes archaeal small subunit proteins as a narrow synonym ('prokaryotic small ribosomal subunit').",
    "Distinguishing D from C relies on probabilistic family-level reasoning (basic character, absence of DNA-binding motifs) rather than a definitive structural proof; some small archaeal transcription regulators exist, though their sequence signatures differ.",
    "The reviewer-only accession Q5JGN5 and organism identity were not available to the evaluated model; the reasoning above uses only the sequence and general protein knowledge."
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
  "benchmark_sequence_length": 150,
  "benchmark_sequence_sha256": "ca24b2f2c78aeeaeecd6fcfc750a322ea6aecc81681fc3099d44313021e584ba",
  "current_entry_audit": {
    "entryVersion": 106,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-02-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 150,
  "current_source_sequence_sha256": "ca24b2f2c78aeeaeecd6fcfc750a322ea6aecc81681fc3099d44313021e584ba",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 104,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5JGN5",
  "selected_historical_entry_version": 104,
  "selected_historical_record_sha256": "6db90196a1a395ff770ce2fe5f3dc8be7b57ed1244fe3114f10726e4eadae529",
  "selected_historical_source_sequence_length": 150,
  "selected_historical_source_sequence_sha256": "ca24b2f2c78aeeaeecd6fcfc750a322ea6aecc81681fc3099d44313021e584ba",
  "selected_historical_version": {
    "accession": "Q5JGN5",
    "database": "Swiss-Prot",
    "entryVersion": 104,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RS19E_THEKO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JGN5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5JGN5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:19.785707+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JGN5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JGN5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":106,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-02-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:19.785707+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JGN5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JGN5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Pyrococcus kodakaraensis (strain KOD1)\",\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Thermococcus\"],\"scientificName\":\"Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)\",\"taxonId\":69014}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:19.785707+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JGN5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JGN5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01474\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Small ribosomal subunit protein eS19\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:19.785707+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JGN5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JGN5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0022627\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosolic small ribosomal subunit\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/27",
  "retrieved_utc": "2026-11-02T04:31:19.785707+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JGN5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JGN5?format=txt&versions=104)

```json
{
  "entry_version": 104,
  "evidence_id": "H1",
  "excerpt": "ID   RS19E_THEKO             Reviewed;         150 AA.\nAC   Q5JGN5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-FEB-2005, sequence version 1.\nDT   18-JUN-2025, entry version 104.\nDE   RecName: Full=Small ribosomal subunit protein eS19 {ECO:0000255|HAMAP-Rule:MF_01474};\nGN   Name=rps19e {ECO:0000255|HAMAP-Rule:MF_01474};\nGN   OrderedLocusNames=TK1276 {ECO:0000312|EMBL:BAD85465.1};\nOS   Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)\nOS   (Pyrococcus kodakaraensis (strain KOD1)).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Thermococcus.\nOX   NCBI_TaxID=69014;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:23.320142+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6db90196a1a395ff770ce2fe5f3dc8be7b57ed1244fe3114f10726e4eadae529",
  "url": "https://rest.uniprot.org/unisave/Q5JGN5?format=txt&versions=104"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JGN5?format=txt&versions=104)

```json
{
  "entry_version": 104,
  "evidence_id": "H2",
  "excerpt": "DR   GO; GO:0022627; C:cytosolic small ribosomal subunit; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:23.320142+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6db90196a1a395ff770ce2fe5f3dc8be7b57ed1244fe3114f10726e4eadae529",
  "url": "https://rest.uniprot.org/unisave/Q5JGN5?format=txt&versions=104"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000181\nname: obsolete cytosolic small ribosomal subunit\nnamespace: cellular_component\ndef: \"OBSOLETE. (Was not defined before being made obsolete).\" [GOC:ai]\ncomment: This term was made obsolete because more specific children exist.\nsynonym: \"cytosolic small ribosomal subunit\" EXACT []\nis_obsolete: true\nconsider: GO:0022627\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000181",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1801-1810",
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
  "excerpt": "[Term]\nid: GO:0005667\nname: transcription regulator complex\nnamespace: cellular_component\nalt_id: GO:0044797\nalt_id: GO:0044798\ndef: \"A protein complex that is capable of associating with DNA by direct binding, or via other DNA-binding proteins or complexes, and regulating transcription.\" [GOC:jl]\nsubset: goslim_pir\nsynonym: \"cytoplasmic transcription factor complex\" RELATED []\nsynonym: \"nuclear transcription factor complex\" RELATED []\nsynonym: \"transcription factor complex\" RELATED []\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005667",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58346-58358",
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
  "excerpt": "[Term]\nid: GO:0022627\nname: cytosolic small ribosomal subunit\nnamespace: cellular_component\nalt_id: GO:0005843\nalt_id: GO:0009283\nalt_id: GO:0030499\nalt_id: GO:0030873\ndef: \"The small subunit of a ribosome located in the cytosol.\" [GOC:mtg_sensu]\nsynonym: \"30S ribosomal subunit\" NARROW []\nsynonym: \"40S ribosomal subunit\" NARROW []\nsynonym: \"eukaryotic ribosomal SSU\" NARROW []\nsynonym: \"prokaryotic small ribosomal subunit\" NARROW []\nis_a: GO:0015935 ! small ribosomal subunit\nrelationship: part_of GO:0022626 ! cytosolic ribosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0022627",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 160585-160600",
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
  "excerpt": "[Term]\nid: GO:0030896\nname: checkpoint clamp complex\nnamespace: cellular_component\ndef: \"Conserved heterotrimeric complex of PCNA-like proteins that is loaded onto DNA at sites of DNA damage.\" [PMID:12531008]\ncomment: Note that the following subunit names have been used: human RAD9/RAD1/HUS1; S. pombe Rad9/Rad1/Hus1; S. cerevisiae Ddc1p/Rad17p/Mec3p.\nsynonym: \"CCC\" EXACT []\nsynonym: \"Rad9-Hus1-Rad1 (9-1-1) clamp complex\" EXACT []\nis_a: GO:0140513 ! nuclear protein-containing complex\nrelationship: part_of GO:0000794 ! condensed nuclear chromosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030896",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 171270-171280",
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
  "excerpt": "[Term]\nid: GO:0043190\nname: ATP-binding cassette (ABC) transporter complex\nnamespace: cellular_component\nalt_id: GO:0043191\nalt_id: GO:0043192\ndef: \"A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter.\" [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"ABC-type efflux permease complex\" NARROW []\nsynonym: \"ABC-type efflux porter complex\" NARROW []\nsynonym: \"ABC-type uptake permease complex\" NARROW []\nsynonym: \"mating pheromone exporter\" NARROW []\nis_a: GO:0098533 ! ATPase dependent transmembrane transport complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043190",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 244782-244797",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
