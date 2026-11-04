# catalytic_activity_0148

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0148.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — 4&#x27;-phosphooxetanocin A + H2O = oxetanocin A + phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSLLDIIYQLRQVPRWDGSFQFEKEDVSQHSFSVIAISHILCELKETLEGKKINKEKLLLYALYHDVTEVVSTHIISPVKKNSILKDPFNAFREQIKNSLFDNLPITLSDTLSTILNNNDLEIQEIVEHADHVDAYCKSCIEVHRGNKDFISIQRSLGDKLDNLTKEYPYLKEFQNLFLKDFPLENKNYRYLN

[Multiple Choices]
A. O-phospho-L-serine + sulfite + H(+) = L-cysteate + phosphate
B. 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O
C. O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate
D. 4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1374)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein EC 3.1.3.112 and the reaction in choice D, with experimental evidence codes citing two papers. This supports the keyed reaction, while the annotation is not itself a direct review of those experiments.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short sequence contains an HD-like histidine/aspartate motif pattern consistent with a metal-dependent phosphohydrolase. Among these choices, D is the direct phosphatase reaction; A and C are biosynthetic reactions that release phosphate as part of different transformations, and B is a large polyketide-synthase reaction incompatible with this small protein. This provides a meaningful family-level distinction without requiring prior knowledge of this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of an HD-domain phosphohydrolase and comparison with the offered reaction types meaningfully favors D. The precise oxetanocin substrate specificity is not established by that motif alone, so the inference is probabilistic rather than a full independent demonstration of the exact reaction.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and C also produce phosphate, their overall transformations are not simple phosphatase reactions and are not equally supported by the sequence's phosphohydrolase-like features."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and was not available as input to the evaluated model.",
    "The sequence match establishes applicability of the cited annotation, but the precise substrate preference would be harder to infer from sequence motifs alone."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry O24769 (OXSA_PRIMG) explicitly annotates the catalytic activity as '4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate' (EC 3.1.3.112), supported by experimental evidence (ECO:0000269) from two independent publications (PMID:27849620, PMID:28346939) including X-ray crystallography with substrate complexes. The sequence matches exactly (194 AA, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear HD-domain motif ('EVEHADHVDAY'), which is a well-known family marker for phosphohydrolases found across diverse organisms (e.g., HDGAP, various bacterial phosphohydrolases). Among the four choices, only D represents a phosphatase/hydrolysis reaction (removal of a phosphate group via water). Choices A and C are trans-sulfuration reactions requiring PLP-dependent enzymes (cysteine synthase/cystathionine gamma-synthase families), and B is a massive polyketide synthase reaction requiring a multi-domain megasynthase (far exceeding 194 AA). The small protein size (~194 AA) further excludes B. Recognizing the HD motif as a phosphohydrolase family marker and noting that D is the sole phosphatase reaction among the options provides a concrete family-level inference that distinguishes D from A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HD domain is a transferable, well-characterized family feature indicating phosphohydrolase activity. The critical discrimination does not require knowing the exact substrate name '4'-phosphooxetanocin A' in advance; it requires recognizing that D is the only phosphatase-type reaction among the choices, which follows from family-level knowledge of HD domains combined with elimination of non-phosphatase reaction types (trans-sulfuration for A/C, polyketide synthesis for B). The small size also eliminates B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D is a phosphatase reaction; A and C are trans-sulfuration reactions (PLP-dependent), and B is a polyketide synthase reaction. The HD motif and small size uniquely point to a phosphatase, making D the only defensible choice.


### Important caveats

- The specific substrate '4'-phosphooxetanocin A' is an unusual natural product; a model would select D based on recognizing it as the phosphatase option rather than independently predicting this exact substrate from sequence.
- The HD domain is shared among many phosphohydrolases with diverse substrates; the family-level inference identifies the reaction TYPE (phosphatase) but not the specific substrate. This is sufficient here because only one option is a phosphatase reaction.
- The UniProt entry was first publicly released in 2025-02-05, so this specific annotation may not have been in databases at the time of benchmark construction, though the underlying papers (2016, 2017) predate it.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear HD-domain motif ('EVEHADHVDAY'), which is a well-known family marker for phosphohydrolases found across diverse organisms (e.g., HDGAP, various bacterial phosphohydrolases). Among the four choices, only D represents a phosphatase/hydrolysis reaction (removal of a phosphate group via water). Choices A and C are trans-sulfuration reactions requiring PLP-dependent enzymes (cysteine synthase/cystathionine gamma-synthase families), and B is a massive polyketide synthase reaction requiring a multi-domain megasynthase (far exceeding 194 AA). The small protein size (~194 AA) further excludes B. Recognizing the HD motif as a phosphohydrolase family marker and noting that D is the sole phosphatase reaction among the options provides a concrete family-level inference that distinguishes D from A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HD domain is a transferable, well-characterized family feature indicating phosphohydrolase activity. The critical discrimination does not require knowing the exact substrate name '4'-phosphooxetanocin A' in advance; it requires recognizing that D is the only phosphatase-type reaction among the choices, which follows from family-level knowledge of HD domains combined with elimination of non-phosphatase reaction types (trans-sulfuration for A/C, polyketide synthesis for B). The small size also eliminates B."
  },
  "case_id": "catalytic_activity_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry O24769 (OXSA_PRIMG) explicitly annotates the catalytic activity as '4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate' (EC 3.1.3.112), supported by experimental evidence (ECO:0000269) from two independent publications (PMID:27849620, PMID:28346939) including X-ray crystallography with substrate complexes. The sequence matches exactly (194 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The specific substrate '4'-phosphooxetanocin A' is an unusual natural product; a model would select D based on recognizing it as the phosphatase option rather than independently predicting this exact substrate from sequence.",
    "The HD domain is shared among many phosphohydrolases with diverse substrates; the family-level inference identifies the reaction TYPE (phosphatase) but not the specific substrate. This is sufficient here because only one option is a phosphatase reaction.",
    "The UniProt entry was first publicly released in 2025-02-05, so this specific annotation may not have been in databases at the time of benchmark construction, though the underlying papers (2016, 2017) predate it."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D is a phosphatase reaction; A and C are trans-sulfuration reactions (PLP-dependent), and B is a polyketide synthase reaction. The HD motif and small size uniquely point to a phosphatase, making D the only defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry O24769 (OXSA_PRIMG) explicitly annotates the catalytic activity as '4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate' (EC 3.1.3.112), supported by experimental evidence (ECO:0000269) from two independent publications (PMID:27849620, PMID:28346939) including X-ray crystallography with substrate complexes. The sequence matches exactly (194 AA, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear HD-domain motif ('EVEHADHVDAY'), which is a well-known family marker for phosphohydrolases found across diverse organisms (e.g., HDGAP, various bacterial phosphohydrolases). Among the four choices, only D represents a phosphatase/hydrolysis reaction (removal of a phosphate group via water). Choices A and C are trans-sulfuration reactions requiring PLP-dependent enzymes (cysteine synthase/cystathionine gamma-synthase families), and B is a massive polyketide synthase reaction requiring a multi-domain megasynthase (far exceeding 194 AA). The small protein size (~194 AA) further excludes B. Recognizing the HD motif as a phosphohydrolase family marker and noting that D is the sole phosphatase reaction among the options provides a concrete family-level inference that distinguishes D from A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "The HD domain is a transferable, well-characterized family feature indicating phosphohydrolase activity. The critical discrimination does not require knowing the exact substrate name '4'-phosphooxetanocin A' in advance; it requires recognizing that D is the only phosphatase-type reaction among the choices, which follows from family-level knowledge of HD domains combined with elimination of non-phosphatase reaction types (trans-sulfuration for A/C, polyketide synthesis for B). The small size also eliminates B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D is a phosphatase reaction; A and C are trans-sulfuration reactions (PLP-dependent), and B is a polyketide synthase reaction. The HD motif and small size uniquely point to a phosphatase, making D the only defensible choice."
  },
  "important_caveats": [
    "The specific substrate '4'-phosphooxetanocin A' is an unusual natural product; a model would select D based on recognizing it as the phosphatase option rather than independently predicting this exact substrate from sequence.",
    "The HD domain is shared among many phosphohydrolases with diverse substrates; the family-level inference identifies the reaction TYPE (phosphatase) but not the specific substrate. This is sufficient here because only one option is a phosphatase reaction.",
    "The UniProt entry was first publicly released in 2025-02-05, so this specific annotation may not have been in databases at the time of benchmark construction, though the underlying papers (2016, 2017) predate it."
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
  "benchmark_sequence_length": 194,
  "benchmark_sequence_sha256": "cc417e15ac0354c49fef7a10ef2eaa3595a3619ba1429df8c3467cd7ce1b7a72",
  "current_entry_audit": {
    "entryVersion": 77,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-01-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 194,
  "current_source_sequence_sha256": "cc417e15ac0354c49fef7a10ef2eaa3595a3619ba1429df8c3467cd7ce1b7a72",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 75,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O24769",
  "selected_historical_entry_version": 75,
  "selected_historical_record_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "selected_historical_source_sequence_length": 194,
  "selected_historical_source_sequence_sha256": "cc417e15ac0354c49fef7a10ef2eaa3595a3619ba1429df8c3467cd7ce1b7a72",
  "selected_historical_version": {
    "accession": "O24769",
    "database": "Swiss-Prot",
    "entryVersion": 75,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OXSA_PRIMG",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O24769\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":77,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-01-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacillus megaterium\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Priestia\"],\"scientificName\":\"Priestia megaterium\",\"taxonId\":1404}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"value\":\"HD-domain phosphohydrolase OxsA\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27849620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"value\":\"3.1.3.112\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"4'-phosphooxetanocin A phosphatase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27849620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81368\"}}],\"reaction\":{\"ecNumber\":\"3.1.3.112\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27849620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"name\":\"4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81367\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:85720\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:86012\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bridwell-Rabb J.\",\"Zhong A.\",\"Sun H.G.\",\"Drennan C.L.\",\"Liu H.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28346939\"},{\"database\":\"DOI\",\"id\":\"10.1038/nature21689\"}],\"citationType\":\"journal article\",\"firstPage\":\"322\",\"id\":\"28346939\",\"journal\":\"Nature\",\"lastPage\":\"326\",\"publicationDate\":\"2017\",\"title\":\"A B12-dependent radical SAM enzyme involved in oxetanocin A biosynthesis.\",\"volume\":\"544\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24769.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Bridwell-Rabb J.\",\"Kang G.\",\"Zhong A.\",\"Liu H.W.\",\"Drennan C.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27849620\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1613610113\"}],\"citationType\":\"journal article\",\"firstPage\":\"13750\",\"id\":\"27849620\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"13755\",\"publicationDate\":\"2016\",\"title\":\"An HD domain phosphohydrolase active site tailored for oxetanocin-A biosynthesis.\",\"volume\":\"113\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TK6\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TK7\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TK8\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TK9\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5TKA\",\"source\":\"PDB\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM; OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND OXETANOCIN A TRIPHOSPHATE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DOMAIN\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:10.548137+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c63e689d95c3766e652d2d5563f236adaca6c85d877b17df78572f9e47ef24b",
  "url": "https://rest.uniprot.org/uniprotkb/O24769.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H1",
  "excerpt": "ID   OXSA_PRIMG              Reviewed;         194 AA.\nAC   O24769;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JAN-1998, sequence version 1.\nDT   18-JUN-2025, entry version 75.\nDE   RecName: Full=4'-phosphooxetanocin A phosphatase {ECO:0000305};\nDE            EC=3.1.3.112 {ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};\nDE   AltName: Full=HD-domain phosphohydrolase OxsA {ECO:0000303|PubMed:28346939};\nGN   Name=oxsA {ECO:0000312|EMBL:BAA21630.1};\nOS   Priestia megaterium (Bacillus megaterium).\nOG   Plasmid pOXT1 {ECO:0000303|PubMed:10227144}.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Priestia.\nOX   NCBI_TaxID=1404;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4'-phosphooxetanocin A phosphatase {ECO:0000305};\nDE            EC=3.1.3.112 {ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};\nDE   AltName: Full=HD-domain phosphohydrolase OxsA {ECO:0000303|PubMed:28346939};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=NK84-0128; PLASMID=pOXT1;\nRX   PubMed=10227144; DOI=10.1271/bbb.63.563;\nRA   Morita M., Tomita K., Ishizawa M., Takagi K., Kawamura F., Takahashi H.,\nRA   Morino T.;\nRT   \"Cloning of oxetanocin A biosynthetic and resistance genes that reside on a\nRT   plasmid of Bacillus megaterium strain NK84-0128.\";\nRL   Biosci. Biotechnol. Biochem. 63:563-566(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=28346939; DOI=10.1038/nature21689;\nRA   Bridwell-Rabb J., Zhong A., Sun H.G., Drennan C.L., Liu H.W.;\nRT   \"A B12-dependent radical SAM enzyme involved in oxetanocin A\nRT   biosynthesis.\";\nRL   Nature 544:322-326(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H5",
  "excerpt": "RN   [3] {ECO:0007744|PDB:5TK6, ECO:0007744|PDB:5TK7, ECO:0007744|PDB:5TK8, ECO:0007744|PDB:5TK9, ECO:0007744|PDB:5TKA}\nRP   X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEXES WITH MAGNESIUM;\nRP   OXETANOCIN A; OXETANOCIN A MONOPHOSPHATE; OXETANOCIN A DIPHOSPHATE AND\nRP   OXETANOCIN A TRIPHOSPHATE, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND DOMAIN.\nRX   PubMed=27849620; DOI=10.1073/pnas.1613610113;\nRA   Bridwell-Rabb J., Kang G., Zhong A., Liu H.W., Drennan C.L.;\nRT   \"An HD domain phosphohydrolase active site tailored for oxetanocin-A\nRT   biosynthesis.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 113:13750-13755(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24769?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4'-phosphooxetanocin A + H2O = oxetanocin A + phosphate;\nCC         Xref=Rhea:RHEA:81367, ChEBI:CHEBI:15377, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:85720, ChEBI:CHEBI:86012; EC=3.1.3.112;\nCC         Evidence={ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81368;\nCC         Evidence={ECO:0000269|PubMed:27849620, ECO:0000269|PubMed:28346939};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:21.063065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bab6b179917835711477092cc4cbfcd87e9b1a12b22b046feb1fb9be2c17050d",
  "url": "https://rest.uniprot.org/unisave/O24769?format=txt&versions=75"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 148. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
