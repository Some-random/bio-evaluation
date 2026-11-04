# pathway_0099

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0099.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Antibiotic biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNTQPLERALAAFREVLGTAHVSTDESARAAAETATFATTHRIPAIISPGSAAEVEACVRIAREHGVPLYPVSTGKNWGYGSRVPTSDGAIVLSLARMNRILDFNEELAYVAIEPGVTMRQLVAYLNDRGSRLMLSVTGSTPDSSVVGNICDRGFGAGVNAERIAHICNIEVVLPNGERLNTGFGRFPGAQTASIHRWGIGPQLDGLFTQSNLGIVTRMTIWLAPRPRHHEIFYFRLRDERRVEAVTDIIRDLKLQGLPRASVSLWNDYKLVSMKGQYPWQEAAGKTPLPEALLAKLRRAWGGAAWLGGGAILAASQDQIAAERAVIRKALHPHVDKLSFVGQRAARVARLLQRPVQRLTGFDLSEVVRAYEQSPHLGIPMERNIRSAYWRKKAPPPEQTDPDRDRCGAIWLAPAVPSTGKHVGTALRIVRERALAHAFEPGISVIFATERCANIVVALMYDRELPGEDGRAMACYQDIFDRLAAQGYLPYRLGIQSQSALPAAQSSYGTVVGALKRALDPDDILAPGRYDFRHEWPPADN

[Multiple Choices]
A. Antibiotic biosynthesis. .
B. Cell wall degradation
C. Protein biosynthesis
D. Protein modification
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

> The supplied sequence exactly matches the sequence in the reviewed UniProt record. That record assigns the protein to antibiotic biosynthesis and identifies it as a decarboxylase involved in chondrochloren biosynthesis; the pathway annotation cites experimental evidence and published work on the enzyme and pathway.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's specific role as a decarboxylase in the chondrochloren antibiotic biosynthetic pathway, or equivalent evidence linking it to that biosynthetic gene cluster.


**Reason**

> The sequence is consistent with a soluble enzyme, but that alone does not meaningfully distinguish antibiotic biosynthesis from the other offered pathway categories. No clear transferable family or sequence feature in the input establishes its specific pathway role; the pathway assignment depends on protein-specific functional or gene-cluster information absent from the prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein-specific evidence supports A, and the other choices are not equally supported by the supplied evidence.


### Important caveats

