# GO_cellular_component_0066

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0066.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — cytoplasm

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGVEEADKLKQLGNAAFSERKWHLAIDMYTKAIELTKTPTLFCNRALAELRAELPGAALADADAALGIEPTFAKAYYHKASAYLSLGKHKQALTNYKKVVDLAPQNSDAQAKVEFCKKEIRRINFENAIMTPDEAPLSQTIKLGSVRADYDGPRIENETVTVEFVEAMKEHFRLEKLIDRHDVIFILLEVQKILKKCPNFVSINVPVGEEITVCGDTHGQYYDLLNIFKLNGNPLETNRYLFNGDFVDRGSYSFENIMTLFAYKVLYPDHFFLSRGNHEGVSMNRMYGFEGEVTQKYNSEMFRLFTEVFNSLPIGHIINNEVFVVHGGLYSSDKVTLDDLQHPNRFRDIPESGLICESLWSDPQPMPGRAPSKRGVSCLSFGPDVTETFLNNNNLKLLVRSHEVKDEGYEIEHGGKCITVFSAPNYCDQMGNKGAFIRFTGGDMKPRFTTFTHVPHPGKRPMHYATGFGLF

[Multiple Choices]
A. transcription factor TFIID complex
B. mitochondrial matrix
C. SAGA complex
D. cytoplasm
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

> The sequence-matched annotation reports that the protein is predominantly in the cytosol, with some nuclear presence; the cytoplasm choice is therefore supported as its primary location. The cited localization is experimental rather than merely computational.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal TPR-rich region followed by a conserved serine/threonine phosphatase catalytic domain, a pattern transferable to soluble PP5-family phosphatases. Such a soluble enzyme, without an evident N-terminal mitochondrial targeting peptide, is a better fit for cytoplasm than mitochondrial matrix; the sequence also does not suggest a TFIID or SAGA complex subunit.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family and sequence features provide a credible distinction among these options without requiring the exact protein's localization annotation. They support cytoplasm probabilistically, though they do not independently establish the protein's observed cytosolic predominance.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein may also occur in the nucleus, but that is not one of the offered choices; the evidence identifies cytosol as the predominant location.


### Important caveats

