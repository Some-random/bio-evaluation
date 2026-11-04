# EC_number_0117

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0117.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSIALALAAAPAVLAQSQLWGQCGGIGWNGPTTCVSGATCTKINDWYHQCLPGGNNNNPPPATTSQWTPPPAQTSSNPPPNNGGGGGNTLHEKFKARGKQYFGTEIDHYHLNNNQLMEIARREFGQITHENSMKWDATEPSRGSFSFGNADRVVDWATSNGKLIRGHTLLWHSQLPQWVQNINDRNTLTQVIENHVKTIMTRYKGKIFHYDVVNEILDENGGLRNSVFSRVLGEDFVGIAFRAARATDPDAKLYINDYNLDSANYAKTRGMINLVNKWVSQGVPIDGIGTQAHLAGPGGWNPASGVPAALQALAGANVKEVAITELDIQGAGANDYVTVANACLNVQKCVGITVWGVSDRDSWRSNENPLLYDGSYRPKAAYNALMNAL

[Multiple Choices]
A. 3.2.1.105
B. 3.2.1.8
C. 4.2.3.1
D. 2.7.7.43
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

> The sequence-matched UniProt entry assigns EC 3.2.1.8 and describes hydrolysis of (1→4)-β-D-xylosidic linkages, citing experimental evidence (ECO:0000269). The annotation is linked to a paper reporting characterization of the enzyme, though the paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, followed by a large globular fungal carbohydrate-active enzyme domain. Its sequence and architecture are consistent with a fungal endo-xylanase; transferable knowledge of these enzymes supports hydrolysis of β-1,4 linkages (option B). This meaningfully favors B over the distinct enzyme class in A and the unrelated reaction classes in C and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers a credible family-level route to the endo-xylanase choice without needing the exact protein's database annotation. This is a biologically informed inference rather than certainty about substrate specificity from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based endo-xylanase inference favors B among the offered choices; no alternative is comparably supported.


### Important caveats

- The reviewer-only database evidence supports the key but was not part of the original input.
- The database annotation cites experimental evidence, but that underlying study was not independently evaluated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, followed by a large globular fungal carbohydrate-active enzyme domain. Its sequence and architecture are consistent with a fungal endo-xylanase; transferable knowledge of these enzymes supports hydrolysis of β-1,4 linkages (option B). This meaningfully favors B over the distinct enzyme class in A and the unrelated reaction classes in C and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a credible family-level route to the endo-xylanase choice without needing the exact protein's database annotation. This is a biologically informed inference rather than certainty about substrate specificity from sequence alone."
  },
  "case_id": "EC_number_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.8 and describes hydrolysis of (1→4)-β-D-xylosidic linkages, citing experimental evidence (ECO:0000269). The annotation is linked to a paper reporting characterization of the enzyme, though the paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only database evidence supports the key but was not part of the original input.",
    "The database annotation cites experimental evidence, but that underlying study was not independently evaluated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based endo-xylanase inference favors B among the offered choices; no alternative is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.8 and describes hydrolysis of (1→4)-β-D-xylosidic linkages, citing experimental evidence (ECO:0000269). The annotation is linked to a paper reporting characterization of the enzyme, though the paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, followed by a large globular fungal carbohydrate-active enzyme domain. Its sequence and architecture are consistent with a fungal endo-xylanase; transferable knowledge of these enzymes supports hydrolysis of β-1,4 linkages (option B). This meaningfully favors B over the distinct enzyme class in A and the unrelated reaction classes in C and D.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a credible family-level route to the endo-xylanase choice without needing the exact protein's database annotation. This is a biologically informed inference rather than certainty about substrate specificity from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based endo-xylanase inference favors B among the offered choices; no alternative is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only database evidence supports the key but was not part of the original input.",
    "The database annotation cites experimental evidence, but that underlying study was not independently evaluated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry M4MEY9 (XYNC_HUMIN) annotates this protein as Endo-1,4-beta-xylanase C with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed:23306124). The catalytic activity is explicitly stated as endohydrolysis of (1→4)-β-D-xylosidic linkages in xylans. Sequence match is confirmed (SHA256 identical, 390 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark GH11 (Glycoside Hydrolase family 11) xylanase motif 'ITVWGVSD' (visible in 'CVGITVWGVSDRDSWRSNENPLLYDGSYRPKAAYNALMNAL'), along with a fungal signal peptide and the characteristic β-jelly-roll catalytic domain architecture (~180-250 aa core within the 390-aa precursor). GH11 xylanases are well-known to correspond to EC 3.2.1.8 (endo-1,4-β-xylanase). The 'ITVWGVSD' motif with its conserved glutamate catalytic residues is a family-level signature learned from many characterized GH11 xylanases (Trichoderma, Aspergillus, Humicola, Bacillus, etc.). EC 4.2.3.1 (lyase, e.g., terpene synthase) and EC 2.7.7.43 (transferase, e.g., polynucleotide adenylyltransferase) would lack glycoside hydrolase motifs entirely. EC 3.2.1.105 (a different glycosidase family, e.g., β-agarase/GH86) would show different conserved motifs and domain architecture. Thus, recognizing the GH11 'ITVWGVSD' signature from family-level knowledge meaningfully distinguishes B (3.2.1.8) from all other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH11 ITVWGVSD motif and overall secreted-fungal-xylanase architecture are well-established transferable knowledge from numerous characterized GH11 xylanases. This family-level signature clearly separates a xylanase (EC 3.2.1.8) from lyases, transferases, and other glycosidase families, allowing a knowledgeable model to select B without needing the specific database annotation of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GH11 ITVWGVSD motif is specific to xylanases (EC 3.2.1.8) and does not overlap with the motifs expected for EC 3.2.1.105, EC 4.2.3.1, or EC 2.7.7.43. The distractors belong to entirely different reaction classes or glycosidase families with distinct sequence signatures.


