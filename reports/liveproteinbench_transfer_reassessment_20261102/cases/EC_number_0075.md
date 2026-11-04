# EC_number_0075

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0075.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.5.1.76

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKIDESLNVHSSLLQLIGNTPLLELHKITKGLKGRYFAKLEAFNVGHSAKDRVAKYIVEDAERKGLLKPGSTIVETSSGNTGYSLAMISALRGYRCIIAISDKSSHDKVEMLQALGAEVHLCPANVAPDDPRSYYEVAKRIHNETPNSIYVNQYFNPLNPESHYQTGREIWEQTQGEITHVVVCSGTGGTISGIAHYLKEQNPRVQVLGVDAYGSAIKKYHETREFDPAEVYPYKIEGIGKNLIPTATDFDVIDEFIKVTDKDAALMARKLARTEGLFMGYTSGAAIQAVKQYAEAGKFDENSIVVVLFADHGSRYMNKIYSDDWMKKQGFID

[Multiple Choices]
A. 2.5.1.160
B. 5.3.99.13
C. 2.7.11.1
D. 2.5.1.76
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

> The sequence matches the UniProt entry annotated as EC 2.5.1.76, and that entry reports the cysteate-forming reaction with ECO:0000269 evidence linked to a publication. This supports the key, though the cited experiment was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 333-residue sequence is consistent with a soluble amino-acid sulfur-substitution enzyme: its length and conserved-looking glycine-rich region and lysine-containing active-site pattern are compatible with a PLP-dependent cysteine-synthase-like family. Transferable knowledge of that family makes cysteate synthase (D) a credible prediction; the kinase and isomerase choices are much less compatible, and A is not the same recognizable family-level candidate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> This is a probabilistic family-based inference from the sequence, not proof of the exact substrate specificity. The sequence provides a meaningful basis for favoring D among these alternatives, although distinguishing closely related sulfur-transfer reactions could require stronger homology or functional evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence-level family inference.


### Important caveats

