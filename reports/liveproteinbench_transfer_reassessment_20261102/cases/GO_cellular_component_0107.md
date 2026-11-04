# GO_cellular_component_0107

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0107.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — cytosolic large ribosomal subunit

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKYPKQIRTYCPFCKRHTIHKVEKVKKRPRSELSAGQRRFRRKLKGYTGFPRPNPAGREKPVKKLDLRFRCTVCGKAHTRGQGFRVKKFELVEV

[Multiple Choices]
A. neuromuscular junction
B. cytosolic large ribosomal subunit
C. mitochondrial inner membrane
D. Golgi apparatus
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

> The exact sequence matches a UniProt entry annotated as large ribosomal subunit protein eL42, and the entry assigns it to the cytosolic large ribosomal subunit. The protein-family annotation is computational (HAMAP), and the GO annotation is phylogenetically inferred (IBA), not experimental evidence, but both support choice B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is short and strongly enriched in Lys and Arg, with cysteine-rich motifs, a pattern characteristic of basic ribosomal proteins. It lacks a long hydrophobic segment expected for a membrane protein and lacks an evident secretory targeting signal, making the mitochondrial inner membrane and Golgi choices poor fits; a neuromuscular-junction location is also not suggested by the sequence. Transferable recognition of ribosomal-protein sequence patterns therefore meaningfully favors the cytosolic large ribosomal subunit.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence composition and motifs can distinguish B from these alternatives without knowing this exact protein's database record. The exact eL42 annotation strengthens the key's support but is not necessary for the offered-choice distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence features favor a ribosomal protein over the offered membrane, Golgi, and neuromuscular-junction locations.


### Important caveats

