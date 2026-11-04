# GO_molecular_function_0124

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0124.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKEKGEEKMNDSRKITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRKIERIEKGDSYIPDVSSNVLKDLVQNKQLVVYTPHTGIEEFQNSEYVIVTVPTPINKQKEPDLSALIAASHYIKQNLQAGQTFIFESSTYPGTLEEVIIPIIAQSGKEVGKDYYIGYSPERIDPANQQYTVQTIPKVISGQTERCKQQVQKLYSTIFDTVVPVSSPKVAEMCKLFENIQRLVNISLVNELNILCEKLGIDFREALEAAATKPFGFTPYWPGPGIGGHCIPVDPLYFQWKARQLGQSSQLIEVAHMINEKMPQQIVTQVKELSAPPGTVFLIGIAYKKDVNDLRESPALPIIELLVNEGYKVQYHDPYISSAKIGDKIYDSIPLKKKTLEKADCILIVTDHSNIDWNICKGMKHVIDTRGVLKKVSA

[Multiple Choices]
A. carboxylic ester hydrolase activity
B. oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor
C. metal ion binding
D. transcription coregulator activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

### Expected-answer support: contradicted

> The sequence-matched record reports an experimentally supported NAD-dependent dehydrogenase reaction (C5, C6), but the reaction is EC 1.1.1.136, not the CH-CH-donor activity specified by option B (GO2). The exact B annotation is present as IEA:InterPro (C8), which is computational evidence and does not resolve the mismatch with the experimental reaction.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an NAD-dependent dehydrogenase, including a plausible nucleotide-cofactor-binding region near its N-terminus. Transferable knowledge of enzyme families therefore makes an oxidoreductase choice much more plausible than ester hydrolase, metal-ion binding, or transcription coregulator activity. This supports B as the closest offered choice, but not its specific CH-CH-donor subtype.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A learner can meaningfully favor the redox-enzyme option from sequence patterns and general family knowledge without knowing this exact protein's record. However, those clues support the broad dehydrogenase function and do not establish that the precise activity named in B is correct.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported as the closest broad function, but the experimentally characterized reaction does not match the precise donor-group subtype in B; thus the choices appear to omit an exact answer.


### Important caveats

