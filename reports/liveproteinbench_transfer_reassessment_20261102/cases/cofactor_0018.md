# cofactor_0018

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0018.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — pyridoxal 5&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNSMHPETLMVHGGMDGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHALKDGDSAVYQRLWQPGVARFETALAELEHADEAVAFATGMAAMTAALLAAVNAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEAEIASAIQDDTGLVIVETPANPSLDLVDLDSVVAAAGTVPVLVDNTFCTPVLQQPIRHGAALVLHSATKYLGGHGDAMGGIIATNSDWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLAAHPAITAVHYPGLNGQDPRGLLGRQMSGGGAMIALELAGGFDAARSFVEHCSLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLEDDLIAALDASRAAA

[Multiple Choices]
A. pyridoxal 5'-phosphate
B. Cu(2+)
C. [4Fe-4S] cluster
D. [2Fe-2S] cluster
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

> The sequence-matched historical UniProt record annotates pyridoxal 5'-phosphate as the cofactor. That annotation is transferred by similarity from another UniProt entry (ECO:0000250), rather than evidence of a direct experiment on this exact protein; nevertheless, it supports the key and is consistent with the known PLP dependence of this enzyme family.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a PLP-dependent enzyme of the methionine gamma-lyase family. Transferable knowledge that this family uses PLP, together with the PLP-enzyme-like sequence/fold pattern, meaningfully favors option A over the copper and iron-sulfur cluster choices. This is a family-level inference, not a claim that the exact target's annotation was supplied.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the sequence's enzyme-family pattern provides a credible basis to distinguish PLP from the offered metal cofactors without knowing the target's database record. The family inference is probabilistic, not a direct measurement of cofactor binding in this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are distinct cofactor classes, and the PLP-dependent enzyme-family inference favors only A.


### Important caveats

