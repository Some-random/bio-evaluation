# GO_cellular_component_0099

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0099.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — cytosol

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSDMKAIHFGGGNIGRGFVAEFLHKSGYEVVFVDVMDAIINALQQNKSYTVTEVGTSETKSKTIDNYRAINSKTDEDKVVEEIATADIVTCAVGPNILKFIAPVIAKGIENRKKDSPIAVIACENAIGATDTLRKFIEEKLSDSTKSNIQDKARFANSAIDRIVPMQDENAGLNVKIEKFYEWCVESKPFLPSQPPKIEGVHFVEDLTPFIERKLFTVNTGHATAAYYGYNRGKECIHDVLQDKELNEIVRNTLKETAHLIVNKHEISEEDQNQYVEKIIKRISNPVLKDNVERVGRAPLRKLSRNERFIGPAAHLAEMGAKYDALLGGIEMCLRFQNVEGDDESFELAKILKENSSSDATEKITGLERNHTLFPAVEEVVKKVQA

[Multiple Choices]
A. actin cytoskeleton
B. cell leading edge
C. mitochondrial inner membrane
D. cytosol
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

> The sequence-matched UniProt record assigns cytosol (GO:0005829), but the annotation is computationally inferred by TreeGrafter rather than direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble metabolic dehydrogenase: it lacks an obvious N-terminal mitochondrial targeting peptide and has no long hydrophobic segment suggestive of a membrane anchor. Family-level knowledge that such enzymes are generally soluble supports cytosol over mitochondrial inner membrane, actin cytoskeleton, or cell leading edge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A credible sequence- and family-based inference distinguishes cytosol among these choices, although it does not establish localization experimentally or rule out every possible non-cytosolic pool.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, cytosol is the best-supported primary compartment.


### Important caveats

