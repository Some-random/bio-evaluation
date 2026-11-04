# pathway_0185

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0185.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDKISIIPIVGVALSLAIILQLGRTYWRLRHIPGPFPACITNFQRVGWVKTKRAHLILQDMHKKYGEVVRIGPNMVSFSNPEVIPTVYPARSGFPKGDFYVTLRPYTRGGGALHAVFNTTEEDLHKQIKSPIAPMFTPANTPSFEGLVDEVLTCIHEKLDENFIANSEIFNLGQWLQYFAFDVMGTMTFSKRYGFLDTGKDVGRMLGTIVDFMRDAAPMTQIPWLDWALRKNRIGDSIQRLFGKTASLGILGFVGKAIKERQELLSKGDFKVSDEKSGRKDFLTRFIELQQNDPKIPPWAPTAWTFSNVIAGSDSVGSLMRTTMFNLLVYPHTLEKLHDELRSAGVSRPYPKWSEIRNLLYLDACVQEGARMHPPFALPFERVVPAGGITILGYYLPGGTVVGGSPYVVNRHRETFGRDAEFWRPERWLESDEGHKRKLEQGVLTFGAGRRVCLGKHVGILEIKKLISFLVLNYDIRVVNPEKFELENSWFFFQRGLYATIRKRPDAVAVKNQQV

[Multiple Choices]
A. terpenoid biosynthesis. .
B. NAD(+) from nicotinamide D-ribonucleotide: step 1/1. .
C. glycosylphosphatidylinositol-anchor biosynthesis. .
D. Secondary metabolite biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates this protein to secondary metabolite biosynthesis and terpenoid biosynthesis, with experimental-evidence code ECO:0000269. This supports the keyed choice D, although it also supports choice A.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific pathway role or substrate of this P450 in its biosynthetic cluster, needed to choose between terpenoid biosynthesis (A) and the broader secondary-metabolite category (D).


**Reason**

> The sequence is consistent with a membrane-associated cytochrome P450, and that family-level knowledge makes B and C poor fits. But generic P450 features do not distinguish A from D: both are plausible pathway assignments, and the exact protein's role is needed to select between them.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> The source annotation lists both terpenoid biosynthesis and secondary metabolite biosynthesis, and the choices present them separately without clarifying whether the more specific pathway or broader category is preferred.


### Important caveats

- The reviewer-only annotation supports the key but was not part of the original input.
- The annotation supports both A and D; it does not establish that D is uniquely the primary pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific pathway role or substrate of this P450 in its biosynthetic cluster, needed to choose between terpenoid biosynthesis (A) and the broader secondary-metabolite category (D).",
    "reason": "The sequence is consistent with a membrane-associated cytochrome P450, and that family-level knowledge makes B and C poor fits. But generic P450 features do not distinguish A from D: both are plausible pathway assignments, and the exact protein's role is needed to select between them."
  },
  "case_id": "pathway_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to secondary metabolite biosynthesis and terpenoid biosynthesis, with experimental-evidence code ECO:0000269. This supports the keyed choice D, although it also supports choice A."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original input.",
    "The annotation supports both A and D; it does not establish that D is uniquely the primary pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "The source annotation lists both terpenoid biosynthesis and secondary metabolite biosynthesis, and the choices present them separately without clarifying whether the more specific pathway or broader category is preferred."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein to secondary metabolite biosynthesis and terpenoid biosynthesis, with experimental-evidence code ECO:0000269. This supports the keyed choice D, although it also supports choice A.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific pathway role or substrate of this P450 in its biosynthetic cluster, needed to choose between terpenoid biosynthesis (A) and the broader secondary-metabolite category (D).",
    "reason": "The sequence is consistent with a membrane-associated cytochrome P450, and that family-level knowledge makes B and C poor fits. But generic P450 features do not distinguish A from D: both are plausible pathway assignments, and the exact protein's role is needed to select between them."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "The source annotation lists both terpenoid biosynthesis and secondary metabolite biosynthesis, and the choices present them separately without clarifying whether the more specific pathway or broader category is preferred."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original input.",
    "The annotation supports both A and D; it does not establish that D is uniquely the primary pathway."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) states the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis,' supported by experimental evidence (ECO:0000269|PubMed:38404388). The expected answer D ('Secondary metabolite biosynthesis') matches the first listed pathway category. However, option A ('terpenoid biosynthesis') is equally supported by the same annotation as the second listed category.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif (FGAGRRVCLGKHVG at ~residue 340), identifying it as a P450 monooxygenase. From transferable knowledge: (1) P450s are not involved in NAD+ biosynthesis or GPI-anchor biosynthesis, eliminating B and C. (2) In fungi, P450s are overwhelmingly associated with secondary metabolism (a well-established empirical pattern across fungal genomes). (3) Without specific terpene-cyclase-like features or cluster context visible in the sequence, the broader category 'secondary metabolite biosynthesis' (D) is the more defensible general prediction than the narrower 'terpenoid biosynthesis' (A), since terpenoid biosynthesis is a subset of secondary metabolite biosynthesis in fungi. A model reasoning from P450 identity + fungal secondary-metabolism prevalence would land on D as the safest and most inclusive correct answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the P450 from the heme-binding motif, eliminate B and C based on pathway–enzyme-type incompatibility, and prefer D over A using the general principle that fungal P450s are predominantly secondary-metabolism enzymes and that the broader category is the safer prediction when sub-pathway specificity is not evident from sequence alone. This constitutes a concrete, transferable inference chain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> The UniProt annotation lists both 'Secondary metabolite biosynthesis' and 'terpenoid biosynthesis' as pathway assignments for this protein (separated by a semicolon, indicating both apply). Option D matches the first category and option A matches the second. Since terpenoid biosynthesis in fungi is a subcategory of secondary metabolite biosynthesis, both are technically correct pathway assignments. The question asks for 'the most relevant pathway,' which could reasonably be answered as either the broader (D) or more specific (A) category.


