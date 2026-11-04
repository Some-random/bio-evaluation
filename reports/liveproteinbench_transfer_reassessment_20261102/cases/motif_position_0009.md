# motif_position_0009

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/motif_position_0009.txt)

**Task:** `motif_position`  
**Expected answer:** **D** — 301..304

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDDLFPLIFPSEPAQASGPYVEIIEQPKQRGMRFRYKCEGRSAGSIPGERSTDTTKTHPTIKINGYTGPGTVRISLVTKDPPHRPHPHELVGKDCRDGFYEAELCPDRCIHSFQNLGIQCVKKRDLEQAISQRIQTNNNPFQVPIEEQRGDYDLNAVRLCFQVTVRDPSGRPLRLTPVLSHPIFDNRAPNTAELKICRVNRNSGSCLGGDEIFLLCDKVQKEDIEVYFTGPGWEARGSFSQADVHRQVAIVFRTPPYADPSLQAPVRVSMQLRRPSDRELSEPMEFQYLPDTDDRHRIEEKRKRTYETFKSIMKKSPFNGPTEPRPPPRRIAVPSRGPTSVPKPAPQPYAFSTSLSTINFDEFSPMVLPPGQISNQALALAPSSAPVLAQTMVPSSAMVPSLAQPPAPVPVLAPGPPQSLSAPVPKSTQAGEGTLSEALLHLQFDADEDLGALLGNNTDPGVFTDLASVDNSEFQQLLNQGVAMSHSTAEPMLMEYPEAITRLVTGSQRPPDPAPATLGTSGLPNGLSGDEDFSSIADMDFSALLSQISS

[Multiple Choices]
A. 135..141
B. 74..119
C. 133..139
D. 301..304
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Motif Position Prediction, which is to identify the specific positions of a conserved motif within a protein sequence. A motif is a short, recurring pattern in protein sequences that is often associated with a specific function or structure. Based on the provided protein sequence, you will need to determine the start and end positions of the motif.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation places a nuclear localization signal at 301..304, matching D. This is a computationally supported annotation, not evidence of experimental validation.

