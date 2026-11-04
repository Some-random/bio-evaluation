# GO_cellular_component_0170

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0170.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIIDLFQSKKLIISIIILILRISLFSCAEHLFFNNNFNFFNFSENNHAKVNELNIDTKYLYQGLRNINIYLALSALNGITKEKINDISQWNGYKTRNNDETNISNVVVTEWKQLNKKSFFLKNNNISNNDNLIKGMPNPYFINSLTEDINNINLYFNIRNDIKYGEIIYKGTYIPHIYNNIFLIFLISYMYWFCIKILFNGYIKGKYVAKEYILKISTLFIFFVILKISLIFLPAILSCIVCLILTFYFYSISMSPCKDIFYLFESTRIKKEPIGWIIIVYAESILIGNVIYNFLCPPKIIIIFIRYIQNDFLVKIICLTIILFISFLIFFLMISNIFPAKKAQNFVFSFTSSYLIVSCFAYFWNIFLLRFLNNTNIFQIEPIMFFSYTPKFVFNRQNMFALFMIFAMSILSIIFPRIKKLKQNIFDMKENIYDSDIDIGKASKNRYNIILNYFT

[Multiple Choices]
A. rhoptry
B. vacuolar membrane
C. spindle
D. plasma membrane
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

> The sequence-matched UniProt annotation reports plasma-membrane localization in female gametes and ookinetes, alongside flagellar localization in male gametes. Thus D is supported for relevant stages, although localization is stage-dependent rather than exclusively at the plasma membrane.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has several strongly hydrophobic segments, supporting a multi-pass membrane-protein inference and making a membrane location more plausible than the spindle. But that feature does not meaningfully distinguish plasma membrane from vacuolar membrane; the sequence alone supplies no clear compartment-specific targeting signal.


**Missing item-specific fact**

> The protein's experimentally observed subcellular distribution, including its developmental-stage dependence, is not given in the original input.


**Reason**

> A general membrane-protein inference transfers from sequence features, but it does not settle the key distinction between choices B and D. Resolving that distinction requires protein-specific localization information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> From the original sequence, a multi-pass membrane protein could plausibly reside in either the plasma or vacuolar membrane; the supplied sequence does not distinguish these destinations. The reviewer-only localization evidence supports D, but was not part of the original input.


### Important caveats

