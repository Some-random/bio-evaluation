# transmembrane_0028

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0028.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 1404..1424

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGKTKIYSVGFTVHEAQTLVTEKGQPVDPLVVVRCCGREYRTEIKYAKSNVVSWDESHTWTDLCLTDEEWETAYITFEVQAANAFWRNTLLGLVSVQLRLIQLRKTHQIRKALPLQHPDDTDVHGSLRVTVFACAPGEAPPSPGEEEVLEEEDHNDYDDLRKAVIDTNQVVEREAGSRLYHVYVTAYRVEDLPRSSKGARDPFVTCEFAGCKLKSTQARGCCSHTFNECFRFPVVTPLPEDAILIKIWDWNFMKADELIAVGRISFSELRTRQMVPRWFNLYGFDDEEVAQATKVAGQGGRLVANCYLGRILLGARAERLTKEDDLMPAHTVAARPYETPPVIPLAVLADVYEVQGAPGEKVSVEIWCGPARARTKWVTGLETKAAQRAGVAPQAFNRAMEGALGVASYLRGDIPEGEDRFPFDNTEGRVEDLRLVVPEDTKQQWDIIISLYVRGTTKGFMGDTRIAFQRLKMSKIPGHVHNNPRAPIWVPLISTPPFESVKPAPAILMVIEKSKVEAFARSKRKHVTAVGYQLRAYVYAARNLLSPSGALPNPFVQVACAGTSRETEVFEQTSSPVFMDCLLLDITMMTDPVSRLPTVAPIVVTLFEQRSWGIQFLGRATCHYDRLRGRLKPGESPTVAEPRWIKLRGGKYANRHLGDVLLLLELIRKRDAEIIPAFPMRPVVNMCNLTFSCLGVRSLYMTQRAKRLDYVSIRKGQDKKTELRRIRGPLLRISVSSYASAGRGNNEAILRYERNLPEDPTTVNKLWTTVTKAANADIFKVVNMEIDVPVDPIYDPRLVVQVYDRKQKPKYFIGEYSMSLVPLIPWVLDQQSAIEAVSPVNDFTDTVDLKHLGGLLRGFHGNSKNRGTGQIGLEALSAADRETADAHKEKTLAQSRFATYDPDNKTFSDSWLLPSGLPKILVSSYAVPGFRCDVIYTNMFTLNVYIPAKFVLFAEGKRAADKKTKEQYARPSVDSTLEQFLDDVIFPSDSLKKSVMGDIDVTGFVKFFVNLTHHEEPNPHVDSSAAEWASSEDRMRRHLRGEDAYPKLLKIRVYVIRAISLYVGDDRILPNPYLLFNLGDKSDTLRAEAKPNTHNPEFFTVWEKDVMFPDDSQFELQVWSAHEGTSGGLDDIFIGSTCIDLEERWFSKEWQKSMSKNQVPMEYRPLKQMPSGSFKGTVEMWVELMDFQKAGEVPKFDLQSPAATEVEIRVIVWGARNLNFKALGKDFVDAMIRCNLDCTGYRGSQPIAQQTDVHYYSKTGAAIFNWRMVYSRVVMPVSTCVLQIAAYDNRNMGESPFIGEVNLELRRYLERVASTLNSIDVDAELKLINRSRESADVSSFGFVQVSLQFISQSEATSKPVGLGREPPNRDPRLTTPQEGRKWEDVLGSAGLRVDYRPLWYWVRVAAVVFLSIWIFVVAFLYPSLLG

[Multiple Choices]
A. 35..55
B. 1408..1428
C. 1404..1424
D. 1404..1424; 630..652
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

> The sequence-matched UniProt annotation identifies a helical transmembrane region at 1404..1424. Its evidence code (ECO:0000255) indicates computational annotation, not direct experimental validation, but it supports the keyed answer for the property asked.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conspicuous C-terminal stretch rich in hydrophobic residues, consistent with a membrane-spanning helix. Choice C covers that stretch; B extends past the 1426-residue sequence, and D adds a region at 630..652 that does not show a comparable uninterrupted hydrophobic segment. A transferable sequence-based inference therefore distinguishes C among these options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The terminal hydrophobic run and the sequence length are visible in the original input. Recognizing that a roughly 20-residue hydrophobic helix is characteristic of a transmembrane segment is transferable biological knowledge; exact boundaries may be approximate, but the offered alternatives make C meaningfully distinguishable.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is the offered interval that matches the C-terminal hydrophobic stretch. B exceeds the supplied sequence length, while D adds a region without a comparably clear membrane-spanning sequence.


