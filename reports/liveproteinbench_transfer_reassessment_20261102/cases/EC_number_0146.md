# EC_number_0146

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0146.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 2.7.2.4

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
A. 2.7.2.4
B. 2.7.1.52
C. 1.14.14.126
D. 1.1.1.136
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

> The matched sequence is annotated as an aspartokinase with EC 2.7.2.4, and the stated reaction is phosphorylation of L-aspartate. The annotation is transferred from a UniProt homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 615-residue sequence is consistent with a large amino-acid-biosynthesis kinase with regulatory regions, rather than either oxidoreductase in C or D. Transferable kinase-family knowledge also distinguishes it from B: homoserine kinases are a different, generally more compact kinase family, while the sequence architecture is consistent with aspartokinase. This supports A probabilistically from the sequence and choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence and architecture provide a meaningful basis for choosing the aspartokinase option, although the exact substrate specificity is not established from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the sequence and family-level inference favor A; the other kinase option is a distinct enzyme family, and C and D are oxidoreductases.


### Important caveats

- The supplied annotation and reaction are supported by transfer from a homolog, not by direct experimental evidence cited here.
- Reviewer-only identity and annotation evidence were not available as original model inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 615-residue sequence is consistent with a large amino-acid-biosynthesis kinase with regulatory regions, rather than either oxidoreductase in C or D. Transferable kinase-family knowledge also distinguishes it from B: homoserine kinases are a different, generally more compact kinase family, while the sequence architecture is consistent with aspartokinase. This supports A probabilistically from the sequence and choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and architecture provide a meaningful basis for choosing the aspartokinase option, although the exact substrate specificity is not established from sequence alone."
  },
  "case_id": "EC_number_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an aspartokinase with EC 2.7.2.4, and the stated reaction is phosphorylation of L-aspartate. The annotation is transferred from a UniProt homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The supplied annotation and reaction are supported by transfer from a homolog, not by direct experimental evidence cited here.",
    "Reviewer-only identity and annotation evidence were not available as original model inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the sequence and family-level inference favor A; the other kinase option is a distinct enzyme family, and C and D are oxidoreductases."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an aspartokinase with EC 2.7.2.4, and the stated reaction is phosphorylation of L-aspartate. The annotation is transferred from a UniProt homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 615-residue sequence is consistent with a large amino-acid-biosynthesis kinase with regulatory regions, rather than either oxidoreductase in C or D. Transferable kinase-family knowledge also distinguishes it from B: homoserine kinases are a different, generally more compact kinase family, while the sequence architecture is consistent with aspartokinase. This supports A probabilistically from the sequence and choices.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and architecture provide a meaningful basis for choosing the aspartokinase option, although the exact substrate specificity is not established from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the sequence and family-level inference favor A; the other kinase option is a distinct enzyme family, and C and D are oxidoreductases."
  },
  "important_caveats": [
    "The supplied annotation and reaction are supported by transfer from a homolog, not by direct experimental evidence cited here.",
    "Reviewer-only identity and annotation evidence were not available as original model inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9VS37 annotates this protein as Aspartokinase with EC 2.7.2.4 (evidence code ECO:0000250, transferred by similarity to P10869). The catalytic reaction is L-aspartate + ATP = 4-phospho-L-aspartate + ADP. The sequence matches the benchmark input exactly (615 aa, SHA256 confirmed). The annotation is by similarity rather than direct experimental assay on this exact protein, but it is a curated Swiss-Prot annotation with a published functional reference (PubMed:18757810 on threonine biosynthetic genes in C. neoformans).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear P-loop/Walker A motif 'GGTSVGKS' at the N-terminus, which is a hallmark of nucleotide-binding kinases, immediately eliminating oxidoreductases (C: 1.14.14.126 cytochrome P450; D: 1.1.1.136 dihydroxyacetone reductase). The N-terminal ~150 residues show an ACT (allosteric feedback inhibition) domain signature (the 'LLLQ...IVCSARSTQTKSLGTTNLLLQ' pattern with beta-sheet topology), which is characteristic of amino acid biosynthesis enzymes, particularly aspartokinase and related amino acid kinases. The central region contains the amino acid kinase family motifs: 'VGTGER' (substrate-binding loop) and 'GYFGPVPGSLLAQIGRGYTDLC' (conserved GHMP-adjacent region in amino acid kinases). This two-domain architecture (ACT + amino acid kinase catalytic domain) is diagnostic of the amino acid kinase family (EC 2.7.2.x), distinguishing it from acetyl-CoA synthetase ADP-forming (2.7.1.52, option B), which belongs to a different superfamily with a distinct fold lacking ACT domains and the specific amino acid kinase motif set. Thus, family-level knowledge of amino acid kinases and ACT domains meaningfully selects option A over B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P-loop motif identifies this as a kinase (eliminating C and D). The ACT domain plus amino acid kinase family motifs (GGTSVGKS, VGTGER, GYFGPVPGSLLAQIGRGYTDLC) are well-known transferable features of the amino acid kinase superfamily (EC 2.7.2.x), distinguishing it from acetyl-CoA synthetase (2.7.1.52). This constitutes legitimate family-level inference from conserved sequence features shared with other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three EC classes (2.7.2.x, 2.7.1.x, 1.14.x, 1.1.x). The sequence clearly shows kinase features (P-loop) eliminating oxidoreductases, and the ACT domain plus amino acid kinase motifs distinguish 2.7.2.4 from 2.7.1.52. No other option is defensible.


### Important caveats

- The UniProt EC annotation is by similarity (ECO:0000250) to P10869, not direct experimental characterization of this exact protein, though a functional reference (PubMed:18757810) supports its role in threonine biosynthesis.
- The ACT domain identification is based on general fold recognition; without structural data, this is a probabilistic inference consistent with the sequence pattern.
- The benchmark sequence is from Cryptococcus neoformans (fungal), and fungal aspartokinases (HOM3 gene) are well-characterized members of the amino acid kinase family.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear P-loop/Walker A motif 'GGTSVGKS' at the N-terminus, which is a hallmark of nucleotide-binding kinases, immediately eliminating oxidoreductases (C: 1.14.14.126 cytochrome P450; D: 1.1.1.136 dihydroxyacetone reductase). The N-terminal ~150 residues show an ACT (allosteric feedback inhibition) domain signature (the 'LLLQ...IVCSARSTQTKSLGTTNLLLQ' pattern with beta-sheet topology), which is characteristic of amino acid biosynthesis enzymes, particularly aspartokinase and related amino acid kinases. The central region contains the amino acid kinase family motifs: 'VGTGER' (substrate-binding loop) and 'GYFGPVPGSLLAQIGRGYTDLC' (conserved GHMP-adjacent region in amino acid kinases). This two-domain architecture (ACT + amino acid kinase catalytic domain) is diagnostic of the amino acid kinase family (EC 2.7.2.x), distinguishing it from acetyl-CoA synthetase ADP-forming (2.7.1.52, option B), which belongs to a different superfamily with a distinct fold lacking ACT domains and the specific amino acid kinase motif set. Thus, family-level knowledge of amino acid kinases and ACT domains meaningfully selects option A over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif identifies this as a kinase (eliminating C and D). The ACT domain plus amino acid kinase family motifs (GGTSVGKS, VGTGER, GYFGPVPGSLLAQIGRGYTDLC) are well-known transferable features of the amino acid kinase superfamily (EC 2.7.2.x), distinguishing it from acetyl-CoA synthetase (2.7.1.52). This constitutes legitimate family-level inference from conserved sequence features shared with other proteins."
  },
  "case_id": "EC_number_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry J9VS37 annotates this protein as Aspartokinase with EC 2.7.2.4 (evidence code ECO:0000250, transferred by similarity to P10869). The catalytic reaction is L-aspartate + ATP = 4-phospho-L-aspartate + ADP. The sequence matches the benchmark input exactly (615 aa, SHA256 confirmed). The annotation is by similarity rather than direct experimental assay on this exact protein, but it is a curated Swiss-Prot annotation with a published functional reference (PubMed:18757810 on threonine biosynthetic genes in C. neoformans)."
  },
  "important_caveats": [
    "The UniProt EC annotation is by similarity (ECO:0000250) to P10869, not direct experimental characterization of this exact protein, though a functional reference (PubMed:18757810) supports its role in threonine biosynthesis.",
    "The ACT domain identification is based on general fold recognition; without structural data, this is a probabilistic inference consistent with the sequence pattern.",
    "The benchmark sequence is from Cryptococcus neoformans (fungal), and fungal aspartokinases (HOM3 gene) are well-characterized members of the amino acid kinase family."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three EC classes (2.7.2.x, 2.7.1.x, 1.14.x, 1.1.x). The sequence clearly shows kinase features (P-loop) eliminating oxidoreductases, and the ACT domain plus amino acid kinase motifs distinguish 2.7.2.4 from 2.7.1.52. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9VS37 annotates this protein as Aspartokinase with EC 2.7.2.4 (evidence code ECO:0000250, transferred by similarity to P10869). The catalytic reaction is L-aspartate + ATP = 4-phospho-L-aspartate + ADP. The sequence matches the benchmark input exactly (615 aa, SHA256 confirmed). The annotation is by similarity rather than direct experimental assay on this exact protein, but it is a curated Swiss-Prot annotation with a published functional reference (PubMed:18757810 on threonine biosynthetic genes in C. neoformans).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear P-loop/Walker A motif 'GGTSVGKS' at the N-terminus, which is a hallmark of nucleotide-binding kinases, immediately eliminating oxidoreductases (C: 1.14.14.126 cytochrome P450; D: 1.1.1.136 dihydroxyacetone reductase). The N-terminal ~150 residues show an ACT (allosteric feedback inhibition) domain signature (the 'LLLQ...IVCSARSTQTKSLGTTNLLLQ' pattern with beta-sheet topology), which is characteristic of amino acid biosynthesis enzymes, particularly aspartokinase and related amino acid kinases. The central region contains the amino acid kinase family motifs: 'VGTGER' (substrate-binding loop) and 'GYFGPVPGSLLAQIGRGYTDLC' (conserved GHMP-adjacent region in amino acid kinases). This two-domain architecture (ACT + amino acid kinase catalytic domain) is diagnostic of the amino acid kinase family (EC 2.7.2.x), distinguishing it from acetyl-CoA synthetase ADP-forming (2.7.1.52, option B), which belongs to a different superfamily with a distinct fold lacking ACT domains and the specific amino acid kinase motif set. Thus, family-level knowledge of amino acid kinases and ACT domains meaningfully selects option A over B.",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif identifies this as a kinase (eliminating C and D). The ACT domain plus amino acid kinase family motifs (GGTSVGKS, VGTGER, GYFGPVPGSLLAQIGRGYTDLC) are well-known transferable features of the amino acid kinase superfamily (EC 2.7.2.x), distinguishing it from acetyl-CoA synthetase (2.7.1.52). This constitutes legitimate family-level inference from conserved sequence features shared with other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three EC classes (2.7.2.x, 2.7.1.x, 1.14.x, 1.1.x). The sequence clearly shows kinase features (P-loop) eliminating oxidoreductases, and the ACT domain plus amino acid kinase motifs distinguish 2.7.2.4 from 2.7.1.52. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt EC annotation is by similarity (ECO:0000250) to P10869, not direct experimental characterization of this exact protein, though a functional reference (PubMed:18757810) supports its role in threonine biosynthesis.",
    "The ACT domain identification is based on general fold recognition; without structural data, this is a probabilistic inference consistent with the sequence pattern.",
    "The benchmark sequence is from Cryptococcus neoformans (fungal), and fungal aspartokinases (HOM3 gene) are well-characterized members of the amino acid kinase family."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23777\"}}],\"reaction\":{\"ecNumber\":\"2.7.2.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"name\":\"L-aspartate + ATP = 4-phospho-L-aspartate + ADP\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23776\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29991\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "DE   RecName: Full=Aspartokinase {ECO:0000305};\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;\nCC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.138363+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49",
  "url": "https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