- The reviewer-only cofactor annotation is similarity-transferred, not direct experimental evidence for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent enzyme of the methionine gamma-lyase family. Transferable knowledge that this family uses PLP, together with the PLP-enzyme-like sequence/fold pattern, meaningfully favors option A over the copper and iron-sulfur cluster choices. This is a family-level inference, not a claim that the exact target's annotation was supplied.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the sequence's enzyme-family pattern provides a credible basis to distinguish PLP from the offered metal cofactors without knowing the target's database record. The family inference is probabilistic, not a direct measurement of cofactor binding in this protein."
  },
  "case_id": "cofactor_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates pyridoxal 5'-phosphate as the cofactor. That annotation is transferred by similarity from another UniProt entry (ECO:0000250), rather than evidence of a direct experiment on this exact protein; nevertheless, it supports the key and is consistent with the known PLP dependence of this enzyme family."
  },
  "important_caveats": [
    "The reviewer-only cofactor annotation is similarity-transferred, not direct experimental evidence for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are distinct cofactor classes, and the PLP-dependent enzyme-family inference favors only A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates pyridoxal 5'-phosphate as the cofactor. That annotation is transferred by similarity from another UniProt entry (ECO:0000250), rather than evidence of a direct experiment on this exact protein; nevertheless, it supports the key and is consistent with the known PLP dependence of this enzyme family.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent enzyme of the methionine gamma-lyase family. Transferable knowledge that this family uses PLP, together with the PLP-enzyme-like sequence/fold pattern, meaningfully favors option A over the copper and iron-sulfur cluster choices. This is a family-level inference, not a claim that the exact target's annotation was supplied.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the sequence's enzyme-family pattern provides a credible basis to distinguish PLP from the offered metal cofactors without knowing the target's database record. The family inference is probabilistic, not a direct measurement of cofactor binding in this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are distinct cofactor classes, and the PLP-dependent enzyme-family inference favors only A."
  },
  "important_caveats": [
    "The reviewer-only cofactor annotation is similarity-transferred, not direct experimental evidence for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A1H1YBL2) annotates this protein as L-methionine gamma-lyase (EC 4.4.1.11), a well-established PLP-dependent enzyme. The cofactor annotation lists pyridoxal 5'-phosphate (ChEBI:597326). Although the evidence code is ECO:0000250 (inferred by similarity to A0A2H1K3G9), methionine gamma-lyase is a canonical member of the PLP fold type I superfamily, and PLP dependence is a well-established biochemical fact for this enzyme class across many characterized homologs.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmark features of fold type I PLP-dependent enzymes (the aminotransferase/decarboxylase superfamily): (1) The overall length (~393 aa) and domain architecture are consistent with the TIM-barrel fold of PLP fold type I enzymes. (2) Multiple 'GG' motifs appear in positions consistent with the conserved catalytic lysine environment (e.g., 'GGGAMIALELAGGF', 'GGHGDAMGGIIATNSDWAMRLRQ'), which in PLP enzymes forms the Schiff base with the cofactor. (3) The 'HP' motif in 'LHPMGAYLLHRG' is characteristic of PLP fold type I enzymes. (4) Critically, the sequence LACKS the Cys-rich motifs (CxxCxxC patterns) required for &#91;2Fe-2S&#93; or &#91;4Fe-4S&#93; cluster coordination, effectively ruling out options C and D. (5) The sequence also lacks the histidine-rich or mixed His/Cys motifs typical of Cu(2+) coordination sites (as in SOD, laccase, cytochrome oxidase), ruling out option B. These positive and negative sequence signatures allow a knowledgeable model to infer PLP dependence from family-level recognition of the PLP fold type I superfamily, without needing to identify this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model trained on general biochemistry and protein families can recognize the PLP fold type I architecture from sequence motifs (GG near catalytic Lys, HP motif, TIM-barrel spacing) and can exclude metal cofactors by the absence of their characteristic ligand-binding motifs. This is a legitimate family-level inference applicable across hundreds of characterized PLP enzymes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mutually exclusive cofactor types. The sequence clearly lacks Cys-rich motifs (ruling out both Fe-S clusters) and lacks His-rich motifs (ruling out Cu2+). Only PLP fold type I features are present. No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation is computational (ECO:0000250, by similarity), not from direct experimental cofactor reconstitution for this specific protein. However, PLP dependence of methionine gamma-lyase is well-established across characterized homologs.
- The reviewer-only evidence reveals the organism (Brevibacterium sandarakinum) and exact identity, which were not available to the evaluated model. The reasoning above relies only on sequence features and general family knowledge.
- The sequence does not contain an obvious single 'GG-K' catalytic lysine in the classic aspartate aminotransferase context, but the overall fold-type I signature is sufficiently recognizable for a probabilistic family assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmark features of fold type I PLP-dependent enzymes (the aminotransferase/decarboxylase superfamily): (1) The overall length (~393 aa) and domain architecture are consistent with the TIM-barrel fold of PLP fold type I enzymes. (2) Multiple 'GG' motifs appear in positions consistent with the conserved catalytic lysine environment (e.g., 'GGGAMIALELAGGF', 'GGHGDAMGGIIATNSDWAMRLRQ'), which in PLP enzymes forms the Schiff base with the cofactor. (3) The 'HP' motif in 'LHPMGAYLLHRG' is characteristic of PLP fold type I enzymes. (4) Critically, the sequence LACKS the Cys-rich motifs (CxxCxxC patterns) required for [2Fe-2S] or [4Fe-4S] cluster coordination, effectively ruling out options C and D. (5) The sequence also lacks the histidine-rich or mixed His/Cys motifs typical of Cu(2+) coordination sites (as in SOD, laccase, cytochrome oxidase), ruling out option B. These positive and negative sequence signatures allow a knowledgeable model to infer PLP dependence from family-level recognition of the PLP fold type I superfamily, without needing to identify this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model trained on general biochemistry and protein families can recognize the PLP fold type I architecture from sequence motifs (GG near catalytic Lys, HP motif, TIM-barrel spacing) and can exclude metal cofactors by the absence of their characteristic ligand-binding motifs. This is a legitimate family-level inference applicable across hundreds of characterized PLP enzymes."
  },
  "case_id": "cofactor_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1H1YBL2) annotates this protein as L-methionine gamma-lyase (EC 4.4.1.11), a well-established PLP-dependent enzyme. The cofactor annotation lists pyridoxal 5'-phosphate (ChEBI:597326). Although the evidence code is ECO:0000250 (inferred by similarity to A0A2H1K3G9), methionine gamma-lyase is a canonical member of the PLP fold type I superfamily, and PLP dependence is a well-established biochemical fact for this enzyme class across many characterized homologs."
  },
  "important_caveats": [
    "The UniProt annotation is computational (ECO:0000250, by similarity), not from direct experimental cofactor reconstitution for this specific protein. However, PLP dependence of methionine gamma-lyase is well-established across characterized homologs.",
    "The reviewer-only evidence reveals the organism (Brevibacterium sandarakinum) and exact identity, which were not available to the evaluated model. The reasoning above relies only on sequence features and general family knowledge.",
    "The sequence does not contain an obvious single 'GG-K' catalytic lysine in the classic aspartate aminotransferase context, but the overall fold-type I signature is sufficiently recognizable for a probabilistic family assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive cofactor types. The sequence clearly lacks Cys-rich motifs (ruling out both Fe-S clusters) and lacks His-rich motifs (ruling out Cu2+). Only PLP fold type I features are present. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1H1YBL2) annotates this protein as L-methionine gamma-lyase (EC 4.4.1.11), a well-established PLP-dependent enzyme. The cofactor annotation lists pyridoxal 5'-phosphate (ChEBI:597326). Although the evidence code is ECO:0000250 (inferred by similarity to A0A2H1K3G9), methionine gamma-lyase is a canonical member of the PLP fold type I superfamily, and PLP dependence is a well-established biochemical fact for this enzyme class across many characterized homologs.",
    "evidence_ids": ["C5", "H3", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmark features of fold type I PLP-dependent enzymes (the aminotransferase/decarboxylase superfamily): (1) The overall length (~393 aa) and domain architecture are consistent with the TIM-barrel fold of PLP fold type I enzymes. (2) Multiple 'GG' motifs appear in positions consistent with the conserved catalytic lysine environment (e.g., 'GGGAMIALELAGGF', 'GGHGDAMGGIIATNSDWAMRLRQ'), which in PLP enzymes forms the Schiff base with the cofactor. (3) The 'HP' motif in 'LHPMGAYLLHRG' is characteristic of PLP fold type I enzymes. (4) Critically, the sequence LACKS the Cys-rich motifs (CxxCxxC patterns) required for [2Fe-2S] or [4Fe-4S] cluster coordination, effectively ruling out options C and D. (5) The sequence also lacks the histidine-rich or mixed His/Cys motifs typical of Cu(2+) coordination sites (as in SOD, laccase, cytochrome oxidase), ruling out option B. These positive and negative sequence signatures allow a knowledgeable model to infer PLP dependence from family-level recognition of the PLP fold type I superfamily, without needing to identify this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "A model trained on general biochemistry and protein families can recognize the PLP fold type I architecture from sequence motifs (GG near catalytic Lys, HP motif, TIM-barrel spacing) and can exclude metal cofactors by the absence of their characteristic ligand-binding motifs. This is a legitimate family-level inference applicable across hundreds of characterized PLP enzymes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive cofactor types. The sequence clearly lacks Cys-rich motifs (ruling out both Fe-S clusters) and lacks His-rich motifs (ruling out Cu2+). Only PLP fold type I features are present. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation is computational (ECO:0000250, by similarity), not from direct experimental cofactor reconstitution for this specific protein. However, PLP dependence of methionine gamma-lyase is well-established across characterized homologs.",
    "The reviewer-only evidence reveals the organism (Brevibacterium sandarakinum) and exact identity, which were not available to the evaluated model. The reasoning above relies only on sequence features and general family knowledge.",
    "The sequence does not contain an obvious single 'GG-K' catalytic lysine in the classic aspartate aminotransferase context, but the overall fold-type I signature is sufficiently recognizable for a probabilistic family assignment."
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
  "benchmark_sequence_length": 393,
  "benchmark_sequence_sha256": "d62ef1248b2c7e60f020a849ac08272c51994b6267c0d401825afaddef80c605",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-01-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 393,
  "current_source_sequence_sha256": "d62ef1248b2c7e60f020a849ac08272c51994b6267c0d401825afaddef80c605",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1H1YBL2",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2",
  "selected_historical_source_sequence_length": 393,
  "selected_historical_source_sequence_sha256": "d62ef1248b2c7e60f020a849ac08272c51994b6267c0d401825afaddef80c605",
  "selected_historical_version": {
    "accession": "A0A1H1YBL2",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MEGL_BRESA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1H1YBL2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-01-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Micrococcales\",\"Brevibacteriaceae\",\"Brevibacterium\"],\"scientificName\":\"Brevibacterium sandarakinum\",\"taxonId\":629680}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"4.4.1.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"Homocysteine desulfhydrase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"4.4.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"L-methionine gamma-lyase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"value\":\"MGL\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:597326\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A2H1K3G9\",\"source\":\"UniProtKB\"}],\"name\":\"pyridoxal 5'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:35.559742+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f5674fa9408e7d3987f379a501b18c3e46ccc978eeb5437c6fe35fdcc0e36ab",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1H1YBL2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   MEGL_BRESA              Reviewed;         393 AA.\nAC   A0A1H1YBL2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JAN-2017, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=L-methionine gamma-lyase {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            Short=MGL {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            EC=4.4.1.11 {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            EC=4.4.1.2 {ECO:0000250|UniProtKB:A0A2H1K3G9};\nGN   ORFNames=SAMN04489751_4033 {ECO:0000312|EMBL:SDT18406.1};\nOS   Brevibacterium sandarakinum.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales;\nOC   Brevibacteriaceae; Brevibacterium.\nOX   NCBI_TaxID=629680;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.341815+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2",
  "url": "https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-methionine gamma-lyase {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            Short=MGL {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            EC=4.4.1.11 {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000250|UniProtKB:A0A2H1K3G9};\nDE            EC=4.4.1.2 {ECO:0000250|UniProtKB:A0A2H1K3G9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.341815+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2",
  "url": "https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;\nCC         Evidence={ECO:0000250|UniProtKB:A0A2H1K3G9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.341815+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5e5688fed3c5afbeb1081e5c750f61df902b7913de336d8e81a8000a21e4f8f2",
  "url": "https://rest.uniprot.org/unisave/A0A1H1YBL2?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 18. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
