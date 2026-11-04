# pathway_0133

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0133.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAATDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNDMGCFTYPLVPGFETVGTATEVGSKVTKVKVGDKVAVGIMVGSCGKCDECVNDRECYCPEVITSYGRIDHDGTPTYGGFSSETVANEKFVFCFPEKLPMAAGAPLLNAGVSVYSAMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSTSKKGEAINDLGADAFLVSTDAEQMQAGSGTLDGILDTVPVVHPIEALLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVVSTIGGSTKETQEMLDFAAEHDITASVEIIPMDYVNTAMERIEKGDVRYRFVIDIGNTLTPPES

[Multiple Choices]
A. Alkaloid biosynthesis
B. 5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis. .
C. Cell wall degradation
D. terpenoid biosynthesis. .
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

> The sequence-matched UniProt records annotate this protein to alkaloid biosynthesis, specifically ajmaline biosynthesis. The pathway annotation cites experimental evidence, though the cited studies were not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's specific biochemical role—its pathway substrate and connection to alkaloid rather than terpenoid biosynthesis—is not supplied in the sequence or choices.


**Reason**

> The sequence is consistent with a soluble reductase, but generic enzyme-family or cofactor-binding features do not meaningfully distinguish alkaloid from terpenoid biosynthesis here. The pathway assignment depends on the specific biochemical role of this protein, rather than a pathway-specific cue evident from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source evidence supports alkaloid biosynthesis; the fact that ajmaline biosynthesis involves a monoterpenoid indole alkaloid does not make the broader terpenoid-biosynthesis option equally apt.


### Important caveats

- The source evidence is reviewer-only and was not available to the evaluated model.
- Sequence identity is established for the supplied sequence, but the cited primary studies were not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific biochemical role—its pathway substrate and connection to alkaloid rather than terpenoid biosynthesis—is not supplied in the sequence or choices.",
    "reason": "The sequence is consistent with a soluble reductase, but generic enzyme-family or cofactor-binding features do not meaningfully distinguish alkaloid from terpenoid biosynthesis here. The pathway assignment depends on the specific biochemical role of this protein, rather than a pathway-specific cue evident from the original input."
  },
  "case_id": "pathway_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate this protein to alkaloid biosynthesis, specifically ajmaline biosynthesis. The pathway annotation cites experimental evidence, though the cited studies were not independently reviewed here."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and was not available to the evaluated model.",
    "Sequence identity is established for the supplied sequence, but the cited primary studies were not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports alkaloid biosynthesis; the fact that ajmaline biosynthesis involves a monoterpenoid indole alkaloid does not make the broader terpenoid-biosynthesis option equally apt."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate this protein to alkaloid biosynthesis, specifically ajmaline biosynthesis. The pathway annotation cites experimental evidence, though the cited studies were not independently reviewed here.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's specific biochemical role—its pathway substrate and connection to alkaloid rather than terpenoid biosynthesis—is not supplied in the sequence or choices.",
    "reason": "The sequence is consistent with a soluble reductase, but generic enzyme-family or cofactor-binding features do not meaningfully distinguish alkaloid from terpenoid biosynthesis here. The pathway assignment depends on the specific biochemical role of this protein, rather than a pathway-specific cue evident from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports alkaloid biosynthesis; the fact that ajmaline biosynthesis involves a monoterpenoid indole alkaloid does not make the broader terpenoid-biosynthesis option equally apt."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and was not available to the evaluated model.",
    "Sequence identity is established for the supplied sequence, but the cited primary studies were not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (A0A0U3S9Q3, 1,2-Dihydrovomilenine reductase from Rauvolfia serpentina) explicitly annotates its pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence codes (ECO:0000269) from three independent PubMed references (12391554, 26715562, 38212296). The sequence matches the benchmark input exactly. Choice A (Alkaloid biosynthesis) is directly supported by the database annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains a zinc-binding motif (C-x-x-C clusters: 'GSCGKCDECVNDRECYCPE') and a Rossmann-fold NAD(P)-binding motif ('VGATMGSFELPILPLGVGRKSVVSTIGG'), identifying it as a CAD-like (cinnamyl alcohol dehydrogenase-like) reductase/dehydrogenase. In plants, this fold is associated with secondary metabolism. Among the four choices: (B) tRNA thio-modification enzymes use radical-SAM or other specialized architectures, not CAD-like reductase folds; (C) cell wall degradation enzymes are glycosidases/lyases with entirely different folds; (D) terpenoid biosynthesis primarily employs terpene synthases (class I/II folds) or cytochrome P450s, not CAD-like reductases. This leaves (A) alkaloid biosynthesis as the only pathway consistent with a plant reductase involved in secondary metabolism. Furthermore, family-level knowledge from Apocynaceae shows that CAD-like reductases have been repeatedly recruited for monoterpenoid indole alkaloid (MIA) biosynthesis in this plant family, providing a transferable pattern linking this fold to alkaloid pathways.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The enzyme fold (CAD-like reductase with zinc and NAD(P) binding sites) combined with general knowledge of plant secondary metabolism and the known recruitment of CAD-like enzymes for alkaloid biosynthesis in Apocynaceae provides a credible inference to distinguish A from B, C, and D. The distractors are eliminated by incompatible enzyme architectures.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different enzyme classes and pathways. The CAD-like reductase fold is incompatible with tRNA modification (B), cell wall degradation (C), or typical terpenoid biosynthesis (D). Alkaloid biosynthesis (A) is the only option consistent with a plant reductase in secondary metabolism.


