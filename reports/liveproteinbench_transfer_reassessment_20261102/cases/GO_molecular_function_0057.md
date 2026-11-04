# GO_molecular_function_0057

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0057.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — ATP binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPARKYKIHVPCTSANIGPGFDVCGIALSLSLSLVVTIPSVSSGAEPLPKIIYTGLDSDNVPLSPYKNLLTRVALYVLRANGITTFPPGVTIEARNEIPFGRGLGSSGAAVIAGVLLGDLLGNLSLPKSRLLDFALMVERHPDNVTAALMGGFVGSYLRELSPEDMSAASIPLAEVLPEYPPDAGPDWGKSPPQPPHGIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARSPPDPDLIYDAMGDRVHQPYRMTLIPGLPKILSTLTPTSHPGLLGICLSGAGPTILALATHNFEAIANEIERIFGDEQVLVDHKVLNIDEKGSWVEDITEA

[Multiple Choices]
A. N-acetylglucosamine-6-sulfatase activity
B. medium-chain fatty acyl-CoA dehydrogenase activity
C. ATP binding
D. nicotinamide phosphoribosyltransferase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated with ATP binding (C7; computational IEA). It is also identified as a homoserine kinase that catalyzes a reaction using ATP (C5, C6, C8), which supports ATP binding as part of its molecular function. The ATP-binding annotation is computational rather than a reported direct binding assay.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a kinase-family protein, and transferable knowledge of ATP-dependent kinases is that they bind ATP to transfer its phosphate group. Among these choices, that supports ATP binding (C) over the unrelated sulfatase, fatty-acyl-CoA dehydrogenase, and nicotinamide phosphoribosyltransferase activities.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference about ATP-dependent kinases gives a meaningful basis for choosing C without needing this exact protein’s database record. The sequence-based family assignment may not be certain from the sequence alone, but the alternatives are sufficiently distinct.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct functions, and ATP binding is supported for an ATP-dependent kinase.


### Important caveats