- The key's exact GO term is computationally annotated, whereas the cited catalytic reaction is experimentally supported and indicates a different oxidoreductase subtype.
- B may be the intended or closest choice among these alternatives without being scientifically correct as worded.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an NAD-dependent dehydrogenase, including a plausible nucleotide-cofactor-binding region near its N-terminus. Transferable knowledge of enzyme families therefore makes an oxidoreductase choice much more plausible than ester hydrolase, metal-ion binding, or transcription coregulator activity. This supports B as the closest offered choice, but not its specific CH-CH-donor subtype.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A learner can meaningfully favor the redox-enzyme option from sequence patterns and general family knowledge without knowing this exact protein's record. However, those clues support the broad dehydrogenase function and do not establish that the precise activity named in B is correct."
  },
  "case_id": "GO_molecular_function_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports an experimentally supported NAD-dependent dehydrogenase reaction (C5, C6), but the reaction is EC 1.1.1.136, not the CH-CH-donor activity specified by option B (GO2). The exact B annotation is present as IEA:InterPro (C8), which is computational evidence and does not resolve the mismatch with the experimental reaction."
  },
  "important_caveats": [
    "The key's exact GO term is computationally annotated, whereas the cited catalytic reaction is experimentally supported and indicates a different oxidoreductase subtype.",
    "B may be the intended or closest choice among these alternatives without being scientifically correct as worded."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported as the closest broad function, but the experimentally characterized reaction does not match the precise donor-group subtype in B; thus the choices appear to omit an exact answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0124",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports an experimentally supported NAD-dependent dehydrogenase reaction (C5, C6), but the reaction is EC 1.1.1.136, not the CH-CH-donor activity specified by option B (GO2). The exact B annotation is present as IEA:InterPro (C8), which is computational evidence and does not resolve the mismatch with the experimental reaction.",
    "evidence_ids": ["C5", "C6", "C8", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an NAD-dependent dehydrogenase, including a plausible nucleotide-cofactor-binding region near its N-terminus. Transferable knowledge of enzyme families therefore makes an oxidoreductase choice much more plausible than ester hydrolase, metal-ion binding, or transcription coregulator activity. This supports B as the closest offered choice, but not its specific CH-CH-donor subtype.",
    "missing_item_specific_fact": "",
    "reason": "A learner can meaningfully favor the redox-enzyme option from sequence patterns and general family knowledge without knowing this exact protein's record. However, those clues support the broad dehydrogenase function and do not establish that the precise activity named in B is correct."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported as the closest broad function, but the experimentally characterized reaction does not match the precise donor-group subtype in B; thus the choices appear to omit an exact answer."
  },
  "important_caveats": [
    "The key's exact GO term is computationally annotated, whereas the cited catalytic reaction is experimentally supported and indicates a different oxidoreductase subtype.",
    "B may be the intended or closest choice among these alternatives without being scientifically correct as worded."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A7GKX6 for this sequence carries GO:0016628 (oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor) as an IEA:InterPro annotation (evidence C8/H6). The experimental evidence (PubMed:20529859, ECO:0000269) confirms the protein is a dehydrogenase (EC 1.1.1.136) that uses NAD+ as cofactor to oxidize UDP-GlcNAc. While EC 1.1.1.136 technically corresponds to CH-OH (GO:0016627) rather than CH-CH (GO:0016628), the GO:0016628 annotation is present in the database entry, and the broader oxidoreductase/NAD category is experimentally confirmed. The key matches a database annotation for this exact sequence.

Citations as saved: [C8](#evidence-c8), [C9](#evidence-c9), [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6), [H7](#evidence-h7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains classic Rossmann-fold glycine-rich motifs: 'GLGYVGLPL' (~residues 20-28) matching the GxGxxG NAD-binding consensus of the first β-strand, and 'GPGIGG' (~residues 265-270) matching a second nucleotide-binding motif. These motifs are hallmarks of NAD/NADP-dependent dehydrogenases (MDR, SDR, and related oxidoreductase families) and are well-established transferable knowledge. Among the four options: (A) carboxylic ester hydrolase would require a GxSxG catalytic triad or lipase-like motif, absent here; (C) metal ion binding as primary function would show zinc-finger, iron-sulfur cluster, or dedicated metal-coordinating motifs, not present; (D) transcription coregulator would show LXXLL motifs or nuclear-receptor-interaction domains, absent. The Rossmann-fold pattern uniquely and strongly points to option B (oxidoreductase with NAD/NADP). The CH-CH vs CH-OH sub-classification is not tested since only one oxidoreductase option is offered.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold glycine-rich motifs (GLGYVGLPL, GPGIGG) are textbook NAD-binding signatures shared across hundreds of dehydrogenase families. Recognizing these motifs and connecting them to oxidoreductase/NAD activity is standard transferable knowledge that meaningfully eliminates A, C, and D without needing the specific UniProt annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different functional categories (hydrolase, oxidoreductase, metal-binding, transcription factor). The Rossmann-fold motifs unambiguously point to oxidoreductase/NAD activity. No other option is defensible given the sequence features.


### Important caveats

- The GO:0016628 annotation (CH-CH group) in UniProt is an automated IEA:InterPro assignment. The experimentally determined EC 1.1.1.136 corresponds to CH-OH (GO:0016627). The key matches the database annotation but is technically imprecise regarding the substrate group (CH-CH vs CH-OH). This does not affect answerability among the four offered choices since only one oxidoreductase option is presented.
- The protein is a UDP-N-acetylglucosamine 6-dehydrogenase (EC 1.1.1.136) from Bacillus cytotoxicus, experimentally characterized in PubMed:20529859.
- The GO:0016628 term definition in the supplied ontology (GO2) explicitly references EC:1.3.1.-, while this enzyme is EC 1.1.1.-, confirming the automated annotation is slightly misassigned at the sub-class level.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains classic Rossmann-fold glycine-rich motifs: 'GLGYVGLPL' (~residues 20-28) matching the GxGxxG NAD-binding consensus of the first β-strand, and 'GPGIGG' (~residues 265-270) matching a second nucleotide-binding motif. These motifs are hallmarks of NAD/NADP-dependent dehydrogenases (MDR, SDR, and related oxidoreductase families) and are well-established transferable knowledge. Among the four options: (A) carboxylic ester hydrolase would require a GxSxG catalytic triad or lipase-like motif, absent here; (C) metal ion binding as primary function would show zinc-finger, iron-sulfur cluster, or dedicated metal-coordinating motifs, not present; (D) transcription coregulator would show LXXLL motifs or nuclear-receptor-interaction domains, absent. The Rossmann-fold pattern uniquely and strongly points to option B (oxidoreductase with NAD/NADP). The CH-CH vs CH-OH sub-classification is not tested since only one oxidoreductase option is offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold glycine-rich motifs (GLGYVGLPL, GPGIGG) are textbook NAD-binding signatures shared across hundreds of dehydrogenase families. Recognizing these motifs and connecting them to oxidoreductase/NAD activity is standard transferable knowledge that meaningfully eliminates A, C, and D without needing the specific UniProt annotation for this protein."
  },
  "case_id": "GO_molecular_function_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "C9",
      "C5",
      "C6",
      "H6",
      "H7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A7GKX6 for this sequence carries GO:0016628 (oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor) as an IEA:InterPro annotation (evidence C8/H6). The experimental evidence (PubMed:20529859, ECO:0000269) confirms the protein is a dehydrogenase (EC 1.1.1.136) that uses NAD+ as cofactor to oxidize UDP-GlcNAc. While EC 1.1.1.136 technically corresponds to CH-OH (GO:0016627) rather than CH-CH (GO:0016628), the GO:0016628 annotation is present in the database entry, and the broader oxidoreductase/NAD category is experimentally confirmed. The key matches a database annotation for this exact sequence."
  },
  "important_caveats": [
    "The GO:0016628 annotation (CH-CH group) in UniProt is an automated IEA:InterPro assignment. The experimentally determined EC 1.1.1.136 corresponds to CH-OH (GO:0016627). The key matches the database annotation but is technically imprecise regarding the substrate group (CH-CH vs CH-OH). This does not affect answerability among the four offered choices since only one oxidoreductase option is presented.",
    "The protein is a UDP-N-acetylglucosamine 6-dehydrogenase (EC 1.1.1.136) from Bacillus cytotoxicus, experimentally characterized in PubMed:20529859.",
    "The GO:0016628 term definition in the supplied ontology (GO2) explicitly references EC:1.3.1.-, while this enzyme is EC 1.1.1.-, confirming the automated annotation is slightly misassigned at the sub-class level."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different functional categories (hydrolase, oxidoreductase, metal-binding, transcription factor). The Rossmann-fold motifs unambiguously point to oxidoreductase/NAD activity. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A7GKX6 for this sequence carries GO:0016628 (oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor) as an IEA:InterPro annotation (evidence C8/H6). The experimental evidence (PubMed:20529859, ECO:0000269) confirms the protein is a dehydrogenase (EC 1.1.1.136) that uses NAD+ as cofactor to oxidize UDP-GlcNAc. While EC 1.1.1.136 technically corresponds to CH-OH (GO:0016627) rather than CH-CH (GO:0016628), the GO:0016628 annotation is present in the database entry, and the broader oxidoreductase/NAD category is experimentally confirmed. The key matches a database annotation for this exact sequence.",
    "evidence_ids": ["C8", "C9", "C5", "C6", "H6", "H7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains classic Rossmann-fold glycine-rich motifs: 'GLGYVGLPL' (~residues 20-28) matching the GxGxxG NAD-binding consensus of the first β-strand, and 'GPGIGG' (~residues 265-270) matching a second nucleotide-binding motif. These motifs are hallmarks of NAD/NADP-dependent dehydrogenases (MDR, SDR, and related oxidoreductase families) and are well-established transferable knowledge. Among the four options: (A) carboxylic ester hydrolase would require a GxSxG catalytic triad or lipase-like motif, absent here; (C) metal ion binding as primary function would show zinc-finger, iron-sulfur cluster, or dedicated metal-coordinating motifs, not present; (D) transcription coregulator would show LXXLL motifs or nuclear-receptor-interaction domains, absent. The Rossmann-fold pattern uniquely and strongly points to option B (oxidoreductase with NAD/NADP). The CH-CH vs CH-OH sub-classification is not tested since only one oxidoreductase option is offered.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold glycine-rich motifs (GLGYVGLPL, GPGIGG) are textbook NAD-binding signatures shared across hundreds of dehydrogenase families. Recognizing these motifs and connecting them to oxidoreductase/NAD activity is standard transferable knowledge that meaningfully eliminates A, C, and D without needing the specific UniProt annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different functional categories (hydrolase, oxidoreductase, metal-binding, transcription factor). The Rossmann-fold motifs unambiguously point to oxidoreductase/NAD activity. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO:0016628 annotation (CH-CH group) in UniProt is an automated IEA:InterPro assignment. The experimentally determined EC 1.1.1.136 corresponds to CH-OH (GO:0016627). The key matches the database annotation but is technically imprecise regarding the substrate group (CH-CH vs CH-OH). This does not affect answerability among the four offered choices since only one oxidoreductase option is presented.",
    "The protein is a UDP-N-acetylglucosamine 6-dehydrogenase (EC 1.1.1.136) from Bacillus cytotoxicus, experimentally characterized in PubMed:20529859.",
    "The GO:0016628 term definition in the supplied ontology (GO2) explicitly references EC:1.3.1.-, while this enzyme is EC 1.1.1.-, confirming the automated annotation is slightly misassigned at the sub-class level."
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
  "benchmark_sequence_length": 423,
  "benchmark_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "current_entry_audit": {
    "entryVersion": 98,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-09-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 423,
  "current_source_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 96,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A7GKX6",
  "selected_historical_entry_version": 96,
  "selected_historical_record_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "selected_historical_source_sequence_length": 423,
  "selected_historical_source_sequence_sha256": "5bad7e65801ec8cb99f507e9a58146ea70fefa83160d8597748c30f9b3364a8a",
  "selected_historical_version": {
    "accession": "A7GKX6",
    "database": "Swiss-Prot",
    "entryVersion": 96,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UGNAD_BACCN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A7GKX6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":98,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-09-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\",\"Bacillus cereus group\"],\"scientificName\":\"Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98)\",\"taxonId\":315749}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.136\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-N-acetyl-D-glucosamine 6-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAc 6-dehydrogenase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"Dehydrogenase involved in the biosynthesis of the nucleotide-sugar UDP-N-acetylxylosamine (UDP-XylNAc) (PubMed:20529859). Catalyzes the conversion of UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-N-acetylglucosaminuronic acid (UDP-GlcNAcA) (PubMed:20529859). Cannot use UDP-glucose, UDP-galactose and UDP-N-acetylgalactosamine as substrates (PubMed:20529859)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13326\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.136\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13325\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65040\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0051287\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:NAD binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0016628\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"id\":\"GO:0047004\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:UDP-N-acetylglucosamine 6-dehydrogenase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Gu X.\",\"Glushka J.\",\"Lee S.G.\",\"Bar-Peled M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20529859\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m110.125872\"}],\"citationType\":\"journal article\",\"firstPage\":\"24825\",\"id\":\"20529859\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"24833\",\"publicationDate\":\"2010\",\"title\":\"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADE43879.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:09.484643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H1",
  "excerpt": "ID   UGNAD_BACCN             Reviewed;         423 AA.\nAC   A7GKX6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-SEP-2007, sequence version 1.\nDT   28-JAN-2026, entry version 96.\nDE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000303|PubMed:20529859};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:20529859};\nGN   Name=UGlcNAcDH {ECO:0000303|PubMed:20529859};\nGN   OrderedLocusNames=Bcer98_0429 {ECO:0000312|EMBL:ABS20784.1};\nOS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;\nOC   Bacillus cereus group.\nOX   NCBI_TaxID=315749;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:ADE43879.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;\nRX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;\nRA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;\nRT   \"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the\nRT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\";\nRL   J. Biol. Chem. 285:24825-24833(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Dehydrogenase involved in the biosynthesis of the nucleotide-\nCC       sugar UDP-N-acetylxylosamine (UDP-XylNAc) (PubMed:20529859). Catalyzes\nCC       the conversion of UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-N-\nCC       acetylglucosaminuronic acid (UDP-GlcNAcA) (PubMed:20529859). Cannot use\nCC       UDP-glucose, UDP-galactose and UDP-N-acetylgalactosamine as substrates\nCC       (PubMed:20529859). {ECO:0000269|PubMed:20529859}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-\nCC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);\nCC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,\nCC         ChEBI:CHEBI:65040; EC=1.1.1.136;\nCC         Evidence={ECO:0000269|PubMed:20529859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;\nCC         Evidence={ECO:0000269|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0051287; F:NAD binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0016628; F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)

```json
{
  "entry_version": 96,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0047004; F:UDP-N-acetylglucosamine 6-dehydrogenase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.633421+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666",
  "url": "https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003712\nname: transcription coregulator activity\nnamespace: molecular_function\nalt_id: GO:0001104\nalt_id: GO:0016455\ndef: \"A transcription regulator activity that modulates the transcription of specific gene sets via binding to a DNA-binding transcription factor at a specific genomic locus, either on its own or as part of a complex. Coregulators often act by altering chromatin structure and modifications. For example, one class of transcription coregulators modifies chromatin structure through covalent modification of histones. A second class remodels the conformation of chromatin in an ATP-dependent fashion. A third class modulates interactions of DNA-bound DNA-binding transcription factors with other transcription coregulators.\" [GOC:txnOH-2018, PMID:10213677, PMID:16858867, PMID:24203923, PMID:25957681, Wikipedia:Transcription_coregulator]\ncomment: Usage guidance: Most transcription coregulators do not bind DNA. Those that do usually bind DNA either in a non-specific or non-direct manner. If a protein binds DNA specifically, consider annotating to GO:0003700 DNA binding transcription factor activity.\nsubset: goslim_drosophila\nsynonym: \"nuclear receptor coreceptor activity\" NARROW []\nsynonym: \"RNA polymerase II transcriptional cofactor activity\" RELATED []\nsynonym: \"transcription cofactor activity\" EXACT []\nsynonym: \"transcription coreceptor activity\" EXACT []\nsynonym: \"transcriptional co-regulator\" EXACT []\nxref: Reactome:R-HSA-5340251 \"NR1H4:DCA,CDCA,LCHA binds RXRA and NCOA1,2\"\nis_a: GO:0140110 ! transcription regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003712",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 28124-28140",
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
  "excerpt": "[Term]\nid: GO:0016628\nname: oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor\nnamespace: molecular_function\ndef: \"Catalysis of an oxidation-reduction (redox) reaction in which a CH-CH group acts as a hydrogen or electron donor and reduces NAD or NADP.\" [EC:1.3.1.-]\nxref: EC:1.3.1.-\nxref: Reactome:R-HSA-4755572 \"Defective SRD5A3 does not reduce pPNOL to DCHOL\"\nxref: Reactome:R-HSA-9661726 \"An unknown reductase reduces D-UBGN to STBN\"\nxref: Reactome:R-HSA-9661745 \"An unknown BILR reduces BIL to D-UBGN\"\nis_a: GO:0016627 ! oxidoreductase activity, acting on the CH-CH group of donors\nproperty_value: skos:exactMatch EC:1.3.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016628",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 128398-128409",
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
  "excerpt": "[Term]\nid: GO:0046872\nname: metal ion binding\nnamespace: molecular_function\ndef: \"Binding to a metal ion.\" [GOC:ai]\nsubset: goslim_agr\nsubset: goslim_drosophila\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsynonym: \"heavy metal binding\" NARROW []\nsynonym: \"metal binding\" EXACT []\nis_a: GO:0043169 ! cation binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046872",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 281280-281292",
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
  "excerpt": "[Term]\nid: GO:0052689\nname: carboxylic ester hydrolase activity\nnamespace: molecular_function\nalt_id: GO:0004091\nalt_id: GO:0004302\nalt_id: GO:0004759\nalt_id: GO:0016789\ndef: \"Catalysis of the hydrolysis of a carboxylic ester bond.\" [EC:3.1.1.-, GOC:curators]\nsubset: goslim_drosophila\nsynonym: \"carboxylate esterase activity\" RELATED []\nsynonym: \"carboxylic esterase activity\" RELATED []\nsynonym: \"hydrolase activity acting on ester bonds\" RELATED [EC:3.1.1.-]\nxref: EC:3.1.1.-\nxref: KEGG_REACTION:R00630\nxref: Reactome:R-HSA-5693691 \"CES1 trimer.CES2 hydrolyse COCN to BEG\"\nxref: Reactome:R-HSA-8937442 \"CES3 hydrolyses CHEST to CHOL and LCFA(-)\"\nxref: Reactome:R-HSA-9749792 \"CES1,CES2 hydrolyze ASA- to ST\"\nxref: UM-BBD_reactionID:r1025\nis_a: GO:0016788 ! hydrolase activity, acting on ester bonds\nproperty_value: skos:exactMatch EC:3.1.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0052689",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 339338-339359",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
