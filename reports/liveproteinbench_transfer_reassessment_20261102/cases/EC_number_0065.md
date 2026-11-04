# EC_number_0065

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0065.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.3.1.36

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGESTQVDLSVKAIGWGAKDASGILHPIKFSRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVVEVGSKVQKFKVGDKVAVGCMVGSCGKCYNCENGMENYCPEPNMADGSVYREQGERSYGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGVVVYSPMKYMGLDKPGKHIGVFGLGGLGSVAVKFIKAFGGKATVISTSRRKEKEAIEEHGADAFVVNSDTEQLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGSLILVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQEMLDFAAKHNILCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYEE

[Multiple Choices]
A. 1.3.1.73
B. 3.6.1.5
C. 2.1.1.393
D. 1.3.1.36
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

> The sequence matches the cited UniProt record, which assigns EC 1.3.1.36 and annotates the catalytic activity with experimental evidence (ECO:0000269). The annotated reaction supports the keyed EC number, though the primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has features consistent with a cofactor-dependent oxidoreductase, which makes the oxidoreductase choices more plausible than the hydrolase or methyltransferase choices. But A and D are both EC 1.3.1 enzymes, so this broad family-level inference does not distinguish them.


**Missing item-specific fact**

> The specific substrate reaction catalyzed by this protein, needed to distinguish EC 1.3.1.36 from EC 1.3.1.73.


**Reason**

> The sequence offers a credible broad redox-enzyme inference, but the decisive distinction between the two oxidoreductase options is substrate-specific activity. No original context or sufficiently specific transferable family feature establishes that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports one assigned EC number; the limitation is that the original sequence and choices do not provide a clear way to infer its substrate-specific activity, not that the alternatives are equivalent.


### Important caveats

