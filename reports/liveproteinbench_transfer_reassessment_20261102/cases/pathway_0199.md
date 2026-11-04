# pathway_0199

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0199.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Carotenoid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQTVTLSIFRFNEFEKRLWVLGQMTANKLGMHYLPKAKFWKMFGSGTGQGFTPKPNWHVWSILAVWPDEETARREVAESPIYQRWTKMADESYTVLLQPTSAWGKWDGKEPFEPVKPASDVRPIAALTRATVKFWKAERFWAREPAISHMIGRNKDVVFKIGVGEVPFVQQVTFSIWPDARSMEEFARGAGGPHGEAIKAVRAENWFKEELYARFQILGTIGKWEGKDPVGEALTARPSEAPKPAPAPAAAQPAPAAEAPKPAPAPVAEKPALAVEMPKPAEPPKPVVEAPKPASAPVASKPMPQGGKPNFKGKPGKGGRKENA

[Multiple Choices]
A. Carotenoid biosynthesis
B. One-carbon metabolism
C. Amino-acid degradation. .
D. LPS O-antigen biosynthesis. .
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

> The sequence-matched UniProt record annotates the protein as spheroidene monooxygenase and places it in carotenoid biosynthesis. The pathway annotation is explicitly supported by similarity evidence, so it supports choice A as a database annotation, though the excerpts do not independently establish direct experimental characterization of this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The glycine-rich sequence segment may be consistent with a nucleotide- or flavin-binding enzyme, but that broad enzyme-level clue does not identify a carotenoid substrate or distinguish carotenoid biosynthesis from the offered one-carbon or amino-acid pathways. The sequence provides no clear pathway-specific feature in the supplied input.


**Missing item-specific fact**

> The protein's substrate-specific family or functional assignment as a spheroidene monooxygenase is needed to connect it to carotenoid biosynthesis.


**Reason**

> The correct pathway depends on assigning this sequence to a substrate-specific enzyme family. Generic sequence features could suggest enzyme class but do not meaningfully distinguish the relevant metabolic pathways among these options without that assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices name distinct pathways, and the supplied evidence supports carotenoid biosynthesis; no second option is comparably supported.


### Important caveats

