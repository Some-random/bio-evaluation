# EC_number_0046

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0046.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 4.2.1.183

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKPAAAAPSDPSKPSKPLKEVPGSYGLPVLGAVKDRLDFYWFQGDTEFFRIRMEQHKSTVFRVNYSPGPPGYPDSRGIILLDQKSFSVLLDNSKVDKSDTLLGPYIPNLAFTGGYRVLPYLDTSEAKHTAYKDLIFELLHVNSSRIIPEYNKVFAETAGSWEERIAKSGKAEVFASSDSMITKFLLRTIVHKDPAEPGPASLGPKFRDTYQLWTGVNFAGIAHTPLPHFLEELLFHTFRLPPFLVKKQYKALANFYRTHATEVLDLAEKKYGLDREETVHQLILILGINARLGLHKMIPALIYYLGLLGEDFQAKIAAEVRSAVHKNRAQGEEGVNITTQALLEMPLLRSTVLETLRLTPSIFYIYGRAREDMVIESHDAAFQIKKGELLGGHQYFVMRDPEVFEEPHKFVADRFLGERGKAVLPYLVWSNGRETESPSSSNKQCPAKDVAELITMQFVAEMFLRYDSFEITKDSFINTTELNVHLKSLKKRSV

[Multiple Choices]
A. 4.2.1.70
B. 2.3.1.319
C. 4.2.1.183
D. 2.1.2.1
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the source sequence, and the curated entry assigns EC 4.2.1.183 to the enzyme and its catalytic reactions. The annotation cites experimental evidence (ECO:0000269, PubMed 26776054), although the primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the plant CYP74 family of fatty-acid-hydroperoxide-metabolizing P450-related enzymes. Transferable sequence and family knowledge can distinguish a CYP74-like enzyme from the unrelated transferase choices B and D; similarity to divinyl ether synthase members provides a credible basis to favor C over the other offered lyase choice A. This is a probabilistic family-level inference, not a direct measurement of this protein's reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers a meaningful family-based route to the divinyl ether synthase EC class, so the answer need not depend on recalling this exact protein's database record. The precise functional assignment among related CYP74 enzymes may remain uncertain from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second option is comparably supported by the sequence and transferable family-level inference among the choices provided.


### Important caveats

- The reviewer-only source supports the key but was not available as original input.
- CYP74 family recognition alone does not experimentally establish the exact reaction; the inference to C is probabilistic.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the plant CYP74 family of fatty-acid-hydroperoxide-metabolizing P450-related enzymes. Transferable sequence and family knowledge can distinguish a CYP74-like enzyme from the unrelated transferase choices B and D; similarity to divinyl ether synthase members provides a credible basis to favor C over the other offered lyase choice A. This is a probabilistic family-level inference, not a direct measurement of this protein's reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a meaningful family-based route to the divinyl ether synthase EC class, so the answer need not depend on recalling this exact protein's database record. The precise functional assignment among related CYP74 enzymes may remain uncertain from sequence alone."
  },
  "case_id": "EC_number_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the source sequence, and the curated entry assigns EC 4.2.1.183 to the enzyme and its catalytic reactions. The annotation cites experimental evidence (ECO:0000269, PubMed 26776054), although the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only source supports the key but was not available as original input.",
    "CYP74 family recognition alone does not experimentally establish the exact reaction; the inference to C is probabilistic."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is comparably supported by the sequence and transferable family-level inference among the choices provided."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the source sequence, and the curated entry assigns EC 4.2.1.183 to the enzyme and its catalytic reactions. The annotation cites experimental evidence (ECO:0000269, PubMed 26776054), although the primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the plant CYP74 family of fatty-acid-hydroperoxide-metabolizing P450-related enzymes. Transferable sequence and family knowledge can distinguish a CYP74-like enzyme from the unrelated transferase choices B and D; similarity to divinyl ether synthase members provides a credible basis to favor C over the other offered lyase choice A. This is a probabilistic family-level inference, not a direct measurement of this protein's reaction.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a meaningful family-based route to the divinyl ether synthase EC class, so the answer need not depend on recalling this exact protein's database record. The precise functional assignment among related CYP74 enzymes may remain uncertain from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is comparably supported by the sequence and transferable family-level inference among the choices provided."
  },
  "important_caveats": [
    "The reviewer-only source supports the key but was not available as original input.",
    "CYP74 family recognition alone does not experimentally establish the exact reaction; the inference to C is probabilistic."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry D8QZ31 (C74M3_SELML) confirms EC 4.2.1.183 (Divinyl ether synthase CYP74M3) with experimental evidence (ECO:0000269, PubMed:26776054). The sequence in the benchmark matches the UniProt entry exactly (495 aa, SHA256 matched). The catalytic activity is the conversion of (13S)-hydroperoxy fatty acids to divinyl ethers + H2O, consistent with EC 4.2.1.183.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~495 aa) contains P450-characteristic features: a hydrophobic N-terminal membrane-anchoring region, the I-helix-like segment (GIAHTPLPHFLEELLFHTFRLPP), and a heme-binding region with a conserved cysteine (QCPAKD). This identifies the protein as a cytochrome P450. Transferable knowledge from the oxylipin/P450 literature establishes that the CYP74 family (unlike typical P450s classified as EC 1.14.x.x monooxygenases) catalyzes internal rearrangements of hydroperoxy fatty acids and is classified as hydro-lyases (EC 4.2.x.x). This eliminates B (EC 2.3.1.319, an acyltransferase) and D (EC 2.1.2.1, formate-THF ligase), neither of which are P450s. Between A (4.2.1.70) and C (4.2.1.183): EC 4.2.1.70 does not correspond to a known CYP74-family divinyl ether synthase or any P450-type hydro-lyase in standard nomenclature, making it an implausible assignment for a P450 sequence. EC 4.2.1.183 is the specific EC number assigned to CYP74M-type divinyl ether synthases. A model recognizing P450 architecture + CYP74-family lyase classification + elimination of the non-P450 options and the non-P450-compatible EC 4.2.1.70 can arrive at C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P450 fold is recognizable from sequence length, hydrophobic segments, I-helix motif, and heme-cysteine region. The CYP74→lyase (EC 4.2.x.x) classification is transferable knowledge from oxylipin metabolism literature. Options B and D are eliminated by P450 recognition. The remaining distinction between A and C relies on knowing that EC 4.2.1.70 is not a valid/assigned EC number for a P450-type enzyme, while 4.2.1.183 is the established number for CYP74M divinyl ether synthases. This is a family-level inference rather than a lookup of this exact protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly incompatible with a P450 architecture. Option A (EC 4.2.1.70) does not correspond to a known P450-family hydro-lyase in current EC nomenclature, making it an implausible assignment for this sequence. Option C is the only EC number consistent with both the P450 architecture and the CYP74 lyase classification.


