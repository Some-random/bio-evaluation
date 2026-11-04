# catalytic_activity_0163

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0163.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — O-phospho-L-serine + sulfite + H(+) = L-cysteate + phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKIDESLNVHSSLLQLIGNTPLLELHKITKGLKGRYFAKLEAFNVGHSAKDRVAKYIVEDAERKGLLKPGSTIVETSSGNTGYSLAMISALRGYRCIIAISDKSSHDKVEMLQALGAEVHLCPANVAPDDPRSYYEVAKRIHNETPNSIYVNQYFNPLNPESHYQTGREIWEQTQGEITHVVVCSGTGGTISGIAHYLKEQNPRVQVLGVDAYGSAIKKYHETREFDPAEVYPYKIEGIGKNLIPTATDFDVIDEFIKVTDKDAALMARKLARTEGLFMGYTSGAAIQAVKQYAEAGKFDENSIVVVLFADHGSRYMNKIYSDDWMKKQGFID

[Multiple Choices]
A. ATP + H2O = ADP + phosphate + H(+)
B. O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)
C. O-phospho-L-serine + sulfite + H(+) = L-cysteate + phosphate
D. L-tyrosine + H(+) = tyramine + CO2
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

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry identifies the protein as cysteate synthase and gives the reaction in choice C. The annotation cites experimental evidence (ECO:0000269); the archived entry also records the same reaction, though the cited paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a PLP-dependent sulfur-amino-acid synthase, and family-level recognition of a cysteine-synthase/O-phosphoserine sulfhydrylase-like enzyme provides a transferable route to favoring C: that family uses O-phosphoserine in sulfur incorporation, unlike the homoserine-plus-cysteine reaction in B. The sequence does not look like an ATP-hydrolysis enzyme, while D describes amino-acid decarboxylation rather than this synthase-family chemistry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference can meaningfully distinguish the offered reactions without recalling this exact protein's database record. The distinction between the related sulfur-amino-acid synthase alternatives is not guaranteed by generic PLP-enzyme features alone, so recognizing the relevant family is important.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options specify distinct reactions, and the supplied annotation supports C.


### Important caveats

