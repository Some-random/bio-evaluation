# GO_biological_process_0016

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0016.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **D** — threonine biosynthetic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTPSKKRCGVLGATGAVGTRFILLLEQSPLLELVAVGASERSAGKKYRDAVRWKQASPMPASVADLTVRRCAPSEFSDCDIIFSGLDPVAAGDIEMAFLKANFAVFSNAKNYRLDPIVPLVVPLVNAGHIDVIPAQRKHYGLDKGLIVCNSNCAVVGLVIPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPFIPGEEGKIATESRKILGNLNPDLAGFSDQQPLQVSVACNRVPVLDGHTVCASLRFVNRPAPTASQVRDALREYKSEVQLLGCPSAPRQAIHVLDDVDRPQPRLDRDTEAGYACSVGRIREDDSGVFDIQFVALSHNTVLGASGSSILNAESAILKGYI

[Multiple Choices]
A. response to xenobiotic stimulus
B. negative regulation of neuromuscular synaptic transmission
C. doxorubicin transport
D. threonine biosynthetic process
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

> The sequence-matched UniProt record identifies the protein as aspartate-semialdehyde dehydrogenase and describes its role in amino-acid biosynthesis, including threonine biosynthesis. The threonine-biosynthesis GO annotation is marked IDA, indicating an experimental-evidence annotation rather than only a computational prediction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C10](#evidence-c10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 362-aa sequence has a glycine-rich N-terminal region consistent with a nucleotide-binding enzyme, and its overall sequence is compatible with the aspartate-semialdehyde dehydrogenase family. Knowledge transferable from this enzyme family connects its product, aspartate semialdehyde, to the aspartate-family amino-acid pathways, including threonine biosynthesis. That makes D meaningfully distinguishable from xenobiotic response, neuromuscular regulation, and doxorubicin transport.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level enzyme and pathway inference provides a credible basis for choosing D without knowing this exact protein's database entry. The inference does not imply that threonine biosynthesis is its only pathway role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein may contribute to more than one amino-acid biosynthetic pathway, but only D among the offered choices describes a relevant biosynthetic process.


### Important caveats

- The source identifies multiple aspartate-family biosynthetic roles; the wording 'primary' may oversimplify the enzyme's broader pathway contributions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 362-aa sequence has a glycine-rich N-terminal region consistent with a nucleotide-binding enzyme, and its overall sequence is compatible with the aspartate-semialdehyde dehydrogenase family. Knowledge transferable from this enzyme family connects its product, aspartate semialdehyde, to the aspartate-family amino-acid pathways, including threonine biosynthesis. That makes D meaningfully distinguishable from xenobiotic response, neuromuscular regulation, and doxorubicin transport.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level enzyme and pathway inference provides a credible basis for choosing D without knowing this exact protein's database entry. The inference does not imply that threonine biosynthesis is its only pathway role."
  },
  "case_id": "GO_biological_process_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C10"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as aspartate-semialdehyde dehydrogenase and describes its role in amino-acid biosynthesis, including threonine biosynthesis. The threonine-biosynthesis GO annotation is marked IDA, indicating an experimental-evidence annotation rather than only a computational prediction."
  },
  "important_caveats": [
    "The source identifies multiple aspartate-family biosynthetic roles; the wording 'primary' may oversimplify the enzyme's broader pathway contributions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may contribute to more than one amino-acid biosynthetic pathway, but only D among the offered choices describes a relevant biosynthetic process."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as aspartate-semialdehyde dehydrogenase and describes its role in amino-acid biosynthesis, including threonine biosynthesis. The threonine-biosynthesis GO annotation is marked IDA, indicating an experimental-evidence annotation rather than only a computational prediction.",
    "evidence_ids": ["C4", "C5", "C7", "C10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 362-aa sequence has a glycine-rich N-terminal region consistent with a nucleotide-binding enzyme, and its overall sequence is compatible with the aspartate-semialdehyde dehydrogenase family. Knowledge transferable from this enzyme family connects its product, aspartate semialdehyde, to the aspartate-family amino-acid pathways, including threonine biosynthesis. That makes D meaningfully distinguishable from xenobiotic response, neuromuscular regulation, and doxorubicin transport.",
    "missing_item_specific_fact": "",
    "reason": "A family-level enzyme and pathway inference provides a credible basis for choosing D without knowing this exact protein's database entry. The inference does not imply that threonine biosynthesis is its only pathway role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may contribute to more than one amino-acid biosynthetic pathway, but only D among the offered choices describes a relevant biosynthetic process."
  },
  "important_caveats": [
    "The source identifies multiple aspartate-family biosynthetic roles; the wording 'primary' may oversimplify the enzyme's broader pathway contributions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A179UL48) annotates this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with GO:0009088 'threonine biosynthetic process' at IDA evidence level (direct assay, PubMed:30107909). The pathway comment explicitly states: 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The answer D is directly and experimentally supported.

Citations as saved: [C10](#evidence-c10), [C7](#evidence-c7), [C5](#evidence-c5), [H9](#evidence-h9), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'GVLGATGAVGTRFILLLEQ' contains the canonical GxGxxG Rossmann-fold nucleotide-binding motif characteristic of NAD(P)-dependent dehydrogenases. The C-terminal region contains a 'CPS' motif (around position ~310) consistent with the catalytic cysteine of aspartate-semialdehyde dehydrogenase (ASD), a well-characterized ~350-360 aa enzyme family present in all organisms. Recognizing this as an NADPH-dependent dehydrogenase in amino acid biosynthesis (transferable from knowledge of E. coli ASD, yeast ASD, and other homologs) eliminates: (B) neuromuscular synaptic transmission (a signaling/regulatory function, not a dehydrogenase), (C) doxorubicin transport (a membrane transporter, not a soluble enzyme), and (A) xenobiotic response (while some xenobiotic enzymes have Rossmann folds, the specific catalytic Cys motif, ~360 aa length, and overall architecture match ASD rather than P450 reductases or xenobiotic-metabolizing enzymes). Among the four choices, only D (threonine biosynthetic process) is consistent with an NADPH-dependent dehydrogenase in amino acid biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold motif, catalytic cysteine, protein length, and overall sequence architecture are transferable features recognizable from knowledge of the ASD enzyme family across multiple organisms. These features meaningfully distinguish a biosynthetic dehydrogenase from a transporter, neural regulator, or xenobiotic-response protein among the four offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although ASD participates in multiple aspartate-family pathways (threonine, methionine, lysine), only option D corresponds to any of these. The other three options (xenobiotic response, neuromuscular transmission, doxorubicin transport) are entirely unrelated to this enzyme class. No ambiguity exists among the offered choices.


### Important caveats

- The protein also participates in methionine and lysine biosynthesis, but neither appears among the choices, so this does not create ambiguity.
- The GO:0009088 annotation carries IDA (direct assay) evidence from PubMed:30107909, indicating experimental confirmation rather than mere computational transfer.
- The sequence was matched to UniProt A0A179UL48 (Blastomyces gilchristii ASD) with exact SHA-256 match at both current and historical (v26) snapshots.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'GVLGATGAVGTRFILLLEQ' contains the canonical GxGxxG Rossmann-fold nucleotide-binding motif characteristic of NAD(P)-dependent dehydrogenases. The C-terminal region contains a 'CPS' motif (around position ~310) consistent with the catalytic cysteine of aspartate-semialdehyde dehydrogenase (ASD), a well-characterized ~350-360 aa enzyme family present in all organisms. Recognizing this as an NADPH-dependent dehydrogenase in amino acid biosynthesis (transferable from knowledge of E. coli ASD, yeast ASD, and other homologs) eliminates: (B) neuromuscular synaptic transmission (a signaling/regulatory function, not a dehydrogenase), (C) doxorubicin transport (a membrane transporter, not a soluble enzyme), and (A) xenobiotic response (while some xenobiotic enzymes have Rossmann folds, the specific catalytic Cys motif, ~360 aa length, and overall architecture match ASD rather than P450 reductases or xenobiotic-metabolizing enzymes). Among the four choices, only D (threonine biosynthetic process) is consistent with an NADPH-dependent dehydrogenase in amino acid biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold motif, catalytic cysteine, protein length, and overall sequence architecture are transferable features recognizable from knowledge of the ASD enzyme family across multiple organisms. These features meaningfully distinguish a biosynthetic dehydrogenase from a transporter, neural regulator, or xenobiotic-response protein among the four offered choices."
  },
  "case_id": "GO_biological_process_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C10",
      "C7",
      "C5",
      "H9",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A179UL48) annotates this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with GO:0009088 'threonine biosynthetic process' at IDA evidence level (direct assay, PubMed:30107909). The pathway comment explicitly states: 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The answer D is directly and experimentally supported."
  },
  "important_caveats": [
    "The protein also participates in methionine and lysine biosynthesis, but neither appears among the choices, so this does not create ambiguity.",
    "The GO:0009088 annotation carries IDA (direct assay) evidence from PubMed:30107909, indicating experimental confirmation rather than mere computational transfer.",
    "The sequence was matched to UniProt A0A179UL48 (Blastomyces gilchristii ASD) with exact SHA-256 match at both current and historical (v26) snapshots."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although ASD participates in multiple aspartate-family pathways (threonine, methionine, lysine), only option D corresponds to any of these. The other three options (xenobiotic response, neuromuscular transmission, doxorubicin transport) are entirely unrelated to this enzyme class. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A179UL48) annotates this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with GO:0009088 'threonine biosynthetic process' at IDA evidence level (direct assay, PubMed:30107909). The pathway comment explicitly states: 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The answer D is directly and experimentally supported.",
    "evidence_ids": ["C10", "C7", "C5", "H9", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'GVLGATGAVGTRFILLLEQ' contains the canonical GxGxxG Rossmann-fold nucleotide-binding motif characteristic of NAD(P)-dependent dehydrogenases. The C-terminal region contains a 'CPS' motif (around position ~310) consistent with the catalytic cysteine of aspartate-semialdehyde dehydrogenase (ASD), a well-characterized ~350-360 aa enzyme family present in all organisms. Recognizing this as an NADPH-dependent dehydrogenase in amino acid biosynthesis (transferable from knowledge of E. coli ASD, yeast ASD, and other homologs) eliminates: (B) neuromuscular synaptic transmission (a signaling/regulatory function, not a dehydrogenase), (C) doxorubicin transport (a membrane transporter, not a soluble enzyme), and (A) xenobiotic response (while some xenobiotic enzymes have Rossmann folds, the specific catalytic Cys motif, ~360 aa length, and overall architecture match ASD rather than P450 reductases or xenobiotic-metabolizing enzymes). Among the four choices, only D (threonine biosynthetic process) is consistent with an NADPH-dependent dehydrogenase in amino acid biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold motif, catalytic cysteine, protein length, and overall sequence architecture are transferable features recognizable from knowledge of the ASD enzyme family across multiple organisms. These features meaningfully distinguish a biosynthetic dehydrogenase from a transporter, neural regulator, or xenobiotic-response protein among the four offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although ASD participates in multiple aspartate-family pathways (threonine, methionine, lysine), only option D corresponds to any of these. The other three options (xenobiotic response, neuromuscular transmission, doxorubicin transport) are entirely unrelated to this enzyme class. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The protein also participates in methionine and lysine biosynthesis, but neither appears among the choices, so this does not create ambiguity.",
    "The GO:0009088 annotation carries IDA (direct assay) evidence from PubMed:30107909, indicating experimental confirmation rather than mere computational transfer.",
    "The sequence was matched to UniProt A0A179UL48 (Blastomyces gilchristii ASD) with exact SHA-256 match at both current and historical (v26) snapshots."
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
  "benchmark_sequence_length": 362,
  "benchmark_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 362,
  "current_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A179UL48",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "selected_historical_source_sequence_length": 362,
  "selected_historical_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "selected_historical_version": {
    "accession": "A0A179UL48",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_BLAGS",
    "sequenceVersion": 2
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A179UL48\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Blastomyces dermatitidis\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002038\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Onygenales\",\"Ajellomycetaceae\",\"Blastomyces\"],\"scientificName\":\"Blastomyces gilchristii (strain SLH14081)\",\"taxonId\":559298}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the NADPH-dependent formation of L-aspartate 4-semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-aspartate (PubMed:29608391, PubMed:30107909). Mediates the second step in the biosynthesis of amino acids that derive from aspartate (the aspartate family of amino acids), including methioinine and threonine, the latter of which is a precursor to isoleucine (PubMed:30107909)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0071266\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:'de novo' L-methionine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/23",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"id\":\"GO:0009090\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:L-homoserine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/24",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"id\":\"GO:0009088\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:L-threonine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/25",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30107909\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2018.08.053\"}],\"citationType\":\"journal article\",\"firstPage\":\"2848\",\"id\":\"30107909\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"2854\",\"publicationDate\":\"2018\",\"title\":\"Structural insights into inhibitor binding to a fungal ortholog of aspartate semialdehyde dehydrogenase.\",\"volume\":\"503\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C85\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_BLAGS              Reviewed;         362 AA.\nAC   A0A179UL48;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};\nGN   ORFNames=BDBG_16922 {ECO:0000312|EMBL:OAT07949.1};\nOS   Blastomyces gilchristii (strain SLH14081) (Blastomyces dermatitidis).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Onygenales; Ajellomycetaceae; Blastomyces.\nOX   NCBI_TaxID=559298 {ECO:0000312|Proteomes:UP000002038};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:6C85, ECO:0007744|PDB:6C8W}\nRP   X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND\nRP   NADP(+), FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=30107909; DOI=10.1016/j.bbrc.2018.08.053;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structural insights into inhibitor binding to a fungal ortholog of\nRT   aspartate semialdehyde dehydrogenase.\";\nRL   Biochem. Biophys. Res. Commun. 503:2848-2854(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate 4-\nCC       semialdehyde (L-ASA) by the reductive dephosphorylation of 4-phospho-L-\nCC       aspartate (PubMed:29608391, PubMed:30107909). Mediates the second step\nCC       in the biosynthesis of amino acids that derive from aspartate (the\nCC       aspartate family of amino acids), including methioinine and threonine,\nCC       the latter of which is a precursor to isoleucine (PubMed:30107909).\nCC       {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H5",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-homoserine from L-aspartate: step 2/3.\nCC       {ECO:0000269|PubMed:30107909}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H6",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:30107909}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0071266; P:'de novo' L-methionine biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0009089; P:lysine biosynthetic process via diaminopimelate; IEA:UniProtKB-UniPathway.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0009088; P:threonine biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0009410\nname: response to xenobiotic stimulus\nnamespace: biological_process\nalt_id: GO:0017035\nalt_id: GO:0017104\nalt_id: GO:0042493\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a stimulus from a xenobiotic, a compound foreign to the organism exposed to it. It may be synthesized by another organism (like ampicilin) or it can be a synthetic chemical.\" [GOC:jl, GOC:krc]\nsubset: goslim_candida\nsynonym: \"drug resistance\" RELATED []\nsynonym: \"drug susceptibility/resistance\" RELATED []\nsynonym: \"response to drug\" RELATED []\nis_a: GO:0042221 ! response to chemical\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009410",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 95982-95995",
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
  "excerpt": "[Term]\nid: GO:1900074\nname: negative regulation of neuromuscular synaptic transmission\nnamespace: biological_process\ndef: \"Any process that stops, prevents or reduces the frequency, rate or extent of neuromuscular synaptic transmission.\" [GOC:kmv, GOC:TermGenie]\nsynonym: \"down regulation of neuromuscular synaptic transmission\" RELATED [GOC:TermGenie]\nsynonym: \"down-regulation of neuromuscular synaptic transmission\" RELATED [GOC:TermGenie]\nsynonym: \"downregulation of neuromuscular synaptic transmission\" RELATED [GOC:TermGenie]\nsynonym: \"inhibition of neuromuscular synaptic transmission\" RELATED [GOC:TermGenie]\nis_a: GO:0050805 ! negative regulation of synaptic transmission\nis_a: GO:1900073 ! regulation of neuromuscular synaptic transmission\nrelationship: negatively_regulates GO:0007274 ! neuromuscular synaptic transmission\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1900074",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 454062-454074",
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
  "excerpt": "[Term]\nid: GO:1900753\nname: doxorubicin transport\nnamespace: biological_process\ndef: \"The directed movement of a doxorubicin into, out of or within a cell, or between cells, by means of some agent such as a transporter or pore.\" [GOC:TermGenie, PMID:12057006, PMID:15090538, PMID:19063901, PMID:19651502, PMID:9651400]\nsynonym: \"(1S,3S)-3,5,12-trihydroxy-3-(hydroxyacetyl)-10-methoxy-6,11-dioxo-1,2,3,4,6,11-hexahydrotetracen-1-yl 3-amino-2,3,6-trideoxy-alpha-L-lyxo-hexopyranoside transport\" EXACT [GOC:TermGenie]\nsynonym: \"(1S,3S)-3-glycoloyl-3,5,12-trihydroxy-10-methoxy-6,11-dioxo-1,2,3,4,6,11-hexahydrotetracen-1-yl 3-amino-2,3,6-trideoxy-alpha-L-lyxo-hexopyranoside transport\" RELATED [GOC:TermGenie]\nsynonym: \"(8S-cis)-10-((3-amino-2,3,6-trideoxy-alpha-L-lyxo-hexopyranosyl)oxy)-7,8,9,10-tetrahydro-6,8,11-trihydroxy-8-(hydroxyacetyl)-1-methoxy-5,12-naphthacenedione transport\" RELATED [GOC:TermGenie]\nsynonym: \"14-hydroxydaunomycin transport\" RELATED [GOC:TermGenie]\nsynonym: \"14-hydroxydaunorubicine transport\" RELATED [GOC:TermGenie]\nsynonym: \"Adriamycin transport\" RELATED [GOC:TermGenie]\nsynonym: \"doxorubicine transport\" RELATED [GOC:TermGenie]\nsynonym: \"doxorubicinum transport\" RELATED [GOC:TermGenie]\nis_a: GO:0015850 ! organic hydroxy compound transport\nis_a: GO:0071705 ! nitrogen compound transport\nis_a: GO:1901656 ! glycoside transport\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1900753",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 466070-466086",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 16. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
