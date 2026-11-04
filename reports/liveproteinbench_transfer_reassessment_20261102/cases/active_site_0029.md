# active_site_0029

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0029.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 286 (Charge relay system)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRTVFIYACIISLVLRTIPAHNDLMSKEKENKEKDVHKIIEDLRFLEKVDAILENSNMTIDDVKADADAYNPDEDAPKEELNKIEMEKKKAEEEAKNSKKKILERYLLDEKKKKSLRLIVSENHATSPSFFEESLIQEDFMSFIQSKGEIVNLKNLKSMIIELNSDMTDKELEAYITLLKKKGAHVESDELVGADSIYVDIIKDAVKRGDTSINFKKMQSNMLEVENKTYEKLNNNLKKSKNSYKKSFFNDEYRNLQWGLDLARLDDAQEMITTNSVETTKICVIDSGIDYNHPDLKGNIYVNLNELNGKEGIDDDNNGIIDDIYGVNYVNNTGDPWDDHNHGSHVSGIISAIGNNSIGVVGVNPSSKLVICKALDDKKLGRLGNIFKCIDYCINKKVNIINGSFSFDEYSTIFSSTIEYLARLGILFVVSSSNCSHPPSSIPDITRCDLSVNSKYPSVLSTQYDNMVVVANLKKKINGEYDISINSFYSDIYCQVSAPGANIYSTASRGSYMELSGTSMAAPHVAGIASIILSINPDLTYKQVVNILKNSVVKLSSHKNKIAWGGYIDILNAVKNAISSKNSYIRFQGIRMWKSKKRN

[Multiple Choices]
A. Position 286 (Charge relay system)
B. Position 180 (For beta-ketoacyl synthase activity)
C. Position 12 (Proton acceptor)
D. Position 365 (For beta-ketoacyl synthase 1 activity)
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

> The sequence-matched UniProt record annotates position 286 as part of the charge-relay system. This is a computational PROSITE-ProRule annotation, not direct experimental validation of that residue in this protein.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a secreted subtilisin-like serine protease: its N-terminal hydrophobic segment is signal-peptide-like, and the later enzyme region is compatible with a protease catalytic domain. Subtilisin-family proteases use a conserved Asp-His-Ser charge relay. Position 286 is a plausible catalytic charge-relay residue, whereas position 12 lies in the signal-peptide-like segment and the beta-ketoacyl-synthase choices name an unrelated enzyme activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the sequence context give a meaningful basis to select A among these alternatives without knowing this protein's database annotation. This supports a probabilistic inference, not experimental proof of the exact residue's role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A is compatible with the sequence-based subtilisin-protease inference among the offered choices. Although the full charge relay includes multiple residues, the other offered positions do not provide a comparably defensible alternative.


### Important caveats