### Important caveats

- The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational.
- The ITVWGVSD motif is a strong but not absolutely exclusive GH11 marker; some engineered variants or divergent members may show slight deviations, but in this sequence it is clearly present.
- EC 3.2.1.105 is a less common glycosidase; a model unfamiliar with this specific EC number might struggle to exclude it on motif grounds alone, but the overall GH11 architecture and fungal xylanase context strongly favor 3.2.1.8.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark GH11 (Glycoside Hydrolase family 11) xylanase motif 'ITVWGVSD' (visible in 'CVGITVWGVSDRDSWRSNENPLLYDGSYRPKAAYNALMNAL'), along with a fungal signal peptide and the characteristic β-jelly-roll catalytic domain architecture (~180-250 aa core within the 390-aa precursor). GH11 xylanases are well-known to correspond to EC 3.2.1.8 (endo-1,4-β-xylanase). The 'ITVWGVSD' motif with its conserved glutamate catalytic residues is a family-level signature learned from many characterized GH11 xylanases (Trichoderma, Aspergillus, Humicola, Bacillus, etc.). EC 4.2.3.1 (lyase, e.g., terpene synthase) and EC 2.7.7.43 (transferase, e.g., polynucleotide adenylyltransferase) would lack glycoside hydrolase motifs entirely. EC 3.2.1.105 (a different glycosidase family, e.g., β-agarase/GH86) would show different conserved motifs and domain architecture. Thus, recognizing the GH11 'ITVWGVSD' signature from family-level knowledge meaningfully distinguishes B (3.2.1.8) from all other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH11 ITVWGVSD motif and overall secreted-fungal-xylanase architecture are well-established transferable knowledge from numerous characterized GH11 xylanases. This family-level signature clearly separates a xylanase (EC 3.2.1.8) from lyases, transferases, and other glycosidase families, allowing a knowledgeable model to select B without needing the specific database annotation of this exact protein."
  },
  "case_id": "EC_number_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry M4MEY9 (XYNC_HUMIN) annotates this protein as Endo-1,4-beta-xylanase C with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed:23306124). The catalytic activity is explicitly stated as endohydrolysis of (1→4)-β-D-xylosidic linkages in xylans. Sequence match is confirmed (SHA256 identical, 390 aa)."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational.",
    "The ITVWGVSD motif is a strong but not absolutely exclusive GH11 marker; some engineered variants or divergent members may show slight deviations, but in this sequence it is clearly present.",
    "EC 3.2.1.105 is a less common glycosidase; a model unfamiliar with this specific EC number might struggle to exclude it on motif grounds alone, but the overall GH11 architecture and fungal xylanase context strongly favor 3.2.1.8."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH11 ITVWGVSD motif is specific to xylanases (EC 3.2.1.8) and does not overlap with the motifs expected for EC 3.2.1.105, EC 4.2.3.1, or EC 2.7.7.43. The distractors belong to entirely different reaction classes or glycosidase families with distinct sequence signatures."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry M4MEY9 (XYNC_HUMIN) annotates this protein as Endo-1,4-beta-xylanase C with EC 3.2.1.8, supported by experimental evidence (ECO:0000269, PubMed:23306124). The catalytic activity is explicitly stated as endohydrolysis of (1→4)-β-D-xylosidic linkages in xylans. Sequence match is confirmed (SHA256 identical, 390 aa).",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark GH11 (Glycoside Hydrolase family 11) xylanase motif 'ITVWGVSD' (visible in 'CVGITVWGVSDRDSWRSNENPLLYDGSYRPKAAYNALMNAL'), along with a fungal signal peptide and the characteristic β-jelly-roll catalytic domain architecture (~180-250 aa core within the 390-aa precursor). GH11 xylanases are well-known to correspond to EC 3.2.1.8 (endo-1,4-β-xylanase). The 'ITVWGVSD' motif with its conserved glutamate catalytic residues is a family-level signature learned from many characterized GH11 xylanases (Trichoderma, Aspergillus, Humicola, Bacillus, etc.). EC 4.2.3.1 (lyase, e.g., terpene synthase) and EC 2.7.7.43 (transferase, e.g., polynucleotide adenylyltransferase) would lack glycoside hydrolase motifs entirely. EC 3.2.1.105 (a different glycosidase family, e.g., β-agarase/GH86) would show different conserved motifs and domain architecture. Thus, recognizing the GH11 'ITVWGVSD' signature from family-level knowledge meaningfully distinguishes B (3.2.1.8) from all other choices.",
    "missing_item_specific_fact": "",
    "reason": "The GH11 ITVWGVSD motif and overall secreted-fungal-xylanase architecture are well-established transferable knowledge from numerous characterized GH11 xylanases. This family-level signature clearly separates a xylanase (EC 3.2.1.8) from lyases, transferases, and other glycosidase families, allowing a knowledgeable model to select B without needing the specific database annotation of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH11 ITVWGVSD motif is specific to xylanases (EC 3.2.1.8) and does not overlap with the motifs expected for EC 3.2.1.105, EC 4.2.3.1, or EC 2.7.7.43. The distractors belong to entirely different reaction classes or glycosidase families with distinct sequence signatures."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational.",
    "The ITVWGVSD motif is a strong but not absolutely exclusive GH11 marker; some engineered variants or divergent members may show slight deviations, but in this sequence it is clearly present.",
    "EC 3.2.1.105 is a less common glycosidase; a model unfamiliar with this specific EC number might struggle to exclude it on motif grounds alone, but the overall GH11 architecture and fungal xylanase context strongly favor 3.2.1.8."
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
  "benchmark_sequence_length": 390,
  "benchmark_sequence_sha256": "1c8664061e849fad663355cf9160457527204ce7ad6cf995f8c64f1f58ff76bd",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 390,
  "current_source_sequence_sha256": "1c8664061e849fad663355cf9160457527204ce7ad6cf995f8c64f1f58ff76bd",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 41,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "M4MEY9",
  "selected_historical_entry_version": 41,
  "selected_historical_record_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "selected_historical_source_sequence_length": 390,
  "selected_historical_source_sequence_sha256": "1c8664061e849fad663355cf9160457527204ce7ad6cf995f8c64f1f58ff76bd",
  "selected_historical_version": {
    "accession": "M4MEY9",
    "database": "Swiss-Prot",
    "entryVersion": 41,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNC_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MEY9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase C\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase C\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:11.429543+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e",
  "url": "https://rest.uniprot.org/uniprotkb/M4MEY9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H1",
  "excerpt": "ID   XYNC_HUMIN              Reviewed;         390 AA.\nAC   M4MEY9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 41.\nDE   RecName: Full=Endo-1,4-beta-xylanase C {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase C {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynC {ECO:0000303|PubMed:23306124};\nGN   Synonyms=Xyl3 {ECO:0000303|PubMed:8190078},\nGN   XynW {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Endo-1,4-beta-xylanase C {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase C {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   IDENTIFICATION.\nRX   PubMed=8190078; DOI=10.1007/bf00301060;\nRA   Dalboege H., Hansen H.P.H.;\nRT   \"A novel method for efficient expression cloning of fungal enzyme genes.\";\nRL   Mol. Gen. Genet. 243:253-260(1994).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:23306124};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.495114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b",
  "url": "https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