- The pathway and enzyme annotations use similarity evidence; the supplied excerpts do not establish the extent of direct experimental validation for this exact sequence.
- The reviewer-only organism and database annotations were not part of the original input and are not used as transferable clues.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The glycine-rich sequence segment may be consistent with a nucleotide- or flavin-binding enzyme, but that broad enzyme-level clue does not identify a carotenoid substrate or distinguish carotenoid biosynthesis from the offered one-carbon or amino-acid pathways. The sequence provides no clear pathway-specific feature in the supplied input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate-specific family or functional assignment as a spheroidene monooxygenase is needed to connect it to carotenoid biosynthesis.",
    "reason": "The correct pathway depends on assigning this sequence to a substrate-specific enzyme family. Generic sequence features could suggest enzyme class but do not meaningfully distinguish the relevant metabolic pathways among these options without that assignment."
  },
  "case_id": "pathway_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as spheroidene monooxygenase and places it in carotenoid biosynthesis. The pathway annotation is explicitly supported by similarity evidence, so it supports choice A as a database annotation, though the excerpts do not independently establish direct experimental characterization of this exact protein."
  },
  "important_caveats": [
    "The pathway and enzyme annotations use similarity evidence; the supplied excerpts do not establish the extent of direct experimental validation for this exact sequence.",
    "The reviewer-only organism and database annotations were not part of the original input and are not used as transferable clues."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct pathways, and the supplied evidence supports carotenoid biosynthesis; no second option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as spheroidene monooxygenase and places it in carotenoid biosynthesis. The pathway annotation is explicitly supported by similarity evidence, so it supports choice A as a database annotation, though the excerpts do not independently establish direct experimental characterization of this exact protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The glycine-rich sequence segment may be consistent with a nucleotide- or flavin-binding enzyme, but that broad enzyme-level clue does not identify a carotenoid substrate or distinguish carotenoid biosynthesis from the offered one-carbon or amino-acid pathways. The sequence provides no clear pathway-specific feature in the supplied input.",
    "missing_item_specific_fact": "The protein's substrate-specific family or functional assignment as a spheroidene monooxygenase is needed to connect it to carotenoid biosynthesis.",
    "reason": "The correct pathway depends on assigning this sequence to a substrate-specific enzyme family. Generic sequence features could suggest enzyme class but do not meaningfully distinguish the relevant metabolic pathways among these options without that assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct pathways, and the supplied evidence supports carotenoid biosynthesis; no second option is comparably supported."
  },
  "important_caveats": [
    "The pathway and enzyme annotations use similarity evidence; the supplied excerpts do not establish the extent of direct experimental validation for this exact sequence.",
    "The reviewer-only organism and database annotations were not part of the original input and are not used as transferable clues."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q3J189, CRTA_CERS4) explicitly annotates the protein as Spheroidene monooxygenase (CrtA, EC 1.14.15.9) with pathway 'Carotenoid biosynthesis; spheroidene biosynthesis.' While the EC assignment uses similarity transfer (ECO:0000250 from P17055), the function is corroborated by experimental evidence (PubMed:20851979, Lee et al. 2010, Appl. Environ. Microbiol.) demonstrating spheroidene monooxygenase activity. The gene name crtA and the 1995 genomic study (PubMed:7721699) placing it in the carotenoid biosynthesis gene cluster further support the annotation. The expected answer 'Carotenoid biosynthesis' is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of this protein contains distinctive Ala/Pro-rich tandem repeats (APKPAPAPAAAQPAPAAEAPKPAPAPVAEKPALAVEMPKPAEPPKPVVEAPKPASAPVASKPMPQGGKPNFKGKPGKGGRKENA). This is a well-documented family-level signature of CrtA (spheroidene monooxygenase) proteins across multiple purple bacteria (Rhodobacter, Rhodopseudomonas, Bradyrhizobium, etc.), where the catalytic domain is followed by a long Ala/Pro-rich tail. Combined with the N-terminal catalytic domain architecture containing motifs consistent with a carotenoid-modifying enzyme (hydrophobic core, conserved aromatic residues), this pattern distinguishes the protein from one-carbon metabolism enzymes (e.g., methylenetetrahydrofolate reductase, methionine synthase — different folds), amino-acid degradation enzymes (deaminases, transaminases — different folds), and LPS O-antigen biosynthesis enzymes (glycosyltransferases, polymerases — different folds). A model trained on the CrtA family literature from multiple organisms could recognize the Ala/Pro-rich C-terminus as a hallmark of carotenoid pathway enzymes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The C-terminal Ala/Pro-rich repeats are a shared, well-documented feature of CrtA homologs across multiple bacterial genera, making this a legitimate family-level inference rather than a lookup of this single protein's annotation. The four distractor pathways involve entirely different enzyme families with incompatible architectures, so the family recognition meaningfully narrows the answer to carotenoid biosynthesis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct metabolic pathways with non-overlapping enzyme families. The Ala/Pro-rich C-terminus and catalytic domain architecture are incompatible with one-carbon metabolism, amino-acid degradation, or LPS O-antigen biosynthesis enzymes. Only carotenoid biosynthesis (CrtA) matches the observed sequence features.


### Important caveats

