# pathway_0178

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0178.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSASTPTAPYLEDLVRNSLDQNLPWVVQKYGGTSVGKSLDNITKIVGSYIDNGSKVAIVCSARSTQTKSLGTTNLLLQASREALQPAMSSSGDGRSGSMSGTATPFYPKRVGSGFFGKDQSTSMTSSVSSLSQLESQLGRSGSPSPFQSSSSRSPPRSPATPSQDSSISQEPAFHATVDLIKKGHLEAARASLKGGPLRDELEEEIERDCESLRSFLYAAQIIDEISPRSQDSIVGTGERLACKIVAAALRDRGVDSELVVLDNIVDASMSAASEAVSVDAGDQGVAQLGQEFYDQLSFRLGERLRECGQRVPVVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLKASELQVWKEVDGIFTADPRKVPSARLVPIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCLSYPRSPATEMAGLQLQ

[Multiple Choices]
A. IMP biosynthesis via de novo pathway
B. spheroidene biosynthesis. .
C. oxylipin biosynthesis. .
D. Amino-acid biosynthesis
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

> The sequence-matched UniProt record annotates the protein in amino-acid biosynthesis, including methionine and threonine biosynthesis from aspartate. Those pathway annotations cite experimental evidence, although the cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the aspartokinase family: its conserved kinase-like features and overall architecture support an ATP-dependent enzyme acting in aspartate-family amino-acid synthesis. Aspartokinase catalyzes an early step leading to amino acids such as threonine and methionine, making D a meaningful fit over the unrelated IMP, spheroidene, and oxylipin pathways.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the known role of aspartokinases provide a transferable basis for choosing amino-acid biosynthesis; identifying the exact protein's database record is not necessary to distinguish these options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, amino-acid biosynthesis is the clear pathway-level match for an aspartokinase.


### Important caveats

- The reviewer-only sequence-matched annotations support the key, but the exact author source snapshot is unknown.
- The family assignment from sequence is a biological inference, not a direct experimental measurement from the supplied input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the aspartokinase family: its conserved kinase-like features and overall architecture support an ATP-dependent enzyme acting in aspartate-family amino-acid synthesis. Aspartokinase catalyzes an early step leading to amino acids such as threonine and methionine, making D a meaningful fit over the unrelated IMP, spheroidene, and oxylipin pathways.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known role of aspartokinases provide a transferable basis for choosing amino-acid biosynthesis; identifying the exact protein's database record is not necessary to distinguish these options."
  },
  "case_id": "pathway_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein in amino-acid biosynthesis, including methionine and threonine biosynthesis from aspartate. Those pathway annotations cite experimental evidence, although the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotations support the key, but the exact author source snapshot is unknown.",
    "The family assignment from sequence is a biological inference, not a direct experimental measurement from the supplied input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, amino-acid biosynthesis is the clear pathway-level match for an aspartokinase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein in amino-acid biosynthesis, including methionine and threonine biosynthesis from aspartate. Those pathway annotations cite experimental evidence, although the cited paper was not independently reviewed here.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the aspartokinase family: its conserved kinase-like features and overall architecture support an ATP-dependent enzyme acting in aspartate-family amino-acid synthesis. Aspartokinase catalyzes an early step leading to amino acids such as threonine and methionine, making D a meaningful fit over the unrelated IMP, spheroidene, and oxylipin pathways.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known role of aspartokinases provide a transferable basis for choosing amino-acid biosynthesis; identifying the exact protein's database record is not necessary to distinguish these options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, amino-acid biosynthesis is the clear pathway-level match for an aspartokinase."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotations support the key, but the exact author source snapshot is unknown.",
    "The family assignment from sequence is a biological inference, not a direct experimental measurement from the supplied input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (J9VS37) annotates this protein as Aspartokinase (EC 2.7.2.4), catalyzing step 1 of both L-methionine biosynthesis via de novo pathway and L-threonine biosynthesis from L-aspartate. Both annotations fall under 'Amino-acid biosynthesis,' matching option D. The EC number and pathway comments are supported by experimental evidence (PubMed:18757810, gene disruption studies in Cryptococcus neoformans).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of the amino acid kinase superfamily (PF00696): an N-terminal P-loop/ATP-binding motif (GGTSVGKS) in a regulatory domain, and a catalytic domain with the highly conserved 'VVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLK' pattern. This two-domain architecture (regulatory + catalytic) is the defining structural signature of aspartokinases and related amino acid kinases (N-acetylglutamate kinase, glutamate kinase). Among the offered choices: (B) spheroidene biosynthesis involves carotenoid desaturases/hydroxylases with entirely different folds; (C) oxylipin biosynthesis involves lipoxygenases with Fe-binding His motifs and hydroperoxide lyases; (A) IMP (purine) biosynthesis uses amidotransferases, synthetases, and cyclohydrolases with no amino acid kinase fold. The amino acid kinase catalytic domain is specific to amino-acid biosynthetic pathways (aspartate superfamily: Met, Thr, Lys, Ile; or glutamate family: Pro, Arg). A model recognizing the PF00696 fold and its association with amino-acid biosynthesis across many characterized homologs (E. coli LysC, yeast HOM3, etc.) can confidently select D over A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence-level family signature (amino acid kinase P-loop + catalytic domain with GYFGPVPG motif) is a well-characterized, transferable feature across hundreds of homologs. This distinguishes the protein from purine biosynthesis enzymes (A), carotenoid-modifying enzymes (B), and lipoxygenases (C) without requiring knowledge of this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C describe entirely different enzyme classes (carotenoid modifiers, lipoxygenases) with incompatible sequence features. Option A (IMP/purine biosynthesis) involves amidotransferases and synthetases lacking the amino acid kinase fold. Only D is consistent with the observed amino acid kinase architecture.