### Important caveats

- The CAD-like fold is classically associated with lignin/phenylpropanoid biosynthesis; its recruitment to alkaloid biosynthesis is a family-level pattern specific to Apocynaceae and related families, which a model must have learned from multiple related proteins.
- Without the option 'lignin biosynthesis' present, the model must reason by elimination among the given choices rather than by direct positive identification of the CAD pathway.
- The reviewer-only evidence confirms experimental annotation (ECO:0000269), but the evaluated model only has the sequence and choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains a zinc-binding motif (C-x-x-C clusters: 'GSCGKCDECVNDRECYCPE') and a Rossmann-fold NAD(P)-binding motif ('VGATMGSFELPILPLGVGRKSVVSTIGG'), identifying it as a CAD-like (cinnamyl alcohol dehydrogenase-like) reductase/dehydrogenase. In plants, this fold is associated with secondary metabolism. Among the four choices: (B) tRNA thio-modification enzymes use radical-SAM or other specialized architectures, not CAD-like reductase folds; (C) cell wall degradation enzymes are glycosidases/lyases with entirely different folds; (D) terpenoid biosynthesis primarily employs terpene synthases (class I/II folds) or cytochrome P450s, not CAD-like reductases. This leaves (A) alkaloid biosynthesis as the only pathway consistent with a plant reductase involved in secondary metabolism. Furthermore, family-level knowledge from Apocynaceae shows that CAD-like reductases have been repeatedly recruited for monoterpenoid indole alkaloid (MIA) biosynthesis in this plant family, providing a transferable pattern linking this fold to alkaloid pathways.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The enzyme fold (CAD-like reductase with zinc and NAD(P) binding sites) combined with general knowledge of plant secondary metabolism and the known recruitment of CAD-like enzymes for alkaloid biosynthesis in Apocynaceae provides a credible inference to distinguish A from B, C, and D. The distractors are eliminated by incompatible enzyme architectures."
  },
  "case_id": "pathway_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A0U3S9Q3, 1,2-Dihydrovomilenine reductase from Rauvolfia serpentina) explicitly annotates its pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence codes (ECO:0000269) from three independent PubMed references (12391554, 26715562, 38212296). The sequence matches the benchmark input exactly. Choice A (Alkaloid biosynthesis) is directly supported by the database annotation."
  },
  "important_caveats": [
    "The CAD-like fold is classically associated with lignin/phenylpropanoid biosynthesis; its recruitment to alkaloid biosynthesis is a family-level pattern specific to Apocynaceae and related families, which a model must have learned from multiple related proteins.",
    "Without the option 'lignin biosynthesis' present, the model must reason by elimination among the given choices rather than by direct positive identification of the CAD pathway.",
    "The reviewer-only evidence confirms experimental annotation (ECO:0000269), but the evaluated model only has the sequence and choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes and pathways. The CAD-like reductase fold is incompatible with tRNA modification (B), cell wall degradation (C), or typical terpenoid biosynthesis (D). Alkaloid biosynthesis (A) is the only option consistent with a plant reductase in secondary metabolism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A0U3S9Q3, 1,2-Dihydrovomilenine reductase from Rauvolfia serpentina) explicitly annotates its pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence codes (ECO:0000269) from three independent PubMed references (12391554, 26715562, 38212296). The sequence matches the benchmark input exactly. Choice A (Alkaloid biosynthesis) is directly supported by the database annotation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains a zinc-binding motif (C-x-x-C clusters: 'GSCGKCDECVNDRECYCPE') and a Rossmann-fold NAD(P)-binding motif ('VGATMGSFELPILPLGVGRKSVVSTIGG'), identifying it as a CAD-like (cinnamyl alcohol dehydrogenase-like) reductase/dehydrogenase. In plants, this fold is associated with secondary metabolism. Among the four choices: (B) tRNA thio-modification enzymes use radical-SAM or other specialized architectures, not CAD-like reductase folds; (C) cell wall degradation enzymes are glycosidases/lyases with entirely different folds; (D) terpenoid biosynthesis primarily employs terpene synthases (class I/II folds) or cytochrome P450s, not CAD-like reductases. This leaves (A) alkaloid biosynthesis as the only pathway consistent with a plant reductase involved in secondary metabolism. Furthermore, family-level knowledge from Apocynaceae shows that CAD-like reductases have been repeatedly recruited for monoterpenoid indole alkaloid (MIA) biosynthesis in this plant family, providing a transferable pattern linking this fold to alkaloid pathways.",
    "missing_item_specific_fact": "",
    "reason": "The enzyme fold (CAD-like reductase with zinc and NAD(P) binding sites) combined with general knowledge of plant secondary metabolism and the known recruitment of CAD-like enzymes for alkaloid biosynthesis in Apocynaceae provides a credible inference to distinguish A from B, C, and D. The distractors are eliminated by incompatible enzyme architectures."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes and pathways. The CAD-like reductase fold is incompatible with tRNA modification (B), cell wall degradation (C), or typical terpenoid biosynthesis (D). Alkaloid biosynthesis (A) is the only option consistent with a plant reductase in secondary metabolism."
  },
  "important_caveats": [
    "The CAD-like fold is classically associated with lignin/phenylpropanoid biosynthesis; its recruitment to alkaloid biosynthesis is a family-level pattern specific to Apocynaceae and related families, which a model must have learned from multiple related proteins.",
    "Without the option 'lignin biosynthesis' present, the model must reason by elimination among the given choices rather than by direct positive identification of the CAD pathway.",
    "The reviewer-only evidence confirms experimental annotation (ECO:0000269), but the evaluated model only has the sequence and choices."
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
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0U3S9Q3",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "selected_historical_version": {
    "accession": "A0A0U3S9Q3",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHVOR_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U3S9Q3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Protein RR4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsRR4\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsVR2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.73\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"1,2-Dihydrovomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsDHVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis; ajmaline biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Geissler M.\",\"Burghard M.\",\"Volk J.\",\"Staniek A.\",\"Warzecha H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26715562\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00425-015-2446-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"813\",\"id\":\"26715562\",\"journal\":\"Planta\",\"lastPage\":\"824\",\"publicationDate\":\"2016\",\"title\":\"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\",\"volume\":\"243\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ALW82981.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1)\",\"PROTEIN SEQUENCE OF 5-13 AND 298-308\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61918.1\",\"source\":\"EMBL\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Gao S.\",\"von Schumann G.\",\"Stoeckigt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12391554\"},{\"database\":\"DOI\",\"id\":\"10.1055/s-2002-34935\"}],\"citationType\":\"journal article\",\"firstPage\":\"906\",\"id\":\"12391554\",\"journal\":\"Planta Med.\",\"lastPage\":\"911\",\"publicationDate\":\"2002\",\"title\":\"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis of the antiarrhythmic alkaloid ajmaline.\",\"volume\":\"68\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   DHVOR_RAUSE             Reviewed;         363 AA.\nAC   A0A0U3S9Q3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};\nDE            Short=RsDHVR {ECO:0000303|PubMed:26715562};\nDE            EC=1.3.1.73 {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=Protein RR4 {ECO:0000303|PubMed:26715562};\nDE            Short=RsRR4 {ECO:0000303|PubMed:26715562};\nDE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RsVR2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296};\nGN   Name=DHVR {ECO:0000303|PubMed:26715562};\nGN   Synonyms=RR4 {ECO:0000303|PubMed:26715562},\nGN   VR2 {ECO:0000303|PubMed:26715562};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ALW82981.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1), PROTEIN SEQUENCE OF 5-13 AND\nRP   298-308, FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=26715562; DOI=10.1007/s00425-015-2446-6;\nRA   Geissler M., Burghard M., Volk J., Staniek A., Warzecha H.;\nRT   \"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to\nRT   the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\";\nRL   Planta 243:813-824(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:WKU61918.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRX   PubMed=12391554; DOI=10.1055/s-2002-34935;\nRA   Gao S., von Schumann G., Stoeckigt J.;\nRT   \"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis\nRT   of the antiarrhythmic alkaloid ajmaline.\";\nRL   Planta Med. 68:906-911(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H5",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.\nCC       {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:26715562,\nCC       ECO:0000269|PubMed:38212296}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
