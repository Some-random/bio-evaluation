# motif_position_0012

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/motif_position_0012.txt)

**Task:** `motif_position`  
**Expected answer:** **B** — 380..383

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIVKISWPKNNITSECFRRFGSFKRRSKSKKMSAFIEETKSLLPRIAFIACGCFSPPTPMHLRMFEIAKDHFEMQGTHRVVGGIISPTHDSYGKKGLASALDRCAMVKLATQSSNWIRLSDWEVHQNQWMRTQAVLQHHQNYINNHINSGGGGGDDGENTHLPGWLPRGLHDSRDPVHLKLLCGADLLESFAVPGLWAEADIEDIVANHGLVVITRAGSNPGKFIFDSDILTKYQSNITLITNWVPNEVSSTLIRRLLGRGQSVKYLLDDLVLEYIKRQRLFNFKSKYITDAVRPNHLLFNHAYTDNNKNANSYSIGDQLEQDMDESDTPSPQLQHTPTSRVFCCGEVPLRGSKVLRSGPGQAVQVITMQADEKEESQAKKQKISQVQL

[Multiple Choices]
A. 6..14
B. 380..383
C. 9..19
D. 216..220
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

> The supplied sequence matches the source sequence, and both the current and archived UniProt records annotate positions 380–383 as a nuclear localization signal. The annotation cites experimental evidence, though the primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence at positions 380–383 is KKQK, a compact Lys-rich pattern consistent with a classical nuclear localization signal (often a short cluster of basic residues). That transferable motif knowledge makes B more credible than the other offered segments, which are less concentrated in basic residues.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The exact annotation is absent from the prompt, but the offered choices can be meaningfully distinguished from the sequence using transferable knowledge about basic-residue nuclear localization signals. This supports a probabilistic inference without requiring recall of this protein’s database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered segments, 380–383 is the clearest compact basic cluster consistent with a nuclear localization signal.


### Important caveats

