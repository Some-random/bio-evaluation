# cofactor_0126

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0126.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — FAD

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNNQSAKKSPTRLTYISDIIEISPYLRRLVLSGEQLANFPADQQGAYVKVLIPQPGETTVNMTLTGPNAAIKRSYTIREFDPVRGQLSLDFVINKHTGPATDWAKLANVGDTVAIAGPGPLKMNRFDFNDYLLFGDSTSINAVDALIKRLPATAKGHIIMLVNSHQEQALLSQHPLLKTHWLVLNDSITAEQQIDWLLDKLELFGDLPAVTQVFVGLEATQVRVIKQYLLEQQQLPLSSISATGYWKRNTDADTFGKQKQMQPL

[Multiple Choices]
A. Mn(2+)
B. pantetheine 4'-phosphate
C. Co(2+)
D. FAD
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the UniProt sequence, whose cofactor annotation identifies FAD with experimental evidence. The cited structural study also reports the protein crystallized in complex with FAD. This supports choice D, while the annotation does not establish that the other listed compounds are never present under any condition.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A credible sequence-family inference is that this compact bacterial enzyme belongs to the siderophore-interacting/reductase family, whose related enzymes use flavin chemistry; that makes FAD a meaningful prediction for an oxidoreductase, rather than a transition-metal ion or pantetheine 4'-phosphate. This is a probabilistic family-level inference, not a proof from a single diagnostic motif.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The full sequence can support family recognition or homology-based inference transferable from related proteins, which meaningfully favors FAD among these choices. The exact protein's experimental cofactor measurement would strengthen the answer but is not necessary to make a defensible prediction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports FAD, and no other offered choice is comparably defensible.


### Important caveats

