# GO_cellular_component_0128

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0128.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSHTSTPNHASAAPPRKWYDMTSAEFYVYVVAFMCGISMLMPINAVFSAPSYMLQYYLYATKDPNHVPQMTNFWSNVMTYYNLIGLVTGLVMEPLTLLKSFRKIPMLVRLLGGLCILIVEIIVLMAVPARGTTEGGAVATMCIAGFIGGLGKSIFESTVYGMFGAFPPSFTSIMMGGVGISGVLTSLIQIIVKAALPDTYEGVKKQSYIYYSLDVGIQAATFIALIMMRFNSFAQLHFGDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLVDREHSDDVDEHGDALRAVEGPTSNEILRATSIISVLRSIKWMFVSCAFVFVVTLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRVAPALRFMWPRSYNQRWIIVAASFARVIFVPLLLLYSYHYIPSEAYGYVIMVIFGFSSGYVASMSLTLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIREKY

[Multiple Choices]
A. plasma membrane
B. egg coat
C. endocytic vesicle
D. nucleoplasm
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

> The sequence matches the reviewed record, whose GO annotation assigns plasma membrane with IEA:TreeGrafter evidence; the record also predicts a multipass membrane protein. This supports the key, though it is computational annotation rather than direct experimental localization evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has many hydrophobic transmembrane segments and a pattern consistent with a multipass transporter, plausibly an equilibrative nucleoside-transporter-family protein. Transferable knowledge that such transporters commonly function at the cell surface makes plasma membrane a meaningful choice over egg coat or nucleoplasm, and more likely than an endocytic vesicle as the primary location.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The strong multipass-transporter signal and family-level localization tendency offer a credible distinction among these choices without requiring the target's exact database annotation. The sequence alone does not prove plasma-membrane localization, and vesicular localization is not impossible.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives are sufficiently distinguished by the multipass transporter features and the usual cell-surface localization of this transporter class; no second option is equally supported as the primary location.


### Important caveats