- The source annotation supports the keyed coordinates and labels the evidence experimental, but the cited primary study was not independently validated here.
- The inference from the sequence pattern is meaningful but is not, by itself, experimental proof of localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence at positions 380–383 is KKQK, a compact Lys-rich pattern consistent with a classical nuclear localization signal (often a short cluster of basic residues). That transferable motif knowledge makes B more credible than the other offered segments, which are less concentrated in basic residues.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The exact annotation is absent from the prompt, but the offered choices can be meaningfully distinguished from the sequence using transferable knowledge about basic-residue nuclear localization signals. This supports a probabilistic inference without requiring recall of this protein’s database entry."
  },
  "case_id": "motif_position_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence, and both the current and archived UniProt records annotate positions 380–383 as a nuclear localization signal. The annotation cites experimental evidence, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The source annotation supports the keyed coordinates and labels the evidence experimental, but the cited primary study was not independently validated here.",
    "The inference from the sequence pattern is meaningful but is not, by itself, experimental proof of localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered segments, 380–383 is the clearest compact basic cluster consistent with a nuclear localization signal."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence, and both the current and archived UniProt records annotate positions 380–383 as a nuclear localization signal. The annotation cites experimental evidence, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence at positions 380–383 is KKQK, a compact Lys-rich pattern consistent with a classical nuclear localization signal (often a short cluster of basic residues). That transferable motif knowledge makes B more credible than the other offered segments, which are less concentrated in basic residues.",
    "missing_item_specific_fact": "",
    "reason": "The exact annotation is absent from the prompt, but the offered choices can be meaningfully distinguished from the sequence using transferable knowledge about basic-residue nuclear localization signals. This supports a probabilistic inference without requiring recall of this protein’s database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered segments, 380–383 is the clearest compact basic cluster consistent with a nuclear localization signal."
  },
  "important_caveats": [
    "The source annotation supports the keyed coordinates and labels the evidence experimental, but the cited primary study was not independently validated here.",
    "The inference from the sequence pattern is meaningful but is not, by itself, experimental proof of localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VC03 (Drosophila NMNAT, 389 aa) annotates a Nuclear Localization Signal motif at positions 380-383 with experimental evidence (ECO:0000269|PubMed:26616331, Ruan et al. 2015). The sequence at positions 380-383 is KKQK, a basic cluster consistent with a classical monopartite NLS. The sequence matches the benchmark input exactly (SHA256 confirmed). The annotation is supported by mutagenesis of LYS-380 reported in the same paper.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C8](#evidence-c8), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Among the four options, only B (positions 380-383: KKQK) exhibits a recognizable protein motif pattern — a short cluster of basic residues (K,K,Q,K) characteristic of a classical monopartite Nuclear Localization Signal (NLS). NLS motifs are well-established transferable knowledge: they consist of 4-8 predominantly basic residues (Lys, Arg) often in clusters like PKKKRKV or similar. Option A (6-14: SWPKNNITS), C (9-19: KNNITSECFRR), and D (216-220: RAGSN) do not match any standard conserved motif pattern (no catalytic motif, no nucleotide-binding motif, no recognizable structural motif). A model familiar with NLS patterns can identify KKQK as a basic cluster consistent with nuclear targeting and eliminate the other three options as lacking recognizable motif character. The C-terminal location of a short basic cluster is also a common NLS placement pattern learned from many proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The key transferable feature is recognition of a basic amino acid cluster (KKQK) as an NLS-like motif. This is standard knowledge from many proteins (SV40 T-antigen NLS, nucleoplasmin NLS, etc.). The other three options present sequences (SWPKNNITS, KNNITSECFRR, RAGSN) that do not correspond to any well-known conserved motif family, allowing elimination. The question does not require knowing this specific protein's annotation; pattern recognition of the basic cluster versus non-motif sequences distinguishes B from A, C, D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the question says 'a conserved motif' without specifying which one, among the four offered options only B shows a recognizable motif pattern (basic NLS-like cluster). The N-terminal basic region (positions ~23-31: FKRRSKSKKM) is a stronger basic cluster but is not offered as an option. Among the actual choices, B is the only one with clear motif character, making the alternatives distinguishable.


### Important caveats

- The question does not specify which motif is being asked about, relying on the model to identify the only recognizable motif among the four options.
- The N-terminal region (positions 21-31) contains a stronger basic cluster (FKRRSKSKKM) that could also be NLS-like, but it is not among the options.
- The 'conserved' qualifier is not directly verifiable from a single sequence without alignment data.
- The NLS annotation is experimentally supported (mutagenesis of Lys-380, PubMed:26616331), not merely computational prediction.
- The sequence is confirmed to match Q9VC03 (Drosophila NMNAT) at 389 residues with exact SHA256 match.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Among the four options, only B (positions 380-383: KKQK) exhibits a recognizable protein motif pattern — a short cluster of basic residues (K,K,Q,K) characteristic of a classical monopartite Nuclear Localization Signal (NLS). NLS motifs are well-established transferable knowledge: they consist of 4-8 predominantly basic residues (Lys, Arg) often in clusters like PKKKRKV or similar. Option A (6-14: SWPKNNITS), C (9-19: KNNITSECFRR), and D (216-220: RAGSN) do not match any standard conserved motif pattern (no catalytic motif, no nucleotide-binding motif, no recognizable structural motif). A model familiar with NLS patterns can identify KKQK as a basic cluster consistent with nuclear targeting and eliminate the other three options as lacking recognizable motif character. The C-terminal location of a short basic cluster is also a common NLS placement pattern learned from many proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The key transferable feature is recognition of a basic amino acid cluster (KKQK) as an NLS-like motif. This is standard knowledge from many proteins (SV40 T-antigen NLS, nucleoplasmin NLS, etc.). The other three options present sequences (SWPKNNITS, KNNITSECFRR, RAGSN) that do not correspond to any well-known conserved motif family, allowing elimination. The question does not require knowing this specific protein's annotation; pattern recognition of the basic cluster versus non-motif sequences distinguishes B from A, C, D."
  },
  "case_id": "motif_position_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (Drosophila NMNAT, 389 aa) annotates a Nuclear Localization Signal motif at positions 380-383 with experimental evidence (ECO:0000269|PubMed:26616331, Ruan et al. 2015). The sequence at positions 380-383 is KKQK, a basic cluster consistent with a classical monopartite NLS. The sequence matches the benchmark input exactly (SHA256 confirmed). The annotation is supported by mutagenesis of LYS-380 reported in the same paper."
  },
  "important_caveats": [
    "The question does not specify which motif is being asked about, relying on the model to identify the only recognizable motif among the four options.",
    "The N-terminal region (positions 21-31) contains a stronger basic cluster (FKRRSKSKKM) that could also be NLS-like, but it is not among the options.",
    "The 'conserved' qualifier is not directly verifiable from a single sequence without alignment data.",
    "The NLS annotation is experimentally supported (mutagenesis of Lys-380, PubMed:26616331), not merely computational prediction.",
    "The sequence is confirmed to match Q9VC03 (Drosophila NMNAT) at 389 residues with exact SHA256 match."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the question says 'a conserved motif' without specifying which one, among the four offered options only B shows a recognizable motif pattern (basic NLS-like cluster). The N-terminal basic region (positions ~23-31: FKRRSKSKKM) is a stronger basic cluster but is not offered as an option. Among the actual choices, B is the only one with clear motif character, making the alternatives distinguishable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "motif_position_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (Drosophila NMNAT, 389 aa) annotates a Nuclear Localization Signal motif at positions 380-383 with experimental evidence (ECO:0000269|PubMed:26616331, Ruan et al. 2015). The sequence at positions 380-383 is KKQK, a basic cluster consistent with a classical monopartite NLS. The sequence matches the benchmark input exactly (SHA256 confirmed). The annotation is supported by mutagenesis of LYS-380 reported in the same paper.",
    "evidence_ids": ["C5", "H5", "C8", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Among the four options, only B (positions 380-383: KKQK) exhibits a recognizable protein motif pattern — a short cluster of basic residues (K,K,Q,K) characteristic of a classical monopartite Nuclear Localization Signal (NLS). NLS motifs are well-established transferable knowledge: they consist of 4-8 predominantly basic residues (Lys, Arg) often in clusters like PKKKRKV or similar. Option A (6-14: SWPKNNITS), C (9-19: KNNITSECFRR), and D (216-220: RAGSN) do not match any standard conserved motif pattern (no catalytic motif, no nucleotide-binding motif, no recognizable structural motif). A model familiar with NLS patterns can identify KKQK as a basic cluster consistent with nuclear targeting and eliminate the other three options as lacking recognizable motif character. The C-terminal location of a short basic cluster is also a common NLS placement pattern learned from many proteins.",
    "missing_item_specific_fact": "",
    "reason": "The key transferable feature is recognition of a basic amino acid cluster (KKQK) as an NLS-like motif. This is standard knowledge from many proteins (SV40 T-antigen NLS, nucleoplasmin NLS, etc.). The other three options present sequences (SWPKNNITS, KNNITSECFRR, RAGSN) that do not correspond to any well-known conserved motif family, allowing elimination. The question does not require knowing this specific protein's annotation; pattern recognition of the basic cluster versus non-motif sequences distinguishes B from A, C, D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the question says 'a conserved motif' without specifying which one, among the four offered options only B shows a recognizable motif pattern (basic NLS-like cluster). The N-terminal basic region (positions ~23-31: FKRRSKSKKM) is a stronger basic cluster but is not offered as an option. Among the actual choices, B is the only one with clear motif character, making the alternatives distinguishable."
  },
  "important_caveats": [
    "The question does not specify which motif is being asked about, relying on the model to identify the only recognizable motif among the four options.",
    "The N-terminal region (positions 21-31) contains a stronger basic cluster (FKRRSKSKKM) that could also be NLS-like, but it is not among the options.",
    "The 'conserved' qualifier is not directly verifiable from a single sequence without alignment data.",
    "The NLS annotation is experimentally supported (mutagenesis of Lys-380, PubMed:26616331), not merely computational prediction.",
    "The sequence is confirmed to match Q9VC03 (Drosophila NMNAT) at 389 residues with exact SHA256 match."
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
  "benchmark_sequence_length": 389,
  "benchmark_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "current_entry_audit": {
    "entryVersion": 189,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 4
  },
  "current_record_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 389,
  "current_source_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 187,
      "exact_sequence_comparison": "matched",
      "sequence_version": 4
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VC03",
  "selected_historical_entry_version": 187,
  "selected_historical_record_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "selected_historical_source_sequence_length": 389,
  "selected_historical_source_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "selected_historical_version": {
    "accession": "Q9VC03",
    "database": "Swiss-Prot",
    "entryVersion": 187,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMNA_DROME",
    "sequenceVersion": 4
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VC03\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":189,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":4}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039254\",\"source\":\"FlyBase\"}],\"value\":\"Nicotinamide mononucleotide adenylyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039254\",\"source\":\"FlyBase\"}],\"value\":\"dNmnat\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17132048\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19403820\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"value\":\"2.7.7.1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"value\":\"2.7.7.18\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"value\":\"Nicotinamide-nucleotide adenylyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nuclear localization signal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":383},\"start\":{\"modifier\":\"EXACT\",\"value\":380}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhai R.G.\",\"Cao Y.\",\"Hiesinger P.R.\",\"Zhou Y.\",\"Mehta S.Q.\",\"Schulze K.L.\",\"Verstreken P.\",\"Bellen H.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17132048\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pbio.0040416\"}],\"citationType\":\"journal article\",\"firstPage\":\"e416\",\"id\":\"17132048\",\"journal\":\"PLoS Biol.\",\"lastPage\":\"e416\",\"publicationDate\":\"2006\",\"title\":\"Drosophila NMNAT maintains neural integrity independent of its NAD synthesis activity.\",\"volume\":\"4\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Sasaki Y.\",\"Vohra B.P.\",\"Lund F.E.\",\"Milbrandt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19403820\"},{\"database\":\"DOI\",\"id\":\"10.1523/jneurosci.5469-08.2009\"}],\"citationType\":\"journal article\",\"firstPage\":\"5525\",\"id\":\"19403820\",\"journal\":\"J. Neurosci.\",\"lastPage\":\"5535\",\"publicationDate\":\"2009\",\"title\":\"Nicotinamide mononucleotide adenylyl transferase-mediated axonal protection requires enzymatic activity but not increased levels of neuronal nicotinamide adenine dinucleotide.\",\"volume\":\"29\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Ruan K.\",\"Zhu Y.\",\"Li C.\",\"Brazill J.M.\",\"Zhai R.G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26616331\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms10057\"}],\"citationType\":\"journal article\",\"firstPage\":\"10057\",\"id\":\"26616331\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"10057\",\"publicationDate\":\"2015\",\"title\":\"Alternative splicing of Drosophila Nmnat functions as a switch to enhance neuroprotection under stress.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":10,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"ALTERNATIVE SPLICING\",\"INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS\",\"NUCLEAR LOCALIZATION SIGNAL\",\"MUTAGENESIS OF LYS-380\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/9",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H1",
  "excerpt": "ID   NMNA_DROME              Reviewed;         389 AA.\nAC   Q9VC03; A0A0B4KHH7; Q7KS06; Q8T405;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 4.\nDT   28-JAN-2026, entry version 187.\nDE   RecName: Full=Nicotinamide-nucleotide adenylyltransferase {ECO:0000255|RuleBase:RU362021};\nDE            EC=2.7.7.1 {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048, ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\nDE            EC=2.7.7.18 {ECO:0000255|RuleBase:RU362021};\nDE   AltName: Full=Nicotinamide mononucleotide adenylyltransferase {ECO:0000312|FlyBase:FBgn0039254};\nDE            Short=dNmnat {ECO:0000312|FlyBase:FBgn0039254};\nGN   Name=Nmnat {ECO:0000303|PubMed:17132048, ECO:0000312|FlyBase:FBgn0039254};\nGN   ORFNames=CG13645 {ECO:0000312|FlyBase:FBgn0039254};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H2",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, TISSUE SPECIFICITY,\nRP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255.\nRX   PubMed=17132048; DOI=10.1371/journal.pbio.0040416;\nRA   Zhai R.G., Cao Y., Hiesinger P.R., Zhou Y., Mehta S.Q., Schulze K.L.,\nRA   Verstreken P., Bellen H.J.;\nRT   \"Drosophila NMNAT maintains neural integrity independent of its NAD\nRT   synthesis activity.\";\nRL   PLoS Biol. 4:e416-e416(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H3",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND SUBCELLULAR LOCATION.\nRX   PubMed=19403820; DOI=10.1523/jneurosci.5469-08.2009;\nRA   Sasaki Y., Vohra B.P., Lund F.E., Milbrandt J.;\nRT   \"Nicotinamide mononucleotide adenylyl transferase-mediated axonal\nRT   protection requires enzymatic activity but not increased levels of neuronal\nRT   nicotinamide adenine dinucleotide.\";\nRL   J. Neurosci. 29:5525-5535(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H4",
  "excerpt": "RN   [10] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, ALTERNATIVE SPLICING,\nRP   INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS, NUCLEAR LOCALISAION SIGNAL,\nRP   AND MUTAGENESIS OF LYS-380.\nRX   PubMed=26616331; DOI=10.1038/ncomms10057;\nRA   Ruan K., Zhu Y., Li C., Brazill J.M., Zhai R.G.;\nRT   \"Alternative splicing of Drosophila Nmnat functions as a switch to enhance\nRT   neuroprotection under stress.\";\nRL   Nat. Commun. 6:10057-10057(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H5",
  "excerpt": "FT   MOTIF           380..383\nFT                   /note=\"Nuclear localization signal\"\nFT                   /evidence=\"ECO:0000269|PubMed:26616331\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 329-331",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/motif_position.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
