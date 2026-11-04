# GO_biological_process_0092

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0092.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **C** — chromatin remodeling

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPLTAESAAQQIQDRLKDIQQNIHNVDEERRRAENSIASLVRSLHATNQKVKPLLKASLTEAAQEEATIRAALAKIHEIRSIRNERRIQARNAGNKEAIRRGALMKMVQLSAQTLPLFVGKLGERAPALCGAIPAEGNYVAKVGDNVAALAKGIDEEENWILAEVVQFLHRQNKYDVIDIDEEQKDRHVLSKRKVIPLPLMRANPETDGHALFPKDTVVMALYPQTTCFYKAIVHRLPQTATEDYEVLFEDSSYTNGYAEPLPVAQRYVIAYRPTKKGAGSGSGNLSSA

[Multiple Choices]
A. tRNA methylation
B. cellular response to angiotensin
C. chromatin remodeling
D. mitochondrial respiratory chain complex assembly
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record identifies the protein as a SAGA-associated factor and reports that it is a component of histone acetyltransferase complexes. It also carries a chromatin remodeling GO annotation with IDA evidence. These support choice C for this sequence, while the annotation is not itself proof that every aspect of the broad GO term was independently experimentally established.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence's compact, largely soluble architecture is compatible with a nuclear chromatin-complex subunit rather than a membrane receptor, mitochondrial respiratory-chain component, or catalytic tRNA methyltransferase. More specifically, a recognizable Sgf29-like Tudor-domain reader architecture would, by transferable family knowledge, point toward SAGA-associated histone modification and chromatin regulation. That meaningfully favors chromatin remodeling among the offered choices, though the sequence alone may not establish the precise GO annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and the known roles of chromatin-associated Tudor-domain/SAGA proteins can distinguish C from these alternatives without recalling this exact protein's recorded annotation. The inference is probabilistic, not a complete independent demonstration of the GO term.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe substantially different processes, and the available family-level inference favors chromatin remodeling; none of the other options is comparably supported.


### Important caveats

