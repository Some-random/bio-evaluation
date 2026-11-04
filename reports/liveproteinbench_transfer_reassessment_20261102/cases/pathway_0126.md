# pathway_0126

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0126.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Carbohydrate degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAAVTRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRALEQELSGTVFIPGDVTQERDLQTLVSETLSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEVNLLGTYTLIKLALPHLRKSRGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRHGVRVNCISPGNIWTPLWEELAASTSDPRATILEGTLAQPLGRMGQPAEVAAAAVFLASEATFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH

[Multiple Choices]
A. Carbohydrate degradation
B. Alkaloid biosynthesis. .
C. peptidoglycan degradation. .
D. pyruvate from D-glyceraldehyde 3-phosphate: step 2/5. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record assigns this protein to carbohydrate degradation, specifically L-fucose degradation. The annotation is supported by evidence transferred from another UniProt entry (ECO:0000250), not by direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal glycine-rich Rossmann-like motif and sequence are consistent with a soluble short-chain dehydrogenase/reductase, rather than the usual glyceraldehyde-3-phosphate dehydrogenase of the specific glycolytic step in D. Among the options, carbohydrate degradation is a credible broad pathway for a sugar-oxidizing dehydrogenase; alkaloid and peptidoglycan pathways are less plausible matches. This is a family-level, probabilistic inference, not proof of the precise substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable enzyme-family knowledge and the contrast with the specific glycolytic enzyme in D give a meaningful basis to favor A among these alternatives, even though the sequence alone does not establish the exact pathway annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices distinguish broad carbohydrate degradation from a specific glycolytic step and unrelated specialized pathways; no second option is comparably supported by the sequence-level inference.


### Important caveats

