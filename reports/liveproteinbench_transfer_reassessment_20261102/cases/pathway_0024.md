# pathway_0024

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0024.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAISPEVEHPNKAFGFAARDPSGLLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSQDLENYCPDQILTYSATYTDGTTTYGGYSSLMVADEHFVIRWPENLPMDIGAPLLCAGITTYSPLRHFGLDKPGTHVGIVGLGGLGHVAVKFAKAFGAKVTVISTSEGKKQEAVEKLGADAFLVSRDPEQMQAAAATLDGIIDTVSAVHPILPLVNLLKSQGKLIMVGAPEKPIELPVFPLLLGRKIVAGSAIGGLKETQDMIDFAAKHNILPDVELIPMDYVNTAMERLLKADVKYRFVIDICNTLKSA

[Multiple Choices]
A. L-fucose degradation. .
B. glycosylphosphatidylinositol-anchor biosynthesis. .
C. Alkaloid biosynthesis
D. terpenoid biosynthesis.
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

> The supplied sequence matches the reviewed record annotated as vomilenine reductase, with the pathway listed as alkaloid biosynthesis, specifically ajmaline biosynthesis. The pathway annotation carries experimental evidence codes, though the excerpts provide the database annotation and its evidence references rather than the experiments themselves.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's substrate-specific function as vomilenine reductase, or equivalent evidence that it acts in ajmaline/alkaloid biosynthesis.


**Reason**

> The sequence is consistent with a soluble enzyme, which makes the membrane-associated GPI-anchor option less plausible, but enzyme-family or general sequence features do not meaningfully distinguish alkaloid biosynthesis from the other soluble metabolic pathways offered. Assigning the specific alkaloid pathway requires knowledge of this protein's substrate or pathway role, which is not given in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone leaves the pathway underdetermined, but the evidence does not establish another offered pathway as a defensible answer.


### Important caveats

