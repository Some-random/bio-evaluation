# GO_molecular_function_0087

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0087.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — isomerase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIRLLYLLVKPAGMSDETFRAECLRHYEMSHDVPGLHKYEVRLVAEQPTDTHVPFFDIGHVDAIGECWFKDDAAYATYMASDIRKAWFEHGKTFIGQLKPFRTAPVAGDEPAS

[Multiple Choices]
A. S-adenosyl-L-methionine binding
B. isomerase activity
C. carbohydrate binding
D. rRNA binding
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

> The sequence-matched entry reports experimentally supported isomerase activity and the catalytic isomerization of 4-methylmuconolactone to 3-methylmuconolactone. This supports the broader offered choice, isomerase activity.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a compact, enzyme-like protein. It lacks the characteristic cysteine cluster associated with radical SAM enzymes, has no conspicuously basic profile suggesting rRNA binding, and provides no obvious carbohydrate-binding domain signature. Among these choices, a catalytic isomerase is a credible inference from the sequence and transferable protein-family and sequence-pattern knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> These features do not establish the exact substrate or enzyme family, but they provide a meaningful basis for choosing isomerase activity over the offered binding functions. The inference is probabilistic, not a substitute for experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices contrast a broad catalytic function with three distinct binding functions; no second option is comparably supported by the available sequence features.


### Important caveats

