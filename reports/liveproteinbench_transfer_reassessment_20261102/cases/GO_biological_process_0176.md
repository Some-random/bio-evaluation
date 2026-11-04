# GO_biological_process_0176

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0176.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **C** — sterol metabolic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MELITLLSALLVLAIVSLSTFFVLYYNTPTKDGKTLPPGRMGWPFIGESYDFFAAGWKGKPESFIFDRLKKFAKGNLNGQFRTSLFGNKSIVVAGAAANKLLFSNEKKLVTMWWPPSIDKAFPSTAQLSANEEALLMRKFFPSFLIRREALQRYIPIMDDCTRRHFATGAWGPSDKIEAFNVTQDYTFWVACRVFMSIDAQEDPETVDSLFRHFNVLKAGIYSMHIDLPWTNFHHAMKASHAIRSAVEQIAKKRRAELAEGKAFPTQDMLSYMLETPITSAEDSKDGKAKYLNDADIGTKILGLLVGGHDTSSTVIAFFFKFMAENPHVYEAIYKEQMEVAATKAPGELLNWDDLQKMKYSWCAICEVMRLTPPVQGAFRQAITDFTHNGYLIPKGWKIYWSTHSTHRNPEIFPQPEKFDPTRFEGNGPPAFSFVPFGGGPRMCPGKEYARLQVLTFVHHIVTKFKWEQILPNEKIIVSPMPYPEKNLPLRMIARSESATLA

[Multiple Choices]
A. daunorubicin transport
B. L-fucose catabolic process
C. sterol metabolic process
D. cellular response to tumor necrosis factor
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

### Expected-answer support: contradicted

> The sequence-matched entry has a computational TreeGrafter annotation for sterol metabolic process (C8), but its experimentally supported function is oxidation of beta-amyrin and oleanolic acid in triterpenoid/saponin biosynthesis (C5, C7, C9). Those substrates and processes are not sterols as defined by the supplied GO term definition, so the experimental evidence does not support C as the protein's primary process.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal membrane anchor and a conserved cytochrome P450 heme-binding region, consistent with a membrane-associated P450 oxidase. Transferable knowledge that P450s oxidize hydrophobic metabolites makes a metabolic-process choice much more plausible than daunorubicin transport, L-fucose catabolism, or a TNF response; among the offered choices, C is the meaningful candidate. This does not establish sterol substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A P450-family inference from sequence features and the alternatives meaningfully distinguishes C, even though the sequence alone does not establish the enzyme's exact substrate or biological pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives are otherwise substantially less compatible with a membrane-associated P450 oxidase. The main caveat is that C is a poor description of the experimentally characterized triterpenoid/saponin pathway, not that another offered option is comparably supported.


### Important caveats

