# transmembrane_0114

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0114.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 1250..1269

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKISKCAFVAISALVLIQATQTVKSQEPLVQSQLVTTVALTQDNRLLVEEIGPYASQSAGKEYYKHIEKIIVDNDVYEKSLEGERTFDINYQGIKINADLIKDGKHELTIVNKKDGDILITFIKKGDKVTFISAQKLGTTDHQDSLKKDVLSDKTVPQNQGTQKVVKSGKNTANLSLITKLSQEDGAILFPEIDRYSDNKQIKALTQQITKVTVNGTVYKDLISDSVKDTNGWVSNMTGLHLGTKAFKDGENTIVISSKGFEDVTITVTKKDGQIHFVSAKQKQHVTAEDRQSTKLDVTTLEKAIKEADAIIAKESNKDAVKDLAEKLQVIKDSYKEIKDSKLLADTHRLLKDTIESYQAGEVSINNLTEGTYTLNFKANKENSEESSMLQGAFDKRAKLVVKADGTMEISMLNTALGQFLIDFSIESKGTYPAAVRKQVGQKDINGSYIRSEFTMPIDDLDKLHKGAVLVSAMGGQESDLNHYDKYTKLDMTFSKTVTKGWSGYQVETDDKEKGVGTERLEKVLVKLGKDLDGDGKLSKTELEQIRGELRLDHYELTDISLLKHAKNITELHLDGNQITEIPKELFSQMKQLRFLNLRSNHLTYLDKDTFKSNAQLRELYLSSNFIHSLEGGLFQSLHHLEQLDLSKNRIGRLCDNPFEGLSRLTSLGFAENSLEEIPEKALEPLTSLNFIDLSQNNLALLPKTIEKLRALSTIVASRNHITRIDNISFKNLPKLSVLDLSTNEISNLPNGIFKQNNQLTKLDFFNNLLTQVEESVFPDVETLNLDVKFNQIKSVSPKVRALIGQHKLTPQKHIAKLEASLDGEKIKYHQAFSLLDLYYWEQKTNSAIDKELVSVEEYQQLLQEKGSDTVSLLNDMQVDWSIVIQLQKKASNGQYVTVDEKLLSNDPKDDLTGEFSLKDPGTYRIRKALITKKFATQKEHIYLTSNDILVAKGPHSHQKDLVENGLRALNQKQLRDGIYYLNASMLKTDLASESMSNKAINHRVTLVVKKGVSYLEVEFRGIKVGKMLGYLGELSYFVDGYQRDLAGKPVGRTKKAEVVSYFTDVTGLPLADRYGKNYPKVLRMKLIEQAKKDGLVPLQVFVPIMDAISKGSGLQTVFMRLDWASLTTEKAKVVKETNNPQENSHLTSTDQLKGPQNRQQEKTPTSPPSAATGIANLTDLLAKKATGQSTQETSKTDDTDKAEKLKQLVRDHQTSIEGKTAKDTKTKKSDKKHRSNQQSNGEESSSRYHLIAGLSSFMIVALGFIIGRKTLFK

[Multiple Choices]
A. 223..243; 6520..6540; 6552..6572; 6578..6598; 6627..6647; 6770..6790; 6831..6851; 6888..6908; 6912..6932; 7017..7037
B. 1250..1269
C. 1253..1267
D. 1250..1269; 742..763
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence has a hydrophobic C-terminal segment consistent with the keyed 1250..1269 helix. The matched UniProt record annotates that exact interval as a transmembrane helix; its ECO:0000255 evidence indicates computational annotation, not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains a conspicuous hydrophobic stretch near its C-terminus, unlike the largely soluble-looking sequence preceding it. A roughly 20-residue hydrophobic alpha helix is a standard transferable signature of a membrane-spanning segment, supporting B. C selects only a shorter internal portion of that stretch, which is less plausible as the complete membrane-crossing span.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and standard length/hydrophobicity patterns for transmembrane helices meaningfully distinguish B from the offered alternatives without needing the target's database record. The precise boundaries remain prediction-level rather than experimentally established by the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although C overlaps the hydrophobic core, its shorter interval is less consistent with a complete membrane-spanning helix; B gives the more plausible full span. The other choices include implausible coordinates or an additional unsupported segment.


