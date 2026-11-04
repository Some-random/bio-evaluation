# pathway_0110

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0110.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKQVQIPEIELNSGHKMPLVGFGTCVPDPIPPLEELAGIFLEAIKVGYRHFDTASSYGTEEALGRAVAQAIETGLVNGREEFFISSKLWCEDADLDLILPALKKTLGNMGLDYLDLSMIHMPVRVRKGAEMFNYTKEDLLPFDIQGTWKAMEECNKLGLAKSIGVSNYSCEKLTKLLENATVPPAVNQVEMNVVWQQRKLLPFCKEKNIHVTAWSPLLSYGAVWGSNAVMENPILVEIAASKNKTVAQVALRWIYEQGASFIMRTFNKDRMFENVQIFDWELTKEELDKIQKIPQRRGTLGEDFIHPEGPIKSVEDLWDGDL

[Multiple Choices]
A. Capsule biogenesis
B. Lipid metabolism. .
C. Alkaloid biosynthesis. .
D. L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9. .
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

> The matched sequence has a UniProt pathway annotation of alkaloid biosynthesis with experimental-evidence code ECO:0000269; the historical entry gives the same annotation. The cited evidence supports the key, though the underlying study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The exact enzyme’s substrate and pathway role, which identify it as participating in alkaloid biosynthesis.


**Reason**

> The sequence may support an inference that this is a soluble metabolic enzyme, but it provides no clear pathway-specific feature that meaningfully separates alkaloid biosynthesis from the other metabolic options. A generic enzyme-family or catalytic-class inference would not establish the relevant pathway; the specific enzyme–substrate assignment is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports C as the annotated pathway. The sequence alone makes the choice difficult, but that lack of answerability does not establish another pathway as a defensible biological answer.


### Important caveats