### Important caveats

- The GGxGxGKS P-loop is found in many ATP-binding proteins; the full two-domain architecture with the specific catalytic-domain motifs (GYFGPVPG, surrounding context) is needed to assign the amino acid kinase family specifically.
- The reviewer-only evidence confirms the protein is from Cryptococcus neoformans, but the organism identity was not provided to the evaluated model; the reasoning relies solely on sequence-level family recognition.
- The pathway annotation in UniProt is supported by experimental gene-disruption evidence (PubMed:18757810), not merely computational transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the amino acid kinase superfamily (PF00696): an N-terminal P-loop/ATP-binding motif (GGTSVGKS) in a regulatory domain, and a catalytic domain with the highly conserved 'VVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLK' pattern. This two-domain architecture (regulatory + catalytic) is the defining structural signature of aspartokinases and related amino acid kinases (N-acetylglutamate kinase, glutamate kinase). Among the offered choices: (B) spheroidene biosynthesis involves carotenoid desaturases/hydroxylases with entirely different folds; (C) oxylipin biosynthesis involves lipoxygenases with Fe-binding His motifs and hydroperoxide lyases; (A) IMP (purine) biosynthesis uses amidotransferases, synthetases, and cyclohydrolases with no amino acid kinase fold. The amino acid kinase catalytic domain is specific to amino-acid biosynthetic pathways (aspartate superfamily: Met, Thr, Lys, Ile; or glutamate family: Pro, Arg). A model recognizing the PF00696 fold and its association with amino-acid biosynthesis across many characterized homologs (E. coli LysC, yeast HOM3, etc.) can confidently select D over A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence-level family signature (amino acid kinase P-loop + catalytic domain with GYFGPVPG motif) is a well-characterized, transferable feature across hundreds of homologs. This distinguishes the protein from purine biosynthesis enzymes (A), carotenoid-modifying enzymes (B), and lipoxygenases (C) without requiring knowledge of this exact protein's database entry."
  },
  "case_id": "pathway_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (J9VS37) annotates this protein as Aspartokinase (EC 2.7.2.4), catalyzing step 1 of both L-methionine biosynthesis via de novo pathway and L-threonine biosynthesis from L-aspartate. Both annotations fall under 'Amino-acid biosynthesis,' matching option D. The EC number and pathway comments are supported by experimental evidence (PubMed:18757810, gene disruption studies in Cryptococcus neoformans)."
  },
  "important_caveats": [
    "The GGxGxGKS P-loop is found in many ATP-binding proteins; the full two-domain architecture with the specific catalytic-domain motifs (GYFGPVPG, surrounding context) is needed to assign the amino acid kinase family specifically.",
    "The reviewer-only evidence confirms the protein is from Cryptococcus neoformans, but the organism identity was not provided to the evaluated model; the reasoning relies solely on sequence-level family recognition.",
    "The pathway annotation in UniProt is supported by experimental gene-disruption evidence (PubMed:18757810), not merely computational transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C describe entirely different enzyme classes (carotenoid modifiers, lipoxygenases) with incompatible sequence features. Option A (IMP/purine biosynthesis) involves amidotransferases and synthetases lacking the amino acid kinase fold. Only D is consistent with the observed amino acid kinase architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (J9VS37) annotates this protein as Aspartokinase (EC 2.7.2.4), catalyzing step 1 of both L-methionine biosynthesis via de novo pathway and L-threonine biosynthesis from L-aspartate. Both annotations fall under 'Amino-acid biosynthesis,' matching option D. The EC number and pathway comments are supported by experimental evidence (PubMed:18757810, gene disruption studies in Cryptococcus neoformans).",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the amino acid kinase superfamily (PF00696): an N-terminal P-loop/ATP-binding motif (GGTSVGKS) in a regulatory domain, and a catalytic domain with the highly conserved 'VVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLK' pattern. This two-domain architecture (regulatory + catalytic) is the defining structural signature of aspartokinases and related amino acid kinases (N-acetylglutamate kinase, glutamate kinase). Among the offered choices: (B) spheroidene biosynthesis involves carotenoid desaturases/hydroxylases with entirely different folds; (C) oxylipin biosynthesis involves lipoxygenases with Fe-binding His motifs and hydroperoxide lyases; (A) IMP (purine) biosynthesis uses amidotransferases, synthetases, and cyclohydrolases with no amino acid kinase fold. The amino acid kinase catalytic domain is specific to amino-acid biosynthetic pathways (aspartate superfamily: Met, Thr, Lys, Ile; or glutamate family: Pro, Arg). A model recognizing the PF00696 fold and its association with amino-acid biosynthesis across many characterized homologs (E. coli LysC, yeast HOM3, etc.) can confidently select D over A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "The sequence-level family signature (amino acid kinase P-loop + catalytic domain with GYFGPVPG motif) is a well-characterized, transferable feature across hundreds of homologs. This distinguishes the protein from purine biosynthesis enzymes (A), carotenoid-modifying enzymes (B), and lipoxygenases (C) without requiring knowledge of this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C describe entirely different enzyme classes (carotenoid modifiers, lipoxygenases) with incompatible sequence features. Option A (IMP/purine biosynthesis) involves amidotransferases and synthetases lacking the amino acid kinase fold. Only D is consistent with the observed amino acid kinase architecture."
  },
  "important_caveats": [
    "The GGxGxGKS P-loop is found in many ATP-binding proteins; the full two-domain architecture with the specific catalytic-domain motifs (GYFGPVPG, surrounding context) is needed to assign the amino acid kinase family specifically.",
    "The reviewer-only evidence confirms the protein is from Cryptococcus neoformans, but the organism identity was not provided to the evaluated model; the reasoning relies solely on sequence-level family recognition.",
    "The pathway annotation in UniProt is supported by experimental gene-disruption evidence (PubMed:18757810), not merely computational transfer."
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
  "benchmark_sequence_length": 615,
  "benchmark_sequence_sha256": "536d54264e6ff3f5d7f7604b6c1376b560b69f4005ef267570182f96dffb6a42",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 615,
  "current_source_sequence_sha256": "536d54264e6ff3f5d7f7604b6c1376b560b69f4005ef267570182f96dffb6a42",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 66,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VS37",
  "selected_historical_entry_version": 66,
  "selected_historical_record_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "selected_historical_source_sequence_length": 615,
  "selected_historical_source_sequence_sha256": "536d54264e6ff3f5d7f7604b6c1376b560b69f4005ef267570182f96dffb6a42",
  "selected_historical_version": {
    "accession": "J9VS37",
    "database": "Swiss-Prot",
    "entryVersion": 66,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AK_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VS37\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.4\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartokinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18757810\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 1/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18757810\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 1/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Kingsbury J.M.\",\"McCusker J.H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18757810\"},{\"database\":\"DOI\",\"id\":\"10.1099/mic.0.2008/019729-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"2767\",\"id\":\"18757810\",\"journal\":\"Microbiology\",\"lastPage\":\"2775\",\"publicationDate\":\"2008\",\"title\":\"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\",\"volume\":\"154\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:11.359613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb",
  "url": "https://rest.uniprot.org/uniprotkb/J9VS37.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H1",
  "excerpt": "ID   AK_CRYN9                Reviewed;         615 AA.\nAC   J9VS37;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 66.\nDE   RecName: Full=Aspartokinase {ECO:0000305};\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\nGN   Name=HOM3 {ECO:0000303|PubMed:18757810};\nGN   ORFNames=CNAG_04347 {ECO:0000312|EMBL:AFR97078.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;\nRA   Kingsbury J.M., McCusker J.H.;\nRT   \"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\";\nRL   Microbiology 154:2767-2775(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-homoserine from L-aspartate: step 1/3.\nCC       {ECO:0000269|PubMed:18757810}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 1/5. {ECO:0000269|PubMed:18757810}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 178. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
