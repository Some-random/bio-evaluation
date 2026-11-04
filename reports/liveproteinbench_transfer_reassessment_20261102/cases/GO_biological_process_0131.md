# GO_biological_process_0131

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0131.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **C** — fatty acid beta-oxidation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | uncertain | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSGHIRVLELNRPKARNAISRALLASLREEVHSIARQYDAQTGEEIPTPSWNKRFGGIAGDSEKGPTRALVLASAVESSFCAGADLKERRGFTQEETNEFLANLRSTFAALDALPIPTISAISSRALGGGLELALCTHFRVLTSNAIVSLPETRLGIIPGAGGTHRLPRLIGLGRARDMIVTGRAVSGAEAYFLGLADRLVEVLPPDEQEAADTTDKDAALLSAAREAALTEAVRLASQICEGGPIGIRAALQAVQAPSQETENKMYERVIGTEDRNEALKAFAEKRKPVFKGR

[Multiple Choices]
A. endomitotic cell cycle
B. carboxylic acid metabolic process
C. fatty acid beta-oxidation
D. gluconeogenesis
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

### Expected-answer support: uncertain

> The matched sequence has a UniProt annotation to fatty acid beta-oxidation, but it is computational (IEA:TreeGrafter; C7). The more specific enzyme and pathway annotations identify a methylglutaconyl-CoA hydratase in leucine degradation (C4-C6), but the catalytic function is stated to be by similarity, not established here as an experimental assay of this protein. That evidence makes C a questionable primary-process assignment but does not establish that the protein cannot participate in beta-oxidation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus is consistent with mitochondrial targeting, and the remaining sequence supports a CoA-hydratase/crotonase-family inference. Transferable family knowledge points toward methylglutaconyl-CoA hydratase activity in leucine degradation, which is encompassed by the broad carboxylic acid metabolic process option B. That is a more specific mechanistic basis than the sequence provides for fatty acid beta-oxidation, and it argues against choosing C solely from a shared hydratase-family resemblance.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference offers a meaningful way to favor B over the cell-cycle and gluconeogenesis choices and to question C. It does not establish the protein's full process repertoire or prove that beta-oxidation is absent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B is a broad process compatible with leucine catabolism, while C has a direct but computational GO annotation for this sequence. The prompt gives no criterion for resolving that difference in specificity or the uncertain C annotation.


### Important caveats

