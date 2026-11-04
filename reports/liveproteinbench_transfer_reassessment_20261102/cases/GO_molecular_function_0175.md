# GO_molecular_function_0175

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0175.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — nucleoside transmembrane transporter activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLKGGTAAPAPMAPPRKWYDMTSAEFYVYVVAFMCGISIMMPINAVFSAPSYMLEYYLYATKDPFLVPKMTNFWTNVMTYYNLISMVTSLVVEPLTLLKSFRKIPMLVRLLGGLSVLIIEIIVLMVVPARGTTEAGAVATMCIAGFIGGLGTSIFESTVYGMFGAFPPSFTSIMMGGVGISGVLTSLIQIIVKAALPDTYEGVKKQSYIYYSLDVGIQAATFIALIMMRFNSFAQLHFGDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY

[Multiple Choices]
A. DNA-binding transcription activator activity
B. nucleoside transmembrane transporter activity
C. RNA polymerase II transcription regulatory region sequence-specific DNA binding
D. cardiolipin synthase (CMP-forming)
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

> The matched protein record describes nucleoside transport and cites experimental evidence for transport of adenosine and other nucleosides; its GO annotation also assigns nucleoside transmembrane transporter activity. This supports choice B.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is dominated by long hydrophobic segments consistent with a multipass membrane protein. Transferable knowledge of equilibrative nucleoside transporter families makes nucleoside transport a credible inference from this architecture. That strongly favors B over the DNA-binding transcription functions in A and C; the sequence also does not suggest the catalytic cardiolipin synthase function in D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices make the family-level inference discriminating: a multipass transporter is a meaningful match for B, whereas A and C imply DNA-binding regulatory proteins. The sequence alone does not establish substrate specificity, but the alternatives do not require that finer distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered alternatives, B is the clear fit for a multipass nucleoside transporter.


### Important caveats