- The source's GO assignment is IBA, a phylogenetic inference, rather than direct experimental localization.
- The exact author source snapshot is unknown, although the sequence-matched historical and current records support the same answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is short and strongly enriched in Lys and Arg, with cysteine-rich motifs, a pattern characteristic of basic ribosomal proteins. It lacks a long hydrophobic segment expected for a membrane protein and lacks an evident secretory targeting signal, making the mitochondrial inner membrane and Golgi choices poor fits; a neuromuscular-junction location is also not suggested by the sequence. Transferable recognition of ribosomal-protein sequence patterns therefore meaningfully favors the cytosolic large ribosomal subunit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence composition and motifs can distinguish B from these alternatives without knowing this exact protein's database record. The exact eL42 annotation strengthens the key's support but is not necessary for the offered-choice distinction."
  },
  "case_id": "GO_cellular_component_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as large ribosomal subunit protein eL42, and the entry assigns it to the cytosolic large ribosomal subunit. The protein-family annotation is computational (HAMAP), and the GO annotation is phylogenetically inferred (IBA), not experimental evidence, but both support choice B."
  },
  "important_caveats": [
    "The source's GO assignment is IBA, a phylogenetic inference, rather than direct experimental localization.",
    "The exact author source snapshot is unknown, although the sequence-matched historical and current records support the same answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features favor a ribosomal protein over the offered membrane, Golgi, and neuromuscular-junction locations."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as large ribosomal subunit protein eL42, and the entry assigns it to the cytosolic large ribosomal subunit. The protein-family annotation is computational (HAMAP), and the GO annotation is phylogenetically inferred (IBA), not experimental evidence, but both support choice B.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is short and strongly enriched in Lys and Arg, with cysteine-rich motifs, a pattern characteristic of basic ribosomal proteins. It lacks a long hydrophobic segment expected for a membrane protein and lacks an evident secretory targeting signal, making the mitochondrial inner membrane and Golgi choices poor fits; a neuromuscular-junction location is also not suggested by the sequence. Transferable recognition of ribosomal-protein sequence patterns therefore meaningfully favors the cytosolic large ribosomal subunit.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence composition and motifs can distinguish B from these alternatives without knowing this exact protein's database record. The exact eL42 annotation strengthens the key's support but is not necessary for the offered-choice distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features favor a ribosomal protein over the offered membrane, Golgi, and neuromuscular-junction locations."
  },
  "important_caveats": [
    "The source's GO assignment is IBA, a phylogenetic inference, rather than direct experimental localization.",
    "The exact author source snapshot is unknown, although the sequence-matched historical and current records support the same answer."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q5JE51) annotates this 94-aa protein as 'Large ribosomal subunit protein eL42' via HAMAP-Rule MF_01476 (C4) and assigns GO:0022625 'cytosolic large ribosomal subunit' with IBA:GO_Central evidence (C5, H2). The sequence is extremely basic (high K/R content), very short, and contains zinc-binding Cys motifs (CPFCKR, CTVCGK), all hallmarks of ribosomal proteins. The GO annotation is computational (IBA), but the protein identity as a ribosomal protein is well-supported by sequence features, and ribosomal proteins reside in the cytosol/cytoplasm. The expected answer B is consistent with the annotation and sequence characteristics.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits multiple well-known ribosomal protein features: (1) very small size (94 aa), typical of ribosomal proteins across all domains of life; (2) extreme basicity with numerous Lys and Arg residues, reflecting the need to bind negatively charged rRNA; (3) paired Cys motifs (C-P-F-C-K-R and C-T-V-C-G-K) consistent with zinc-binding motifs found in many eukaryotic/archaeal ribosomal proteins including eL42. Against option C (mitochondrial inner membrane): no N-terminal amphipathic targeting helix, no transmembrane segments. Against option D (Golgi apparatus): no signal peptide, no transmembrane domain, no Golgi retention motifs. Against option A (neuromuscular junction): this is a specialized animal cell-cell junction; no small basic protein with zinc-binding motifs would localize there—NMJ proteins are typically large membrane-associated proteins (e.g., AChR, dystrophin). The ribosomal protein family characteristics are extensively documented across hundreds of homologs and represent strong transferable knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the ribosomal protein signature (small size, extreme basicity, zinc-binding Cys motifs) from general knowledge of ribosomal proteins learned across many organisms. This family-level inference clearly distinguishes option B from the other three choices, none of which match the sequence's physicochemical properties or structural motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other three options are clearly excluded: neuromuscular junction (A) is an animal-specific synapse structure incompatible with a small basic zinc-binding protein; mitochondrial inner membrane (C) requires targeting signals absent here; Golgi apparatus (D) requires membrane/signal features absent here. Only B is consistent with the sequence features.


### Important caveats

