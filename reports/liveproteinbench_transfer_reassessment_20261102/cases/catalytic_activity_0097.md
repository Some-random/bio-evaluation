# catalytic_activity_0097

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0097.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKEIKIQNIIINEEKAPLVVPEIGINHNGSLELAKIMVDAAFSAGAKIIKHQTHIVEDEMSKAAKKVIPGNAKISIYEIMQKCALDYKDELALKEYTEKLGLVYLSTPFSRAGANRLEDMGVSAFKIGSGECNNYPLIKHIAAFKKPMIVSTGMNSIESIKPTVKILLDNEIPFVLMHTTNLYPTPHNLVRLNAMLELKKEFSCMVGLSDHTTDNLACLGAVALGACVLERHFTDSMDRSGPDIVCSMDTKALKELIMQSEQMAIMRGNNESKKAAKQEQVTIDFAFASVVSIKDIKKGEVLSMDNIWVKRPGLGGISAAEFENILGKKALRDIENDTQLSYEDFA

[Multiple Choices]
A. L-dopa + H(+) = dopamine + CO2
B. isopentadecanoyl-CoA + L-cysteate + H(+) = 3-oxocapnine + CO2 + CoA
C. (19E)-geissoschizine + NADPH + H(+) = (16R,19E)-isositsirikine + NADP(+)
D. N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate
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

> The sequence matches the annotated protein sequence, and the historical UniProt record assigns it the reaction in D with experimental evidence cited to a publication. This supports the key, though the primary paper was not independently reviewed here.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the NeuB/N-acetylneuraminate-synthase family, whose members catalyze formation of N-acetylneuraminate from N-acetylmannosamine and phosphoenolpyruvate. That family-level connection meaningfully distinguishes D from the unrelated decarboxylation, specialized CoA-dependent, and NADPH-dependent transformations in A–C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing a shared enzyme-family sequence pattern and transferring the family’s characteristic chemistry is a credible route to selecting D without knowing this exact protein’s database entry. The sequence-based inference is not by itself experimental proof.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reaction in D is the one associated with the inferred enzyme family; the other options describe distinct enzyme activities.


### Important caveats

