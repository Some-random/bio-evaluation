# active_site_0036

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0036.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 327 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTIRGTLSELSRAADAFAHEVDEAGYGDYTFLPDNSPFDLSFLTSKGLEARGSLIAAAEKILRLAKGPQGCLASFADTKGIEMGTIQALTQLEVPDKVPLQGSITYEELAGVIRVAPELLQRLVRLAALAGFLIEDESGAVRHTAMSAVFLRDTAAGDTARFLFDVDMRAYSFFADSLRLDPSGQNIGDGPTALAFQHDSDDQGNRPTIWDILERNPIQRARFHSTMQALGSFPSHLLKHILVAHDWHSIGSLVDVGGSLGHASLVIAENFPEIRITVQDLPDVVERGRSSLPTVPHAERVSFQAHDLFQEQAIIADAYFLRQILHDWPDGDAERIVRCLIPAMRPGAKLLIMDIVVPEPGAISPYMEKYLRTYDVSMFSMFSAKERTVQQLRDLVERCSARLQFQGISCPPGSATSLLSWVYSAE

[Multiple Choices]
A. Position 2723 (Proton acceptor; for dehydratase activity 2)
B. Position 327 (Proton acceptor)
C. Position 180 (For beta-ketoacyl synthase activity)
D. Position 161 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates position 327 as a proton acceptor. This is a computational PROSITE-ProRule annotation, not direct experimental evidence for that residue; the record also identifies the protein as an O-methyltransferase. The sequence has His at position 327, consistent with the annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a SAM-dependent O-methyltransferase, and its His-Asp pair at positions 327–328 is a plausible catalytic-base motif: histidine can accept a proton during methylation of a substrate hydroxyl. This makes B a meaningful choice among the options. The sequence also directly rules against D as stated because position 161 is alanine, while A is outside the 427-residue sequence and C describes an unrelated activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about O-methyltransferase chemistry and catalytic histidine residues, together with the sequence and the alternatives, gives a credible basis for selecting B without knowing this protein's database annotation. The specific role remains an inference rather than a direct demonstration.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably defensible: one is out of range, one assigns an unrelated activity, and the proposed proton donor is alanine at the stated position.


### Important caveats