- The sequence match supports applicability of the cited database record; the actual author source snapshot is unknown.
- The pathway judgment rests on a database annotation with experimental evidence codes, not independent review of the cited experiments.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate-specific function as vomilenine reductase, or equivalent evidence that it acts in ajmaline/alkaloid biosynthesis.",
    "reason": "The sequence is consistent with a soluble enzyme, which makes the membrane-associated GPI-anchor option less plausible, but enzyme-family or general sequence features do not meaningfully distinguish alkaloid biosynthesis from the other soluble metabolic pathways offered. Assigning the specific alkaloid pathway requires knowledge of this protein's substrate or pathway role, which is not given in the original input."
  },
  "case_id": "pathway_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed record annotated as vomilenine reductase, with the pathway listed as alkaloid biosynthesis, specifically ajmaline biosynthesis. The pathway annotation carries experimental evidence codes, though the excerpts provide the database annotation and its evidence references rather than the experiments themselves."
  },
  "important_caveats": [
    "The sequence match supports applicability of the cited database record; the actual author source snapshot is unknown.",
    "The pathway judgment rests on a database annotation with experimental evidence codes, not independent review of the cited experiments."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone leaves the pathway underdetermined, but the evidence does not establish another offered pathway as a defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed record annotated as vomilenine reductase, with the pathway listed as alkaloid biosynthesis, specifically ajmaline biosynthesis. The pathway annotation carries experimental evidence codes, though the excerpts provide the database annotation and its evidence references rather than the experiments themselves.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's substrate-specific function as vomilenine reductase, or equivalent evidence that it acts in ajmaline/alkaloid biosynthesis.",
    "reason": "The sequence is consistent with a soluble enzyme, which makes the membrane-associated GPI-anchor option less plausible, but enzyme-family or general sequence features do not meaningfully distinguish alkaloid biosynthesis from the other soluble metabolic pathways offered. Assigning the specific alkaloid pathway requires knowledge of this protein's substrate or pathway role, which is not given in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone leaves the pathway underdetermined, but the evidence does not establish another offered pathway as a defensible answer."
  },
  "important_caveats": [
    "The sequence match supports applicability of the cited database record; the actual author source snapshot is unknown.",
    "The pathway judgment rests on a database annotation with experimental evidence codes, not independent review of the cited experiments."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ3 annotates this protein as Vomilenine reductase (EC 1.5.1.32) from Rauvolfia serpentina, with pathway comment 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence codes ECO:0000269 from PubMed:11937349 and PubMed:38212296. Ajmaline is a well-characterized antiarrhythmic monoterpene indole alkaloid. The expected answer 'Alkaloid biosynthesis' is directly and experimentally supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two Rossmann-fold motifs (GGLGHVAVK and GSAIGGLKETQ, matching GxGxxG NAD(P)H-binding patterns) and a zinc-binding region (GICHSDLHM and C-X-X-C patterns in GCLVGSCRKCDMCSQ), identifying it as an NAD(P)-dependent zinc-containing oxidoreductase. Eliminating the other options: (1) GPI-anchor biosynthesis relies on glycosyltransferases, phosphatases, and transamidases—not NAD(P)H-dependent reductases with zinc sites; (2) L-fucose degradation involves a mutarotase (isomerase), a kinase, and an aldolase—none matching a Rossmann-fold zinc reductase; (3) Terpenoid biosynthesis core enzymes are terpene synthases (with DDxxD or NSE/DTE motifs, class I/II folds ~250-400 aa) and prenyltransferases (DDxxD motifs)—none of which are present here. Alkaloid biosynthesis in plants commonly employs NAD(P)H-dependent reductases and zinc-containing dehydrogenases (e.g., dihydroflavonol reductases, strictosidine synthase-associated reductases, and various indole alkaloid reductases), making this the best match among the four choices. This elimination-by-enzyme-class argument is transferable across plant secondary metabolism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the presence of Rossmann-fold and zinc-binding motifs to identify the enzyme class as an NAD(P)-dependent oxidoreductase, then eliminate GPI-anchor biosynthesis (glycosyltransferase/phosphatase pathway) and L-fucose degradation (isomerase/kinase/aldolase pathway) by enzyme-class mismatch, and further eliminate terpenoid biosynthesis by the absence of characteristic terpene synthase/prenyltransferase motifs (DDxxD). The remaining choice—alkaloid biosynthesis—is the pathway most commonly associated with plant NAD(P)H-dependent zinc reductases among the options. This is a defensible probabilistic inference from transferable enzyme-class knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four pathways involve fundamentally different enzyme classes. The sequence's Rossmann-fold zinc reductase features clearly eliminate GPI-anchor biosynthesis and L-fucose degradation. The absence of terpene synthase/prenyltransferase motifs argues against terpenoid biosynthesis. Alkaloid biosynthesis is the most consistent remaining option.


### Important caveats

- The reasoning is an elimination-based probabilistic argument rather than a positive identification of the specific alkaloid pathway; a generic plant NAD(P)H reductase could theoretically participate in other pathways not offered as choices.
- The protein is annotated as a 'CAD2-homolog' (cinnamyl alcohol dehydrogenase homolog), which could initially mislead toward phenylpropanoid/lignin biosynthesis, but this pathway is not among the choices.
- The UniProt entry was first publicly released in June 2025; the benchmark's data-construction date is unknown, so the author may have used a pre-publication or different source.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two Rossmann-fold motifs (GGLGHVAVK and GSAIGGLKETQ, matching GxGxxG NAD(P)H-binding patterns) and a zinc-binding region (GICHSDLHM and C-X-X-C patterns in GCLVGSCRKCDMCSQ), identifying it as an NAD(P)-dependent zinc-containing oxidoreductase. Eliminating the other options: (1) GPI-anchor biosynthesis relies on glycosyltransferases, phosphatases, and transamidases—not NAD(P)H-dependent reductases with zinc sites; (2) L-fucose degradation involves a mutarotase (isomerase), a kinase, and an aldolase—none matching a Rossmann-fold zinc reductase; (3) Terpenoid biosynthesis core enzymes are terpene synthases (with DDxxD or NSE/DTE motifs, class I/II folds ~250-400 aa) and prenyltransferases (DDxxD motifs)—none of which are present here. Alkaloid biosynthesis in plants commonly employs NAD(P)H-dependent reductases and zinc-containing dehydrogenases (e.g., dihydroflavonol reductases, strictosidine synthase-associated reductases, and various indole alkaloid reductases), making this the best match among the four choices. This elimination-by-enzyme-class argument is transferable across plant secondary metabolism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the presence of Rossmann-fold and zinc-binding motifs to identify the enzyme class as an NAD(P)-dependent oxidoreductase, then eliminate GPI-anchor biosynthesis (glycosyltransferase/phosphatase pathway) and L-fucose degradation (isomerase/kinase/aldolase pathway) by enzyme-class mismatch, and further eliminate terpenoid biosynthesis by the absence of characteristic terpene synthase/prenyltransferase motifs (DDxxD). The remaining choice—alkaloid biosynthesis—is the pathway most commonly associated with plant NAD(P)H-dependent zinc reductases among the options. This is a defensible probabilistic inference from transferable enzyme-class knowledge."
  },
  "case_id": "pathway_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ3 annotates this protein as Vomilenine reductase (EC 1.5.1.32) from Rauvolfia serpentina, with pathway comment 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence codes ECO:0000269 from PubMed:11937349 and PubMed:38212296. Ajmaline is a well-characterized antiarrhythmic monoterpene indole alkaloid. The expected answer 'Alkaloid biosynthesis' is directly and experimentally supported."
  },
  "important_caveats": [
    "The reasoning is an elimination-based probabilistic argument rather than a positive identification of the specific alkaloid pathway; a generic plant NAD(P)H reductase could theoretically participate in other pathways not offered as choices.",
    "The protein is annotated as a 'CAD2-homolog' (cinnamyl alcohol dehydrogenase homolog), which could initially mislead toward phenylpropanoid/lignin biosynthesis, but this pathway is not among the choices.",
    "The UniProt entry was first publicly released in June 2025; the benchmark's data-construction date is unknown, so the author may have used a pre-publication or different source."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four pathways involve fundamentally different enzyme classes. The sequence's Rossmann-fold zinc reductase features clearly eliminate GPI-anchor biosynthesis and L-fucose degradation. The absence of terpene synthase/prenyltransferase motifs argues against terpenoid biosynthesis. Alkaloid biosynthesis is the most consistent remaining option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ3 annotates this protein as Vomilenine reductase (EC 1.5.1.32) from Rauvolfia serpentina, with pathway comment 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence codes ECO:0000269 from PubMed:11937349 and PubMed:38212296. Ajmaline is a well-characterized antiarrhythmic monoterpene indole alkaloid. The expected answer 'Alkaloid biosynthesis' is directly and experimentally supported.",
    "evidence_ids": ["C5", "C6", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two Rossmann-fold motifs (GGLGHVAVK and GSAIGGLKETQ, matching GxGxxG NAD(P)H-binding patterns) and a zinc-binding region (GICHSDLHM and C-X-X-C patterns in GCLVGSCRKCDMCSQ), identifying it as an NAD(P)-dependent zinc-containing oxidoreductase. Eliminating the other options: (1) GPI-anchor biosynthesis relies on glycosyltransferases, phosphatases, and transamidases—not NAD(P)H-dependent reductases with zinc sites; (2) L-fucose degradation involves a mutarotase (isomerase), a kinase, and an aldolase—none matching a Rossmann-fold zinc reductase; (3) Terpenoid biosynthesis core enzymes are terpene synthases (with DDxxD or NSE/DTE motifs, class I/II folds ~250-400 aa) and prenyltransferases (DDxxD motifs)—none of which are present here. Alkaloid biosynthesis in plants commonly employs NAD(P)H-dependent reductases and zinc-containing dehydrogenases (e.g., dihydroflavonol reductases, strictosidine synthase-associated reductases, and various indole alkaloid reductases), making this the best match among the four choices. This elimination-by-enzyme-class argument is transferable across plant secondary metabolism.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the presence of Rossmann-fold and zinc-binding motifs to identify the enzyme class as an NAD(P)-dependent oxidoreductase, then eliminate GPI-anchor biosynthesis (glycosyltransferase/phosphatase pathway) and L-fucose degradation (isomerase/kinase/aldolase pathway) by enzyme-class mismatch, and further eliminate terpenoid biosynthesis by the absence of characteristic terpene synthase/prenyltransferase motifs (DDxxD). The remaining choice—alkaloid biosynthesis—is the pathway most commonly associated with plant NAD(P)H-dependent zinc reductases among the options. This is a defensible probabilistic inference from transferable enzyme-class knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four pathways involve fundamentally different enzyme classes. The sequence's Rossmann-fold zinc reductase features clearly eliminate GPI-anchor biosynthesis and L-fucose degradation. The absence of terpene synthase/prenyltransferase motifs argues against terpenoid biosynthesis. Alkaloid biosynthesis is the most consistent remaining option."
  },
  "important_caveats": [
    "The reasoning is an elimination-based probabilistic argument rather than a positive identification of the specific alkaloid pathway; a generic plant NAD(P)H reductase could theoretically participate in other pathways not offered as choices.",
    "The protein is annotated as a 'CAD2-homolog' (cinnamyl alcohol dehydrogenase homolog), which could initially mislead toward phenylpropanoid/lignin biosynthesis, but this pathway is not among the choices.",
    "The UniProt entry was first publicly released in June 2025; the benchmark's data-construction date is unknown, so the author may have used a pre-publication or different source."
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
  "benchmark_sequence_length": 360,
  "benchmark_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 360,
  "current_source_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ3",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "selected_historical_source_sequence_length": 360,
  "selected_historical_source_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "selected_historical_version": {
    "accession": "P0DXJ3",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VOR1_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"CAD2-homolog protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Protein RR6-2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsRR6-2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11937349\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.32\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11937349\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis; ajmaline biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61927.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"von Schumann G.\",\"Gao S.\",\"Stoeckigt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11937349\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0968-0896(01)00435-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"1913\",\"id\":\"11937349\",\"journal\":\"Bioorg. Med. Chem.\",\"lastPage\":\"1918\",\"publicationDate\":\"2002\",\"title\":\"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the biosynthesis of the therapeutically applied antiarrhythmic alkaloid ajmaline.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"ACTIVITY REGULATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   VOR1_RAUSE              Reviewed;         360 AA.\nAC   P0DXJ3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};\nDE            Short=RsVR {ECO:0000305|PubMed:38212296};\nDE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};\nDE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};\nGN   Name=VR {ECO:0000305|PubMed:38212296};\nGN   Synonyms=RR6-2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WKU61927.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY,\nRP   ACTIVITY REGULATION, AND TISSUE SPECIFICITY.\nRX   PubMed=11937349; DOI=10.1016/s0968-0896(01)00435-7;\nRA   von Schumann G., Gao S., Stoeckigt J.;\nRT   \"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the\nRT   biosynthesis of the therapeutically applied antiarrhythmic alkaloid\nRT   ajmaline.\";\nRL   Bioorg. Med. Chem. 10:1913-1918(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.\nCC       {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