- The EC number annotation in UniProt is transferred by similarity (ECO:0000250 from P17055, the R. sphaeroides strain 2.4.1 CrtA), but experimental validation exists via PubMed:20851979.
- The C-terminal Ala/Pro-rich region is a family-level CrtA feature but is not unique to carotenoid biosynthesis in all possible contexts; however, among the four offered choices, it clearly points to CrtA/carotenoid pathway.
- The reviewer-only evidence confirms the sequence matches UniProt Q3J189 exactly (SHA-256 match), but this accession was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of this protein contains distinctive Ala/Pro-rich tandem repeats (APKPAPAPAAAQPAPAAEAPKPAPAPVAEKPALAVEMPKPAEPPKPVVEAPKPASAPVASKPMPQGGKPNFKGKPGKGGRKENA). This is a well-documented family-level signature of CrtA (spheroidene monooxygenase) proteins across multiple purple bacteria (Rhodobacter, Rhodopseudomonas, Bradyrhizobium, etc.), where the catalytic domain is followed by a long Ala/Pro-rich tail. Combined with the N-terminal catalytic domain architecture containing motifs consistent with a carotenoid-modifying enzyme (hydrophobic core, conserved aromatic residues), this pattern distinguishes the protein from one-carbon metabolism enzymes (e.g., methylenetetrahydrofolate reductase, methionine synthase — different folds), amino-acid degradation enzymes (deaminases, transaminases — different folds), and LPS O-antigen biosynthesis enzymes (glycosyltransferases, polymerases — different folds). A model trained on the CrtA family literature from multiple organisms could recognize the Ala/Pro-rich C-terminus as a hallmark of carotenoid pathway enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The C-terminal Ala/Pro-rich repeats are a shared, well-documented feature of CrtA homologs across multiple bacterial genera, making this a legitimate family-level inference rather than a lookup of this single protein's annotation. The four distractor pathways involve entirely different enzyme families with incompatible architectures, so the family recognition meaningfully narrows the answer to carotenoid biosynthesis."
  },
  "case_id": "pathway_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q3J189, CRTA_CERS4) explicitly annotates the protein as Spheroidene monooxygenase (CrtA, EC 1.14.15.9) with pathway 'Carotenoid biosynthesis; spheroidene biosynthesis.' While the EC assignment uses similarity transfer (ECO:0000250 from P17055), the function is corroborated by experimental evidence (PubMed:20851979, Lee et al. 2010, Appl. Environ. Microbiol.) demonstrating spheroidene monooxygenase activity. The gene name crtA and the 1995 genomic study (PubMed:7721699) placing it in the carotenoid biosynthesis gene cluster further support the annotation. The expected answer 'Carotenoid biosynthesis' is well-supported."
  },
  "important_caveats": [
    "The EC number annotation in UniProt is transferred by similarity (ECO:0000250 from P17055, the R. sphaeroides strain 2.4.1 CrtA), but experimental validation exists via PubMed:20851979.",
    "The C-terminal Ala/Pro-rich region is a family-level CrtA feature but is not unique to carotenoid biosynthesis in all possible contexts; however, among the four offered choices, it clearly points to CrtA/carotenoid pathway.",
    "The reviewer-only evidence confirms the sequence matches UniProt Q3J189 exactly (SHA-256 match), but this accession was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct metabolic pathways with non-overlapping enzyme families. The Ala/Pro-rich C-terminus and catalytic domain architecture are incompatible with one-carbon metabolism, amino-acid degradation, or LPS O-antigen biosynthesis enzymes. Only carotenoid biosynthesis (CrtA) matches the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q3J189, CRTA_CERS4) explicitly annotates the protein as Spheroidene monooxygenase (CrtA, EC 1.14.15.9) with pathway 'Carotenoid biosynthesis; spheroidene biosynthesis.' While the EC assignment uses similarity transfer (ECO:0000250 from P17055), the function is corroborated by experimental evidence (PubMed:20851979, Lee et al. 2010, Appl. Environ. Microbiol.) demonstrating spheroidene monooxygenase activity. The gene name crtA and the 1995 genomic study (PubMed:7721699) placing it in the carotenoid biosynthesis gene cluster further support the annotation. The expected answer 'Carotenoid biosynthesis' is well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of this protein contains distinctive Ala/Pro-rich tandem repeats (APKPAPAPAAAQPAPAAEAPKPAPAPVAEKPALAVEMPKPAEPPKPVVEAPKPASAPVASKPMPQGGKPNFKGKPGKGGRKENA). This is a well-documented family-level signature of CrtA (spheroidene monooxygenase) proteins across multiple purple bacteria (Rhodobacter, Rhodopseudomonas, Bradyrhizobium, etc.), where the catalytic domain is followed by a long Ala/Pro-rich tail. Combined with the N-terminal catalytic domain architecture containing motifs consistent with a carotenoid-modifying enzyme (hydrophobic core, conserved aromatic residues), this pattern distinguishes the protein from one-carbon metabolism enzymes (e.g., methylenetetrahydrofolate reductase, methionine synthase — different folds), amino-acid degradation enzymes (deaminases, transaminases — different folds), and LPS O-antigen biosynthesis enzymes (glycosyltransferases, polymerases — different folds). A model trained on the CrtA family literature from multiple organisms could recognize the Ala/Pro-rich C-terminus as a hallmark of carotenoid pathway enzymes.",
    "missing_item_specific_fact": "",
    "reason": "The C-terminal Ala/Pro-rich repeats are a shared, well-documented feature of CrtA homologs across multiple bacterial genera, making this a legitimate family-level inference rather than a lookup of this single protein's annotation. The four distractor pathways involve entirely different enzyme families with incompatible architectures, so the family recognition meaningfully narrows the answer to carotenoid biosynthesis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct metabolic pathways with non-overlapping enzyme families. The Ala/Pro-rich C-terminus and catalytic domain architecture are incompatible with one-carbon metabolism, amino-acid degradation, or LPS O-antigen biosynthesis enzymes. Only carotenoid biosynthesis (CrtA) matches the observed sequence features."
  },
  "important_caveats": [
    "The EC number annotation in UniProt is transferred by similarity (ECO:0000250 from P17055, the R. sphaeroides strain 2.4.1 CrtA), but experimental validation exists via PubMed:20851979.",
    "The C-terminal Ala/Pro-rich region is a family-level CrtA feature but is not unique to carotenoid biosynthesis in all possible contexts; however, among the four offered choices, it clearly points to CrtA/carotenoid pathway.",
    "The reviewer-only evidence confirms the sequence matches UniProt Q3J189 exactly (SHA-256 match), but this accession was not available to the evaluated model."
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
  "benchmark_sequence_length": 324,
  "benchmark_sequence_sha256": "729a48d70d6bbe461cee74d78aec69eadd0836a65bfc944cb3241dac87281b34",
  "current_entry_audit": {
    "entryVersion": 76,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-11-08",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 324,
  "current_source_sequence_sha256": "729a48d70d6bbe461cee74d78aec69eadd0836a65bfc944cb3241dac87281b34",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q3J189",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "selected_historical_source_sequence_length": 324,
  "selected_historical_source_sequence_sha256": "729a48d70d6bbe461cee74d78aec69eadd0836a65bfc944cb3241dac87281b34",
  "selected_historical_version": {
    "accession": "Q3J189",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRTA_CERS4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q3J189\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":76,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-11-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rhodobacter sphaeroides\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Alphaproteobacteria\",\"Rhodobacterales\",\"Paracoccaceae\",\"Cereibacter\"],\"scientificName\":\"Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.)\",\"taxonId\":272943}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.15.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20851979\",\"source\":\"PubMed\"}],\"value\":\"Spheroidene monooxygenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"value\":\"Carotenoid biosynthesis; spheroidene biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lee P.C.\",\"Holtzapple E.\",\"Schmidt-Dannert C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20851979\"},{\"database\":\"DOI\",\"id\":\"10.1128/aem.01606-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"7328\",\"id\":\"20851979\",\"journal\":\"Appl. Environ. Microbiol.\",\"lastPage\":\"7331\",\"publicationDate\":\"2010\",\"title\":\"Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA expressed in Escherichia coli.\",\"volume\":\"76\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   CRTA_CERS4              Reviewed;         324 AA.\nAC   Q3J189; Q54790;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-NOV-2005, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:20851979};\nDE            EC=1.14.15.9 {ECO:0000250|UniProtKB:P17055};\nGN   Name=crtA {ECO:0000303|PubMed:7721699};\nGN   OrderedLocusNames=RHOS4_18770 {ECO:0000305};\nGN   ORFNames=RSP_0272 {ECO:0000312|EMBL:ABA79445.1};\nOS   Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG\nOS   31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (Rhodobacter\nOS   sphaeroides).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;\nOC   Rhodobacterales; Paracoccaceae; Cereibacter.\nOX   NCBI_TaxID=272943;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB38738.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 / NBRC 12203\nRC   / NCIMB 8253 / ATH 2.4.1.;\nRX   PubMed=7721699; DOI=10.1128/jb.177.8.2064-2073.1995;\nRA   Lang H.P., Cogdell R.J., Takaichi S., Hunter C.N.;\nRT   \"Complete DNA sequence, specific Tn5 insertion map, and gene assignment of\nRT   the carotenoid biosynthesis pathway of Rhodobacter sphaeroides.\";\nRL   J. Bacteriol. 177:2064-2073(1995).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, COFACTOR, SUBSTRATE SPECIFICITY, AND BIOTECHNOLOGY.\nRX   PubMed=20851979; DOI=10.1128/aem.01606-10;\nRA   Lee P.C., Holtzapple E., Schmidt-Dannert C.;\nRT   \"Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA\nRT   expressed in Escherichia coli.\";\nRL   Appl. Environ. Microbiol. 76:7328-7331(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Carotenoid biosynthesis; spheroidene biosynthesis.\nCC       {ECO:0000250|UniProtKB:P17055}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 199. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