- The pathway annotation is based on similarity-based evidence transferred from another protein, not direct experimental evidence shown here.
- The exact substrate and pathway assignment are less certain from sequence motifs alone than the broad enzyme-family inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and sequence are consistent with a soluble short-chain dehydrogenase/reductase, rather than the usual glyceraldehyde-3-phosphate dehydrogenase of the specific glycolytic step in D. Among the options, carbohydrate degradation is a credible broad pathway for a sugar-oxidizing dehydrogenase; alkaloid and peptidoglycan pathways are less plausible matches. This is a family-level, probabilistic inference, not proof of the precise substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family knowledge and the contrast with the specific glycolytic enzyme in D give a meaningful basis to favor A among these alternatives, even though the sequence alone does not establish the exact pathway annotation."
  },
  "case_id": "pathway_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein to carbohydrate degradation, specifically L-fucose degradation. The annotation is supported by evidence transferred from another UniProt entry (ECO:0000250), not by direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The pathway annotation is based on similarity-based evidence transferred from another protein, not direct experimental evidence shown here.",
    "The exact substrate and pathway assignment are less certain from sequence motifs alone than the broad enzyme-family inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish broad carbohydrate degradation from a specific glycolytic step and unrelated specialized pathways; no second option is comparably supported by the sequence-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein to carbohydrate degradation, specifically L-fucose degradation. The annotation is supported by evidence transferred from another UniProt entry (ECO:0000250), not by direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and sequence are consistent with a soluble short-chain dehydrogenase/reductase, rather than the usual glyceraldehyde-3-phosphate dehydrogenase of the specific glycolytic step in D. Among the options, carbohydrate degradation is a credible broad pathway for a sugar-oxidizing dehydrogenase; alkaloid and peptidoglycan pathways are less plausible matches. This is a family-level, probabilistic inference, not proof of the precise substrate.",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family knowledge and the contrast with the specific glycolytic enzyme in D give a meaningful basis to favor A among these alternatives, even though the sequence alone does not establish the exact pathway annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish broad carbohydrate degradation from a specific glycolytic step and unrelated specialized pathways; no second option is comparably supported by the sequence-level inference."
  },
  "important_caveats": [
    "The pathway annotation is based on similarity-based evidence transferred from another protein, not direct experimental evidence shown here.",
    "The exact substrate and pathway assignment are less certain from sequence motifs alone than the broad enzyme-family inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E9Q3D4 (sequence matched, 273 aa) annotates this protein as L-fucose dehydrogenase (EC 1.1.1.122) with pathway 'Carbohydrate degradation; L-fucose degradation' (evidence C5, H2). The annotation is based on similarity to the human ortholog (ECO:0000250), a computational inference, but L-fucose is a deoxy sugar and its oxidation by a dehydrogenase is unambiguously a carbohydrate degradation step. Choice A is supported.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical Short-chain Dehydrogenase/Reductase (SDR) family hallmarks: a Rossmann-fold NAD(P)-binding motif near the N-terminus (TGGSRGIGAA containing the GxGxxG pattern), the SDR catalytic tetrad region including the 'NAGY' motif (N-A-G-Y), and the characteristic ~273-aa length. Recognizing the SDR family eliminates option C (peptidoglycan degradation uses lysozymes, amidases, and transglycosylases—entirely different folds) and option D (the glycolysis step from G3P to pyruvate involves GAPDH, a tetrameric enzyme with a completely different fold, not an SDR). Between the remaining A and B: alkaloid biosynthesis is predominantly a plant/fungal pathway involving P450s, methyltransferases, and decarboxylases, and the sequence lacks bacterial or plant-specific features (no signal peptide, no transmembrane segments, mammalian-like composition). In mammals, NADP-dependent SDRs with sugar-substrate specificity (e.g., L-fucose dehydrogenase, glucose dehydrogenases) participate in carbohydrate degradation. This combination of SDR-family recognition and mammalian context meaningfully distinguishes A from B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SDR family features are directly readable from the sequence (Rossmann motif, catalytic tetrad, length). Transferable knowledge that SDRs are not involved in peptidoglycan degradation or glycolysis eliminates C and D. Knowledge that alkaloid biosynthesis is primarily plant/fungal and uses different enzyme classes, combined with the mammalian-like sequence context, eliminates B. This leaves A as the most defensible choice without needing to recall this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly incompatible with the SDR fold. Option B is strongly disfavored by the mammalian context and the enzyme-class mismatch. Only A remains as a coherent pathway for an NADP-dependent SDR acting on a sugar substrate in a mammalian system.


### Important caveats

- The UniProt annotation is based on similarity (ECO:0000250) to the human ortholog Q9BPX1/Q9MYP6, not direct experimental characterization of the mouse protein.
- The SDR family is very large (>200,000 members) and participates in many pathways; the argument relies on eliminating options rather than positively confirming L-fucose specificity from sequence alone.
- The mammalian origin is inferred from sequence composition and absence of prokaryotic/plant-specific features, not stated in the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical Short-chain Dehydrogenase/Reductase (SDR) family hallmarks: a Rossmann-fold NAD(P)-binding motif near the N-terminus (TGGSRGIGAA containing the GxGxxG pattern), the SDR catalytic tetrad region including the 'NAGY' motif (N-A-G-Y), and the characteristic ~273-aa length. Recognizing the SDR family eliminates option C (peptidoglycan degradation uses lysozymes, amidases, and transglycosylases—entirely different folds) and option D (the glycolysis step from G3P to pyruvate involves GAPDH, a tetrameric enzyme with a completely different fold, not an SDR). Between the remaining A and B: alkaloid biosynthesis is predominantly a plant/fungal pathway involving P450s, methyltransferases, and decarboxylases, and the sequence lacks bacterial or plant-specific features (no signal peptide, no transmembrane segments, mammalian-like composition). In mammals, NADP-dependent SDRs with sugar-substrate specificity (e.g., L-fucose dehydrogenase, glucose dehydrogenases) participate in carbohydrate degradation. This combination of SDR-family recognition and mammalian context meaningfully distinguishes A from B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SDR family features are directly readable from the sequence (Rossmann motif, catalytic tetrad, length). Transferable knowledge that SDRs are not involved in peptidoglycan degradation or glycolysis eliminates C and D. Knowledge that alkaloid biosynthesis is primarily plant/fungal and uses different enzyme classes, combined with the mammalian-like sequence context, eliminates B. This leaves A as the most defensible choice without needing to recall this specific protein's annotation."
  },
  "case_id": "pathway_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E9Q3D4 (sequence matched, 273 aa) annotates this protein as L-fucose dehydrogenase (EC 1.1.1.122) with pathway 'Carbohydrate degradation; L-fucose degradation' (evidence C5, H2). The annotation is based on similarity to the human ortholog (ECO:0000250), a computational inference, but L-fucose is a deoxy sugar and its oxidation by a dehydrogenase is unambiguously a carbohydrate degradation step. Choice A is supported."
  },
  "important_caveats": [
    "The UniProt annotation is based on similarity (ECO:0000250) to the human ortholog Q9BPX1/Q9MYP6, not direct experimental characterization of the mouse protein.",
    "The SDR family is very large (>200,000 members) and participates in many pathways; the argument relies on eliminating options rather than positively confirming L-fucose specificity from sequence alone.",
    "The mammalian origin is inferred from sequence composition and absence of prokaryotic/plant-specific features, not stated in the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with the SDR fold. Option B is strongly disfavored by the mammalian context and the enzyme-class mismatch. Only A remains as a coherent pathway for an NADP-dependent SDR acting on a sugar substrate in a mammalian system."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E9Q3D4 (sequence matched, 273 aa) annotates this protein as L-fucose dehydrogenase (EC 1.1.1.122) with pathway 'Carbohydrate degradation; L-fucose degradation' (evidence C5, H2). The annotation is based on similarity to the human ortholog (ECO:0000250), a computational inference, but L-fucose is a deoxy sugar and its oxidation by a dehydrogenase is unambiguously a carbohydrate degradation step. Choice A is supported.",
    "evidence_ids": ["C5", "H2", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical Short-chain Dehydrogenase/Reductase (SDR) family hallmarks: a Rossmann-fold NAD(P)-binding motif near the N-terminus (TGGSRGIGAA containing the GxGxxG pattern), the SDR catalytic tetrad region including the 'NAGY' motif (N-A-G-Y), and the characteristic ~273-aa length. Recognizing the SDR family eliminates option C (peptidoglycan degradation uses lysozymes, amidases, and transglycosylases—entirely different folds) and option D (the glycolysis step from G3P to pyruvate involves GAPDH, a tetrameric enzyme with a completely different fold, not an SDR). Between the remaining A and B: alkaloid biosynthesis is predominantly a plant/fungal pathway involving P450s, methyltransferases, and decarboxylases, and the sequence lacks bacterial or plant-specific features (no signal peptide, no transmembrane segments, mammalian-like composition). In mammals, NADP-dependent SDRs with sugar-substrate specificity (e.g., L-fucose dehydrogenase, glucose dehydrogenases) participate in carbohydrate degradation. This combination of SDR-family recognition and mammalian context meaningfully distinguishes A from B.",
    "missing_item_specific_fact": "",
    "reason": "The SDR family features are directly readable from the sequence (Rossmann motif, catalytic tetrad, length). Transferable knowledge that SDRs are not involved in peptidoglycan degradation or glycolysis eliminates C and D. Knowledge that alkaloid biosynthesis is primarily plant/fungal and uses different enzyme classes, combined with the mammalian-like sequence context, eliminates B. This leaves A as the most defensible choice without needing to recall this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with the SDR fold. Option B is strongly disfavored by the mammalian context and the enzyme-class mismatch. Only A remains as a coherent pathway for an NADP-dependent SDR acting on a sugar substrate in a mammalian system."
  },
  "important_caveats": [
    "The UniProt annotation is based on similarity (ECO:0000250) to the human ortholog Q9BPX1/Q9MYP6, not direct experimental characterization of the mouse protein.",
    "The SDR family is very large (>200,000 members) and participates in many pathways; the argument relies on eliminating options rather than positively confirming L-fucose specificity from sequence alone.",
    "The mammalian origin is inferred from sequence composition and absence of prokaryotic/plant-specific features, not stated in the original input."
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
  "benchmark_sequence_length": 273,
  "benchmark_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "current_entry_audit": {
    "entryVersion": 97,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-04-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 273,
  "current_source_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 95,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E9Q3D4",
  "selected_historical_entry_version": 95,
  "selected_historical_record_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "selected_historical_source_sequence_length": 273,
  "selected_historical_source_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "selected_historical_version": {
    "accession": "E9Q3D4",
    "database": "Swiss-Prot",
    "entryVersion": 95,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_MOUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E9Q3D4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":97,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-04-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mouse\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Mus\",\"Mus\"],\"scientificName\":\"Mus musculus\",\"taxonId\":10090}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9MYP6\",\"source\":\"UniProtKB\"}],\"value\":\"Carbohydrate degradation; L-fucose degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H1",
  "excerpt": "ID   DHB14_MOUSE             Reviewed;         273 AA.\nAC   E9Q3D4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-APR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 95.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=Hsd17b14 {ECO:0000312|MGI:MGI:1913315}; Synonyms=Dhrs10, retSDR3;\nOS   Mus musculus (Mouse).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Mus; Mus.\nOX   NCBI_TaxID=10090;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H2",
  "excerpt": "CC   -!- PATHWAY: Carbohydrate degradation; L-fucose degradation.\nCC       {ECO:0000250|UniProtKB:Q9MYP6}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 126. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
