# pathway_0010

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0010.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Antifungal biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLHLTPLIFLSLAMAAAVGVWGVFTWNGGFDEMDGIVASHQSTGILGLQHCPDLDRGLMSMVAFNLPVVGRNPIFPAGRRFMVQFLANVAVIPVILNTEGARAEPGSLVRYSTTWGLFSQMATSAVMCPLYGFWFVRQSGAKQTEGGTLRPLPPNKWVVPSSVLIGYGIPALLSFDPFQWGLDLQIRGILAFTLYPLCISLTARLMRKVSKKRGRSLSPEWNSTISYVAVGVVGMVSHLWYLGTGLTGYPLSGDAVSSVAGPTEVGRAAQLVLLFLQIDYVITFAAMLLLAWHELTRHQLVRSWRAAGTLAVGWLFLGPGATLAAAWALREQWLSRPRGVRGEIKQKPK

[Multiple Choices]
A. polypeptide chain elongation. .
B. Antifungal biosynthesis. .
C. tetrahydrofolate interconversion. .
D. Purine metabolism
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

> A sequence-matched UniProt annotation assigns the protein to antifungal biosynthesis and cites experimental evidence (ECO:0000269). This supports B, though the cited study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and appears to encode a multipass membrane protein. That makes a ribosomal elongation role and many typical folate- or purine-metabolism enzymes less plausible, but it does not specifically indicate antifungal biosynthesis.


**Missing item-specific fact**

> The sequence's membership and role in an antifungal biosynthetic pathway are not supplied; establishing that association requires target-specific annotation or evidence.


**Reason**

> The sequence offers a weak filter against some alternatives, but no recognizable family feature or pathway-specific motif meaningfully distinguishes antifungal biosynthesis from the listed choices. The decisive pathway association is a fact about this protein not inferable from the provided context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied source annotation supports B; no competing option is supported by the available evidence.


### Important caveats