- The residue-specific active-site annotation is attributed to PROSITE-ProRule and should not be presented as experimentally established by the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent O-methyltransferase, and its His-Asp pair at positions 327–328 is a plausible catalytic-base motif: histidine can accept a proton during methylation of a substrate hydroxyl. This makes B a meaningful choice among the options. The sequence also directly rules against D as stated because position 161 is alanine, while A is outside the 427-residue sequence and C describes an unrelated activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about O-methyltransferase chemistry and catalytic histidine residues, together with the sequence and the alternatives, gives a credible basis for selecting B without knowing this protein's database annotation. The specific role remains an inference rather than a direct demonstration."
  },
  "case_id": "active_site_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 327 as a proton acceptor. This is a computational PROSITE-ProRule annotation, not direct experimental evidence for that residue; the record also identifies the protein as an O-methyltransferase. The sequence has His at position 327, consistent with the annotation."
  },
  "important_caveats": [
    "The residue-specific active-site annotation is attributed to PROSITE-ProRule and should not be presented as experimentally established by the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably defensible: one is out of range, one assigns an unrelated activity, and the proposed proton donor is alanine at the stated position."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 327 as a proton acceptor. This is a computational PROSITE-ProRule annotation, not direct experimental evidence for that residue; the record also identifies the protein as an O-methyltransferase. The sequence has His at position 327, consistent with the annotation.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent O-methyltransferase, and its His-Asp pair at positions 327–328 is a plausible catalytic-base motif: histidine can accept a proton during methylation of a substrate hydroxyl. This makes B a meaningful choice among the options. The sequence also directly rules against D as stated because position 161 is alanine, while A is outside the 427-residue sequence and C describes an unrelated activity.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about O-methyltransferase chemistry and catalytic histidine residues, together with the sequence and the alternatives, gives a credible basis for selecting B without knowing this protein's database annotation. The specific role remains an inference rather than a direct demonstration."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably defensible: one is out of range, one assigns an unrelated activity, and the proposed proton donor is alanine at the stated position."
  },
  "important_caveats": [
    "The residue-specific active-site annotation is attributed to PROSITE-ProRule and should not be presented as experimentally established by the supplied evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (evidence C5 and H3) explicitly lists position 327 as 'Active site' with description 'Proton acceptor', matching the expected answer exactly. The evidence code is ECO:0000255 (PROSITE-ProRule:PRU01020), indicating a computational/pattern-based annotation rather than direct experimental validation, but the annotation is present and unambiguous in the database entry. The sequence at position 327 is Histidine (H), which is chemically consistent with a proton-acceptor (general base) role in methyltransferase catalysis.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple elimination pathways distinguish B from the other options using transferable knowledge: (1) Option A cites position 2723, which is impossible for a 427-residue protein—immediate elimination. (2) Option C references 'beta-ketoacyl synthase activity,' a fatty-acid-synthase enzyme class with a completely different catalytic mechanism (condensation via a Cys nucleophile) and unrelated to the sequence features visible here (SAM-binding motifs, methyltransferase fold). (3) Option D places a 'proton donor' at position 161, which is Alanine (A)—a residue with no ionizable side chain, chemically incapable of proton donation. (4) Position 327 is Histidine (H), the canonical general acid/base catalyst with a pKa near physiological pH, perfectly suited as a proton acceptor. Furthermore, recognizing the protein as a SAM-dependent methyltransferase (EC 2.1.x) from sequence motifs implies the catalytic mechanism requires deprotonation of the substrate (e.g., a hydroxyl) to generate a nucleophile for methyl transfer from SAM, necessitating a proton acceptor (general base) rather than a proton donor. This mechanistic expectation, combined with the chemical identity of residue 327 (His), uniquely supports option B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer is distinguishable through: protein-length constraint (eliminates A), enzyme-class mismatch (eliminates C), amino-acid chemistry at the cited positions (Ala cannot be a proton donor, eliminating D), and general catalytic principles of methyltransferases requiring a general base (His at 327 is the only chemically viable proton acceptor among the options). None of these require recalling the specific UniProt record for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are each independently eliminable by straightforward reasoning (impossible position, wrong enzyme class, chemically inert residue). Only B remains as a chemically and mechanistically coherent answer.


### Important caveats

- The UniProt annotation for position 327 carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a computational/pattern-based prediction, not a direct experimental measurement (e.g., mutagenesis or crystallographic catalysis assay).
- The protein is annotated as O-methyltransferase FrzF (EC 2.1.1.-) involved in FR901483 biosynthesis, but this identity was not provided to the evaluated model; the model must infer enzyme class from sequence features.
- The reviewer-only accession and organism information were absent from the original model input and were not used in the transferability argument.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple elimination pathways distinguish B from the other options using transferable knowledge: (1) Option A cites position 2723, which is impossible for a 427-residue protein—immediate elimination. (2) Option C references 'beta-ketoacyl synthase activity,' a fatty-acid-synthase enzyme class with a completely different catalytic mechanism (condensation via a Cys nucleophile) and unrelated to the sequence features visible here (SAM-binding motifs, methyltransferase fold). (3) Option D places a 'proton donor' at position 161, which is Alanine (A)—a residue with no ionizable side chain, chemically incapable of proton donation. (4) Position 327 is Histidine (H), the canonical general acid/base catalyst with a pKa near physiological pH, perfectly suited as a proton acceptor. Furthermore, recognizing the protein as a SAM-dependent methyltransferase (EC 2.1.x) from sequence motifs implies the catalytic mechanism requires deprotonation of the substrate (e.g., a hydroxyl) to generate a nucleophile for methyl transfer from SAM, necessitating a proton acceptor (general base) rather than a proton donor. This mechanistic expectation, combined with the chemical identity of residue 327 (His), uniquely supports option B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer is distinguishable through: protein-length constraint (eliminates A), enzyme-class mismatch (eliminates C), amino-acid chemistry at the cited positions (Ala cannot be a proton donor, eliminating D), and general catalytic principles of methyltransferases requiring a general base (His at 327 is the only chemically viable proton acceptor among the options). None of these require recalling the specific UniProt record for this exact protein."
  },
  "case_id": "active_site_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5 and H3) explicitly lists position 327 as 'Active site' with description 'Proton acceptor', matching the expected answer exactly. The evidence code is ECO:0000255 (PROSITE-ProRule:PRU01020), indicating a computational/pattern-based annotation rather than direct experimental validation, but the annotation is present and unambiguous in the database entry. The sequence at position 327 is Histidine (H), which is chemically consistent with a proton-acceptor (general base) role in methyltransferase catalysis."
  },
  "important_caveats": [
    "The UniProt annotation for position 327 carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a computational/pattern-based prediction, not a direct experimental measurement (e.g., mutagenesis or crystallographic catalysis assay).",
    "The protein is annotated as O-methyltransferase FrzF (EC 2.1.1.-) involved in FR901483 biosynthesis, but this identity was not provided to the evaluated model; the model must infer enzyme class from sequence features.",
    "The reviewer-only accession and organism information were absent from the original model input and were not used in the transferability argument."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are each independently eliminable by straightforward reasoning (impossible position, wrong enzyme class, chemically inert residue). Only B remains as a chemically and mechanistically coherent answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5 and H3) explicitly lists position 327 as 'Active site' with description 'Proton acceptor', matching the expected answer exactly. The evidence code is ECO:0000255 (PROSITE-ProRule:PRU01020), indicating a computational/pattern-based annotation rather than direct experimental validation, but the annotation is present and unambiguous in the database entry. The sequence at position 327 is Histidine (H), which is chemically consistent with a proton-acceptor (general base) role in methyltransferase catalysis.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple elimination pathways distinguish B from the other options using transferable knowledge: (1) Option A cites position 2723, which is impossible for a 427-residue protein—immediate elimination. (2) Option C references 'beta-ketoacyl synthase activity,' a fatty-acid-synthase enzyme class with a completely different catalytic mechanism (condensation via a Cys nucleophile) and unrelated to the sequence features visible here (SAM-binding motifs, methyltransferase fold). (3) Option D places a 'proton donor' at position 161, which is Alanine (A)—a residue with no ionizable side chain, chemically incapable of proton donation. (4) Position 327 is Histidine (H), the canonical general acid/base catalyst with a pKa near physiological pH, perfectly suited as a proton acceptor. Furthermore, recognizing the protein as a SAM-dependent methyltransferase (EC 2.1.x) from sequence motifs implies the catalytic mechanism requires deprotonation of the substrate (e.g., a hydroxyl) to generate a nucleophile for methyl transfer from SAM, necessitating a proton acceptor (general base) rather than a proton donor. This mechanistic expectation, combined with the chemical identity of residue 327 (His), uniquely supports option B.",
    "missing_item_specific_fact": "",
    "reason": "The answer is distinguishable through: protein-length constraint (eliminates A), enzyme-class mismatch (eliminates C), amino-acid chemistry at the cited positions (Ala cannot be a proton donor, eliminating D), and general catalytic principles of methyltransferases requiring a general base (His at 327 is the only chemically viable proton acceptor among the options). None of these require recalling the specific UniProt record for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are each independently eliminable by straightforward reasoning (impossible position, wrong enzyme class, chemically inert residue). Only B remains as a chemically and mechanistically coherent answer."
  },
  "important_caveats": [
    "The UniProt annotation for position 327 carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a computational/pattern-based prediction, not a direct experimental measurement (e.g., mutagenesis or crystallographic catalysis assay).",
    "The protein is annotated as O-methyltransferase FrzF (EC 2.1.1.-) involved in FR901483 biosynthesis, but this identity was not provided to the evaluated model; the model must infer enzyme class from sequence features.",
    "The reviewer-only accession and organism information were absent from the original model input and were not used in the transferability argument."
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
  "benchmark_sequence_length": 427,
  "benchmark_sequence_sha256": "6ca0908cdd116ff442cc6cf6287077f0ed455a179f72a73421b513fdffa4f3b0",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 427,
  "current_source_sequence_sha256": "6ca0908cdd116ff442cc6cf6287077f0ed455a179f72a73421b513fdffa4f3b0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8J1Z8",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "selected_historical_source_sequence_length": 427,
  "selected_historical_source_sequence_sha256": "6ca0908cdd116ff442cc6cf6287077f0ed455a179f72a73421b513fdffa4f3b0",
  "selected_historical_version": {
    "accession": "A0A7T8J1Z8",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZF_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8J1Z8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein F\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase FrzF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":327},\"start\":{\"modifier\":\"EXACT\",\"value\":327}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":281},\"start\":{\"modifier\":\"EXACT\",\"value\":281}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:52.176056+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   FRZF_CLASX              Reviewed;         427 AA.\nAC   A0A7T8J1Z8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=O-methyltransferase FrzF {ECO:0000303|PubMed:33372776};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein F {ECO:0000303|PubMed:33372776};\nGN   Name=FrzF {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        327\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         281\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.122159+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 36. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