- The reviewer-only record supports the key but was not part of the original input; the answerability judgment rests on transferable sequence and family-level knowledge.
- Multipass topology alone cannot establish the exact transported substrates or experimentally confirm function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is dominated by long hydrophobic segments consistent with a multipass membrane protein. Transferable knowledge of equilibrative nucleoside transporter families makes nucleoside transport a credible inference from this architecture. That strongly favors B over the DNA-binding transcription functions in A and C; the sequence also does not suggest the catalytic cardiolipin synthase function in D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices make the family-level inference discriminating: a multipass transporter is a meaningful match for B, whereas A and C imply DNA-binding regulatory proteins. The sequence alone does not establish substrate specificity, but the alternatives do not require that finer distinction."
  },
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11"
    ],
    "judgment": "supported",
    "reason": "The matched protein record describes nucleoside transport and cites experimental evidence for transport of adenosine and other nucleosides; its GO annotation also assigns nucleoside transmembrane transporter activity. This supports choice B."
  },
  "important_caveats": [
    "The reviewer-only record supports the key but was not part of the original input; the answerability judgment rests on transferable sequence and family-level knowledge.",
    "Multipass topology alone cannot establish the exact transported substrates or experimentally confirm function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, B is the clear fit for a multipass nucleoside transporter."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein record describes nucleoside transport and cites experimental evidence for transport of adenosine and other nucleosides; its GO annotation also assigns nucleoside transmembrane transporter activity. This supports choice B.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is dominated by long hydrophobic segments consistent with a multipass membrane protein. Transferable knowledge of equilibrative nucleoside transporter families makes nucleoside transport a credible inference from this architecture. That strongly favors B over the DNA-binding transcription functions in A and C; the sequence also does not suggest the catalytic cardiolipin synthase function in D.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices make the family-level inference discriminating: a multipass transporter is a meaningful match for B, whereas A and C imply DNA-binding regulatory proteins. The sequence alone does not establish substrate specificity, but the alternatives do not require that finer distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, B is the clear fit for a multipass nucleoside transporter."
  },
  "important_caveats": [
    "The reviewer-only record supports the key but was not part of the original input; the answerability judgment rests on transferable sequence and family-level knowledge.",
    "Multipass topology alone cannot establish the exact transported substrates or experimentally confirm function."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9GTP5 is named 'Nucleoside transporter 1' (CfNT1) with experimental evidence (ECO:0000269, direct assay) from three independent PubMed studies demonstrating transport of adenosine, hypoxanthine, inosine, uridine, and cytidine. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (SHA-256 match, 497 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C11](#evidence-c11), [H5](#evidence-h5), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 497-residue sequence exhibits a clear multi-pass transmembrane topology: numerous hydrophobic stretches (~11-12 predicted TMs) interrupted by a large central hydrophilic loop (approximately residues 200-280: 'GDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY'). This 11-12 TM + large central loop architecture is the hallmark of the equilibrative nucleoside transporter (ENT/SLC29) family. This immediately eliminates options A and C (DNA-binding transcription factors require nuclear localization, DNA-binding motifs like zinc fingers or helix-turn-helix, and are not multi-pass membrane proteins). Option D (cardiolipin synthase, CMP-forming) belongs to the CDP-alcohol phosphatidyltransferase family, which has a distinct fold with fewer (~6-8) TMs and catalytic motifs (e.g., the conserved 'P...S...S' phosphatidyltransferase motif) absent here. The ENT-specific topology with the characteristic central loop and overall TM count meaningfully distinguishes B from D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the multi-pass membrane topology from the hydrophobicity pattern, identify the ENT-family signature (11-12 TMs with a large central hydrophilic loop), and use family-level knowledge to exclude DNA-binding activities (A, C) and the CDP-alcohol phosphatidyltransferase fold (D). This is a legitimate transferable inference from membrane protein family architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are clearly incompatible with a multi-pass membrane protein lacking any DNA-binding motif. Option D (cardiolipin synthase) has a fundamentally different fold and TM topology from the ENT-like architecture observed. Only B is consistent with the sequence features.


### Important caveats

- The GO annotation in UniProt is IEA:InterPro (computational by similarity), but the underlying experimental evidence (ECO:0000269) from three independent studies confirms the transporter function directly.
- The protein is from Crithidia fasciculata (a trypanosomatid), an organism whose nucleoside transporters are well-studied as drug targets; this biological context supports the ENT assignment.
- The sequence-to-topology argument relies on hydrophobicity analysis and family-level pattern recognition rather than a solved structure of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 497-residue sequence exhibits a clear multi-pass transmembrane topology: numerous hydrophobic stretches (~11-12 predicted TMs) interrupted by a large central hydrophilic loop (approximately residues 200-280: 'GDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY'). This 11-12 TM + large central loop architecture is the hallmark of the equilibrative nucleoside transporter (ENT/SLC29) family. This immediately eliminates options A and C (DNA-binding transcription factors require nuclear localization, DNA-binding motifs like zinc fingers or helix-turn-helix, and are not multi-pass membrane proteins). Option D (cardiolipin synthase, CMP-forming) belongs to the CDP-alcohol phosphatidyltransferase family, which has a distinct fold with fewer (~6-8) TMs and catalytic motifs (e.g., the conserved 'P...S...S' phosphatidyltransferase motif) absent here. The ENT-specific topology with the characteristic central loop and overall TM count meaningfully distinguishes B from D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the multi-pass membrane topology from the hydrophobicity pattern, identify the ENT-family signature (11-12 TMs with a large central hydrophilic loop), and use family-level knowledge to exclude DNA-binding activities (A, C) and the CDP-alcohol phosphatidyltransferase fold (D). This is a legitimate transferable inference from membrane protein family architecture."
  },
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C11",
      "H5",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP5 is named 'Nucleoside transporter 1' (CfNT1) with experimental evidence (ECO:0000269, direct assay) from three independent PubMed studies demonstrating transport of adenosine, hypoxanthine, inosine, uridine, and cytidine. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (SHA-256 match, 497 aa)."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA:InterPro (computational by similarity), but the underlying experimental evidence (ECO:0000269) from three independent studies confirms the transporter function directly.",
    "The protein is from Crithidia fasciculata (a trypanosomatid), an organism whose nucleoside transporters are well-studied as drug targets; this biological context supports the ENT assignment.",
    "The sequence-to-topology argument relies on hydrophobicity analysis and family-level pattern recognition rather than a solved structure of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly incompatible with a multi-pass membrane protein lacking any DNA-binding motif. Option D (cardiolipin synthase) has a fundamentally different fold and TM topology from the ENT-like architecture observed. Only B is consistent with the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP5 is named 'Nucleoside transporter 1' (CfNT1) with experimental evidence (ECO:0000269, direct assay) from three independent PubMed studies demonstrating transport of adenosine, hypoxanthine, inosine, uridine, and cytidine. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (SHA-256 match, 497 aa).",
    "evidence_ids": ["C4", "C5", "C6", "C11", "H5", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 497-residue sequence exhibits a clear multi-pass transmembrane topology: numerous hydrophobic stretches (~11-12 predicted TMs) interrupted by a large central hydrophilic loop (approximately residues 200-280: 'GDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY'). This 11-12 TM + large central loop architecture is the hallmark of the equilibrative nucleoside transporter (ENT/SLC29) family. This immediately eliminates options A and C (DNA-binding transcription factors require nuclear localization, DNA-binding motifs like zinc fingers or helix-turn-helix, and are not multi-pass membrane proteins). Option D (cardiolipin synthase, CMP-forming) belongs to the CDP-alcohol phosphatidyltransferase family, which has a distinct fold with fewer (~6-8) TMs and catalytic motifs (e.g., the conserved 'P...S...S' phosphatidyltransferase motif) absent here. The ENT-specific topology with the characteristic central loop and overall TM count meaningfully distinguishes B from D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the multi-pass membrane topology from the hydrophobicity pattern, identify the ENT-family signature (11-12 TMs with a large central hydrophilic loop), and use family-level knowledge to exclude DNA-binding activities (A, C) and the CDP-alcohol phosphatidyltransferase fold (D). This is a legitimate transferable inference from membrane protein family architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly incompatible with a multi-pass membrane protein lacking any DNA-binding motif. Option D (cardiolipin synthase) has a fundamentally different fold and TM topology from the ENT-like architecture observed. Only B is consistent with the sequence features."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA:InterPro (computational by similarity), but the underlying experimental evidence (ECO:0000269) from three independent studies confirms the transporter function directly.",
    "The protein is from Crithidia fasciculata (a trypanosomatid), an organism whose nucleoside transporters are well-studied as drug targets; this biological context supports the ENT assignment.",
    "The sequence-to-topology argument relies on hydrophobicity analysis and family-level pattern recognition rather than a solved structure of this exact protein."
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
  "benchmark_sequence_length": 497,
  "benchmark_sequence_sha256": "3164fbc4f11b9d95188d1d240b8371851f4562adacc551b564f7e6157797e81d",
  "current_entry_audit": {
    "entryVersion": 57,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2001-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 497,
  "current_source_sequence_sha256": "3164fbc4f11b9d95188d1d240b8371851f4562adacc551b564f7e6157797e81d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 57,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9GTP5",
  "selected_historical_entry_version": 57,
  "selected_historical_record_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "selected_historical_source_sequence_length": 497,
  "selected_historical_source_sequence_sha256": "3164fbc4f11b9d95188d1d240b8371851f4562adacc551b564f7e6157797e81d",
  "selected_historical_version": {
    "accession": "Q9GTP5",
    "database": "Swiss-Prot",
    "entryVersion": 57,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NT1_CRIFA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9GTP5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":57,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2001-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAG22610.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Crithidia\"],\"scientificName\":\"Crithidia fasciculata\",\"taxonId\":5656}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"value\":\"CfNT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20037157\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter with broad substrate specificity (PubMed:15694482). Transports adenosine with high affinity (PubMed:15694482, PubMed:20037157, PubMed:24120444). Can also transport hypoxanthine, inosine, uridine and cytidine (PubMed:15694482)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20037157\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"name\":\"adenosine(in) = adenosine(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75343\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16335\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"name\":\"hypoxanthine(out) = hypoxanthine(in)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:71515\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17368\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"name\":\"inosine(in) = inosine(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75375\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17596\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"name\":\"uridine(out) = uridine(in)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:71519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16704\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"name\":\"cytidine(in) = cytidine(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75367\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17562\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005337\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:nucleoside transmembrane transporter activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu W.\",\"Arendt C.S.\",\"Gessford S.K.\",\"Ntaba D.\",\"Carter N.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15694482\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2004.11.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"15694482\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"12\",\"publicationDate\":\"2005\",\"title\":\"Identification and characterization of purine nucleoside transporters from Crithidia fasciculata.\",\"volume\":\"140\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"INDUCTION BY PUFINE STARVATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20037157\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.074351\"}],\"citationType\":\"journal article\",\"firstPage\":\"6024\",\"id\":\"20037157\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"6035\",\"publicationDate\":\"2010\",\"title\":\"Role of transmembrane domain 4 in ligand permeation by Crithidia fasciculata equilibrative nucleoside transporter 2 (CfNT2).\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24120444\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2013.09.007\"}],\"citationType\":\"journal article\",\"firstPage\":\"75\",\"id\":\"24120444\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"79\",\"publicationDate\":\"2013\",\"title\":\"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-affinity equilibrative nucleoside transporter specific for adenosine.\",\"volume\":\"191\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF THR-153\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H1",
  "excerpt": "ID   NT1_CRIFA               Reviewed;         497 AA.\nAC   Q9GTP5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2001, sequence version 1.\nDT   28-JAN-2026, entry version 57.\nDE   RecName: Full=Nucleoside transporter 1 {ECO:0000303|PubMed:15694482};\nDE            Short=CfNT1 {ECO:0000303|PubMed:15694482, ECO:0000303|PubMed:20037157, ECO:0000303|PubMed:24120444};\nOS   Crithidia fasciculata.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Crithidia.\nOX   NCBI_TaxID=5656 {ECO:0000312|EMBL:AAG22610.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   INDUCTION BY PUFINE STARVATION.\nRX   PubMed=15694482; DOI=10.1016/j.molbiopara.2004.11.018;\nRA   Liu W., Arendt C.S., Gessford S.K., Ntaba D., Carter N.S., Ullman B.;\nRT   \"Identification and characterization of purine nucleoside transporters from\nRT   Crithidia fasciculata.\";\nRL   Mol. Biochem. Parasitol. 140:1-12(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, AND SUBCELLULAR LOCATION.\nRX   PubMed=20037157; DOI=10.1074/jbc.m109.074351;\nRA   Arendt C.S., Ullman B.;\nRT   \"Role of transmembrane domain 4 in ligand permeation by Crithidia\nRT   fasciculata equilibrative nucleoside transporter 2 (CfNT2).\";\nRL   J. Biol. Chem. 285:6024-6035(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   MUTAGENESIS OF THR-153.\nRX   PubMed=24120444; DOI=10.1016/j.molbiopara.2013.09.007;\nRA   Arendt C.S.;\nRT   \"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-\nRT   affinity equilibrative nucleoside transporter specific for adenosine.\";\nRL   Mol. Biochem. Parasitol. 191:75-79(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Nucleoside transporter with broad substrate specificity\nCC       (PubMed:15694482). Transports adenosine with high affinity\nCC       (PubMed:15694482, PubMed:20037157, PubMed:24120444). Can also transport\nCC       hypoxanthine, inosine, uridine and cytidine (PubMed:15694482).\nCC       {ECO:0000269|PubMed:15694482, ECO:0000269|PubMed:20037157,\nCC       ECO:0000269|PubMed:24120444}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=adenosine(in) = adenosine(out); Xref=Rhea:RHEA:75343,\nCC         ChEBI:CHEBI:16335; Evidence={ECO:0000269|PubMed:15694482,\nCC         ECO:0000269|PubMed:20037157, ECO:0000269|PubMed:24120444};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=hypoxanthine(out) = hypoxanthine(in); Xref=Rhea:RHEA:71515,\nCC         ChEBI:CHEBI:17368; Evidence={ECO:0000269|PubMed:15694482};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=inosine(in) = inosine(out); Xref=Rhea:RHEA:75375,\nCC         ChEBI:CHEBI:17596; Evidence={ECO:0000269|PubMed:15694482};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=uridine(out) = uridine(in); Xref=Rhea:RHEA:71519,\nCC         ChEBI:CHEBI:16704; Evidence={ECO:0000269|PubMed:15694482};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=cytidine(in) = cytidine(out); Xref=Rhea:RHEA:75367,\nCC         ChEBI:CHEBI:17562; Evidence={ECO:0000269|PubMed:15694482};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H11",
  "excerpt": "DR   GO; GO:0005337; F:nucleoside transmembrane transporter activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000977\nname: RNA polymerase II transcription regulatory region sequence-specific DNA binding\nnamespace: molecular_function\nalt_id: GO:0001012\ndef: \"Binding to a specific sequence of DNA that is part of a regulatory region that controls the transcription of a gene or cistron by RNA polymerase II.\" [GOC:txnOH]\ncomment: To minimize ambiguity in the use of the word \"promoter\" in GO, we have chosen the phrase \"transcription regulatory region\" to refer to all of the regulatory regions. Regulatory regions in the DNA which control initiation may include the \"core promoter\" where the basal transcription machinery binds, the \"core promoter proximal region\" where regulatory factors other than the basal machinery bind. There are also additional regulatory regions, in both the DNA and the RNA transcript, which regulate elongation or termination of transcription.\nsynonym: \"RNA polymerase II regulatory region DNA binding\" RELATED []\nis_a: GO:0000976 ! transcription cis-regulatory region binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000977",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 7116-7125",
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
  "excerpt": "[Term]\nid: GO:0001216\nname: DNA-binding transcription activator activity\nnamespace: molecular_function\nalt_id: GO:0001140\nalt_id: GO:0001215\ndef: \"A DNA-binding transcription factor activity that activates or increases transcription of specific gene sets.\" [GOC:txnOH-2018]\ncomment: For usage guidance, see comment in GO:0003700 ; DNA-binding transcription factor activity.\nsynonym: \"bacterial-type RNA polymerase core promoter proximal region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription\" RELATED []\nsynonym: \"bacterial-type RNA polymerase transcriptional activator activity, metal ion regulated sequence-specific DNA binding\" NARROW []\nsynonym: \"bacterial-type RNA polymerase transcriptional activator activity, sequence-specific DNA binding\" NARROW []\nsynonym: \"metal ion regulated sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"transcriptional activator activity, bacterial-type RNA polymerase core promoter proximal region sequence-specific binding\" NARROW []\nsynonym: \"transcriptional activator activity, bacterial-type RNA polymerase proximal promoter sequence-specific DNA binding\" RELATED []\nis_a: GO:0003700 ! DNA-binding transcription factor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0001216",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 8558-8574",
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
  "excerpt": "[Term]\nid: GO:0005337\nname: nucleoside transmembrane transporter activity\nnamespace: molecular_function\ndef: \"Enables the transfer of a nucleoside, a nucleobase linked to either beta-D-ribofuranose (ribonucleoside) or 2-deoxy-beta-D-ribofuranose, (a deoxyribonucleotide) from one side of a membrane to the other.\" [GOC:ai]\nsynonym: \"intracellular nucleoside transmembrane transporter activity\" NARROW []\nxref: Reactome:R-HSA-109527 \"Equilibrative transport (import) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 2\"\nxref: Reactome:R-HSA-109529 \"Equilibrative transport (export) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 2\"\nxref: Reactome:R-HSA-109534 \"Equilibrative transport (export) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 1\"\nxref: Reactome:R-HSA-109536 \"Equilibrative transport (import) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 1\"\nxref: Reactome:R-HSA-5628807 \"Defective SLC29A3 does not transport nucleosides from lysosomal lumen to cytosol\"\nxref: Reactome:R-HSA-727740 \"Equilibrative transport (import) of adenosine and biogenic amines by solute carrier family 29 (nucleoside transporters), member 4\"\nxref: Reactome:R-HSA-727749 \"SLC29A3 transports nucleosides from lysosomal lumen to cytosol\"\nxref: Reactome:R-HSA-727767 \"SLC29A3 transports nucleosides from cytosol to lysosomal lumen\"\nxref: Reactome:R-HSA-727768 \"Equilibrative transport (export) of adenosine and biogenic amines by solute carrier family 29 (nucleoside transporters), member 4\"\nxref: Reactome:R-HSA-9751024 \"SLC29A1,2 transport 6MP from extracellular region to cytosol\"\nxref: Reactome:R-HSA-9754929 \"SLC29A3 transports RBV,RBV-TP from cytosol to mitochondrial matrix\"\nxref: Reactome:R-HSA-9755015 \"SLC29A1 transports RBV from extracellular region to cytosol\"\nxref: Reactome:R-HSA-9755035 \"SLC29A1 transports RBV from cytosol to extracellular region\"\nis_a: GO:0015932 ! nucleobase-containing compound transmembrane transporter activity\nis_a: GO:1901505 ! carbohydrate derivative transmembrane transporter activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005337",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 55843-55864",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 175. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
