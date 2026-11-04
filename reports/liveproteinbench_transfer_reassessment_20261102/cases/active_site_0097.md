# active_site_0097

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0097.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 170 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MHLASSLFLLATLPFGFAAGKGKGKGKDNSDVGLDVLAKKAGLKYFGAATDTPGQRERAGLEDKYPEYDRIMWHSPEFGSTTPTNGQKWLFVEPERGVFNFTEGDVVASKARQHGKLLRCHALVWHSQLAPWVEETEWTPEELRKVIVDHITAVAGHYKGQCYAWDVVNEALNEDGTYRESVFYKVLGEEYIKLAFETAAKVDPKAKLYYNDYNLEWPSAKTEGAKRIVKLLKDAKIPIHGVGLQAHLIAEQHPTLDDHIAAIRGFTQLGVEVALTELDIRLKTPATEENLALQREAYKNVVGACVQVCGCVGVTIWDFYDPFSWVPYFFEGEGAPLLWFEDFSKHPAYYGVVEALTNKTRRSKRSISDRRAKLLA

[Multiple Choices]
A. Position 217 (Lowers pKa of active site Tyr)
B. Position 170 (Proton donor)
C. Position 735 (For beta-ketoacyl synthase activity)
D. Position 27 (Proton acceptor)
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

> The sequence-matched UniProt record annotates position 170 as the proton donor, with the annotation attributed to a PROSITE-ProRule. This supports the key, though it is computational annotation rather than direct residue-specific experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a fungal xylanase in the GH10-like glycosidase family. Transferable knowledge of this family’s conserved catalytic glutamates makes a proton-donor assignment at position 170 credible; position 27 lies in the N-terminal signal-peptide region, position 735 is outside the 376-residue sequence, and the Tyr/pKa claim at 217 does not fit the usual xylanase catalytic mechanism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence and catalytic-mechanism knowledge meaningfully favors B among these choices without needing the exact protein’s database record. The inference is credible but does not independently prove the residue’s role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives do not present another comparably plausible catalytic-residue assignment; one position is out of range and another is in the signal-peptide region.


### Important caveats

- The reviewer-only annotation is computationally attributed to PROSITE-ProRule; the supplied evidence does not establish direct experimental validation of position 170.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a fungal xylanase in the GH10-like glycosidase family. Transferable knowledge of this family’s conserved catalytic glutamates makes a proton-donor assignment at position 170 credible; position 27 lies in the N-terminal signal-peptide region, position 735 is outside the 376-residue sequence, and the Tyr/pKa claim at 217 does not fit the usual xylanase catalytic mechanism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and catalytic-mechanism knowledge meaningfully favors B among these choices without needing the exact protein’s database record. The inference is credible but does not independently prove the residue’s role."
  },
  "case_id": "active_site_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 170 as the proton donor, with the annotation attributed to a PROSITE-ProRule. This supports the key, though it is computational annotation rather than direct residue-specific experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only annotation is computationally attributed to PROSITE-ProRule; the supplied evidence does not establish direct experimental validation of position 170."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives do not present another comparably plausible catalytic-residue assignment; one position is out of range and another is in the signal-peptide region."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 170 as the proton donor, with the annotation attributed to a PROSITE-ProRule. This supports the key, though it is computational annotation rather than direct residue-specific experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a fungal xylanase in the GH10-like glycosidase family. Transferable knowledge of this family’s conserved catalytic glutamates makes a proton-donor assignment at position 170 credible; position 27 lies in the N-terminal signal-peptide region, position 735 is outside the 376-residue sequence, and the Tyr/pKa claim at 217 does not fit the usual xylanase catalytic mechanism.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and catalytic-mechanism knowledge meaningfully favors B among these choices without needing the exact protein’s database record. The inference is credible but does not independently prove the residue’s role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives do not present another comparably plausible catalytic-residue assignment; one position is out of range and another is in the signal-peptide region."
  },
  "important_caveats": [
    "The reviewer-only annotation is computationally attributed to PROSITE-ProRule; the supplied evidence does not establish direct experimental validation of position 170."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) explicitly lists position 170 as 'Proton donor' with evidence ECO:0000255|PROSITE-ProRule:PRU01096 (GH10 glycoside hydrolase profile). The residue at position 170 in the supplied sequence is Glu (E), consistent with the GH10 catalytic mechanism. The annotation is computational (PROSITE-ProRule profiling) rather than directly experimental, but it is a well-established family-level assignment for GH10 xylanases. The expected answer B is supported.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark GH10 xylanase motifs, notably the 'WDF' motif (~position 290) and the characteristic catalytic Glu pair separated by ~107 residues (E170 and E277). A model recognizing GH10 family features (the DF motif, the TIM-barrel fold sequence context, the two-Glu catalytic dyad with ~100-110 residue spacing) can identify the proton donor as the N-terminal Glu (position 170) and the nucleophile as the C-terminal Glu (position 277). Furthermore, the distractors are eliminable: C references position 735 in a 376-residue protein (impossible); D places a 'proton acceptor' at position 27, which falls within the signal peptide (MHLASSLFLLATLPFGFAAG); A invokes 'Tyr pKa lowering,' a mechanism associated with tyrosinase/catechol oxidase, not xylanase. Family-level knowledge from other GH10 xylanases (e.g., xylanase A from other fungi) establishes that the first Glu in the catalytic pair acts as proton donor, making B the only consistent choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of GH10 family sequence motifs (DF motif, two-Glu catalytic dyad with ~107-residue spacing) is transferable knowledge from other GH10 proteins. The proton-donor/nucleophile assignment follows from established family-level catalytic mechanism. The other options are eliminated by basic facts (C exceeds protein length, D is in the signal peptide, A describes a non-xylanase mechanism). No target-specific memorization is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option B is consistent with the protein being a GH10 xylanase. Option C is physically impossible (position 735 in a 376-aa protein), D places a catalytic residue in the signal peptide, and A describes a tyrosinase-type mechanism irrelevant to xylanases.


