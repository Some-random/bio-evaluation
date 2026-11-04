# pathway_0141

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0141.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSYKAFLITLAAVTRVLTYPANSSFELVDRSGTPSSTGTSGGYYYSFWTDGGADVTYTNGAGGEYKLQWSGNGNLVGGKGWNPGSAKAVTYSGTYSPNGNSYLSLYGWTTSPLIEYYVVENFGTYDPSTGATLKGTVVSDGATYKIYQTQRVNQPSIIGTATFYQYWSVRQTKRTGGTVTTGNHFNAWKALGMNMGTFDYMIVATEGYFSSGSSDITVGSSTGGGDSGSPTSAPTTSPTTSPGGTCGALYSQCGGTGFTGSQCCASGTCKYANSYYSQCL

[Multiple Choices]
A. Glycan degradation
B. LPS O-antigen biosynthesis. .
C. Pyrimidine metabolism
D. NAD(+) from nicotinamide D-ribonucleotide: step 1/1. .
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

> The sequence-matched record identifies the protein as an endo-1,4-beta-xylanase (EC 3.2.1.8) and assigns it to glycan degradation, specifically xylan degradation. This supports choice A. The pathway assignment is attributed to a PROSITE rule, so it is computational annotation rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a secreted protein, and the sequence is consistent with a fungal glycoside hydrolase such as a xylanase. Transferable knowledge that secreted xylanases hydrolyze xylan, a plant cell-wall glycan, supports glycan degradation. That distinguishes A from LPS O-antigen biosynthesis, which is associated with bacterial surface-polysaccharide synthesis, and from the intracellular nucleotide and NAD metabolic alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the secretion-enzyme pattern offer a credible inference among these choices; the exact target's database annotation is not necessary to distinguish the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct pathways, and the sequence supports a secreted glycan-degrading enzyme rather than the listed biosynthetic or nucleotide-metabolism alternatives.


### Important caveats