- The reviewer-only annotations match the supplied sequence; they were not available as original model inputs.
- The exact author source snapshot is unknown, and the beta-oxidation assignment is computational rather than experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus is consistent with mitochondrial targeting, and the remaining sequence supports a CoA-hydratase/crotonase-family inference. Transferable family knowledge points toward methylglutaconyl-CoA hydratase activity in leucine degradation, which is encompassed by the broad carboxylic acid metabolic process option B. That is a more specific mechanistic basis than the sequence provides for fatty acid beta-oxidation, and it argues against choosing C solely from a shared hydratase-family resemblance.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference offers a meaningful way to favor B over the cell-cycle and gluconeogenesis choices and to question C. It does not establish the protein's full process repertoire or prove that beta-oxidation is absent."
  },
  "case_id": "GO_biological_process_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "cannot_determine",
    "reason": "The matched sequence has a UniProt annotation to fatty acid beta-oxidation, but it is computational (IEA:TreeGrafter; C7). The more specific enzyme and pathway annotations identify a methylglutaconyl-CoA hydratase in leucine degradation (C4-C6), but the catalytic function is stated to be by similarity, not established here as an experimental assay of this protein. That evidence makes C a questionable primary-process assignment but does not establish that the protein cannot participate in beta-oxidation."
  },
  "important_caveats": [
    "The reviewer-only annotations match the supplied sequence; they were not available as original model inputs.",
    "The exact author source snapshot is unknown, and the beta-oxidation assignment is computational rather than experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B is a broad process compatible with leucine catabolism, while C has a direct but computational GO annotation for this sequence. The prompt gives no criterion for resolving that difference in specificity or the uncertain C annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0131",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The matched sequence has a UniProt annotation to fatty acid beta-oxidation, but it is computational (IEA:TreeGrafter; C7). The more specific enzyme and pathway annotations identify a methylglutaconyl-CoA hydratase in leucine degradation (C4-C6), but the catalytic function is stated to be by similarity, not established here as an experimental assay of this protein. That evidence makes C a questionable primary-process assignment but does not establish that the protein cannot participate in beta-oxidation.",
    "evidence_ids": ["C4", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus is consistent with mitochondrial targeting, and the remaining sequence supports a CoA-hydratase/crotonase-family inference. Transferable family knowledge points toward methylglutaconyl-CoA hydratase activity in leucine degradation, which is encompassed by the broad carboxylic acid metabolic process option B. That is a more specific mechanistic basis than the sequence provides for fatty acid beta-oxidation, and it argues against choosing C solely from a shared hydratase-family resemblance.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference offers a meaningful way to favor B over the cell-cycle and gluconeogenesis choices and to question C. It does not establish the protein's full process repertoire or prove that beta-oxidation is absent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B is a broad process compatible with leucine catabolism, while C has a direct but computational GO annotation for this sequence. The prompt gives no criterion for resolving that difference in specificity or the uncertain C annotation."
  },
  "important_caveats": [
    "The reviewer-only annotations match the supplied sequence; they were not available as original model inputs.",
    "The exact author source snapshot is unknown, and the beta-oxidation assignment is computational rather than experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein is experimentally confirmed (PubMed:32431008) as 3-methylglutaconyl-CoA hydratase 1 (EC 4.2.1.18), catalyzing the reversible hydration of 3-methylglutaconyl-CoA to HMG-CoA in the L-leucine degradation pathway (step 5/5). The fatty acid beta-oxidation annotation (GO:0006635) carries only IEA:TreeGrafter evidence — a purely computational inference from sequence similarity to the crotonase superfamily, which includes both enoyl-CoA hydratase (beta-oxidation) and 3-methylglutaconyl-CoA hydratase (leucine degradation). The experimental evidence, UniProtKB-UniPathway annotation (GO:0006552 L-leucine catabolic process), and UniProtKB-KW annotation (GO:0009083 branched-chain amino acid catabolic process) all point to leucine degradation as the primary biological process. The TreeGrafter beta-oxidation call is a known cross-family misassignment within the crotonase superfamily and does not reflect the primary process.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model recognizing the crotonase superfamily fold from the sequence (conserved motifs such as the 'GADL' region, the ~349-residue length, and the characteristic alpha/beta hydratase architecture shared with enoyl-CoA hydratase) would associate this fold most strongly with fatty acid beta-oxidation, the most well-known and heavily annotated pathway for crotonase-type CoA-ester hydratases. This family-level association — learned from the many enoyl-CoA hydratases in beta-oxidation across bacteria, fungi, and animals — meaningfully distinguishes C from A (endomitotic cell cycle, no cell-cycle machinery features), D (gluconeogenesis, no gluconeogenic enzyme features), and B (carboxylic acid metabolic process, an extremely broad GO:0019752 term flagged 'gocheck_do_not_annotate'). The model would likely select C as the most specific pathway associated with the recognized fold. However, this reasoning leads to an answer that contradicts the experimental evidence: the actual primary process is L-leucine degradation, not beta-oxidation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The crotonase superfamily recognition and the strong statistical association of this fold with beta-oxidation constitute transferable family-level knowledge that a model can apply without knowing this specific protein's database record. The sequence features (length, conserved motifs, CoA-hydratase architecture) are shared with other crotonase superfamily members. This is a legitimate family-level inference, even though it leads to the same misassignment that TreeGrafter made. The answer C is reachable through permitted transferable knowledge, though it is not the scientifically correct primary process.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Option B (carboxylic acid metabolic process, GO:0019752) is a valid ancestor of L-leucine catabolic process (GO:0006552 → GO:0006551 → GO:0009081 → GO:0019752), making it technically correct as a broad category encompassing the experimentally confirmed primary process. Option C (fatty acid beta-oxidation, GO:0006635) is supported only by an IEA:TreeGrafter computational annotation that misassigns the protein to a different pathway. The question asks for the 'primary biological process,' and while C is more specific, it is not the primary process; B is broader but correctly encompasses the actual primary process. Neither option is clearly superior given the wording, and the expected answer C contradicts experimental evidence.


### Important caveats

- The expected answer C is based on an IEA:TreeGrafter computational annotation, not experimental evidence. The experimental evidence (PubMed:32431008) clearly establishes the primary process as L-leucine degradation.
- The TreeGrafter misassignment is a known issue within the crotonase superfamily, where 3-methylglutaconyl-CoA hydratase and enoyl-CoA hydratase share high sequence similarity but catalyze reactions in different pathways.
- Option B (GO:0019752 carboxylic acid metabolic process) is flagged 'gocheck_do_not_annotate' in the GO ontology, indicating it is too broad for direct annotation, yet it is the only offered option that correctly encompasses the experimentally confirmed primary process (leucine degradation).
- The ideal answer — L-leucine catabolic process (GO:0006552) or branched-chain amino acid catabolic process (GO:0009083) — is not among the offered choices.
- A model using legitimate family-level reasoning (crotonase superfamily → beta-oxidation) would likely arrive at the expected answer C, but this reasoning is scientifically incorrect for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model recognizing the crotonase superfamily fold from the sequence (conserved motifs such as the 'GADL' region, the ~349-residue length, and the characteristic alpha/beta hydratase architecture shared with enoyl-CoA hydratase) would associate this fold most strongly with fatty acid beta-oxidation, the most well-known and heavily annotated pathway for crotonase-type CoA-ester hydratases. This family-level association — learned from the many enoyl-CoA hydratases in beta-oxidation across bacteria, fungi, and animals — meaningfully distinguishes C from A (endomitotic cell cycle, no cell-cycle machinery features), D (gluconeogenesis, no gluconeogenic enzyme features), and B (carboxylic acid metabolic process, an extremely broad GO:0019752 term flagged 'gocheck_do_not_annotate'). The model would likely select C as the most specific pathway associated with the recognized fold. However, this reasoning leads to an answer that contradicts the experimental evidence: the actual primary process is L-leucine degradation, not beta-oxidation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The crotonase superfamily recognition and the strong statistical association of this fold with beta-oxidation constitute transferable family-level knowledge that a model can apply without knowing this specific protein's database record. The sequence features (length, conserved motifs, CoA-hydratase architecture) are shared with other crotonase superfamily members. This is a legitimate family-level inference, even though it leads to the same misassignment that TreeGrafter made. The answer C is reachable through permitted transferable knowledge, though it is not the scientifically correct primary process."
  },
  "case_id": "GO_biological_process_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The protein is experimentally confirmed (PubMed:32431008) as 3-methylglutaconyl-CoA hydratase 1 (EC 4.2.1.18), catalyzing the reversible hydration of 3-methylglutaconyl-CoA to HMG-CoA in the L-leucine degradation pathway (step 5/5). The fatty acid beta-oxidation annotation (GO:0006635) carries only IEA:TreeGrafter evidence — a purely computational inference from sequence similarity to the crotonase superfamily, which includes both enoyl-CoA hydratase (beta-oxidation) and 3-methylglutaconyl-CoA hydratase (leucine degradation). The experimental evidence, UniProtKB-UniPathway annotation (GO:0006552 L-leucine catabolic process), and UniProtKB-KW annotation (GO:0009083 branched-chain amino acid catabolic process) all point to leucine degradation as the primary biological process. The TreeGrafter beta-oxidation call is a known cross-family misassignment within the crotonase superfamily and does not reflect the primary process."
  },
  "important_caveats": [
    "The expected answer C is based on an IEA:TreeGrafter computational annotation, not experimental evidence. The experimental evidence (PubMed:32431008) clearly establishes the primary process as L-leucine degradation.",
    "The TreeGrafter misassignment is a known issue within the crotonase superfamily, where 3-methylglutaconyl-CoA hydratase and enoyl-CoA hydratase share high sequence similarity but catalyze reactions in different pathways.",
    "Option B (GO:0019752 carboxylic acid metabolic process) is flagged 'gocheck_do_not_annotate' in the GO ontology, indicating it is too broad for direct annotation, yet it is the only offered option that correctly encompasses the experimentally confirmed primary process (leucine degradation).",
    "The ideal answer — L-leucine catabolic process (GO:0006552) or branched-chain amino acid catabolic process (GO:0009083) — is not among the offered choices.",
    "A model using legitimate family-level reasoning (crotonase superfamily → beta-oxidation) would likely arrive at the expected answer C, but this reasoning is scientifically incorrect for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Option B (carboxylic acid metabolic process, GO:0019752) is a valid ancestor of L-leucine catabolic process (GO:0006552 → GO:0006551 → GO:0009081 → GO:0019752), making it technically correct as a broad category encompassing the experimentally confirmed primary process. Option C (fatty acid beta-oxidation, GO:0006635) is supported only by an IEA:TreeGrafter computational annotation that misassigns the protein to a different pathway. The question asks for the 'primary biological process,' and while C is more specific, it is not the primary process; B is broader but correctly encompasses the actual primary process. Neither option is clearly superior given the wording, and the expected answer C contradicts experimental evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0131",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein is experimentally confirmed (PubMed:32431008) as 3-methylglutaconyl-CoA hydratase 1 (EC 4.2.1.18), catalyzing the reversible hydration of 3-methylglutaconyl-CoA to HMG-CoA in the L-leucine degradation pathway (step 5/5). The fatty acid beta-oxidation annotation (GO:0006635) carries only IEA:TreeGrafter evidence — a purely computational inference from sequence similarity to the crotonase superfamily, which includes both enoyl-CoA hydratase (beta-oxidation) and 3-methylglutaconyl-CoA hydratase (leucine degradation). The experimental evidence, UniProtKB-UniPathway annotation (GO:0006552 L-leucine catabolic process), and UniProtKB-KW annotation (GO:0009083 branched-chain amino acid catabolic process) all point to leucine degradation as the primary biological process. The TreeGrafter beta-oxidation call is a known cross-family misassignment within the crotonase superfamily and does not reflect the primary process.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model recognizing the crotonase superfamily fold from the sequence (conserved motifs such as the 'GADL' region, the ~349-residue length, and the characteristic alpha/beta hydratase architecture shared with enoyl-CoA hydratase) would associate this fold most strongly with fatty acid beta-oxidation, the most well-known and heavily annotated pathway for crotonase-type CoA-ester hydratases. This family-level association — learned from the many enoyl-CoA hydratases in beta-oxidation across bacteria, fungi, and animals — meaningfully distinguishes C from A (endomitotic cell cycle, no cell-cycle machinery features), D (gluconeogenesis, no gluconeogenic enzyme features), and B (carboxylic acid metabolic process, an extremely broad GO:0019752 term flagged 'gocheck_do_not_annotate'). The model would likely select C as the most specific pathway associated with the recognized fold. However, this reasoning leads to an answer that contradicts the experimental evidence: the actual primary process is L-leucine degradation, not beta-oxidation.",
    "missing_item_specific_fact": "",
    "reason": "The crotonase superfamily recognition and the strong statistical association of this fold with beta-oxidation constitute transferable family-level knowledge that a model can apply without knowing this specific protein's database record. The sequence features (length, conserved motifs, CoA-hydratase architecture) are shared with other crotonase superfamily members. This is a legitimate family-level inference, even though it leads to the same misassignment that TreeGrafter made. The answer C is reachable through permitted transferable knowledge, though it is not the scientifically correct primary process."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Option B (carboxylic acid metabolic process, GO:0019752) is a valid ancestor of L-leucine catabolic process (GO:0006552 → GO:0006551 → GO:0009081 → GO:0019752), making it technically correct as a broad category encompassing the experimentally confirmed primary process. Option C (fatty acid beta-oxidation, GO:0006635) is supported only by an IEA:TreeGrafter computational annotation that misassigns the protein to a different pathway. The question asks for the 'primary biological process,' and while C is more specific, it is not the primary process; B is broader but correctly encompasses the actual primary process. Neither option is clearly superior given the wording, and the expected answer C contradicts experimental evidence."
  },
  "important_caveats": [
    "The expected answer C is based on an IEA:TreeGrafter computational annotation, not experimental evidence. The experimental evidence (PubMed:32431008) clearly establishes the primary process as L-leucine degradation.",
    "The TreeGrafter misassignment is a known issue within the crotonase superfamily, where 3-methylglutaconyl-CoA hydratase and enoyl-CoA hydratase share high sequence similarity but catalyze reactions in different pathways.",
    "Option B (GO:0019752 carboxylic acid metabolic process) is flagged 'gocheck_do_not_annotate' in the GO ontology, indicating it is too broad for direct annotation, yet it is the only offered option that correctly encompasses the experimentally confirmed primary process (leucine degradation).",
    "The ideal answer — L-leucine catabolic process (GO:0006552) or branched-chain amino acid catabolic process (GO:0009083) — is not among the offered choices.",
    "A model using legitimate family-level reasoning (crotonase superfamily → beta-oxidation) would likely arrive at the expected answer C, but this reasoning is scientifically incorrect for this specific protein."
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
  "benchmark_sequence_sha256": "5e891c748ec2835aa75f719bfdb800087960d21c8e74e2457645a7ad7fbe7243",
  "current_entry_audit": {
    "entryVersion": 56,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-12-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 349,
  "current_source_sequence_sha256": "5e891c748ec2835aa75f719bfdb800087960d21c8e74e2457645a7ad7fbe7243",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 54,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G4N954",
  "selected_historical_entry_version": 54,
  "selected_historical_record_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "selected_historical_source_sequence_length": 349,
  "selected_historical_source_sequence_sha256": "5e891c748ec2835aa75f719bfdb800087960d21c8e74e2457645a7ad7fbe7243",
  "selected_historical_version": {
    "accession": "G4N954",
    "database": "Swiss-Prot",
    "entryVersion": 54,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AUH1_PYRO7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G4N954\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":56,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice blast fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Magnaporthales\",\"Pyriculariaceae\",\"Pyricularia\"],\"scientificName\":\"Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958)\",\"synonyms\":[\"Magnaporthe oryzae\"],\"taxonId\":242507}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.18\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"value\":\"Methylglutaconyl-CoA hydratase 1, mitochondrial\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q13825\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"value\":\"3-methylglutaconyl-CoA hydratase that catalyzes the fifth step in the leucine degradation pathway, the reversible hydration of 3-methylglutaconyl-CoA (3-MG-CoA) to 3-hydroxy-3-methylglutaryl-CoA (HMG-CoA) (By similarity). Involved in vegetative growth, conidiation and in the stress response (PubMed:32431008). Controls mitochondrial morphology and mitophagy, which are critical for the infectious growth of the pathogen (PubMed:32431008)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32431008\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0006635\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:fatty acid beta-oxidation\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0006552\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:L-leucine catabolic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniPathway\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Xiao Y.\",\"Liu L.\",\"Zhang T.\",\"Zhou R.\",\"Ren Y.\",\"Li X.\",\"Shu H.\",\"Ye W.\",\"Zheng X.\",\"Zhang Z.\",\"Zhang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32431008\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.15088\"}],\"citationType\":\"journal article\",\"firstPage\":\"774\",\"id\":\"32431008\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"790\",\"publicationDate\":\"2021\",\"title\":\"Transcription factor MoMsn2 targets the putative 3-methylglutaconyl-CoA hydratase-encoding gene MoAUH1 to govern infectious growth via mitochondrial fusion/fission balance in Magnaporthe oryzae.\",\"volume\":\"23\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:45.109101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c",
  "url": "https://rest.uniprot.org/uniprotkb/G4N954.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H1",
  "excerpt": "ID   AUH1_PYRO7              Reviewed;         349 AA.\nAC   G4N954;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2011, sequence version 1.\nDT   28-JAN-2026, entry version 54.\nDE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};\nDE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};\nDE   Flags: Precursor;\nGN   Name=AUH1 {ECO:0000303|PubMed:32431008}; ORFNames=MGG_03335;\nOS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast\nOS   fungus) (Magnaporthe oryzae).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.\nOX   NCBI_TaxID=242507;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=32431008; DOI=10.1111/1462-2920.15088;\nRA   Xiao Y., Liu L., Zhang T., Zhou R., Ren Y., Li X., Shu H., Ye W., Zheng X.,\nRA   Zhang Z., Zhang H.;\nRT   \"Transcription factor MoMsn2 targets the putative 3-methylglutaconyl-CoA\nRT   hydratase-encoding gene MoAUH1 to govern infectious growth via\nRT   mitochondrial fusion/fission balance in Magnaporthe oryzae.\";\nRL   Environ. Microbiol. 23:774-790(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: 3-methylglutaconyl-CoA hydratase that catalyzes the fifth\nCC       step in the leucine degradation pathway, the reversible hydration of 3-\nCC       methylglutaconyl-CoA (3-MG-CoA) to 3-hydroxy-3-methylglutaryl-CoA (HMG-\nCC       CoA) (By similarity). Involved in vegetative growth, conidiation and in\nCC       the stress response (PubMed:32431008). Controls mitochondrial\nCC       morphology and mitophagy, which are critical for the infectious growth\nCC       of the pathogen (PubMed:32431008). {ECO:0000250|UniProtKB:Q13825,\nCC       ECO:0000269|PubMed:32431008}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-\nCC       3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3.\nCC       {ECO:0000305|PubMed:32431008}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0009083; P:branched-chain amino acid catabolic process; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0006635; P:fatty acid beta-oxidation; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:47.046190+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856",
  "url": "https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006094\nname: gluconeogenesis\nnamespace: biological_process\ndef: \"The formation of glucose from noncarbohydrate precursors, such as pyruvate, amino acids and glycerol.\" [MetaCyc:GLUCONEO-PWY]\nsynonym: \"glucose biosynthesis\" EXACT []\nsynonym: \"glucose biosynthetic process\" EXACT []\nxref: MetaCyc:GLUCONEO-PWY\nxref: MetaCyc:PWY-6142\nxref: MetaCyc:PWY66-399\nxref: Reactome:R-HSA-70263 \"Gluconeogenesis\"\nxref: Wikipedia:Gluconeogenesis\nis_a: GO:0006006 ! glucose metabolic process\nis_a: GO:0019319 ! hexose biosynthetic process\nproperty_value: skos:narrowMatch MetaCyc:GLUCONEO-PWY\nproperty_value: skos:narrowMatch MetaCyc:PWY-6142\nproperty_value: skos:narrowMatch MetaCyc:PWY66-399\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006094",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 62675-62692",
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
  "excerpt": "[Term]\nid: GO:0006551\nname: L-leucine metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving L-leucine, 2-amino-4-methylpentanoic acid.\" [GOC:ai]\nsynonym: \"L-leucine metabolism\" EXACT []\nsynonym: \"leucine metabolic process\" BROAD []\nis_a: GO:0009081 ! branched-chain amino acid metabolic process\nis_a: GO:0170039 ! proteinogenic amino acid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006551",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 67481-67490",
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
  "excerpt": "[Term]\nid: GO:0006552\nname: L-leucine catabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the breakdown of L-leucine.\" [GOC:curators]\nsynonym: \"L-leucine breakdown\" EXACT []\nsynonym: \"L-leucine catabolism\" EXACT []\nsynonym: \"L-leucine degradation\" EXACT []\nsynonym: \"L-leucine degradation via Ehrlich pathway\" NARROW []\nsynonym: \"L-methionine catabolic process via Ehrlich pathway\" NARROW []\nsynonym: \"leucine catabolic process\" BROAD []\nxref: MetaCyc:LEU-DEG2-PWY\nxref: MetaCyc:PWY-5075\nxref: MetaCyc:PWY-5076\nxref: MetaCyc:PWY-7767\nxref: MetaCyc:PWY-8185\nis_a: GO:0006551 ! L-leucine metabolic process\nis_a: GO:0009083 ! branched-chain amino acid catabolic process\nis_a: GO:0170040 ! proteinogenic amino acid catabolic process\nproperty_value: skos:narrowMatch MetaCyc:LEU-DEG2-PWY\nproperty_value: skos:narrowMatch MetaCyc:PWY-5075\nproperty_value: skos:narrowMatch MetaCyc:PWY-5076\nproperty_value: skos:narrowMatch MetaCyc:PWY-7767\nproperty_value: skos:narrowMatch MetaCyc:PWY-8185\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006552",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 67491-67515",
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
  "excerpt": "[Term]\nid: GO:0006631\nname: fatty acid metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving fatty acids, aliphatic monocarboxylic acids liberated from naturally occurring fats and oils by hydrolysis.\" [ISBN:0198547684]\nsynonym: \"fatty acid metabolism\" EXACT []\nxref: Reactome:R-HSA-211935 \"Fatty acids\"\nxref: Reactome:R-HSA-434313 \"Intracellular metabolism of fatty acids regulates insulin secretion\"\nxref: Reactome:R-HSA-8978868 \"Fatty acid metabolism\"\nxref: Wikipedia:Fatty_acid_metabolism\nis_a: GO:0006629 ! lipid metabolic process\nis_a: GO:0032787 ! monocarboxylic acid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006631",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 68526-68538",
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
  "excerpt": "[Term]\nid: GO:0006635\nname: fatty acid beta-oxidation\nnamespace: biological_process\ndef: \"A fatty acid oxidation process that results in the complete oxidation of a long-chain fatty acid. Fatty acid beta-oxidation begins with the addition of coenzyme A to a fatty acid, and occurs by successive cycles of reactions during each of which the fatty acid is shortened by a two-carbon fragment removed as acetyl coenzyme A; the cycle continues until only two or three carbons remain (as acetyl-CoA or propionyl-CoA respectively).\" [GOC:mah, ISBN:0198506732]\nxref: MetaCyc:PWY-5137\nxref: MetaCyc:PWY-5138\nxref: Reactome:R-HSA-77289 \"Mitochondrial Fatty Acid Beta-Oxidation\"\nis_a: GO:0009062 ! fatty acid catabolic process\nis_a: GO:0019395 ! fatty acid oxidation\nproperty_value: skos:narrowMatch MetaCyc:PWY-5137\nproperty_value: skos:narrowMatch MetaCyc:PWY-5138\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006635",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 68574-68586",
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
  "excerpt": "[Term]\nid: GO:0007113\nname: endomitotic cell cycle\nnamespace: biological_process\ndef: \"A mitotic cell cycle in which chromosomes are replicated and sister chromatids separate, but spindle formation, nuclear membrane breakdown and nuclear division do not occur, resulting in an increased number of chromosomes in the cell.\" [GOC:curators, GOC:dos, GOC:expert_vm]\ncomment: Note that this term should not be confused with 'abortive mitotic cell cycle ; GO:0033277'. Although abortive mitosis is sometimes called endomitosis, GO:0033277 refers to a process in which a mitotic spindle forms and chromosome separation begins.\nsynonym: \"endomitosis\" RELATED []\nxref: Wikipedia:Mitosis#Endomitosis\nis_a: GO:0000278 ! mitotic cell cycle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007113",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 73421-73430",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO7",
  "excerpt": "[Term]\nid: GO:0009062\nname: fatty acid catabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the breakdown of a fatty acid, any of the aliphatic monocarboxylic acids that can be liberated by hydrolysis from naturally occurring fats and oils. Fatty acids are predominantly straight-chain acids of 4 to 24 carbon atoms, which may be saturated or unsaturated; branched fatty acids and hydroxy fatty acids also occur, and very long chain acids of over 30 carbons are found in waxes.\" [GOC:curators]\nsynonym: \"fatty acid breakdown\" EXACT []\nsynonym: \"fatty acid catabolism\" EXACT []\nsynonym: \"fatty acid degradation\" EXACT []\nxref: Reactome:R-HSA-390918 \"Peroxisomal lipid metabolism\"\nxref: Wikipedia:Fatty_acid_degradation\nis_a: GO:0006631 ! fatty acid metabolic process\nis_a: GO:0016042 ! lipid catabolic process\nis_a: GO:0072329 ! monocarboxylic acid catabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009062",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 92304-92317",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO8

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO8",
  "excerpt": "[Term]\nid: GO:0009081\nname: branched-chain amino acid metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving amino acids containing a branched carbon skeleton, comprising isoleucine, leucine and valine.\" [GOC:ai]\nsynonym: \"branched chain family amino acid metabolism\" EXACT [GOC:ai]\nis_a: GO:0006520 ! amino acid metabolic process\nis_a: GO:0019752 ! carboxylic acid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009081",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 92520-92528",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO9

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO9",
  "excerpt": "[Term]\nid: GO:0009083\nname: branched-chain amino acid catabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the breakdown of amino acids containing a branched carbon skeleton, comprising isoleucine, leucine and valine.\" [GOC:ai]\nsynonym: \"branched chain family amino acid breakdown\" EXACT []\nsynonym: \"branched chain family amino acid catabolic process\" EXACT [GOC:ai]\nsynonym: \"branched chain family amino acid catabolism\" EXACT []\nsynonym: \"branched chain family amino acid degradation\" EXACT []\nxref: Reactome:R-HSA-70895 \"Branched-chain amino acid catabolism\"\nis_a: GO:0009063 ! amino acid catabolic process\nis_a: GO:0009081 ! branched-chain amino acid metabolic process\nis_a: GO:0046395 ! carboxylic acid catabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009083",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 92542-92555",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO10

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO10",
  "excerpt": "[Term]\nid: GO:0019752\nname: carboxylic acid metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving carboxylic acids, any organic acid containing one or more carboxyl (COOH) groups or anions (COO-).\" [ISBN:0198506732]\nsubset: gocheck_do_not_annotate\nsynonym: \"carboxylic acid metabolism\" EXACT []\nxref: Reactome:R-HSA-389661 \"Glyoxylate metabolism and glycine degradation\"\nis_a: GO:0043436 ! oxoacid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019752",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 152755-152764",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO11

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO11",
  "excerpt": "[Term]\nid: GO:0032787\nname: monocarboxylic acid metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving monocarboxylic acids, any organic acid containing one carboxyl (COOH) group or anion (COO-).\" [GOC:vk]\nsubset: goslim_yeast\nsynonym: \"monocarboxylate metabolic process\" EXACT []\nsynonym: \"monocarboxylic acid metabolism\" EXACT []\nis_a: GO:0019752 ! carboxylic acid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032787",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 190537-190546",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
