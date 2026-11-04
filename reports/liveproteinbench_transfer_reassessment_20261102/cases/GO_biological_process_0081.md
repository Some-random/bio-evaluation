# GO_biological_process_0081

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0081.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **D** — adenylate cyclase-activating G protein-coupled receptor signaling pathway

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGGCMSREASEEMEQRKKSQAIDREIMDDSRRLRRECKILLLGSGESGKSTIVKQMKIIHQNGYTVDELQHYRLTVYKNLVDCAKALIDAMRQFDIVPEHEANKEHMEFLYTFQVDPDPNVPLDLHVSKAVAALWDDPAVPSVLEHQSEFYIMDSAPYFFAEAARIGSPEYIPSEADVLRARTKTTGIYETRFTMGQLNIHMFDVGGQRSERKKWIHCFESVTSIIFCVALSEYDQVLLEEQNQNRMLESLVLFDSVVNSRWFVRTSIILFLNKVDLFRQKLPRTPLSNYFPDYSGGPDVNRAAKYLLWRFNQVNRAHLNLYPHLTQATDTSNIRLVFAAVKETILQNALKDSGIL

[Multiple Choices]
A. response to abscisic acid
B. homoserine biosynthetic process
C. DNA topological change
D. adenylate cyclase-activating G protein-coupled receptor signaling pathway
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

> The sequence-matched UniProt record identifies the protein as a heterotrimeric G-protein alpha subunit and reports experimental evidence for its role in adenylate cyclase-activating GPCR signaling, supporting D. The separate GO annotation is computationally inferred, but the cited functional evidence is not solely an inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a characteristic G-protein alpha-subunit nucleotide-binding motif (including GSGESGKST) and conserved GTPase-domain features. Transferable knowledge of heterotrimeric G proteins links G-alpha subunits to GPCR signaling; among these choices, D is the one describing that signaling class. This supports D probabilistically without establishing the exact pathway details from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the G-alpha family provides a meaningful basis to distinguish D from the unrelated choices about abscisic-acid response, homoserine biosynthesis, and DNA topology. The exact ligand and pathway role would require protein-specific evidence, but are not needed to identify the best offered choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-family inference points to G-protein signaling, and no other offered option is comparably supported.


### Important caveats