### Important caveats

- The supporting database annotation is computational, not direct experimental evidence.
- Predicted transmembrane boundaries can be approximate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conspicuous C-terminal stretch rich in hydrophobic residues, consistent with a membrane-spanning helix. Choice C covers that stretch; B extends past the 1426-residue sequence, and D adds a region at 630..652 that does not show a comparable uninterrupted hydrophobic segment. A transferable sequence-based inference therefore distinguishes C among these options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The terminal hydrophobic run and the sequence length are visible in the original input. Recognizing that a roughly 20-residue hydrophobic helix is characteristic of a transmembrane segment is transferable biological knowledge; exact boundaries may be approximate, but the offered alternatives make C meaningfully distinguishable."
  },
  "case_id": "transmembrane_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies a helical transmembrane region at 1404..1424. Its evidence code (ECO:0000255) indicates computational annotation, not direct experimental validation, but it supports the keyed answer for the property asked."
  },
  "important_caveats": [
    "The supporting database annotation is computational, not direct experimental evidence.",
    "Predicted transmembrane boundaries can be approximate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the offered interval that matches the C-terminal hydrophobic stretch. B exceeds the supplied sequence length, while D adds a region without a comparably clear membrane-spanning sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies a helical transmembrane region at 1404..1424. Its evidence code (ECO:0000255) indicates computational annotation, not direct experimental validation, but it supports the keyed answer for the property asked.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conspicuous C-terminal stretch rich in hydrophobic residues, consistent with a membrane-spanning helix. Choice C covers that stretch; B extends past the 1426-residue sequence, and D adds a region at 630..652 that does not show a comparable uninterrupted hydrophobic segment. A transferable sequence-based inference therefore distinguishes C among these options.",
    "missing_item_specific_fact": "",
    "reason": "The terminal hydrophobic run and the sequence length are visible in the original input. Recognizing that a roughly 20-residue hydrophobic helix is characteristic of a transmembrane segment is transferable biological knowledge; exact boundaries may be approximate, but the offered alternatives make C meaningfully distinguishable."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the offered interval that matches the C-terminal hydrophobic stretch. B exceeds the supplied sequence length, while D adds a region without a comparably clear membrane-spanning sequence."
  },
  "important_caveats": [
    "The supporting database annotation is computational, not direct experimental evidence.",
    "Predicted transmembrane boundaries can be approximate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H4) explicitly lists a transmembrane helical region at 1404..1424 with evidence code ECO:0000255 (by similarity, i.e., computational). The sequence at positions 1404-1424 corresponds to VAAVVFLSIWIFVVAFLYPSLL, a 21-residue stretch of predominantly hydrophobic residues consistent with a single-pass TM helix. The sequence length is 1426, so this annotation is within range. The expected answer C matches the annotated region.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A model can apply standard hydrophobicity analysis to distinguish the options. (1) Option B (1408..1428) is immediately eliminated because the sequence is only 1426 residues long, making position 1428 out of range. (2) Option A (35..55) corresponds to CGREYRTEIKYAKSNVVSWDE, which contains multiple charged residues (R, E, K, K, D, E) and cannot form a TM helix. (3) The C-terminal region (approximately 1404-1424: VAAVVFLSIWIFVVAFLYPSLL) is a clear 21-residue hydrophobic stretch consistent with a TM alpha-helix. (4) Option D adds a second TM region at 630..652. Examining that region (RGNNEAILRYERNLPEDPTTVNK) reveals numerous charged and polar residues (R, N, E, D, K), making it incompatible with a TM helix. More broadly, the middle of this 1426-residue protein is dominated by charged/polar residues typical of cytosolic domains, while the only sufficiently long hydrophobic stretch is at the C-terminus. General membrane-protein topology knowledge (single-pass proteins have one TM helix; the rest is hydrophilic cytosolic/extracellular) supports choosing C over D without needing to know the specific protein identity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is answerable by hydrophobicity analysis of the provided sequence combined with general knowledge of TM helix requirements (~20 hydrophobic residues) and membrane protein topology. The C-terminal hydrophobic stretch is unambiguous, option B is out of range, option A is clearly charged, and option D's additional region at 630-652 is also charged. No protein-specific annotation or database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D each contain clear disqualifying features: A has charged residues at the claimed TM position, B exceeds the sequence length, and D's additional region at 630-652 is clearly hydrophilic. Only C identifies a genuine hydrophobic TM stretch within the valid sequence range.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), meaning it is a computational/transferred prediction rather than experimentally verified.
- Precisely counting to position 630 in a 1426-residue sequence is challenging for a language model, but the overall hydrophobicity pattern (charged middle, hydrophobic C-terminus) allows reasoning about single-pass topology without exact residue counting.
- The sequence is from Toxoplasma gondii Ferlin 2 (a rhoptry protein), but this identity is not needed to answer the question from sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can apply standard hydrophobicity analysis to distinguish the options. (1) Option B (1408..1428) is immediately eliminated because the sequence is only 1426 residues long, making position 1428 out of range. (2) Option A (35..55) corresponds to CGREYRTEIKYAKSNVVSWDE, which contains multiple charged residues (R, E, K, K, D, E) and cannot form a TM helix. (3) The C-terminal region (approximately 1404-1424: VAAVVFLSIWIFVVAFLYPSLL) is a clear 21-residue hydrophobic stretch consistent with a TM alpha-helix. (4) Option D adds a second TM region at 630..652. Examining that region (RGNNEAILRYERNLPEDPTTVNK) reveals numerous charged and polar residues (R, N, E, D, K), making it incompatible with a TM helix. More broadly, the middle of this 1426-residue protein is dominated by charged/polar residues typical of cytosolic domains, while the only sufficiently long hydrophobic stretch is at the C-terminus. General membrane-protein topology knowledge (single-pass proteins have one TM helix; the rest is hydrophilic cytosolic/extracellular) supports choosing C over D without needing to know the specific protein identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable by hydrophobicity analysis of the provided sequence combined with general knowledge of TM helix requirements (~20 hydrophobic residues) and membrane protein topology. The C-terminal hydrophobic stretch is unambiguous, option B is out of range, option A is clearly charged, and option D's additional region at 630-652 is also charged. No protein-specific annotation or database lookup is required."
  },
  "case_id": "transmembrane_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H4) explicitly lists a transmembrane helical region at 1404..1424 with evidence code ECO:0000255 (by similarity, i.e., computational). The sequence at positions 1404-1424 corresponds to VAAVVFLSIWIFVVAFLYPSLL, a 21-residue stretch of predominantly hydrophobic residues consistent with a single-pass TM helix. The sequence length is 1426, so this annotation is within range. The expected answer C matches the annotated region."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), meaning it is a computational/transferred prediction rather than experimentally verified.",
    "Precisely counting to position 630 in a 1426-residue sequence is challenging for a language model, but the overall hydrophobicity pattern (charged middle, hydrophobic C-terminus) allows reasoning about single-pass topology without exact residue counting.",
    "The sequence is from Toxoplasma gondii Ferlin 2 (a rhoptry protein), but this identity is not needed to answer the question from sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D each contain clear disqualifying features: A has charged residues at the claimed TM position, B exceeds the sequence length, and D's additional region at 630-652 is clearly hydrophilic. Only C identifies a genuine hydrophobic TM stretch within the valid sequence range."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H4) explicitly lists a transmembrane helical region at 1404..1424 with evidence code ECO:0000255 (by similarity, i.e., computational). The sequence at positions 1404-1424 corresponds to VAAVVFLSIWIFVVAFLYPSLL, a 21-residue stretch of predominantly hydrophobic residues consistent with a single-pass TM helix. The sequence length is 1426, so this annotation is within range. The expected answer C matches the annotated region.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A model can apply standard hydrophobicity analysis to distinguish the options. (1) Option B (1408..1428) is immediately eliminated because the sequence is only 1426 residues long, making position 1428 out of range. (2) Option A (35..55) corresponds to CGREYRTEIKYAKSNVVSWDE, which contains multiple charged residues (R, E, K, K, D, E) and cannot form a TM helix. (3) The C-terminal region (approximately 1404-1424: VAAVVFLSIWIFVVAFLYPSLL) is a clear 21-residue hydrophobic stretch consistent with a TM alpha-helix. (4) Option D adds a second TM region at 630..652. Examining that region (RGNNEAILRYERNLPEDPTTVNK) reveals numerous charged and polar residues (R, N, E, D, K), making it incompatible with a TM helix. More broadly, the middle of this 1426-residue protein is dominated by charged/polar residues typical of cytosolic domains, while the only sufficiently long hydrophobic stretch is at the C-terminus. General membrane-protein topology knowledge (single-pass proteins have one TM helix; the rest is hydrophilic cytosolic/extracellular) supports choosing C over D without needing to know the specific protein identity.",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable by hydrophobicity analysis of the provided sequence combined with general knowledge of TM helix requirements (~20 hydrophobic residues) and membrane protein topology. The C-terminal hydrophobic stretch is unambiguous, option B is out of range, option A is clearly charged, and option D's additional region at 630-652 is also charged. No protein-specific annotation or database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D each contain clear disqualifying features: A has charged residues at the claimed TM position, B exceeds the sequence length, and D's additional region at 630-652 is clearly hydrophilic. Only C identifies a genuine hydrophobic TM stretch within the valid sequence range."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), meaning it is a computational/transferred prediction rather than experimentally verified.",
    "Precisely counting to position 630 in a 1426-residue sequence is challenging for a language model, but the overall hydrophobicity pattern (charged middle, hydrophobic C-terminus) allows reasoning about single-pass topology without exact residue counting.",
    "The sequence is from Toxoplasma gondii Ferlin 2 (a rhoptry protein), but this identity is not needed to answer the question from sequence features alone."
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
  "benchmark_sequence_length": 1426,
  "benchmark_sequence_sha256": "5f16751b277974553550fa64f384077c33893fe628f81cead65b9d7ff0905bb2",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-04-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1426,
  "current_source_sequence_sha256": "5f16751b277974553550fa64f384077c33893fe628f81cead65b9d7ff0905bb2",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7J6K2G0",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "selected_historical_source_sequence_length": 1426,
  "selected_historical_source_sequence_sha256": "5f16751b277974553550fa64f384077c33893fe628f81cead65b9d7ff0905bb2",
  "selected_historical_version": {
    "accession": "A0A7J6K2G0",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FER2_TOXGO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7J6K2G0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-04-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000557509\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii\",\"taxonId\":5811}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30279285\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"Ferlin 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"FER2\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30279285\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"TgFER2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1424},\"start\":{\"modifier\":\"EXACT\",\"value\":1404}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Coleman B.I.\",\"Saha S.\",\"Sato S.\",\"Engelberg K.\",\"Ferguson D.J.P.\",\"Coppens I.\",\"Lodoen M.B.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30279285\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.01510-18\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30279285\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2018\",\"title\":\"A Member of the Ferlin Calcium Sensor Family Is Essential for Toxoplasma gondii Rhoptry Secretion.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30279285\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"RH\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Tagoe D.N.A.\",\"Drozda A.A.\",\"Falco J.A.\",\"Bechtel T.J.\",\"Weerapana E.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33803212\"},{\"database\":\"DOI\",\"id\":\"10.3390/life11030217\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"33803212\",\"journal\":\"Life\",\"lastPage\":\"0\",\"publicationDate\":\"2021\",\"title\":\"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule Secretion.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"RH\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:50.269882+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   FER2_TOXGO              Reviewed;        1426 AA.\nAC   A0A7J6K2G0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-APR-2021, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Ferlin 2 {ECO:0000303|PubMed:30279285, ECO:0000303|PubMed:33803212};\nDE            Short=FER2 {ECO:0000303|PubMed:33803212};\nDE            Short=TgFER2 {ECO:0000303|PubMed:30279285, ECO:0000303|PubMed:33803212};\nGN   ORFNames=TGRH88_069870 {ECO:0000312|EMBL:KAF4641177.1};\nOS   Toxoplasma gondii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=5811 {ECO:0000312|Proteomes:UP000557509};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=RH {ECO:0000303|PubMed:30279285};\nRX   PubMed=30279285; DOI=10.1128/mbio.01510-18;\nRA   Coleman B.I., Saha S., Sato S., Engelberg K., Ferguson D.J.P., Coppens I.,\nRA   Lodoen M.B., Gubbels M.J.;\nRT   \"A Member of the Ferlin Calcium Sensor Family Is Essential for Toxoplasma\nRT   gondii Rhoptry Secretion.\";\nRL   MBio 9:0-0(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION.\nRC   STRAIN=RH {ECO:0000303|PubMed:33803212};\nRX   PubMed=33803212; DOI=10.3390/life11030217;\nRA   Tagoe D.N.A., Drozda A.A., Falco J.A., Bechtel T.J., Weerapana E.,\nRA   Gubbels M.J.;\nRT   \"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule\nRT   Secretion.\";\nRL   Life 11:0-0(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        1404..1424\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.007451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