- The pathway annotation is experimentally evidence-coded and sequence-matched, but the cited primary study was not independently checked.
- The organism and target-specific annotation were reviewer-only information, not original inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact enzyme’s substrate and pathway role, which identify it as participating in alkaloid biosynthesis.",
    "reason": "The sequence may support an inference that this is a soluble metabolic enzyme, but it provides no clear pathway-specific feature that meaningfully separates alkaloid biosynthesis from the other metabolic options. A generic enzyme-family or catalytic-class inference would not establish the relevant pathway; the specific enzyme–substrate assignment is needed."
  },
  "case_id": "pathway_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt pathway annotation of alkaloid biosynthesis with experimental-evidence code ECO:0000269; the historical entry gives the same annotation. The cited evidence supports the key, though the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The pathway annotation is experimentally evidence-coded and sequence-matched, but the cited primary study was not independently checked.",
    "The organism and target-specific annotation were reviewer-only information, not original inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C as the annotated pathway. The sequence alone makes the choice difficult, but that lack of answerability does not establish another pathway as a defensible biological answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt pathway annotation of alkaloid biosynthesis with experimental-evidence code ECO:0000269; the historical entry gives the same annotation. The cited evidence supports the key, though the underlying study was not independently reviewed here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The exact enzyme’s substrate and pathway role, which identify it as participating in alkaloid biosynthesis.",
    "reason": "The sequence may support an inference that this is a soluble metabolic enzyme, but it provides no clear pathway-specific feature that meaningfully separates alkaloid biosynthesis from the other metabolic options. A generic enzyme-family or catalytic-class inference would not establish the relevant pathway; the specific enzyme–substrate assignment is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C as the annotated pathway. The sequence alone makes the choice difficult, but that lack of answerability does not establish another pathway as a defensible biological answer."
  },
  "important_caveats": [
    "The pathway annotation is experimentally evidence-coded and sequence-matched, but the cited primary study was not independently checked.",
    "The organism and target-specific annotation were reviewer-only information, not original inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7S518 (Rhazimal reductase 1, EC 1.1.1.440, from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 from PubMed:36349266 (Wang et al., Chem. Sci. 2022). The enzyme catalyzes a reduction step in the monoterpene indole alkaloid (MIA) biosynthetic pathway. The sequence in the question matches the source entry exactly (323 AA, SHA256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (323 AA) shows features of a plant protein (amino acid composition, absence of bacterial-specific motifs) with an SDR/oxidoreductase-like fold: a 'GFGTCVPD' Rossmann-type NAD(P)-binding motif, a 'GAVWGS' glycine-rich region, and potential catalytic Tyr-Gly residues. (1) Capsule biogenesis (A) involves bacterial glycosyltransferases, polymerases, and transporters — incompatible with an SDR fold and a plant-type sequence. (2) Histidine biosynthesis from PRPP (D) involves ATP phosphoribosyltransferase, pyrophosphatases, cyclohydrolases, and isomerases — none are SDR-type reductases, and the sequence lacks any match to these enzyme classes. (3) Lipid metabolism (B): while some plant reductases participate in lipid biosynthesis (e.g., 3-ketoacyl-ACP reductase), those specific SDR subfamilies carry distinctive substrate-binding motifs (e.g., the 'DD' motif in the NAD-binding cleft of KCR). The observed sequence lacks these lipid-specific subfamily signatures. (4) Plant SDR enzymes are statistically enriched in secondary metabolism (terpenoid/alkaloid/phenylpropanoid pathways) rather than primary lipid metabolism. The combination of plant origin + SDR fold + absence of lipid-metabolism-specific motifs + enrichment of plant SDRs in secondary metabolism provides a probabilistic but meaningful argument favoring alkaloid biosynthesis (C) over the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of A and D rests on well-established pathway-enzyme-class incompatibility (capsule enzymes are not SDRs; histidine pathway enzymes are not SDRs) and plant-vs-bacterial context. The B-vs-C distinction is probabilistic: the SDR fold without lipid-specific subfamily motifs, combined with the statistical predominance of plant SDRs in secondary metabolism, provides a transferable (though not deterministic) argument favoring alkaloid biosynthesis. A knowledgeable model can meaningfully narrow to C without recalling this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are eliminated by enzyme-class and organismal-context arguments. Option B is weakened by the absence of lipid-metabolism-specific SDR subfamily motifs. While the B-vs-C distinction is probabilistic rather than absolute, the available sequence features and family-level knowledge provide a meaningful preference for C. No two options are equally defensible given the sequence evidence.


### Important caveats

- The B-vs-C distinction relies on a statistical/family-level tendency (plant SDRs enriched in secondary metabolism) rather than a definitive sequence motif unique to alkaloid pathway enzymes.
- The protein was only annotated in UniProt as recently as June 2025 (first public date); a model trained on earlier data might not have encountered this specific enzyme, but the reasoning does not depend on memorizing this entry.
- The SDR superfamily is extremely large and diverse; the argument that this particular SDR is not a lipid-metabolism enzyme is based on absence of specific subfamily motifs rather than positive identification of an alkaloid-pathway motif.
- The reviewer-only evidence confirms experimental (ECO:0000269) pathway assignment from a 2022 publication, but this information was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (323 AA) shows features of a plant protein (amino acid composition, absence of bacterial-specific motifs) with an SDR/oxidoreductase-like fold: a 'GFGTCVPD' Rossmann-type NAD(P)-binding motif, a 'GAVWGS' glycine-rich region, and potential catalytic Tyr-Gly residues. (1) Capsule biogenesis (A) involves bacterial glycosyltransferases, polymerases, and transporters — incompatible with an SDR fold and a plant-type sequence. (2) Histidine biosynthesis from PRPP (D) involves ATP phosphoribosyltransferase, pyrophosphatases, cyclohydrolases, and isomerases — none are SDR-type reductases, and the sequence lacks any match to these enzyme classes. (3) Lipid metabolism (B): while some plant reductases participate in lipid biosynthesis (e.g., 3-ketoacyl-ACP reductase), those specific SDR subfamilies carry distinctive substrate-binding motifs (e.g., the 'DD' motif in the NAD-binding cleft of KCR). The observed sequence lacks these lipid-specific subfamily signatures. (4) Plant SDR enzymes are statistically enriched in secondary metabolism (terpenoid/alkaloid/phenylpropanoid pathways) rather than primary lipid metabolism. The combination of plant origin + SDR fold + absence of lipid-metabolism-specific motifs + enrichment of plant SDRs in secondary metabolism provides a probabilistic but meaningful argument favoring alkaloid biosynthesis (C) over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and D rests on well-established pathway-enzyme-class incompatibility (capsule enzymes are not SDRs; histidine pathway enzymes are not SDRs) and plant-vs-bacterial context. The B-vs-C distinction is probabilistic: the SDR fold without lipid-specific subfamily motifs, combined with the statistical predominance of plant SDRs in secondary metabolism, provides a transferable (though not deterministic) argument favoring alkaloid biosynthesis. A knowledgeable model can meaningfully narrow to C without recalling this exact protein's database entry."
  },
  "case_id": "pathway_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S518 (Rhazimal reductase 1, EC 1.1.1.440, from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 from PubMed:36349266 (Wang et al., Chem. Sci. 2022). The enzyme catalyzes a reduction step in the monoterpene indole alkaloid (MIA) biosynthetic pathway. The sequence in the question matches the source entry exactly (323 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The B-vs-C distinction relies on a statistical/family-level tendency (plant SDRs enriched in secondary metabolism) rather than a definitive sequence motif unique to alkaloid pathway enzymes.",
    "The protein was only annotated in UniProt as recently as June 2025 (first public date); a model trained on earlier data might not have encountered this specific enzyme, but the reasoning does not depend on memorizing this entry.",
    "The SDR superfamily is extremely large and diverse; the argument that this particular SDR is not a lipid-metabolism enzyme is based on absence of specific subfamily motifs rather than positive identification of an alkaloid-pathway motif.",
    "The reviewer-only evidence confirms experimental (ECO:0000269) pathway assignment from a 2022 publication, but this information was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are eliminated by enzyme-class and organismal-context arguments. Option B is weakened by the absence of lipid-metabolism-specific SDR subfamily motifs. While the B-vs-C distinction is probabilistic rather than absolute, the available sequence features and family-level knowledge provide a meaningful preference for C. No two options are equally defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S518 (Rhazimal reductase 1, EC 1.1.1.440, from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 from PubMed:36349266 (Wang et al., Chem. Sci. 2022). The enzyme catalyzes a reduction step in the monoterpene indole alkaloid (MIA) biosynthetic pathway. The sequence in the question matches the source entry exactly (323 AA, SHA256 confirmed).",
    "evidence_ids": ["C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (323 AA) shows features of a plant protein (amino acid composition, absence of bacterial-specific motifs) with an SDR/oxidoreductase-like fold: a 'GFGTCVPD' Rossmann-type NAD(P)-binding motif, a 'GAVWGS' glycine-rich region, and potential catalytic Tyr-Gly residues. (1) Capsule biogenesis (A) involves bacterial glycosyltransferases, polymerases, and transporters — incompatible with an SDR fold and a plant-type sequence. (2) Histidine biosynthesis from PRPP (D) involves ATP phosphoribosyltransferase, pyrophosphatases, cyclohydrolases, and isomerases — none are SDR-type reductases, and the sequence lacks any match to these enzyme classes. (3) Lipid metabolism (B): while some plant reductases participate in lipid biosynthesis (e.g., 3-ketoacyl-ACP reductase), those specific SDR subfamilies carry distinctive substrate-binding motifs (e.g., the 'DD' motif in the NAD-binding cleft of KCR). The observed sequence lacks these lipid-specific subfamily signatures. (4) Plant SDR enzymes are statistically enriched in secondary metabolism (terpenoid/alkaloid/phenylpropanoid pathways) rather than primary lipid metabolism. The combination of plant origin + SDR fold + absence of lipid-metabolism-specific motifs + enrichment of plant SDRs in secondary metabolism provides a probabilistic but meaningful argument favoring alkaloid biosynthesis (C) over the other three options.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and D rests on well-established pathway-enzyme-class incompatibility (capsule enzymes are not SDRs; histidine pathway enzymes are not SDRs) and plant-vs-bacterial context. The B-vs-C distinction is probabilistic: the SDR fold without lipid-specific subfamily motifs, combined with the statistical predominance of plant SDRs in secondary metabolism, provides a transferable (though not deterministic) argument favoring alkaloid biosynthesis. A knowledgeable model can meaningfully narrow to C without recalling this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are eliminated by enzyme-class and organismal-context arguments. Option B is weakened by the absence of lipid-metabolism-specific SDR subfamily motifs. While the B-vs-C distinction is probabilistic rather than absolute, the available sequence features and family-level knowledge provide a meaningful preference for C. No two options are equally defensible given the sequence evidence."
  },
  "important_caveats": [
    "The B-vs-C distinction relies on a statistical/family-level tendency (plant SDRs enriched in secondary metabolism) rather than a definitive sequence motif unique to alkaloid pathway enzymes.",
    "The protein was only annotated in UniProt as recently as June 2025 (first public date); a model trained on earlier data might not have encountered this specific enzyme, but the reasoning does not depend on memorizing this entry.",
    "The SDR superfamily is extremely large and diverse; the argument that this particular SDR is not a lipid-metabolism enzyme is based on absence of specific subfamily motifs rather than positive identification of an alkaloid-pathway motif.",
    "The reviewer-only evidence confirms experimental (ECO:0000269) pathway assignment from a 2022 publication, but this information was not available to the evaluated model."
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
  "benchmark_sequence_length": 323,
  "benchmark_sequence_sha256": "016d2556a5540f503b5f5d1c251aaf15f9f522ff3142edec17aaac977d884675",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 323,
  "current_source_sequence_sha256": "016d2556a5540f503b5f5d1c251aaf15f9f522ff3142edec17aaac977d884675",
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
  "requested_accession": "A0A9E7S518",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "selected_historical_source_sequence_length": 323,
  "selected_historical_source_sequence_sha256": "016d2556a5540f503b5f5d1c251aaf15f9f522ff3142edec17aaac977d884675",
  "selected_historical_version": {
    "accession": "A0A9E7S518",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RHR1_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7S518\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.440\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Rhazimal reductase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsRHR1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65385.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   RHR1_ALSSC              Reviewed;         323 AA.\nAC   A0A9E7S518;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Rhazimal reductase 1 {ECO:0000303|PubMed:36349266};\nDE            Short=AsRHR1 {ECO:0000303|PubMed:36349266};\nDE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};\nGN   Name=RHR1 {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65385.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:36349266}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