- The supplied annotation evidence matches the sequence, but the author’s exact source snapshot is unknown.
- The ATP-binding annotation is computational; the cited reaction and kinase annotations support the function but do not themselves document a direct ATP-binding measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a kinase-family protein, and transferable knowledge of ATP-dependent kinases is that they bind ATP to transfer its phosphate group. Among these choices, that supports ATP binding (C) over the unrelated sulfatase, fatty-acyl-CoA dehydrogenase, and nicotinamide phosphoribosyltransferase activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference about ATP-dependent kinases gives a meaningful basis for choosing C without needing this exact protein’s database record. The sequence-based family assignment may not be certain from the sequence alone, but the alternatives are sufficiently distinct."
  },
  "case_id": "GO_molecular_function_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated with ATP binding (C7; computational IEA). It is also identified as a homoserine kinase that catalyzes a reaction using ATP (C5, C6, C8), which supports ATP binding as part of its molecular function. The ATP-binding annotation is computational rather than a reported direct binding assay."
  },
  "important_caveats": [
    "The supplied annotation evidence matches the sequence, but the author’s exact source snapshot is unknown.",
    "The ATP-binding annotation is computational; the cited reaction and kinase annotations support the function but do not themselves document a direct ATP-binding measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct functions, and ATP binding is supported for an ATP-dependent kinase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated with ATP binding (C7; computational IEA). It is also identified as a homoserine kinase that catalyzes a reaction using ATP (C5, C6, C8), which supports ATP binding as part of its molecular function. The ATP-binding annotation is computational rather than a reported direct binding assay.",
    "evidence_ids": ["C5", "C6", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a kinase-family protein, and transferable knowledge of ATP-dependent kinases is that they bind ATP to transfer its phosphate group. Among these choices, that supports ATP binding (C) over the unrelated sulfatase, fatty-acyl-CoA dehydrogenase, and nicotinamide phosphoribosyltransferase activities.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference about ATP-dependent kinases gives a meaningful basis for choosing C without needing this exact protein’s database record. The sequence-based family assignment may not be certain from the sequence alone, but the alternatives are sufficiently distinct."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct functions, and ATP binding is supported for an ATP-dependent kinase."
  },
  "important_caveats": [
    "The supplied annotation evidence matches the sequence, but the author’s exact source snapshot is unknown.",
    "The ATP-binding annotation is computational; the cited reaction and kinase annotations support the function but do not themselves document a direct ATP-binding measurement."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is a homoserine kinase (EC 2.7.1.39) that catalyzes L-homoserine + ATP → O-phospho-L-homoserine + ADP + H+. The GO annotation GO:0005524 (ATP binding) is present for this protein (evidence C7, H5), albeit as an IEA annotation. Among the four offered choices, C is the only one that applies to this protein; the primary catalytic function (homoserine kinase activity, GO:0004413) is not among the options. The ATP binding annotation is a legitimate molecular function for an ATP-dependent kinase, and the other three options (sulfatase, dehydrogenase, phosphoribosyltransferase) are entirely unrelated enzyme classes.

Citations as saved: [C7](#evidence-c7), [C6](#evidence-c6), [H5](#evidence-h5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the motif 'GLGSSG' (in the region 'GLGSSGAAVIAGVLLGDLLGNLSLPK'), which is a well-known signature of the GHMP kinase superfamily (Galactokinase, Homoserine kinase, Mevalonate kinase, Phosphomevalonate kinase). GHMP kinases are ATP-dependent enzymes that transfer a phosphate group from ATP to their substrate. Recognizing this family motif allows inference that the protein binds ATP as a co-substrate, supporting 'ATP binding' (option C). The other options are eliminated by the absence of their characteristic sequence features: sulfatases (option A) require a C-X-P-X-R motif or formylglycine-modification context; medium-chain acyl-CoA dehydrogenases (option B) contain FAD-binding Rossmann-fold motifs (e.g., 'GxGxxG' in a distinct structural context) and are much larger proteins; nicotinamide phosphoribosyltransferases (option D) belong to a completely different transferase fold family with no resemblance to kinase motifs. The GLGSSG family signature plus the general principle that kinases bind ATP provides a concrete, transferable inference that meaningfully distinguishes C from A, B, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GLGSSG motif is a conserved, widely taught family-level feature of GHMP kinases. A knowledgeable model recognizing this motif can infer the protein is an ATP-dependent kinase, making ATP binding the only applicable molecular function among the four choices. The elimination of A, B, D relies on the absence of their respective family signatures, which is standard comparative reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the prompt asks for the 'primary molecular function' and the true primary function (homoserine kinase activity, GO:0004413) is not among the options, only one of the four choices (C, ATP binding) is annotated for this protein. Options A, B, and D describe entirely unrelated enzyme activities with no sequence or functional overlap. No ambiguity in selection arises among the offered alternatives.


### Important caveats

- The primary molecular function of this protein is homoserine kinase activity (GO:0004413, IGI evidence), not ATP binding. The question's phrasing 'primary molecular function' is slightly misleading since ATP binding (GO:0005524, IEA:InterPro) is a secondary annotation. However, since the true primary function is not among the choices, C remains the only valid answer.
- The ATP binding annotation carries IEA (Inferred from Electronic Annotation) evidence via InterPro/UniProtKB-KW, not direct experimental measurement for this specific protein. The experimental evidence (PubMed:18757810) supports the kinase function but the ATP-binding annotation is computationally transferred.
- The GLGSSG motif identification as a GHMP kinase signature is well-established in the literature but the reviewer should note this is a family-level pattern, not a unique fingerprint; some non-GHMP proteins may contain similar short sequences. In this case, the full context (sequence length, overall composition, and absence of competing family motifs) supports the assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the motif 'GLGSSG' (in the region 'GLGSSGAAVIAGVLLGDLLGNLSLPK'), which is a well-known signature of the GHMP kinase superfamily (Galactokinase, Homoserine kinase, Mevalonate kinase, Phosphomevalonate kinase). GHMP kinases are ATP-dependent enzymes that transfer a phosphate group from ATP to their substrate. Recognizing this family motif allows inference that the protein binds ATP as a co-substrate, supporting 'ATP binding' (option C). The other options are eliminated by the absence of their characteristic sequence features: sulfatases (option A) require a C-X-P-X-R motif or formylglycine-modification context; medium-chain acyl-CoA dehydrogenases (option B) contain FAD-binding Rossmann-fold motifs (e.g., 'GxGxxG' in a distinct structural context) and are much larger proteins; nicotinamide phosphoribosyltransferases (option D) belong to a completely different transferase fold family with no resemblance to kinase motifs. The GLGSSG family signature plus the general principle that kinases bind ATP provides a concrete, transferable inference that meaningfully distinguishes C from A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GLGSSG motif is a conserved, widely taught family-level feature of GHMP kinases. A knowledgeable model recognizing this motif can infer the protein is an ATP-dependent kinase, making ATP binding the only applicable molecular function among the four choices. The elimination of A, B, D relies on the absence of their respective family signatures, which is standard comparative reasoning."
  },
  "case_id": "GO_molecular_function_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C6",
      "H5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The protein is a homoserine kinase (EC 2.7.1.39) that catalyzes L-homoserine + ATP → O-phospho-L-homoserine + ADP + H+. The GO annotation GO:0005524 (ATP binding) is present for this protein (evidence C7, H5), albeit as an IEA annotation. Among the four offered choices, C is the only one that applies to this protein; the primary catalytic function (homoserine kinase activity, GO:0004413) is not among the options. The ATP binding annotation is a legitimate molecular function for an ATP-dependent kinase, and the other three options (sulfatase, dehydrogenase, phosphoribosyltransferase) are entirely unrelated enzyme classes."
  },
  "important_caveats": [
    "The primary molecular function of this protein is homoserine kinase activity (GO:0004413, IGI evidence), not ATP binding. The question's phrasing 'primary molecular function' is slightly misleading since ATP binding (GO:0005524, IEA:InterPro) is a secondary annotation. However, since the true primary function is not among the choices, C remains the only valid answer.",
    "The ATP binding annotation carries IEA (Inferred from Electronic Annotation) evidence via InterPro/UniProtKB-KW, not direct experimental measurement for this specific protein. The experimental evidence (PubMed:18757810) supports the kinase function but the ATP-binding annotation is computationally transferred.",
    "The GLGSSG motif identification as a GHMP kinase signature is well-established in the literature but the reviewer should note this is a family-level pattern, not a unique fingerprint; some non-GHMP proteins may contain similar short sequences. In this case, the full context (sequence length, overall composition, and absence of competing family motifs) supports the assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the prompt asks for the 'primary molecular function' and the true primary function (homoserine kinase activity, GO:0004413) is not among the options, only one of the four choices (C, ATP binding) is annotated for this protein. Options A, B, and D describe entirely unrelated enzyme activities with no sequence or functional overlap. No ambiguity in selection arises among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is a homoserine kinase (EC 2.7.1.39) that catalyzes L-homoserine + ATP → O-phospho-L-homoserine + ADP + H+. The GO annotation GO:0005524 (ATP binding) is present for this protein (evidence C7, H5), albeit as an IEA annotation. Among the four offered choices, C is the only one that applies to this protein; the primary catalytic function (homoserine kinase activity, GO:0004413) is not among the options. The ATP binding annotation is a legitimate molecular function for an ATP-dependent kinase, and the other three options (sulfatase, dehydrogenase, phosphoribosyltransferase) are entirely unrelated enzyme classes.",
    "evidence_ids": ["C7", "C6", "H5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the motif 'GLGSSG' (in the region 'GLGSSGAAVIAGVLLGDLLGNLSLPK'), which is a well-known signature of the GHMP kinase superfamily (Galactokinase, Homoserine kinase, Mevalonate kinase, Phosphomevalonate kinase). GHMP kinases are ATP-dependent enzymes that transfer a phosphate group from ATP to their substrate. Recognizing this family motif allows inference that the protein binds ATP as a co-substrate, supporting 'ATP binding' (option C). The other options are eliminated by the absence of their characteristic sequence features: sulfatases (option A) require a C-X-P-X-R motif or formylglycine-modification context; medium-chain acyl-CoA dehydrogenases (option B) contain FAD-binding Rossmann-fold motifs (e.g., 'GxGxxG' in a distinct structural context) and are much larger proteins; nicotinamide phosphoribosyltransferases (option D) belong to a completely different transferase fold family with no resemblance to kinase motifs. The GLGSSG family signature plus the general principle that kinases bind ATP provides a concrete, transferable inference that meaningfully distinguishes C from A, B, and D.",
    "missing_item_specific_fact": "",
    "reason": "The GLGSSG motif is a conserved, widely taught family-level feature of GHMP kinases. A knowledgeable model recognizing this motif can infer the protein is an ATP-dependent kinase, making ATP binding the only applicable molecular function among the four choices. The elimination of A, B, D relies on the absence of their respective family signatures, which is standard comparative reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the prompt asks for the 'primary molecular function' and the true primary function (homoserine kinase activity, GO:0004413) is not among the options, only one of the four choices (C, ATP binding) is annotated for this protein. Options A, B, and D describe entirely unrelated enzyme activities with no sequence or functional overlap. No ambiguity in selection arises among the offered alternatives."
  },
  "important_caveats": [
    "The primary molecular function of this protein is homoserine kinase activity (GO:0004413, IGI evidence), not ATP binding. The question's phrasing 'primary molecular function' is slightly misleading since ATP binding (GO:0005524, IEA:InterPro) is a secondary annotation. However, since the true primary function is not among the choices, C remains the only valid answer.",
    "The ATP binding annotation carries IEA (Inferred from Electronic Annotation) evidence via InterPro/UniProtKB-KW, not direct experimental measurement for this specific protein. The experimental evidence (PubMed:18757810) supports the kinase function but the ATP-binding annotation is computationally transferred.",
    "The GLGSSG motif identification as a GHMP kinase signature is well-established in the literature but the reviewer should note this is a family-level pattern, not a unique fingerprint; some non-GHMP proteins may contain similar short sequences. In this case, the full context (sequence length, overall composition, and absence of competing family motifs) supports the assignment."
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
  "benchmark_sequence_length": 357,
  "benchmark_sequence_sha256": "0d5b6ca56754f8b7a34530cb0993479508f4e035318ede70547b7393e120e776",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 357,
  "current_source_sequence_sha256": "0d5b6ca56754f8b7a34530cb0993479508f4e035318ede70547b7393e120e776",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VU26",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "selected_historical_source_sequence_length": 357,
  "selected_historical_source_sequence_sha256": "0d5b6ca56754f8b7a34530cb0993479508f4e035318ede70547b7393e120e776",
  "selected_historical_version": {
    "accession": "J9VU26",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "KHSE_CRYN9",
    "sequenceVersion": 1
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VU26\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17423\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.1.39\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Homoserine kinase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HK\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HSK\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18757810\",\"source\":\"PubMed\"}],\"value\":\"Commits homoserine to the threonine biosynthesis pathway by catalyzing its O-phosphorylation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17423\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13986\"}}],\"reaction\":{\"ecNumber\":\"2.7.1.39\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17423\",\"source\":\"UniProtKB\"}],\"name\":\"L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13985\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57476\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57590\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005524\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:ATP binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000316\",\"id\":\"18757810\",\"source\":\"PubMed\"}],\"id\":\"GO:0004413\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:homoserine kinase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IGI:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Kingsbury J.M.\",\"McCusker J.H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18757810\"},{\"database\":\"DOI\",\"id\":\"10.1099/mic.0.2008/019729-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"2767\",\"id\":\"18757810\",\"journal\":\"Microbiology\",\"lastPage\":\"2775\",\"publicationDate\":\"2008\",\"title\":\"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\",\"volume\":\"154\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ACC85591.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   KHSE_CRYN9              Reviewed;         357 AA.\nAC   J9VU26; B2MVI2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Homoserine kinase {ECO:0000305};\nDE            Short=HK {ECO:0000305};\nDE            Short=HSK {ECO:0000305};\nDE            EC=2.7.1.39 {ECO:0000250|UniProtKB:P17423};\nGN   Name=THR1 {ECO:0000303|PubMed:18757810};\nGN   ORFNames=CNAG_04156 {ECO:0000312|EMBL:AFR96886.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ACC85591.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;\nRA   Kingsbury J.M., McCusker J.H.;\nRT   \"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\";\nRL   Microbiology 154:2767-2775(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Commits homoserine to the threonine biosynthesis pathway by\nCC       catalyzing its O-phosphorylation. {ECO:0000269|PubMed:18757810}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+);\nCC         Xref=Rhea:RHEA:13985, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:57476, ChEBI:CHEBI:57590, ChEBI:CHEBI:456216;\nCC         EC=2.7.1.39; Evidence={ECO:0000250|UniProtKB:P17423};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13986;\nCC         Evidence={ECO:0000250|UniProtKB:P17423};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0004413; F:homoserine kinase activity; IGI:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005524\nname: ATP binding\nnamespace: molecular_function\ndef: \"Binding to ATP, adenosine 5'-triphosphate, a universally important coenzyme and enzyme regulator.\" [ISBN:0198506732]\nsynonym: \"Mg-ATP binding\" EXACT []\nsynonym: \"MgATP binding\" EXACT []\nxref: Reactome:R-HSA-265682 \"KCNJ11 tetramer:ABCC8 tetramer binds 4xATP, closing the channel\"\nis_a: GO:0032559 ! adenyl ribonucleotide binding\nis_a: GO:0035639 ! purine ribonucleoside triphosphate binding\nis_a: GO:0043168 ! anion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005524",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 57041-57052",
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
  "excerpt": "[Term]\nid: GO:0008449\nname: N-acetylglucosamine-6-sulfatase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of the 6-sulfate group of the N-acetyl-D-glucosamine 6-sulfate units of heparan sulfate and keratan sulfate.\" [EC:3.1.6.14]\nsynonym: \"2-acetamido-2-deoxy-D-glucose 6-sulfate sulfatase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"acetylglucosamine 6-sulfatase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"chondroitinsulfatase\" BROAD [EC:3.1.6.14]\nsynonym: \"glucosamine-6-sulfatase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"N-acetyl-D-glucosamine-6-sulfate 6-sulfohydrolase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"N-acetylglucosamine 6-sulfate sulfatase activity\" RELATED [EC:3.1.6.14]\nsynonym: \"N-acetylglucosamine-6-sulphatase activity\" EXACT []\nsynonym: \"O,N-disulfate O-sulfohydrolase activity\" RELATED [EC:3.1.6.14]\nxref: EC:3.1.6.14\nxref: MetaCyc:3.1.6.14-RXN\nxref: Reactome:R-HSA-1638032 \"GNS:Ca2+ cleaves sulfate from GlcNAc-6-sulfate units of keratan sulfate\"\nxref: Reactome:R-HSA-2263495 \"Defective GNS does not hydrolyse 6-sulfate from GlcNAc6S\"\nis_a: GO:0008484 ! sulfuric ester hydrolase activity\nproperty_value: skos:exactMatch EC:3.1.6.14\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008449",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 83469-83488",
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
  "excerpt": "[Term]\nid: GO:0047280\nname: nicotinamide phosphoribosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: diphosphate + nicotinamide mononucleotide = 5-phospho-alpha-D-ribose 1-diphosphate + H+ + nicotinamide.\" [RHEA:16149]\nsynonym: \"nicotinamide mononucleotide pyrophosphorylase activity\" RELATED [EC:2.4.2.12]\nsynonym: \"nicotinamide mononucleotide synthetase activity\" RELATED [EC:2.4.2.12]\nsynonym: \"nicotinamide-nucleotide:diphosphate phospho-alpha-D-ribosyltransferase activity\" RELATED [EC:2.4.2.12]\nsynonym: \"NMN diphosphorylase activity\" RELATED [EC:2.4.2.12]\nsynonym: \"NMN pyrophosphorylase activity\" RELATED [EC:2.4.2.12]\nsynonym: \"NMN synthetase activity\" RELATED [EC:2.4.2.12]\nxref: EC:2.4.2.12\nxref: KEGG_REACTION:R01271\nxref: MetaCyc:2.4.2.12-RXN\nxref: Reactome:R-HSA-197250 \"NAMPT transfers PRIB to NAM to form NAMN\"\nxref: RHEA:16149\nis_a: GO:0016763 ! pentosyltransferase activity\nproperty_value: skos:exactMatch EC:2.4.2.12\nproperty_value: skos:exactMatch RHEA:16149\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0047280",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 287522-287541",
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
  "excerpt": "[Term]\nid: GO:0070991\nname: medium-chain fatty acyl-CoA dehydrogenase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a medium-chain 2,3-saturated fatty acyl-CoA + H+ + oxidized [electron-transfer flavoprotein] = a medium-chain trans-(2E)-enoyl-CoA + reduced [electron-transfer flavoprotein]. A medium-chain fatty acid has an aliphatic tail containing 6 to 12 carbons.\" [RHEA:14477]\ncomment: While there is not universal consensus on the lengths of short-, medium-, long- and very-long-chain fatty acids, the GO uses the definitions in ChEBI (see CHEBI:26666, CHEBI:59554, CHEBI:15904 and CHEBI:27283).\nsynonym: \"MCAD activity\" EXACT [GOC:mah]\nxref: EC:1.3.8.7\nxref: MetaCyc:RXN-11734\nxref: RHEA:14477\nxref: RHEA:43464\nxref: RHEA:47296\nxref: RHEA:48176\nxref: RHEA:48180\nxref: RHEA:48208\nxref: RHEA:82951\nxref: RHEA:84471\nxref: RHEA:84475\nxref: RHEA:84607\nxref: RHEA:84611\nxref: RHEA:84615\nis_a: GO:0003995 ! acyl-CoA dehydrogenase activity\nproperty_value: skos:exactMatch EC:1.3.8.7\nproperty_value: skos:exactMatch MetaCyc:RXN-11734\nproperty_value: skos:exactMatch RHEA:14477\nproperty_value: skos:narrowMatch RHEA:43464\nproperty_value: skos:narrowMatch RHEA:47296\nproperty_value: skos:narrowMatch RHEA:48176\nproperty_value: skos:narrowMatch RHEA:48180\nproperty_value: skos:narrowMatch RHEA:48208\nproperty_value: skos:narrowMatch RHEA:82951\nproperty_value: skos:narrowMatch RHEA:84471\nproperty_value: skos:narrowMatch RHEA:84475\nproperty_value: skos:narrowMatch RHEA:84607\nproperty_value: skos:narrowMatch RHEA:84611\nproperty_value: skos:narrowMatch RHEA:84615\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070991",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 373007-373043",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