- The reviewer-only sequence-matched GO annotation supports the key but was not an original input.
- The sequence-based family inference is not conclusive, and chromatin remodeling is a broad process label for a protein associated with histone-modifying complexes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's compact, largely soluble architecture is compatible with a nuclear chromatin-complex subunit rather than a membrane receptor, mitochondrial respiratory-chain component, or catalytic tRNA methyltransferase. More specifically, a recognizable Sgf29-like Tudor-domain reader architecture would, by transferable family knowledge, point toward SAGA-associated histone modification and chromatin regulation. That meaningfully favors chromatin remodeling among the offered choices, though the sequence alone may not establish the precise GO annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the known roles of chromatin-associated Tudor-domain/SAGA proteins can distinguish C from these alternatives without recalling this exact protein's recorded annotation. The inference is probabilistic, not a complete independent demonstration of the GO term."
  },
  "case_id": "GO_biological_process_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as a SAGA-associated factor and reports that it is a component of histone acetyltransferase complexes. It also carries a chromatin remodeling GO annotation with IDA evidence. These support choice C for this sequence, while the annotation is not itself proof that every aspect of the broad GO term was independently experimentally established."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched GO annotation supports the key but was not an original input.",
    "The sequence-based family inference is not conclusive, and chromatin remodeling is a broad process label for a protein associated with histone-modifying complexes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different processes, and the available family-level inference favors chromatin remodeling; none of the other options is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as a SAGA-associated factor and reports that it is a component of histone acetyltransferase complexes. It also carries a chromatin remodeling GO annotation with IDA evidence. These support choice C for this sequence, while the annotation is not itself proof that every aspect of the broad GO term was independently experimentally established.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence's compact, largely soluble architecture is compatible with a nuclear chromatin-complex subunit rather than a membrane receptor, mitochondrial respiratory-chain component, or catalytic tRNA methyltransferase. More specifically, a recognizable Sgf29-like Tudor-domain reader architecture would, by transferable family knowledge, point toward SAGA-associated histone modification and chromatin regulation. That meaningfully favors chromatin remodeling among the offered choices, though the sequence alone may not establish the precise GO annotation.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the known roles of chromatin-associated Tudor-domain/SAGA proteins can distinguish C from these alternatives without recalling this exact protein's recorded annotation. The inference is probabilistic, not a complete independent demonstration of the GO term."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different processes, and the available family-level inference favors chromatin remodeling; none of the other options is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched GO annotation supports the key but was not an original input.",
    "The sequence-based family inference is not conclusive, and chromatin remodeling is a broad process label for a protein associated with histone-modifying complexes."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q9W2I4, Sgf29_DROME) is directly annotated with GO:0006338 (chromatin remodeling) with IDA evidence (PubMed:18327268, FlyBase). The protein is experimentally confirmed as a component of the SAGA and CHAT histone acetyltransferase complexes that acetylate histone H3 (multiple PubMed references: 16980620, 20008933, 21764853, 24493646, 30559249). Histone acetylation is a well-defined mechanism of chromatin remodeling per the GO:0006338 definition ('A dynamic process of chromatin reorganization resulting in changes to chromatin structure'). The IDA evidence code confirms direct experimental demonstration.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H7](#evidence-h7), [H8](#evidence-h8), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a histone fold domain (approximately residues 30-110), recognizable by the characteristic alternating pattern of hydrophobic and charged residues forming three alpha helices connected by loops (e.g., 'ERRRAENSIASLVRSLHATNQKVKPLLKASLTEAAQEEATIRAALAKIHEIRSIRNERR'). Histone fold domains are a hallmark of chromatin-associated proteins, found in core histones, histone-fold TAFs (TAF6, TAF9), Spt proteins, and SAGA complex subunits. Additionally, the C-terminal region (~residues 180-289) shows features consistent with a WD40-like beta-propeller domain, another motif common in chromatin regulators (e.g., WDR5 in SAGA). This domain architecture strongly points to chromatin-related function. Conversely: (A) tRNA methylation requires methyltransferase motifs (Rossmann fold, SAM-binding motifs I/II/X/IV) which are absent; (B) cellular response to angiotensin requires receptor/signaling components (GPCR 7TM, kinase, G-protein interaction) which are absent; (D) mitochondrial respiratory chain complex assembly requires an N-terminal mitochondrial targeting transit peptide (amphipathic helix with positively charged residues) and assembly factor domains, none of which are present. The histone fold + WD40 combination is a well-established family-level signature for chromatin remodeling/transcription coactivator complexes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the histone fold domain from its sequence pattern (alternating hydrophobic/charged residues in a helix-loop-helix-loop-helix arrangement) and connect it to chromatin biology via well-established family knowledge (histones, TAFs, Spt proteins, SAGA subunits all share this fold). The WD40-like C-terminal region further supports a chromatin-regulator identity. The absence of methyltransferase, signaling, or mitochondrial-targeting features cleanly eliminates options A, B, and D. This is a legitimate transfer inference from domain architecture knowledge learned across many chromatin-associated proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only C (chromatin remodeling) is consistent with a histone-fold-containing, WD40-containing nuclear protein. The other three options require entirely different domain architectures (methyltransferase, GPCR/signaling, mitochondrial targeting) that are clearly absent from the sequence. No ambiguity exists among the offered alternatives.


### Important caveats

- The histone fold domain recognition from raw sequence is a pattern-matching task that may vary in reliability depending on model training, though the alternating hydrophobic/charged pattern is well-documented in structural biology literature.
- GO:0006338 (chromatin remodeling) is a broad term encompassing histone modifications, nucleosome repositioning, and ATP-dependent remodeling. The SAGA complex's primary role is histone acetylation for transcription, which falls under this umbrella per the GO definition.
- The reviewer-only evidence confirms the annotation with IDA (direct assay) evidence, but this was not available to the evaluated model. The reasoning argument relies solely on sequence features and transferable domain knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a histone fold domain (approximately residues 30-110), recognizable by the characteristic alternating pattern of hydrophobic and charged residues forming three alpha helices connected by loops (e.g., 'ERRRAENSIASLVRSLHATNQKVKPLLKASLTEAAQEEATIRAALAKIHEIRSIRNERR'). Histone fold domains are a hallmark of chromatin-associated proteins, found in core histones, histone-fold TAFs (TAF6, TAF9), Spt proteins, and SAGA complex subunits. Additionally, the C-terminal region (~residues 180-289) shows features consistent with a WD40-like beta-propeller domain, another motif common in chromatin regulators (e.g., WDR5 in SAGA). This domain architecture strongly points to chromatin-related function. Conversely: (A) tRNA methylation requires methyltransferase motifs (Rossmann fold, SAM-binding motifs I/II/X/IV) which are absent; (B) cellular response to angiotensin requires receptor/signaling components (GPCR 7TM, kinase, G-protein interaction) which are absent; (D) mitochondrial respiratory chain complex assembly requires an N-terminal mitochondrial targeting transit peptide (amphipathic helix with positively charged residues) and assembly factor domains, none of which are present. The histone fold + WD40 combination is a well-established family-level signature for chromatin remodeling/transcription coactivator complexes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the histone fold domain from its sequence pattern (alternating hydrophobic/charged residues in a helix-loop-helix-loop-helix arrangement) and connect it to chromatin biology via well-established family knowledge (histones, TAFs, Spt proteins, SAGA subunits all share this fold). The WD40-like C-terminal region further supports a chromatin-regulator identity. The absence of methyltransferase, signaling, or mitochondrial-targeting features cleanly eliminates options A, B, and D. This is a legitimate transfer inference from domain architecture knowledge learned across many chromatin-associated proteins."
  },
  "case_id": "GO_biological_process_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H7",
      "H8",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q9W2I4, Sgf29_DROME) is directly annotated with GO:0006338 (chromatin remodeling) with IDA evidence (PubMed:18327268, FlyBase). The protein is experimentally confirmed as a component of the SAGA and CHAT histone acetyltransferase complexes that acetylate histone H3 (multiple PubMed references: 16980620, 20008933, 21764853, 24493646, 30559249). Histone acetylation is a well-defined mechanism of chromatin remodeling per the GO:0006338 definition ('A dynamic process of chromatin reorganization resulting in changes to chromatin structure'). The IDA evidence code confirms direct experimental demonstration."
  },
  "important_caveats": [
    "The histone fold domain recognition from raw sequence is a pattern-matching task that may vary in reliability depending on model training, though the alternating hydrophobic/charged pattern is well-documented in structural biology literature.",
    "GO:0006338 (chromatin remodeling) is a broad term encompassing histone modifications, nucleosome repositioning, and ATP-dependent remodeling. The SAGA complex's primary role is histone acetylation for transcription, which falls under this umbrella per the GO definition.",
    "The reviewer-only evidence confirms the annotation with IDA (direct assay) evidence, but this was not available to the evaluated model. The reasoning argument relies solely on sequence features and transferable domain knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only C (chromatin remodeling) is consistent with a histone-fold-containing, WD40-containing nuclear protein. The other three options require entirely different domain architectures (methyltransferase, GPCR/signaling, mitochondrial targeting) that are clearly absent from the sequence. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q9W2I4, Sgf29_DROME) is directly annotated with GO:0006338 (chromatin remodeling) with IDA evidence (PubMed:18327268, FlyBase). The protein is experimentally confirmed as a component of the SAGA and CHAT histone acetyltransferase complexes that acetylate histone H3 (multiple PubMed references: 16980620, 20008933, 21764853, 24493646, 30559249). Histone acetylation is a well-defined mechanism of chromatin remodeling per the GO:0006338 definition ('A dynamic process of chromatin reorganization resulting in changes to chromatin structure'). The IDA evidence code confirms direct experimental demonstration.",
    "evidence_ids": ["C5", "C6", "H7", "H8", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a histone fold domain (approximately residues 30-110), recognizable by the characteristic alternating pattern of hydrophobic and charged residues forming three alpha helices connected by loops (e.g., 'ERRRAENSIASLVRSLHATNQKVKPLLKASLTEAAQEEATIRAALAKIHEIRSIRNERR'). Histone fold domains are a hallmark of chromatin-associated proteins, found in core histones, histone-fold TAFs (TAF6, TAF9), Spt proteins, and SAGA complex subunits. Additionally, the C-terminal region (~residues 180-289) shows features consistent with a WD40-like beta-propeller domain, another motif common in chromatin regulators (e.g., WDR5 in SAGA). This domain architecture strongly points to chromatin-related function. Conversely: (A) tRNA methylation requires methyltransferase motifs (Rossmann fold, SAM-binding motifs I/II/X/IV) which are absent; (B) cellular response to angiotensin requires receptor/signaling components (GPCR 7TM, kinase, G-protein interaction) which are absent; (D) mitochondrial respiratory chain complex assembly requires an N-terminal mitochondrial targeting transit peptide (amphipathic helix with positively charged residues) and assembly factor domains, none of which are present. The histone fold + WD40 combination is a well-established family-level signature for chromatin remodeling/transcription coactivator complexes.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the histone fold domain from its sequence pattern (alternating hydrophobic/charged residues in a helix-loop-helix-loop-helix arrangement) and connect it to chromatin biology via well-established family knowledge (histones, TAFs, Spt proteins, SAGA subunits all share this fold). The WD40-like C-terminal region further supports a chromatin-regulator identity. The absence of methyltransferase, signaling, or mitochondrial-targeting features cleanly eliminates options A, B, and D. This is a legitimate transfer inference from domain architecture knowledge learned across many chromatin-associated proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only C (chromatin remodeling) is consistent with a histone-fold-containing, WD40-containing nuclear protein. The other three options require entirely different domain architectures (methyltransferase, GPCR/signaling, mitochondrial targeting) that are clearly absent from the sequence. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The histone fold domain recognition from raw sequence is a pattern-matching task that may vary in reliability depending on model training, though the alternating hydrophobic/charged pattern is well-documented in structural biology literature.",
    "GO:0006338 (chromatin remodeling) is a broad term encompassing histone modifications, nucleosome repositioning, and ATP-dependent remodeling. The SAGA complex's primary role is histone acetylation for transcription, which falls under this umbrella per the GO definition.",
    "The reviewer-only evidence confirms the annotation with IDA (direct assay) evidence, but this was not available to the evaluated model. The reasoning argument relies solely on sequence features and transferable domain knowledge."
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
  "benchmark_sequence_length": 289,
  "benchmark_sequence_sha256": "56bfcc6869c1cec19263500d511a7aa9d950b825750317b030d3a5072e39bde4",
  "current_entry_audit": {
    "entryVersion": 174,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-10-01",
    "sequenceVersion": 2
  },
  "current_record_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 289,
  "current_source_sequence_sha256": "56bfcc6869c1cec19263500d511a7aa9d950b825750317b030d3a5072e39bde4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 172,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9W2I4",
  "selected_historical_entry_version": 172,
  "selected_historical_record_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "selected_historical_source_sequence_length": 289,
  "selected_historical_source_sequence_sha256": "56bfcc6869c1cec19263500d511a7aa9d950b825750317b030d3a5072e39bde4",
  "selected_historical_version": {
    "accession": "Q9W2I4",
    "database": "Swiss-Prot",
    "entryVersion": 172,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SGF29_DROME",
    "sequenceVersion": 2
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9W2I4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":174,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-10-01\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"SAGA complex subunit Sgf29\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0050390\",\"source\":\"FlyBase\"}],\"value\":\"SAGA-associated factor 29kDa\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16980620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20008933\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21764853\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24493646\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30559249\",\"source\":\"PubMed\"}],\"value\":\"Component of both the SAGA and CHAT histone acetyltransferase complexes, which both predominantly acetylate histone H3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"18327268\",\"source\":\"PubMed\"}],\"id\":\"GO:0006338\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:chromatin remodeling\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/43",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33004486\",\"source\":\"PubMed\"}],\"id\":\"GO:0045893\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:positive regulation of DNA-templated transcription\"},{\"key\":\"GoEvidenceType\",\"value\":\"NAS:ComplexPortal\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/44",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"22426530\",\"source\":\"PubMed\"}],\"id\":\"GO:0006355\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:regulation of DNA-templated transcription\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:ComplexPortal\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/45",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30715476\",\"source\":\"PubMed\"}],\"id\":\"GO:0006357\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:regulation of transcription by RNA polymerase II\"},{\"key\":\"GoEvidenceType\",\"value\":\"NAS:ComplexPortal\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/46",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Guelman S.\",\"Suganuma T.\",\"Florens L.\",\"Weake V.\",\"Swanson S.K.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16980620\"},{\"database\":\"DOI\",\"id\":\"10.1128/mcb.00130-06\"}],\"citationType\":\"journal article\",\"firstPage\":\"7178\",\"id\":\"16980620\",\"journal\":\"Mol. Cell. Biol.\",\"lastPage\":\"7189\",\"publicationDate\":\"2006\",\"title\":\"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA required for histone H3 acetylation.\",\"volume\":\"26\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Swanson S.K.\",\"Mushegian A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20008933\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.1846409\"}],\"citationType\":\"journal article\",\"firstPage\":\"2818\",\"id\":\"20008933\",\"journal\":\"Genes Dev.\",\"lastPage\":\"2823\",\"publicationDate\":\"2009\",\"title\":\"A novel histone fold domain-containing protein that replaces TAF6 in Drosophila SAGA is required for SAGA-dependent gene expression.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Dyer J.O.\",\"Seidel C.\",\"Box A.\",\"Swanson S.K.\",\"Peak A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21764853\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.2046211\"}],\"citationType\":\"journal article\",\"firstPage\":\"1499\",\"id\":\"21764853\",\"journal\":\"Genes Dev.\",\"lastPage\":\"1509\",\"publicationDate\":\"2011\",\"title\":\"Post-transcription initiation function of the ubiquitous SAGA complex in tissue-specific gene activation.\",\"volume\":\"25\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"DEVELOPMENTAL STAGE\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Mohan R.D.\",\"Dialynas G.\",\"Weake V.M.\",\"Liu J.\",\"Martin-Brown S.\",\"Florens L.\",\"Washburn M.P.\",\"Workman J.L.\",\"Abmayr S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24493646\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.225151.113\"}],\"citationType\":\"journal article\",\"firstPage\":\"259\",\"id\":\"24493646\",\"journal\":\"Genes Dev.\",\"lastPage\":\"272\",\"publicationDate\":\"2014\",\"title\":\"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination and leads to neural and retinal degeneration.\",\"volume\":\"28\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2I4.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"citation\":{\"authors\":[\"Torres-Zelada E.F.\",\"Stephenson R.E.\",\"Alpsoy A.\",\"Anderson B.D.\",\"Swanson S.K.\",\"Florens L.\",\"Dykhuizen E.C.\",\"Washburn M.P.\",\"Weake V.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30559249\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.214072\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30559249\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is necessary for histone acetylation and viability.\",\"volume\":\"132\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":8,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA AND CHAT COMPLEXES\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:33:46.947791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99e79ffdf07452f0c2ae6b5b82b60c28b7ea2d0331542973f4e028462aab9481",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2I4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "entry_version": 172,
  "evidence_id": "H1",
  "excerpt": "ID   SGF29_DROME             Reviewed;         289 AA.\nAC   Q9W2I4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2002, sequence version 2.\nDT   28-JAN-2026, entry version 172.\nDE   RecName: Full=SAGA-associated factor 29kDa {ECO:0000312|FlyBase:FBgn0050390};\nDE   AltName: Full=SAGA complex subunit Sgf29 {ECO:0000305};\nGN   Name=Sgf29 {ECO:0000303|PubMed:16980620, ECO:0000312|FlyBase:FBgn0050390};\nGN   ORFNames=CG30390 {ECO:0000312|FlyBase:FBgn0050390};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "entry_version": 172,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, AND IDENTIFICATION BY MASS\nRP   SPECTROMETRY.\nRX   PubMed=16980620; DOI=10.1128/mcb.00130-06;\nRA   Guelman S., Suganuma T., Florens L., Weake V., Swanson S.K., Washburn M.P.,\nRA   Abmayr S.M., Workman J.L.;\nRT   \"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA\nRT   required for histone H3 acetylation.\";\nRL   Mol. Cell. Biol. 26:7178-7189(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "entry_version": 172,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=20008933; DOI=10.1101/gad.1846409;\nRA   Weake V.M., Swanson S.K., Mushegian A., Florens L., Washburn M.P.,\nRA   Abmayr S.M., Workman J.L.;\nRT   \"A novel histone fold domain-containing protein that replaces TAF6 in\nRT   Drosophila SAGA is required for SAGA-dependent gene expression.\";\nRL   Genes Dev. 23:2818-2823(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "entry_version": 172,
  "evidence_id": "H4",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, DEVELOPMENTAL STAGE, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=21764853; DOI=10.1101/gad.2046211;\nRA   Weake V.M., Dyer J.O., Seidel C., Box A., Swanson S.K., Peak A.,\nRA   Florens L., Washburn M.P., Abmayr S.M., Workman J.L.;\nRT   \"Post-transcription initiation function of the ubiquitous SAGA complex in\nRT   tissue-specific gene activation.\";\nRL   Genes Dev. 25:1499-1509(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "entry_version": 172,
  "evidence_id": "H5",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=24493646; DOI=10.1101/gad.225151.113;\nRA   Mohan R.D., Dialynas G., Weake V.M., Liu J., Martin-Brown S., Florens L.,\nRA   Washburn M.P., Workman J.L., Abmayr S.M.;\nRT   \"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination\nRT   and leads to neural and retinal degeneration.\";\nRL   Genes Dev. 28:259-272(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "entry_version": 172,
  "evidence_id": "H6",
  "excerpt": "RN   [8] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA AND CHAT COMPLEXES, AND IDENTIFICATION\nRP   BY MASS SPECTROMETRY.\nRX   PubMed=30559249; DOI=10.1242/jcs.214072;\nRA   Torres-Zelada E.F., Stephenson R.E., Alpsoy A., Anderson B.D.,\nRA   Swanson S.K., Florens L., Dykhuizen E.C., Washburn M.P., Weake V.M.;\nRT   \"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is\nRT   necessary for histone acetylation and viability.\";\nRL   J. Cell Sci. 132:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "entry_version": 172,
  "evidence_id": "H7",
  "excerpt": "CC   -!- FUNCTION: Component of both the SAGA and CHAT histone acetyltransferase\nCC       complexes, which both predominantly acetylate histone H3.\nCC       {ECO:0000269|PubMed:16980620, ECO:0000269|PubMed:20008933,\nCC       ECO:0000269|PubMed:21764853, ECO:0000269|PubMed:24493646,\nCC       ECO:0000269|PubMed:30559249}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172)

```json
{
  "entry_version": 172,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0006338; P:chromatin remodeling; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:50.066048+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 186-186",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9cdab37ca5165bf0ed7c572bc5323ec3cdbf7ef551b85431bdf2251f55d4d874",
  "url": "https://rest.uniprot.org/unisave/Q9W2I4?format=txt&versions=172"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006338\nname: chromatin remodeling\nnamespace: biological_process\nalt_id: GO:0043044\ndef: \"A dynamic process of chromatin reorganization resulting in changes to chromatin structure. These changes allow DNA metabolic processes such as transcriptional regulation, DNA recombination, DNA repair, and DNA replication.\" [GOC:jid, GOC:vw, PMID:12042764, PMID:12697820]\nsynonym: \"ATP-dependent chromatin remodeling\" NARROW []\nsynonym: \"ATP-dependent chromatin remodelling\" NARROW []\nsynonym: \"chromatin modeling\" EXACT []\nsynonym: \"chromatin modelling\" EXACT []\nsynonym: \"chromatin remodelling\" EXACT []\nis_a: GO:0006325 ! chromatin organization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006338",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 65237-65249",
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
  "excerpt": "[Term]\nid: GO:0030488\nname: tRNA methylation\nnamespace: biological_process\ndef: \"The posttranscriptional addition of methyl groups to specific residues in a tRNA molecule.\" [GOC:mah]\nis_a: GO:0001510 ! RNA methylation\nis_a: GO:0006400 ! tRNA modification\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030488",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 166575-166582",
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
  "excerpt": "[Term]\nid: GO:0033108\nname: mitochondrial respiratory chain complex assembly\nnamespace: biological_process\ndef: \"The aggregation, arrangement and bonding together of a set of components to form a mitochondrial respiratory chain complex or between respiratory chain complexes to form high-order structures.\" [GOC:mah]\nis_a: GO:0065003 ! protein-containing complex assembly\nrelationship: part_of GO:0007005 ! mitochondrion organization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0033108",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 193816-193823",
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
  "excerpt": "[Term]\nid: GO:1904385\nname: cellular response to angiotensin\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of an angiotensin stimulus. Angiotensin is any of three physiologically active peptides (angiotensin II, III, or IV) processed from angiotensinogen.\" [GO_REF:0000071, GOC:TermGenie, PMID:22982863]\nis_a: GO:0071375 ! cellular response to peptide hormone stimulus\nis_a: GO:1990776 ! response to angiotensin\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1904385",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 522013-522020",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 92. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