- The supplied evidence supports position 286 through a computational annotation; it does not establish direct experimental confirmation.
- Position 286 is one component of a catalytic charge-relay system, not by itself the complete active site.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a secreted subtilisin-like serine protease: its N-terminal hydrophobic segment is signal-peptide-like, and the later enzyme region is compatible with a protease catalytic domain. Subtilisin-family proteases use a conserved Asp-His-Ser charge relay. Position 286 is a plausible catalytic charge-relay residue, whereas position 12 lies in the signal-peptide-like segment and the beta-ketoacyl-synthase choices name an unrelated enzyme activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the sequence context give a meaningful basis to select A among these alternatives without knowing this protein's database annotation. This supports a probabilistic inference, not experimental proof of the exact residue's role."
  },
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 286 as part of the charge-relay system. This is a computational PROSITE-ProRule annotation, not direct experimental validation of that residue in this protein."
  },
  "important_caveats": [
    "The supplied evidence supports position 286 through a computational annotation; it does not establish direct experimental confirmation.",
    "Position 286 is one component of a catalytic charge-relay system, not by itself the complete active site."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A is compatible with the sequence-based subtilisin-protease inference among the offered choices. Although the full charge relay includes multiple residues, the other offered positions do not provide a comparably defensible alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 286 as part of the charge-relay system. This is a computational PROSITE-ProRule annotation, not direct experimental validation of that residue in this protein.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a secreted subtilisin-like serine protease: its N-terminal hydrophobic segment is signal-peptide-like, and the later enzyme region is compatible with a protease catalytic domain. Subtilisin-family proteases use a conserved Asp-His-Ser charge relay. Position 286 is a plausible catalytic charge-relay residue, whereas position 12 lies in the signal-peptide-like segment and the beta-ketoacyl-synthase choices name an unrelated enzyme activity.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the sequence context give a meaningful basis to select A among these alternatives without knowing this protein's database annotation. This supports a probabilistic inference, not experimental proof of the exact residue's role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A is compatible with the sequence-based subtilisin-protease inference among the offered choices. Although the full charge relay includes multiple residues, the other offered positions do not provide a comparably defensible alternative."
  },
  "important_caveats": [
    "The supplied evidence supports position 286 through a computational annotation; it does not establish direct experimental confirmation.",
    "Position 286 is one component of a catalytic charge-relay system, not by itself the complete active site."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A509AM03 (Subtilisin-like protease 1, PbSUB1) explicitly annotates position 286 as an Active site with description 'Charge relay system' (evidence C5/H6). The protein is EC 3.4.21.62, a subtilisin-type serine protease whose catalytic triad (Asp286-His342-Ser519) constitutes the charge relay system. The annotation is based on PROSITE-ProRule (ECO:0000255, computational/prorule evidence), which is consistent with the well-established subtilisin mechanism. The sequence confirms: position 286 is Asp (in IDSG context), 342 is His (in NHGSHVSG context), and 519 is Ser (in GTSMA context), matching the canonical subtilisin triad.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'GTSMA' motif (positions 517-521: G-T-S-M-A), which is the hallmark signature of subtilisin-type serine proteases' catalytic serine. This is an extremely well-known family-level sequence feature. Subtilisins catalyze via an Asp-His-Ser 'charge relay system' — this is the standard mechanistic terminology for this enzyme family. Option A ('Position 286, Charge relay system') matches both the family identification (subtilisin) and the correct mechanistic description. Options B and D ('beta-ketoacyl synthase') refer to fatty acid synthase, a completely different enzyme class with a Cys-His-His active site and no sequence similarity to subtilisins. Option C ('Proton acceptor') is generic terminology not associated with subtilisin catalysis. A model recognizing the GTSMA motif and knowing subtilisin mechanism can confidently select A and eliminate the others.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GTSMA motif is a universally recognized family signature for subtilisin-type proteases, and 'charge relay system' is the standard mechanistic descriptor for the subtilisin catalytic triad. This combination of family recognition (from the sequence) and mechanistic knowledge (from other subtilisin proteins) meaningfully and uniquely identifies option A among the four choices. No target-specific annotation lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A identifies a position that is an annotated active site with the correct functional description. Positions 180, 12, and 365 are not active sites, and their associated functions (beta-ketoacyl synthase, proton acceptor) are inconsistent with a subtilisin-type protease. The distractors are clearly eliminable by family recognition.


### Important caveats

- The active site annotation at position 286 is based on PROSITE-ProRule (ECO:0000255), a computational/prorule inference, not direct experimental mutagenesis of this specific protein. However, it is consistent with the well-established subtilisin mechanism and the sequence context (IDSG motif).
- The question lists only one position per option, whereas the full catalytic center comprises three residues (286, 342, 519). The question format asks which single option correctly identifies an active site residue with its function, which is unambiguous.
- The protein identity (Plasmodium berghei SUB1) was not provided to the model; identification relies solely on sequence motif recognition, which is sufficient given the distinctive GTSMA motif.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'GTSMA' motif (positions 517-521: G-T-S-M-A), which is the hallmark signature of subtilisin-type serine proteases' catalytic serine. This is an extremely well-known family-level sequence feature. Subtilisins catalyze via an Asp-His-Ser 'charge relay system' — this is the standard mechanistic terminology for this enzyme family. Option A ('Position 286, Charge relay system') matches both the family identification (subtilisin) and the correct mechanistic description. Options B and D ('beta-ketoacyl synthase') refer to fatty acid synthase, a completely different enzyme class with a Cys-His-His active site and no sequence similarity to subtilisins. Option C ('Proton acceptor') is generic terminology not associated with subtilisin catalysis. A model recognizing the GTSMA motif and knowing subtilisin mechanism can confidently select A and eliminate the others.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GTSMA motif is a universally recognized family signature for subtilisin-type proteases, and 'charge relay system' is the standard mechanistic descriptor for the subtilisin catalytic triad. This combination of family recognition (from the sequence) and mechanistic knowledge (from other subtilisin proteins) meaningfully and uniquely identifies option A among the four choices. No target-specific annotation lookup is required."
  },
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A509AM03 (Subtilisin-like protease 1, PbSUB1) explicitly annotates position 286 as an Active site with description 'Charge relay system' (evidence C5/H6). The protein is EC 3.4.21.62, a subtilisin-type serine protease whose catalytic triad (Asp286-His342-Ser519) constitutes the charge relay system. The annotation is based on PROSITE-ProRule (ECO:0000255, computational/prorule evidence), which is consistent with the well-established subtilisin mechanism. The sequence confirms: position 286 is Asp (in IDSG context), 342 is His (in NHGSHVSG context), and 519 is Ser (in GTSMA context), matching the canonical subtilisin triad."
  },
  "important_caveats": [
    "The active site annotation at position 286 is based on PROSITE-ProRule (ECO:0000255), a computational/prorule inference, not direct experimental mutagenesis of this specific protein. However, it is consistent with the well-established subtilisin mechanism and the sequence context (IDSG motif).",
    "The question lists only one position per option, whereas the full catalytic center comprises three residues (286, 342, 519). The question format asks which single option correctly identifies an active site residue with its function, which is unambiguous.",
    "The protein identity (Plasmodium berghei SUB1) was not provided to the model; identification relies solely on sequence motif recognition, which is sufficient given the distinctive GTSMA motif."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A identifies a position that is an annotated active site with the correct functional description. Positions 180, 12, and 365 are not active sites, and their associated functions (beta-ketoacyl synthase, proton acceptor) are inconsistent with a subtilisin-type protease. The distractors are clearly eliminable by family recognition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A509AM03 (Subtilisin-like protease 1, PbSUB1) explicitly annotates position 286 as an Active site with description 'Charge relay system' (evidence C5/H6). The protein is EC 3.4.21.62, a subtilisin-type serine protease whose catalytic triad (Asp286-His342-Ser519) constitutes the charge relay system. The annotation is based on PROSITE-ProRule (ECO:0000255, computational/prorule evidence), which is consistent with the well-established subtilisin mechanism. The sequence confirms: position 286 is Asp (in IDSG context), 342 is His (in NHGSHVSG context), and 519 is Ser (in GTSMA context), matching the canonical subtilisin triad.",
    "evidence_ids": ["C5", "H6", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'GTSMA' motif (positions 517-521: G-T-S-M-A), which is the hallmark signature of subtilisin-type serine proteases' catalytic serine. This is an extremely well-known family-level sequence feature. Subtilisins catalyze via an Asp-His-Ser 'charge relay system' — this is the standard mechanistic terminology for this enzyme family. Option A ('Position 286, Charge relay system') matches both the family identification (subtilisin) and the correct mechanistic description. Options B and D ('beta-ketoacyl synthase') refer to fatty acid synthase, a completely different enzyme class with a Cys-His-His active site and no sequence similarity to subtilisins. Option C ('Proton acceptor') is generic terminology not associated with subtilisin catalysis. A model recognizing the GTSMA motif and knowing subtilisin mechanism can confidently select A and eliminate the others.",
    "missing_item_specific_fact": "",
    "reason": "The GTSMA motif is a universally recognized family signature for subtilisin-type proteases, and 'charge relay system' is the standard mechanistic descriptor for the subtilisin catalytic triad. This combination of family recognition (from the sequence) and mechanistic knowledge (from other subtilisin proteins) meaningfully and uniquely identifies option A among the four choices. No target-specific annotation lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A identifies a position that is an annotated active site with the correct functional description. Positions 180, 12, and 365 are not active sites, and their associated functions (beta-ketoacyl synthase, proton acceptor) are inconsistent with a subtilisin-type protease. The distractors are clearly eliminable by family recognition."
  },
  "important_caveats": [
    "The active site annotation at position 286 is based on PROSITE-ProRule (ECO:0000255), a computational/prorule inference, not direct experimental mutagenesis of this specific protein. However, it is consistent with the well-established subtilisin mechanism and the sequence context (IDSG motif).",
    "The question lists only one position per option, whereas the full catalytic center comprises three residues (286, 342, 519). The question format asks which single option correctly identifies an active site residue with its function, which is unambiguous.",
    "The protein identity (Plasmodium berghei SUB1) was not provided to the model; identification relies solely on sequence motif recognition, which is sufficient given the distinctive GTSMA motif."
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
  "benchmark_sequence_length": 599,
  "benchmark_sequence_sha256": "c5873da74b946ad1a9fd22f718bcaa153629124ee65112b496cac3092aaf6e26",
  "current_entry_audit": {
    "entryVersion": 31,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-09-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 599,
  "current_source_sequence_sha256": "c5873da74b946ad1a9fd22f718bcaa153629124ee65112b496cac3092aaf6e26",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A509AM03",
  "selected_historical_entry_version": 30,
  "selected_historical_record_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "selected_historical_source_sequence_length": 599,
  "selected_historical_source_sequence_sha256": "c5873da74b946ad1a9fd22f718bcaa153629124ee65112b496cac3092aaf6e26",
  "selected_historical_version": {
    "accession": "A0A509AM03",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "SUB1_PLABA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A509AM03\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":31,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-09-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000074855\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Vinckeia\"],\"scientificName\":\"Plasmodium berghei (strain Anka)\",\"taxonId\":5823}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24089525\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24348254\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30941868\",\"source\":\"PubMed\"}],\"value\":\"PbSUB1\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"}],\"value\":\"3.4.21.62\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24348254\",\"source\":\"PubMed\"}],\"value\":\"Subtilisin-like protease 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01240\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":286},\"start\":{\"modifier\":\"EXACT\",\"value\":286}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01240\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":342},\"start\":{\"modifier\":\"EXACT\",\"value\":342}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01240\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":519},\"start\":{\"modifier\":\"EXACT\",\"value\":519}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":123},\"start\":{\"modifier\":\"EXACT\",\"value\":123}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":126},\"start\":{\"modifier\":\"EXACT\",\"value\":126}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":128},\"start\":{\"modifier\":\"EXACT\",\"value\":128}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"4\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":183},\"start\":{\"modifier\":\"EXACT\",\"value\":183}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":295},\"start\":{\"modifier\":\"EXACT\",\"value\":295}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":306},\"start\":{\"modifier\":\"EXACT\",\"value\":306}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":306},\"start\":{\"modifier\":\"EXACT\",\"value\":306}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":314},\"start\":{\"modifier\":\"EXACT\",\"value\":314}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":315},\"start\":{\"modifier\":\"EXACT\",\"value\":315}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":316},\"start\":{\"modifier\":\"EXACT\",\"value\":316}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":318},\"start\":{\"modifier\":\"EXACT\",\"value\":318}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":320},\"start\":{\"modifier\":\"EXACT\",\"value\":320}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"2\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":322},\"start\":{\"modifier\":\"EXACT\",\"value\":322}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"3\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":323},\"start\":{\"modifier\":\"EXACT\",\"value\":323}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":353}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":356},\"start\":{\"modifier\":\"EXACT\",\"value\":356}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/24",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":358},\"start\":{\"modifier\":\"EXACT\",\"value\":358}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/25",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I0V0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29108\",\"label\":\"1\",\"name\":\"Ca(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":360},\"start\":{\"modifier\":\"EXACT\",\"value\":360}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/26",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C27",
  "excerpt": "{\"description\":\"Cleavage\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":196},\"start\":{\"modifier\":\"EXACT\",\"value\":195}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/27",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C28",
  "excerpt": "{\"citation\":{\"authors\":[\"Bouillon A.\",\"Giganti D.\",\"Benedet C.\",\"Gorgette O.\",\"Petres S.\",\"Crublet E.\",\"Girard-Blanc C.\",\"Witkowski B.\",\"Menard D.\",\"Nilges M.\",\"Mercereau-Puijalon O.\",\"Stoven V.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23653352\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m113.456764\"}],\"citationType\":\"journal article\",\"firstPage\":\"18561\",\"id\":\"23653352\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"18573\",\"publicationDate\":\"2013\",\"title\":\"In Silico screening on the three-dimensional model of the Plasmodium vivax SUB1 protease leads to the validation of a novel anti-parasite compound.\",\"volume\":\"288\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"PROTEOLYTIC CLEAVAGE\",\"CLEAVAGE SITE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C29",
  "excerpt": "{\"citation\":{\"authors\":[\"Tawk L.\",\"Lacroix C.\",\"Gueirard P.\",\"Kent R.\",\"Gorgette O.\",\"Thiberge S.\",\"Mercereau-Puijalon O.\",\"Menard R.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24089525\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m113.513234\"}],\"citationType\":\"journal article\",\"firstPage\":\"33336\",\"id\":\"24089525\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"33346\",\"publicationDate\":\"2013\",\"title\":\"A key role for Plasmodium subtilisin-like SUB1 protease in egress of malaria parasites from host hepatocytes.\",\"volume\":\"288\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C30",
  "excerpt": "{\"citation\":{\"authors\":[\"Suarez C.\",\"Volkmann K.\",\"Gomes A.R.\",\"Billker O.\",\"Blackman M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24348254\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1003811\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1003811\",\"id\":\"24348254\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1003811\",\"publicationDate\":\"2013\",\"title\":\"The malarial serine protease SUB1 plays an essential role in parasite liver stage development.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence C31

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)

