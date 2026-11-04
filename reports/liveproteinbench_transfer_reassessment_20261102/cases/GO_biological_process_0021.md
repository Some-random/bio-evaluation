# GO_biological_process_0021

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0021.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **D** — NAD biosynthetic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ

[Multiple Choices]
A. tRNA acetylation
B. inflammatory response
C. negative regulation of apoptotic process in bone marrow cell
D. NAD biosynthetic process
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

> The sequence-matched UniProt record identifies the protein as glutamine-dependent NAD(+) synthetase and describes its reaction as converting deamido-NAD to NAD, supporting NAD biosynthesis. The function and GO annotation are computationally assigned by HAMAP/UniRule, not evidence of a direct experiment on this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 552-residue sequence is consistent with the two-domain bacterial NadE family: glutamine-dependent NAD synthetases combine glutamine amidotransferase and ATP-dependent synthetase activities to complete NAD formation. That transferable family-level knowledge points to NAD biosynthesis (D), rather than tRNA acetylation; the inflammatory and bone-marrow apoptosis choices also describe host-cell processes, not the direct pathway of this bacterial enzyme.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence meaningfully distinguishes D among these alternatives; it does not require recalling this exact protein's annotation. The sequence alone may not prove the exact annotation, but certainty is not required for a defensible choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered processes are sufficiently distinct, and the NadE-family inference supports only NAD biosynthesis among them.


### Important caveats