### Important caveats

- The source annotation is computational, and the author's exact source snapshot is unknown; the historical and current records cited here match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains a conspicuous hydrophobic stretch near its C-terminus, unlike the largely soluble-looking sequence preceding it. A roughly 20-residue hydrophobic alpha helix is a standard transferable signature of a membrane-spanning segment, supporting B. C selects only a shorter internal portion of that stretch, which is less plausible as the complete membrane-crossing span.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and standard length/hydrophobicity patterns for transmembrane helices meaningfully distinguish B from the offered alternatives without needing the target's database record. The precise boundaries remain prediction-level rather than experimentally established by the supplied evidence."
  },
  "case_id": "transmembrane_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence has a hydrophobic C-terminal segment consistent with the keyed 1250..1269 helix. The matched UniProt record annotates that exact interval as a transmembrane helix; its ECO:0000255 evidence indicates computational annotation, not direct experimental confirmation."
  },
  "important_caveats": [
    "The source annotation is computational, and the author's exact source snapshot is unknown; the historical and current records cited here match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although C overlaps the hydrophobic core, its shorter interval is less consistent with a complete membrane-spanning helix; B gives the more plausible full span. The other choices include implausible coordinates or an additional unsupported segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence has a hydrophobic C-terminal segment consistent with the keyed 1250..1269 helix. The matched UniProt record annotates that exact interval as a transmembrane helix; its ECO:0000255 evidence indicates computational annotation, not direct experimental confirmation.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains a conspicuous hydrophobic stretch near its C-terminus, unlike the largely soluble-looking sequence preceding it. A roughly 20-residue hydrophobic alpha helix is a standard transferable signature of a membrane-spanning segment, supporting B. C selects only a shorter internal portion of that stretch, which is less plausible as the complete membrane-crossing span.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and standard length/hydrophobicity patterns for transmembrane helices meaningfully distinguish B from the offered alternatives without needing the target's database record. The precise boundaries remain prediction-level rather than experimentally established by the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although C overlaps the hydrophobic core, its shorter interval is less consistent with a complete membrane-spanning helix; B gives the more plausible full span. The other choices include implausible coordinates or an additional unsupported segment."
  },
  "important_caveats": [
    "The source annotation is computational, and the author's exact source snapshot is unknown; the historical and current records cited here match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (Q99YA0, Streptococcal hemoprotein receptor, 1275 AA) annotates a single helical transmembrane region at positions 1250-1269 (evidence C5/H4). The sequence at that position (YHLIAGLSSFMIVALGFIIG) is a predominantly hydrophobic 20-residue segment consistent with a single-pass TM anchor. The annotation carries ECO:0000255 (prosequence-based prediction), but the protein's cell-surface receptor topology is independently supported by subcellular location data (PubMed:12595414, evidence C6/H2). Answer B matches the annotated region exactly.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can identify the C-terminal hydrophobic stretch by scanning the sequence. The region around positions 1250-1269 (YHLIAGLSSFMIVALGFIIG) is the only long hydrophobic segment near the C-terminus suitable for a TM anchor. The biophysical constraint that a transmembrane alpha-helix requires approximately 18-25 hydrophobic residues to span the ~30 Å hydrophobic core of a lipid bilayer distinguishes option B (20 residues, 1250-1269) from option C (15 residues, 1253-1267): 15 residues is too short for a standard TM helix. Option A is eliminated because it lists positions (6520-7037) far exceeding the 1275-residue protein length. Option D is eliminated because region 742-763 (NGIFKQNNQLTKLDFFNNLLTQ) is rich in polar/charged residues (N, K, Q, D, T) and is clearly not hydrophobic. Family-level knowledge of Gram-positive cell-surface proteins (LPXTG-anchored or single-TM-anchor receptors) supports a single C-terminal TM helix, consistent with B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction among the four options relies on (1) recognizing that option A contains impossible positions for a 1275-aa protein, (2) recognizing that option D's second region is not hydrophobic, and (3) applying the well-established biophysical minimum-length requirement for TM helices (~18-25 residues) to prefer the 20-residue segment (B) over the 15-residue segment (C). All of these use the original sequence and general membrane-biology knowledge transferable across proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is trivially eliminated by out-of-range positions. Option D is eliminated by the non-hydrophobic nature of the 742-763 segment. Between B and C, the biophysical length constraint for TM helices provides a clear preference for the 20-residue segment (B) over the 15-residue segment (C). No genuine ambiguity remains among the offered choices.


### Important caveats

- The UniProt TM annotation at 1250-1269 carries evidence code ECO:0000255 (prosequence-based/computational prediction), not direct experimental determination of the helix boundaries.
- The protein's single-pass membrane topology is functionally supported by subcellular location studies (PubMed:12595414), but exact helix boundaries remain a computational assignment.
- Option C (1253-1267) captures the most hydrophobic core and is not wildly wrong; it is simply below the typical minimum length for a TM helix, making B the stronger choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can identify the C-terminal hydrophobic stretch by scanning the sequence. The region around positions 1250-1269 (YHLIAGLSSFMIVALGFIIG) is the only long hydrophobic segment near the C-terminus suitable for a TM anchor. The biophysical constraint that a transmembrane alpha-helix requires approximately 18-25 hydrophobic residues to span the ~30 Å hydrophobic core of a lipid bilayer distinguishes option B (20 residues, 1250-1269) from option C (15 residues, 1253-1267): 15 residues is too short for a standard TM helix. Option A is eliminated because it lists positions (6520-7037) far exceeding the 1275-residue protein length. Option D is eliminated because region 742-763 (NGIFKQNNQLTKLDFFNNLLTQ) is rich in polar/charged residues (N, K, Q, D, T) and is clearly not hydrophobic. Family-level knowledge of Gram-positive cell-surface proteins (LPXTG-anchored or single-TM-anchor receptors) supports a single C-terminal TM helix, consistent with B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction among the four options relies on (1) recognizing that option A contains impossible positions for a 1275-aa protein, (2) recognizing that option D's second region is not hydrophobic, and (3) applying the well-established biophysical minimum-length requirement for TM helices (~18-25 residues) to prefer the 20-residue segment (B) over the 15-residue segment (C). All of these use the original sequence and general membrane-biology knowledge transferable across proteins."
  },
  "case_id": "transmembrane_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Q99YA0, Streptococcal hemoprotein receptor, 1275 AA) annotates a single helical transmembrane region at positions 1250-1269 (evidence C5/H4). The sequence at that position (YHLIAGLSSFMIVALGFIIG) is a predominantly hydrophobic 20-residue segment consistent with a single-pass TM anchor. The annotation carries ECO:0000255 (prosequence-based prediction), but the protein's cell-surface receptor topology is independently supported by subcellular location data (PubMed:12595414, evidence C6/H2). Answer B matches the annotated region exactly."
  },
  "important_caveats": [
    "The UniProt TM annotation at 1250-1269 carries evidence code ECO:0000255 (prosequence-based/computational prediction), not direct experimental determination of the helix boundaries.",
    "The protein's single-pass membrane topology is functionally supported by subcellular location studies (PubMed:12595414), but exact helix boundaries remain a computational assignment.",
    "Option C (1253-1267) captures the most hydrophobic core and is not wildly wrong; it is simply below the typical minimum length for a TM helix, making B the stronger choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is trivially eliminated by out-of-range positions. Option D is eliminated by the non-hydrophobic nature of the 742-763 segment. Between B and C, the biophysical length constraint for TM helices provides a clear preference for the 20-residue segment (B) over the 15-residue segment (C). No genuine ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Q99YA0, Streptococcal hemoprotein receptor, 1275 AA) annotates a single helical transmembrane region at positions 1250-1269 (evidence C5/H4). The sequence at that position (YHLIAGLSSFMIVALGFIIG) is a predominantly hydrophobic 20-residue segment consistent with a single-pass TM anchor. The annotation carries ECO:0000255 (prosequence-based prediction), but the protein's cell-surface receptor topology is independently supported by subcellular location data (PubMed:12595414, evidence C6/H2). Answer B matches the annotated region exactly.",
    "evidence_ids": ["C5", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can identify the C-terminal hydrophobic stretch by scanning the sequence. The region around positions 1250-1269 (YHLIAGLSSFMIVALGFIIG) is the only long hydrophobic segment near the C-terminus suitable for a TM anchor. The biophysical constraint that a transmembrane alpha-helix requires approximately 18-25 hydrophobic residues to span the ~30 Å hydrophobic core of a lipid bilayer distinguishes option B (20 residues, 1250-1269) from option C (15 residues, 1253-1267): 15 residues is too short for a standard TM helix. Option A is eliminated because it lists positions (6520-7037) far exceeding the 1275-residue protein length. Option D is eliminated because region 742-763 (NGIFKQNNQLTKLDFFNNLLTQ) is rich in polar/charged residues (N, K, Q, D, T) and is clearly not hydrophobic. Family-level knowledge of Gram-positive cell-surface proteins (LPXTG-anchored or single-TM-anchor receptors) supports a single C-terminal TM helix, consistent with B.",
    "missing_item_specific_fact": "",
    "reason": "The distinction among the four options relies on (1) recognizing that option A contains impossible positions for a 1275-aa protein, (2) recognizing that option D's second region is not hydrophobic, and (3) applying the well-established biophysical minimum-length requirement for TM helices (~18-25 residues) to prefer the 20-residue segment (B) over the 15-residue segment (C). All of these use the original sequence and general membrane-biology knowledge transferable across proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is trivially eliminated by out-of-range positions. Option D is eliminated by the non-hydrophobic nature of the 742-763 segment. Between B and C, the biophysical length constraint for TM helices provides a clear preference for the 20-residue segment (B) over the 15-residue segment (C). No genuine ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The UniProt TM annotation at 1250-1269 carries evidence code ECO:0000255 (prosequence-based/computational prediction), not direct experimental determination of the helix boundaries.",
    "The protein's single-pass membrane topology is functionally supported by subcellular location studies (PubMed:12595414), but exact helix boundaries remain a computational assignment.",
    "Option C (1253-1267) captures the most hydrophobic core and is not wildly wrong; it is simply below the typical minimum length for a TM helix, making B the stronger choice."
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
  "benchmark_sequence_length": 1275,
  "benchmark_sequence_sha256": "9f82b8226fd57dc98ee899bdb14b94015792e1f6c1dc2a4eb732d834f35cb31c",
  "current_entry_audit": {
    "entryVersion": 158,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "13d192b72925d5c393cc3105671c42e63812538c0c7b0b4492aea8192c61a8b1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1275,
  "current_source_sequence_sha256": "9f82b8226fd57dc98ee899bdb14b94015792e1f6c1dc2a4eb732d834f35cb31c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 156,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q99YA0",
  "selected_historical_entry_version": 156,
  "selected_historical_record_sha256": "19d54403bf689f1c46885d29ac65062d1747c6a8f0492de30c3b76138294fd49",
  "selected_historical_source_sequence_length": 1275,
  "selected_historical_source_sequence_sha256": "9f82b8226fd57dc98ee899bdb14b94015792e1f6c1dc2a4eb732d834f35cb31c",
  "selected_historical_version": {
    "accession": "Q99YA0",
    "database": "Swiss-Prot",
    "entryVersion": 156,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SHR_STRP1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q99YA0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q99YA0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:26.368907+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "13d192b72925d5c393cc3105671c42e63812538c0c7b0b4492aea8192c61a8b1",
  "url": "https://rest.uniprot.org/uniprotkb/Q99YA0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q99YA0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":158,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:26.368907+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "13d192b72925d5c393cc3105671c42e63812538c0c7b0b4492aea8192c61a8b1",
  "url": "https://rest.uniprot.org/uniprotkb/Q99YA0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q99YA0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Lactobacillales\",\"Streptococcaceae\",\"Streptococcus\"],\"scientificName\":\"Streptococcus pyogenes serotype M1\",\"taxonId\":301447}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:26.368907+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "13d192b72925d5c393cc3105671c42e63812538c0c7b0b4492aea8192c61a8b1",
  "url": "https://rest.uniprot.org/uniprotkb/Q99YA0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q99YA0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38438508\",\"source\":\"PubMed\"}],\"value\":\"Heme-acquisition protein Shr\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ABW80932.1\",\"source\":\"EMBL\"}],\"value\":\"Heme-binding protein Shr\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"12595414\",\"source\":\"PubMed\"}],\"value\":\"Hemoprotein binding receptor\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"12595414\",\"source\":\"PubMed\"}],\"value\":\"Streptococcal hemoprotein receptor\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:26.368907+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "13d192b72925d5c393cc3105671c42e63812538c0c7b0b4492aea8192c61a8b1",
  "url": "https://rest.uniprot.org/uniprotkb/Q99YA0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q99YA0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1269},\"start\":{\"modifier\":\"EXACT\",\"value\":1250}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:26.368907+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "13d192b72925d5c393cc3105671c42e63812538c0c7b0b4492aea8192c61a8b1",
  "url": "https://rest.uniprot.org/uniprotkb/Q99YA0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q99YA0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bates C.S.\",\"Montanez G.E.\",\"Woods C.R.\",\"Vincent R.M.\",\"Eichenbaum Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12595414\"},{\"database\":\"DOI\",\"id\":\"10.1128/iai.71.3.1042-1055.2003\"}],\"citationType\":\"journal article\",\"firstPage\":\"1042\",\"id\":\"12595414\",\"journal\":\"Infect. Immun.\",\"lastPage\":\"1055\",\"publicationDate\":\"2003\",\"title\":\"Identification and characterization of a Streptococcus pyogenes operon involved in binding of hemoproteins and acquisition of iron.\",\"volume\":\"71\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700294 / SF370 / Serotype M1\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION AS A RECEPTOR\",\"SUBCELLULAR LOCATION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:26.368907+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "13d192b72925d5c393cc3105671c42e63812538c0c7b0b4492aea8192c61a8b1",
  "url": "https://rest.uniprot.org/uniprotkb/Q99YA0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q99YA0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Senoo A.\",\"Hoshino M.\",\"Shiomi T.\",\"Nakakido M.\",\"Nagatoishi S.\",\"Kuroda D.\",\"Nakagawa I.\",\"Tame J.R.H.\",\"Caaveiro J.M.M.\",\"Tsumoto K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38438508\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41598-024-55734-x\"}],\"citationType\":\"journal article\",\"firstPage\":\"5374\",\"id\":\"38438508\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"5374\",\"publicationDate\":\"2024\",\"title\":\"Structural basis for the recognition of human hemoglobin by the heme-acquisition protein Shr from Streptococcus pyogenes.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7CUD\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7CUE\",\"source\":\"PDB\"}],\"referenceNumber\":10,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 171-294 IN COMPLEX WITH HEMOGLOBIN\",\"DOMAIN\",\"BIOTECHNOLOGY\",\"MUTAGENESIS OF ARG-196; TYR-197; GLN-209; ILE-224; SER-225 AND MET-238\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/9",
  "retrieved_utc": "2026-11-01T06:25:26.368907+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "13d192b72925d5c393cc3105671c42e63812538c0c7b0b4492aea8192c61a8b1",
  "url": "https://rest.uniprot.org/uniprotkb/Q99YA0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q99YA0?format=txt&versions=156)

```json
{
  "entry_version": 156,
  "evidence_id": "H1",
  "excerpt": "ID   SHR_STRP1               Reviewed;        1275 AA.\nAC   Q99YA0; B0LFQ8; Q48WX7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2001, sequence version 1.\nDT   28-JAN-2026, entry version 156.\nDE   RecName: Full=Streptococcal hemoprotein receptor {ECO:0000303|PubMed:12595414};\nDE   AltName: Full=Heme-acquisition protein Shr {ECO:0000303|PubMed:38438508};\nDE   AltName: Full=Heme-binding protein Shr {ECO:0000312|EMBL:ABW80932.1};\nDE   AltName: Full=Hemoprotein binding receptor {ECO:0000303|PubMed:12595414};\nDE   Flags: Precursor;\nGN   Name=shr {ECO:0000303|PubMed:12595414};\nGN   OrderedLocusNames=SPy_1798 {ECO:0000312|EMBL:AAK34530.1};\nOS   Streptococcus pyogenes serotype M1.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae;\nOC   Streptococcus.\nOX   NCBI_TaxID=301447;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.568124+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19d54403bf689f1c46885d29ac65062d1747c6a8f0492de30c3b76138294fd49",
  "url": "https://rest.uniprot.org/unisave/Q99YA0?format=txt&versions=156"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q99YA0?format=txt&versions=156)

```json
{
  "entry_version": 156,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   FUNCTION AS A RECEPTOR, SUBCELLULAR LOCATION, INDUCTION, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 700294 / SF370 / Serotype M1;\nRX   PubMed=12595414; DOI=10.1128/iai.71.3.1042-1055.2003;\nRA   Bates C.S., Montanez G.E., Woods C.R., Vincent R.M., Eichenbaum Z.;\nRT   \"Identification and characterization of a Streptococcus pyogenes operon\nRT   involved in binding of hemoproteins and acquisition of iron.\";\nRL   Infect. Immun. 71:1042-1055(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.568124+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19d54403bf689f1c46885d29ac65062d1747c6a8f0492de30c3b76138294fd49",
  "url": "https://rest.uniprot.org/unisave/Q99YA0?format=txt&versions=156"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q99YA0?format=txt&versions=156)

```json
{
  "entry_version": 156,
  "evidence_id": "H3",
  "excerpt": "RN   [10] {ECO:0007744|PDB:7CUD, ECO:0007744|PDB:7CUE}\nRP   X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 171-294 IN COMPLEX WITH\nRP   HEMOGLOBIN, DOMAIN, BIOTECHNOLOGY, AND MUTAGENESIS OF ARG-196; TYR-197;\nRP   GLN-209; ILE-224; SER-225 AND MET-238.\nRX   PubMed=38438508; DOI=10.1038/s41598-024-55734-x;\nRA   Senoo A., Hoshino M., Shiomi T., Nakakido M., Nagatoishi S., Kuroda D.,\nRA   Nakagawa I., Tame J.R.H., Caaveiro J.M.M., Tsumoto K.;\nRT   \"Structural basis for the recognition of human hemoglobin by the heme-\nRT   acquisition protein Shr from Streptococcus pyogenes.\";\nRL   Sci. Rep. 14:5374-5374(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.568124+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19d54403bf689f1c46885d29ac65062d1747c6a8f0492de30c3b76138294fd49",
  "url": "https://rest.uniprot.org/unisave/Q99YA0?format=txt&versions=156"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q99YA0?format=txt&versions=156)

```json
{
  "entry_version": 156,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        1250..1269\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.568124+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 268-270",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19d54403bf689f1c46885d29ac65062d1747c6a8f0492de30c3b76138294fd49",
  "url": "https://rest.uniprot.org/unisave/Q99YA0?format=txt&versions=156"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 114. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