- The reviewer-only evidence reports a sequence match and experimental-evidence codes, but the cited primary publication was not independently validated.
- The actual source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a cofactor-dependent oxidoreductase, which makes the oxidoreductase choices more plausible than the hydrolase or methyltransferase choices. But A and D are both EC 1.3.1 enzymes, so this broad family-level inference does not distinguish them.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate reaction catalyzed by this protein, needed to distinguish EC 1.3.1.36 from EC 1.3.1.73.",
    "reason": "The sequence offers a credible broad redox-enzyme inference, but the decisive distinction between the two oxidoreductase options is substrate-specific activity. No original context or sufficiently specific transferable family feature establishes that distinction."
  },
  "case_id": "EC_number_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which assigns EC 1.3.1.36 and annotates the catalytic activity with experimental evidence (ECO:0000269). The annotated reaction supports the keyed EC number, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only evidence reports a sequence match and experimental-evidence codes, but the cited primary publication was not independently validated.",
    "The actual source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one assigned EC number; the limitation is that the original sequence and choices do not provide a clear way to infer its substrate-specific activity, not that the alternatives are equivalent."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which assigns EC 1.3.1.36 and annotates the catalytic activity with experimental evidence (ECO:0000269). The annotated reaction supports the keyed EC number, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has features consistent with a cofactor-dependent oxidoreductase, which makes the oxidoreductase choices more plausible than the hydrolase or methyltransferase choices. But A and D are both EC 1.3.1 enzymes, so this broad family-level inference does not distinguish them.",
    "missing_item_specific_fact": "The specific substrate reaction catalyzed by this protein, needed to distinguish EC 1.3.1.36 from EC 1.3.1.73.",
    "reason": "The sequence offers a credible broad redox-enzyme inference, but the decisive distinction between the two oxidoreductase options is substrate-specific activity. No original context or sufficiently specific transferable family feature establishes that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one assigned EC number; the limitation is that the original sequence and choices do not provide a clear way to infer its substrate-specific activity, not that the alternatives are equivalent."
  },
  "important_caveats": [
    "The reviewer-only evidence reports a sequence match and experimental-evidence codes, but the cited primary publication was not independently validated.",
    "The actual source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A9E7LUR3) annotates this protein as Geissoschizine synthase with EC 1.3.1.36, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic activity (19E-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH) is explicitly assigned to EC 1.3.1.36. The sequence matches exactly (SHA256 confirmed). The annotation is experimental, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GGLGSVAVK at ~position 170) and SDR-family catalytic features (YxxxN pattern near 'YGGCSN', and SxxxK-type residues in the C-terminal region). This immediately eliminates B (EC 3.6.1.5, a hydrolase acting on acid anhydrides) and C (EC 2.1.1.393, a methyltransferase), as neither would possess a Rossmann-fold oxidoreductase architecture. Between the two remaining 1.3.1.x options: EC 1.3.1.73 corresponds to a mitochondrial fatty-acid-pathway dehydrogenase (typically ~280-300 aa, NAD+-dependent, with a conserved Arg in the Rossmann fold for NAD+ 2'-OH discrimination and a narrow acyl-CoA channel). The supplied sequence is 364 aa, lacks a mitochondrial targeting peptide, shows no conserved NAD+-specific Arg in the GxGxxG region (suggesting NADP+ preference), and has a larger domain architecture consistent with plant specialized-metabolism SDRs involved in monoterpene indole alkaloid (MIA) biosynthesis. Transferable knowledge from other plant SDRs in the strictosidine/MIA pathway (e.g., from Catharanthus, Rauvolfia) supports recognizing this as a plant alkaloid-pathway oxidoreductase rather than a mitochondrial beta-oxidation enzyme, favoring D (1.3.1.36) over A (1.3.1.73).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold SDR architecture eliminates the hydrolase and transferase options unambiguously. The remaining A-vs-D distinction is supported by family-level inference: the sequence length, absence of mitochondrial targeting, apparent NADP+ preference, and overall SDR subfamily architecture align with plant MIA-biosynthesis SDRs (known from other Apocynaceae/Rubiaceae proteins) rather than mitochondrial fatty-acid dehydrogenases. This is a defensible probabilistic generalization from related proteins, not a lookup of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While both A and D fall in EC 1.3.1.x, the sequence-level features (size, cofactor preference pattern, absence of mitochondrial targeting, SDR subfamily architecture) provide a meaningful basis to favor D over A. B and C are clearly eliminated by the oxidoreductase fold. No two options are genuinely indistinguishable given the available evidence.


### Important caveats

- The distinction between EC 1.3.1.36 and EC 1.3.1.73 relies on family-level inference and probabilistic generalization from other plant SDRs; it is not a deductive proof from first principles.
- The exact identity of EC 1.3.1.73 was inferred from general EC classification knowledge; if it refers to a different enzyme than a mitochondrial fatty-acid dehydrogenase, the argument would need adjustment.
- The UniProt annotation is experimental (ECO:0000269), strengthening the expected-answer support, but the model's reasoning path relies on sequence-level family recognition rather than the annotation itself.
- The reviewer-only evidence confirms sequence match and experimental annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GGLGSVAVK at ~position 170) and SDR-family catalytic features (YxxxN pattern near 'YGGCSN', and SxxxK-type residues in the C-terminal region). This immediately eliminates B (EC 3.6.1.5, a hydrolase acting on acid anhydrides) and C (EC 2.1.1.393, a methyltransferase), as neither would possess a Rossmann-fold oxidoreductase architecture. Between the two remaining 1.3.1.x options: EC 1.3.1.73 corresponds to a mitochondrial fatty-acid-pathway dehydrogenase (typically ~280-300 aa, NAD+-dependent, with a conserved Arg in the Rossmann fold for NAD+ 2'-OH discrimination and a narrow acyl-CoA channel). The supplied sequence is 364 aa, lacks a mitochondrial targeting peptide, shows no conserved NAD+-specific Arg in the GxGxxG region (suggesting NADP+ preference), and has a larger domain architecture consistent with plant specialized-metabolism SDRs involved in monoterpene indole alkaloid (MIA) biosynthesis. Transferable knowledge from other plant SDRs in the strictosidine/MIA pathway (e.g., from Catharanthus, Rauvolfia) supports recognizing this as a plant alkaloid-pathway oxidoreductase rather than a mitochondrial beta-oxidation enzyme, favoring D (1.3.1.36) over A (1.3.1.73).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold SDR architecture eliminates the hydrolase and transferase options unambiguously. The remaining A-vs-D distinction is supported by family-level inference: the sequence length, absence of mitochondrial targeting, apparent NADP+ preference, and overall SDR subfamily architecture align with plant MIA-biosynthesis SDRs (known from other Apocynaceae/Rubiaceae proteins) rather than mitochondrial fatty-acid dehydrogenases. This is a defensible probabilistic generalization from related proteins, not a lookup of this specific entry's annotation."
  },
  "case_id": "EC_number_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7LUR3) annotates this protein as Geissoschizine synthase with EC 1.3.1.36, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic activity (19E-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH) is explicitly assigned to EC 1.3.1.36. The sequence matches exactly (SHA256 confirmed). The annotation is experimental, not merely computational."
  },
  "important_caveats": [
    "The distinction between EC 1.3.1.36 and EC 1.3.1.73 relies on family-level inference and probabilistic generalization from other plant SDRs; it is not a deductive proof from first principles.",
    "The exact identity of EC 1.3.1.73 was inferred from general EC classification knowledge; if it refers to a different enzyme than a mitochondrial fatty-acid dehydrogenase, the argument would need adjustment.",
    "The UniProt annotation is experimental (ECO:0000269), strengthening the expected-answer support, but the model's reasoning path relies on sequence-level family recognition rather than the annotation itself.",
    "The reviewer-only evidence confirms sequence match and experimental annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both A and D fall in EC 1.3.1.x, the sequence-level features (size, cofactor preference pattern, absence of mitochondrial targeting, SDR subfamily architecture) provide a meaningful basis to favor D over A. B and C are clearly eliminated by the oxidoreductase fold. No two options are genuinely indistinguishable given the available evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7LUR3) annotates this protein as Geissoschizine synthase with EC 1.3.1.36, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic activity (19E-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH) is explicitly assigned to EC 1.3.1.36. The sequence matches exactly (SHA256 confirmed). The annotation is experimental, not merely computational.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GGLGSVAVK at ~position 170) and SDR-family catalytic features (YxxxN pattern near 'YGGCSN', and SxxxK-type residues in the C-terminal region). This immediately eliminates B (EC 3.6.1.5, a hydrolase acting on acid anhydrides) and C (EC 2.1.1.393, a methyltransferase), as neither would possess a Rossmann-fold oxidoreductase architecture. Between the two remaining 1.3.1.x options: EC 1.3.1.73 corresponds to a mitochondrial fatty-acid-pathway dehydrogenase (typically ~280-300 aa, NAD+-dependent, with a conserved Arg in the Rossmann fold for NAD+ 2'-OH discrimination and a narrow acyl-CoA channel). The supplied sequence is 364 aa, lacks a mitochondrial targeting peptide, shows no conserved NAD+-specific Arg in the GxGxxG region (suggesting NADP+ preference), and has a larger domain architecture consistent with plant specialized-metabolism SDRs involved in monoterpene indole alkaloid (MIA) biosynthesis. Transferable knowledge from other plant SDRs in the strictosidine/MIA pathway (e.g., from Catharanthus, Rauvolfia) supports recognizing this as a plant alkaloid-pathway oxidoreductase rather than a mitochondrial beta-oxidation enzyme, favoring D (1.3.1.36) over A (1.3.1.73).",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold SDR architecture eliminates the hydrolase and transferase options unambiguously. The remaining A-vs-D distinction is supported by family-level inference: the sequence length, absence of mitochondrial targeting, apparent NADP+ preference, and overall SDR subfamily architecture align with plant MIA-biosynthesis SDRs (known from other Apocynaceae/Rubiaceae proteins) rather than mitochondrial fatty-acid dehydrogenases. This is a defensible probabilistic generalization from related proteins, not a lookup of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both A and D fall in EC 1.3.1.x, the sequence-level features (size, cofactor preference pattern, absence of mitochondrial targeting, SDR subfamily architecture) provide a meaningful basis to favor D over A. B and C are clearly eliminated by the oxidoreductase fold. No two options are genuinely indistinguishable given the available evidence."
  },
  "important_caveats": [
    "The distinction between EC 1.3.1.36 and EC 1.3.1.73 relies on family-level inference and probabilistic generalization from other plant SDRs; it is not a deductive proof from first principles.",
    "The exact identity of EC 1.3.1.73 was inferred from general EC classification knowledge; if it refers to a different enzyme than a mitochondrial fatty-acid dehydrogenase, the argument would need adjustment.",
    "The UniProt annotation is experimental (ECO:0000269), strengthening the expected-answer support, but the model's reasoning path relies on sequence-level family recognition rather than the annotation itself.",
    "The reviewer-only evidence confirms sequence match and experimental annotation but was not available to the evaluated model."
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
  "benchmark_sequence_length": 364,
  "benchmark_sequence_sha256": "6b2d31d337a1bc9f1e5478cf9eeafb327d5b0429e737e3aae6290d6c0ee2da2e",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 364,
  "current_source_sequence_sha256": "6b2d31d337a1bc9f1e5478cf9eeafb327d5b0429e737e3aae6290d6c0ee2da2e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7LUR3",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "selected_historical_source_sequence_length": 364,
  "selected_historical_source_sequence_sha256": "6b2d31d337a1bc9f1e5478cf9eeafb327d5b0429e737e3aae6290d6c0ee2da2e",
  "selected_historical_version": {
    "accession": "A0A9E7LUR3",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GS_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7LUR3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Alcohol dehydrogenase GS\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Geissoschizine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsGS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:11378\"}}],\"reaction\":{\"ecNumber\":\"1.3.1.36\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"name\":\"(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:11376\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17037\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17294\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:83840\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"name\":\"(19E)-geissoschizine + NADPH + H(+) = (16R,19E)-isositsirikine + NADP(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83839\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17037\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70508\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:83844\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"name\":\"(19E)-geissoschizine + NADPH + H(+) = (16R,19Z)-isositsirikine + NADP(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83843\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17037\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:233403\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65381.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:11.087134+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   GS_ALSSC                Reviewed;         364 AA.\nAC   A0A9E7LUR3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:36349266};\nDE            Short=AsGS {ECO:0000303|PubMed:36349266};\nDE            EC=1.3.1.36 {ECO:0000269|PubMed:36349266};\nDE   AltName: Full=Alcohol dehydrogenase GS {ECO:0000305};\nGN   Name=GS {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:36349266};\nDE            Short=AsGS {ECO:0000303|PubMed:36349266};\nDE            EC=1.3.1.36 {ECO:0000269|PubMed:36349266};\nDE   AltName: Full=Alcohol dehydrogenase GS {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65381.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine +\nCC         NADPH; Xref=Rhea:RHEA:11376, ChEBI:CHEBI:17037, ChEBI:CHEBI:17294,\nCC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.3.1.36;\nCC         Evidence={ECO:0000269|PubMed:36349266};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:11378;\nCC         Evidence={ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(19E)-geissoschizine + NADPH + H(+) = (16R,19E)-isositsirikine\nCC         + NADP(+); Xref=Rhea:RHEA:83839, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:17037, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,\nCC         ChEBI:CHEBI:70508; Evidence={ECO:0000269|PubMed:36349266};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83840;\nCC         Evidence={ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(19E)-geissoschizine + NADPH + H(+) = (16R,19Z)-isositsirikine\nCC         + NADP(+); Xref=Rhea:RHEA:83843, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:17037, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,\nCC         ChEBI:CHEBI:233403; Evidence={ECO:0000269|PubMed:36349266};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83844;\nCC         Evidence={ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:15.563182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 65. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
