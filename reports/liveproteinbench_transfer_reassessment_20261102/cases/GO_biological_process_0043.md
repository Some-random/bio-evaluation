# GO_biological_process_0043

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0043.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **C** — threonine biosynthetic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASYPKKKCGVLGATGSVGQRFILLLADHPFLELHAIGASNRSAGKKYKDAVRWKQTTAMSERLSNLVLRDCRADQFSDCDLVFSGLNSDVAGEIEMEFIKAEIPVFSNAKNYRKHPLVPLVVPTVNPQHLDLIPHQRKEFGLKKGFLVCNSNCAVIGVVIPFAALQAKFGPVEEVEVFTEQAVSGAGYPGVPSMDIMDNVIPYISGEEDKLENEAQKILGSLNADATAFDEQKGLTVGATCTRVGVTDGHMAFVSLRFKNRPGPSAEEVKQAMREYQSEAQKLGCPSAPREAIKVFDEPDRPQPRLDRDISKGYTVSVGRVREAAPGSYFDLRFAALSHNTVIGAAGSSILNAEVAVIKGYI

[Multiple Choices]
A. chitin metabolic process
B. cobalt ion transport
C. threonine biosynthetic process
D. killing of cells of another organism
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the annotated aspartate-semialdehyde dehydrogenase. The record describes its role in aspartate-family amino-acid biosynthesis, including threonine, and includes an experimentally supported GO annotation for threonine biosynthesis.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C10](#evidence-c10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a conserved metabolic enzyme family; recognizing it as aspartate-semialdehyde dehydrogenase by shared sequence and family patterns supports an amino-acid biosynthesis role. This enzyme produces an intermediate used in the aspartate-family pathway, including threonine biosynthesis, making C meaningfully distinguishable from chitin metabolism, cobalt transport, and killing another organism's cells.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and transferable pathway knowledge provides a credible basis for selecting C among these alternatives, without requiring recall of this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The enzyme participates in more than one aspartate-family amino-acid pathway, but only threonine biosynthesis is represented among the offered choices.


### Important caveats

- Threonine biosynthesis is not the enzyme's exclusive biological process; the enzyme catalyzes an earlier shared step in aspartate-family amino-acid biosynthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a conserved metabolic enzyme family; recognizing it as aspartate-semialdehyde dehydrogenase by shared sequence and family patterns supports an amino-acid biosynthesis role. This enzyme produces an intermediate used in the aspartate-family pathway, including threonine biosynthesis, making C meaningfully distinguishable from chitin metabolism, cobalt transport, and killing another organism's cells.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and transferable pathway knowledge provides a credible basis for selecting C among these alternatives, without requiring recall of this exact protein's database record."
  },
  "case_id": "GO_biological_process_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C10"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated aspartate-semialdehyde dehydrogenase. The record describes its role in aspartate-family amino-acid biosynthesis, including threonine, and includes an experimentally supported GO annotation for threonine biosynthesis."
  },
  "important_caveats": [
    "Threonine biosynthesis is not the enzyme's exclusive biological process; the enzyme catalyzes an earlier shared step in aspartate-family amino-acid biosynthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme participates in more than one aspartate-family amino-acid pathway, but only threonine biosynthesis is represented among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated aspartate-semialdehyde dehydrogenase. The record describes its role in aspartate-family amino-acid biosynthesis, including threonine, and includes an experimentally supported GO annotation for threonine biosynthesis.",
    "evidence_ids": ["C5", "C7", "C10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a conserved metabolic enzyme family; recognizing it as aspartate-semialdehyde dehydrogenase by shared sequence and family patterns supports an amino-acid biosynthesis role. This enzyme produces an intermediate used in the aspartate-family pathway, including threonine biosynthesis, making C meaningfully distinguishable from chitin metabolism, cobalt transport, and killing another organism's cells.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and transferable pathway knowledge provides a credible basis for selecting C among these alternatives, without requiring recall of this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme participates in more than one aspartate-family amino-acid pathway, but only threonine biosynthesis is represented among the offered choices."
  },
  "important_caveats": [
    "Threonine biosynthesis is not the enzyme's exclusive biological process; the enzyme catalyzes an earlier shared step in aspartate-family amino-acid biosynthesis."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms the protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q4WWR8, gene hom2). The GO annotation GO:0009088 (L-threonine biosynthetic process) carries IDA (Inferred by Direct Assay) evidence from PubMed:28045392, an experimental study. The pathway annotation explicitly states: 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The FUNCTION comment confirms it 'mediates the second step in the biosynthesis of amino acids that derive from aspartate…including methionine and threonine.' Among the four offered choices, only C corresponds to this enzyme's documented role.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C10](#evidence-c10), [H4](#evidence-h4), [H6](#evidence-h6), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'GVLGATGSVGQRF' contains the canonical Rossmann-fold NAD(P)-binding motif (GxGxxG pattern), immediately identifying this as an NAD(P)-dependent dehydrogenase rather than a transporter, glycosidase, or pore-forming protein. The internal motif 'CNSNCAVIG' contains the catalytic cysteine characteristic of the aspartate-semialdehyde dehydrogenase (ASADH) family. ASADH is a textbook enzyme in the aspartate biosynthetic pathway: it converts 4-phospho-L-aspartate to L-aspartate-4-semialdehyde, the committed intermediate leading to homoserine, threonine, and methionine. A model recognizing the Rossmann fold and ASADH catalytic residues can eliminate: A (chitin metabolic process requires glycosidases/chitin synthases with entirely different folds), B (cobalt ion transport requires transmembrane helices and metal-binding sites absent here), and D (cell killing requires pore-forming or lytic domains). Only C (threonine biosynthetic process) is consistent with a dehydrogenase in the aspartate pathway. This inference relies on widely taught biochemistry and conserved sequence motifs shared across the ASADH superfamily in bacteria, fungi, and plants.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann fold and ASADH catalytic cysteine motif are transferable sequence features recognized across many homologs. The connection between ASADH and threonine biosynthesis is standard biochemistry knowledge learned from the aspartate pathway in E. coli, yeast, and other organisms. The three distractors describe protein classes (glycosidases, metal transporters, cytolytic proteins) with completely different structural architectures, making them readily eliminable from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although ASADH participates in both threonine and methionine biosynthesis, only threonine biosynthetic process is offered among the four choices. The other three options (chitin metabolism, cobalt transport, cell killing) are structurally and mechanistically incompatible with a NADPH-dependent dehydrogenase bearing a Rossmann fold and ASADH catalytic cysteine. No ambiguity exists among the offered alternatives.


### Important caveats

- The protein also participates in methionine/homoserine biosynthesis (step 2/3), but that option is not offered, so it does not create ambiguity among the four choices.
- The GO annotation for threonine biosynthetic process (GO:0009088) has IDA evidence from a crystallographic/biochemical study (PubMed:28045392), providing experimental support.
- The Rossmann fold motif is shared across many dehydrogenase families; correct family assignment to ASADH specifically depends on recognizing the catalytic cysteine and overall sequence context, which is achievable but requires familiarity with the ASADH family.
- The reviewer-only UniProt accession and organism identity were not available to the evaluated model; the reasoning above relies solely on sequence motifs and general biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'GVLGATGSVGQRF' contains the canonical Rossmann-fold NAD(P)-binding motif (GxGxxG pattern), immediately identifying this as an NAD(P)-dependent dehydrogenase rather than a transporter, glycosidase, or pore-forming protein. The internal motif 'CNSNCAVIG' contains the catalytic cysteine characteristic of the aspartate-semialdehyde dehydrogenase (ASADH) family. ASADH is a textbook enzyme in the aspartate biosynthetic pathway: it converts 4-phospho-L-aspartate to L-aspartate-4-semialdehyde, the committed intermediate leading to homoserine, threonine, and methionine. A model recognizing the Rossmann fold and ASADH catalytic residues can eliminate: A (chitin metabolic process requires glycosidases/chitin synthases with entirely different folds), B (cobalt ion transport requires transmembrane helices and metal-binding sites absent here), and D (cell killing requires pore-forming or lytic domains). Only C (threonine biosynthetic process) is consistent with a dehydrogenase in the aspartate pathway. This inference relies on widely taught biochemistry and conserved sequence motifs shared across the ASADH superfamily in bacteria, fungi, and plants.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold and ASADH catalytic cysteine motif are transferable sequence features recognized across many homologs. The connection between ASADH and threonine biosynthesis is standard biochemistry knowledge learned from the aspartate pathway in E. coli, yeast, and other organisms. The three distractors describe protein classes (glycosidases, metal transporters, cytolytic proteins) with completely different structural architectures, making them readily eliminable from the sequence alone."
  },
  "case_id": "GO_biological_process_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C10",
      "H4",
      "H6",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q4WWR8, gene hom2). The GO annotation GO:0009088 (L-threonine biosynthetic process) carries IDA (Inferred by Direct Assay) evidence from PubMed:28045392, an experimental study. The pathway annotation explicitly states: 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The FUNCTION comment confirms it 'mediates the second step in the biosynthesis of amino acids that derive from aspartate…including methionine and threonine.' Among the four offered choices, only C corresponds to this enzyme's documented role."
  },
  "important_caveats": [
    "The protein also participates in methionine/homoserine biosynthesis (step 2/3), but that option is not offered, so it does not create ambiguity among the four choices.",
    "The GO annotation for threonine biosynthetic process (GO:0009088) has IDA evidence from a crystallographic/biochemical study (PubMed:28045392), providing experimental support.",
    "The Rossmann fold motif is shared across many dehydrogenase families; correct family assignment to ASADH specifically depends on recognizing the catalytic cysteine and overall sequence context, which is achievable but requires familiarity with the ASADH family.",
    "The reviewer-only UniProt accession and organism identity were not available to the evaluated model; the reasoning above relies solely on sequence motifs and general biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although ASADH participates in both threonine and methionine biosynthesis, only threonine biosynthetic process is offered among the four choices. The other three options (chitin metabolism, cobalt transport, cell killing) are structurally and mechanistically incompatible with a NADPH-dependent dehydrogenase bearing a Rossmann fold and ASADH catalytic cysteine. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q4WWR8, gene hom2). The GO annotation GO:0009088 (L-threonine biosynthetic process) carries IDA (Inferred by Direct Assay) evidence from PubMed:28045392, an experimental study. The pathway annotation explicitly states: 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The FUNCTION comment confirms it 'mediates the second step in the biosynthesis of amino acids that derive from aspartate…including methionine and threonine.' Among the four offered choices, only C corresponds to this enzyme's documented role.",
    "evidence_ids": ["C4", "C5", "C7", "C10", "H4", "H6", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'GVLGATGSVGQRF' contains the canonical Rossmann-fold NAD(P)-binding motif (GxGxxG pattern), immediately identifying this as an NAD(P)-dependent dehydrogenase rather than a transporter, glycosidase, or pore-forming protein. The internal motif 'CNSNCAVIG' contains the catalytic cysteine characteristic of the aspartate-semialdehyde dehydrogenase (ASADH) family. ASADH is a textbook enzyme in the aspartate biosynthetic pathway: it converts 4-phospho-L-aspartate to L-aspartate-4-semialdehyde, the committed intermediate leading to homoserine, threonine, and methionine. A model recognizing the Rossmann fold and ASADH catalytic residues can eliminate: A (chitin metabolic process requires glycosidases/chitin synthases with entirely different folds), B (cobalt ion transport requires transmembrane helices and metal-binding sites absent here), and D (cell killing requires pore-forming or lytic domains). Only C (threonine biosynthetic process) is consistent with a dehydrogenase in the aspartate pathway. This inference relies on widely taught biochemistry and conserved sequence motifs shared across the ASADH superfamily in bacteria, fungi, and plants.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold and ASADH catalytic cysteine motif are transferable sequence features recognized across many homologs. The connection between ASADH and threonine biosynthesis is standard biochemistry knowledge learned from the aspartate pathway in E. coli, yeast, and other organisms. The three distractors describe protein classes (glycosidases, metal transporters, cytolytic proteins) with completely different structural architectures, making them readily eliminable from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although ASADH participates in both threonine and methionine biosynthesis, only threonine biosynthetic process is offered among the four choices. The other three options (chitin metabolism, cobalt transport, cell killing) are structurally and mechanistically incompatible with a NADPH-dependent dehydrogenase bearing a Rossmann fold and ASADH catalytic cysteine. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The protein also participates in methionine/homoserine biosynthesis (step 2/3), but that option is not offered, so it does not create ambiguity among the four choices.",
    "The GO annotation for threonine biosynthetic process (GO:0009088) has IDA evidence from a crystallographic/biochemical study (PubMed:28045392), providing experimental support.",
    "The Rossmann fold motif is shared across many dehydrogenase families; correct family assignment to ASADH specifically depends on recognizing the catalytic cysteine and overall sequence context, which is achievable but requires familiarity with the ASADH family.",
    "The reviewer-only UniProt accession and organism identity were not available to the evaluated model; the reasoning above relies solely on sequence motifs and general biochemistry."
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
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 118,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4WWR8",
  "selected_historical_entry_version": 118,
  "selected_historical_record_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "selected_historical_version": {
    "accession": "Q4WWR8",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_ASPFU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WWR8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002530\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28045392\",\"source\":\"PubMed\"}],\"value\":\"AfASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the NADPH-dependent formation of L-aspartate 4-semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-aspartate (PubMed:28045392, PubMed:29608391). Mediates the second step in the biosynthesis of amino acids that derive from aspartate (the aspartate family of amino acids), including methioinine and threonine, the latter of which is a precursor to isoleucine (PubMed:28045392)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0071266\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:'de novo' L-methionine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/27",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"28045392\",\"source\":\"PubMed\"}],\"id\":\"GO:0009090\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:L-homoserine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/28",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"28045392\",\"source\":\"PubMed\"}],\"id\":\"GO:0009088\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:L-threonine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/29",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28045392\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2053230x16020070\"}],\"citationType\":\"journal article\",\"firstPage\":\"36\",\"id\":\"28045392\",\"journal\":\"Acta Crystallogr. F\",\"lastPage\":\"44\",\"publicationDate\":\"2017\",\"title\":\"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from Aspergillus fumigatus.\",\"volume\":\"73\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5JW6\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_ASPFU              Reviewed;         363 AA.\nAC   Q4WWR8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\nDE   AltName: Full=AfASADH {ECO:0000303|PubMed:28045392};\nGN   Name=hom2 {ECO:0000305};\nGN   ORFNames=AFUA_3G06830 {ECO:0000312|EMBL:EAL92885.1};\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879 {ECO:0000312|Proteomes:UP000002530};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0007744|PDB:5JW6}\nRP   X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=28045392; DOI=10.1107/s2053230x16020070;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from\nRT   Aspergillus fumigatus.\";\nRL   Acta Crystallogr. F 73:36-44(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate 4-\nCC       semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-\nCC       aspartate (PubMed:28045392, PubMed:29608391). Mediates the second step\nCC       in the biosynthesis of amino acids that derive from aspartate (the\nCC       aspartate family of amino acids), including methioinine and threonine,\nCC       the latter of which is a precursor to isoleucine (PubMed:28045392).\nCC       {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H5",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-homoserine from L-aspartate: step 2/3.\nCC       {ECO:0000269|PubMed:28045392}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H6",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:28045392}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0071266; P:'de novo' L-methionine biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 134-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0009090; P:homoserine biosynthetic process; IEA:EnsemblFungi.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 135-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0009086; P:methionine biosynthetic process; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-136",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0009088; P:threonine biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 137-137",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006030\nname: chitin metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving chitin, a linear polysaccharide consisting of beta-(1->4)-linked N-acetyl-D-glucosamine residues.\" [GOC:jl, ISBN:0198506732]\nsynonym: \"beta-1,4-linked N-acetylglucosamine metabolic process\" EXACT []\nsynonym: \"beta-1,4-linked N-acetylglucosamine metabolism\" EXACT []\nsynonym: \"chitin metabolism\" EXACT []\nis_a: GO:0006022 ! aminoglycan metabolic process\nis_a: GO:0006040 ! amino sugar metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006030",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 61916-61926",
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
  "excerpt": "[Term]\nid: GO:0006824\nname: cobalt ion transport\nnamespace: biological_process\ndef: \"The directed movement of cobalt (Co2+) ions into, out of or within a cell, or between cells, by means of some agent such as a transporter or pore.\" [GOC:ai]\nsynonym: \"cobalt transport\" EXACT []\nis_a: GO:0000041 ! transition metal ion transport\nis_a: GO:0098655 ! monoatomic cation transmembrane transport\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006824",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 70716-70724",
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
  "excerpt": "[Term]\nid: GO:0031640\nname: killing of cells of another organism\nnamespace: biological_process\nalt_id: GO:0001908\nalt_id: GO:0051852\ndef: \"Any process in an organism that results in the killing of cells of another organism, including in some cases the death of the other organism. Killing here refers to the induction of death in one cell by another cell, not cell-autonomous death due to internal or other environmental conditions.\" [GOC:add]\nsubset: goslim_pir\nsynonym: \"killing of cells of other organism\" EXACT []\nis_a: GO:0001906 ! cell killing\nis_a: GO:0141061 ! disruption of cell in another organism\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031640",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 178549-178560",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