- A G-alpha family assignment alone does not prove adenylate cyclase activation or the precise receptor and ligand; those details are supported by the reviewer-only functional evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a characteristic G-protein alpha-subunit nucleotide-binding motif (including GSGESGKST) and conserved GTPase-domain features. Transferable knowledge of heterotrimeric G proteins links G-alpha subunits to GPCR signaling; among these choices, D is the one describing that signaling class. This supports D probabilistically without establishing the exact pathway details from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the G-alpha family provides a meaningful basis to distinguish D from the unrelated choices about abscisic-acid response, homoserine biosynthesis, and DNA topology. The exact ligand and pathway role would require protein-specific evidence, but are not needed to identify the best offered choice."
  },
  "case_id": "GO_biological_process_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as a heterotrimeric G-protein alpha subunit and reports experimental evidence for its role in adenylate cyclase-activating GPCR signaling, supporting D. The separate GO annotation is computationally inferred, but the cited functional evidence is not solely an inference."
  },
  "important_caveats": [
    "A G-alpha family assignment alone does not prove adenylate cyclase activation or the precise receptor and ligand; those details are supported by the reviewer-only functional evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference points to G-protein signaling, and no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as a heterotrimeric G-protein alpha subunit and reports experimental evidence for its role in adenylate cyclase-activating GPCR signaling, supporting D. The separate GO annotation is computationally inferred, but the cited functional evidence is not solely an inference.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a characteristic G-protein alpha-subunit nucleotide-binding motif (including GSGESGKST) and conserved GTPase-domain features. Transferable knowledge of heterotrimeric G proteins links G-alpha subunits to GPCR signaling; among these choices, D is the one describing that signaling class. This supports D probabilistically without establishing the exact pathway details from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the G-alpha family provides a meaningful basis to distinguish D from the unrelated choices about abscisic-acid response, homoserine biosynthesis, and DNA topology. The exact ligand and pathway role would require protein-specific evidence, but are not needed to identify the best offered choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference points to G-protein signaling, and no other offered option is comparably supported."
  },
  "important_caveats": [
    "A G-alpha family assignment alone does not prove adenylate cyclase activation or the precise receptor and ligand; those details are supported by the reviewer-only functional evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (G1XJZ0, sequence matched) identifies this protein as 'Guanine nucleotide-binding protein alpha-2 subunit' (GPA2) from Arthrobotrys oligospora. The FUNCTION comment, supported by experimental evidence (ECO:0000269) from two peer-reviewed papers (PubMed:35993904 and PubMed:38649409), explicitly states it is the alpha subunit of a heterotrimeric G protein involved in 'adenylate cyclase-activating ascaroside pheromone-activated G protein-coupled receptor signaling pathway.' GO:0007189 (adenylate cyclase-activating G protein-coupled receptor signaling pathway) is annotated to this entry. The author's expected answer D matches exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [C10](#evidence-c10), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark Gα protein motifs recognizable from general protein-family knowledge: (1) the P-loop/Walker-A nucleotide-binding motif 'GSGESGKSTIVKQMKII' (GxxxxGK&#91;ST&#93; pattern), (2) the switch II region 'MFDVGGQRSERKK' containing the conserved DVGGQ motif, (3) the N-terminal 'MGGC' myristoylation/cysteine motif typical of lipid-modified Gα subunits, and (4) an overall length (~356 aa) consistent with Gα subunits. A knowledgeable model can recognize this as a heterotrimeric Gα subunit. Gα subunits are the canonical transducers in GPCR signaling pathways. Among the four options, only D involves GPCR signaling. Options A (abscisic acid response – a plant hormone pathway), B (homoserine biosynthesis – amino acid metabolism), and C (DNA topological change – DNA metabolism/topoisomerases) are mechanistically incompatible with a Gα protein. Even without knowing the exact GO term, family-level recognition of Gα → GPCR signaling eliminates A, B, and C, leaving D as the only viable choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Gα family is identifiable from conserved sequence motifs present in the input (GxxxxGK&#91;ST&#93;, DVGGQ, N-terminal MGGC, ~356 aa length). The general biological principle that Gα subunits transduce GPCR signals is transferable knowledge from the broader family of G proteins studied across many organisms. Only one option (D) references GPCR signaling; the other three describe entirely unrelated biological processes (plant hormone response, amino acid biosynthesis, DNA topology). The distinction between adenylate cyclase-activating vs. inhibiting is not tested because only the activating variant is offered as a choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe biological processes (plant hormone response, amino acid biosynthesis, DNA topology) that are mechanistically incompatible with any Gα protein. Option D is the sole GPCR-related choice. No alternative option is defensible for a Gα subunit.


### Important caveats

- The specific GO annotation GO:0007189 carries evidence code IEA:TreeGrafter (computational transfer), but the FUNCTION comment is backed by experimental evidence (ECO:0000269) from two independent papers confirming the adenylate cyclase-activating GPCR role.
- Distinguishing Gαs (stimulatory) from Gαi (inhibitory) purely from sequence is difficult due to ~60% identity in the nucleotide-binding domain; however, this distinction is not needed because only the 'activating' GPCR option is offered.
- The protein is from a nematode-trapping fungus (Arthrobotrys oligospora), but organism identity is not provided in the model input; the reasoning relies on sequence motifs and general Gα biology, not organism-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark Gα protein motifs recognizable from general protein-family knowledge: (1) the P-loop/Walker-A nucleotide-binding motif 'GSGESGKSTIVKQMKII' (GxxxxGK[ST] pattern), (2) the switch II region 'MFDVGGQRSERKK' containing the conserved DVGGQ motif, (3) the N-terminal 'MGGC' myristoylation/cysteine motif typical of lipid-modified Gα subunits, and (4) an overall length (~356 aa) consistent with Gα subunits. A knowledgeable model can recognize this as a heterotrimeric Gα subunit. Gα subunits are the canonical transducers in GPCR signaling pathways. Among the four options, only D involves GPCR signaling. Options A (abscisic acid response – a plant hormone pathway), B (homoserine biosynthesis – amino acid metabolism), and C (DNA topological change – DNA metabolism/topoisomerases) are mechanistically incompatible with a Gα protein. Even without knowing the exact GO term, family-level recognition of Gα → GPCR signaling eliminates A, B, and C, leaving D as the only viable choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Gα family is identifiable from conserved sequence motifs present in the input (GxxxxGK[ST], DVGGQ, N-terminal MGGC, ~356 aa length). The general biological principle that Gα subunits transduce GPCR signals is transferable knowledge from the broader family of G proteins studied across many organisms. Only one option (D) references GPCR signaling; the other three describe entirely unrelated biological processes (plant hormone response, amino acid biosynthesis, DNA topology). The distinction between adenylate cyclase-activating vs. inhibiting is not tested because only the activating variant is offered as a choice."
  },
  "case_id": "GO_biological_process_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "C10",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (G1XJZ0, sequence matched) identifies this protein as 'Guanine nucleotide-binding protein alpha-2 subunit' (GPA2) from Arthrobotrys oligospora. The FUNCTION comment, supported by experimental evidence (ECO:0000269) from two peer-reviewed papers (PubMed:35993904 and PubMed:38649409), explicitly states it is the alpha subunit of a heterotrimeric G protein involved in 'adenylate cyclase-activating ascaroside pheromone-activated G protein-coupled receptor signaling pathway.' GO:0007189 (adenylate cyclase-activating G protein-coupled receptor signaling pathway) is annotated to this entry. The author's expected answer D matches exactly."
  },
  "important_caveats": [
    "The specific GO annotation GO:0007189 carries evidence code IEA:TreeGrafter (computational transfer), but the FUNCTION comment is backed by experimental evidence (ECO:0000269) from two independent papers confirming the adenylate cyclase-activating GPCR role.",
    "Distinguishing Gαs (stimulatory) from Gαi (inhibitory) purely from sequence is difficult due to ~60% identity in the nucleotide-binding domain; however, this distinction is not needed because only the 'activating' GPCR option is offered.",
    "The protein is from a nematode-trapping fungus (Arthrobotrys oligospora), but organism identity is not provided in the model input; the reasoning relies on sequence motifs and general Gα biology, not organism-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe biological processes (plant hormone response, amino acid biosynthesis, DNA topology) that are mechanistically incompatible with any Gα protein. Option D is the sole GPCR-related choice. No alternative option is defensible for a Gα subunit."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (G1XJZ0, sequence matched) identifies this protein as 'Guanine nucleotide-binding protein alpha-2 subunit' (GPA2) from Arthrobotrys oligospora. The FUNCTION comment, supported by experimental evidence (ECO:0000269) from two peer-reviewed papers (PubMed:35993904 and PubMed:38649409), explicitly states it is the alpha subunit of a heterotrimeric G protein involved in 'adenylate cyclase-activating ascaroside pheromone-activated G protein-coupled receptor signaling pathway.' GO:0007189 (adenylate cyclase-activating G protein-coupled receptor signaling pathway) is annotated to this entry. The author's expected answer D matches exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C9", "C10", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark Gα protein motifs recognizable from general protein-family knowledge: (1) the P-loop/Walker-A nucleotide-binding motif 'GSGESGKSTIVKQMKII' (GxxxxGK[ST] pattern), (2) the switch II region 'MFDVGGQRSERKK' containing the conserved DVGGQ motif, (3) the N-terminal 'MGGC' myristoylation/cysteine motif typical of lipid-modified Gα subunits, and (4) an overall length (~356 aa) consistent with Gα subunits. A knowledgeable model can recognize this as a heterotrimeric Gα subunit. Gα subunits are the canonical transducers in GPCR signaling pathways. Among the four options, only D involves GPCR signaling. Options A (abscisic acid response – a plant hormone pathway), B (homoserine biosynthesis – amino acid metabolism), and C (DNA topological change – DNA metabolism/topoisomerases) are mechanistically incompatible with a Gα protein. Even without knowing the exact GO term, family-level recognition of Gα → GPCR signaling eliminates A, B, and C, leaving D as the only viable choice.",
    "missing_item_specific_fact": "",
    "reason": "The Gα family is identifiable from conserved sequence motifs present in the input (GxxxxGK[ST], DVGGQ, N-terminal MGGC, ~356 aa length). The general biological principle that Gα subunits transduce GPCR signals is transferable knowledge from the broader family of G proteins studied across many organisms. Only one option (D) references GPCR signaling; the other three describe entirely unrelated biological processes (plant hormone response, amino acid biosynthesis, DNA topology). The distinction between adenylate cyclase-activating vs. inhibiting is not tested because only the activating variant is offered as a choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe biological processes (plant hormone response, amino acid biosynthesis, DNA topology) that are mechanistically incompatible with any Gα protein. Option D is the sole GPCR-related choice. No alternative option is defensible for a Gα subunit."
  },
  "important_caveats": [
    "The specific GO annotation GO:0007189 carries evidence code IEA:TreeGrafter (computational transfer), but the FUNCTION comment is backed by experimental evidence (ECO:0000269) from two independent papers confirming the adenylate cyclase-activating GPCR role.",
    "Distinguishing Gαs (stimulatory) from Gαi (inhibitory) purely from sequence is difficult due to ~60% identity in the nucleotide-binding domain; however, this distinction is not needed because only the 'activating' GPCR option is offered.",
    "The protein is from a nematode-trapping fungus (Arthrobotrys oligospora), but organism identity is not provided in the model input; the reasoning relies on sequence motifs and general Gα biology, not organism-specific knowledge."
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
  "benchmark_sequence_length": 356,
  "benchmark_sequence_sha256": "20d06b8f54f80f59091b2748b9cdcad33301db262f1f84583d9379e61dc7eaa2",
  "current_entry_audit": {
    "entryVersion": 69,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 356,
  "current_source_sequence_sha256": "20d06b8f54f80f59091b2748b9cdcad33301db262f1f84583d9379e61dc7eaa2",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G1XJZ0",
  "selected_historical_entry_version": 67,
  "selected_historical_record_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "selected_historical_source_sequence_length": 356,
  "selected_historical_source_sequence_sha256": "20d06b8f54f80f59091b2748b9cdcad33301db262f1f84583d9379e61dc7eaa2",
  "selected_historical_version": {
    "accession": "G1XJZ0",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GPA2_ARTOA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G1XJZ0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":69,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Nematode-trapping fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008784\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Orbiliomycetes\",\"Orbiliales\",\"Orbiliaceae\",\"Orbilia\",\"Orbilia oligospora\"],\"scientificName\":\"Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\",\"synonyms\":[\"Didymozoophaga oligospora\"],\"taxonId\":756982}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Guanine nucleotide-binding protein alpha-2 subunit\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35993904\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38649409\",\"source\":\"PubMed\"}],\"value\":\"Alpha subunit of the heterotrimeric guanine nucleotide-binding protein (G protein) involved in adenylate cyclase-activating ascaroside pheromone-activated G protein-coupled receptor signaling pathway (PubMed:35993904, PubMed:38649409). Binding of prey ascaroside pheromones to transmembrane receptors GPR2 and GPR3 leads to activation of the pathway and positive regulation of trap formation for nematode capture (PubMed:35993904, PubMed:38649409)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0007189\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:adenylate cyclase-activating G protein-coupled receptor signaling pathway\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0032502\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:developmental process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0010255\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:glucose mediated signaling pathway\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/21",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Chen S.A.\",\"Lin H.C.\",\"Hsueh Y.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35993904\"},{\"database\":\"DOI\",\"id\":\"10.1093/g3journal/jkac217\"}],\"citationType\":\"journal article\",\"firstPage\":\"jkac217\",\"id\":\"35993904\",\"journal\":\"G3 (Bethesda)\",\"lastPage\":\"jkac217\",\"publicationDate\":\"2022\",\"title\":\"The cAMP-PKA pathway regulates prey sensing and trap morphogenesis in the nematode-trapping fungus Arthrobotrys oligospora.\",\"volume\":\"12\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Kuo C.Y.\",\"Tay R.J.\",\"Lin H.C.\",\"Juan S.C.\",\"Vidal-Diez de Ulzurrun G.\",\"Chang Y.C.\",\"Hoki J.\",\"Schroeder F.C.\",\"Hsueh Y.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38649409\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41564-024-01679-w\"}],\"citationType\":\"journal article\",\"firstPage\":\"1738\",\"id\":\"38649409\",\"journal\":\"Nat. Microbiol.\",\"lastPage\":\"1751\",\"publicationDate\":\"2024\",\"title\":\"The nematode-trapping fungus Arthrobotrys oligospora detects prey pheromones via G protein-coupled receptors.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38649409\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"TWF154\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH GPR2 AND GPR3\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:28:34.414621+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50",
  "url": "https://rest.uniprot.org/uniprotkb/G1XJZ0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H1",
  "excerpt": "ID   GPA2_ARTOA              Reviewed;         356 AA.\nAC   G1XJZ0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Guanine nucleotide-binding protein alpha-2 subunit {ECO:0000305};\nGN   Name=GPA2 {ECO:0000303|PubMed:38649409};\nGN   ORFNames=AOL_s00109g19 {ECO:0000312|EMBL:EGX46447.1};\nOS   Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\nOS   (Nematode-trapping fungus) (Didymozoophaga oligospora).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Orbiliomycetes;\nOC   Orbiliales; Orbiliaceae; Orbilia; Orbilia oligospora.\nOX   NCBI_TaxID=756982 {ECO:0000312|Proteomes:UP000008784};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=35993904; DOI=10.1093/g3journal/jkac217;\nRA   Chen S.A., Lin H.C., Hsueh Y.P.;\nRT   \"The cAMP-PKA pathway regulates prey sensing and trap morphogenesis in the\nRT   nematode-trapping fungus Arthrobotrys oligospora.\";\nRL   G3 (Bethesda) 12:jkac217-jkac217(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND INTERACTION WITH GPR2 AND GPR3.\nRC   STRAIN=TWF154 {ECO:0000303|PubMed:38649409};\nRX   PubMed=38649409; DOI=10.1038/s41564-024-01679-w;\nRA   Kuo C.Y., Tay R.J., Lin H.C., Juan S.C., Vidal-Diez de Ulzurrun G.,\nRA   Chang Y.C., Hoki J., Schroeder F.C., Hsueh Y.P.;\nRT   \"The nematode-trapping fungus Arthrobotrys oligospora detects prey\nRT   pheromones via G protein-coupled receptors.\";\nRL   Nat. Microbiol. 9:1738-1751(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Alpha subunit of the heterotrimeric guanine nucleotide-\nCC       binding protein (G protein) involved in adenylate cyclase-activating\nCC       ascaroside pheromone-activated G protein-coupled receptor signaling\nCC       pathway (PubMed:35993904, PubMed:38649409). Binding of prey ascaroside\nCC       pheromones to transmembrane receptors GPR2 and GPR3 leads to activation\nCC       of the pathway and positive regulation of trap formation for nematode\nCC       capture (PubMed:35993904, PubMed:38649409).\nCC       {ECO:0000269|PubMed:35993904, ECO:0000269|PubMed:38649409}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0010619; P:adenylate cyclase-activating glucose-activated G protein-coupled receptor signaling pathway; IEA:EnsemblFungi.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0030437; P:ascospore formation; IEA:EnsemblFungi.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0001403; P:invasive growth in response to glucose limitation; IEA:EnsemblFungi.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0010515; P:negative regulation of induction of conjugation with cellular fusion; IEA:EnsemblFungi.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0000122; P:negative regulation of transcription by RNA polymerase II; IEA:EnsemblFungi.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0007124; P:pseudohyphal growth; IEA:EnsemblFungi.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:42.163763+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f",
  "url": "https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006265\nname: DNA topological change\nnamespace: biological_process\ndef: \"The process in which a transformation is induced in the topological structure of a double-stranded DNA helix, resulting in a change in linking number.\" [ISBN:071673706X, ISBN:0935702490]\ncomment: Note that the synonym 'DNA underwinding' should not be confused with 'DNA unwinding ; GO:0006268', which refers to DNA strand separation, and is a type of geometric change. GO:0006265 refers to alteration of the superhelical density of double-stranded DNA. Note that DNA topological change and DNA geometric change (GO:0032392) are distinct, but are usually coupled in vivo.\nsynonym: \"DNA underwinding\" NARROW []\nis_a: GO:0006259 ! DNA metabolic process\nis_a: GO:0071103 ! DNA conformation change\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006265",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 64593-64602",
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
  "excerpt": "[Term]\nid: GO:0007189\nname: adenylate cyclase-activating G protein-coupled receptor signaling pathway\nnamespace: biological_process\nalt_id: GO:0010579\nalt_id: GO:0010580\ndef: \"A G protein-coupled receptor signaling pathway in which the signal is transmitted via the activation of adenylyl cyclase activity which results in an increase in the intracellular concentration of cyclic AMP (cAMP). This pathway is negatively regulated by phosphodiesterase, which cleaves cAMP and terminates the signaling.\" [GOC:dph, GOC:mah, GOC:signaling, GOC:tb, ISBN:0815316194]\ncomment: This term can be used to annotate ligands, receptors and G-proteins that lead to activation of adenylate cyclase activity within a signaling pathway.\nsynonym: \"activation of adenylate cyclase activity by G-protein signaling pathway\" RELATED [GOC:bf]\nsynonym: \"activation of adenylate cyclase activity involved in G-protein signaling\" RELATED [GOC:signaling]\nsynonym: \"adenylate cyclase-activating GPCR signaling pathway\" EXACT [GOC:signaling]\nsynonym: \"G protein signaling, adenylate cyclase activating pathway\" EXACT []\nsynonym: \"G protein signaling, adenylyl cyclase activating pathway\" EXACT []\nsynonym: \"G protein signalling, adenylate cyclase activating pathway\" EXACT []\nsynonym: \"G protein signalling, adenylyl cyclase activating pathway\" EXACT []\nsynonym: \"G-protein signaling, adenylate cyclase activating pathway\" EXACT [GOC:dph, GOC:tb]\nsynonym: \"G-protein signaling, adenylyl cyclase activating pathway\" EXACT []\nsynonym: \"G-protein signalling, adenylate cyclase activating pathway\" EXACT []\nsynonym: \"G-protein signalling, adenylyl cyclase activating pathway\" EXACT []\nsynonym: \"GPCR signaling pathway via activation of adenylate cyclase\" EXACT [GOC:bf]\nsynonym: \"GPCR signaling pathway via activation of adenylate cyclase activity\" EXACT [GOC:signaling]\nsynonym: \"positive regulation of adenylate cyclase activity by G-protein signaling pathway\" RELATED [GOC:signaling]\nsynonym: \"positive regulation of adenylate cyclase activity by G-protein signalling pathway\" RELATED [GOC:mah]\nsynonym: \"positive regulation of adenylate cyclase activity involved in G-protein coupled receptor signaling pathway\" EXACT []\nxref: Reactome:R-HSA-170660 \"Adenylate cyclase activating pathway\"\nis_a: GO:0007188 ! adenylate cyclase-modulating G protein-coupled receptor signaling pathway\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007189",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 74186-74212",
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
  "excerpt": "[Term]\nid: GO:0009737\nname: response to abscisic acid\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of an abscisic acid stimulus.\" [GOC:jl]\nsynonym: \"response to abscisic acid stimulus\" EXACT [GOC:dos]\nis_a: GO:0009725 ! response to hormone\nis_a: GO:0033993 ! response to lipid\nis_a: GO:0097305 ! response to alcohol\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009737",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 99213-99222",
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
  "excerpt": "[Term]\nid: GO:0010619\nname: adenylate cyclase-activating glucose-activated G protein-coupled receptor signaling pathway\nnamespace: biological_process\ndef: \"An adenylate cyclase-activating G protein-coupled receptor signaling pathway initiated by glucose binding to its receptor on the surface of the target cell, and ending with the regulation of a downstream cellular process.\" [GOC:dph, GOC:signaling, GOC:tb]\nsynonym: \"activation of adenylate cyclase activity by glucose involved in G-protein signaling\" EXACT [GOC:dph, GOC:tb]\nsynonym: \"activation of adenylate cyclase activity by glucose-triggered G-protein signaling pathway\" EXACT [GOC:signaling]\nsynonym: \"activation of adenylate cyclase activity by glucose-triggered G-protein signalling pathway\" EXACT [GOC:mah]\nsynonym: \"glucose-sensing PKA pathway\" EXACT []\nis_a: GO:0007189 ! adenylate cyclase-activating G protein-coupled receptor signaling pathway\nrelationship: part_of GO:0010255 ! glucose mediated signaling pathway\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0010619",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 107519-107530",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