- The GO annotation uses IBA:GO_Central (computational inference by biological aspect), not direct experimental localization evidence.
- The protein is from an archaeon (Thermococcus kodakarensis), which lacks mitochondria and Golgi; however, the organism identity is not given in the model input and the reasoning does not depend on it—the sequence features alone suffice.
- The HAMAP-Rule assignment (MF_01476) is computational but well-established for this ribosomal protein family.
- The model is not told the organism, but the ribosomal protein signature is domain-independent and sufficient to select B over the eukaryotic-specific alternatives.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits multiple well-known ribosomal protein features: (1) very small size (94 aa), typical of ribosomal proteins across all domains of life; (2) extreme basicity with numerous Lys and Arg residues, reflecting the need to bind negatively charged rRNA; (3) paired Cys motifs (C-P-F-C-K-R and C-T-V-C-G-K) consistent with zinc-binding motifs found in many eukaryotic/archaeal ribosomal proteins including eL42. Against option C (mitochondrial inner membrane): no N-terminal amphipathic targeting helix, no transmembrane segments. Against option D (Golgi apparatus): no signal peptide, no transmembrane domain, no Golgi retention motifs. Against option A (neuromuscular junction): this is a specialized animal cell-cell junction; no small basic protein with zinc-binding motifs would localize there—NMJ proteins are typically large membrane-associated proteins (e.g., AChR, dystrophin). The ribosomal protein family characteristics are extensively documented across hundreds of homologs and represent strong transferable knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the ribosomal protein signature (small size, extreme basicity, zinc-binding Cys motifs) from general knowledge of ribosomal proteins learned across many organisms. This family-level inference clearly distinguishes option B from the other three choices, none of which match the sequence's physicochemical properties or structural motifs."
  },
  "case_id": "GO_cellular_component_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q5JE51) annotates this 94-aa protein as 'Large ribosomal subunit protein eL42' via HAMAP-Rule MF_01476 (C4) and assigns GO:0022625 'cytosolic large ribosomal subunit' with IBA:GO_Central evidence (C5, H2). The sequence is extremely basic (high K/R content), very short, and contains zinc-binding Cys motifs (CPFCKR, CTVCGK), all hallmarks of ribosomal proteins. The GO annotation is computational (IBA), but the protein identity as a ribosomal protein is well-supported by sequence features, and ribosomal proteins reside in the cytosol/cytoplasm. The expected answer B is consistent with the annotation and sequence characteristics."
  },
  "important_caveats": [
    "The GO annotation uses IBA:GO_Central (computational inference by biological aspect), not direct experimental localization evidence.",
    "The protein is from an archaeon (Thermococcus kodakarensis), which lacks mitochondria and Golgi; however, the organism identity is not given in the model input and the reasoning does not depend on it—the sequence features alone suffice.",
    "The HAMAP-Rule assignment (MF_01476) is computational but well-established for this ribosomal protein family.",
    "The model is not told the organism, but the ribosomal protein signature is domain-independent and sufficient to select B over the eukaryotic-specific alternatives."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options are clearly excluded: neuromuscular junction (A) is an animal-specific synapse structure incompatible with a small basic zinc-binding protein; mitochondrial inner membrane (C) requires targeting signals absent here; Golgi apparatus (D) requires membrane/signal features absent here. Only B is consistent with the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q5JE51) annotates this 94-aa protein as 'Large ribosomal subunit protein eL42' via HAMAP-Rule MF_01476 (C4) and assigns GO:0022625 'cytosolic large ribosomal subunit' with IBA:GO_Central evidence (C5, H2). The sequence is extremely basic (high K/R content), very short, and contains zinc-binding Cys motifs (CPFCKR, CTVCGK), all hallmarks of ribosomal proteins. The GO annotation is computational (IBA), but the protein identity as a ribosomal protein is well-supported by sequence features, and ribosomal proteins reside in the cytosol/cytoplasm. The expected answer B is consistent with the annotation and sequence characteristics.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits multiple well-known ribosomal protein features: (1) very small size (94 aa), typical of ribosomal proteins across all domains of life; (2) extreme basicity with numerous Lys and Arg residues, reflecting the need to bind negatively charged rRNA; (3) paired Cys motifs (C-P-F-C-K-R and C-T-V-C-G-K) consistent with zinc-binding motifs found in many eukaryotic/archaeal ribosomal proteins including eL42. Against option C (mitochondrial inner membrane): no N-terminal amphipathic targeting helix, no transmembrane segments. Against option D (Golgi apparatus): no signal peptide, no transmembrane domain, no Golgi retention motifs. Against option A (neuromuscular junction): this is a specialized animal cell-cell junction; no small basic protein with zinc-binding motifs would localize there—NMJ proteins are typically large membrane-associated proteins (e.g., AChR, dystrophin). The ribosomal protein family characteristics are extensively documented across hundreds of homologs and represent strong transferable knowledge.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the ribosomal protein signature (small size, extreme basicity, zinc-binding Cys motifs) from general knowledge of ribosomal proteins learned across many organisms. This family-level inference clearly distinguishes option B from the other three choices, none of which match the sequence's physicochemical properties or structural motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options are clearly excluded: neuromuscular junction (A) is an animal-specific synapse structure incompatible with a small basic zinc-binding protein; mitochondrial inner membrane (C) requires targeting signals absent here; Golgi apparatus (D) requires membrane/signal features absent here. Only B is consistent with the sequence features."
  },
  "important_caveats": [
    "The GO annotation uses IBA:GO_Central (computational inference by biological aspect), not direct experimental localization evidence.",
    "The protein is from an archaeon (Thermococcus kodakarensis), which lacks mitochondria and Golgi; however, the organism identity is not given in the model input and the reasoning does not depend on it—the sequence features alone suffice.",
    "The HAMAP-Rule assignment (MF_01476) is computational but well-established for this ribosomal protein family.",
    "The model is not told the organism, but the ribosomal protein signature is domain-independent and sufficient to select B over the eukaryotic-specific alternatives."
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
  "benchmark_sequence_length": 94,
  "benchmark_sequence_sha256": "c0a362a3050d93d98be75f3ac1029e6c8fd68639ca3f45c8eda8bc47cee0a113",
  "current_entry_audit": {
    "entryVersion": 109,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-02-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 94,
  "current_source_sequence_sha256": "c0a362a3050d93d98be75f3ac1029e6c8fd68639ca3f45c8eda8bc47cee0a113",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 107,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5JE51",
  "selected_historical_entry_version": 107,
  "selected_historical_record_sha256": "54b03ede26cd2994aa8e16a71cdff8115aa30c55b07be10c28b083c9be3d4ed5",
  "selected_historical_source_sequence_length": 94,
  "selected_historical_source_sequence_sha256": "c0a362a3050d93d98be75f3ac1029e6c8fd68639ca3f45c8eda8bc47cee0a113",
  "selected_historical_version": {
    "accession": "Q5JE51",
    "database": "Swiss-Prot",
    "entryVersion": 107,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RL44E_THEKO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JE51.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5JE51\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:15.985869+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JE51.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JE51.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":109,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-02-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:15.985869+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JE51.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JE51.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Pyrococcus kodakaraensis (strain KOD1)\",\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Thermococcus\"],\"scientificName\":\"Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)\",\"taxonId\":69014}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:15.985869+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JE51.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JE51.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01476\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Large ribosomal subunit protein eL42\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:15.985869+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JE51.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JE51.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0022625\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosolic large ribosomal subunit\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/25",
  "retrieved_utc": "2026-11-02T04:31:15.985869+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33",
  "url": "https://rest.uniprot.org/uniprotkb/Q5JE51.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JE51?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H1",
  "excerpt": "ID   RL44E_THEKO             Reviewed;          94 AA.\nAC   Q5JE51;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-FEB-2005, sequence version 1.\nDT   28-JAN-2026, entry version 107.\nDE   RecName: Full=Large ribosomal subunit protein eL42 {ECO:0000255|HAMAP-Rule:MF_01476};\nGN   Name=rpl44e {ECO:0000255|HAMAP-Rule:MF_01476};\nGN   OrderedLocusNames=TK1098 {ECO:0000312|EMBL:BAD85287.1};\nOS   Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)\nOS   (Pyrococcus kodakaraensis (strain KOD1)).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Thermococcus.\nOX   NCBI_TaxID=69014;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:20.329246+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "54b03ede26cd2994aa8e16a71cdff8115aa30c55b07be10c28b083c9be3d4ed5",
  "url": "https://rest.uniprot.org/unisave/Q5JE51?format=txt&versions=107"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JE51?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H2",
  "excerpt": "DR   GO; GO:0022625; C:cytosolic large ribosomal subunit; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:20.329246+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "54b03ede26cd2994aa8e16a71cdff8115aa30c55b07be10c28b083c9be3d4ed5",
  "url": "https://rest.uniprot.org/unisave/Q5JE51?format=txt&versions=107"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000180\nname: obsolete cytosolic large ribosomal subunit\nnamespace: cellular_component\ndef: \"OBSOLETE. (Was not defined before being made obsolete).\" [GOC:ai]\ncomment: This term was made obsolete because more specific children exist.\nsynonym: \"cytosolic large ribosomal subunit\" EXACT []\nis_obsolete: true\nconsider: GO:0022625\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000180",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1791-1800",
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
  "excerpt": "[Term]\nid: GO:0005743\nname: mitochondrial inner membrane\nnamespace: cellular_component\ndef: \"The inner, i.e. lumen-facing, lipid bilayer of the mitochondrial envelope. It is highly folded to form cristae.\" [GOC:ai]\nsynonym: \"inner mitochondrial membrane\" EXACT []\nsynonym: \"inner mitochondrion membrane\" EXACT []\nsynonym: \"mitochondrion inner membrane\" EXACT []\nxref: NIF_Subcellular:sao1371347282\nxref: Wikipedia:Inner_mitochondrial_membrane\nis_a: GO:0019866 ! organelle inner membrane\nis_a: GO:0031966 ! mitochondrial membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005743",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59031-59043",
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
  "excerpt": "[Term]\nid: GO:0005794\nname: Golgi apparatus\nnamespace: cellular_component\ndef: \"A membrane-bound cytoplasmic organelle of the endomembrane system that further processes the core oligosaccharides (e.g. N-glycans) added to proteins in the endoplasmic reticulum and packages them into membrane-bound vesicles. The Golgi apparatus operates at the intersection of the secretory, lysosomal, and endocytic pathways.\" [ISBN:0198506732, PMID:9695800]\ncomment: Note that the Golgi apparatus can be located in various places in the cytoplasm. In plants and lower animal cells, the Golgi apparatus exists as many copies of discrete stacks dispersed throughout the cytoplasm, while the Golgi apparatus of interphase mammalian cells is a juxtanuclear, often pericentriolar reticulum, where the discrete Golgi stacks are stitched together to form a compact and interconnected ribbon, sometimes called the Golgi ribbon.\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"Golgi\" BROAD []\nsynonym: \"Golgi complex\" EXACT []\nsynonym: \"Golgi ribbon\" NARROW []\nxref: NIF_Subcellular:sao451912436\nxref: Wikipedia:Golgi_apparatus\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005794",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59587-59612",
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
  "excerpt": "[Term]\nid: GO:0022625\nname: cytosolic large ribosomal subunit\nnamespace: cellular_component\nalt_id: GO:0005842\nalt_id: GO:0009282\nalt_id: GO:0030498\nalt_id: GO:0030872\ndef: \"The large subunit of a ribosome located in the cytosol.\" [GOC:mtg_sensu]\nsynonym: \"50S ribosomal subunit\" NARROW []\nsynonym: \"60S ribosomal subunit\" NARROW []\nsynonym: \"eukaryotic ribosomal LSU\" NARROW []\nsynonym: \"prokaryotic large ribosomal subunit\" NARROW []\nis_a: GO:0015934 ! large ribosomal subunit\nrelationship: part_of GO:0022626 ! cytosolic ribosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0022625",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 160556-160571",
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
  "excerpt": "[Term]\nid: GO:0031594\nname: neuromuscular junction\nnamespace: cellular_component\ndef: \"The junction between the axon of a motor neuron and a muscle fiber. In response to the arrival of action potentials, the presynaptic button releases molecules of neurotransmitters into the synaptic cleft. These diffuse across the cleft and transmit the signal to the postsynaptic membrane of the muscle fiber, leading to a change in post-synaptic potential.\" [GOC:nln]\ncomment: In vertebrates, the term 'neuromuscular junction' is limited to synapses targeting skeletal muscle fibers - all of which are cholinergic and excitatory. Both inhibitory and excitatory neuromuscular junctions exist in invertebrates, utilizing a range of neurotransmitters including glutamate, GABA and 5-HT.\nsynonym: \"motor endplate\" RELATED [NIF_Subcellular:nlx_subcell_20090512]\nsynonym: \"NMJ\" RELATED [GOC:ha]\nxref: NIF_Subcellular:sao1124888485\nxref: Wikipedia:Neuromuscular_junction\nis_a: GO:0045202 ! synapse\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031594",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 178139-178150",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