- The pathway annotation is supported by cited experimental literature, but the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific role as a decarboxylase in the chondrochloren antibiotic biosynthetic pathway, or equivalent evidence linking it to that biosynthetic gene cluster.",
    "reason": "The sequence is consistent with a soluble enzyme, but that alone does not meaningfully distinguish antibiotic biosynthesis from the other offered pathway categories. No clear transferable family or sequence feature in the input establishes its specific pathway role; the pathway assignment depends on protein-specific functional or gene-cluster information absent from the prompt."
  },
  "case_id": "pathway_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the reviewed UniProt record. That record assigns the protein to antibiotic biosynthesis and identifies it as a decarboxylase involved in chondrochloren biosynthesis; the pathway annotation cites experimental evidence and published work on the enzyme and pathway."
  },
  "important_caveats": [
    "The pathway annotation is supported by cited experimental literature, but the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports A, and the other choices are not equally supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the reviewed UniProt record. That record assigns the protein to antibiotic biosynthesis and identifies it as a decarboxylase involved in chondrochloren biosynthesis; the pathway annotation cites experimental evidence and published work on the enzyme and pathway.",
    "evidence_ids": ["C4", "C5", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's specific role as a decarboxylase in the chondrochloren antibiotic biosynthetic pathway, or equivalent evidence linking it to that biosynthetic gene cluster.",
    "reason": "The sequence is consistent with a soluble enzyme, but that alone does not meaningfully distinguish antibiotic biosynthesis from the other offered pathway categories. No clear transferable family or sequence feature in the input establishes its specific pathway role; the pathway assignment depends on protein-specific functional or gene-cluster information absent from the prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports A, and the other choices are not equally supported by the supplied evidence."
  },
  "important_caveats": [
    "The pathway annotation is supported by cited experimental literature, but the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B9ZUK6 annotates this protein (CndG, 1'-carboxy-chondrochloren decarboxylase, EC 4.1.1.129) with PATHWAY: 'Antibiotic biosynthesis' supported by experimental evidence (ECO:0000269|PubMed:20080978) and curated assignment (ECO:0000305|PubMed:19171307). The protein catalyzes a step in the biosynthesis of chondrochlorens, which are antibiotic compounds produced by Chondromyces crocatus. The sequence matches the benchmark exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks hallmarks of cell wall degradation enzymes (no glycoside hydrolase motifs, no lysozyme/transglycosylase domains, no peptidase catalytic triads typical of autolysins) — eliminating B. It lacks ribosomal protein features, tRNA synthetase motifs, or translation factor domains — eliminating C. It lacks kinase, methyltransferase, ubiquitin-ligase, or acetyltransferase motifs that characterize protein-modification enzymes — eliminating D. The sequence is consistent with a small-molecule metabolic enzyme (decarboxylase-like fold with substrate-binding and catalytic residues). Among the four offered pathways, a specialized small-molecule metabolic enzyme (particularly an unusual oxidative decarboxylase acting on an aromatic intermediate) is most plausibly assigned to antibiotic biosynthesis, as secondary/specialized metabolic pathways are the primary home of such unusual enzymatic transformations. This is an elimination-based inference: the protein clearly does not fit B, C, or D, leaving A as the best-supported option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination argument is concrete: the sequence visibly lacks domains characteristic of glycosidases/lysozymes (B), translation machinery (C), or protein-modifying enzymes (D). Recognizing it as a small-molecule metabolic enzyme (likely a decarboxylase) and placing it in the pathway category that handles specialized secondary metabolites (antibiotic biosynthesis) is a defensible transfer inference from general enzymology and pathway classification knowledge. The inference is probabilistic rather than certain, but it meaningfully distinguishes A from the other three options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are sufficiently distinct in functional category that elimination reasoning clearly removes B, C, and D. No other pathway (e.g., central carbon metabolism, amino acid biosynthesis) is offered as a competing alternative, so A stands as the only viable choice after elimination.


### Important caveats

- The positive identification of 'antibiotic biosynthesis' specifically (rather than, e.g., 'aromatic amino acid metabolism') relies primarily on elimination of the other three options rather than on a unique sequence signature for antibiotic pathways.
- The protein's unusual oxidative decarboxylase mechanism (EC 4.1.1.129) is itself rare and often associated with specialized metabolism, which supports the antibiotic biosynthesis assignment but is not a definitive sequence-level signature.
- Knowledge of the organism (Chondromyces crocatus, a myxobacterium prolific in antibiotic production) or gene-cluster context would strengthen the assignment, but neither is provided in the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks hallmarks of cell wall degradation enzymes (no glycoside hydrolase motifs, no lysozyme/transglycosylase domains, no peptidase catalytic triads typical of autolysins) — eliminating B. It lacks ribosomal protein features, tRNA synthetase motifs, or translation factor domains — eliminating C. It lacks kinase, methyltransferase, ubiquitin-ligase, or acetyltransferase motifs that characterize protein-modification enzymes — eliminating D. The sequence is consistent with a small-molecule metabolic enzyme (decarboxylase-like fold with substrate-binding and catalytic residues). Among the four offered pathways, a specialized small-molecule metabolic enzyme (particularly an unusual oxidative decarboxylase acting on an aromatic intermediate) is most plausibly assigned to antibiotic biosynthesis, as secondary/specialized metabolic pathways are the primary home of such unusual enzymatic transformations. This is an elimination-based inference: the protein clearly does not fit B, C, or D, leaving A as the best-supported option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination argument is concrete: the sequence visibly lacks domains characteristic of glycosidases/lysozymes (B), translation machinery (C), or protein-modifying enzymes (D). Recognizing it as a small-molecule metabolic enzyme (likely a decarboxylase) and placing it in the pathway category that handles specialized secondary metabolites (antibiotic biosynthesis) is a defensible transfer inference from general enzymology and pathway classification knowledge. The inference is probabilistic rather than certain, but it meaningfully distinguishes A from the other three options."
  },
  "case_id": "pathway_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B9ZUK6 annotates this protein (CndG, 1'-carboxy-chondrochloren decarboxylase, EC 4.1.1.129) with PATHWAY: 'Antibiotic biosynthesis' supported by experimental evidence (ECO:0000269|PubMed:20080978) and curated assignment (ECO:0000305|PubMed:19171307). The protein catalyzes a step in the biosynthesis of chondrochlorens, which are antibiotic compounds produced by Chondromyces crocatus. The sequence matches the benchmark exactly."
  },
  "important_caveats": [
    "The positive identification of 'antibiotic biosynthesis' specifically (rather than, e.g., 'aromatic amino acid metabolism') relies primarily on elimination of the other three options rather than on a unique sequence signature for antibiotic pathways.",
    "The protein's unusual oxidative decarboxylase mechanism (EC 4.1.1.129) is itself rare and often associated with specialized metabolism, which supports the antibiotic biosynthesis assignment but is not a definitive sequence-level signature.",
    "Knowledge of the organism (Chondromyces crocatus, a myxobacterium prolific in antibiotic production) or gene-cluster context would strengthen the assignment, but neither is provided in the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct in functional category that elimination reasoning clearly removes B, C, and D. No other pathway (e.g., central carbon metabolism, amino acid biosynthesis) is offered as a competing alternative, so A stands as the only viable choice after elimination."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"pathway_0099","expected_answer_check":{"judgment":"supported","reason":"The UniProt entry B9ZUK6 annotates this protein (CndG, 1'-carboxy-chondrochloren decarboxylase, EC 4.1.1.129) with PATHWAY: 'Antibiotic biosynthesis' supported by experimental evidence (ECO:0000269|PubMed:20080978) and curated assignment (ECO:0000305|PubMed:19171307). The protein catalyzes a step in the biosynthesis of chondrochlorens, which are antibiotic compounds produced by Chondromyces crocatus. The sequence matches the benchmark exactly.","evidence_ids":["C4","C5","C6","C7","H4"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The sequence lacks hallmarks of cell wall degradation enzymes (no glycoside hydrolase motifs, no lysozyme/transglycosylase domains, no peptidase catalytic triads typical of autolysins) — eliminating B. It lacks ribosomal protein features, tRNA synthetase motifs, or translation factor domains — eliminating C. It lacks kinase, methyltransferase, ubiquitin-ligase, or acetyltransferase motifs that characterize protein-modification enzymes — eliminating D. The sequence is consistent with a small-molecule metabolic enzyme (decarboxylase-like fold with substrate-binding and catalytic residues). Among the four offered pathways, a specialized small-molecule metabolic enzyme (particularly an unusual oxidative decarboxylase acting on an aromatic intermediate) is most plausibly assigned to antibiotic biosynthesis, as secondary/specialized metabolic pathways are the primary home of such unusual enzymatic transformations. This is an elimination-based inference: the protein clearly does not fit B, C, or D, leaving A as the best-supported option.","missing_item_specific_fact":"","reason":"The elimination argument is concrete: the sequence visibly lacks domains characteristic of glycosidases/lysozymes (B), translation machinery (C), or protein-modifying enzymes (D). Recognizing it as a small-molecule metabolic enzyme (likely a decarboxylase) and placing it in the pathway category that handles specialized secondary metabolites (antibiotic biosynthesis) is a defensible transfer inference from general enzymology and pathway classification knowledge. The inference is probabilistic rather than certain, but it meaningfully distinguishes A from the other three options."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"The four options are sufficiently distinct in functional category that elimination reasoning clearly removes B, C, and D. No other pathway (e.g., central carbon metabolism, amino acid biosynthesis) is offered as a competing alternative, so A stands as the only viable choice after elimination."},"important_caveats":["The positive identification of 'antibiotic biosynthesis' specifically (rather than, e.g., 'aromatic amino acid metabolism') relies primarily on elimination of the other three options rather than on a unique sequence signature for antibiotic pathways.","The protein's unusual oxidative decarboxylase mechanism (EC 4.1.1.129) is itself rare and often associated with specialized metabolism, which supports the antibiotic biosynthesis assignment but is not a definitive sequence-level signature.","Knowledge of the organism (Chondromyces crocatus, a myxobacterium prolific in antibiotic production) or gene-cluster context would strengthen the assignment, but neither is provided in the original input."]}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 541,
  "benchmark_sequence_sha256": "10620a06bbc0e32940892848fc0f774fc31cefc9e778f3b2f6ed6a95426db921",
  "current_entry_audit": {
    "entryVersion": 63,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-04-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 541,
  "current_source_sequence_sha256": "10620a06bbc0e32940892848fc0f774fc31cefc9e778f3b2f6ed6a95426db921",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 61,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B9ZUK6",
  "selected_historical_entry_version": 61,
  "selected_historical_record_sha256": "f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de",
  "selected_historical_source_sequence_length": 541,
  "selected_historical_source_sequence_sha256": "10620a06bbc0e32940892848fc0f774fc31cefc9e778f3b2f6ed6a95426db921",
  "selected_historical_version": {
    "accession": "B9ZUK6",
    "database": "Swiss-Prot",
    "entryVersion": 61,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CNDG_CHOCO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B9ZUK6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:01.455195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56",
  "url": "https://rest.uniprot.org/uniprotkb/B9ZUK6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":63,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-04-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:01.455195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56",
  "url": "https://rest.uniprot.org/uniprotkb/B9ZUK6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Myxococcota\",\"Polyangia\",\"Polyangiales\",\"Polyangiaceae\",\"Chondromyces\"],\"scientificName\":\"Chondromyces crocatus\",\"taxonId\":52}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:01.455195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56",
  "url": "https://rest.uniprot.org/uniprotkb/B9ZUK6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20080978\",\"source\":\"PubMed\"}],\"value\":\"Oxidative decarboxylase CndG\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20080978\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.129\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1'-carboxy-chondrochloren decarboxylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:01.455195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56",
  "url": "https://rest.uniprot.org/uniprotkb/B9ZUK6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20080978\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19171307\",\"source\":\"PubMed\"}],\"value\":\"Antibiotic biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:25:01.455195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56",
  "url": "https://rest.uniprot.org/uniprotkb/B9ZUK6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Rachid S.\",\"Scharfe M.\",\"Bloecker H.\",\"Weissman K.J.\",\"Mueller R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19171307\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.chembiol.2008.11.005\"}],\"citationType\":\"journal article\",\"firstPage\":\"70\",\"id\":\"19171307\",\"journal\":\"Chem. Biol.\",\"lastPage\":\"81\",\"publicationDate\":\"2009\",\"title\":\"Unusual chemistry in the biosynthesis of the antibiotic chondrochlorens.\",\"volume\":\"16\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAQ43085.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 14714 / JCM 12616 / Cm c5\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"GENE CLUSTER\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:01.455195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56",
  "url": "https://rest.uniprot.org/uniprotkb/B9ZUK6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Rachid S.\",\"Revermann O.\",\"Dauth C.\",\"Kazmaier U.\",\"Mueller R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20080978\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.079707\"}],\"citationType\":\"journal article\",\"firstPage\":\"12482\",\"id\":\"20080978\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"12489\",\"publicationDate\":\"2010\",\"title\":\"Characterization of a novel type of oxidative decarboxylase involved in the biosynthesis of the styryl moiety of chondrochloren from an acylated tyrosine.\",\"volume\":\"285\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 14714 / JCM 12616 / Cm c5\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"MASS SPECTROMETRY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:01.455195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56",
  "url": "https://rest.uniprot.org/uniprotkb/B9ZUK6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H1",
  "excerpt": "ID   CNDG_CHOCO              Reviewed;         541 AA.\nAC   B9ZUK6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-APR-2009, sequence version 1.\nDT   28-JAN-2026, entry version 61.\nDE   RecName: Full=1'-carboxy-chondrochloren decarboxylase {ECO:0000305};\nDE            EC=4.1.1.129 {ECO:0000269|PubMed:20080978};\nDE   AltName: Full=Oxidative decarboxylase CndG {ECO:0000303|PubMed:20080978};\nGN   Name=cndG {ECO:0000303|PubMed:19171307};\nGN   ORFNames=CMC5_053350 {ECO:0000312|EMBL:AKT41174.1};\nOS   Chondromyces crocatus.\nOC   Bacteria; Pseudomonadati; Myxococcota; Polyangia; Polyangiales;\nOC   Polyangiaceae; Chondromyces.\nOX   NCBI_TaxID=52;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.921419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de",
  "url": "https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAQ43085.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], GENE CLUSTER, AND PATHWAY.\nRC   STRAIN=DSM 14714 / JCM 12616 / Cm c5;\nRX   PubMed=19171307; DOI=10.1016/j.chembiol.2008.11.005;\nRA   Rachid S., Scharfe M., Bloecker H., Weissman K.J., Mueller R.;\nRT   \"Unusual chemistry in the biosynthesis of the antibiotic chondrochlorens.\";\nRL   Chem. Biol. 16:70-81(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.921419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de",
  "url": "https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, PATHWAY, MASS SPECTROMETRY, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=DSM 14714 / JCM 12616 / Cm c5;\nRX   PubMed=20080978; DOI=10.1074/jbc.m109.079707;\nRA   Rachid S., Revermann O., Dauth C., Kazmaier U., Mueller R.;\nRT   \"Characterization of a novel type of oxidative decarboxylase involved in\nRT   the biosynthesis of the styryl moiety of chondrochloren from an acylated\nRT   tyrosine.\";\nRL   J. Biol. Chem. 285:12482-12489(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.921419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de",
  "url": "https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Antibiotic biosynthesis. {ECO:0000269|PubMed:20080978,\nCC       ECO:0000305|PubMed:19171307}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:55.921419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de",
  "url": "https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