- The family-level inference is probabilistic; the sequence alone does not establish the experimentally measured reaction with certainty.
- The reviewer-only annotation matches the supplied sequence, but its cited primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent sulfur-amino-acid synthase, and family-level recognition of a cysteine-synthase/O-phosphoserine sulfhydrylase-like enzyme provides a transferable route to favoring C: that family uses O-phosphoserine in sulfur incorporation, unlike the homoserine-plus-cysteine reaction in B. The sequence does not look like an ATP-hydrolysis enzyme, while D describes amino-acid decarboxylation rather than this synthase-family chemistry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can meaningfully distinguish the offered reactions without recalling this exact protein's database record. The distinction between the related sulfur-amino-acid synthase alternatives is not guaranteed by generic PLP-enzyme features alone, so recognizing the relevant family is important."
  },
  "case_id": "catalytic_activity_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry identifies the protein as cysteate synthase and gives the reaction in choice C. The annotation cites experimental evidence (ECO:0000269); the archived entry also records the same reaction, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The family-level inference is probabilistic; the sequence alone does not establish the experimentally measured reaction with certainty.",
    "The reviewer-only annotation matches the supplied sequence, but its cited primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options specify distinct reactions, and the supplied annotation supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry identifies the protein as cysteate synthase and gives the reaction in choice C. The annotation cites experimental evidence (ECO:0000269); the archived entry also records the same reaction, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent sulfur-amino-acid synthase, and family-level recognition of a cysteine-synthase/O-phosphoserine sulfhydrylase-like enzyme provides a transferable route to favoring C: that family uses O-phosphoserine in sulfur incorporation, unlike the homoserine-plus-cysteine reaction in B. The sequence does not look like an ATP-hydrolysis enzyme, while D describes amino-acid decarboxylation rather than this synthase-family chemistry.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can meaningfully distinguish the offered reactions without recalling this exact protein's database record. The distinction between the related sulfur-amino-acid synthase alternatives is not guaranteed by generic PLP-enzyme features alone, so recognizing the relevant family is important."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options specify distinct reactions, and the supplied annotation supports C."
  },
  "important_caveats": [
    "The family-level inference is probabilistic; the sequence alone does not establish the experimentally measured reaction with certainty.",
    "The reviewer-only annotation matches the supplied sequence, but its cited primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C7M8J5 (sequence SHA256 matched, 333 aa) annotates this protein as Cysteate synthase (EC 2.5.1.76) with catalytic activity 'O-phospho-L-serine + sulfite + H(+) = L-cysteate + phosphate', supported by experimental evidence (ECO:0000269, PubMed:35414181, Liu et al. Biochemistry 2022). This matches option C verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A chain of eliminations using transferable PLP-enzyme knowledge distinguishes C from the other options: (1) The motif 'SGTGGT' (residues ~137-142) is a hallmark of fold-type I PLP-dependent enzymes, immediately eliminating option A (ATPase, no PLP cofactor). (2) Fold-type I PLP enzymes include transferases and transaminases; tyrosine decarboxylases (option D) belong to fold-type III PLP enzymes with a fundamentally different active-site architecture and PLP-binding context, so the GGTGG-type motif argues against D. (3) Both B (cystathionine gamma-synthase, MetB, EC 2.5.1.48) and C (cysteate synthase, CapA, EC 2.5.1.76) are fold-type I PLP transferases with sulfur chemistry, so the fold argument alone does not separate them. However, bacterial MetB enzymes are typically 400–450 residues (e.g., E. coli MetB is 409 aa), whereas the supplied sequence is only 333 residues. This notable length shortfall is inconsistent with the canonical MetB architecture and more consistent with the smaller CapA family. (4) The remaining choice C is thus favored. The reasoning is probabilistic (a short MetB homolog cannot be strictly excluded by length alone) but provides a concrete, transferable basis for preferring C over B, A, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The reasoning relies on well-known transferable features: the GGTGG-type PLP-binding motif for fold-type I assignment, the fold-type distinction between transferases and decarboxylases, and the typical size range of MetB-family enzymes learned from multiple homologs. No fact unique to this exact protein's database record is required to eliminate A, D, and (probabilistically) B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B and C are both fold-type I PLP transferases involving sulfur nucleophiles, the 333-residue length is atypical for MetB (~400+ aa) and the elimination chain through fold type and size provides a meaningful preference for C. No other option is equally defensible after applying the PLP-fold and length arguments.


### Important caveats

- Cysteate synthase (CapA) was only experimentally characterized in 2022 (PubMed:35414181); it is a relatively new enzyme family, so a model's training exposure to CapA-specific sequence features may be limited. The reasoning here depends more on eliminating alternatives (A, D, B) than on positively recognizing CapA-specific motifs.
- The length argument against MetB is probabilistic: an unusually short MetB homolog could theoretically exist, though none are commonly documented at 333 aa.
- The sequence is 333 residues matching UniProt C7M8J5 (CapA_CAPOD, Capnocytophaga ochracea). Organism identity was not provided to the model and was not used in the reasoning chain.
- The experimental evidence (ECO:0000269) in the UniProt record confirms the catalytic activity assignment, but this annotation was reviewer-only and not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A chain of eliminations using transferable PLP-enzyme knowledge distinguishes C from the other options: (1) The motif 'SGTGGT' (residues ~137-142) is a hallmark of fold-type I PLP-dependent enzymes, immediately eliminating option A (ATPase, no PLP cofactor). (2) Fold-type I PLP enzymes include transferases and transaminases; tyrosine decarboxylases (option D) belong to fold-type III PLP enzymes with a fundamentally different active-site architecture and PLP-binding context, so the GGTGG-type motif argues against D. (3) Both B (cystathionine gamma-synthase, MetB, EC 2.5.1.48) and C (cysteate synthase, CapA, EC 2.5.1.76) are fold-type I PLP transferases with sulfur chemistry, so the fold argument alone does not separate them. However, bacterial MetB enzymes are typically 400–450 residues (e.g., E. coli MetB is 409 aa), whereas the supplied sequence is only 333 residues. This notable length shortfall is inconsistent with the canonical MetB architecture and more consistent with the smaller CapA family. (4) The remaining choice C is thus favored. The reasoning is probabilistic (a short MetB homolog cannot be strictly excluded by length alone) but provides a concrete, transferable basis for preferring C over B, A, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The reasoning relies on well-known transferable features: the GGTGG-type PLP-binding motif for fold-type I assignment, the fold-type distinction between transferases and decarboxylases, and the typical size range of MetB-family enzymes learned from multiple homologs. No fact unique to this exact protein's database record is required to eliminate A, D, and (probabilistically) B."
  },
  "case_id": "catalytic_activity_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C7M8J5 (sequence SHA256 matched, 333 aa) annotates this protein as Cysteate synthase (EC 2.5.1.76) with catalytic activity 'O-phospho-L-serine + sulfite + H(+) = L-cysteate + phosphate', supported by experimental evidence (ECO:0000269, PubMed:35414181, Liu et al. Biochemistry 2022). This matches option C verbatim."
  },
  "important_caveats": [
    "Cysteate synthase (CapA) was only experimentally characterized in 2022 (PubMed:35414181); it is a relatively new enzyme family, so a model's training exposure to CapA-specific sequence features may be limited. The reasoning here depends more on eliminating alternatives (A, D, B) than on positively recognizing CapA-specific motifs.",
    "The length argument against MetB is probabilistic: an unusually short MetB homolog could theoretically exist, though none are commonly documented at 333 aa.",
    "The sequence is 333 residues matching UniProt C7M8J5 (CapA_CAPOD, Capnocytophaga ochracea). Organism identity was not provided to the model and was not used in the reasoning chain.",
    "The experimental evidence (ECO:0000269) in the UniProt record confirms the catalytic activity assignment, but this annotation was reviewer-only and not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and C are both fold-type I PLP transferases involving sulfur nucleophiles, the 333-residue length is atypical for MetB (~400+ aa) and the elimination chain through fold type and size provides a meaningful preference for C. No other option is equally defensible after applying the PLP-fold and length arguments."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C7M8J5 (sequence SHA256 matched, 333 aa) annotates this protein as Cysteate synthase (EC 2.5.1.76) with catalytic activity 'O-phospho-L-serine + sulfite + H(+) = L-cysteate + phosphate', supported by experimental evidence (ECO:0000269, PubMed:35414181, Liu et al. Biochemistry 2022). This matches option C verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A chain of eliminations using transferable PLP-enzyme knowledge distinguishes C from the other options: (1) The motif 'SGTGGT' (residues ~137-142) is a hallmark of fold-type I PLP-dependent enzymes, immediately eliminating option A (ATPase, no PLP cofactor). (2) Fold-type I PLP enzymes include transferases and transaminases; tyrosine decarboxylases (option D) belong to fold-type III PLP enzymes with a fundamentally different active-site architecture and PLP-binding context, so the GGTGG-type motif argues against D. (3) Both B (cystathionine gamma-synthase, MetB, EC 2.5.1.48) and C (cysteate synthase, CapA, EC 2.5.1.76) are fold-type I PLP transferases with sulfur chemistry, so the fold argument alone does not separate them. However, bacterial MetB enzymes are typically 400–450 residues (e.g., E. coli MetB is 409 aa), whereas the supplied sequence is only 333 residues. This notable length shortfall is inconsistent with the canonical MetB architecture and more consistent with the smaller CapA family. (4) The remaining choice C is thus favored. The reasoning is probabilistic (a short MetB homolog cannot be strictly excluded by length alone) but provides a concrete, transferable basis for preferring C over B, A, and D.",
    "missing_item_specific_fact": "",
    "reason": "The reasoning relies on well-known transferable features: the GGTGG-type PLP-binding motif for fold-type I assignment, the fold-type distinction between transferases and decarboxylases, and the typical size range of MetB-family enzymes learned from multiple homologs. No fact unique to this exact protein's database record is required to eliminate A, D, and (probabilistically) B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and C are both fold-type I PLP transferases involving sulfur nucleophiles, the 333-residue length is atypical for MetB (~400+ aa) and the elimination chain through fold type and size provides a meaningful preference for C. No other option is equally defensible after applying the PLP-fold and length arguments."
  },
  "important_caveats": [
    "Cysteate synthase (CapA) was only experimentally characterized in 2022 (PubMed:35414181); it is a relatively new enzyme family, so a model's training exposure to CapA-specific sequence features may be limited. The reasoning here depends more on eliminating alternatives (A, D, B) than on positively recognizing CapA-specific motifs.",
    "The length argument against MetB is probabilistic: an unusually short MetB homolog could theoretically exist, though none are commonly documented at 333 aa.",
    "The sequence is 333 residues matching UniProt C7M8J5 (CapA_CAPOD, Capnocytophaga ochracea). Organism identity was not provided to the model and was not used in the reasoning chain.",
    "The experimental evidence (ECO:0000269) in the UniProt record confirms the catalytic activity assignment, but this annotation was reviewer-only and not available to the evaluated model."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 163. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