- The supplied location annotation is computational and should not be treated as experimental confirmation.
- The sequence-based inference supports a likely location, not an experimentally verified exclusive localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble metabolic dehydrogenase: it lacks an obvious N-terminal mitochondrial targeting peptide and has no long hydrophobic segment suggestive of a membrane anchor. Family-level knowledge that such enzymes are generally soluble supports cytosol over mitochondrial inner membrane, actin cytoskeleton, or cell leading edge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A credible sequence- and family-based inference distinguishes cytosol among these choices, although it does not establish localization experimentally or rule out every possible non-cytosolic pool."
  },
  "case_id": "GO_cellular_component_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns cytosol (GO:0005829), but the annotation is computationally inferred by TreeGrafter rather than direct experimental evidence."
  },
  "important_caveats": [
    "The supplied location annotation is computational and should not be treated as experimental confirmation.",
    "The sequence-based inference supports a likely location, not an experimentally verified exclusive localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, cytosol is the best-supported primary compartment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns cytosol (GO:0005829), but the annotation is computationally inferred by TreeGrafter rather than direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble metabolic dehydrogenase: it lacks an obvious N-terminal mitochondrial targeting peptide and has no long hydrophobic segment suggestive of a membrane anchor. Family-level knowledge that such enzymes are generally soluble supports cytosol over mitochondrial inner membrane, actin cytoskeleton, or cell leading edge.",
    "missing_item_specific_fact": "",
    "reason": "A credible sequence- and family-based inference distinguishes cytosol among these choices, although it does not establish localization experimentally or rule out every possible non-cytosolic pool."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, cytosol is the best-supported primary compartment."
  },
  "important_caveats": [
    "The supplied location annotation is computational and should not be treated as experimental confirmation.",
    "The sequence-based inference supports a likely location, not an experimentally verified exclusive localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17), a well-characterized enzyme in the cytosolic mannitol biosynthesis pathway. The UniProt GO annotation GO:0005829 (cytosol) is present, though with evidence code IEA:TreeGrafter (computational inference). However, the biology is well-established: mannitol-1-phosphate 5-dehydrogenase catalyzes the NAD+-dependent oxidation of mannitol-1-phosphate to fructose-6-phosphate in the cytosol across fungi, plants, and bacteria. The sequence contains a Rossmann-fold NAD(P)-binding motif (GGGNIGRGF) and lacks any mitochondrial targeting sequence, transmembrane domains, or signal peptides, consistent with a soluble cytosolic enzyme.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays a classic Rossmann-fold NAD(P)-binding motif (GGGNIGRGF at positions ~10-18), identifying it as a dehydrogenase. Critically, the N-terminus (MSDMKAIHFGGGNIGRGF...) lacks a mitochondrial targeting presequence (no amphipathic helix rich in Ser/Thr/Arg), no transmembrane hydrophobic stretches, and no ER signal peptide. Mannitol-1-phosphate 5-dehydrogenase is a well-known member of the mannitol biosynthesis pathway (fructose-6-phosphate → mannitol-1-phosphate → mannitol), which operates entirely in the cytosol in all characterized organisms. Option A (actin cytoskeleton) is excluded because the sequence has no actin-binding motifs or cytoskeletal protein features. Option B (cell leading edge) is irrelevant for a fungal cell and has no sequence basis. Option C (mitochondrial inner membrane) requires both a mitochondrial targeting sequence and transmembrane segments, neither of which is present. The combination of (1) family-level knowledge that mannitol-1-phosphate dehydrogenase is cytosolic, (2) the soluble Rossmann-fold architecture, and (3) absence of any organelle-targeting signals provides a concrete, transferable argument for cytosol over the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the Rossmann-fold NAD(P)-binding enzyme, recognize the mannitol-1-phosphate dehydrogenase family, recall that this enzyme functions in the cytosolic mannitol biosynthesis pathway, and note the absence of mitochondrial targeting sequences or transmembrane domains. This combination of family knowledge, pathway biology, and sequence-feature analysis meaningfully distinguishes cytosol from the other three options without requiring the specific database annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated. The actin cytoskeleton and cell leading edge are clearly inappropriate for a dehydrogenase enzyme. Mitochondrial inner membrane requires specific targeting signals and transmembrane segments absent from the sequence. Cytosol is the only compartment consistent with a soluble NAD(P)-dependent dehydrogenase lacking targeting signals.


### Important caveats

- The GO annotation is IEA:TreeGrafter (computational inference by homology), not experimental localization data. However, the cytosolic localization of mannitol-1-phosphate 5-dehydrogenase is well-supported by the biochemistry of the mannitol biosynthesis pathway across multiple organisms.
- The sequence is 386 amino acids, consistent with a soluble enzyme. No hydrophobic stretches suggestive of membrane insertion were identified.
- The organism is a fungus (Aureobasidium melanogenum); the 'cell leading edge' option is particularly inapplicable to fungal biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays a classic Rossmann-fold NAD(P)-binding motif (GGGNIGRGF at positions ~10-18), identifying it as a dehydrogenase. Critically, the N-terminus (MSDMKAIHFGGGNIGRGF...) lacks a mitochondrial targeting presequence (no amphipathic helix rich in Ser/Thr/Arg), no transmembrane hydrophobic stretches, and no ER signal peptide. Mannitol-1-phosphate 5-dehydrogenase is a well-known member of the mannitol biosynthesis pathway (fructose-6-phosphate → mannitol-1-phosphate → mannitol), which operates entirely in the cytosol in all characterized organisms. Option A (actin cytoskeleton) is excluded because the sequence has no actin-binding motifs or cytoskeletal protein features. Option B (cell leading edge) is irrelevant for a fungal cell and has no sequence basis. Option C (mitochondrial inner membrane) requires both a mitochondrial targeting sequence and transmembrane segments, neither of which is present. The combination of (1) family-level knowledge that mannitol-1-phosphate dehydrogenase is cytosolic, (2) the soluble Rossmann-fold architecture, and (3) absence of any organelle-targeting signals provides a concrete, transferable argument for cytosol over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann-fold NAD(P)-binding enzyme, recognize the mannitol-1-phosphate dehydrogenase family, recall that this enzyme functions in the cytosolic mannitol biosynthesis pathway, and note the absence of mitochondrial targeting sequences or transmembrane domains. This combination of family knowledge, pathway biology, and sequence-feature analysis meaningfully distinguishes cytosol from the other three options without requiring the specific database annotation for this exact protein."
  },
  "case_id": "GO_cellular_component_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The protein is Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17), a well-characterized enzyme in the cytosolic mannitol biosynthesis pathway. The UniProt GO annotation GO:0005829 (cytosol) is present, though with evidence code IEA:TreeGrafter (computational inference). However, the biology is well-established: mannitol-1-phosphate 5-dehydrogenase catalyzes the NAD+-dependent oxidation of mannitol-1-phosphate to fructose-6-phosphate in the cytosol across fungi, plants, and bacteria. The sequence contains a Rossmann-fold NAD(P)-binding motif (GGGNIGRGF) and lacks any mitochondrial targeting sequence, transmembrane domains, or signal peptides, consistent with a soluble cytosolic enzyme."
  },
  "important_caveats": [
    "The GO annotation is IEA:TreeGrafter (computational inference by homology), not experimental localization data. However, the cytosolic localization of mannitol-1-phosphate 5-dehydrogenase is well-supported by the biochemistry of the mannitol biosynthesis pathway across multiple organisms.",
    "The sequence is 386 amino acids, consistent with a soluble enzyme. No hydrophobic stretches suggestive of membrane insertion were identified.",
    "The organism is a fungus (Aureobasidium melanogenum); the 'cell leading edge' option is particularly inapplicable to fungal biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated. The actin cytoskeleton and cell leading edge are clearly inappropriate for a dehydrogenase enzyme. Mitochondrial inner membrane requires specific targeting signals and transmembrane segments absent from the sequence. Cytosol is the only compartment consistent with a soluble NAD(P)-dependent dehydrogenase lacking targeting signals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17), a well-characterized enzyme in the cytosolic mannitol biosynthesis pathway. The UniProt GO annotation GO:0005829 (cytosol) is present, though with evidence code IEA:TreeGrafter (computational inference). However, the biology is well-established: mannitol-1-phosphate 5-dehydrogenase catalyzes the NAD+-dependent oxidation of mannitol-1-phosphate to fructose-6-phosphate in the cytosol across fungi, plants, and bacteria. The sequence contains a Rossmann-fold NAD(P)-binding motif (GGGNIGRGF) and lacks any mitochondrial targeting sequence, transmembrane domains, or signal peptides, consistent with a soluble cytosolic enzyme.",
    "evidence_ids": ["C5", "C4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays a classic Rossmann-fold NAD(P)-binding motif (GGGNIGRGF at positions ~10-18), identifying it as a dehydrogenase. Critically, the N-terminus (MSDMKAIHFGGGNIGRGF...) lacks a mitochondrial targeting presequence (no amphipathic helix rich in Ser/Thr/Arg), no transmembrane hydrophobic stretches, and no ER signal peptide. Mannitol-1-phosphate 5-dehydrogenase is a well-known member of the mannitol biosynthesis pathway (fructose-6-phosphate → mannitol-1-phosphate → mannitol), which operates entirely in the cytosol in all characterized organisms. Option A (actin cytoskeleton) is excluded because the sequence has no actin-binding motifs or cytoskeletal protein features. Option B (cell leading edge) is irrelevant for a fungal cell and has no sequence basis. Option C (mitochondrial inner membrane) requires both a mitochondrial targeting sequence and transmembrane segments, neither of which is present. The combination of (1) family-level knowledge that mannitol-1-phosphate dehydrogenase is cytosolic, (2) the soluble Rossmann-fold architecture, and (3) absence of any organelle-targeting signals provides a concrete, transferable argument for cytosol over the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann-fold NAD(P)-binding enzyme, recognize the mannitol-1-phosphate dehydrogenase family, recall that this enzyme functions in the cytosolic mannitol biosynthesis pathway, and note the absence of mitochondrial targeting sequences or transmembrane domains. This combination of family knowledge, pathway biology, and sequence-feature analysis meaningfully distinguishes cytosol from the other three options without requiring the specific database annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated. The actin cytoskeleton and cell leading edge are clearly inappropriate for a dehydrogenase enzyme. Mitochondrial inner membrane requires specific targeting signals and transmembrane segments absent from the sequence. Cytosol is the only compartment consistent with a soluble NAD(P)-dependent dehydrogenase lacking targeting signals."
  },
  "important_caveats": [
    "The GO annotation is IEA:TreeGrafter (computational inference by homology), not experimental localization data. However, the cytosolic localization of mannitol-1-phosphate 5-dehydrogenase is well-supported by the biochemistry of the mannitol biosynthesis pathway across multiple organisms.",
    "The sequence is 386 amino acids, consistent with a soluble enzyme. No hydrophobic stretches suggestive of membrane insertion were identified.",
    "The organism is a fungus (Aureobasidium melanogenum); the 'cell leading edge' option is particularly inapplicable to fungal biology."
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
  "benchmark_sequence_length": 386,
  "benchmark_sequence_sha256": "0560835617463254f8bb4727e9aa3fdfd4d7e2ebec6b8a2c79e57b4d0f7ae518",
  "current_entry_audit": {
    "entryVersion": 16,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 386,
  "current_source_sequence_sha256": "0560835617463254f8bb4727e9aa3fdfd4d7e2ebec6b8a2c79e57b4d0f7ae518",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 15,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A223HDH4",
  "selected_historical_entry_version": 15,
  "selected_historical_record_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "selected_historical_source_sequence_length": 386,
  "selected_historical_source_sequence_sha256": "0560835617463254f8bb4727e9aa3fdfd4d7e2ebec6b8a2c79e57b4d0f7ae518",
  "selected_historical_version": {
    "accession": "A0A223HDH4",
    "database": "Swiss-Prot",
    "entryVersion": 15,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "MPDH_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A223HDH4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":16,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1A4\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.17\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"Mannitol-1-phosphate 5-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"MPDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005829\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosol\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H1",
  "excerpt": "ID   MPDH_AURME              Reviewed;         386 AA.\nAC   A0A223HDH4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 15.\nDE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=MPDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005829; C:cytosol; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
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

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0015629\nname: actin cytoskeleton\nnamespace: cellular_component\ndef: \"The part of the cytoskeleton (the internal framework of a cell) composed of actin and associated proteins. Includes actin cytoskeleton-associated complexes.\" [GOC:jl, ISBN:0395825172, ISBN:0815316194]\nis_a: GO:0005856 ! cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015629",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 119402-119408",
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
  "excerpt": "[Term]\nid: GO:0031252\nname: cell leading edge\nnamespace: cellular_component\ndef: \"The area of a motile cell closest to the direction of movement.\" [GOC:pg]\nsubset: goslim_pir\nsynonym: \"front of cell\" EXACT []\nsynonym: \"leading edge of cell\" EXACT []\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031252",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 174523-174532",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