- The reviewer-only pathway annotation is attributed to a PROSITE rule; the excerpts do not independently establish experimental validation of this protein's pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secreted protein, and the sequence is consistent with a fungal glycoside hydrolase such as a xylanase. Transferable knowledge that secreted xylanases hydrolyze xylan, a plant cell-wall glycan, supports glycan degradation. That distinguishes A from LPS O-antigen biosynthesis, which is associated with bacterial surface-polysaccharide synthesis, and from the intracellular nucleotide and NAD metabolic alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the secretion-enzyme pattern offer a credible inference among these choices; the exact target's database annotation is not necessary to distinguish the answer."
  },
  "case_id": "pathway_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as an endo-1,4-beta-xylanase (EC 3.2.1.8) and assigns it to glycan degradation, specifically xylan degradation. This supports choice A. The pathway assignment is attributed to a PROSITE rule, so it is computational annotation rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only pathway annotation is attributed to a PROSITE rule; the excerpts do not independently establish experimental validation of this protein's pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct pathways, and the sequence supports a secreted glycan-degrading enzyme rather than the listed biosynthetic or nucleotide-metabolism alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as an endo-1,4-beta-xylanase (EC 3.2.1.8) and assigns it to glycan degradation, specifically xylan degradation. This supports choice A. The pathway assignment is attributed to a PROSITE rule, so it is computational annotation rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secreted protein, and the sequence is consistent with a fungal glycoside hydrolase such as a xylanase. Transferable knowledge that secreted xylanases hydrolyze xylan, a plant cell-wall glycan, supports glycan degradation. That distinguishes A from LPS O-antigen biosynthesis, which is associated with bacterial surface-polysaccharide synthesis, and from the intracellular nucleotide and NAD metabolic alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the secretion-enzyme pattern offer a credible inference among these choices; the exact target's database annotation is not necessary to distinguish the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct pathways, and the sequence supports a secreted glycan-degrading enzyme rather than the listed biosynthetic or nucleotide-metabolism alternatives."
  },
  "important_caveats": [
    "The reviewer-only pathway annotation is attributed to a PROSITE rule; the excerpts do not independently establish experimental validation of this protein's pathway assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation assigns EC 3.2.1.8 (Endo-1,4-beta-xylanase) and pathway 'Glycan degradation; xylan degradation' based on PROSITE-ProRule PRU01097 (sequence-motif-based inference). Xylan is a glycan (polysaccharide), and its enzymatic degradation by a glycoside hydrolase falls squarely under 'Glycan degradation.' The EC assignment is computational (ECO:0000255) rather than experimentally verified for this exact protein, but the GH10 family motifs are genuinely present in the sequence and the EC-to-pathway mapping is standard.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal catalytic domain contains hallmark motifs of Glycoside Hydrolase Family 10 (GH10) xylanases: 'WTDGG' (TIM-barrel catalytic region), 'WSGNG' (substrate-binding loop), 'YVVENFG' (catalytic acid/base NEFG motif), and 'YQYWS' (conserved GH10 signature). A model trained on protein families recognizes these as diagnostic of GH10 xylanases, which hydrolyze xylan—a β-1,4-linked xylose polysaccharide (a glycan). This directly maps to 'Glycan degradation.' The N-terminal hydrophobic stretch (MVSYKAFLITLAAVTRVLT) is a signal peptide indicating a secreted extracellular enzyme, consistent with a fungal cell-wall-degrading glycosidase. The C-terminal Ser/Thr-rich linker with cysteines is a common extension in fungal GH10 enzymes. Against the distractors: (B) LPS O-antigen biosynthesis is a Gram-negative bacterial pathway involving glycosyltransferases and ABC transporters, not secreted hydrolases; (C) Pyrimidine metabolism involves entirely different enzyme classes (dihydroorotase, carbamoyltransferase, dihydrofolate reductase) with no resemblance to this sequence; (D) NAD(+) synthesis from NMN involves NAD synthetase (EC 6.3.1.5) with an ATP-binding/adenylyltransferase fold, absent here. The GH10 motif recognition plus the secreted-enzyme context meaningfully and specifically selects option A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH10 xylanase family motifs (WTDGG, WSGNG, NEFG, YQYWS) are among the most well-characterized sequence signatures in glycoside hydrolase biochemistry. Recognizing them from the raw sequence and connecting xylan hydrolysis to 'Glycan degradation' is a standard family-level inference learned across many GH10 proteins. The distractors belong to unrelated enzyme superfamilies and organismal contexts, making them distinguishable without memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span clearly distinct biochemical categories (glycan hydrolase, bacterial LPS biosynthesis, nucleotide metabolism, cofactor biosynthesis). The GH10 motifs unambiguously point to glycan degradation and exclude the others.


### Important caveats

- The EC 3.2.1.8 assignment is computational (PROSITE-ProRule motif match, ECO:0000255), not experimentally validated for this exact protein; the cited PubMed reference discusses EIX-like protein perception by plant receptors, not direct xylanase assay.
- The 'ethylene-inducing' name reflects a moonlighting signaling role in plant-pathogen interaction; the primary enzymatic classification remains xylan degradation.
- The reviewer-only evidence confirms sequence match to UniProt A0A384JXV5 but this accession was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal catalytic domain contains hallmark motifs of Glycoside Hydrolase Family 10 (GH10) xylanases: 'WTDGG' (TIM-barrel catalytic region), 'WSGNG' (substrate-binding loop), 'YVVENFG' (catalytic acid/base NEFG motif), and 'YQYWS' (conserved GH10 signature). A model trained on protein families recognizes these as diagnostic of GH10 xylanases, which hydrolyze xylan—a β-1,4-linked xylose polysaccharide (a glycan). This directly maps to 'Glycan degradation.' The N-terminal hydrophobic stretch (MVSYKAFLITLAAVTRVLT) is a signal peptide indicating a secreted extracellular enzyme, consistent with a fungal cell-wall-degrading glycosidase. The C-terminal Ser/Thr-rich linker with cysteines is a common extension in fungal GH10 enzymes. Against the distractors: (B) LPS O-antigen biosynthesis is a Gram-negative bacterial pathway involving glycosyltransferases and ABC transporters, not secreted hydrolases; (C) Pyrimidine metabolism involves entirely different enzyme classes (dihydroorotase, carbamoyltransferase, dihydrofolate reductase) with no resemblance to this sequence; (D) NAD(+) synthesis from NMN involves NAD synthetase (EC 6.3.1.5) with an ATP-binding/adenylyltransferase fold, absent here. The GH10 motif recognition plus the secreted-enzyme context meaningfully and specifically selects option A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH10 xylanase family motifs (WTDGG, WSGNG, NEFG, YQYWS) are among the most well-characterized sequence signatures in glycoside hydrolase biochemistry. Recognizing them from the raw sequence and connecting xylan hydrolysis to 'Glycan degradation' is a standard family-level inference learned across many GH10 proteins. The distractors belong to unrelated enzyme superfamilies and organismal contexts, making them distinguishable without memorizing this specific protein's database entry."
  },
  "case_id": "pathway_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation assigns EC 3.2.1.8 (Endo-1,4-beta-xylanase) and pathway 'Glycan degradation; xylan degradation' based on PROSITE-ProRule PRU01097 (sequence-motif-based inference). Xylan is a glycan (polysaccharide), and its enzymatic degradation by a glycoside hydrolase falls squarely under 'Glycan degradation.' The EC assignment is computational (ECO:0000255) rather than experimentally verified for this exact protein, but the GH10 family motifs are genuinely present in the sequence and the EC-to-pathway mapping is standard."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment is computational (PROSITE-ProRule motif match, ECO:0000255), not experimentally validated for this exact protein; the cited PubMed reference discusses EIX-like protein perception by plant receptors, not direct xylanase assay.",
    "The 'ethylene-inducing' name reflects a moonlighting signaling role in plant-pathogen interaction; the primary enzymatic classification remains xylan degradation.",
    "The reviewer-only evidence confirms sequence match to UniProt A0A384JXV5 but this accession was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span clearly distinct biochemical categories (glycan hydrolase, bacterial LPS biosynthesis, nucleotide metabolism, cofactor biosynthesis). The GH10 motifs unambiguously point to glycan degradation and exclude the others."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation assigns EC 3.2.1.8 (Endo-1,4-beta-xylanase) and pathway 'Glycan degradation; xylan degradation' based on PROSITE-ProRule PRU01097 (sequence-motif-based inference). Xylan is a glycan (polysaccharide), and its enzymatic degradation by a glycoside hydrolase falls squarely under 'Glycan degradation.' The EC assignment is computational (ECO:0000255) rather than experimentally verified for this exact protein, but the GH10 family motifs are genuinely present in the sequence and the EC-to-pathway mapping is standard.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal catalytic domain contains hallmark motifs of Glycoside Hydrolase Family 10 (GH10) xylanases: 'WTDGG' (TIM-barrel catalytic region), 'WSGNG' (substrate-binding loop), 'YVVENFG' (catalytic acid/base NEFG motif), and 'YQYWS' (conserved GH10 signature). A model trained on protein families recognizes these as diagnostic of GH10 xylanases, which hydrolyze xylan—a β-1,4-linked xylose polysaccharide (a glycan). This directly maps to 'Glycan degradation.' The N-terminal hydrophobic stretch (MVSYKAFLITLAAVTRVLT) is a signal peptide indicating a secreted extracellular enzyme, consistent with a fungal cell-wall-degrading glycosidase. The C-terminal Ser/Thr-rich linker with cysteines is a common extension in fungal GH10 enzymes. Against the distractors: (B) LPS O-antigen biosynthesis is a Gram-negative bacterial pathway involving glycosyltransferases and ABC transporters, not secreted hydrolases; (C) Pyrimidine metabolism involves entirely different enzyme classes (dihydroorotase, carbamoyltransferase, dihydrofolate reductase) with no resemblance to this sequence; (D) NAD(+) synthesis from NMN involves NAD synthetase (EC 6.3.1.5) with an ATP-binding/adenylyltransferase fold, absent here. The GH10 motif recognition plus the secreted-enzyme context meaningfully and specifically selects option A.",
    "missing_item_specific_fact": "",
    "reason": "The GH10 xylanase family motifs (WTDGG, WSGNG, NEFG, YQYWS) are among the most well-characterized sequence signatures in glycoside hydrolase biochemistry. Recognizing them from the raw sequence and connecting xylan hydrolysis to 'Glycan degradation' is a standard family-level inference learned across many GH10 proteins. The distractors belong to unrelated enzyme superfamilies and organismal contexts, making them distinguishable without memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span clearly distinct biochemical categories (glycan hydrolase, bacterial LPS biosynthesis, nucleotide metabolism, cofactor biosynthesis). The GH10 motifs unambiguously point to glycan degradation and exclude the others."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment is computational (PROSITE-ProRule motif match, ECO:0000255), not experimentally validated for this exact protein; the cited PubMed reference discusses EIX-like protein perception by plant receptors, not direct xylanase assay.",
    "The 'ethylene-inducing' name reflects a moonlighting signaling role in plant-pathogen interaction; the primary enzymatic classification remains xylan degradation.",
    "The reviewer-only evidence confirms sequence match to UniProt A0A384JXV5 but this accession was not available to the evaluated model."
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
  "benchmark_sequence_length": 281,
  "benchmark_sequence_sha256": "01bc2397489efa344f606d78b71821f92a88f6b9264a6c8ef38136aff7712472",
  "current_entry_audit": {
    "entryVersion": 27,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 281,
  "current_source_sequence_sha256": "01bc2397489efa344f606d78b71821f92a88f6b9264a6c8ef38136aff7712472",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 25,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384JXV5",
  "selected_historical_entry_version": 25,
  "selected_historical_record_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "selected_historical_source_sequence_length": 281,
  "selected_historical_source_sequence_sha256": "01bc2397489efa344f606d78b71821f92a88f6b9264a6c8ef38136aff7712472",
  "selected_historical_version": {
    "accession": "A0A384JXV5",
    "database": "Swiss-Prot",
    "entryVersion": 25,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX1_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384JXV5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":27,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX1\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Glycan degradation; xylan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:58.123065+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384JXV5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H1",
  "excerpt": "ID   EIX1_BOTFB              Reviewed;         281 AA.\nAC   A0A384JXV5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 25.\nDE   RecName: Full=Ethylene-inducing xylanase 1 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX1 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX1 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX1 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_12g00090;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "url": "https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "url": "https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-\nCC       ProRule:PRU01097}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:00.003931+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef",
  "url": "https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