- The localization evidence is specific to the sequence-matched protein and should not be confused with the family-level inference available from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal TPR-rich region followed by a conserved serine/threonine phosphatase catalytic domain, a pattern transferable to soluble PP5-family phosphatases. Such a soluble enzyme, without an evident N-terminal mitochondrial targeting peptide, is a better fit for cytoplasm than mitochondrial matrix; the sequence also does not suggest a TFIID or SAGA complex subunit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family and sequence features provide a credible distinction among these options without requiring the exact protein's localization annotation. They support cytoplasm probabilistically, though they do not independently establish the protein's observed cytosolic predominance."
  },
  "case_id": "GO_cellular_component_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched annotation reports that the protein is predominantly in the cytosol, with some nuclear presence; the cytoplasm choice is therefore supported as its primary location. The cited localization is experimental rather than merely computational."
  },
  "important_caveats": [
    "The localization evidence is specific to the sequence-matched protein and should not be confused with the family-level inference available from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may also occur in the nucleus, but that is not one of the offered choices; the evidence identifies cytosol as the predominant location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched annotation reports that the protein is predominantly in the cytosol, with some nuclear presence; the cytoplasm choice is therefore supported as its primary location. The cited localization is experimental rather than merely computational.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal TPR-rich region followed by a conserved serine/threonine phosphatase catalytic domain, a pattern transferable to soluble PP5-family phosphatases. Such a soluble enzyme, without an evident N-terminal mitochondrial targeting peptide, is a better fit for cytoplasm than mitochondrial matrix; the sequence also does not suggest a TFIID or SAGA complex subunit.",
    "missing_item_specific_fact": "",
    "reason": "Family and sequence features provide a credible distinction among these options without requiring the exact protein's localization annotation. They support cytoplasm probabilistically, though they do not independently establish the protein's observed cytosolic predominance."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may also occur in the nucleus, but that is not one of the offered choices; the evidence identifies cytosol as the predominant location."
  },
  "important_caveats": [
    "The localization evidence is specific to the sequence-matched protein and should not be confused with the family-level inference available from the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q388N2, PPP5_TRYB2) annotates this protein as 'Predominantly present in the cytosol and localizes densely to the area near the nucleus' with experimental evidence (ECO:0000269, PubMed:11290414). GO:0005737 (cytoplasm) is annotated with IDA evidence. While GO:0005634 (nucleus) is also annotated, the question asks for the 'primary' compartment, and the evidence explicitly states 'predominantly' cytosolic. The expected answer D (cytoplasm) is well-supported by direct experimental data.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of the PPP-family phosphatase superfamily: 'GDTHGQYY' (GD catalytic motif), 'HGGLYSS' (HG motif), and 'GDFVDRGSYSFEN' (second GD-containing motif). The N-terminal region (~200 residues) exhibits the heptad-repeat pattern characteristic of tetratricopeptide repeat (TPR) domains. The TPR+PPP domain architecture is the defining signature of protein phosphatase 5 (PP5/T5) family members across eukaryotes (human PP5, yeast Ppz1, etc.), which are predominantly cytoplasmic proteins. Mitochondrial matrix proteins require N-terminal amphipathic targeting sequences rich in Arg/Ser/Thr and lacking acidic residues; this N-terminus contains interspersed Glu/Asp residues inconsistent with a mitochondrial targeting signal. TFIID (TBP+TAFs) and SAGA (GCN5, Ada, SPT proteins) are multi-subunit transcriptional complexes with entirely different domain architectures—neither contains PPP-family phosphatase motifs or TPR domains. A knowledgeable model recognizing the TPR+PPP architecture can confidently assign cytoplasmic localization by analogy to the well-characterized cytoplasmic localization of PP5 homologs in human, yeast, and other eukaryotes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PPP-family catalytic motifs (GD, HGGLYSS) and TPR-like N-terminal architecture are directly readable from the sequence. Transferable knowledge that PP5-family phosphatases are cytoplasmic across eukaryotes, combined with the absence of mitochondrial targeting signals and the absence of any TFIID/SAGA component features, meaningfully distinguishes option D from A, B, and C without requiring recall of this specific Trypanosoma entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices (TFIID complex, mitochondrial matrix, SAGA complex, cytoplasm), only cytoplasm is consistent with a TPR+PPP-family phosphatase. The protein is also annotated to nucleus, but nucleus is not among the options. No ambiguity exists among the presented alternatives.


### Important caveats

- The protein is also experimentally annotated to the nucleus (GO:0005634, IDA), but the primary/predominant location is cytosol, and nucleus is not an offered option.
- The organism is Trypanosoma brucei; PP5 homologs in trypanosomatids may have some organism-specific localization differences, but the predominant cytoplasmic localization is consistent with the broader PP5 family pattern.
- The reviewer-only evidence confirms the sequence matches Q388N2 exactly (472 aa, SHA256 match), but this accession was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the PPP-family phosphatase superfamily: 'GDTHGQYY' (GD catalytic motif), 'HGGLYSS' (HG motif), and 'GDFVDRGSYSFEN' (second GD-containing motif). The N-terminal region (~200 residues) exhibits the heptad-repeat pattern characteristic of tetratricopeptide repeat (TPR) domains. The TPR+PPP domain architecture is the defining signature of protein phosphatase 5 (PP5/T5) family members across eukaryotes (human PP5, yeast Ppz1, etc.), which are predominantly cytoplasmic proteins. Mitochondrial matrix proteins require N-terminal amphipathic targeting sequences rich in Arg/Ser/Thr and lacking acidic residues; this N-terminus contains interspersed Glu/Asp residues inconsistent with a mitochondrial targeting signal. TFIID (TBP+TAFs) and SAGA (GCN5, Ada, SPT proteins) are multi-subunit transcriptional complexes with entirely different domain architectures—neither contains PPP-family phosphatase motifs or TPR domains. A knowledgeable model recognizing the TPR+PPP architecture can confidently assign cytoplasmic localization by analogy to the well-characterized cytoplasmic localization of PP5 homologs in human, yeast, and other eukaryotes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PPP-family catalytic motifs (GD, HGGLYSS) and TPR-like N-terminal architecture are directly readable from the sequence. Transferable knowledge that PP5-family phosphatases are cytoplasmic across eukaryotes, combined with the absence of mitochondrial targeting signals and the absence of any TFIID/SAGA component features, meaningfully distinguishes option D from A, B, and C without requiring recall of this specific Trypanosoma entry's annotation."
  },
  "case_id": "GO_cellular_component_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q388N2, PPP5_TRYB2) annotates this protein as 'Predominantly present in the cytosol and localizes densely to the area near the nucleus' with experimental evidence (ECO:0000269, PubMed:11290414). GO:0005737 (cytoplasm) is annotated with IDA evidence. While GO:0005634 (nucleus) is also annotated, the question asks for the 'primary' compartment, and the evidence explicitly states 'predominantly' cytosolic. The expected answer D (cytoplasm) is well-supported by direct experimental data."
  },
  "important_caveats": [
    "The protein is also experimentally annotated to the nucleus (GO:0005634, IDA), but the primary/predominant location is cytosol, and nucleus is not an offered option.",
    "The organism is Trypanosoma brucei; PP5 homologs in trypanosomatids may have some organism-specific localization differences, but the predominant cytoplasmic localization is consistent with the broader PP5 family pattern.",
    "The reviewer-only evidence confirms the sequence matches Q388N2 exactly (472 aa, SHA256 match), but this accession was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices (TFIID complex, mitochondrial matrix, SAGA complex, cytoplasm), only cytoplasm is consistent with a TPR+PPP-family phosphatase. The protein is also annotated to nucleus, but nucleus is not among the options. No ambiguity exists among the presented alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q388N2, PPP5_TRYB2) annotates this protein as 'Predominantly present in the cytosol and localizes densely to the area near the nucleus' with experimental evidence (ECO:0000269, PubMed:11290414). GO:0005737 (cytoplasm) is annotated with IDA evidence. While GO:0005634 (nucleus) is also annotated, the question asks for the 'primary' compartment, and the evidence explicitly states 'predominantly' cytosolic. The expected answer D (cytoplasm) is well-supported by direct experimental data.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the PPP-family phosphatase superfamily: 'GDTHGQYY' (GD catalytic motif), 'HGGLYSS' (HG motif), and 'GDFVDRGSYSFEN' (second GD-containing motif). The N-terminal region (~200 residues) exhibits the heptad-repeat pattern characteristic of tetratricopeptide repeat (TPR) domains. The TPR+PPP domain architecture is the defining signature of protein phosphatase 5 (PP5/T5) family members across eukaryotes (human PP5, yeast Ppz1, etc.), which are predominantly cytoplasmic proteins. Mitochondrial matrix proteins require N-terminal amphipathic targeting sequences rich in Arg/Ser/Thr and lacking acidic residues; this N-terminus contains interspersed Glu/Asp residues inconsistent with a mitochondrial targeting signal. TFIID (TBP+TAFs) and SAGA (GCN5, Ada, SPT proteins) are multi-subunit transcriptional complexes with entirely different domain architectures—neither contains PPP-family phosphatase motifs or TPR domains. A knowledgeable model recognizing the TPR+PPP architecture can confidently assign cytoplasmic localization by analogy to the well-characterized cytoplasmic localization of PP5 homologs in human, yeast, and other eukaryotes.",
    "missing_item_specific_fact": "",
    "reason": "The PPP-family catalytic motifs (GD, HGGLYSS) and TPR-like N-terminal architecture are directly readable from the sequence. Transferable knowledge that PP5-family phosphatases are cytoplasmic across eukaryotes, combined with the absence of mitochondrial targeting signals and the absence of any TFIID/SAGA component features, meaningfully distinguishes option D from A, B, and C without requiring recall of this specific Trypanosoma entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices (TFIID complex, mitochondrial matrix, SAGA complex, cytoplasm), only cytoplasm is consistent with a TPR+PPP-family phosphatase. The protein is also annotated to nucleus, but nucleus is not among the options. No ambiguity exists among the presented alternatives."
  },
  "important_caveats": [
    "The protein is also experimentally annotated to the nucleus (GO:0005634, IDA), but the primary/predominant location is cytosol, and nucleus is not an offered option.",
    "The organism is Trypanosoma brucei; PP5 homologs in trypanosomatids may have some organism-specific localization differences, but the predominant cytoplasmic localization is consistent with the broader PP5 family pattern.",
    "The reviewer-only evidence confirms the sequence matches Q388N2 exactly (472 aa, SHA256 match), but this accession was not available to the evaluated model."
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
  "benchmark_sequence_length": 472,
  "benchmark_sequence_sha256": "cc9358577e82c28a804de40071ec7b0e03104416e51a61cdb314664011a043f5",
  "current_entry_audit": {
    "entryVersion": 116,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-11-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 472,
  "current_source_sequence_sha256": "cc9358577e82c28a804de40071ec7b0e03104416e51a61cdb314664011a043f5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 114,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q388N2",
  "selected_historical_entry_version": 114,
  "selected_historical_record_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "selected_historical_source_sequence_length": 472,
  "selected_historical_source_sequence_sha256": "cc9358577e82c28a804de40071ec7b0e03104416e51a61cdb314664011a043f5",
  "selected_historical_version": {
    "accession": "Q388N2",
    "database": "Swiss-Prot",
    "entryVersion": 114,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PPP5_TRYB2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q388N2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":116,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-11-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008524\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Trypanosoma\"],\"scientificName\":\"Trypanosoma brucei brucei (strain 927/4 GUTat10.1)\",\"taxonId\":185431}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"value\":\"TbPP5\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"value\":\"3.1.3.16\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Serine/threonine-protein phosphatase T\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PPT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"value\":\"Predominantly present in the cytosol and localizes densely to the area near the nucleus (PubMed:11290414). Also present in the nucleus of some cells (PubMed:11290414)\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"id\":\"SL-0091\",\"value\":\"Cytoplasm, cytosol\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"id\":\"SL-0191\",\"value\":\"Nucleus\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"id\":\"GO:0005737\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"id\":\"GO:0005829\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosol\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Chaudhuri M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11290414\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0378-1119(01)00367-5\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"11290414\",\"journal\":\"Gene\",\"lastPage\":\"13\",\"publicationDate\":\"2001\",\"title\":\"Cloning and characterization of a novel serine/threonine protein phosphatase type 5 from Trypanosoma brucei.\",\"volume\":\"266\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11290414\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"LUMP 1026\"}],\"referenceNumber\":2,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:44.659218+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936",
  "url": "https://rest.uniprot.org/uniprotkb/Q388N2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H1",
  "excerpt": "ID   PPP5_TRYB2              Reviewed;         472 AA.\nAC   Q388N2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-NOV-2005, sequence version 1.\nDT   28-JAN-2026, entry version 114.\nDE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000305};\nDE            Short=PPT {ECO:0000305};\nDE            EC=3.1.3.16 {ECO:0000305|PubMed:11290414};\nDE   AltName: Full=TbPP5 {ECO:0000303|PubMed:11290414};\nGN   Name=PPT1 {ECO:0000305};\nGN   ORFNames=Tb10.05.0110 {ECO:0000312|EMBL:EAN78738.1};\nOS   Trypanosoma brucei brucei (strain 927/4 GUTat10.1).\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Trypanosoma.\nOX   NCBI_TaxID=185431 {ECO:0000312|Proteomes:UP000008524};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBCELLULAR LOCATION.\nRC   STRAIN=LUMP 1026 {ECO:0000303|PubMed:11290414};\nRX   PubMed=11290414; DOI=10.1016/s0378-1119(01)00367-5;\nRA   Chaudhuri M.;\nRT   \"Cloning and characterization of a novel serine/threonine protein\nRT   phosphatase type 5 from Trypanosoma brucei.\";\nRL   Gene 266:1-13(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:11290414}.\nCC       Nucleus {ECO:0000269|PubMed:11290414}. Note=Predominantly present in\nCC       the cytosol and localizes densely to the area near the nucleus\nCC       (PubMed:11290414). Also present in the nucleus of some cells\nCC       (PubMed:11290414). {ECO:0000269|PubMed:11290414}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; IDA:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005829; C:cytosol; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:47.011986+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f",
  "url": "https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000124\nname: SAGA complex\nnamespace: cellular_component\nalt_id: GO:0000125\nalt_id: GO:0030914\ndef: \"A SAGA-type histone acetyltransferase complex that deubiquitinates H2A and/or H2B. This complex is organized into several functional submodules: a structural core including the activator binding module and consisting of ADA1 or a homolog, members of the SPT and TAF protein families as well as promotor recruitment factor TRRAP/TRA1, a histone acetyltransferase (HAT) module consisting of GCN5/KAT2A or PCAF/KAT2B, ADA2, ADA3/NGG1, and SGF29 or homologues thereof, a histone deubiquitinase (DUB) module consisting of ATXN7/SGF73, ATXN7L3/SGF11, ENY2/SUS1 and USP22/UBP8 or homologues thereof, and in some taxa a splicing module consisting of SF3B3 and SF3B5 or homologues thereof (not in fungi). In budding yeast also contains Spt8 which distinguishes it from SAGA-like (SLIK) complex (GO:0046695).\" [PMID:10637607, PMID:17337012, PMID:19056896, PMID:20838651, PMID:33004486]\nsynonym: \"PCAF complex\" NARROW []\nsynonym: \"PCAF histone acetylase-associated complex\" NARROW []\nsynonym: \"Spt-Ada-Gcn5-acetyltransferase complex\" EXACT []\nsynonym: \"SPT3-TAF9-GCN5 acetylase complex\" RELATED [GOC:rl, PMID:18838386]\nsynonym: \"SPT3-TAF9-PCAF acetylase complex\" NARROW [PMID:18838386]\nsynonym: \"STAGA coactivator complex\" RELATED []\nsynonym: \"STAGA complex\" RELATED [PMID:32616828, PMID:33004486, PMID:34112237]\nis_a: GO:0070461 ! SAGA-type complex\nis_a: GO:1905368 ! peptidase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000124",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1252-1268",
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
  "excerpt": "[Term]\nid: GO:0005669\nname: transcription factor TFIID complex\nnamespace: cellular_component\ndef: \"A complex composed of TATA binding protein (TBP) and TBP associated factors (TAFs); the total mass is typically about 800 kDa. Most of the TAFs are conserved across species. In TATA-containing promoters for RNA polymerase II (Pol II), TFIID is believed to recognize at least two distinct elements, the TATA element and a downstream promoter element. TFIID is also involved in recognition of TATA-less Pol II promoters. Binding of TFIID to DNA is necessary but not sufficient for transcription initiation from most RNA polymerase II promoters.\" [GOC:krc, GOC:mah, ISBN:0471953393, ISBN:0879695501]\nis_a: GO:0090575 ! RNA polymerase II transcription regulator complex\nrelationship: part_of GO:0016591 ! RNA polymerase II, holoenzyme\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005669",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58368-58375",
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

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0005759\nname: mitochondrial matrix\nnamespace: cellular_component\nalt_id: GO:0031980\ndef: \"The gel-like material, with considerable fine structure, that lies in the matrix space, or lumen, of a mitochondrion. It contains the enzymes of the tricarboxylic acid cycle and, in some organisms, the enzymes concerned with fatty acid oxidation.\" [GOC:as, ISBN:0198506732]\nsynonym: \"mitochondrial lumen\" EXACT []\nsynonym: \"mitochondrial stroma\" NARROW []\nxref: NIF_Subcellular:sao1804523077\nxref: Wikipedia:Mitochondrial_matrix\nis_a: GO:0070013 ! intracellular organelle lumen\nrelationship: part_of GO:0005739 ! mitochondrion\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005759",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59194-59206",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 66. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