Citations as saved: [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence at 301..304 is KRKR, a short, strongly basic cluster characteristic of nuclear localization signals. That transferable motif pattern makes D meaningfully distinguishable from the other offered intervals without needing the exact protein’s database record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A basic NLS-like sequence pattern directly supports D. The stem does not name the motif, but the KRKR cluster provides a credible sequence-based inference among these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The stem is underspecified because it does not identify the motif, but among the offered intervals D contains the distinctive KRKR NLS-like pattern; no other option is comparably supported.


### Important caveats

- The cited annotation is computationally supported; the supplied evidence does not establish experimental confirmation.
- The exact intended motif is not named in the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence at 301..304 is KRKR, a short, strongly basic cluster characteristic of nuclear localization signals. That transferable motif pattern makes D meaningfully distinguishable from the other offered intervals without needing the exact protein’s database record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A basic NLS-like sequence pattern directly supports D. The stem does not name the motif, but the KRKR cluster provides a credible sequence-based inference among these choices."
  },
  "case_id": "motif_position_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "H9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places a nuclear localization signal at 301..304, matching D. This is a computationally supported annotation, not evidence of experimental validation."
  },
  "important_caveats": [
    "The cited annotation is computationally supported; the supplied evidence does not establish experimental confirmation.",
    "The exact intended motif is not named in the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The stem is underspecified because it does not identify the motif, but among the offered intervals D contains the distinctive KRKR NLS-like pattern; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places a nuclear localization signal at 301..304, matching D. This is a computationally supported annotation, not evidence of experimental validation.",
    "evidence_ids": ["H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence at 301..304 is KRKR, a short, strongly basic cluster characteristic of nuclear localization signals. That transferable motif pattern makes D meaningfully distinguishable from the other offered intervals without needing the exact protein’s database record.",
    "missing_item_specific_fact": "",
    "reason": "A basic NLS-like sequence pattern directly supports D. The stem does not name the motif, but the KRKR cluster provides a credible sequence-based inference among these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The stem is underspecified because it does not identify the motif, but among the offered intervals D contains the distinctive KRKR NLS-like pattern; no other option is comparably supported."
  },
  "important_caveats": [
    "The cited annotation is computationally supported; the supplied evidence does not establish experimental confirmation.",
    "The exact intended motif is not named in the question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C12, H9) explicitly records a Nuclear Localization Signal motif at positions 301-304 with evidence code ECO:0000255 (PROSITE-ProRule). The sequence at positions 301-304 is KRKR, the well-characterized bipartite NLS of NF-κB p65/RelA, confirmed by extensive experimental literature. The sequence matches the benchmark input (SHA256 match confirmed in source_applicability).

Citations as saved: [C12](#evidence-c12), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains the Rel Homology Domain (RHD) characteristic of the NF-κB/Rel transcription factor family. NF-κB p65/RelA is one of the most extensively studied transcription factors, and its KRKR nuclear localization signal at positions 301-304 is textbook-level knowledge in signal transduction biology, appearing in virtually every NF-κB review and textbook. A knowledgeable model can: (1) recognize the RHD domain pattern → NF-κB/Rel family; (2) recall the well-known KRKR NLS motif of p65; (3) verify that positions 301-304 in the given sequence read KRKR. Among the offered choices, only D (301-304, KRKR) corresponds to a recognized conserved motif. Option B (74-119) is 46 residues, far too long for a 'motif.' Options A (135-141) and C (133-139) fall within the RHD domain but do not match any annotated or well-known motif pattern. The KRKR basic-residue cluster is itself a recognizable NLS signature independent of protein identity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The KRKR NLS at 301-304 in NF-κB p65 is canonical, extensively documented knowledge transferable from NF-κB biology. The RHD domain in the sequence enables family recognition, and the KRKR pattern is a classic NLS motif recognizable by its basic-residue composition. The distractor options are eliminable: B is too long for a motif, A and C do not correspond to any known conserved motif.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The question asks for 'the conserved motif' (singular). Among the four options, only D (301-304, KRKR NLS) corresponds to a well-known, experimentally validated conserved motif. The other options are either too long (B) or do not match recognized motifs (A, C). No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is a curated/computational annotation. However, the KRKR NLS in p65 is also supported by extensive experimental mutagenesis and importin-binding studies in the primary literature.
- The question does not specify which motif to identify, but the multiple-choice format and the fact that only one option matches a recognized conserved motif resolves this.
- The NLS position 301-304 is conserved between human and rat p65/RelA, so knowledge from human NF-κB literature transfers directly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains the Rel Homology Domain (RHD) characteristic of the NF-κB/Rel transcription factor family. NF-κB p65/RelA is one of the most extensively studied transcription factors, and its KRKR nuclear localization signal at positions 301-304 is textbook-level knowledge in signal transduction biology, appearing in virtually every NF-κB review and textbook. A knowledgeable model can: (1) recognize the RHD domain pattern → NF-κB/Rel family; (2) recall the well-known KRKR NLS motif of p65; (3) verify that positions 301-304 in the given sequence read KRKR. Among the offered choices, only D (301-304, KRKR) corresponds to a recognized conserved motif. Option B (74-119) is 46 residues, far too long for a 'motif.' Options A (135-141) and C (133-139) fall within the RHD domain but do not match any annotated or well-known motif pattern. The KRKR basic-residue cluster is itself a recognizable NLS signature independent of protein identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The KRKR NLS at 301-304 in NF-κB p65 is canonical, extensively documented knowledge transferable from NF-κB biology. The RHD domain in the sequence enables family recognition, and the KRKR pattern is a classic NLS motif recognizable by its basic-residue composition. The distractor options are eliminable: B is too long for a motif, A and C do not correspond to any known conserved motif."
  },
  "case_id": "motif_position_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C12",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C12, H9) explicitly records a Nuclear Localization Signal motif at positions 301-304 with evidence code ECO:0000255 (PROSITE-ProRule). The sequence at positions 301-304 is KRKR, the well-characterized bipartite NLS of NF-κB p65/RelA, confirmed by extensive experimental literature. The sequence matches the benchmark input (SHA256 match confirmed in source_applicability)."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is a curated/computational annotation. However, the KRKR NLS in p65 is also supported by extensive experimental mutagenesis and importin-binding studies in the primary literature.",
    "The question does not specify which motif to identify, but the multiple-choice format and the fact that only one option matches a recognized conserved motif resolves this.",
    "The NLS position 301-304 is conserved between human and rat p65/RelA, so knowledge from human NF-κB literature transfers directly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for 'the conserved motif' (singular). Among the four options, only D (301-304, KRKR NLS) corresponds to a well-known, experimentally validated conserved motif. The other options are either too long (B) or do not match recognized motifs (A, C). No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "motif_position_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C12, H9) explicitly records a Nuclear Localization Signal motif at positions 301-304 with evidence code ECO:0000255 (PROSITE-ProRule). The sequence at positions 301-304 is KRKR, the well-characterized bipartite NLS of NF-κB p65/RelA, confirmed by extensive experimental literature. The sequence matches the benchmark input (SHA256 match confirmed in source_applicability).",
    "evidence_ids": ["C12", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains the Rel Homology Domain (RHD) characteristic of the NF-κB/Rel transcription factor family. NF-κB p65/RelA is one of the most extensively studied transcription factors, and its KRKR nuclear localization signal at positions 301-304 is textbook-level knowledge in signal transduction biology, appearing in virtually every NF-κB review and textbook. A knowledgeable model can: (1) recognize the RHD domain pattern → NF-κB/Rel family; (2) recall the well-known KRKR NLS motif of p65; (3) verify that positions 301-304 in the given sequence read KRKR. Among the offered choices, only D (301-304, KRKR) corresponds to a recognized conserved motif. Option B (74-119) is 46 residues, far too long for a 'motif.' Options A (135-141) and C (133-139) fall within the RHD domain but do not match any annotated or well-known motif pattern. The KRKR basic-residue cluster is itself a recognizable NLS signature independent of protein identity.",
    "missing_item_specific_fact": "",
    "reason": "The KRKR NLS at 301-304 in NF-κB p65 is canonical, extensively documented knowledge transferable from NF-κB biology. The RHD domain in the sequence enables family recognition, and the KRKR pattern is a classic NLS motif recognizable by its basic-residue composition. The distractor options are eliminable: B is too long for a motif, A and C do not correspond to any known conserved motif."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for 'the conserved motif' (singular). Among the four options, only D (301-304, KRKR NLS) corresponds to a well-known, experimentally validated conserved motif. The other options are either too long (B) or do not match recognized motifs (A, C). No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is a curated/computational annotation. However, the KRKR NLS in p65 is also supported by extensive experimental mutagenesis and importin-binding studies in the primary literature.",
    "The question does not specify which motif to identify, but the multiple-choice format and the fact that only one option matches a recognized conserved motif resolves this.",
    "The NLS position 301-304 is conserved between human and rat p65/RelA, so knowledge from human NF-κB literature transfers directly."
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
  "benchmark_sequence_length": 550,
  "benchmark_sequence_sha256": "e11a943a896fdb8d7c09130ae5ecbbe04feeeaaa317e97b890245ddc50786af2",
  "current_entry_audit": {
    "entryVersion": 177,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 550,
  "current_source_sequence_sha256": "e11a943a896fdb8d7c09130ae5ecbbe04feeeaaa317e97b890245ddc50786af2",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 175,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q7TQN4",
  "selected_historical_entry_version": 175,
  "selected_historical_record_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "selected_historical_source_sequence_length": 550,
  "selected_historical_source_sequence_sha256": "e11a943a896fdb8d7c09130ae5ecbbe04feeeaaa317e97b890245ddc50786af2",
  "selected_historical_version": {
    "accession": "Q7TQN4",
    "database": "Swiss-Prot",
    "entryVersion": 175,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TF65_RAT",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q7TQN4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":177,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Nuclear factor NF-kappa-B p65 subunit\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Transcription factor p65\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"RHD\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00265\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":190},\"start\":{\"modifier\":\"EXACT\",\"value\":16}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":60},\"start\":{\"modifier\":\"EXACT\",\"value\":41}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":345},\"start\":{\"modifier\":\"EXACT\",\"value\":311}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Transcriptional activation domain 3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q04207\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":388},\"start\":{\"modifier\":\"EXACT\",\"value\":342}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Transcriptional activation domain 1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q04206\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":476},\"start\":{\"modifier\":\"EXACT\",\"value\":414}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":531},\"start\":{\"modifier\":\"EXACT\",\"value\":505}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Transcriptional activation domain 2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q04207\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":550},\"start\":{\"modifier\":\"EXACT\",\"value\":520}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Nuclear localization signal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":304},\"start\":{\"modifier\":\"EXACT\",\"value\":301}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7TQN4.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"9aaTAD\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":543},\"start\":{\"modifier\":\"EXACT\",\"value\":535}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:31:52.888470+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce95521447f3ca9467dcc36e1a3473a14ea42f53ec7008c56245b30bf2fb4ede",
  "url": "https://rest.uniprot.org/uniprotkb/Q7TQN4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H1",
  "excerpt": "ID   TF65_RAT                Reviewed;         550 AA.\nAC   Q7TQN4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2003, sequence version 1.\nDT   28-JAN-2026, entry version 175.\nDE   RecName: Full=Transcription factor p65;\nDE   AltName: Full=Nuclear factor NF-kappa-B p65 subunit;\nGN   Name=Rela {ECO:0000312|RGD:727889}; Synonyms=nos2;\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H2",
  "excerpt": "FT   DOMAIN          16..190\nFT                   /note=\"RHD\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00265\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 418-420",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H3",
  "excerpt": "FT   REGION          41..60\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 421-423",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H4",
  "excerpt": "FT   REGION          311..345\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 424-426",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H5",
  "excerpt": "FT   REGION          342..388\nFT                   /note=\"Transcriptional activation domain 3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q04207\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 427-429",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H6",
  "excerpt": "FT   REGION          414..476\nFT                   /note=\"Transcriptional activation domain 1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q04206\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 430-432",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H7",
  "excerpt": "FT   REGION          505..531\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 433-435",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H8",
  "excerpt": "FT   REGION          520..550\nFT                   /note=\"Transcriptional activation domain 2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q04207\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 436-438",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H9",
  "excerpt": "FT   MOTIF           301..304\nFT                   /note=\"Nuclear localization signal\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 439-441",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175)

```json
{
  "entry_version": 175,
  "evidence_id": "H10",
  "excerpt": "FT   MOTIF           535..543\nFT                   /note=\"9aaTAD\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.408337+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 442-444",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d41f7a5862a46cbf21435ce753b71b87dfc68f3a6c53341d119c80ad3767abee",
  "url": "https://rest.uniprot.org/unisave/Q7TQN4?format=txt&versions=175"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/motif_position.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