```json
{
  "evidence_id": "C31",
  "excerpt": "{\"citation\":{\"authors\":[\"Pace T.\",\"Grasso F.\",\"Camarda G.\",\"Suarez C.\",\"Blackman M.J.\",\"Ponzi M.\",\"Olivieri A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30941868\"},{\"database\":\"DOI\",\"id\":\"10.1111/cmi.13028\"}],\"citationType\":\"journal article\",\"firstPage\":\"e13028\",\"id\":\"30941868\",\"journal\":\"Cell. Microbiol.\",\"lastPage\":\"e13028\",\"publicationDate\":\"2019\",\"title\":\"The Plasmodium berghei serine protease PbSUB1 plays an important role in male gamete egress.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:24:47.276162+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM03.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H1",
  "excerpt": "ID   SUB1_PLABA              Reviewed;         599 AA.\nAC   A0A509AM03;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-SEP-2019, sequence version 1.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:24348254};\nDE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352};\nDE   AltName: Full=PbSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:24089525, ECO:0000303|PubMed:24348254, ECO:0000303|PubMed:30941868};\nDE   Flags: Precursor;\nGN   Name=SUB1 {ECO:0000305};\nGN   ORFNames=PBANKA_1107100 {ECO:0000312|EMBL:VUC56494.1};\nOS   Plasmodium berghei (strain Anka).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).\nOX   NCBI_TaxID=5823 {ECO:0000312|Proteomes:UP000074855};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, PROTEOLYTIC CLEAVAGE, AND CLEAVAGE SITE.\nRX   PubMed=23653352; DOI=10.1074/jbc.m113.456764;\nRA   Bouillon A., Giganti D., Benedet C., Gorgette O., Petres S., Crublet E.,\nRA   Girard-Blanc C., Witkowski B., Menard D., Nilges M., Mercereau-Puijalon O.,\nRA   Stoven V., Barale J.C.;\nRT   \"In Silico screening on the three-dimensional model of the Plasmodium vivax\nRT   SUB1 protease leads to the validation of a novel anti-parasite compound.\";\nRL   J. Biol. Chem. 288:18561-18573(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, DEVELOPMENTAL STAGE, AND DISRUPTION PHENOTYPE.\nRX   PubMed=24089525; DOI=10.1074/jbc.m113.513234;\nRA   Tawk L., Lacroix C., Gueirard P., Kent R., Gorgette O., Thiberge S.,\nRA   Mercereau-Puijalon O., Menard R., Barale J.C.;\nRT   \"A key role for Plasmodium subtilisin-like SUB1 protease in egress of\nRT   malaria parasites from host hepatocytes.\";\nRL   J. Biol. Chem. 288:33336-33346(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=24348254; DOI=10.1371/journal.ppat.1003811;\nRA   Suarez C., Volkmann K., Gomes A.R., Billker O., Blackman M.J.;\nRT   \"The malarial serine protease SUB1 plays an essential role in parasite\nRT   liver stage development.\";\nRL   PLoS Pathog. 9:e1003811-e1003811(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H5",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=30941868; DOI=10.1111/cmi.13028;\nRA   Pace T., Grasso F., Camarda G., Suarez C., Blackman M.J., Ponzi M.,\nRA   Olivieri A.;\nRT   \"The Plasmodium berghei serine protease PbSUB1 plays an important role in\nRT   male gamete egress.\";\nRL   Cell. Microbiol. 21:e13028-e13028(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H6",
  "excerpt": "FT   ACT_SITE        286\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01240\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 178-180",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H7",
  "excerpt": "FT   ACT_SITE        342\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01240\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 181-183",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H8",
  "excerpt": "FT   ACT_SITE        519\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01240\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 184-186",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         123\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 187-191",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         126\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 192-196",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         128\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 197-201",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         183\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 202-206",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         251\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 207-211",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         295\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 212-216",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H15",
  "excerpt": "FT   BINDING         306\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 217-221",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H16",
  "excerpt": "FT   BINDING         306\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 222-226",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H17",
  "excerpt": "FT   BINDING         314\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 227-231",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H18",
  "excerpt": "FT   BINDING         315\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 232-236",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H19",
  "excerpt": "FT   BINDING         316\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 237-241",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H20",
  "excerpt": "FT   BINDING         318\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 242-246",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H21",
  "excerpt": "FT   BINDING         320\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 247-251",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H22",
  "excerpt": "FT   BINDING         322\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 252-256",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H23",
  "excerpt": "FT   BINDING         323\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 257-261",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H24",
  "excerpt": "FT   BINDING         353\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 262-266",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H25",
  "excerpt": "FT   BINDING         356\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 267-271",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H26",
  "excerpt": "FT   BINDING         358\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 272-276",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H27",
  "excerpt": "FT   BINDING         360\nFT                   /ligand=\"Ca(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29108\"\nFT                   /ligand_label=\"1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8I0V0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 277-281",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H28",
  "excerpt": "FT   SITE            195..196\nFT                   /note=\"Cleavage\"\nFT                   /evidence=\"ECO:0000269|PubMed:23653352\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.257005+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 282-284",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02",
  "url": "https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 29. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