- The exact-sequence database annotation for C is computational, whereas the supplied evidence for triterpenoid and saponin biosynthesis is experimental.
- The exact enzyme's substrate specificity is not established by the sequence-family inference alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal membrane anchor and a conserved cytochrome P450 heme-binding region, consistent with a membrane-associated P450 oxidase. Transferable knowledge that P450s oxidize hydrophobic metabolites makes a metabolic-process choice much more plausible than daunorubicin transport, L-fucose catabolism, or a TNF response; among the offered choices, C is the meaningful candidate. This does not establish sterol substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A P450-family inference from sequence features and the alternatives meaningfully distinguishes C, even though the sequence alone does not establish the enzyme's exact substrate or biological pathway."
  },
  "case_id": "GO_biological_process_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "C9",
      "GO1"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched entry has a computational TreeGrafter annotation for sterol metabolic process (C8), but its experimentally supported function is oxidation of beta-amyrin and oleanolic acid in triterpenoid/saponin biosynthesis (C5, C7, C9). Those substrates and processes are not sterols as defined by the supplied GO term definition, so the experimental evidence does not support C as the protein's primary process."
  },
  "important_caveats": [
    "The exact-sequence database annotation for C is computational, whereas the supplied evidence for triterpenoid and saponin biosynthesis is experimental.",
    "The exact enzyme's substrate specificity is not established by the sequence-family inference alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are otherwise substantially less compatible with a membrane-associated P450 oxidase. The main caveat is that C is a poor description of the experimentally characterized triterpenoid/saponin pathway, not that another offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0176",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched entry has a computational TreeGrafter annotation for sterol metabolic process (C8), but its experimentally supported function is oxidation of beta-amyrin and oleanolic acid in triterpenoid/saponin biosynthesis (C5, C7, C9). Those substrates and processes are not sterols as defined by the supplied GO term definition, so the experimental evidence does not support C as the protein's primary process.",
    "evidence_ids": ["C5", "C7", "C8", "C9", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal membrane anchor and a conserved cytochrome P450 heme-binding region, consistent with a membrane-associated P450 oxidase. Transferable knowledge that P450s oxidize hydrophobic metabolites makes a metabolic-process choice much more plausible than daunorubicin transport, L-fucose catabolism, or a TNF response; among the offered choices, C is the meaningful candidate. This does not establish sterol substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "A P450-family inference from sequence features and the alternatives meaningfully distinguishes C, even though the sequence alone does not establish the enzyme's exact substrate or biological pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are otherwise substantially less compatible with a membrane-associated P450 oxidase. The main caveat is that C is a poor description of the experimentally characterized triterpenoid/saponin pathway, not that another offered option is comparably supported."
  },
  "important_caveats": [
    "The exact-sequence database annotation for C is computational, whereas the supplied evidence for triterpenoid and saponin biosynthesis is experimental.",
    "The exact enzyme's substrate specificity is not established by the sequence-family inference alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is CYP716A379, a cytochrome P450 that oxidizes beta-amyrin to oleanolic acid and then to echinocystic acid in the saponin/triterpenoid biosynthetic pathway. The experimental GO annotations (IDA) are 'saponin biosynthetic process' (GO:0016135) and 'triterpenoid biosynthetic process' (GO:0016104). The 'sterol metabolic process' annotation (GO:0016125) is present but carries only IEA:TreeGrafter evidence (computational inference). While triterpenoids are not strictly sterols (they are pentacyclic triterpenes, not tetracyclic steroids with hydrocarbon side-chains), they share the isoprenoid/terpenoid biosynthetic lineage with sterols, and among the four offered choices, C is the only one consistent with a P450 catalyzing oxidative transformations of terpenoid substrates. The answer is the best available option and has database annotation, though the precise experimental term would be 'triterpenoid biosynthetic process.'

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif (FSFVPFGGGPRMC) and an N-terminal hydrophobic ER-anchor (MELITLLSALLVLAIVSLSTFFVLYY), identifying it as a microsomal P450 monooxygenase. P450s catalyze oxidative transformations of small organic molecules. Among the four choices: (A) daunorubicin transport requires a transporter protein (ABC/MFS family), not a monooxygenase; (B) L-fucose catabolism involves sugar-processing enzymes (kinases, dehydrogenases, aldolases), not P450s; (D) cellular response to TNF is an animal-specific cytokine signaling pathway absent in plants. Only (C) sterol metabolic process describes enzymatic transformation of small terpenoid/steroid substrates, which is the hallmark function of plant P450s (e.g., CYP51 in sterol biosynthesis, CYP716 family in triterpenoid oxidation). The family-level knowledge that plant P450s participate in terpenoid/steroid metabolism, combined with elimination of the three mechanistically incompatible options, uniquely selects C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the P450 heme-binding signature and ER-anchor from the sequence, combined with general knowledge that P450s are monooxygenases acting on small molecules (not transporters, sugar-catabolism enzymes, or animal cytokine signaling components), allows a knowledgeable model to eliminate A, B, and D and select C. The plant CYP716 family's well-known role in triterpenoid/terpenoid oxidation further supports C as the closest available GO term.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are mechanistically incompatible with a cytochrome P450 monooxygenase. Only C describes a metabolic process involving enzymatic oxidation of small terpenoid/steroid substrates. While the precise term should be 'triterpenoid biosynthetic process,' that option is not offered, and C is the only viable alternative among the four.


### Important caveats

- The experimental GO annotation is 'triterpenoid biosynthetic process' (IDA) and 'saponin biosynthetic process' (IDA), not 'sterol metabolic process.' The sterol annotation is IEA:TreeGrafter (computational transfer).
- Triterpenoids (pentacyclic, e.g., beta-amyrin) are not strictly sterols (tetracyclic with hydrocarbon side-chain) per the GO definition, but share the isoprenoid biosynthetic lineage.
- The answer C is the best available option among the four choices, but is not the most precise experimental annotation for this enzyme.
- The protein is from Saponaria officinalis (soapwort), a plant; TNF signaling (option D) is animal-specific, reinforcing elimination of D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FSFVPFGGGPRMC) and an N-terminal hydrophobic ER-anchor (MELITLLSALLVLAIVSLSTFFVLYY), identifying it as a microsomal P450 monooxygenase. P450s catalyze oxidative transformations of small organic molecules. Among the four choices: (A) daunorubicin transport requires a transporter protein (ABC/MFS family), not a monooxygenase; (B) L-fucose catabolism involves sugar-processing enzymes (kinases, dehydrogenases, aldolases), not P450s; (D) cellular response to TNF is an animal-specific cytokine signaling pathway absent in plants. Only (C) sterol metabolic process describes enzymatic transformation of small terpenoid/steroid substrates, which is the hallmark function of plant P450s (e.g., CYP51 in sterol biosynthesis, CYP716 family in triterpenoid oxidation). The family-level knowledge that plant P450s participate in terpenoid/steroid metabolism, combined with elimination of the three mechanistically incompatible options, uniquely selects C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the P450 heme-binding signature and ER-anchor from the sequence, combined with general knowledge that P450s are monooxygenases acting on small molecules (not transporters, sugar-catabolism enzymes, or animal cytokine signaling components), allows a knowledgeable model to eliminate A, B, and D and select C. The plant CYP716 family's well-known role in triterpenoid/terpenoid oxidation further supports C as the closest available GO term."
  },
  "case_id": "GO_biological_process_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein is CYP716A379, a cytochrome P450 that oxidizes beta-amyrin to oleanolic acid and then to echinocystic acid in the saponin/triterpenoid biosynthetic pathway. The experimental GO annotations (IDA) are 'saponin biosynthetic process' (GO:0016135) and 'triterpenoid biosynthetic process' (GO:0016104). The 'sterol metabolic process' annotation (GO:0016125) is present but carries only IEA:TreeGrafter evidence (computational inference). While triterpenoids are not strictly sterols (they are pentacyclic triterpenes, not tetracyclic steroids with hydrocarbon side-chains), they share the isoprenoid/terpenoid biosynthetic lineage with sterols, and among the four offered choices, C is the only one consistent with a P450 catalyzing oxidative transformations of terpenoid substrates. The answer is the best available option and has database annotation, though the precise experimental term would be 'triterpenoid biosynthetic process.'"
  },
  "important_caveats": [
    "The experimental GO annotation is 'triterpenoid biosynthetic process' (IDA) and 'saponin biosynthetic process' (IDA), not 'sterol metabolic process.' The sterol annotation is IEA:TreeGrafter (computational transfer).",
    "Triterpenoids (pentacyclic, e.g., beta-amyrin) are not strictly sterols (tetracyclic with hydrocarbon side-chain) per the GO definition, but share the isoprenoid biosynthetic lineage.",
    "The answer C is the best available option among the four choices, but is not the most precise experimental annotation for this enzyme.",
    "The protein is from Saponaria officinalis (soapwort), a plant; TNF signaling (option D) is animal-specific, reinforcing elimination of D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are mechanistically incompatible with a cytochrome P450 monooxygenase. Only C describes a metabolic process involving enzymatic oxidation of small terpenoid/steroid substrates. While the precise term should be 'triterpenoid biosynthetic process,' that option is not offered, and C is the only viable alternative among the four."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is CYP716A379, a cytochrome P450 that oxidizes beta-amyrin to oleanolic acid and then to echinocystic acid in the saponin/triterpenoid biosynthetic pathway. The experimental GO annotations (IDA) are 'saponin biosynthetic process' (GO:0016135) and 'triterpenoid biosynthetic process' (GO:0016104). The 'sterol metabolic process' annotation (GO:0016125) is present but carries only IEA:TreeGrafter evidence (computational inference). While triterpenoids are not strictly sterols (they are pentacyclic triterpenes, not tetracyclic steroids with hydrocarbon side-chains), they share the isoprenoid/terpenoid biosynthetic lineage with sterols, and among the four offered choices, C is the only one consistent with a P450 catalyzing oxidative transformations of terpenoid substrates. The answer is the best available option and has database annotation, though the precise experimental term would be 'triterpenoid biosynthetic process.'",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FSFVPFGGGPRMC) and an N-terminal hydrophobic ER-anchor (MELITLLSALLVLAIVSLSTFFVLYY), identifying it as a microsomal P450 monooxygenase. P450s catalyze oxidative transformations of small organic molecules. Among the four choices: (A) daunorubicin transport requires a transporter protein (ABC/MFS family), not a monooxygenase; (B) L-fucose catabolism involves sugar-processing enzymes (kinases, dehydrogenases, aldolases), not P450s; (D) cellular response to TNF is an animal-specific cytokine signaling pathway absent in plants. Only (C) sterol metabolic process describes enzymatic transformation of small terpenoid/steroid substrates, which is the hallmark function of plant P450s (e.g., CYP51 in sterol biosynthesis, CYP716 family in triterpenoid oxidation). The family-level knowledge that plant P450s participate in terpenoid/steroid metabolism, combined with elimination of the three mechanistically incompatible options, uniquely selects C.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the P450 heme-binding signature and ER-anchor from the sequence, combined with general knowledge that P450s are monooxygenases acting on small molecules (not transporters, sugar-catabolism enzymes, or animal cytokine signaling components), allows a knowledgeable model to eliminate A, B, and D and select C. The plant CYP716 family's well-known role in triterpenoid/terpenoid oxidation further supports C as the closest available GO term."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are mechanistically incompatible with a cytochrome P450 monooxygenase. Only C describes a metabolic process involving enzymatic oxidation of small terpenoid/steroid substrates. While the precise term should be 'triterpenoid biosynthetic process,' that option is not offered, and C is the only viable alternative among the four."
  },
  "important_caveats": [
    "The experimental GO annotation is 'triterpenoid biosynthetic process' (IDA) and 'saponin biosynthetic process' (IDA), not 'sterol metabolic process.' The sterol annotation is IEA:TreeGrafter (computational transfer).",
    "Triterpenoids (pentacyclic, e.g., beta-amyrin) are not strictly sterols (tetracyclic with hydrocarbon side-chain) per the GO definition, but share the isoprenoid biosynthetic lineage.",
    "The answer C is the best available option among the four choices, but is not the most precise experimental annotation for this enzyme.",
    "The protein is from Saponaria officinalis (soapwort), a plant; TNF signaling (option D) is animal-specific, reinforcing elimination of D."
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
  "benchmark_sequence_length": 502,
  "benchmark_sequence_sha256": "a27906e96c4671d9e4d58120851aefbfda32a7b83248e671ac9d77994264a654",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 502,
  "current_source_sequence_sha256": "a27906e96c4671d9e4d58120851aefbfda32a7b83248e671ac9d77994264a654",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAW1JA93",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "selected_historical_source_sequence_length": 502,
  "selected_historical_source_sequence_sha256": "a27906e96c4671d9e4d58120851aefbfda32a7b83248e671ac9d77994264a654",
  "selected_historical_version": {
    "accession": "A0AAW1JA93",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C7169_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1JA93\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 716A379\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoCYP716A379\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Oleanolic acid 16-monooxygenase CYP716A379\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.126\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Beta-amyrin 28-monooxygenase CYP716A379\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). An oxidoreductase that facilitates the oxidation of the methyl group to a carboxyl group at the C-28 position of beta-amyrin, resulting in the formation of oleanolic acid (PubMed:39043959). Catalyzes also the subsequent oxidation of the methyl group to a< carboxyl group at the C-16 alpha position of oleanolic acid, resulting in the formation of echinocystic acid (PubMed:39043959)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"id\":\"GO:0016135\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:saponin biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0016125\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:sterol metabolic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"id\":\"GO:0016104\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:triterpenoid biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48155.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:36.226265+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   C7169_SAPOF             Reviewed;         502 AA.\nAC   A0AAW1JA93;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A379 {ECO:0000305};\nDE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};\nDE   AltName: Full=Cytochrome P450 716A379 {ECO:0000303|PubMed:39043959};\nDE            Short=SoCYP716A379 {ECO:0000303|PubMed:39043959};\nDE   AltName: Full=Oleanolic acid 16-monooxygenase CYP716A379 {ECO:0000305};\nDE            EC=1.14.14.- {ECO:0000269|PubMed:39043959};\nGN   Name=CYP716A379 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11043486m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_08G189800 {ECO:0000312|EMBL:KAK9699696.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48155.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.\nCC       saponarioside A and saponarioside B) biosynthetic pathway, leading to\nCC       the production of natural products with detergent properties used as\nCC       traditional sources of soap (PubMed:39043959). An oxidoreductase that\nCC       facilitates the oxidation of the methyl group to a carboxyl group at\nCC       the C-28 position of beta-amyrin, resulting in the formation of\nCC       oleanolic acid (PubMed:39043959). Catalyzes also the subsequent\nCC       oxidation of the methyl group to a< carboxyl group at the C-16 alpha\nCC       position of oleanolic acid, resulting in the formation of echinocystic\nCC       acid (PubMed:39043959). {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0016135; P:saponin biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0016125; P:sterol metabolic process; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0016104; P:triterpenoid biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:38.624320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9",
  "url": "https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0016125\nname: sterol metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving sterols, steroids with one or more hydroxyl groups and a hydrocarbon side-chain in the molecule.\" [ISBN:0198547684]\nsynonym: \"sterol metabolism\" EXACT []\nxref: Reactome:R-HSA-211976 \"Endogenous sterols\"\nis_a: GO:0008202 ! steroid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016125",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 123728-123736",
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
  "excerpt": "[Term]\nid: GO:0042355\nname: L-fucose catabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the breakdown of L-fucose (6-deoxy-Lgalactose).\" [GOC:jl]\nsynonym: \"L-fucose breakdown\" EXACT []\nsynonym: \"L-fucose catabolism\" EXACT []\nsynonym: \"L-fucose degradation\" EXACT []\nxref: MetaCyc:FUCCAT-PWY\nxref: MetaCyc:PWY-8318\nxref: MetaCyc:PWY-8444\nis_a: GO:0019320 ! hexose catabolic process\nis_a: GO:0042354 ! L-fucose metabolic process\nproperty_value: skos:narrowMatch MetaCyc:FUCCAT-PWY\nproperty_value: skos:narrowMatch MetaCyc:PWY-8318\nproperty_value: skos:narrowMatch MetaCyc:PWY-8444\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042355",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 236676-236692",
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
  "excerpt": "[Term]\nid: GO:0043215\nname: daunorubicin transport\nnamespace: biological_process\ndef: \"The directed movement of daunorubicin, an anthracycline antibiotic produced by Streptomyces coeruleorubidus or S. peucetius and used as an antineoplastic into, out of or within a cell, or between cells, by means of some agent such as a transporter or pore.\" [GOC:jl, GOC:mlg]\nis_a: GO:0071705 ! nitrogen compound transport\nis_a: GO:1901656 ! glycoside transport\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043215",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 244991-244998",
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
  "excerpt": "[Term]\nid: GO:0071356\nname: cellular response to tumor necrosis factor\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a tumor necrosis factor stimulus.\" [GOC:mah]\nsynonym: \"cellular response to TNF\" EXACT [GOC:mah]\nis_a: GO:0034612 ! response to tumor necrosis factor\nis_a: GO:0071345 ! cellular response to cytokine stimulus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071356",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 376344-376352",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 176. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