- The reviewer evidence matches the supplied sequence, but the function and GO assignment cited there are computational annotations rather than direct experimental confirmation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 552-residue sequence is consistent with the two-domain bacterial NadE family: glutamine-dependent NAD synthetases combine glutamine amidotransferase and ATP-dependent synthetase activities to complete NAD formation. That transferable family-level knowledge points to NAD biosynthesis (D), rather than tRNA acetylation; the inflammatory and bone-marrow apoptosis choices also describe host-cell processes, not the direct pathway of this bacterial enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence meaningfully distinguishes D among these alternatives; it does not require recalling this exact protein's annotation. The sequence alone may not prove the exact annotation, but certainty is not required for a defensible choice."
  },
  "case_id": "GO_biological_process_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as glutamine-dependent NAD(+) synthetase and describes its reaction as converting deamido-NAD to NAD, supporting NAD biosynthesis. The function and GO annotation are computationally assigned by HAMAP/UniRule, not evidence of a direct experiment on this protein."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the function and GO assignment cited there are computational annotations rather than direct experimental confirmation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered processes are sufficiently distinct, and the NadE-family inference supports only NAD biosynthesis among them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as glutamine-dependent NAD(+) synthetase and describes its reaction as converting deamido-NAD to NAD, supporting NAD biosynthesis. The function and GO annotation are computationally assigned by HAMAP/UniRule, not evidence of a direct experiment on this protein.",
    "evidence_ids": ["C4", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 552-residue sequence is consistent with the two-domain bacterial NadE family: glutamine-dependent NAD synthetases combine glutamine amidotransferase and ATP-dependent synthetase activities to complete NAD formation. That transferable family-level knowledge points to NAD biosynthesis (D), rather than tRNA acetylation; the inflammatory and bone-marrow apoptosis choices also describe host-cell processes, not the direct pathway of this bacterial enzyme.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence meaningfully distinguishes D among these alternatives; it does not require recalling this exact protein's annotation. The sequence alone may not prove the exact annotation, but certainty is not required for a defensible choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered processes are sufficiently distinct, and the NadE-family inference supports only NAD biosynthesis among them."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the function and GO assignment cited there are computational annotations rather than direct experimental confirmation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0H2X6L3 (NADE_XANC8) is annotated with GO:0009435 'NAD+ biosynthetic process' (IEA:UniProtKB-UniRule, HAMAP-Rule MF_02090). The function comment states 'Catalyzes the ATP-dependent amidation of deamido-NAD to form NAD. Uses L-glutamine as a nitrogen source.' The pathway is 'NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1.' A PubMed reference (38429435) provides a DISRUPTION PHENOTYPE supporting NAD+ biosynthesis. The sequence matches the benchmark input exactly. The expected answer D is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a hallmark 'GWP' motif (GWPQSAGSVVY around residue ~60) within an N-terminal glutamine amidotransferase (GAT) domain, a well-known conserved feature across the GAT superfamily (shared with GMP synthase, carbamoyl phosphate synthetase, etc.). Combined with a C-terminal synthetase domain and overall ~550 aa two-domain architecture, this is characteristic of bacterial NAD+ synthetase (NadE). Among the four options: (B) inflammatory response and (C) negative regulation of apoptotic process in bone marrow cell are vertebrate-specific processes incompatible with a bacterial enzyme lacking signal peptides, transmembrane segments, or eukaryotic regulatory motifs. (A) tRNA acetylation requires a GNAT-fold acetyltransferase, which is structurally and sequentially distinct from the GAT+synthetase architecture observed. (D) NAD biosynthetic process is the only option involving a GAT-containing amidotransferase in a bacterial metabolic context, making it the uniquely consistent choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the GWP motif and two-domain GAT+synthetase architecture can eliminate options A (wrong fold), B and C (vertebrate-specific processes in a bacterial protein), leaving D as the only viable answer. This relies on transferable knowledge of the GAT superfamily, bacterial vs. vertebrate biology, and NadE family architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span entirely different biological contexts (bacterial cofactor biosynthesis, vertebrate inflammation, vertebrate apoptosis regulation, RNA modification). The GAT domain and bacterial nature of the protein uniquely point to D among the choices.


### Important caveats

- The GO annotation for this protein carries evidence code IEA:UniProtKB-UniRule (HAMAP-Rule MF_02090), which is a computational/family-based assignment rather than direct experimental characterization of this exact enzyme. However, a PubMed reference with DISRUPTION PHENOTYPE provides experimental corroboration.
- The GAT domain is shared across multiple enzyme families (GMP synthase, CPS, etc.); the specific NadE assignment relies on the full two-domain architecture and the context of the offered choices rather than the GAT motif alone.
- The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning above relies only on sequence features and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a hallmark 'GWP' motif (GWPQSAGSVVY around residue ~60) within an N-terminal glutamine amidotransferase (GAT) domain, a well-known conserved feature across the GAT superfamily (shared with GMP synthase, carbamoyl phosphate synthetase, etc.). Combined with a C-terminal synthetase domain and overall ~550 aa two-domain architecture, this is characteristic of bacterial NAD+ synthetase (NadE). Among the four options: (B) inflammatory response and (C) negative regulation of apoptotic process in bone marrow cell are vertebrate-specific processes incompatible with a bacterial enzyme lacking signal peptides, transmembrane segments, or eukaryotic regulatory motifs. (A) tRNA acetylation requires a GNAT-fold acetyltransferase, which is structurally and sequentially distinct from the GAT+synthetase architecture observed. (D) NAD biosynthetic process is the only option involving a GAT-containing amidotransferase in a bacterial metabolic context, making it the uniquely consistent choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the GWP motif and two-domain GAT+synthetase architecture can eliminate options A (wrong fold), B and C (vertebrate-specific processes in a bacterial protein), leaving D as the only viable answer. This relies on transferable knowledge of the GAT superfamily, bacterial vs. vertebrate biology, and NadE family architecture."
  },
  "case_id": "GO_biological_process_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 (NADE_XANC8) is annotated with GO:0009435 'NAD+ biosynthetic process' (IEA:UniProtKB-UniRule, HAMAP-Rule MF_02090). The function comment states 'Catalyzes the ATP-dependent amidation of deamido-NAD to form NAD. Uses L-glutamine as a nitrogen source.' The pathway is 'NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1.' A PubMed reference (38429435) provides a DISRUPTION PHENOTYPE supporting NAD+ biosynthesis. The sequence matches the benchmark input exactly. The expected answer D is well-supported."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code IEA:UniProtKB-UniRule (HAMAP-Rule MF_02090), which is a computational/family-based assignment rather than direct experimental characterization of this exact enzyme. However, a PubMed reference with DISRUPTION PHENOTYPE provides experimental corroboration.",
    "The GAT domain is shared across multiple enzyme families (GMP synthase, CPS, etc.); the specific NadE assignment relies on the full two-domain architecture and the context of the offered choices rather than the GAT motif alone.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning above relies only on sequence features and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different biological contexts (bacterial cofactor biosynthesis, vertebrate inflammation, vertebrate apoptosis regulation, RNA modification). The GAT domain and bacterial nature of the protein uniquely point to D among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 (NADE_XANC8) is annotated with GO:0009435 'NAD+ biosynthetic process' (IEA:UniProtKB-UniRule, HAMAP-Rule MF_02090). The function comment states 'Catalyzes the ATP-dependent amidation of deamido-NAD to form NAD. Uses L-glutamine as a nitrogen source.' The pathway is 'NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1.' A PubMed reference (38429435) provides a DISRUPTION PHENOTYPE supporting NAD+ biosynthesis. The sequence matches the benchmark input exactly. The expected answer D is well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H3", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a hallmark 'GWP' motif (GWPQSAGSVVY around residue ~60) within an N-terminal glutamine amidotransferase (GAT) domain, a well-known conserved feature across the GAT superfamily (shared with GMP synthase, carbamoyl phosphate synthetase, etc.). Combined with a C-terminal synthetase domain and overall ~550 aa two-domain architecture, this is characteristic of bacterial NAD+ synthetase (NadE). Among the four options: (B) inflammatory response and (C) negative regulation of apoptotic process in bone marrow cell are vertebrate-specific processes incompatible with a bacterial enzyme lacking signal peptides, transmembrane segments, or eukaryotic regulatory motifs. (A) tRNA acetylation requires a GNAT-fold acetyltransferase, which is structurally and sequentially distinct from the GAT+synthetase architecture observed. (D) NAD biosynthetic process is the only option involving a GAT-containing amidotransferase in a bacterial metabolic context, making it the uniquely consistent choice.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the GWP motif and two-domain GAT+synthetase architecture can eliminate options A (wrong fold), B and C (vertebrate-specific processes in a bacterial protein), leaving D as the only viable answer. This relies on transferable knowledge of the GAT superfamily, bacterial vs. vertebrate biology, and NadE family architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different biological contexts (bacterial cofactor biosynthesis, vertebrate inflammation, vertebrate apoptosis regulation, RNA modification). The GAT domain and bacterial nature of the protein uniquely point to D among the choices."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code IEA:UniProtKB-UniRule (HAMAP-Rule MF_02090), which is a computational/family-based assignment rather than direct experimental characterization of this exact enzyme. However, a PubMed reference with DISRUPTION PHENOTYPE provides experimental corroboration.",
    "The GAT domain is shared across multiple enzyme families (GMP synthase, CPS, etc.); the specific NadE assignment relies on the full two-domain architecture and the context of the offered choices rather than the GAT motif alone.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning above relies only on sequence features and general biological knowledge."
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
  "benchmark_sequence_length": 552,
  "benchmark_sequence_sha256": "3d11eda2e9e6481a31767f7fc550e14d13db9c3ed7ac21360bb4b2288341703d",
  "current_entry_audit": {
    "entryVersion": 50,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 552,
  "current_source_sequence_sha256": "3d11eda2e9e6481a31767f7fc550e14d13db9c3ed7ac21360bb4b2288341703d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 49,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0H2X6L3",
  "selected_historical_entry_version": 49,
  "selected_historical_record_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "selected_historical_source_sequence_length": 552,
  "selected_historical_source_sequence_sha256": "3d11eda2e9e6481a31767f7fc550e14d13db9c3ed7ac21360bb4b2288341703d",
  "selected_historical_version": {
    "accession": "A0A0H2X6L3",
    "database": "Swiss-Prot",
    "entryVersion": 49,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NADE_XANC8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0H2X6L3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":50,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Lysobacterales\",\"Lysobacteraceae\",\"Xanthomonas\"],\"scientificName\":\"Xanthomonas campestris pv. campestris (strain 8004)\",\"taxonId\":314565}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"NAD(+) synthase [glutamine-hydrolyzing]\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NAD(+) synthetase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NADS\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"6.3.5.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Glutamine-dependent NAD(+) synthetase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Catalyzes the ATP-dependent amidation of deamido-NAD to form NAD. Uses L-glutamine as a nitrogen source\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009435\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:NAD+ biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniRule\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Xu G.\",\"Ma J.\",\"Fang Q.\",\"Peng Q.\",\"Jiao X.\",\"Hu W.\",\"Zhao Q.\",\"Kong Y.\",\"Liu F.\",\"Shi X.\",\"Tang D.J.\",\"Tang J.L.\",\"Ming Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38429435\"},{\"database\":\"DOI\",\"id\":\"10.1038/s42003-024-05921-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"255\",\"id\":\"38429435\",\"journal\":\"Commun. Biol.\",\"lastPage\":\"255\",\"publicationDate\":\"2024\",\"title\":\"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.\",\"volume\":\"7\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"8004\"}],\"referenceNumber\":2,\"referencePositions\":[\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "entry_version": 49,
  "evidence_id": "H1",
  "excerpt": "ID   NADE_XANC8              Reviewed;         552 AA.\nAC   A0A0H2X6L3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 49.\nDE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};\nDE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};\nDE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};\nDE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};\nDE            Short=NADS {ECO:0000303|PubMed:38429435};\nGN   Name=nadE {ECO:0000255|HAMAP-Rule:MF_02090};\nGN   OrderedLocusNames=XC_1067 {ECO:0000312|EMBL:AAY48137.1};\nOS   Xanthomonas campestris pv. campestris (strain 8004).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Lysobacterales; Lysobacteraceae; Xanthomonas.\nOX   NCBI_TaxID=314565;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "entry_version": 49,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   DISRUPTION PHENOTYPE.\nRC   STRAIN=8004;\nRX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;\nRA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,\nRA   Shi X., Tang D.J., Tang J.L., Ming Z.;\nRT   \"Structural insights into Xanthomonas campestris pv. campestris NAD+\nRT   biosynthesis via the NAM salvage pathway.\";\nRL   Commun. Biol. 7:255-255(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "entry_version": 49,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the ATP-dependent amidation of deamido-NAD to form\nCC       NAD. Uses L-glutamine as a nitrogen source. {ECO:0000255|HAMAP-\nCC       Rule:MF_02090}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "entry_version": 49,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from\nCC       deamido-NAD(+) (L-Gln route): step 1/1. {ECO:0000255|HAMAP-\nCC       Rule:MF_02090}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "entry_version": 49,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0009435; P:NAD+ biosynthetic process; IEA:UniProtKB-UniRule.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006954\nname: inflammatory response\nnamespace: biological_process\ndef: \"The immediate defensive reaction (by vertebrate tissue) to infection or injury caused by chemical or physical agents. The process is characterized by local vasodilation, extravasation of plasma into intercellular spaces and accumulation of white blood cells and macrophages.\" [GO_REF:0000022, ISBN:0198506732]\nsubset: goslim_generic\nsynonym: \"inflammation\" BROAD []\nxref: Wikipedia:Inflammation\nis_a: GO:0006952 ! defense response\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006954",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 71907-71916",
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
  "excerpt": "[Term]\nid: GO:0009435\nname: NAD+ biosynthetic process\nnamespace: biological_process\nalt_id: GO:0006736\ndef: \"The chemical reactions and pathways resulting in the formation of nicotinamide adenine dinucleotide (NAD+), a coenzyme that interconverts with its reduced form, NADH, in many redox and catabolic reactions. NAD+ is derived from various sources including vitamin B3.\" [PMID:28648096]\nsynonym: \"NAD (oxidized) biosynthesis\" EXACT []\nsynonym: \"NAD (oxidized) biosynthetic process\" EXACT []\nsynonym: \"NAD (reduced) biosynthesis\" EXACT []\nsynonym: \"NAD (reduced) biosynthetic process\" EXACT []\nsynonym: \"NAD anabolism\" EXACT []\nsynonym: \"NAD biosynthesis\" EXACT []\nsynonym: \"NAD biosynthetic process\" EXACT []\nsynonym: \"NAD formation\" EXACT []\nsynonym: \"NAD synthesis\" EXACT []\nsynonym: \"NADH biosynthesis\" EXACT []\nsynonym: \"NADH biosynthetic process\" EXACT []\nsynonym: \"nicotinamide adenine dinucleotide biosynthesis\" EXACT []\nsynonym: \"nicotinamide adenine dinucleotide biosynthetic process\" EXACT []\nsynonym: \"oxidized NAD biosynthesis\" EXACT []\nsynonym: \"oxidized NAD biosynthetic process\" EXACT []\nsynonym: \"oxidized nicotinamide adenine dinucleotide biosynthesis\" EXACT []\nsynonym: \"oxidized nicotinamide adenine dinucleotide biosynthetic process\" EXACT []\nsynonym: \"reduced NAD biosynthesis\" EXACT []\nsynonym: \"reduced NAD biosynthetic process\" EXACT []\nsynonym: \"reduced nicotinamide adenine dinucleotide biosynthesis\" EXACT []\nsynonym: \"reduced nicotinamide adenine dinucleotide biosynthetic process\" EXACT []\nis_a: GO:0006164 ! purine nucleotide biosynthetic process\nis_a: GO:0019359 ! nicotinamide nucleotide biosynthetic process\nis_a: GO:0019674 ! NAD+ metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009435",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 96227-96257",
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
  "excerpt": "[Term]\nid: GO:0051391\nname: tRNA acetylation\nnamespace: biological_process\ndef: \"The modification of tRNA structure by addition of an acetyl group to tRNA. An acetyl group is CH3CO-, derived from acetic [ethanoic] acid.\" [GOC:ai]\nis_a: GO:0006400 ! tRNA modification\nis_a: GO:1990884 ! RNA acetylation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051391",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 326232-326239",
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
  "excerpt": "[Term]\nid: GO:0071866\nname: negative regulation of apoptotic process in bone marrow cell\nnamespace: biological_process\ndef: \"Any process that stops, prevents, or reduces the frequency, rate or extent of the occurrence or rate of cell death by apoptotic process in the bone marrow.\" [GOC:mah, GOC:mtg_apoptosis, GOC:yaf, PMID:17063141]\nsynonym: \"down regulation of apoptosis in bone marrow\" EXACT [GOC:mah]\nsynonym: \"down-regulation of apoptosis in bone marrow\" EXACT [GOC:mah]\nsynonym: \"downregulation of apoptosis in bone marrow\" EXACT [GOC:mah]\nsynonym: \"inhibition of apoptosis in bone marrow\" NARROW [GOC:mah]\nsynonym: \"negative regulation of apoptosis in bone marrow\" NARROW []\nsynonym: \"negative regulation of apoptotic process in bone marrow\" EXACT []\nsynonym: \"negative regulation of bone marrow cell apoptosis\" EXACT [GOC:mah, GOC:yaf]\nsynonym: \"negative regulation of bone marrow cell programmed cell death by apoptosis\" EXACT [GOC:mah]\nsynonym: \"negative regulation of killing of bone marrow cells\" EXACT [GOC:mah]\nsynonym: \"negative regulation of programmed cell death of bone marrow cells by apoptosis\" EXACT [GOC:mah]\nsynonym: \"negative regulation of programmed cell death, bone marrow cells\" EXACT [GOC:mah]\nis_a: GO:0043066 ! negative regulation of apoptotic process\nis_a: GO:0071865 ! regulation of apoptotic process in bone marrow cell\nrelationship: negatively_regulates GO:0071839 ! apoptotic process in bone marrow cell\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071866",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 381172-381191",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