- The source annotation reports different localization by developmental stage, including flagella and residual body in male gametes; neither is an offered choice.
- The localization evidence is reported in the supplied database excerpt with experimental evidence attribution; it was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several strongly hydrophobic segments, supporting a multi-pass membrane-protein inference and making a membrane location more plausible than the spindle. But that feature does not meaningfully distinguish plasma membrane from vacuolar membrane; the sequence alone supplies no clear compartment-specific targeting signal.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally observed subcellular distribution, including its developmental-stage dependence, is not given in the original input.",
    "reason": "A general membrane-protein inference transfers from sequence features, but it does not settle the key distinction between choices B and D. Resolving that distinction requires protein-specific localization information."
  },
  "case_id": "GO_cellular_component_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports plasma-membrane localization in female gametes and ookinetes, alongside flagellar localization in male gametes. Thus D is supported for relevant stages, although localization is stage-dependent rather than exclusively at the plasma membrane."
  },
  "important_caveats": [
    "The source annotation reports different localization by developmental stage, including flagella and residual body in male gametes; neither is an offered choice.",
    "The localization evidence is reported in the supplied database excerpt with experimental evidence attribution; it was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "From the original sequence, a multi-pass membrane protein could plausibly reside in either the plasma or vacuolar membrane; the supplied sequence does not distinguish these destinations. The reviewer-only localization evidence supports D, but was not part of the original input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports plasma-membrane localization in female gametes and ookinetes, alongside flagellar localization in male gametes. Thus D is supported for relevant stages, although localization is stage-dependent rather than exclusively at the plasma membrane.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has several strongly hydrophobic segments, supporting a multi-pass membrane-protein inference and making a membrane location more plausible than the spindle. But that feature does not meaningfully distinguish plasma membrane from vacuolar membrane; the sequence alone supplies no clear compartment-specific targeting signal.",
    "missing_item_specific_fact": "The protein's experimentally observed subcellular distribution, including its developmental-stage dependence, is not given in the original input.",
    "reason": "A general membrane-protein inference transfers from sequence features, but it does not settle the key distinction between choices B and D. Resolving that distinction requires protein-specific localization information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "From the original sequence, a multi-pass membrane protein could plausibly reside in either the plasma or vacuolar membrane; the supplied sequence does not distinguish these destinations. The reviewer-only localization evidence supports D, but was not part of the original input."
  },
  "important_caveats": [
    "The source annotation reports different localization by developmental stage, including flagella and residual body in male gametes; neither is an offered choice.",
    "The localization evidence is reported in the supplied database excerpt with experimental evidence attribution; it was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A509AKT6, Pbs54 from Plasmodium berghei) carries experimental evidence (ECO:0000269, PubMed:37774810) for plasma membrane localization in female gametes and ookinetes, annotated as GO:0005886 (plasma membrane) with IEA:UniProtKB-SubCell. The subcellular location comment explicitly states 'in female gametes, localizes to the plasma membrane. In ookinetes, localizes to the plasma membrane.' The protein is annotated as a multi-pass membrane protein. While it also localizes to flagella in male gametes, plasma membrane is a primary annotated location consistent with the expected answer D.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches (at least 5-6 potential transmembrane segments) preceded by an N-terminal signal-peptide-like region, identifying it as a multi-pass membrane protein. This immediately eliminates spindle (C), a microtubule-based structure incompatible with a transmembrane protein. The highly Asn-rich regions (e.g., NNNFNFFNFSENNH, NNNISNNDNLIKG) are a well-known compositional signature of Plasmodium proteins, placing the protein in an apicomplexan context. In Plasmodium, rhoptry proteins (e.g., RON, RAP families) are secreted proteins—either cleaved signal peptides with no TM domains or single-pass proteins processed for secretion into the rhoptry lumen. A multi-pass membrane protein is inconsistent with rhoptry biogenesis, eliminating option A. Between vacuolar membrane (B) and plasma membrane (D): in Plasmodium, the parasitophorous vacuole membrane proteins are predominantly secreted proteins or carry specific export motifs (Pexel), while multi-pass membrane proteins with signal peptides are overwhelmingly plasma membrane proteins (e.g., Pfs48/45 with 6 TM, Pfs230 with 24 TM, Pfs47 with 14 TM—all gamete/ookinete surface proteins). This family-level statistical pattern from other Plasmodium proteins provides a defensible probabilistic basis for choosing plasma membrane over vacuolar membrane.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-pass membrane topology is directly observable from the hydrophobic segment analysis of the sequence. The Plasmodium origin is inferable from the Asn-rich composition. The elimination of rhoptry relies on well-established family-level knowledge that rhoptry proteins are secreted, not multi-pass membrane. The preference for plasma membrane over vacuolar membrane rests on the empirical pattern that multi-pass membrane proteins with signal peptides in Plasmodium are predominantly plasma membrane proteins, a pattern learned from multiple characterized homologs (Pfs48/45, Pfs230, Pfs47). This constitutes a legitimate probabilistic generalization from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While distinguishing B (vacuolar membrane) from D (plasma membrane) requires probabilistic reasoning rather than absolute certainty, the strong family-level pattern in Plasmodium (multi-pass membrane + signal peptide → plasma membrane; secreted/exported → PVM) provides a clear probabilistic preference for D. The other options (A, C) are effectively eliminated by topology and family knowledge. No pair of options is genuinely indistinguishable given the sequence features and transferable knowledge.


### Important caveats

- The protein also localizes to flagella in male gametes per experimental data, but 'plasma membrane' remains a primary annotated location and is the only membrane-compartment option among the choices that matches.
- The Plasmodium identification from Asn-rich composition is a strong but not absolute inference; other apicomplexans or AT-rich organisms could produce similar patterns.
- The multi-pass membrane topology is inferred from hydrophobicity analysis of the sequence, not from experimental structural data available to the model.
- The reviewer-only evidence confirms the protein is Pbs54 from Plasmodium berghei with experimental plasma membrane annotation, but this identity was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (at least 5-6 potential transmembrane segments) preceded by an N-terminal signal-peptide-like region, identifying it as a multi-pass membrane protein. This immediately eliminates spindle (C), a microtubule-based structure incompatible with a transmembrane protein. The highly Asn-rich regions (e.g., NNNFNFFNFSENNH, NNNISNNDNLIKG) are a well-known compositional signature of Plasmodium proteins, placing the protein in an apicomplexan context. In Plasmodium, rhoptry proteins (e.g., RON, RAP families) are secreted proteins—either cleaved signal peptides with no TM domains or single-pass proteins processed for secretion into the rhoptry lumen. A multi-pass membrane protein is inconsistent with rhoptry biogenesis, eliminating option A. Between vacuolar membrane (B) and plasma membrane (D): in Plasmodium, the parasitophorous vacuole membrane proteins are predominantly secreted proteins or carry specific export motifs (Pexel), while multi-pass membrane proteins with signal peptides are overwhelmingly plasma membrane proteins (e.g., Pfs48/45 with 6 TM, Pfs230 with 24 TM, Pfs47 with 14 TM—all gamete/ookinete surface proteins). This family-level statistical pattern from other Plasmodium proteins provides a defensible probabilistic basis for choosing plasma membrane over vacuolar membrane.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass membrane topology is directly observable from the hydrophobic segment analysis of the sequence. The Plasmodium origin is inferable from the Asn-rich composition. The elimination of rhoptry relies on well-established family-level knowledge that rhoptry proteins are secreted, not multi-pass membrane. The preference for plasma membrane over vacuolar membrane rests on the empirical pattern that multi-pass membrane proteins with signal peptides in Plasmodium are predominantly plasma membrane proteins, a pattern learned from multiple characterized homologs (Pfs48/45, Pfs230, Pfs47). This constitutes a legitimate probabilistic generalization from other proteins."
  },
  "case_id": "GO_cellular_component_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A509AKT6, Pbs54 from Plasmodium berghei) carries experimental evidence (ECO:0000269, PubMed:37774810) for plasma membrane localization in female gametes and ookinetes, annotated as GO:0005886 (plasma membrane) with IEA:UniProtKB-SubCell. The subcellular location comment explicitly states 'in female gametes, localizes to the plasma membrane. In ookinetes, localizes to the plasma membrane.' The protein is annotated as a multi-pass membrane protein. While it also localizes to flagella in male gametes, plasma membrane is a primary annotated location consistent with the expected answer D."
  },
  "important_caveats": [
    "The protein also localizes to flagella in male gametes per experimental data, but 'plasma membrane' remains a primary annotated location and is the only membrane-compartment option among the choices that matches.",
    "The Plasmodium identification from Asn-rich composition is a strong but not absolute inference; other apicomplexans or AT-rich organisms could produce similar patterns.",
    "The multi-pass membrane topology is inferred from hydrophobicity analysis of the sequence, not from experimental structural data available to the model.",
    "The reviewer-only evidence confirms the protein is Pbs54 from Plasmodium berghei with experimental plasma membrane annotation, but this identity was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While distinguishing B (vacuolar membrane) from D (plasma membrane) requires probabilistic reasoning rather than absolute certainty, the strong family-level pattern in Plasmodium (multi-pass membrane + signal peptide → plasma membrane; secreted/exported → PVM) provides a clear probabilistic preference for D. The other options (A, C) are effectively eliminated by topology and family knowledge. No pair of options is genuinely indistinguishable given the sequence features and transferable knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A509AKT6, Pbs54 from Plasmodium berghei) carries experimental evidence (ECO:0000269, PubMed:37774810) for plasma membrane localization in female gametes and ookinetes, annotated as GO:0005886 (plasma membrane) with IEA:UniProtKB-SubCell. The subcellular location comment explicitly states 'in female gametes, localizes to the plasma membrane. In ookinetes, localizes to the plasma membrane.' The protein is annotated as a multi-pass membrane protein. While it also localizes to flagella in male gametes, plasma membrane is a primary annotated location consistent with the expected answer D.",
    "evidence_ids": ["C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (at least 5-6 potential transmembrane segments) preceded by an N-terminal signal-peptide-like region, identifying it as a multi-pass membrane protein. This immediately eliminates spindle (C), a microtubule-based structure incompatible with a transmembrane protein. The highly Asn-rich regions (e.g., NNNFNFFNFSENNH, NNNISNNDNLIKG) are a well-known compositional signature of Plasmodium proteins, placing the protein in an apicomplexan context. In Plasmodium, rhoptry proteins (e.g., RON, RAP families) are secreted proteins—either cleaved signal peptides with no TM domains or single-pass proteins processed for secretion into the rhoptry lumen. A multi-pass membrane protein is inconsistent with rhoptry biogenesis, eliminating option A. Between vacuolar membrane (B) and plasma membrane (D): in Plasmodium, the parasitophorous vacuole membrane proteins are predominantly secreted proteins or carry specific export motifs (Pexel), while multi-pass membrane proteins with signal peptides are overwhelmingly plasma membrane proteins (e.g., Pfs48/45 with 6 TM, Pfs230 with 24 TM, Pfs47 with 14 TM—all gamete/ookinete surface proteins). This family-level statistical pattern from other Plasmodium proteins provides a defensible probabilistic basis for choosing plasma membrane over vacuolar membrane.",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass membrane topology is directly observable from the hydrophobic segment analysis of the sequence. The Plasmodium origin is inferable from the Asn-rich composition. The elimination of rhoptry relies on well-established family-level knowledge that rhoptry proteins are secreted, not multi-pass membrane. The preference for plasma membrane over vacuolar membrane rests on the empirical pattern that multi-pass membrane proteins with signal peptides in Plasmodium are predominantly plasma membrane proteins, a pattern learned from multiple characterized homologs (Pfs48/45, Pfs230, Pfs47). This constitutes a legitimate probabilistic generalization from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While distinguishing B (vacuolar membrane) from D (plasma membrane) requires probabilistic reasoning rather than absolute certainty, the strong family-level pattern in Plasmodium (multi-pass membrane + signal peptide → plasma membrane; secreted/exported → PVM) provides a clear probabilistic preference for D. The other options (A, C) are effectively eliminated by topology and family knowledge. No pair of options is genuinely indistinguishable given the sequence features and transferable knowledge."
  },
  "important_caveats": [
    "The protein also localizes to flagella in male gametes per experimental data, but 'plasma membrane' remains a primary annotated location and is the only membrane-compartment option among the choices that matches.",
    "The Plasmodium identification from Asn-rich composition is a strong but not absolute inference; other apicomplexans or AT-rich organisms could produce similar patterns.",
    "The multi-pass membrane topology is inferred from hydrophobicity analysis of the sequence, not from experimental structural data available to the model.",
    "The reviewer-only evidence confirms the protein is Pbs54 from Plasmodium berghei with experimental plasma membrane annotation, but this identity was not available to the evaluated model."
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
  "benchmark_sequence_length": 455,
  "benchmark_sequence_sha256": "1460df501b8bcc92b33e8ca8893f41aacacbf2a45774542573ece53788a3b826",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-09-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 455,
  "current_source_sequence_sha256": "1460df501b8bcc92b33e8ca8893f41aacacbf2a45774542573ece53788a3b826",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A509AKT6",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "selected_historical_source_sequence_length": 455,
  "selected_historical_source_sequence_sha256": "1460df501b8bcc92b33e8ca8893f41aacacbf2a45774542573ece53788a3b826",
  "selected_historical_version": {
    "accession": "A0A509AKT6",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PBS54_PLABA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A509AKT6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-09-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000074855\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Vinckeia\"],\"scientificName\":\"Plasmodium berghei (strain Anka)\",\"taxonId\":5823}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37774810\",\"source\":\"PubMed\"}],\"value\":\"Membrane protein Pbs54\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37774810\",\"source\":\"PubMed\"}],\"value\":\"Pbs54\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37774810\",\"source\":\"PubMed\"}],\"value\":\"In male gametes, localizes to the flagella and residual body; in female gametes, localizes to the plasma membrane. In ookinetes, localizes to the plasma membrane\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37774810\",\"source\":\"PubMed\"}],\"id\":\"SL-0117\",\"value\":\"Cell projection, cilium, flagellum\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37774810\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031514\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:motile cilium\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Pang W.\",\"Bai J.\",\"Zhu L.\",\"Liu F.\",\"Wu Y.\",\"Yang F.\",\"Zheng L.\",\"Liu P.\",\"Zhang Y.\",\"Wang M.\",\"Li J.\",\"Zhu X.\",\"Cui L.\",\"Cao Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37774810\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijpara.2023.08.003\"}],\"citationType\":\"journal article\",\"firstPage\":\"99\",\"id\":\"37774810\",\"journal\":\"Int. J. Parasitol.\",\"lastPage\":\"107\",\"publicationDate\":\"2024\",\"title\":\"Functional characterization of a conserved membrane protein, Pbs54, involved in gamete fertilization in Plasmodium berghei.\",\"volume\":\"54\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   PBS54_PLABA             Reviewed;         455 AA.\nAC   A0A509AKT6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-SEP-2019, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Membrane protein Pbs54 {ECO:0000303|PubMed:37774810};\nDE            Short=Pbs54 {ECO:0000303|PubMed:37774810};\nGN   ORFNames=PBANKA_0813300 {ECO:0000312|EMBL:VUC55291.1};\nOS   Plasmodium berghei (strain Anka).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).\nOX   NCBI_TaxID=5823 {ECO:0000312|Proteomes:UP000074855};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=37774810; DOI=10.1016/j.ijpara.2023.08.003;\nRA   Pang W., Bai J., Zhu L., Liu F., Wu Y., Yang F., Zheng L., Liu P.,\nRA   Zhang Y., Wang M., Li J., Zhu X., Cui L., Cao Y.;\nRT   \"Functional characterization of a conserved membrane protein, Pbs54,\nRT   involved in gamete fertilization in Plasmodium berghei.\";\nRL   Int. J. Parasitol. 54:99-107(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell projection, cilium, flagellum\nCC       {ECO:0000269|PubMed:37774810}. Cell membrane\nCC       {ECO:0000269|PubMed:37774810}; Multi-pass membrane protein\nCC       {ECO:0000255}. Note=In male gametes, localizes to the flagella and\nCC       residual body; in female gametes, localizes to the plasma membrane. In\nCC       ookinetes, localizes to the plasma membrane.\nCC       {ECO:0000269|PubMed:37774810}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0031514; C:motile cilium; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005774\nname: vacuolar membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the vacuole and separating its contents from the cytoplasm of the cell.\" [GOC:ai]\nis_a: GO:0098588 ! bounding membrane of organelle\nrelationship: part_of GO:0005773 ! vacuole\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005774",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59354-59361",
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
  "excerpt": "[Term]\nid: GO:0005819\nname: spindle\nnamespace: cellular_component\ndef: \"The array of microtubules and associated molecules that forms between opposite poles of a eukaryotic cell during mitosis or meiosis and serves to move the duplicated chromosomes apart.\" [ISBN:0198547684]\nxref: Wikipedia:Spindle_apparatus\nis_a: GO:0043232 ! intracellular membraneless organelle\nrelationship: part_of GO:0015630 ! microtubule cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005819",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59855-59863",
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

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0020008\nname: rhoptry\nnamespace: cellular_component\ndef: \"A large, club-shaped secretory organelle that forms part of the apical complex of an apicomplexan parasite, and consists of a bulbous body and a narrow electron-dense neck that extends through the conoid at the apical tip of the parasite. The rhoptry necks serve as ducts through which the contents of the rhoptries are secreted after attachment to the host has been completed and at the commencement of invasion. Rhoptry proteins function in the biogenesis and host organellar association of the parasitophorous vacuole.\" [ISBN:0521664470, PMID:11801218, PMID:16002398]\nsynonym: \"paired organelles\" RELATED []\nsynonym: \"toxoneme\" RELATED []\nxref: Wikipedia:Rhoptry\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0020007 ! apical complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020008",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155180-155190",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