- The supplied localization evidence is computational (IEA:TreeGrafter and a multipass-membrane prediction), not direct experimental proof.
- The exact source snapshot used by the author is unknown, although the matching sequence and historical record support applicability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many hydrophobic transmembrane segments and a pattern consistent with a multipass transporter, plausibly an equilibrative nucleoside-transporter-family protein. Transferable knowledge that such transporters commonly function at the cell surface makes plasma membrane a meaningful choice over egg coat or nucleoplasm, and more likely than an endocytic vesicle as the primary location.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The strong multipass-transporter signal and family-level localization tendency offer a credible distinction among these choices without requiring the target's exact database annotation. The sequence alone does not prove plasma-membrane localization, and vesicular localization is not impossible."
  },
  "case_id": "GO_cellular_component_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the reviewed record, whose GO annotation assigns plasma membrane with IEA:TreeGrafter evidence; the record also predicts a multipass membrane protein. This supports the key, though it is computational annotation rather than direct experimental localization evidence."
  },
  "important_caveats": [
    "The supplied localization evidence is computational (IEA:TreeGrafter and a multipass-membrane prediction), not direct experimental proof.",
    "The exact source snapshot used by the author is unknown, although the matching sequence and historical record support applicability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are sufficiently distinguished by the multipass transporter features and the usual cell-surface localization of this transporter class; no second option is equally supported as the primary location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the reviewed record, whose GO annotation assigns plasma membrane with IEA:TreeGrafter evidence; the record also predicts a multipass membrane protein. This supports the key, though it is computational annotation rather than direct experimental localization evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has many hydrophobic transmembrane segments and a pattern consistent with a multipass transporter, plausibly an equilibrative nucleoside-transporter-family protein. Transferable knowledge that such transporters commonly function at the cell surface makes plasma membrane a meaningful choice over egg coat or nucleoplasm, and more likely than an endocytic vesicle as the primary location.",
    "missing_item_specific_fact": "",
    "reason": "The strong multipass-transporter signal and family-level localization tendency offer a credible distinction among these choices without requiring the target's exact database annotation. The sequence alone does not prove plasma-membrane localization, and vesicular localization is not impossible."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are sufficiently distinguished by the multipass transporter features and the usual cell-surface localization of this transporter class; no second option is equally supported as the primary location."
  },
  "important_caveats": [
    "The supplied localization evidence is computational (IEA:TreeGrafter and a multipass-membrane prediction), not direct experimental proof.",
    "The exact source snapshot used by the author is unknown, although the matching sequence and historical record support applicability."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The GO annotation for this protein (J9UD11, CfAT1) is GO:0005886 (plasma membrane) with IEA:TreeGrafter evidence. UniProt also annotates it as 'Membrane; Multi-pass membrane protein' (ECO:0000255, computational). The protein is an equilibrative nucleoside transporter (ENT family), a well-characterized class of plasma membrane transporters. The sequence shows extensive hydrophobic stretches consistent with ~11 TM segments, matching the ENT topology. While the GO evidence is computational (IEA), the protein family assignment and the functional characterization (high-affinity equilibrative nucleoside transport) strongly support plasma membrane as the primary location.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays numerous long hydrophobic stretches (at least 10-11 TM segments) characteristic of a multi-pass membrane transporter. Nucleoplasm (D) is excluded: no nuclear localization signal is present, and extensive TM helices are incompatible with a soluble nuclear protein. Egg coat (B) is excluded: egg coat proteins are secreted extracellular matrix components (zona pellucida/vitelline membrane) in animals; a multi-pass membrane protein with no signal peptide for secretion is incompatible with this location. The key distinction is between plasma membrane (A) and endocytic vesicle (C). The multi-pass topology with ~11 TM segments matches the equilibrative nucleoside transporter (ENT) family, which is a well-defined family of plasma membrane proteins (hENT1-4, etc.) whose defining function is bidirectional nucleoside transport across the cell surface. ENT transporters are not vesicle-trafficking proteins; they lack endocytic sorting motifs (dileucine, tyrosine-based) and are not classified as vesicular cargo. Family-level knowledge that ENT transporters reside in the plasma membrane meaningfully distinguishes A from C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence's multi-pass TM architecture, absence of NLS, absence of secretion signal, and resemblance to the ENT transporter family (a well-known plasma membrane protein family) allow a knowledgeable model to select plasma membrane over the other three options using transferable family and topology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-distinguished: nucleoplasm requires a soluble protein with NLS, egg coat requires a secreted extracellular matrix protein, and endocytic vesicle would require vesicle-trafficking features. The multi-pass membrane transporter topology and ENT-family resemblance clearly point to plasma membrane as the primary location.


### Important caveats

- The GO plasma membrane annotation carries IEA:TreeGrafter evidence (computational phylogenetic propagation), not direct experimental localization. However, the ENT family is universally characterized as plasma membrane proteins.
- The UniProt subcellular location annotation (Membrane; Multi-pass membrane protein) is also computational (ECO:0000255).
- The organism is Crithidia fasciculata (a trypanosomatid), which is not an animal with eggs, further ruling out egg coat, but this organism identity was not given to the model.
- The sequence's TM count and topology pattern are consistent with ENT transporters but were not explicitly labeled in the input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays numerous long hydrophobic stretches (at least 10-11 TM segments) characteristic of a multi-pass membrane transporter. Nucleoplasm (D) is excluded: no nuclear localization signal is present, and extensive TM helices are incompatible with a soluble nuclear protein. Egg coat (B) is excluded: egg coat proteins are secreted extracellular matrix components (zona pellucida/vitelline membrane) in animals; a multi-pass membrane protein with no signal peptide for secretion is incompatible with this location. The key distinction is between plasma membrane (A) and endocytic vesicle (C). The multi-pass topology with ~11 TM segments matches the equilibrative nucleoside transporter (ENT) family, which is a well-defined family of plasma membrane proteins (hENT1-4, etc.) whose defining function is bidirectional nucleoside transport across the cell surface. ENT transporters are not vesicle-trafficking proteins; they lack endocytic sorting motifs (dileucine, tyrosine-based) and are not classified as vesicular cargo. Family-level knowledge that ENT transporters reside in the plasma membrane meaningfully distinguishes A from C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence's multi-pass TM architecture, absence of NLS, absence of secretion signal, and resemblance to the ENT transporter family (a well-known plasma membrane protein family) allow a knowledgeable model to select plasma membrane over the other three options using transferable family and topology knowledge."
  },
  "case_id": "GO_cellular_component_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The GO annotation for this protein (J9UD11, CfAT1) is GO:0005886 (plasma membrane) with IEA:TreeGrafter evidence. UniProt also annotates it as 'Membrane; Multi-pass membrane protein' (ECO:0000255, computational). The protein is an equilibrative nucleoside transporter (ENT family), a well-characterized class of plasma membrane transporters. The sequence shows extensive hydrophobic stretches consistent with ~11 TM segments, matching the ENT topology. While the GO evidence is computational (IEA), the protein family assignment and the functional characterization (high-affinity equilibrative nucleoside transport) strongly support plasma membrane as the primary location."
  },
  "important_caveats": [
    "The GO plasma membrane annotation carries IEA:TreeGrafter evidence (computational phylogenetic propagation), not direct experimental localization. However, the ENT family is universally characterized as plasma membrane proteins.",
    "The UniProt subcellular location annotation (Membrane; Multi-pass membrane protein) is also computational (ECO:0000255).",
    "The organism is Crithidia fasciculata (a trypanosomatid), which is not an animal with eggs, further ruling out egg coat, but this organism identity was not given to the model.",
    "The sequence's TM count and topology pattern are consistent with ENT transporters but were not explicitly labeled in the input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-distinguished: nucleoplasm requires a soluble protein with NLS, egg coat requires a secreted extracellular matrix protein, and endocytic vesicle would require vesicle-trafficking features. The multi-pass membrane transporter topology and ENT-family resemblance clearly point to plasma membrane as the primary location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The GO annotation for this protein (J9UD11, CfAT1) is GO:0005886 (plasma membrane) with IEA:TreeGrafter evidence. UniProt also annotates it as 'Membrane; Multi-pass membrane protein' (ECO:0000255, computational). The protein is an equilibrative nucleoside transporter (ENT family), a well-characterized class of plasma membrane transporters. The sequence shows extensive hydrophobic stretches consistent with ~11 TM segments, matching the ENT topology. While the GO evidence is computational (IEA), the protein family assignment and the functional characterization (high-affinity equilibrative nucleoside transport) strongly support plasma membrane as the primary location.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays numerous long hydrophobic stretches (at least 10-11 TM segments) characteristic of a multi-pass membrane transporter. Nucleoplasm (D) is excluded: no nuclear localization signal is present, and extensive TM helices are incompatible with a soluble nuclear protein. Egg coat (B) is excluded: egg coat proteins are secreted extracellular matrix components (zona pellucida/vitelline membrane) in animals; a multi-pass membrane protein with no signal peptide for secretion is incompatible with this location. The key distinction is between plasma membrane (A) and endocytic vesicle (C). The multi-pass topology with ~11 TM segments matches the equilibrative nucleoside transporter (ENT) family, which is a well-defined family of plasma membrane proteins (hENT1-4, etc.) whose defining function is bidirectional nucleoside transport across the cell surface. ENT transporters are not vesicle-trafficking proteins; they lack endocytic sorting motifs (dileucine, tyrosine-based) and are not classified as vesicular cargo. Family-level knowledge that ENT transporters reside in the plasma membrane meaningfully distinguishes A from C.",
    "missing_item_specific_fact": "",
    "reason": "The sequence's multi-pass TM architecture, absence of NLS, absence of secretion signal, and resemblance to the ENT transporter family (a well-known plasma membrane protein family) allow a knowledgeable model to select plasma membrane over the other three options using transferable family and topology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-distinguished: nucleoplasm requires a soluble protein with NLS, egg coat requires a secreted extracellular matrix protein, and endocytic vesicle would require vesicle-trafficking features. The multi-pass membrane transporter topology and ENT-family resemblance clearly point to plasma membrane as the primary location."
  },
  "important_caveats": [
    "The GO plasma membrane annotation carries IEA:TreeGrafter evidence (computational phylogenetic propagation), not direct experimental localization. However, the ENT family is universally characterized as plasma membrane proteins.",
    "The UniProt subcellular location annotation (Membrane; Multi-pass membrane protein) is also computational (ECO:0000255).",
    "The organism is Crithidia fasciculata (a trypanosomatid), which is not an animal with eggs, further ruling out egg coat, but this organism identity was not given to the model.",
    "The sequence's TM count and topology pattern are consistent with ENT transporters but were not explicitly labeled in the input."
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
  "benchmark_sequence_length": 496,
  "benchmark_sequence_sha256": "7c36d5c7fae62fcbb8bf70a0ab3d89954fbfbbc6fd19a54c7c3dda630ce5c242",
  "current_entry_audit": {
    "entryVersion": 26,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 496,
  "current_source_sequence_sha256": "7c36d5c7fae62fcbb8bf70a0ab3d89954fbfbbc6fd19a54c7c3dda630ce5c242",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9UD11",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "selected_historical_source_sequence_length": 496,
  "selected_historical_source_sequence_sha256": "7c36d5c7fae62fcbb8bf70a0ab3d89954fbfbbc6fd19a54c7c3dda630ce5c242",
  "selected_historical_version": {
    "accession": "J9UD11",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AT1_CRIFA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9UD11\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":26,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR68832.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Crithidia\"],\"scientificName\":\"Crithidia fasciculata\",\"taxonId\":5656}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"value\":\"Adenosine transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"value\":\"CfAT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-0162\",\"value\":\"Membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24120444\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2013.09.007\"}],\"citationType\":\"journal article\",\"firstPage\":\"75\",\"id\":\"24120444\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"79\",\"publicationDate\":\"2013\",\"title\":\"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-affinity equilibrative nucleoside transporter specific for adenosine.\",\"volume\":\"191\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR68832.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR68833.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF LYS-153\",\"VARIANTS MET-433 AND VAL-481\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:28:53.178363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c",
  "url": "https://rest.uniprot.org/uniprotkb/J9UD11.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   AT1_CRIFA               Reviewed;         496 AA.\nAC   J9UD11; J9U6P1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Adenosine transporter 1 {ECO:0000303|PubMed:24120444};\nDE            Short=CfAT1 {ECO:0000303|PubMed:24120444};\nGN   Name=AT1 {ECO:0000312|EMBL:AFR68832.1};\nGN   Synonyms=AT1.2 {ECO:0000312|EMBL:AFR68833.1};\nOS   Crithidia fasciculata.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Crithidia.\nOX   NCBI_TaxID=5656 {ECO:0000312|EMBL:AFR68832.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AFR68832.1, ECO:0000312|EMBL:AFR68833.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, TRANSPORTER ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, MUTAGENESIS OF LYS-153, AND VARIANTS MET-433\nRP   AND VAL-481.\nRX   PubMed=24120444; DOI=10.1016/j.molbiopara.2013.09.007;\nRA   Arendt C.S.;\nRT   \"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-\nRT   affinity equilibrative nucleoside transporter specific for adenosine.\";\nRL   Mol. Biochem. Parasitol. 191:75-79(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Multi-pass membrane\nCC       protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.181587+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6",
  "url": "https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005654\nname: nucleoplasm\nnamespace: cellular_component\ndef: \"That part of the nuclear content other than the chromosomes or the nucleolus.\" [GOC:ma, ISBN:0124325653]\nsubset: goslim_chembl\nsubset: goslim_generic\nsubset: goslim_plant\nxref: NIF_Subcellular:sao661522542\nxref: Wikipedia:Nucleoplasm\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0031981 ! nuclear lumen\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005654",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58222-58234",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0030139\nname: endocytic vesicle\nnamespace: cellular_component\ndef: \"A membrane-bounded intracellular vesicle formed by invagination of the plasma membrane around an extracellular substance. Endocytic vesicles fuse with early endosomes to deliver the cargo for further sorting.\" [GOC:curators, PMID:19696797]\nsynonym: \"endocytotic transport vesicle\" EXACT []\nsynonym: \"endocytotic vesicle\" EXACT []\nxref: NIF_Subcellular:sao1362520468\nis_a: GO:0031410 ! cytoplasmic vesicle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030139",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 163117-163126",
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
  "excerpt": "[Term]\nid: GO:0035805\nname: egg coat\nnamespace: cellular_component\ndef: \"A specialized extracellular matrix that surrounds the plasma membrane of the ovum of animals. The egg coat provides structural support and can play an essential role in oogenesis, fertilization and early development.\" [PMID:16944418, PMID:17163408]\nsynonym: \"vitelline membrane\" NARROW [PMID:16944418, PMID:17163408]\nsynonym: \"zona pellucida\" NARROW [PMID:16944418, PMID:17163408]\nis_a: GO:0140047 ! specialized extracellular matrix\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035805",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 221420-221428",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
