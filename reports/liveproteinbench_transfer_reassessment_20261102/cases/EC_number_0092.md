# EC_number_0092

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0092.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 1.1.1.122

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAAVTRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRALEQELSGTVFIPGDVTQERDLQTLVSETLSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEVNLLGTYTLIKLALPHLRKSRGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRHGVRVNCISPGNIWTPLWEELAASTSDPRATILEGTLAQPLGRMGQPAEVAAAAVFLASEATFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH

[Multiple Choices]
A. 1.1.1.195
B. 1.1.1.122
C. 2.3.1.319
D. 4.1.1.128
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence is matched to a UniProt entry annotated with EC 1.1.1.122, including the L-fucose dehydrogenase reaction. The annotation is explicitly supported by evidence transferred from another UniProt protein (ECO:0000250), so it supports the key as a database/computational inference, not as direct experimental confirmation for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich Rossmann-like motif consistent with an NAD-dependent short-chain dehydrogenase/reductase. That favors an oxidoreductase over the transferase and lyase options, but does not distinguish the two offered 1.1.1.x choices by substrate specificity.


**Missing item-specific fact**

> The substrate specificity or a validated family/homolog-function assignment for this protein that distinguishes EC 1.1.1.122 from EC 1.1.1.195.


**Reason**

> Transferable sequence knowledge supports a broad dehydrogenase inference, but no concrete feature in the supplied input meaningfully separates choices A and B. Selecting B therefore depends on the exact protein's more specific functional assignment or equivalent evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both choices are EC 1.1.1 oxidoreductases, and the apparent SDR/NAD-binding features do not resolve which substrate-specific EC applies. The supplied sequence alone does not distinguish them.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but its cited evidence is transferred by similarity rather than direct experimental evidence for this protein.
- The original choices provide EC numbers only, without reaction names that might help interpret the alternatives.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich Rossmann-like motif consistent with an NAD-dependent short-chain dehydrogenase/reductase. That favors an oxidoreductase over the transferase and lyase options, but does not distinguish the two offered 1.1.1.x choices by substrate specificity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The substrate specificity or a validated family/homolog-function assignment for this protein that distinguishes EC 1.1.1.122 from EC 1.1.1.195.",
    "reason": "Transferable sequence knowledge supports a broad dehydrogenase inference, but no concrete feature in the supplied input meaningfully separates choices A and B. Selecting B therefore depends on the exact protein's more specific functional assignment or equivalent evidence."
  },
  "case_id": "EC_number_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence is matched to a UniProt entry annotated with EC 1.1.1.122, including the L-fucose dehydrogenase reaction. The annotation is explicitly supported by evidence transferred from another UniProt protein (ECO:0000250), so it supports the key as a database/computational inference, not as direct experimental confirmation for this sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its cited evidence is transferred by similarity rather than direct experimental evidence for this protein.",
    "The original choices provide EC numbers only, without reaction names that might help interpret the alternatives."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both choices are EC 1.1.1 oxidoreductases, and the apparent SDR/NAD-binding features do not resolve which substrate-specific EC applies. The supplied sequence alone does not distinguish them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence is matched to a UniProt entry annotated with EC 1.1.1.122, including the L-fucose dehydrogenase reaction. The annotation is explicitly supported by evidence transferred from another UniProt protein (ECO:0000250), so it supports the key as a database/computational inference, not as direct experimental confirmation for this sequence.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich Rossmann-like motif consistent with an NAD-dependent short-chain dehydrogenase/reductase. That favors an oxidoreductase over the transferase and lyase options, but does not distinguish the two offered 1.1.1.x choices by substrate specificity.",
    "missing_item_specific_fact": "The substrate specificity or a validated family/homolog-function assignment for this protein that distinguishes EC 1.1.1.122 from EC 1.1.1.195.",
    "reason": "Transferable sequence knowledge supports a broad dehydrogenase inference, but no concrete feature in the supplied input meaningfully separates choices A and B. Selecting B therefore depends on the exact protein's more specific functional assignment or equivalent evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both choices are EC 1.1.1 oxidoreductases, and the apparent SDR/NAD-binding features do not resolve which substrate-specific EC applies. The supplied sequence alone does not distinguish them."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its cited evidence is transferred by similarity rather than direct experimental evidence for this protein.",
    "The original choices provide EC numbers only, without reaction names that might help interpret the alternatives."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E9Q3D4 (HSD17B14_MOUSE / DHB14_MOUSE) annotates EC 1.1.1.122 (L-fucose dehydrogenase) with catalytic activities for L-fucose, D-arabinose, and L-galactose oxidation by NAD+. However, the evidence code is ECO:0000250 (inferred by similarity from human Q9BPX1), meaning this is a computational/similarity-based annotation rather than direct experimental characterization. The database annotation supports the key, but the underlying evidence is transferred by homology.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmark short-chain dehydrogenase/reductase (SDR) family features: (1) a TGxxxGxG Rossmann-fold NAD-binding motif in 'VVVVTGGSRGIGAAIVRAF' (T-G-G-S-R-G-I-G matches TGxxxGxG), (2) a putative catalytic tetrad (Ser-Tyr-Lys-Asn) distributed across 'NCISPGNIW' (N, S) and 'GYGRKASKS' (Y, K), and (3) a ~273-aa length typical of SDR enzymes. These features unambiguously place the protein in the oxidoreductase class (EC 1.x.x.x), eliminating C (transferase, EC 2.3.1.319) and D (lyase, EC 4.1.1.128). Between A (1.1.1.195, L-gulonate dehydrogenase) and B (1.1.1.122, L-fucose dehydrogenase), both are NAD-dependent sugar dehydrogenases, but they belong to distinct SDR subfamilies. The sequence architecture—particularly the C-terminal 'TFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH' region and the specific arrangement of the catalytic residues—matches the HSD17B14/retSDR subfamily, a recognized SDR subfamily whose characterized members (e.g., human Q9BPX1) are annotated as L-fucose dehydrogenases. Knowledge of this subfamily's substrate preference, learned from the human homolog and other HSD17B14 orthologs, provides a transferable basis for selecting B over A. The gulonate dehydrogenase subfamily has a different sequence architecture and substrate-binding pocket configuration.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SDR family features (TGxxxGxG motif, catalytic tetrad, protein length) are directly readable from the sequence and eliminate C and D. The A-vs-B distinction rests on subfamily-level recognition: the sequence matches the HSD17B14/retSDR SDR subfamily, whose substrate preference (L-fucose dehydrogenase activity) is known from the human ortholog and other family members. This is transferable knowledge from related proteins, not a lookup of this exact entry's annotation. The inference is probabilistic rather than deterministic, but it meaningfully and credibly distinguishes B from A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A"
]
```

> Both A (1.1.1.195) and B (1.1.1.122) are NAD-dependent sugar dehydrogenases within the broader SDR superfamily. Without confident subfamily-level recognition, a model could argue for either sugar dehydrogenase. The distinction between fucose dehydrogenase and gulonate dehydrogenase depends on specific substrate-binding pocket residues that are not trivially predictable from the sequence alone. However, the overall sequence architecture and the HSD17B14/retSDR subfamily signature provide a reasonable basis for preferring B, making A a weaker but not entirely indefensible alternative.


### Important caveats

- The UniProt annotation for EC 1.1.1.122 is based on similarity inference (ECO:0000250) from human Q9BPX1, not direct experimental characterization of the mouse protein. The true substrate specificity of this mouse ortholog has not been independently confirmed by enzymatic assays.
- The distinction between EC 1.1.1.122 and 1.1.1.195 is at the subfamily level within the SDR superfamily. A model that recognizes SDR features but cannot resolve the specific subfamily would face genuine ambiguity between A and B.
- The reviewer-only evidence confirms the sequence matches E9Q3D4 (DHB14_MOUSE), but this accession and organism identity were not provided to the evaluated model. The model must rely on sequence-intrinsic features and transferable family knowledge.
- Both catalytic activities (L-fucose and D-arabinose/L-galactose oxidation) are annotated under the same EC 1.1.1.122, suggesting broad sugar specificity within this subfamily, which is consistent with the SDR family's known substrate promiscuity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmark short-chain dehydrogenase/reductase (SDR) family features: (1) a TGxxxGxG Rossmann-fold NAD-binding motif in 'VVVVTGGSRGIGAAIVRAF' (T-G-G-S-R-G-I-G matches TGxxxGxG), (2) a putative catalytic tetrad (Ser-Tyr-Lys-Asn) distributed across 'NCISPGNIW' (N, S) and 'GYGRKASKS' (Y, K), and (3) a ~273-aa length typical of SDR enzymes. These features unambiguously place the protein in the oxidoreductase class (EC 1.x.x.x), eliminating C (transferase, EC 2.3.1.319) and D (lyase, EC 4.1.1.128). Between A (1.1.1.195, L-gulonate dehydrogenase) and B (1.1.1.122, L-fucose dehydrogenase), both are NAD-dependent sugar dehydrogenases, but they belong to distinct SDR subfamilies. The sequence architecture—particularly the C-terminal 'TFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH' region and the specific arrangement of the catalytic residues—matches the HSD17B14/retSDR subfamily, a recognized SDR subfamily whose characterized members (e.g., human Q9BPX1) are annotated as L-fucose dehydrogenases. Knowledge of this subfamily's substrate preference, learned from the human homolog and other HSD17B14 orthologs, provides a transferable basis for selecting B over A. The gulonate dehydrogenase subfamily has a different sequence architecture and substrate-binding pocket configuration.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SDR family features (TGxxxGxG motif, catalytic tetrad, protein length) are directly readable from the sequence and eliminate C and D. The A-vs-B distinction rests on subfamily-level recognition: the sequence matches the HSD17B14/retSDR SDR subfamily, whose substrate preference (L-fucose dehydrogenase activity) is known from the human ortholog and other family members. This is transferable knowledge from related proteins, not a lookup of this exact entry's annotation. The inference is probabilistic rather than deterministic, but it meaningfully and credibly distinguishes B from A."
  },
  "case_id": "EC_number_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E9Q3D4 (HSD17B14_MOUSE / DHB14_MOUSE) annotates EC 1.1.1.122 (L-fucose dehydrogenase) with catalytic activities for L-fucose, D-arabinose, and L-galactose oxidation by NAD+. However, the evidence code is ECO:0000250 (inferred by similarity from human Q9BPX1), meaning this is a computational/similarity-based annotation rather than direct experimental characterization. The database annotation supports the key, but the underlying evidence is transferred by homology."
  },
  "important_caveats": [
    "The UniProt annotation for EC 1.1.1.122 is based on similarity inference (ECO:0000250) from human Q9BPX1, not direct experimental characterization of the mouse protein. The true substrate specificity of this mouse ortholog has not been independently confirmed by enzymatic assays.",
    "The distinction between EC 1.1.1.122 and 1.1.1.195 is at the subfamily level within the SDR superfamily. A model that recognizes SDR features but cannot resolve the specific subfamily would face genuine ambiguity between A and B.",
    "The reviewer-only evidence confirms the sequence matches E9Q3D4 (DHB14_MOUSE), but this accession and organism identity were not provided to the evaluated model. The model must rely on sequence-intrinsic features and transferable family knowledge.",
    "Both catalytic activities (L-fucose and D-arabinose/L-galactose oxidation) are annotated under the same EC 1.1.1.122, suggesting broad sugar specificity within this subfamily, which is consistent with the SDR family's known substrate promiscuity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A"
    ],
    "reason": "Both A (1.1.1.195) and B (1.1.1.122) are NAD-dependent sugar dehydrogenases within the broader SDR superfamily. Without confident subfamily-level recognition, a model could argue for either sugar dehydrogenase. The distinction between fucose dehydrogenase and gulonate dehydrogenase depends on specific substrate-binding pocket residues that are not trivially predictable from the sequence alone. However, the overall sequence architecture and the HSD17B14/retSDR subfamily signature provide a reasonable basis for preferring B, making A a weaker but not entirely indefensible alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E9Q3D4 (HSD17B14_MOUSE / DHB14_MOUSE) annotates EC 1.1.1.122 (L-fucose dehydrogenase) with catalytic activities for L-fucose, D-arabinose, and L-galactose oxidation by NAD+. However, the evidence code is ECO:0000250 (inferred by similarity from human Q9BPX1), meaning this is a computational/similarity-based annotation rather than direct experimental characterization. The database annotation supports the key, but the underlying evidence is transferred by homology.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmark short-chain dehydrogenase/reductase (SDR) family features: (1) a TGxxxGxG Rossmann-fold NAD-binding motif in 'VVVVTGGSRGIGAAIVRAF' (T-G-G-S-R-G-I-G matches TGxxxGxG), (2) a putative catalytic tetrad (Ser-Tyr-Lys-Asn) distributed across 'NCISPGNIW' (N, S) and 'GYGRKASKS' (Y, K), and (3) a ~273-aa length typical of SDR enzymes. These features unambiguously place the protein in the oxidoreductase class (EC 1.x.x.x), eliminating C (transferase, EC 2.3.1.319) and D (lyase, EC 4.1.1.128). Between A (1.1.1.195, L-gulonate dehydrogenase) and B (1.1.1.122, L-fucose dehydrogenase), both are NAD-dependent sugar dehydrogenases, but they belong to distinct SDR subfamilies. The sequence architecture—particularly the C-terminal 'TFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH' region and the specific arrangement of the catalytic residues—matches the HSD17B14/retSDR subfamily, a recognized SDR subfamily whose characterized members (e.g., human Q9BPX1) are annotated as L-fucose dehydrogenases. Knowledge of this subfamily's substrate preference, learned from the human homolog and other HSD17B14 orthologs, provides a transferable basis for selecting B over A. The gulonate dehydrogenase subfamily has a different sequence architecture and substrate-binding pocket configuration.",
    "missing_item_specific_fact": "",
    "reason": "The SDR family features (TGxxxGxG motif, catalytic tetrad, protein length) are directly readable from the sequence and eliminate C and D. The A-vs-B distinction rests on subfamily-level recognition: the sequence matches the HSD17B14/retSDR SDR subfamily, whose substrate preference (L-fucose dehydrogenase activity) is known from the human ortholog and other family members. This is transferable knowledge from related proteins, not a lookup of this exact entry's annotation. The inference is probabilistic rather than deterministic, but it meaningfully and credibly distinguishes B from A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A"],
    "reason": "Both A (1.1.1.195) and B (1.1.1.122) are NAD-dependent sugar dehydrogenases within the broader SDR superfamily. Without confident subfamily-level recognition, a model could argue for either sugar dehydrogenase. The distinction between fucose dehydrogenase and gulonate dehydrogenase depends on specific substrate-binding pocket residues that are not trivially predictable from the sequence alone. However, the overall sequence architecture and the HSD17B14/retSDR subfamily signature provide a reasonable basis for preferring B, making A a weaker but not entirely indefensible alternative."
  },
  "important_caveats": [
    "The UniProt annotation for EC 1.1.1.122 is based on similarity inference (ECO:0000250) from human Q9BPX1, not direct experimental characterization of the mouse protein. The true substrate specificity of this mouse ortholog has not been independently confirmed by enzymatic assays.",
    "The distinction between EC 1.1.1.122 and 1.1.1.195 is at the subfamily level within the SDR superfamily. A model that recognizes SDR features but cannot resolve the specific subfamily would face genuine ambiguity between A and B.",
    "The reviewer-only evidence confirms the sequence matches E9Q3D4 (DHB14_MOUSE), but this accession and organism identity were not provided to the evaluated model. The model must rely on sequence-intrinsic features and transferable family knowledge.",
    "Both catalytic activities (L-fucose and D-arabinose/L-galactose oxidation) are annotated under the same EC 1.1.1.122, suggesting broad sugar specificity within this subfamily, which is consistent with the SDR family's known substrate promiscuity."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81516\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"name\":\"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81515\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:2181\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:81457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"name\":\"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:46994\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194242\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"name\":\"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81523\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37619\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:182410\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
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
  "excerpt": "DE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;\nCC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;\nCC         Evidence={ECO:0000250|UniProtKB:Q9BPX1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81519, ChEBI:CHEBI:15378, ChEBI:CHEBI:46994,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:194242;\nCC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81523, ChEBI:CHEBI:15378, ChEBI:CHEBI:37619,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:182410;\nCC         EC=1.1.1.122; Evidence={ECO:0000250|UniProtKB:Q9BPX1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 92. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