- The source annotation is sequence-matched and cites experimental evidence, but the cited primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and appears to encode a multipass membrane protein. That makes a ribosomal elongation role and many typical folate- or purine-metabolism enzymes less plausible, but it does not specifically indicate antifungal biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's membership and role in an antifungal biosynthetic pathway are not supplied; establishing that association requires target-specific annotation or evidence.",
    "reason": "The sequence offers a weak filter against some alternatives, but no recognizable family feature or pathway-specific motif meaningfully distinguishes antifungal biosynthesis from the listed choices. The decisive pathway association is a fact about this protein not inferable from the provided context."
  },
  "case_id": "pathway_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "A sequence-matched UniProt annotation assigns the protein to antifungal biosynthesis and cites experimental evidence (ECO:0000269). This supports B, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The source annotation is sequence-matched and cites experimental evidence, but the cited primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied source annotation supports B; no competing option is supported by the available evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "A sequence-matched UniProt annotation assigns the protein to antifungal biosynthesis and cites experimental evidence (ECO:0000269). This supports B, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and appears to encode a multipass membrane protein. That makes a ribosomal elongation role and many typical folate- or purine-metabolism enzymes less plausible, but it does not specifically indicate antifungal biosynthesis.",
    "missing_item_specific_fact": "The sequence's membership and role in an antifungal biosynthetic pathway are not supplied; establishing that association requires target-specific annotation or evidence.",
    "reason": "The sequence offers a weak filter against some alternatives, but no recognizable family feature or pathway-specific motif meaningfully distinguishes antifungal biosynthesis from the listed choices. The decisive pathway association is a fact about this protein not inferable from the provided context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied source annotation supports B; no competing option is supported by the available evidence."
  },
  "important_caveats": [
    "The source annotation is sequence-matched and cites experimental evidence, but the cited primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P9WEG7 (RSTN5_ASPN3) annotates this 349-aa protein as 'Terpene cyclase rstn5' / 'Restricticin biosynthesis cluster protein 5' with EC 5.4.99.-. The PATHWAY comment explicitly states 'Antifungal biosynthesis' with experimental evidence code ECO:0000269 from PubMed:33857369 (Liu et al., JACS 2021, on CYP51-inhibitor biosynthetic gene clusters). The sequence matches the benchmark input exactly. Choice B is directly supported by the curated annotation backed by experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence can be eliminated against options A, C, and D using well-known protein-family features. (1) Option A (polypeptide chain elongation): ribosomal proteins and elongation factors (EF-Tu, EF-G, eEF1A) are highly conserved, relatively hydrophilic, and lack N-terminal signal peptides. This sequence begins with a clear hydrophobic signal peptide (MLHLTPLIFLSLAMAAAVGVWGVFTWNGG) and is dominated by membrane-spanning hydrophobic stretches—completely inconsistent with ribosomal/elongation machinery. (2) Option C (tetrahydrofolate interconversion): DHFR, SHMT, methylenetetrahydrofolate dehydrogenase, etc., share a Rossmann fold (GxGxxG) or specific folate-binding motifs. No such motif is present. (3) Option D (purine metabolism): PRPP synthetase, IMP dehydrogenase, phosphoribosyltransferases have characteristic PRPP-binding loops and specific catalytic residues absent here. (4) The remaining sequence features—multiple transmembrane-like helices, a GDF motif (variant of the DDxxD/NDxxD terpenoid cyclase signature), ~350 aa length, and membrane association—are hallmarks of fungal membrane-associated terpene cyclases involved in natural-product biosynthesis. Among the four offered choices, only 'Antifungal biosynthesis' (B) is compatible with a membrane-bound terpene cyclase. The elimination of A, C, D relies on canonical structural/sequence signatures of those protein classes, which is transferable knowledge from other proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate ribosomal/elongation proteins, folate enzymes, and purine metabolism enzymes based on the absence of their hallmark motifs (Rossmann fold, PRPP-binding, ribosomal protein conservation) and the presence of a signal peptide plus multiple hydrophobic helices. The residual option B is the only one consistent with a membrane-associated terpene cyclase. While positively naming the pathway 'Antifungal biosynthesis' rather than generic 'terpenoid biosynthesis' is specific, the multiple-choice format makes elimination sufficient to select B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are clearly incompatible with the sequence features (signal peptide, membrane helices, absence of Rossmann/PRPP/ribosomal motifs). Only B remains viable among the four choices. No ambiguity among the offered alternatives.


### Important caveats

- The pathway label 'Antifungal biosynthesis' is a UniProt-specific curated term; a model might more naturally call this 'terpenoid/secondary metabolite biosynthesis.' However, among the four given options, elimination uniquely selects B.
- The GDF motif is a variant of the canonical DDxxD/NDxxD terpenoid cyclase motif; identification as a terpene cyclase from sequence alone is suggestive but not definitive without structural confirmation.
- The UniProt annotation is backed by experimental evidence (ECO:0000269, PubMed:33857369), confirming the pathway assignment.
- The entry was first released in 2025; the benchmark author's source snapshot date is unknown, but the sequence matches both current and historical (entry v2) records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence can be eliminated against options A, C, and D using well-known protein-family features. (1) Option A (polypeptide chain elongation): ribosomal proteins and elongation factors (EF-Tu, EF-G, eEF1A) are highly conserved, relatively hydrophilic, and lack N-terminal signal peptides. This sequence begins with a clear hydrophobic signal peptide (MLHLTPLIFLSLAMAAAVGVWGVFTWNGG) and is dominated by membrane-spanning hydrophobic stretches—completely inconsistent with ribosomal/elongation machinery. (2) Option C (tetrahydrofolate interconversion): DHFR, SHMT, methylenetetrahydrofolate dehydrogenase, etc., share a Rossmann fold (GxGxxG) or specific folate-binding motifs. No such motif is present. (3) Option D (purine metabolism): PRPP synthetase, IMP dehydrogenase, phosphoribosyltransferases have characteristic PRPP-binding loops and specific catalytic residues absent here. (4) The remaining sequence features—multiple transmembrane-like helices, a GDF motif (variant of the DDxxD/NDxxD terpenoid cyclase signature), ~350 aa length, and membrane association—are hallmarks of fungal membrane-associated terpene cyclases involved in natural-product biosynthesis. Among the four offered choices, only 'Antifungal biosynthesis' (B) is compatible with a membrane-bound terpene cyclase. The elimination of A, C, D relies on canonical structural/sequence signatures of those protein classes, which is transferable knowledge from other proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate ribosomal/elongation proteins, folate enzymes, and purine metabolism enzymes based on the absence of their hallmark motifs (Rossmann fold, PRPP-binding, ribosomal protein conservation) and the presence of a signal peptide plus multiple hydrophobic helices. The residual option B is the only one consistent with a membrane-associated terpene cyclase. While positively naming the pathway 'Antifungal biosynthesis' rather than generic 'terpenoid biosynthesis' is specific, the multiple-choice format makes elimination sufficient to select B."
  },
  "case_id": "pathway_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P9WEG7 (RSTN5_ASPN3) annotates this 349-aa protein as 'Terpene cyclase rstn5' / 'Restricticin biosynthesis cluster protein 5' with EC 5.4.99.-. The PATHWAY comment explicitly states 'Antifungal biosynthesis' with experimental evidence code ECO:0000269 from PubMed:33857369 (Liu et al., JACS 2021, on CYP51-inhibitor biosynthetic gene clusters). The sequence matches the benchmark input exactly. Choice B is directly supported by the curated annotation backed by experimental evidence."
  },
  "important_caveats": [
    "The pathway label 'Antifungal biosynthesis' is a UniProt-specific curated term; a model might more naturally call this 'terpenoid/secondary metabolite biosynthesis.' However, among the four given options, elimination uniquely selects B.",
    "The GDF motif is a variant of the canonical DDxxD/NDxxD terpenoid cyclase motif; identification as a terpene cyclase from sequence alone is suggestive but not definitive without structural confirmation.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269, PubMed:33857369), confirming the pathway assignment.",
    "The entry was first released in 2025; the benchmark author's source snapshot date is unknown, but the sequence matches both current and historical (entry v2) records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with the sequence features (signal peptide, membrane helices, absence of Rossmann/PRPP/ribosomal motifs). Only B remains viable among the four choices. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P9WEG7 (RSTN5_ASPN3) annotates this 349-aa protein as 'Terpene cyclase rstn5' / 'Restricticin biosynthesis cluster protein 5' with EC 5.4.99.-. The PATHWAY comment explicitly states 'Antifungal biosynthesis' with experimental evidence code ECO:0000269 from PubMed:33857369 (Liu et al., JACS 2021, on CYP51-inhibitor biosynthetic gene clusters). The sequence matches the benchmark input exactly. Choice B is directly supported by the curated annotation backed by experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence can be eliminated against options A, C, and D using well-known protein-family features. (1) Option A (polypeptide chain elongation): ribosomal proteins and elongation factors (EF-Tu, EF-G, eEF1A) are highly conserved, relatively hydrophilic, and lack N-terminal signal peptides. This sequence begins with a clear hydrophobic signal peptide (MLHLTPLIFLSLAMAAAVGVWGVFTWNGG) and is dominated by membrane-spanning hydrophobic stretches—completely inconsistent with ribosomal/elongation machinery. (2) Option C (tetrahydrofolate interconversion): DHFR, SHMT, methylenetetrahydrofolate dehydrogenase, etc., share a Rossmann fold (GxGxxG) or specific folate-binding motifs. No such motif is present. (3) Option D (purine metabolism): PRPP synthetase, IMP dehydrogenase, phosphoribosyltransferases have characteristic PRPP-binding loops and specific catalytic residues absent here. (4) The remaining sequence features—multiple transmembrane-like helices, a GDF motif (variant of the DDxxD/NDxxD terpenoid cyclase signature), ~350 aa length, and membrane association—are hallmarks of fungal membrane-associated terpene cyclases involved in natural-product biosynthesis. Among the four offered choices, only 'Antifungal biosynthesis' (B) is compatible with a membrane-bound terpene cyclase. The elimination of A, C, D relies on canonical structural/sequence signatures of those protein classes, which is transferable knowledge from other proteins.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate ribosomal/elongation proteins, folate enzymes, and purine metabolism enzymes based on the absence of their hallmark motifs (Rossmann fold, PRPP-binding, ribosomal protein conservation) and the presence of a signal peptide plus multiple hydrophobic helices. The residual option B is the only one consistent with a membrane-associated terpene cyclase. While positively naming the pathway 'Antifungal biosynthesis' rather than generic 'terpenoid biosynthesis' is specific, the multiple-choice format makes elimination sufficient to select B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with the sequence features (signal peptide, membrane helices, absence of Rossmann/PRPP/ribosomal motifs). Only B remains viable among the four choices. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The pathway label 'Antifungal biosynthesis' is a UniProt-specific curated term; a model might more naturally call this 'terpenoid/secondary metabolite biosynthesis.' However, among the four given options, elimination uniquely selects B.",
    "The GDF motif is a variant of the canonical DDxxD/NDxxD terpenoid cyclase motif; identification as a terpene cyclase from sequence alone is suggestive but not definitive without structural confirmation.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269, PubMed:33857369), confirming the pathway assignment.",
    "The entry was first released in 2025; the benchmark author's source snapshot date is unknown, but the sequence matches both current and historical (entry v2) records."
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
  "benchmark_sequence_length": 349,
  "benchmark_sequence_sha256": "81e62647611dee5222b170056638bacd813b9736ff263a1893b00f2e83d6464a",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 349,
  "current_source_sequence_sha256": "81e62647611dee5222b170056638bacd813b9736ff263a1893b00f2e83d6464a",
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
  "requested_accession": "P9WEG7",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "selected_historical_source_sequence_length": 349,
  "selected_historical_source_sequence_sha256": "81e62647611dee5222b170056638bacd813b9736ff263a1893b00f2e83d6464a",
  "selected_historical_version": {
    "accession": "P9WEG7",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2025_02/2025_02",
    "firstReleaseDate": "23-Apr-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RSTN5_ASPN3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEG7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 / M93)\",\"taxonId\":1509407}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein 5\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"5.4.99.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Terpene cyclase rstn5\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Antifungal biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   RSTN5_ASPN3             Reviewed;         349 AA.\nAC   P9WEG7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   09-APR-2025, entry version 2.\nDE   RecName: Full=Terpene cyclase rstn5 {ECO:0000303|PubMed:33857369};\nDE            EC=5.4.99.- {ECO:0000305|PubMed:33857369};\nDE   AltName: Full=Restricticin biosynthesis cluster protein 5 {ECO:0000303|PubMed:33857369};\nGN   Name=rstn5 {ECO:0000303|PubMed:33857369};\nOS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /\nOS   M93).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=1509407;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND PATHWAY.\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000269|PubMed:33857369}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