### Important caveats

- The UniProt pathway annotation lists both 'Secondary metabolite biosynthesis' and 'terpenoid biosynthesis' as applicable, making both A and D factually correct pathway assignments.
- The organism (Annulohypoxylon moriforme, a filamentous fungus) is not stated in the original user input; fungal context must be inferred from sequence features or general P450 knowledge.
- The distinction between A and D rests on whether the question seeks the broadest applicable pathway category or the most specific one; the annotation supports both.
- The protein is a P450 involved in 11'-O-desmethylfendlerol biosynthesis (a polyketide-terpenoid hybrid), so it participates in terpenoid biosynthesis as part of a broader secondary metabolite cluster.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FGAGRRVCLGKHVG at ~residue 340), identifying it as a P450 monooxygenase. From transferable knowledge: (1) P450s are not involved in NAD+ biosynthesis or GPI-anchor biosynthesis, eliminating B and C. (2) In fungi, P450s are overwhelmingly associated with secondary metabolism (a well-established empirical pattern across fungal genomes). (3) Without specific terpene-cyclase-like features or cluster context visible in the sequence, the broader category 'secondary metabolite biosynthesis' (D) is the more defensible general prediction than the narrower 'terpenoid biosynthesis' (A), since terpenoid biosynthesis is a subset of secondary metabolite biosynthesis in fungi. A model reasoning from P450 identity + fungal secondary-metabolism prevalence would land on D as the safest and most inclusive correct answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 from the heme-binding motif, eliminate B and C based on pathway–enzyme-type incompatibility, and prefer D over A using the general principle that fungal P450s are predominantly secondary-metabolism enzymes and that the broader category is the safer prediction when sub-pathway specificity is not evident from sequence alone. This constitutes a concrete, transferable inference chain."
  },
  "case_id": "pathway_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) states the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis,' supported by experimental evidence (ECO:0000269|PubMed:38404388). The expected answer D ('Secondary metabolite biosynthesis') matches the first listed pathway category. However, option A ('terpenoid biosynthesis') is equally supported by the same annotation as the second listed category."
  },
  "important_caveats": [
    "The UniProt pathway annotation lists both 'Secondary metabolite biosynthesis' and 'terpenoid biosynthesis' as applicable, making both A and D factually correct pathway assignments.",
    "The organism (Annulohypoxylon moriforme, a filamentous fungus) is not stated in the original user input; fungal context must be inferred from sequence features or general P450 knowledge.",
    "The distinction between A and D rests on whether the question seeks the broadest applicable pathway category or the most specific one; the annotation supports both.",
    "The protein is a P450 involved in 11'-O-desmethylfendlerol biosynthesis (a polyketide-terpenoid hybrid), so it participates in terpenoid biosynthesis as part of a broader secondary metabolite cluster."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "The UniProt annotation lists both 'Secondary metabolite biosynthesis' and 'terpenoid biosynthesis' as pathway assignments for this protein (separated by a semicolon, indicating both apply). Option D matches the first category and option A matches the second. Since terpenoid biosynthesis in fungi is a subcategory of secondary metabolite biosynthesis, both are technically correct pathway assignments. The question asks for 'the most relevant pathway,' which could reasonably be answered as either the broader (D) or more specific (A) category."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) states the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis,' supported by experimental evidence (ECO:0000269|PubMed:38404388). The expected answer D ('Secondary metabolite biosynthesis') matches the first listed pathway category. However, option A ('terpenoid biosynthesis') is equally supported by the same annotation as the second listed category.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FGAGRRVCLGKHVG at ~residue 340), identifying it as a P450 monooxygenase. From transferable knowledge: (1) P450s are not involved in NAD+ biosynthesis or GPI-anchor biosynthesis, eliminating B and C. (2) In fungi, P450s are overwhelmingly associated with secondary metabolism (a well-established empirical pattern across fungal genomes). (3) Without specific terpene-cyclase-like features or cluster context visible in the sequence, the broader category 'secondary metabolite biosynthesis' (D) is the more defensible general prediction than the narrower 'terpenoid biosynthesis' (A), since terpenoid biosynthesis is a subset of secondary metabolite biosynthesis in fungi. A model reasoning from P450 identity + fungal secondary-metabolism prevalence would land on D as the safest and most inclusive correct answer.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 from the heme-binding motif, eliminate B and C based on pathway–enzyme-type incompatibility, and prefer D over A using the general principle that fungal P450s are predominantly secondary-metabolism enzymes and that the broader category is the safer prediction when sub-pathway specificity is not evident from sequence alone. This constitutes a concrete, transferable inference chain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "The UniProt annotation lists both 'Secondary metabolite biosynthesis' and 'terpenoid biosynthesis' as pathway assignments for this protein (separated by a semicolon, indicating both apply). Option D matches the first category and option A matches the second. Since terpenoid biosynthesis in fungi is a subcategory of secondary metabolite biosynthesis, both are technically correct pathway assignments. The question asks for 'the most relevant pathway,' which could reasonably be answered as either the broader (D) or more specific (A) category."
  },
  "important_caveats": [
    "The UniProt pathway annotation lists both 'Secondary metabolite biosynthesis' and 'terpenoid biosynthesis' as applicable, making both A and D factually correct pathway assignments.",
    "The organism (Annulohypoxylon moriforme, a filamentous fungus) is not stated in the original user input; fungal context must be inferred from sequence features or general P450 knowledge.",
    "The distinction between A and D rests on whether the question seeks the broadest applicable pathway category or the most specific one; the annotation supports both.",
    "The protein is a P450 involved in 11'-O-desmethylfendlerol biosynthesis (a polyketide-terpenoid hybrid), so it participates in terpenoid biosynthesis as part of a broader secondary metabolite cluster."
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
  "benchmark_sequence_length": 515,
  "benchmark_sequence_sha256": "b148dd6535a2478e2a065541559f956e45ac653fa2dceff0ebdbeae21e9d5591",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 515,
  "current_source_sequence_sha256": "b148dd6535a2478e2a065541559f956e45ac653fa2dceff0ebdbeae21e9d5591",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P9WEG0",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "selected_historical_source_sequence_length": 515,
  "selected_historical_source_sequence_sha256": "b148dd6535a2478e2a065541559f956e45ac653fa2dceff0ebdbeae21e9d5591",
  "selected_historical_version": {
    "accession": "P9WEG0",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFMA_ANNMO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEG0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase mfmA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:13.096452+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   MFMA_ANNMO              Reviewed;         515 AA.\nAC   P9WEG0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Cytochrome P450 monooxygenase mfmA {ECO:0000303|PubMed:38404388};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein A {ECO:0000303|PubMed:38404388};\nGN   Name=mfmA {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_29954;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:18.350529+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "url": "https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:18.350529+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "url": "https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:38404388}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:18.350529+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2",
  "url": "https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 185. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