- The reviewer-only evidence supports the key with experimental annotations, but the original input did not include those annotations.
- The sequence-based argument supports the broad choice, not the exact reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a compact, enzyme-like protein. It lacks the characteristic cysteine cluster associated with radical SAM enzymes, has no conspicuously basic profile suggesting rRNA binding, and provides no obvious carbohydrate-binding domain signature. Among these choices, a catalytic isomerase is a credible inference from the sequence and transferable protein-family and sequence-pattern knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "These features do not establish the exact substrate or enzyme family, but they provide a meaningful basis for choosing isomerase activity over the offered binding functions. The inference is probabilistic, not a substitute for experimental characterization."
  },
  "case_id": "GO_molecular_function_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched entry reports experimentally supported isomerase activity and the catalytic isomerization of 4-methylmuconolactone to 3-methylmuconolactone. This supports the broader offered choice, isomerase activity."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key with experimental annotations, but the original input did not include those annotations.",
    "The sequence-based argument supports the broad choice, not the exact reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices contrast a broad catalytic function with three distinct binding functions; no second option is comparably supported by the available sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched entry reports experimentally supported isomerase activity and the catalytic isomerization of 4-methylmuconolactone to 3-methylmuconolactone. This supports the broader offered choice, isomerase activity.",
    "evidence_ids": ["C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a compact, enzyme-like protein. It lacks the characteristic cysteine cluster associated with radical SAM enzymes, has no conspicuously basic profile suggesting rRNA binding, and provides no obvious carbohydrate-binding domain signature. Among these choices, a catalytic isomerase is a credible inference from the sequence and transferable protein-family and sequence-pattern knowledge.",
    "missing_item_specific_fact": "",
    "reason": "These features do not establish the exact substrate or enzyme family, but they provide a meaningful basis for choosing isomerase activity over the offered binding functions. The inference is probabilistic, not a substitute for experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices contrast a broad catalytic function with three distinct binding functions; no second option is comparably supported by the available sequence features."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key with experimental annotations, but the original input did not include those annotations.",
    "The sequence-based argument supports the broad choice, not the exact reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is experimentally characterized (ECO:0000269, two independent PubMed studies) as 4-carboxymethyl-4-methylbutenolide mutase (EC 5.4.99.14), an isomerase. The GO annotation GO:0047469 is_a GO:0016866 (intramolecular transferase activity) is_a GO:0016853 (isomerase activity), confirming that 'isomerase activity' is a valid parent-level description of this protein's molecular function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 113-aa sequence contains the motif 'IGHVDAIGECWFKDDAAY' and surrounding residues that are characteristic of the muconolactone isomerase superfamily (EC 5.3.3.9 / 5.4.99.14), a well-characterized family of small (~110 aa) isomerases involved in aromatic compound degradation. Key transferable features include: (1) the small protein size (~113 aa) matching the muconolactone isomerase fold; (2) the conserved Glu-Asp catalytic dyad embedded in the 'GECWFKDDAAY' region, which is a hallmark of this superfamily; (3) the overall hydrophobic core with a few surface polar residues typical of this fold. These features distinguish the protein from SAM-binding enzymes (which require methyltransferase or radical-SAM CX3CX2C motifs absent here), carbohydrate-binding proteins (which show lectin-like or glycosyltransferase folds absent here), and rRNA-binding proteins (which show ribosomal protein signatures absent here). Family-level recognition of the muconolactone isomerase superfamily, learned from homologs such as Pseudomonas muconolactone isomerase (EC 5.3.3.9), provides a concrete basis to select 'isomerase activity' over the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The muconolactone isomerase superfamily is well-characterized across multiple organisms and structures. The sequence motifs (IGHVDAIGECWFKDDAAY, conserved Glu/Asp catalytic residues, small size) are transferable family signatures that a knowledgeable model can use to assign isomerase activity and exclude the three distractors, which require entirely different structural motifs and folds.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular function categories (methyl-group binding, catalytic isomerization, sugar binding, nucleic acid binding). The sequence features clearly align with the muconolactone isomerase superfamily and exclude the other three categories. No ambiguity among the offered choices.


### Important caveats

- The specific GO term for this protein is GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity), a very specific term. The option 'isomerase activity' (GO:0016853) is a broad parent term reached via two is_a edges. This is valid but less precise than the annotated term.
- The muconolactone isomerase superfamily recognition argument depends on the model having learned family-level sequence signatures from related proteins; the strength of this inference for a given model depends on training data coverage.
- The sequence is short (113 aa) and the family motifs, while recognizable, are not as long or information-rich as in larger multi-domain proteins.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 113-aa sequence contains the motif 'IGHVDAIGECWFKDDAAY' and surrounding residues that are characteristic of the muconolactone isomerase superfamily (EC 5.3.3.9 / 5.4.99.14), a well-characterized family of small (~110 aa) isomerases involved in aromatic compound degradation. Key transferable features include: (1) the small protein size (~113 aa) matching the muconolactone isomerase fold; (2) the conserved Glu-Asp catalytic dyad embedded in the 'GECWFKDDAAY' region, which is a hallmark of this superfamily; (3) the overall hydrophobic core with a few surface polar residues typical of this fold. These features distinguish the protein from SAM-binding enzymes (which require methyltransferase or radical-SAM CX3CX2C motifs absent here), carbohydrate-binding proteins (which show lectin-like or glycosyltransferase folds absent here), and rRNA-binding proteins (which show ribosomal protein signatures absent here). Family-level recognition of the muconolactone isomerase superfamily, learned from homologs such as Pseudomonas muconolactone isomerase (EC 5.3.3.9), provides a concrete basis to select 'isomerase activity' over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The muconolactone isomerase superfamily is well-characterized across multiple organisms and structures. The sequence motifs (IGHVDAIGECWFKDDAAY, conserved Glu/Asp catalytic residues, small size) are transferable family signatures that a knowledgeable model can use to assign isomerase activity and exclude the three distractors, which require entirely different structural motifs and folds."
  },
  "case_id": "GO_molecular_function_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "GO2",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The protein is experimentally characterized (ECO:0000269, two independent PubMed studies) as 4-carboxymethyl-4-methylbutenolide mutase (EC 5.4.99.14), an isomerase. The GO annotation GO:0047469 is_a GO:0016866 (intramolecular transferase activity) is_a GO:0016853 (isomerase activity), confirming that 'isomerase activity' is a valid parent-level description of this protein's molecular function."
  },
  "important_caveats": [
    "The specific GO term for this protein is GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity), a very specific term. The option 'isomerase activity' (GO:0016853) is a broad parent term reached via two is_a edges. This is valid but less precise than the annotated term.",
    "The muconolactone isomerase superfamily recognition argument depends on the model having learned family-level sequence signatures from related proteins; the strength of this inference for a given model depends on training data coverage.",
    "The sequence is short (113 aa) and the family motifs, while recognizable, are not as long or information-rich as in larger multi-domain proteins."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function categories (methyl-group binding, catalytic isomerization, sugar binding, nucleic acid binding). The sequence features clearly align with the muconolactone isomerase superfamily and exclude the other three categories. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is experimentally characterized (ECO:0000269, two independent PubMed studies) as 4-carboxymethyl-4-methylbutenolide mutase (EC 5.4.99.14), an isomerase. The GO annotation GO:0047469 is_a GO:0016866 (intramolecular transferase activity) is_a GO:0016853 (isomerase activity), confirming that 'isomerase activity' is a valid parent-level description of this protein's molecular function.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "GO1", "GO2", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 113-aa sequence contains the motif 'IGHVDAIGECWFKDDAAY' and surrounding residues that are characteristic of the muconolactone isomerase superfamily (EC 5.3.3.9 / 5.4.99.14), a well-characterized family of small (~110 aa) isomerases involved in aromatic compound degradation. Key transferable features include: (1) the small protein size (~113 aa) matching the muconolactone isomerase fold; (2) the conserved Glu-Asp catalytic dyad embedded in the 'GECWFKDDAAY' region, which is a hallmark of this superfamily; (3) the overall hydrophobic core with a few surface polar residues typical of this fold. These features distinguish the protein from SAM-binding enzymes (which require methyltransferase or radical-SAM CX3CX2C motifs absent here), carbohydrate-binding proteins (which show lectin-like or glycosyltransferase folds absent here), and rRNA-binding proteins (which show ribosomal protein signatures absent here). Family-level recognition of the muconolactone isomerase superfamily, learned from homologs such as Pseudomonas muconolactone isomerase (EC 5.3.3.9), provides a concrete basis to select 'isomerase activity' over the other three options.",
    "missing_item_specific_fact": "",
    "reason": "The muconolactone isomerase superfamily is well-characterized across multiple organisms and structures. The sequence motifs (IGHVDAIGECWFKDDAAY, conserved Glu/Asp catalytic residues, small size) are transferable family signatures that a knowledgeable model can use to assign isomerase activity and exclude the three distractors, which require entirely different structural motifs and folds."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function categories (methyl-group binding, catalytic isomerization, sugar binding, nucleic acid binding). The sequence features clearly align with the muconolactone isomerase superfamily and exclude the other three categories. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The specific GO term for this protein is GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity), a very specific term. The option 'isomerase activity' (GO:0016853) is a broad parent term reached via two is_a edges. This is valid but less precise than the annotated term.",
    "The muconolactone isomerase superfamily recognition argument depends on the model having learned family-level sequence signatures from related proteins; the strength of this inference for a given model depends on training data coverage.",
    "The sequence is short (113 aa) and the family motifs, while recognizable, are not as long or information-rich as in larger multi-domain proteins."
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
  "benchmark_sequence_length": 113,
  "benchmark_sequence_sha256": "5cff0d57cd7ece41c777ddb6189bfa6b989a549198f8086c53758f07f892f181",
  "current_entry_audit": {
    "entryVersion": 67,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 113,
  "current_source_sequence_sha256": "5cff0d57cd7ece41c777ddb6189bfa6b989a549198f8086c53758f07f892f181",
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
  "requested_accession": "O51799",
  "selected_historical_entry_version": 65,
  "selected_historical_record_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "selected_historical_source_sequence_length": 113,
  "selected_historical_source_sequence_sha256": "5cff0d57cd7ece41c777ddb6189bfa6b989a549198f8086c53758f07f892f181",
  "selected_historical_version": {
    "accession": "O51799",
    "database": "Swiss-Prot",
    "entryVersion": 65,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MMLI_CUPPJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O51799\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":67,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cupriavidus necator (strain JMP 134)\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Burkholderiaceae\",\"Cupriavidus\"],\"scientificName\":\"Cupriavidus pinatubonensis (strain JMP 134 / LMG 1197)\",\"taxonId\":264198}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"2241929\",\"source\":\"PubMed\"}],\"value\":\"4-carboxymethyl-4-methylbut-2-en-4-olide isomerase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"2241929\",\"source\":\"PubMed\"}],\"value\":\"4-methyl-2-enelactone isomerase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"value\":\"4-methylmuconolactone methylisomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"value\":\"MLMI\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"value\":\"5.4.99.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"4-carboxymethyl-4-methylbutenolide mutase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"value\":\"Isomerase involved in the degradation of 4-methylcatechol (PubMed:2241929). Catalyzes the isomerization of the dead-end metabolite 4-methylmuconolactone (4-ML) to 3-methylmuconolactone (3-ML), which can then be further degraded through a modified 3-oxoadipate pathway (PubMed:2241929, PubMed:9461415). Can also use 1-methylbislactone, but not the isomeric methyl-substituted 4-carboxymethylbut-2-en-4-olides (PubMed:2241929)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:19238\"}}],\"reaction\":{\"ecNumber\":\"5.4.99.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"name\":\"4-methylmuconolactone = 3-methylmuconolactone\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19237\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57883\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57888\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"2241929\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9461415\",\"source\":\"PubMed\"}],\"id\":\"GO:0047469\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:4-carboxymethyl-4-methylbutenolide mutase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Erb R.W.\",\"Timmis K.N.\",\"Pieper D.H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9461415\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0378-1119(97)00565-9\"}],\"citationType\":\"journal article\",\"firstPage\":\"53\",\"id\":\"9461415\",\"journal\":\"Gene\",\"lastPage\":\"62\",\"publicationDate\":\"1998\",\"title\":\"Characterization of a gene cluster from Ralstonia eutropha JMP134 encoding metabolism of 4-methylmuconolactone.\",\"volume\":\"206\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAA67958.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"JMP134 / LMG 1197\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Pieper D.H.\",\"Stadler-Fritzsche K.\",\"Knackmuss H.J.\",\"Engesser K.H.\",\"Bruce N.C.\",\"Cain R.B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"2241929\"},{\"database\":\"DOI\",\"id\":\"10.1042/bj2710529\"}],\"citationType\":\"journal article\",\"firstPage\":\"529\",\"id\":\"2241929\",\"journal\":\"Biochem. J.\",\"lastPage\":\"534\",\"publicationDate\":\"1990\",\"title\":\"Purification and characterization of 4-methylmuconolactone methylisomerase, a novel enzyme of the modified 3-oxoadipate pathway in the gram-negative bacterium Alcaligenes eutrophus JMP 134.\",\"volume\":\"271\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"JMP134 / LMG 1197\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:12.163444+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968",
  "url": "https://rest.uniprot.org/uniprotkb/O51799.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H1",
  "excerpt": "ID   MMLI_CUPPJ              Reviewed;         113 AA.\nAC   O51799; Q471R3;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-1998, sequence version 1.\nDT   28-JAN-2026, entry version 65.\nDE   RecName: Full=4-carboxymethyl-4-methylbutenolide mutase {ECO:0000305};\nDE            EC=5.4.99.14 {ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};\nDE   AltName: Full=4-carboxymethyl-4-methylbut-2-en-4-olide isomerase {ECO:0000303|PubMed:2241929};\nDE   AltName: Full=4-methyl-2-enelactone isomerase {ECO:0000303|PubMed:2241929};\nDE   AltName: Full=4-methylmuconolactone methylisomerase {ECO:0000303|PubMed:2241929, ECO:0000303|PubMed:9461415};\nDE            Short=MLMI {ECO:0000303|PubMed:9461415};\nGN   Name=mmlI {ECO:0000303|PubMed:9461415};\nGN   OrderedLocusNames=Reut_A1503 {ECO:0000312|EMBL:AAZ60870.1};\nOS   Cupriavidus pinatubonensis (strain JMP 134 / LMG 1197) (Cupriavidus necator\nOS   (strain JMP 134)).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Burkholderiaceae; Cupriavidus.\nOX   NCBI_TaxID=264198;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAA67958.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   SUBUNIT.\nRC   STRAIN=JMP134 / LMG 1197;\nRX   PubMed=9461415; DOI=10.1016/s0378-1119(97)00565-9;\nRA   Erb R.W., Timmis K.N., Pieper D.H.;\nRT   \"Characterization of a gene cluster from Ralstonia eutropha JMP134 encoding\nRT   metabolism of 4-methylmuconolactone.\";\nRL   Gene 206:53-62(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, AND BIOPHYSICOCHEMICAL\nRP   PROPERTIES.\nRC   STRAIN=JMP134 / LMG 1197;\nRX   PubMed=2241929; DOI=10.1042/bj2710529;\nRA   Pieper D.H., Stadler-Fritzsche K., Knackmuss H.J., Engesser K.H.,\nRA   Bruce N.C., Cain R.B.;\nRT   \"Purification and characterization of 4-methylmuconolactone\nRT   methylisomerase, a novel enzyme of the modified 3-oxoadipate pathway in the\nRT   gram-negative bacterium Alcaligenes eutrophus JMP 134.\";\nRL   Biochem. J. 271:529-534(1990).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Isomerase involved in the degradation of 4-methylcatechol\nCC       (PubMed:2241929). Catalyzes the isomerization of the dead-end\nCC       metabolite 4-methylmuconolactone (4-ML) to 3-methylmuconolactone (3-\nCC       ML), which can then be further degraded through a modified 3-oxoadipate\nCC       pathway (PubMed:2241929, PubMed:9461415). Can also use 1-\nCC       methylbislactone, but not the isomeric methyl-substituted 4-\nCC       carboxymethylbut-2-en-4-olides (PubMed:2241929).\nCC       {ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-methylmuconolactone = 3-methylmuconolactone;\nCC         Xref=Rhea:RHEA:19237, ChEBI:CHEBI:57883, ChEBI:CHEBI:57888;\nCC         EC=5.4.99.14; Evidence={ECO:0000269|PubMed:2241929,\nCC         ECO:0000269|PubMed:9461415};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19238;\nCC         Evidence={ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0047469; F:4-carboxymethyl-4-methylbutenolide mutase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.847605+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac",
  "url": "https://rest.uniprot.org/unisave/O51799?format=txt&versions=65"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0016853\nname: isomerase activity\nnamespace: molecular_function\ndef: \"Catalysis of the geometric or structural changes within one molecule. Isomerase is the systematic name for any enzyme of EC class 5.\" [ISBN:0198506732]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nsynonym: \"other isomerase activity\" NARROW []\nxref: EC:5.-.-.-\nxref: Reactome:R-HSA-2161666 \"PGA2 is isomerised to PGC2\"\nxref: Reactome:R-HSA-2161735 \"PGC2 is isomerised to PGB2\"\nxref: Reactome:R-HSA-6787623 \"GFUS dimer epimerises GDP-DHDMan to GDP-KDGal\"\nis_a: GO:0003824 ! catalytic activity\nproperty_value: skos:exactMatch EC:5.-.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016853",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130892-130912",
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
  "excerpt": "[Term]\nid: GO:0016866\nname: intramolecular transferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a functional group from one position to another within a single molecule.\" [GOC:mah]\nsynonym: \"intramolecular transferase activity, transferring other groups\" NARROW []\nsynonym: \"mutase activity\" EXACT []\nxref: EC:5.4.-.-\nis_a: GO:0016853 ! isomerase activity\nproperty_value: skos:exactMatch EC:5.4.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016866",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 131035-131045",
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
  "excerpt": "[Term]\nid: GO:0019843\nname: rRNA binding\nnamespace: molecular_function\nalt_id: GO:0000944\ndef: \"Binding to a ribosomal RNA.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_yeast\nsynonym: \"base pairing with rRNA\" NARROW []\nis_a: GO:0003723 ! RNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019843",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 153826-153836",
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
  "excerpt": "[Term]\nid: GO:0030246\nname: carbohydrate binding\nnamespace: molecular_function\nalt_id: GO:0005529\ndef: \"Binding to a carbohydrate, which includes monosaccharides, oligosaccharides and polysaccharides as well as substances derived from monosaccharides by reduction of the carbonyl group (alditols), by oxidation of one or more hydroxy groups to afford the corresponding aldehydes, ketones, or carboxylic acids, or by replacement of one or more hydroxy group(s) by a hydrogen atom. Cyclitols are generally not regarded as carbohydrates.\" [GOC:mah]\nsubset: goslim_agr\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsynonym: \"selectin\" RELATED []\nsynonym: \"sugar binding\" EXACT []\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030246",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 164350-164367",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0047469\nname: 4-carboxymethyl-4-methylbutenolide mutase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 4-carboxymethyl-4-methylbut-2-en-1,4-olide = 4-carboxymethyl-3-methylbut-2-en-1,4-olide.\" [EC:5.4.99.14, RHEA:19237]\nsynonym: \"4-carboxymethyl-4-methylbut-2-en-1,4-olide methylmutase activity\" RELATED [EC:5.4.99.14]\nsynonym: \"4-methyl-2-enelactone isomerase activity\" RELATED [EC:5.4.99.14]\nsynonym: \"4-methyl-2-enelactone methyl-isomerase activity\" RELATED [EC:5.4.99.14]\nsynonym: \"4-methyl-3-enelactone methyl isomerase activity\" RELATED [EC:5.4.99.14]\nsynonym: \"4-methylmuconolactone methylisomerase activity\" RELATED [EC:5.4.99.14]\nxref: EC:5.4.99.14\nxref: KEGG_REACTION:R04510\nxref: MetaCyc:5.4.99.14-RXN\nxref: RHEA:19237\nis_a: GO:0016866 ! intramolecular transferase activity\nproperty_value: skos:exactMatch EC:5.4.99.14\nproperty_value: skos:exactMatch RHEA:19237\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0047469",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 290813-290830",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:1904047\nname: S-adenosyl-L-methionine binding\nnamespace: molecular_function\nalt_id: GO:0070283\ndef: \"Binding to S-adenosyl-L-methionine.\" [GO_REF:0000067, GOC:BHF, GOC:hal, GOC:TermGenie, PMID:22985361]\nsynonym: \"radical SAM enzyme activity\" NARROW []\nxref: Reactome:R-HSA-947535 \"Cyclisation of GTP to precursor Z\"\nis_a: GO:0043169 ! cation binding\nis_a: GO:1901681 ! sulfur compound binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1904047",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 516127-516137",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