- The support evidence is a database annotation citing experimental evidence; the cited primary study was not independently assessed.
- The reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the NeuB/N-acetylneuraminate-synthase family, whose members catalyze formation of N-acetylneuraminate from N-acetylmannosamine and phosphoenolpyruvate. That family-level connection meaningfully distinguishes D from the unrelated decarboxylation, specialized CoA-dependent, and NADPH-dependent transformations in A–C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing a shared enzyme-family sequence pattern and transferring the family’s characteristic chemistry is a credible route to selecting D without knowing this exact protein’s database entry. The sequence-based inference is not by itself experimental proof."
  },
  "case_id": "catalytic_activity_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein sequence, and the historical UniProt record assigns it the reaction in D with experimental evidence cited to a publication. This supports the key, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The support evidence is a database annotation citing experimental evidence; the cited primary study was not independently assessed.",
    "The reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction in D is the one associated with the inferred enzyme family; the other options describe distinct enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein sequence, and the historical UniProt record assigns it the reaction in D with experimental evidence cited to a publication. This supports the key, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["H4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the NeuB/N-acetylneuraminate-synthase family, whose members catalyze formation of N-acetylneuraminate from N-acetylmannosamine and phosphoenolpyruvate. That family-level connection meaningfully distinguishes D from the unrelated decarboxylation, specialized CoA-dependent, and NADPH-dependent transformations in A–C.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing a shared enzyme-family sequence pattern and transferring the family’s characteristic chemistry is a credible route to selecting D without knowing this exact protein’s database entry. The sequence-based inference is not by itself experimental proof."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction in D is the one associated with the inferred enzyme family; the other options describe distinct enzyme activities."
  },
  "important_caveats": [
    "The support evidence is a database annotation citing experimental evidence; the cited primary study was not independently assessed.",
    "The reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DY06 (sequence matched, 346 aa) is annotated as N-acetylneuraminate synthase (EC 2.5.1.56) with experimental evidence (ECO:0000269, PubMed:38382015). The catalytic activity recorded is exactly: N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate, matching option D verbatim. The evidence is from a 2024 Biochemistry paper (Ghosh & Raushel) providing experimental characterization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region 'MVDAAFSAGAKIIKHQTHIVEDEMSKAAKK' (approximately residues 27-57) is a highly conserved motif shared across multiple bacterial NeuB (sialic acid synthase) homologs, including E. coli NeuB and other bacterial Neu5Ac synthases. Recognizing this family-level signature allows inference that the protein belongs to the sialic acid synthase family, whose canonical reaction is the aldol-type condensation of N-acetyl-D-mannosamine with phosphoenolpyruvate to yield N-acetylneuraminate. This directly matches option D. Additionally, the sequence lacks PLP-binding motifs (no lysine in the characteristic Schiff-base-forming context expected for DOPA decarboxylase, ruling out A), lacks a canonical Rossmann fold (GxGxxG) expected for an NADPH-dependent reductase (ruling out C), and option B describes an extremely obscure reaction with no recognizable enzyme family signature in the sequence. The overall length (~346 aa) is also consistent with bacterial NeuB rather than the vertebrate NANS (~355 aa, different fold).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The conserved 'MVDAAFSAGAKIIKHQTHIVEDEMSKAAKK' motif is a transferable family-level feature recognized across multiple NeuB homologs from different bacterial species. This allows a knowledgeable model to identify the sialic acid synthase family and its canonical reaction without needing to look up the specific UniProt accession for this exact protein. The other options can be excluded by absence of corresponding structural/functional motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level motif recognition points unambiguously to option D. Option A requires PLP-dependent enzyme features absent here; option C requires a Rossmann fold absent here; option B describes an extremely unusual reaction with no corresponding sequence signature. No two options are equally defensible given the sequence features.


### Important caveats

- The conserved N-terminal motif recognition relies on the model having learned NeuB family sequences from training data; the strength of this inference depends on the model's exposure to multiple NeuB homologs.
- Option B is so obscure that it likely serves as a pure distractor with no realistic biological counterpart in standard enzyme databases, making it trivially excludable.
- The evidence for the catalytic activity is experimental (ECO:0000269) from a 2024 publication, providing strong support for the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'MVDAAFSAGAKIIKHQTHIVEDEMSKAAKK' (approximately residues 27-57) is a highly conserved motif shared across multiple bacterial NeuB (sialic acid synthase) homologs, including E. coli NeuB and other bacterial Neu5Ac synthases. Recognizing this family-level signature allows inference that the protein belongs to the sialic acid synthase family, whose canonical reaction is the aldol-type condensation of N-acetyl-D-mannosamine with phosphoenolpyruvate to yield N-acetylneuraminate. This directly matches option D. Additionally, the sequence lacks PLP-binding motifs (no lysine in the characteristic Schiff-base-forming context expected for DOPA decarboxylase, ruling out A), lacks a canonical Rossmann fold (GxGxxG) expected for an NADPH-dependent reductase (ruling out C), and option B describes an extremely obscure reaction with no recognizable enzyme family signature in the sequence. The overall length (~346 aa) is also consistent with bacterial NeuB rather than the vertebrate NANS (~355 aa, different fold).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The conserved 'MVDAAFSAGAKIIKHQTHIVEDEMSKAAKK' motif is a transferable family-level feature recognized across multiple NeuB homologs from different bacterial species. This allows a knowledgeable model to identify the sialic acid synthase family and its canonical reaction without needing to look up the specific UniProt accession for this exact protein. The other options can be excluded by absence of corresponding structural/functional motifs."
  },
  "case_id": "catalytic_activity_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DY06 (sequence matched, 346 aa) is annotated as N-acetylneuraminate synthase (EC 2.5.1.56) with experimental evidence (ECO:0000269, PubMed:38382015). The catalytic activity recorded is exactly: N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate, matching option D verbatim. The evidence is from a 2024 Biochemistry paper (Ghosh & Raushel) providing experimental characterization."
  },
  "important_caveats": [
    "The conserved N-terminal motif recognition relies on the model having learned NeuB family sequences from training data; the strength of this inference depends on the model's exposure to multiple NeuB homologs.",
    "Option B is so obscure that it likely serves as a pure distractor with no realistic biological counterpart in standard enzyme databases, making it trivially excludable.",
    "The evidence for the catalytic activity is experimental (ECO:0000269) from a 2024 publication, providing strong support for the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level motif recognition points unambiguously to option D. Option A requires PLP-dependent enzyme features absent here; option C requires a Rossmann fold absent here; option B describes an extremely unusual reaction with no corresponding sequence signature. No two options are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DY06 (sequence matched, 346 aa) is annotated as N-acetylneuraminate synthase (EC 2.5.1.56) with experimental evidence (ECO:0000269, PubMed:38382015). The catalytic activity recorded is exactly: N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate, matching option D verbatim. The evidence is from a 2024 Biochemistry paper (Ghosh & Raushel) providing experimental characterization.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region 'MVDAAFSAGAKIIKHQTHIVEDEMSKAAKK' (approximately residues 27-57) is a highly conserved motif shared across multiple bacterial NeuB (sialic acid synthase) homologs, including E. coli NeuB and other bacterial Neu5Ac synthases. Recognizing this family-level signature allows inference that the protein belongs to the sialic acid synthase family, whose canonical reaction is the aldol-type condensation of N-acetyl-D-mannosamine with phosphoenolpyruvate to yield N-acetylneuraminate. This directly matches option D. Additionally, the sequence lacks PLP-binding motifs (no lysine in the characteristic Schiff-base-forming context expected for DOPA decarboxylase, ruling out A), lacks a canonical Rossmann fold (GxGxxG) expected for an NADPH-dependent reductase (ruling out C), and option B describes an extremely obscure reaction with no recognizable enzyme family signature in the sequence. The overall length (~346 aa) is also consistent with bacterial NeuB rather than the vertebrate NANS (~355 aa, different fold).",
    "missing_item_specific_fact": "",
    "reason": "The conserved 'MVDAAFSAGAKIIKHQTHIVEDEMSKAAKK' motif is a transferable family-level feature recognized across multiple NeuB homologs from different bacterial species. This allows a knowledgeable model to identify the sialic acid synthase family and its canonical reaction without needing to look up the specific UniProt accession for this exact protein. The other options can be excluded by absence of corresponding structural/functional motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level motif recognition points unambiguously to option D. Option A requires PLP-dependent enzyme features absent here; option C requires a Rossmann fold absent here; option B describes an extremely unusual reaction with no corresponding sequence signature. No two options are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The conserved N-terminal motif recognition relies on the model having learned NeuB family sequences from training data; the strength of this inference depends on the model's exposure to multiple NeuB homologs.",
    "Option B is so obscure that it likely serves as a pure distractor with no realistic biological counterpart in standard enzyme databases, making it trivially excludable.",
    "The evidence for the catalytic activity is experimental (ECO:0000269) from a 2024 publication, providing strong support for the annotation."
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
  "benchmark_sequence_length": 346,
  "benchmark_sequence_sha256": "8542949467c46c0d10eb516705d760b1c4148a32078df1045ffb85da51143601",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 346,
  "current_source_sequence_sha256": "8542949467c46c0d10eb516705d760b1c4148a32078df1045ffb85da51143601",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DY06",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0",
  "selected_historical_source_sequence_length": 346,
  "selected_historical_source_sequence_sha256": "8542949467c46c0d10eb516705d760b1c4148a32078df1045ffb85da51143601",
  "selected_historical_version": {
    "accession": "P0DY06",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NEUAS_CAMJ8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DY06\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC 11828)\",\"taxonId\":407148}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.56\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"N-acetylneuraminate synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Neu5Ac synthase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:19274\"}}],\"reaction\":{\"ecNumber\":\"2.5.1.56\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"name\":\"N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-acetylneuraminate + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19273\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35418\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58702\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:63153\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"81116 / NCTC 11828\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   NEUAS_CAMJ8             Reviewed;         346 AA.\nAC   P0DY06;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};\nDE            Short=Neu5Ac synthase {ECO:0000303|PubMed:38382015};\nDE            EC=2.5.1.56 {ECO:0000269|PubMed:38382015};\nGN   Name=HS6.11 {ECO:0000303|PubMed:38382015};\nGN   OrderedLocusNames=C8J_1339 {ECO:0000312|EMBL:ABV52937.1};\nOS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC\nOS   11828).\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=407148;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:07.414593+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0",
  "url": "https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};\nDE            Short=Neu5Ac synthase {ECO:0000303|PubMed:38382015};\nDE            EC=2.5.1.56 {ECO:0000269|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:07.414593+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0",
  "url": "https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=81116 / NCTC 11828;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:07.414593+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0",
  "url": "https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-acetyl-D-mannosamine + phosphoenolpyruvate + H2O = N-\nCC         acetylneuraminate + phosphate; Xref=Rhea:RHEA:19273,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:35418, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:58702, ChEBI:CHEBI:63153; EC=2.5.1.56;\nCC         Evidence={ECO:0000269|PubMed:38382015};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19274;\nCC         Evidence={ECO:0000269|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:07.414593+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0",
  "url": "https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