- The reviewer-only source record matches the sequence, but its exact snapshot at benchmark construction is unknown.
- The source attributes experimental evidence to a publication; that primary study was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 333-residue sequence is consistent with a soluble amino-acid sulfur-substitution enzyme: its length and conserved-looking glycine-rich region and lysine-containing active-site pattern are compatible with a PLP-dependent cysteine-synthase-like family. Transferable knowledge of that family makes cysteate synthase (D) a credible prediction; the kinase and isomerase choices are much less compatible, and A is not the same recognizable family-level candidate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "This is a probabilistic family-based inference from the sequence, not proof of the exact substrate specificity. The sequence provides a meaningful basis for favoring D among these alternatives, although distinguishing closely related sulfur-transfer reactions could require stronger homology or functional evidence."
  },
  "case_id": "EC_number_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as EC 2.5.1.76, and that entry reports the cysteate-forming reaction with ECO:0000269 evidence linked to a publication. This supports the key, though the cited experiment was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only source record matches the sequence, but its exact snapshot at benchmark construction is unknown.",
    "The source attributes experimental evidence to a publication; that primary study was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as EC 2.5.1.76, and that entry reports the cysteate-forming reaction with ECO:0000269 evidence linked to a publication. This supports the key, though the cited experiment was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 333-residue sequence is consistent with a soluble amino-acid sulfur-substitution enzyme: its length and conserved-looking glycine-rich region and lysine-containing active-site pattern are compatible with a PLP-dependent cysteine-synthase-like family. Transferable knowledge of that family makes cysteate synthase (D) a credible prediction; the kinase and isomerase choices are much less compatible, and A is not the same recognizable family-level candidate.",
    "missing_item_specific_fact": "",
    "reason": "This is a probabilistic family-based inference from the sequence, not proof of the exact substrate specificity. The sequence provides a meaningful basis for favoring D among these alternatives, although distinguishing closely related sulfur-transfer reactions could require stronger homology or functional evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level family inference."
  },
  "important_caveats": [
    "The reviewer-only source record matches the sequence, but its exact snapshot at benchmark construction is unknown.",
    "The source attributes experimental evidence to a publication; that primary study was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C7M8J5 is annotated with EC 2.5.1.76 (Cysteate synthase) supported by experimental evidence (ECO:0000269, PubMed:35414181). The sequence in the question matches the UniProt sequence (SHA256 confirmed). The catalytic activity (O-phospho-L-serine + sulfite + H+ = L-cysteate + phosphate) is experimentally validated. The answer D (2.5.1.76) is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains PLP-dependent enzyme motifs (SGNTGY, CSGTGG) and is ~333 aa, consistent with a fold-type I PLP-dependent transferase. This reasonably eliminates C (2.7.11.1, protein kinase — wrong fold, typically much larger, distinct kinase motifs) and B (5.3.99.13, isomerase — wrong mechanism class). However, both remaining options A (2.5.1.160) and D (2.5.1.76) are EC 2.5.1.x transferases that are likely PLP-dependent enzymes in the same sulfonolipid (capnine) biosynthetic pathway. Distinguishing between two closely related EC 2.5.1.x enzymes in the same pathway from sequence alone requires knowing the specific substrate specificity (sulfite condensation for 2.5.1.76 vs. whatever substrate EC 2.5.1.160 uses), which cannot be reliably inferred from general family knowledge or sequence motifs shared between paralogs.


**Missing item-specific fact**

> The specific substrate specificity and active-site architecture that distinguishes this enzyme (capA, cysteate synthase, EC 2.5.1.76) from EC 2.5.1.160 (a related transferase in the same biosynthetic pathway). Both are likely PLP-dependent, similar-sized, and share family-level sequence features, so the specific annotation or experimental characterization of this exact protein is needed to assign the correct 4-digit EC number.


**Reason**

> While general PLP-enzyme recognition eliminates the kinase and isomerase distractors (B and C), the critical distinction between the two EC 2.5.1.x options (A and D) cannot be made from sequence features alone. Both are likely members of the same PLP-dependent transferase family in the capnine biosynthesis pathway. The specific substrate (sulfite for 2.5.1.76) and the exact 4-digit EC assignment require knowledge of this particular protein's experimentally determined function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (2.5.1.160) and D (2.5.1.76) are EC 2.5.1.x transferases likely belonging to the same PLP-dependent enzyme family in the sulfonolipid biosynthesis pathway. Without specific knowledge of which step in the pathway this sequence represents, both are plausible from a family-level perspective. The distinction requires the specific annotation for this protein.


### Important caveats

- The experimental evidence (PubMed:35414181) clearly supports EC 2.5.1.76 for this sequence, but this evidence was not available to the evaluated model.
- EC 2.5.1.160 may be a very recently assigned or obscure EC number, making it a difficult distractor to evaluate from general knowledge.
- The sequence-level features (PLP motifs, size, bacterial origin) are consistent with both remaining options, making the A vs D distinction genuinely sequence-ambiguous without pathway-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains PLP-dependent enzyme motifs (SGNTGY, CSGTGG) and is ~333 aa, consistent with a fold-type I PLP-dependent transferase. This reasonably eliminates C (2.7.11.1, protein kinase — wrong fold, typically much larger, distinct kinase motifs) and B (5.3.99.13, isomerase — wrong mechanism class). However, both remaining options A (2.5.1.160) and D (2.5.1.76) are EC 2.5.1.x transferases that are likely PLP-dependent enzymes in the same sulfonolipid (capnine) biosynthetic pathway. Distinguishing between two closely related EC 2.5.1.x enzymes in the same pathway from sequence alone requires knowing the specific substrate specificity (sulfite condensation for 2.5.1.76 vs. whatever substrate EC 2.5.1.160 uses), which cannot be reliably inferred from general family knowledge or sequence motifs shared between paralogs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity and active-site architecture that distinguishes this enzyme (capA, cysteate synthase, EC 2.5.1.76) from EC 2.5.1.160 (a related transferase in the same biosynthetic pathway). Both are likely PLP-dependent, similar-sized, and share family-level sequence features, so the specific annotation or experimental characterization of this exact protein is needed to assign the correct 4-digit EC number.",
    "reason": "While general PLP-enzyme recognition eliminates the kinase and isomerase distractors (B and C), the critical distinction between the two EC 2.5.1.x options (A and D) cannot be made from sequence features alone. Both are likely members of the same PLP-dependent transferase family in the capnine biosynthesis pathway. The specific substrate (sulfite for 2.5.1.76) and the exact 4-digit EC assignment require knowledge of this particular protein's experimentally determined function."
  },
  "case_id": "EC_number_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C7M8J5 is annotated with EC 2.5.1.76 (Cysteate synthase) supported by experimental evidence (ECO:0000269, PubMed:35414181). The sequence in the question matches the UniProt sequence (SHA256 confirmed). The catalytic activity (O-phospho-L-serine + sulfite + H+ = L-cysteate + phosphate) is experimentally validated. The answer D (2.5.1.76) is well-supported."
  },
  "important_caveats": [
    "The experimental evidence (PubMed:35414181) clearly supports EC 2.5.1.76 for this sequence, but this evidence was not available to the evaluated model.",
    "EC 2.5.1.160 may be a very recently assigned or obscure EC number, making it a difficult distractor to evaluate from general knowledge.",
    "The sequence-level features (PLP motifs, size, bacterial origin) are consistent with both remaining options, making the A vs D distinction genuinely sequence-ambiguous without pathway-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (2.5.1.160) and D (2.5.1.76) are EC 2.5.1.x transferases likely belonging to the same PLP-dependent enzyme family in the sulfonolipid biosynthesis pathway. Without specific knowledge of which step in the pathway this sequence represents, both are plausible from a family-level perspective. The distinction requires the specific annotation for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C7M8J5 is annotated with EC 2.5.1.76 (Cysteate synthase) supported by experimental evidence (ECO:0000269, PubMed:35414181). The sequence in the question matches the UniProt sequence (SHA256 confirmed). The catalytic activity (O-phospho-L-serine + sulfite + H+ = L-cysteate + phosphate) is experimentally validated. The answer D (2.5.1.76) is well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains PLP-dependent enzyme motifs (SGNTGY, CSGTGG) and is ~333 aa, consistent with a fold-type I PLP-dependent transferase. This reasonably eliminates C (2.7.11.1, protein kinase — wrong fold, typically much larger, distinct kinase motifs) and B (5.3.99.13, isomerase — wrong mechanism class). However, both remaining options A (2.5.1.160) and D (2.5.1.76) are EC 2.5.1.x transferases that are likely PLP-dependent enzymes in the same sulfonolipid (capnine) biosynthetic pathway. Distinguishing between two closely related EC 2.5.1.x enzymes in the same pathway from sequence alone requires knowing the specific substrate specificity (sulfite condensation for 2.5.1.76 vs. whatever substrate EC 2.5.1.160 uses), which cannot be reliably inferred from general family knowledge or sequence motifs shared between paralogs.",
    "missing_item_specific_fact": "The specific substrate specificity and active-site architecture that distinguishes this enzyme (capA, cysteate synthase, EC 2.5.1.76) from EC 2.5.1.160 (a related transferase in the same biosynthetic pathway). Both are likely PLP-dependent, similar-sized, and share family-level sequence features, so the specific annotation or experimental characterization of this exact protein is needed to assign the correct 4-digit EC number.",
    "reason": "While general PLP-enzyme recognition eliminates the kinase and isomerase distractors (B and C), the critical distinction between the two EC 2.5.1.x options (A and D) cannot be made from sequence features alone. Both are likely members of the same PLP-dependent transferase family in the capnine biosynthesis pathway. The specific substrate (sulfite for 2.5.1.76) and the exact 4-digit EC assignment require knowledge of this particular protein's experimentally determined function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (2.5.1.160) and D (2.5.1.76) are EC 2.5.1.x transferases likely belonging to the same PLP-dependent enzyme family in the sulfonolipid biosynthesis pathway. Without specific knowledge of which step in the pathway this sequence represents, both are plausible from a family-level perspective. The distinction requires the specific annotation for this protein."
  },
  "important_caveats": [
    "The experimental evidence (PubMed:35414181) clearly supports EC 2.5.1.76 for this sequence, but this evidence was not available to the evaluated model.",
    "EC 2.5.1.160 may be a very recently assigned or obscure EC number, making it a difficult distractor to evaluate from general knowledge.",
    "The sequence-level features (PLP motifs, size, bacterial origin) are consistent with both remaining options, making the A vs D distinction genuinely sequence-ambiguous without pathway-specific knowledge."
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
  "benchmark_sequence_length": 333,
  "benchmark_sequence_sha256": "27d70ef70b1e05efb4edd9f772e95f338a911fbeff53d81928bf3b959e4fbb62",
  "current_entry_audit": {
    "entryVersion": 67,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-10-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 333,
  "current_source_sequence_sha256": "27d70ef70b1e05efb4edd9f772e95f338a911fbeff53d81928bf3b959e4fbb62",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 65,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C7M8J5",
  "selected_historical_entry_version": 65,
  "selected_historical_record_sha256": "b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110",
  "selected_historical_source_sequence_length": 333,
  "selected_historical_source_sequence_sha256": "27d70ef70b1e05efb4edd9f772e95f338a911fbeff53d81928bf3b959e4fbb62",
  "selected_historical_version": {
    "accession": "C7M8J5",
    "database": "Swiss-Prot",
    "entryVersion": 65,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CAPA_CAPOD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C7M8J5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":67,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-10-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacteroides ochraceus\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Bacteroidota\",\"Flavobacteriia\",\"Flavobacteriales\",\"Flavobacteriaceae\",\"Capnocytophaga\"],\"scientificName\":\"Capnocytophaga ochracea (strain ATCC 27872 / DSM 7271 / CCUG 9716 / JCM 12966 / NCTC 12371 / SS31 / VPI 2845)\",\"taxonId\":521097}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.76\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"Cysteate synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:26487\"}}],\"reaction\":{\"ecNumber\":\"2.5.1.76\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"name\":\"O-phospho-L-serine + sulfite + H(+) = L-cysteate + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:26486\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57524\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58090\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu Y.\",\"Wei Y.\",\"Teh T.M.\",\"Liu D.\",\"Zhou Y.\",\"Zhao S.\",\"Ang E.L.\",\"Zhao H.\",\"Zhang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35414181\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.2c00102\"}],\"citationType\":\"journal article\",\"firstPage\":\"2861\",\"id\":\"35414181\",\"journal\":\"Biochemistry\",\"lastPage\":\"2869\",\"publicationDate\":\"2022\",\"title\":\"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.\",\"volume\":\"61\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF LYS-241\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H1",
  "excerpt": "ID   CAPA_CAPOD              Reviewed;         333 AA.\nAC   C7M8J5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-OCT-2009, sequence version 1.\nDT   28-JAN-2026, entry version 65.\nDE   RecName: Full=Cysteate synthase {ECO:0000303|PubMed:35414181};\nDE            EC=2.5.1.76 {ECO:0000269|PubMed:35414181};\nGN   Name=capA {ECO:0000303|PubMed:35414181};\nGN   OrderedLocusNames=Coch_1829 {ECO:0000312|EMBL:ACU93374.1};\nOS   Capnocytophaga ochracea (strain ATCC 27872 / DSM 7271 / CCUG 9716 / JCM\nOS   12966 / NCTC 12371 / SS31 / VPI 2845) (Bacteroides ochraceus).\nOC   Bacteria; Pseudomonadati; Bacteroidota; Flavobacteriia; Flavobacteriales;\nOC   Flavobacteriaceae; Capnocytophaga.\nOX   NCBI_TaxID=521097;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:40.735965+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110",
  "url": "https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cysteate synthase {ECO:0000303|PubMed:35414181};\nDE            EC=2.5.1.76 {ECO:0000269|PubMed:35414181};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:40.735965+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110",
  "url": "https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   MUTAGENESIS OF LYS-241.\nRX   PubMed=35414181; DOI=10.1021/acs.biochem.2c00102;\nRA   Liu Y., Wei Y., Teh T.M., Liu D., Zhou Y., Zhao S., Ang E.L., Zhao H.,\nRA   Zhang Y.;\nRT   \"Identification and Characterization of the Biosynthetic Pathway of the\nRT   Sulfonolipid Capnine.\";\nRL   Biochemistry 61:2861-2869(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:40.735965+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110",
  "url": "https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=O-phospho-L-serine + sulfite + H(+) = L-cysteate + phosphate;\nCC         Xref=Rhea:RHEA:26486, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57524, ChEBI:CHEBI:58090; EC=2.5.1.76;\nCC         Evidence={ECO:0000269|PubMed:35414181};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:26487;\nCC         Evidence={ECO:0000269|PubMed:35414181};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:40.735965+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110",
  "url": "https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