- The family-level sequence inference is less conclusive than the reviewer-only experimental and structural evidence.
- The source evidence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A credible sequence-family inference is that this compact bacterial enzyme belongs to the siderophore-interacting/reductase family, whose related enzymes use flavin chemistry; that makes FAD a meaningful prediction for an oxidoreductase, rather than a transition-metal ion or pantetheine 4'-phosphate. This is a probabilistic family-level inference, not a proof from a single diagnostic motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The full sequence can support family recognition or homology-based inference transferable from related proteins, which meaningfully favors FAD among these choices. The exact protein's experimental cofactor measurement would strengthen the answer but is not necessary to make a defensible prediction."
  },
  "case_id": "cofactor_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt sequence, whose cofactor annotation identifies FAD with experimental evidence. The cited structural study also reports the protein crystallized in complex with FAD. This supports choice D, while the annotation does not establish that the other listed compounds are never present under any condition."
  },
  "important_caveats": [
    "The family-level sequence inference is less conclusive than the reviewer-only experimental and structural evidence.",
    "The source evidence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports FAD, and no other offered choice is comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt sequence, whose cofactor annotation identifies FAD with experimental evidence. The cited structural study also reports the protein crystallized in complex with FAD. This supports choice D, while the annotation does not establish that the other listed compounds are never present under any condition.",
    "evidence_ids": ["C5", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A credible sequence-family inference is that this compact bacterial enzyme belongs to the siderophore-interacting/reductase family, whose related enzymes use flavin chemistry; that makes FAD a meaningful prediction for an oxidoreductase, rather than a transition-metal ion or pantetheine 4'-phosphate. This is a probabilistic family-level inference, not a proof from a single diagnostic motif.",
    "missing_item_specific_fact": "",
    "reason": "The full sequence can support family recognition or homology-based inference transferable from related proteins, which meaningfully favors FAD among these choices. The exact protein's experimental cofactor measurement would strengthen the answer but is not necessary to make a defensible prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports FAD, and no other offered choice is comparably defensible."
  },
  "important_caveats": [
    "The family-level sequence inference is less conclusive than the reviewer-only experimental and structural evidence.",
    "The source evidence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q080S8 annotates FAD as the cofactor with experimental evidence (ECO:0000269) from two independent studies. The 2019 crystal structure (PDB 6GEH, 1.15 Å) explicitly shows the protein 'IN COMPLEX WITH FAD' (evidence C7/H4). The 2016 crystallization paper also confirms the cofactor (C6/H3). This is direct structural experimental evidence, not mere computational annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The siderophore-interacting protein (SIP) family is a well-characterized group of flavoproteins found across multiple organisms (E. coli, Shewanella spp., Pseudomonas, etc.) that consistently use FAD as their cofactor for reducing ferric siderophores. A knowledgeable model could recognize the ~264-aa protein as belonging to this family based on sequence architecture. The sequence contains glycine-rich regions (e.g., 'AIAGPGPLKMNRFDFNDYLLFGD' around residues 100-125) consistent with a modified Rossmann-type FAD-binding fold found in flavoprotein reductases. Additionally, the protein is clearly an oxidoreductase (reductase activity), and among the four choices, FAD is the only organic cofactor appropriate for a small flavoprotein reductase. Mn(2+) and Co(2+) are metal cofactors typical of metalloenzymes (oxidases, superoxide dismutases, etc.), and pantetheine 4'-phosphate is a component of acyl-carrier proteins and CoA-dependent acyltransferases—none of which match a small reductase of this size and composition. Family-level knowledge from other SIP proteins (all flavoproteins) combined with the reductase function and sequence motifs meaningfully distinguishes FAD from the three distractors.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about the SIP flavoprotein family across multiple organisms, the reductase function implied by the sequence context, glycine-rich FAD-binding-like motifs in the sequence, and the inappropriateness of metal cofactors and pantetheine 4'-phosphate for a small reductase collectively allow a knowledgeable model to select FAD without needing to look up this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are functionally distinct: two metal ions (Mn2+, Co2+), one acyl-carrier component (pantetheine 4'-phosphate), and one flavin (FAD). For a small reductase with flavoprotein-like sequence features, only FAD is a defensible cofactor. No other option is biologically plausible for this protein class.


### Important caveats

- The glycine-rich motifs in this sequence are suggestive but not textbook-perfect GxGxxG Rossmann motifs; the primary strength of the inference comes from SIP-family knowledge and functional logic rather than a single unambiguous sequence motif.
- The reviewer-only evidence confirms FAD by crystallography at 1.15 Å, but this target-specific structural fact was not available to the evaluated model.
- The SIP family is well-established as flavoproteins across multiple species, making this a legitimate family-level transfer rather than target-specific memorization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The siderophore-interacting protein (SIP) family is a well-characterized group of flavoproteins found across multiple organisms (E. coli, Shewanella spp., Pseudomonas, etc.) that consistently use FAD as their cofactor for reducing ferric siderophores. A knowledgeable model could recognize the ~264-aa protein as belonging to this family based on sequence architecture. The sequence contains glycine-rich regions (e.g., 'AIAGPGPLKMNRFDFNDYLLFGD' around residues 100-125) consistent with a modified Rossmann-type FAD-binding fold found in flavoprotein reductases. Additionally, the protein is clearly an oxidoreductase (reductase activity), and among the four choices, FAD is the only organic cofactor appropriate for a small flavoprotein reductase. Mn(2+) and Co(2+) are metal cofactors typical of metalloenzymes (oxidases, superoxide dismutases, etc.), and pantetheine 4'-phosphate is a component of acyl-carrier proteins and CoA-dependent acyltransferases—none of which match a small reductase of this size and composition. Family-level knowledge from other SIP proteins (all flavoproteins) combined with the reductase function and sequence motifs meaningfully distinguishes FAD from the three distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about the SIP flavoprotein family across multiple organisms, the reductase function implied by the sequence context, glycine-rich FAD-binding-like motifs in the sequence, and the inappropriateness of metal cofactors and pantetheine 4'-phosphate for a small reductase collectively allow a knowledgeable model to select FAD without needing to look up this exact protein's database entry."
  },
  "case_id": "cofactor_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q080S8 annotates FAD as the cofactor with experimental evidence (ECO:0000269) from two independent studies. The 2019 crystal structure (PDB 6GEH, 1.15 Å) explicitly shows the protein 'IN COMPLEX WITH FAD' (evidence C7/H4). The 2016 crystallization paper also confirms the cofactor (C6/H3). This is direct structural experimental evidence, not mere computational annotation."
  },
  "important_caveats": [
    "The glycine-rich motifs in this sequence are suggestive but not textbook-perfect GxGxxG Rossmann motifs; the primary strength of the inference comes from SIP-family knowledge and functional logic rather than a single unambiguous sequence motif.",
    "The reviewer-only evidence confirms FAD by crystallography at 1.15 Å, but this target-specific structural fact was not available to the evaluated model.",
    "The SIP family is well-established as flavoproteins across multiple species, making this a legitimate family-level transfer rather than target-specific memorization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are functionally distinct: two metal ions (Mn2+, Co2+), one acyl-carrier component (pantetheine 4'-phosphate), and one flavin (FAD). For a small reductase with flavoprotein-like sequence features, only FAD is a defensible cofactor. No other option is biologically plausible for this protein class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q080S8 annotates FAD as the cofactor with experimental evidence (ECO:0000269) from two independent studies. The 2019 crystal structure (PDB 6GEH, 1.15 Å) explicitly shows the protein 'IN COMPLEX WITH FAD' (evidence C7/H4). The 2016 crystallization paper also confirms the cofactor (C6/H3). This is direct structural experimental evidence, not mere computational annotation.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The siderophore-interacting protein (SIP) family is a well-characterized group of flavoproteins found across multiple organisms (E. coli, Shewanella spp., Pseudomonas, etc.) that consistently use FAD as their cofactor for reducing ferric siderophores. A knowledgeable model could recognize the ~264-aa protein as belonging to this family based on sequence architecture. The sequence contains glycine-rich regions (e.g., 'AIAGPGPLKMNRFDFNDYLLFGD' around residues 100-125) consistent with a modified Rossmann-type FAD-binding fold found in flavoprotein reductases. Additionally, the protein is clearly an oxidoreductase (reductase activity), and among the four choices, FAD is the only organic cofactor appropriate for a small flavoprotein reductase. Mn(2+) and Co(2+) are metal cofactors typical of metalloenzymes (oxidases, superoxide dismutases, etc.), and pantetheine 4'-phosphate is a component of acyl-carrier proteins and CoA-dependent acyltransferases—none of which match a small reductase of this size and composition. Family-level knowledge from other SIP proteins (all flavoproteins) combined with the reductase function and sequence motifs meaningfully distinguishes FAD from the three distractors.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about the SIP flavoprotein family across multiple organisms, the reductase function implied by the sequence context, glycine-rich FAD-binding-like motifs in the sequence, and the inappropriateness of metal cofactors and pantetheine 4'-phosphate for a small reductase collectively allow a knowledgeable model to select FAD without needing to look up this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are functionally distinct: two metal ions (Mn2+, Co2+), one acyl-carrier component (pantetheine 4'-phosphate), and one flavin (FAD). For a small reductase with flavoprotein-like sequence features, only FAD is a defensible cofactor. No other option is biologically plausible for this protein class."
  },
  "important_caveats": [
    "The glycine-rich motifs in this sequence are suggestive but not textbook-perfect GxGxxG Rossmann motifs; the primary strength of the inference comes from SIP-family knowledge and functional logic rather than a single unambiguous sequence motif.",
    "The reviewer-only evidence confirms FAD by crystallography at 1.15 Å, but this target-specific structural fact was not available to the evaluated model.",
    "The SIP family is well-established as flavoproteins across multiple species, making this a legitimate family-level transfer rather than target-specific memorization."
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
  "benchmark_sequence_length": 264,
  "benchmark_sequence_sha256": "c5be18c4780bd1933beb115f53469a80b596589a4797f641cba94158693e1bc7",
  "current_entry_audit": {
    "entryVersion": 89,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-31",
    "sequenceVersion": 1
  },
  "current_record_sha256": "686e85b61c68a5a8c93fdec852b4ffb69a3e80fa2cdc6f5ae39dc48863ab8205",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 264,
  "current_source_sequence_sha256": "c5be18c4780bd1933beb115f53469a80b596589a4797f641cba94158693e1bc7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q080S8",
  "selected_historical_entry_version": 87,
  "selected_historical_record_sha256": "a09704b0cc2c3c108c0bf443c4fdd4c81200287642bfdad87485ed0483be730a",
  "selected_historical_source_sequence_length": 264,
  "selected_historical_source_sequence_sha256": "c5be18c4780bd1933beb115f53469a80b596589a4797f641cba94158693e1bc7",
  "selected_historical_version": {
    "accession": "Q080S8",
    "database": "Swiss-Prot",
    "entryVersion": 87,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SFSIP_SHEFN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q080S8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q080S8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:20.736442+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "686e85b61c68a5a8c93fdec852b4ffb69a3e80fa2cdc6f5ae39dc48863ab8205",
  "url": "https://rest.uniprot.org/uniprotkb/Q080S8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q080S8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":89,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-31\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:20.736442+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "686e85b61c68a5a8c93fdec852b4ffb69a3e80fa2cdc6f5ae39dc48863ab8205",
  "url": "https://rest.uniprot.org/uniprotkb/Q080S8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q080S8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Alteromonadales\",\"Shewanellaceae\",\"Shewanella\"],\"scientificName\":\"Shewanella frigidimarina (strain NCIMB 400)\",\"taxonId\":318167}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:20.736442+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "686e85b61c68a5a8c93fdec852b4ffb69a3e80fa2cdc6f5ae39dc48863ab8205",
  "url": "https://rest.uniprot.org/uniprotkb/Q080S8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q080S8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30420426\",\"source\":\"PubMed\"}],\"value\":\"SfSIP\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27599855\",\"source\":\"PubMed\"}],\"value\":\"Siderophore-interacting protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27599855\",\"source\":\"PubMed\"}],\"value\":\"SIP\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30420426\",\"source\":\"PubMed\"}],\"value\":\"1.16.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30420426\",\"source\":\"PubMed\"}],\"value\":\"Ferric siderophore reductase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:20.736442+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "686e85b61c68a5a8c93fdec852b4ffb69a3e80fa2cdc6f5ae39dc48863ab8205",
  "url": "https://rest.uniprot.org/uniprotkb/Q080S8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q080S8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27599855\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30420426\",\"source\":\"PubMed\"}],\"name\":\"FAD\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:20.736442+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "686e85b61c68a5a8c93fdec852b4ffb69a3e80fa2cdc6f5ae39dc48863ab8205",
  "url": "https://rest.uniprot.org/uniprotkb/Q080S8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q080S8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Trindade I.B.\",\"Fonseca B.M.\",\"Matias P.M.\",\"Louro R.O.\",\"Moe E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27599855\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2053230x16011419\"}],\"citationType\":\"journal article\",\"firstPage\":\"667\",\"id\":\"27599855\",\"journal\":\"Acta Crystallogr. F Struct. Biol. Commun.\",\"lastPage\":\"671\",\"publicationDate\":\"2016\",\"title\":\"A putative siderophore-interacting protein from the marine bacterium Shewanella frigidimarina NCIMB 400: cloning, expression, purification, crystallization and X-ray diffraction analysis.\",\"volume\":\"72\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"NCIMB 400\"}],\"referenceNumber\":2,\"referencePositions\":[\"COFACTOR\",\"CRYSTALLIZATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:20.736442+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "686e85b61c68a5a8c93fdec852b4ffb69a3e80fa2cdc6f5ae39dc48863ab8205",
  "url": "https://rest.uniprot.org/uniprotkb/Q080S8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q080S8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Trindade I.B.\",\"Silva J.M.\",\"Fonseca B.M.\",\"Catarino T.\",\"Fujita M.\",\"Matias P.M.\",\"Moe E.\",\"Louro R.O.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30420426\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.ra118.005041\"}],\"citationType\":\"journal article\",\"firstPage\":\"157\",\"id\":\"30420426\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"167\",\"publicationDate\":\"2019\",\"title\":\"Structure and reactivity of a siderophore-interacting protein from the marine bacterium Shewanella reveals unanticipated functional versatility.\",\"volume\":\"294\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6GEH\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"NCIMB 400\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.15 ANGSTROMS) OF 9-264 IN COMPLEX WITH FAD\",\"FUNCTION AS A REDUCTASE\",\"COFACTOR\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:20.736442+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "686e85b61c68a5a8c93fdec852b4ffb69a3e80fa2cdc6f5ae39dc48863ab8205",
  "url": "https://rest.uniprot.org/uniprotkb/Q080S8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H1",
  "excerpt": "ID   SFSIP_SHEFN             Reviewed;         264 AA.\nAC   Q080S8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   31-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=Ferric siderophore reductase {ECO:0000303|PubMed:30420426};\nDE            EC=1.16.-.- {ECO:0000269|PubMed:30420426};\nDE   AltName: Full=SfSIP {ECO:0000303|PubMed:30420426};\nDE   AltName: Full=Siderophore-interacting protein {ECO:0000303|PubMed:27599855};\nDE            Short=SIP {ECO:0000303|PubMed:27599855};\nGN   OrderedLocusNames=Sfri_2392 {ECO:0000312|EMBL:ABI72237.1};\nOS   Shewanella frigidimarina (strain NCIMB 400).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Alteromonadales; Shewanellaceae; Shewanella.\nOX   NCBI_TaxID=318167;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.501275+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a09704b0cc2c3c108c0bf443c4fdd4c81200287642bfdad87485ed0483be730a",
  "url": "https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ferric siderophore reductase {ECO:0000303|PubMed:30420426};\nDE            EC=1.16.-.- {ECO:0000269|PubMed:30420426};\nDE   AltName: Full=SfSIP {ECO:0000303|PubMed:30420426};\nDE   AltName: Full=Siderophore-interacting protein {ECO:0000303|PubMed:27599855};\nDE            Short=SIP {ECO:0000303|PubMed:27599855};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.501275+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a09704b0cc2c3c108c0bf443c4fdd4c81200287642bfdad87485ed0483be730a",
  "url": "https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   COFACTOR, AND CRYSTALLIZATION.\nRC   STRAIN=NCIMB 400;\nRX   PubMed=27599855; DOI=10.1107/s2053230x16011419;\nRA   Trindade I.B., Fonseca B.M., Matias P.M., Louro R.O., Moe E.;\nRT   \"A putative siderophore-interacting protein from the marine bacterium\nRT   Shewanella frigidimarina NCIMB 400: cloning, expression, purification,\nRT   crystallization and X-ray diffraction analysis.\";\nRL   Acta Crystallogr. F Struct. Biol. Commun. 72:667-671(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.501275+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a09704b0cc2c3c108c0bf443c4fdd4c81200287642bfdad87485ed0483be730a",
  "url": "https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H4",
  "excerpt": "RN   [3] {ECO:0007744|PDB:6GEH}\nRP   X-RAY CRYSTALLOGRAPHY (1.15 ANGSTROMS) OF 9-264 IN COMPLEX WITH FAD,\nRP   FUNCTION AS A REDUCTASE, AND COFACTOR.\nRC   STRAIN=NCIMB 400;\nRX   PubMed=30420426; DOI=10.1074/jbc.ra118.005041;\nRA   Trindade I.B., Silva J.M., Fonseca B.M., Catarino T., Fujita M.,\nRA   Matias P.M., Moe E., Louro R.O.;\nRT   \"Structure and reactivity of a siderophore-interacting protein from the\nRT   marine bacterium Shewanella reveals unanticipated functional versatility.\";\nRL   J. Biol. Chem. 294:157-167(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.501275+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a09704b0cc2c3c108c0bf443c4fdd4c81200287642bfdad87485ed0483be730a",
  "url": "https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FAD; Xref=ChEBI:CHEBI:57692;\nCC         Evidence={ECO:0000269|PubMed:27599855, ECO:0000269|PubMed:30420426};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.501275+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a09704b0cc2c3c108c0bf443c4fdd4c81200287642bfdad87485ed0483be730a",
  "url": "https://rest.uniprot.org/unisave/Q080S8?format=txt&versions=87"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 126. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