### Important caveats

- The identification of this as specifically CYP74M (vs. CYP74A/B/C) and the exact EC number 4.2.1.183 were established experimentally (PubMed:26776054). While the P450→lyase reasoning is transferable, the precise subfamily assignment within CYP74 relies on sequence-level comparisons to characterized homologs.
- EC 4.2.1.70 may or may not be a valid assigned EC number; if it were a valid number for an unrelated enzyme, it would still be eliminable by P450 recognition. The reviewer could not confirm its current assignment status.
- The heme-binding motif in this sequence is somewhat degenerate compared to the canonical FGG motif, which is characteristic of CYP74 family P450s.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~495 aa) contains P450-characteristic features: a hydrophobic N-terminal membrane-anchoring region, the I-helix-like segment (GIAHTPLPHFLEELLFHTFRLPP), and a heme-binding region with a conserved cysteine (QCPAKD). This identifies the protein as a cytochrome P450. Transferable knowledge from the oxylipin/P450 literature establishes that the CYP74 family (unlike typical P450s classified as EC 1.14.x.x monooxygenases) catalyzes internal rearrangements of hydroperoxy fatty acids and is classified as hydro-lyases (EC 4.2.x.x). This eliminates B (EC 2.3.1.319, an acyltransferase) and D (EC 2.1.2.1, formate-THF ligase), neither of which are P450s. Between A (4.2.1.70) and C (4.2.1.183): EC 4.2.1.70 does not correspond to a known CYP74-family divinyl ether synthase or any P450-type hydro-lyase in standard nomenclature, making it an implausible assignment for a P450 sequence. EC 4.2.1.183 is the specific EC number assigned to CYP74M-type divinyl ether synthases. A model recognizing P450 architecture + CYP74-family lyase classification + elimination of the non-P450 options and the non-P450-compatible EC 4.2.1.70 can arrive at C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P450 fold is recognizable from sequence length, hydrophobic segments, I-helix motif, and heme-cysteine region. The CYP74→lyase (EC 4.2.x.x) classification is transferable knowledge from oxylipin metabolism literature. Options B and D are eliminated by P450 recognition. The remaining distinction between A and C relies on knowing that EC 4.2.1.70 is not a valid/assigned EC number for a P450-type enzyme, while 4.2.1.183 is the established number for CYP74M divinyl ether synthases. This is a family-level inference rather than a lookup of this exact protein's record."
  },
  "case_id": "EC_number_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry D8QZ31 (C74M3_SELML) confirms EC 4.2.1.183 (Divinyl ether synthase CYP74M3) with experimental evidence (ECO:0000269, PubMed:26776054). The sequence in the benchmark matches the UniProt entry exactly (495 aa, SHA256 matched). The catalytic activity is the conversion of (13S)-hydroperoxy fatty acids to divinyl ethers + H2O, consistent with EC 4.2.1.183."
  },
  "important_caveats": [
    "The identification of this as specifically CYP74M (vs. CYP74A/B/C) and the exact EC number 4.2.1.183 were established experimentally (PubMed:26776054). While the P450→lyase reasoning is transferable, the precise subfamily assignment within CYP74 relies on sequence-level comparisons to characterized homologs.",
    "EC 4.2.1.70 may or may not be a valid assigned EC number; if it were a valid number for an unrelated enzyme, it would still be eliminable by P450 recognition. The reviewer could not confirm its current assignment status.",
    "The heme-binding motif in this sequence is somewhat degenerate compared to the canonical FGG motif, which is characteristic of CYP74 family P450s."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with a P450 architecture. Option A (EC 4.2.1.70) does not correspond to a known P450-family hydro-lyase in current EC nomenclature, making it an implausible assignment for this sequence. Option C is the only EC number consistent with both the P450 architecture and the CYP74 lyase classification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"EC_number_0046","expected_answer_check":{"judgment":"supported","reason":"UniProt entry D8QZ31 (C74M3_SELML) confirms EC 4.2.1.183 (Divinyl ether synthase CYP74M3) with experimental evidence (ECO:0000269, PubMed:26776054). The sequence in the benchmark matches the UniProt entry exactly (495 aa, SHA256 matched). The catalytic activity is the conversion of (13S)-hydroperoxy fatty acids to divinyl ethers + H2O, consistent with EC 4.2.1.183.","evidence_ids":["C4","C5","C6","H2","H4","H5"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The sequence (~495 aa) contains P450-characteristic features: a hydrophobic N-terminal membrane-anchoring region, the I-helix-like segment (GIAHTPLPHFLEELLFHTFRLPP), and a heme-binding region with a conserved cysteine (QCPAKD). This identifies the protein as a cytochrome P450. Transferable knowledge from the oxylipin/P450 literature establishes that the CYP74 family (unlike typical P450s classified as EC 1.14.x.x monooxygenases) catalyzes internal rearrangements of hydroperoxy fatty acids and is classified as hydro-lyases (EC 4.2.x.x). This eliminates B (EC 2.3.1.319, an acyltransferase) and D (EC 2.1.2.1, formate-THF ligase), neither of which are P450s. Between A (4.2.1.70) and C (4.2.1.183): EC 4.2.1.70 does not correspond to a known CYP74-family divinyl ether synthase or any P450-type hydro-lyase in standard nomenclature, making it an implausible assignment for a P450 sequence. EC 4.2.1.183 is the specific EC number assigned to CYP74M-type divinyl ether synthases. A model recognizing P450 architecture + CYP74-family lyase classification + elimination of the non-P450 options and the non-P450-compatible EC 4.2.1.70 can arrive at C.","missing_item_specific_fact":"","reason":"The P450 fold is recognizable from sequence length, hydrophobic segments, I-helix motif, and heme-cysteine region. The CYP74→lyase (EC 4.2.x.x) classification is transferable knowledge from oxylipin metabolism literature. Options B and D are eliminated by P450 recognition. The remaining distinction between A and C relies on knowing that EC 4.2.1.70 is not a valid/assigned EC number for a P450-type enzyme, while 4.2.1.183 is the established number for CYP74M divinyl ether synthases. This is a family-level inference rather than a lookup of this exact protein's record."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"Options B and D are clearly incompatible with a P450 architecture. Option A (EC 4.2.1.70) does not correspond to a known P450-family hydro-lyase in current EC nomenclature, making it an implausible assignment for this sequence. Option C is the only EC number consistent with both the P450 architecture and the CYP74 lyase classification."},"important_caveats":["The identification of this as specifically CYP74M (vs. CYP74A/B/C) and the exact EC number 4.2.1.183 were established experimentally (PubMed:26776054). While the P450→lyase reasoning is transferable, the precise subfamily assignment within CYP74 relies on sequence-level comparisons to characterized homologs.","EC 4.2.1.70 may or may not be a valid assigned EC number; if it were a valid number for an unrelated enzyme, it would still be eliminable by P450 recognition. The reviewer could not confirm its current assignment status.","The heme-binding motif in this sequence is somewhat degenerate compared to the canonical FGG motif, which is characteristic of CYP74 family P450s."]}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 495,
  "benchmark_sequence_sha256": "0b22ddba73dd0ac278bf9cedf5b7de50ecaf7f1f1efc3e1bef923293962e731d",
  "current_entry_audit": {
    "entryVersion": 70,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-10-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 495,
  "current_source_sequence_sha256": "0b22ddba73dd0ac278bf9cedf5b7de50ecaf7f1f1efc3e1bef923293962e731d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 68,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D8QZ31",
  "selected_historical_entry_version": 68,
  "selected_historical_record_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "selected_historical_source_sequence_length": 495,
  "selected_historical_source_sequence_sha256": "0b22ddba73dd0ac278bf9cedf5b7de50ecaf7f1f1efc3e1bef923293962e731d",
  "selected_historical_version": {
    "accession": "D8QZ31",
    "database": "Swiss-Prot",
    "entryVersion": 68,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C74M3_SELML",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D8QZ31\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":70,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-10-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Gemmiferous spikemoss\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Lycopodiopsida\",\"Selaginellales\",\"Selaginellaceae\",\"Selaginelloideae\",\"Selaginella\"],\"scientificName\":\"Selaginella moellendorffii\",\"synonyms\":[\"Kungiselaginella moellendorffii\"],\"taxonId\":88036}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.183\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"Etheroleic acid synthase CYP74M3\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"Divinyl ether synthase CYP74M3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79276\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.183\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"name\":\"(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79275\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57466\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229759\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79272\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.183\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"name\":\"(13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79271\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58757\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229758\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Gorina S.S.\",\"Toporkova Y.Y.\",\"Mukhtarova L.S.\",\"Smirnova E.O.\",\"Chechetkin I.R.\",\"Khairutdinov B.I.\",\"Gogolev Y.V.\",\"Grechkin A.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26776054\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbalip.2016.01.001\"}],\"citationType\":\"journal article\",\"firstPage\":\"301\",\"id\":\"26776054\",\"journal\":\"Biochim. Biophys. Acta\",\"lastPage\":\"309\",\"publicationDate\":\"2016\",\"title\":\"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular cloning and identification of divinyl ether synthases CYP74M1 and CYP74M3.\",\"volume\":\"1861\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H1",
  "excerpt": "ID   C74M3_SELML             Reviewed;         495 AA.\nAC   D8QZ31;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-OCT-2010, sequence version 1.\nDT   28-JAN-2026, entry version 68.\nDE   RecName: Full=Divinyl ether synthase CYP74M3 {ECO:0000303|PubMed:26776054};\nDE   AltName: Full=Etheroleic acid synthase CYP74M3 {ECO:0000305|PubMed:26776054};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};\nGN   Name=CYP74M3 {ECO:0000303|PubMed:26776054};\nGN   Synonyms=DES2 {ECO:0000303|PubMed:26776054};\nGN   ORFNames=SELMODRAFT_81998 {ECO:0000312|EMBL:EFJ34345.1};\nOS   Selaginella moellendorffii (Spikemoss).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Lycopodiopsida; Selaginellales; Selaginellaceae; Selaginella.\nOX   NCBI_TaxID=88036;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Divinyl ether synthase CYP74M3 {ECO:0000303|PubMed:26776054};\nDE   AltName: Full=Etheroleic acid synthase CYP74M3 {ECO:0000305|PubMed:26776054};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRX   PubMed=26776054; DOI=10.1016/j.bbalip.2016.01.001;\nRA   Gorina S.S., Toporkova Y.Y., Mukhtarova L.S., Smirnova E.O.,\nRA   Chechetkin I.R., Khairutdinov B.I., Gogolev Y.V., Grechkin A.N.;\nRT   \"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular\nRT   cloning and identification of divinyl ether synthases CYP74M1 and\nRT   CYP74M3.\";\nRL   Biochim. Biophys. Acta 1861:301-309(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate +\nCC         H2O; Xref=Rhea:RHEA:79275, ChEBI:CHEBI:15377, ChEBI:CHEBI:57466,\nCC         ChEBI:CHEBI:229759; EC=4.2.1.183;\nCC         Evidence={ECO:0000269|PubMed:26776054};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79276;\nCC         Evidence={ECO:0000305|PubMed:26776054};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate =\nCC         etherolenate + H2O; Xref=Rhea:RHEA:79271, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:58757, ChEBI:CHEBI:229758; EC=4.2.1.183;\nCC         Evidence={ECO:0000269|PubMed:26776054};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79272;\nCC         Evidence={ECO:0000305|PubMed:26776054};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 46. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