### Important caveats

- The UniProt active-site annotation uses ECO:0000255 (PROSITE-ProRule), a computational profiling annotation rather than direct experimental mutagenesis evidence for this specific protein.
- The model must correctly identify the protein as a GH10 xylanase from sequence motifs; if it misidentifies the family, the reasoning path breaks down.
- The question lists only one catalytic residue (proton donor at 170) rather than both (nucleophile at 277), which is a valid subset of the active site but may confuse a model expecting the full catalytic pair.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark GH10 xylanase motifs, notably the 'WDF' motif (~position 290) and the characteristic catalytic Glu pair separated by ~107 residues (E170 and E277). A model recognizing GH10 family features (the DF motif, the TIM-barrel fold sequence context, the two-Glu catalytic dyad with ~100-110 residue spacing) can identify the proton donor as the N-terminal Glu (position 170) and the nucleophile as the C-terminal Glu (position 277). Furthermore, the distractors are eliminable: C references position 735 in a 376-residue protein (impossible); D places a 'proton acceptor' at position 27, which falls within the signal peptide (MHLASSLFLLATLPFGFAAG); A invokes 'Tyr pKa lowering,' a mechanism associated with tyrosinase/catechol oxidase, not xylanase. Family-level knowledge from other GH10 xylanases (e.g., xylanase A from other fungi) establishes that the first Glu in the catalytic pair acts as proton donor, making B the only consistent choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of GH10 family sequence motifs (DF motif, two-Glu catalytic dyad with ~107-residue spacing) is transferable knowledge from other GH10 proteins. The proton-donor/nucleophile assignment follows from established family-level catalytic mechanism. The other options are eliminated by basic facts (C exceeds protein length, D is in the signal peptide, A describes a non-xylanase mechanism). No target-specific memorization is required."
  },
  "case_id": "active_site_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly lists position 170 as 'Proton donor' with evidence ECO:0000255|PROSITE-ProRule:PRU01096 (GH10 glycoside hydrolase profile). The residue at position 170 in the supplied sequence is Glu (E), consistent with the GH10 catalytic mechanism. The annotation is computational (PROSITE-ProRule profiling) rather than directly experimental, but it is a well-established family-level assignment for GH10 xylanases. The expected answer B is supported."
  },
  "important_caveats": [
    "The UniProt active-site annotation uses ECO:0000255 (PROSITE-ProRule), a computational profiling annotation rather than direct experimental mutagenesis evidence for this specific protein.",
    "The model must correctly identify the protein as a GH10 xylanase from sequence motifs; if it misidentifies the family, the reasoning path breaks down.",
    "The question lists only one catalytic residue (proton donor at 170) rather than both (nucleophile at 277), which is a valid subset of the active site but may confuse a model expecting the full catalytic pair."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B is consistent with the protein being a GH10 xylanase. Option C is physically impossible (position 735 in a 376-aa protein), D places a catalytic residue in the signal peptide, and A describes a tyrosinase-type mechanism irrelevant to xylanases."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly lists position 170 as 'Proton donor' with evidence ECO:0000255|PROSITE-ProRule:PRU01096 (GH10 glycoside hydrolase profile). The residue at position 170 in the supplied sequence is Glu (E), consistent with the GH10 catalytic mechanism. The annotation is computational (PROSITE-ProRule profiling) rather than directly experimental, but it is a well-established family-level assignment for GH10 xylanases. The expected answer B is supported.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark GH10 xylanase motifs, notably the 'WDF' motif (~position 290) and the characteristic catalytic Glu pair separated by ~107 residues (E170 and E277). A model recognizing GH10 family features (the DF motif, the TIM-barrel fold sequence context, the two-Glu catalytic dyad with ~100-110 residue spacing) can identify the proton donor as the N-terminal Glu (position 170) and the nucleophile as the C-terminal Glu (position 277). Furthermore, the distractors are eliminable: C references position 735 in a 376-residue protein (impossible); D places a 'proton acceptor' at position 27, which falls within the signal peptide (MHLASSLFLLATLPFGFAAG); A invokes 'Tyr pKa lowering,' a mechanism associated with tyrosinase/catechol oxidase, not xylanase. Family-level knowledge from other GH10 xylanases (e.g., xylanase A from other fungi) establishes that the first Glu in the catalytic pair acts as proton donor, making B the only consistent choice.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of GH10 family sequence motifs (DF motif, two-Glu catalytic dyad with ~107-residue spacing) is transferable knowledge from other GH10 proteins. The proton-donor/nucleophile assignment follows from established family-level catalytic mechanism. The other options are eliminated by basic facts (C exceeds protein length, D is in the signal peptide, A describes a non-xylanase mechanism). No target-specific memorization is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B is consistent with the protein being a GH10 xylanase. Option C is physically impossible (position 735 in a 376-aa protein), D places a catalytic residue in the signal peptide, and A describes a tyrosinase-type mechanism irrelevant to xylanases."
  },
  "important_caveats": [
    "The UniProt active-site annotation uses ECO:0000255 (PROSITE-ProRule), a computational profiling annotation rather than direct experimental mutagenesis evidence for this specific protein.",
    "The model must correctly identify the protein as a GH10 xylanase from sequence motifs; if it misidentifies the family, the reasoning path breaks down.",
    "The question lists only one catalytic residue (proton donor at 170) rather than both (nucleophile at 277), which is a valid subset of the active site but may confuse a model expecting the full catalytic pair."
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
  "benchmark_sequence_length": 376,
  "benchmark_sequence_sha256": "099e0d9d31b95aad01d9114eec635a5ba258509622920c5ebd279553304abc33",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 376,
  "current_source_sequence_sha256": "099e0d9d31b95aad01d9114eec635a5ba258509622920c5ebd279553304abc33",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "M4MGK7",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "selected_historical_source_sequence_length": 376,
  "selected_historical_source_sequence_sha256": "099e0d9d31b95aad01d9114eec635a5ba258509622920c5ebd279553304abc33",
  "selected_historical_version": {
    "accession": "M4MGK7",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNA_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MGK7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase A\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01096\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":170},\"start\":{\"modifier\":\"EXACT\",\"value\":170}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01096\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":277},\"start\":{\"modifier\":\"EXACT\",\"value\":277}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   XYNA_HUMIN              Reviewed;         376 AA.\nAC   M4MGK7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Endo-1,4-beta-xylanase A {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase A {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynA {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        170\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01096\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        277\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01096\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
