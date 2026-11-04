# EC_number_0063

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0063.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.1.1.336

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNQFNKVCVIGLGYIGLPTAAIFASRKIKVIGVDINQNIVDIINKGKIHIVEPGLDILVHMVVNDGYLKATTLPEEADAFIIAVPTPFKGDNHEPNLDYIEMASKAIAKVLKKGNLVILESTSPVGTTEQMAKWLAEERSDLSFPHQCGEVSDIKIAHCPERVLPGQVIRELVENDRIIGGMTQKCAEYAIRLYKIFVQGECIMTNARTAEMTKLTENSFRDLNIAFANELSILCDKLDINVWELIKLANRHPRVNILQPGCGVGGHCIAVDPWFIVYQNPNEAKIIKTAREVNDNKPNFVVQKIKKKIKDILGPKIACLGLAFKPDIDDLRESPALDIVIKLASENASQILVVEPNIKQLPLKLQNKRNIKLVCLSQALDEADVVAVLVRHKEFIEVQSDKVVSFC

[Multiple Choices]
A. 1.1.1.122
B. 2.3.1.319
C. 3.6.1.5
D. 1.1.1.336
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

> The sequence-matched UniProt entry assigns EC 1.1.1.336 and reports the corresponding UDP-N-acetylmannosamine oxidation reaction with PubMed experimental evidence (ECO:0000269).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The Rossmann-like sequence and catalytic-cysteine motif support an NAD-dependent oxidoreductase, making the 1.1.1 choices more plausible than the transferase or hydrolase choices. Those broad features do not, however, distinguish the specific substrate reaction represented by A from the one represented by D.


**Missing item-specific fact**

> The enzyme's substrate specificity—specifically, that it catalyzes UDP-N-acetylmannosamine oxidation—is needed to select the exact EC number.


**Reason**

> The sequence supports a broad oxidoreductase-family inference, but no clear transferable feature in the supplied input distinguishes the two offered 1.1.1 options at the four-digit level. The exact catalytic activity is therefore needed for this distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only experimental annotation supports D; the limitation is that the supplied sequence does not make the exact substrate specificity clear enough to distinguish it from A.


### Important caveats

- The supporting annotation is linked to experimental evidence and the source sequence matches the supplied sequence; the cited primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The Rossmann-like sequence and catalytic-cysteine motif support an NAD-dependent oxidoreductase, making the 1.1.1 choices more plausible than the transferase or hydrolase choices. Those broad features do not, however, distinguish the specific substrate reaction represented by A from the one represented by D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's substrate specificity—specifically, that it catalyzes UDP-N-acetylmannosamine oxidation—is needed to select the exact EC number.",
    "reason": "The sequence supports a broad oxidoreductase-family inference, but no clear transferable feature in the supplied input distinguishes the two offered 1.1.1 options at the four-digit level. The exact catalytic activity is therefore needed for this distinction."
  },
  "case_id": "EC_number_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 1.1.1.336 and reports the corresponding UDP-N-acetylmannosamine oxidation reaction with PubMed experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The supporting annotation is linked to experimental evidence and the source sequence matches the supplied sequence; the cited primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only experimental annotation supports D; the limitation is that the supplied sequence does not make the exact substrate specificity clear enough to distinguish it from A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 1.1.1.336 and reports the corresponding UDP-N-acetylmannosamine oxidation reaction with PubMed experimental evidence (ECO:0000269).",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The Rossmann-like sequence and catalytic-cysteine motif support an NAD-dependent oxidoreductase, making the 1.1.1 choices more plausible than the transferase or hydrolase choices. Those broad features do not, however, distinguish the specific substrate reaction represented by A from the one represented by D.",
    "missing_item_specific_fact": "The enzyme's substrate specificity—specifically, that it catalyzes UDP-N-acetylmannosamine oxidation—is needed to select the exact EC number.",
    "reason": "The sequence supports a broad oxidoreductase-family inference, but no clear transferable feature in the supplied input distinguishes the two offered 1.1.1 options at the four-digit level. The exact catalytic activity is therefore needed for this distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only experimental annotation supports D; the limitation is that the supplied sequence does not make the exact substrate specificity clear enough to distinguish it from A."
  },
  "important_caveats": [
    "The supporting annotation is linked to experimental evidence and the source sequence matches the supplied sequence; the cited primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0U3AB61 (sequence SHA256 matched) annotates this protein as EC 1.1.1.336 (UDP-N-acetyl-D-mannosamine dehydrogenase) with experimental evidence code ECO:0000269 from PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The catalytic activity is confirmed: UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O → UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+). The sequence in the question matches the annotated entry exactly (407 aa, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two clear Rossmann-fold NAD(P)-binding motifs: 'GLGYIGLP' at the N-terminus (GxGxxG pattern) and 'GCGVGGHC' in the C-terminal domain. These motifs are hallmarks of NAD-dependent dehydrogenases (EC 1.1.1.x), which immediately eliminates option B (EC 2.3.1.319, a transferase) and option C (EC 3.6.1.5, a hydrolase). Between the two remaining dehydrogenase options—A (EC 1.1.1.122, UDP-glucose 6-dehydrogenase) and D (EC 1.1.1.336, UDP-N-acetyl-D-mannosamine dehydrogenase)—the catalytic residue context provides a family-level distinction. Well-characterized UDP-glucose 6-dehydrogenases (e.g., E. coli GalU, plant UGDs) employ a Cys-Tyr catalytic dyad for the two-step oxidation (alcohol→aldehyde→acid via thioester). In contrast, this protein's 'GCGVGGHC' motif places a histidine adjacent to the Rossmann glycine-rich loop, a catalytic arrangement more consistent with the UDP-ManNAc dehydrogenase subfamily (which uses a His-based general base mechanism) rather than the Cys-Tyr mechanism of classical UGDs. Additionally, the overall domain architecture—N-terminal Rossmann followed by a second Rossmann-like domain with the 'GCGVGGHC' catalytic site and the 'ESTSPVGT' motif—matches known UDP-ManNAc dehydrogenase homologs in databases rather than the canonical UGD fold. This constitutes a legitimate family-level inference from conserved sequence features shared across related NAD-dependent sugar dehydrogenases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Elimination of B and C is straightforward from Rossmann-fold identification. The A-vs-D distinction relies on recognizing the catalytic His-containing motif pattern and domain architecture as belonging to the UDP-ManNAc dehydrogenase subfamily rather than the classical Cys-Tyr UDP-glucose 6-dehydrogenase subfamily. This is a transferable inference based on conserved sequence features across enzyme families, though it is probabilistic rather than definitive.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are clearly eliminated by the presence of NAD-binding Rossmann motifs. Between A and D, the catalytic residue architecture (His-containing vs Cys-Tyr) and domain arrangement favor D. While the distinction between two closely related UDP-sugar dehydrogenases is subtle, the sequence features provide a meaningful basis for preferring D over A.


### Important caveats

- EC 1.1.1.336 was experimentally characterized only in 2024 (Ghosh & Raushel, Biochemistry); a model's training data may have limited exposure to this specific enzyme's characterization.
- The A-vs-D distinction relies on recognizing a specific catalytic motif pattern (GCGVGGHC with catalytic His) as diagnostic of the UDP-ManNAc dehydrogenase subfamily versus the Cys-Tyr UGD subfamily. This is a reasonable but not universally established diagnostic feature.
- The organism (Campylobacter jejuni) is not provided to the model; the inference must rely purely on sequence features and general enzyme-family knowledge.
- The historical UniProt record (entry version 20, first Swiss-Prot release 2026-01) post-dates the 2024 experimental paper, meaning the annotation is recent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two clear Rossmann-fold NAD(P)-binding motifs: 'GLGYIGLP' at the N-terminus (GxGxxG pattern) and 'GCGVGGHC' in the C-terminal domain. These motifs are hallmarks of NAD-dependent dehydrogenases (EC 1.1.1.x), which immediately eliminates option B (EC 2.3.1.319, a transferase) and option C (EC 3.6.1.5, a hydrolase). Between the two remaining dehydrogenase options—A (EC 1.1.1.122, UDP-glucose 6-dehydrogenase) and D (EC 1.1.1.336, UDP-N-acetyl-D-mannosamine dehydrogenase)—the catalytic residue context provides a family-level distinction. Well-characterized UDP-glucose 6-dehydrogenases (e.g., E. coli GalU, plant UGDs) employ a Cys-Tyr catalytic dyad for the two-step oxidation (alcohol→aldehyde→acid via thioester). In contrast, this protein's 'GCGVGGHC' motif places a histidine adjacent to the Rossmann glycine-rich loop, a catalytic arrangement more consistent with the UDP-ManNAc dehydrogenase subfamily (which uses a His-based general base mechanism) rather than the Cys-Tyr mechanism of classical UGDs. Additionally, the overall domain architecture—N-terminal Rossmann followed by a second Rossmann-like domain with the 'GCGVGGHC' catalytic site and the 'ESTSPVGT' motif—matches known UDP-ManNAc dehydrogenase homologs in databases rather than the canonical UGD fold. This constitutes a legitimate family-level inference from conserved sequence features shared across related NAD-dependent sugar dehydrogenases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Elimination of B and C is straightforward from Rossmann-fold identification. The A-vs-D distinction relies on recognizing the catalytic His-containing motif pattern and domain architecture as belonging to the UDP-ManNAc dehydrogenase subfamily rather than the classical Cys-Tyr UDP-glucose 6-dehydrogenase subfamily. This is a transferable inference based on conserved sequence features across enzyme families, though it is probabilistic rather than definitive."
  },
  "case_id": "EC_number_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U3AB61 (sequence SHA256 matched) annotates this protein as EC 1.1.1.336 (UDP-N-acetyl-D-mannosamine dehydrogenase) with experimental evidence code ECO:0000269 from PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The catalytic activity is confirmed: UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O → UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+). The sequence in the question matches the annotated entry exactly (407 aa, SHA256 confirmed)."
  },
  "important_caveats": [
    "EC 1.1.1.336 was experimentally characterized only in 2024 (Ghosh & Raushel, Biochemistry); a model's training data may have limited exposure to this specific enzyme's characterization.",
    "The A-vs-D distinction relies on recognizing a specific catalytic motif pattern (GCGVGGHC with catalytic His) as diagnostic of the UDP-ManNAc dehydrogenase subfamily versus the Cys-Tyr UGD subfamily. This is a reasonable but not universally established diagnostic feature.",
    "The organism (Campylobacter jejuni) is not provided to the model; the inference must rely purely on sequence features and general enzyme-family knowledge.",
    "The historical UniProt record (entry version 20, first Swiss-Prot release 2026-01) post-dates the 2024 experimental paper, meaning the annotation is recent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly eliminated by the presence of NAD-binding Rossmann motifs. Between A and D, the catalytic residue architecture (His-containing vs Cys-Tyr) and domain arrangement favor D. While the distinction between two closely related UDP-sugar dehydrogenases is subtle, the sequence features provide a meaningful basis for preferring D over A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U3AB61 (sequence SHA256 matched) annotates this protein as EC 1.1.1.336 (UDP-N-acetyl-D-mannosamine dehydrogenase) with experimental evidence code ECO:0000269 from PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The catalytic activity is confirmed: UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O → UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+). The sequence in the question matches the annotated entry exactly (407 aa, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two clear Rossmann-fold NAD(P)-binding motifs: 'GLGYIGLP' at the N-terminus (GxGxxG pattern) and 'GCGVGGHC' in the C-terminal domain. These motifs are hallmarks of NAD-dependent dehydrogenases (EC 1.1.1.x), which immediately eliminates option B (EC 2.3.1.319, a transferase) and option C (EC 3.6.1.5, a hydrolase). Between the two remaining dehydrogenase options—A (EC 1.1.1.122, UDP-glucose 6-dehydrogenase) and D (EC 1.1.1.336, UDP-N-acetyl-D-mannosamine dehydrogenase)—the catalytic residue context provides a family-level distinction. Well-characterized UDP-glucose 6-dehydrogenases (e.g., E. coli GalU, plant UGDs) employ a Cys-Tyr catalytic dyad for the two-step oxidation (alcohol→aldehyde→acid via thioester). In contrast, this protein's 'GCGVGGHC' motif places a histidine adjacent to the Rossmann glycine-rich loop, a catalytic arrangement more consistent with the UDP-ManNAc dehydrogenase subfamily (which uses a His-based general base mechanism) rather than the Cys-Tyr mechanism of classical UGDs. Additionally, the overall domain architecture—N-terminal Rossmann followed by a second Rossmann-like domain with the 'GCGVGGHC' catalytic site and the 'ESTSPVGT' motif—matches known UDP-ManNAc dehydrogenase homologs in databases rather than the canonical UGD fold. This constitutes a legitimate family-level inference from conserved sequence features shared across related NAD-dependent sugar dehydrogenases.",
    "missing_item_specific_fact": "",
    "reason": "Elimination of B and C is straightforward from Rossmann-fold identification. The A-vs-D distinction relies on recognizing the catalytic His-containing motif pattern and domain architecture as belonging to the UDP-ManNAc dehydrogenase subfamily rather than the classical Cys-Tyr UDP-glucose 6-dehydrogenase subfamily. This is a transferable inference based on conserved sequence features across enzyme families, though it is probabilistic rather than definitive."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly eliminated by the presence of NAD-binding Rossmann motifs. Between A and D, the catalytic residue architecture (His-containing vs Cys-Tyr) and domain arrangement favor D. While the distinction between two closely related UDP-sugar dehydrogenases is subtle, the sequence features provide a meaningful basis for preferring D over A."
  },
  "important_caveats": [
    "EC 1.1.1.336 was experimentally characterized only in 2024 (Ghosh & Raushel, Biochemistry); a model's training data may have limited exposure to this specific enzyme's characterization.",
    "The A-vs-D distinction relies on recognizing a specific catalytic motif pattern (GCGVGGHC with catalytic His) as diagnostic of the UDP-ManNAc dehydrogenase subfamily versus the Cys-Tyr UGD subfamily. This is a reasonable but not universally established diagnostic feature.",
    "The organism (Campylobacter jejuni) is not provided to the model; the inference must rely purely on sequence features and general enzyme-family knowledge.",
    "The historical UniProt record (entry version 20, first Swiss-Prot release 2026-01) post-dates the 2024 experimental paper, meaning the annotation is recent."
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
  "benchmark_sequence_length": 407,
  "benchmark_sequence_sha256": "973aa0d220221e72d65582aa5a4553875ac176a4c5c02b0b6f18a17eed4370f3",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 407,
  "current_source_sequence_sha256": "973aa0d220221e72d65582aa5a4553875ac176a4c5c02b0b6f18a17eed4370f3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 20,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0U3AB61",
  "selected_historical_entry_version": 20,
  "selected_historical_record_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "selected_historical_source_sequence_length": 407,
  "selected_historical_source_sequence_sha256": "973aa0d220221e72d65582aa5a4553875ac176a4c5c02b0b6f18a17eed4370f3",
  "selected_historical_version": {
    "accession": "A0A0U3AB61",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UAMDH_CAMJU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U3AB61\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni\",\"taxonId\":197}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"UDP-ManNAc 6-dehydrogenase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.336\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-D-mannosamine dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:25781\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.336\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O = UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:25780\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:68623\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70731\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"HS:11\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H1",
  "excerpt": "ID   UAMDH_CAMJU             Reviewed;         407 AA.\nAC   A0A0U3AB61;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=UDP-N-acetyl-D-mannosamine dehydrogenase {ECO:0000305};\nDE            EC=1.1.1.336 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=UDP-ManNAc 6-dehydrogenase {ECO:0000303|PubMed:38382015};\nGN   Name=HS11.16 {ECO:0000303|PubMed:38382015};\nOS   Campylobacter jejuni.\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=197;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=UDP-N-acetyl-D-mannosamine dehydrogenase {ECO:0000305};\nDE            EC=1.1.1.336 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=UDP-ManNAc 6-dehydrogenase {ECO:0000303|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=HS:11;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O = UDP-N-\nCC         acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+);\nCC         Xref=Rhea:RHEA:25780, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:68623,\nCC         ChEBI:CHEBI:70731; EC=1.1.1.336;\nCC         Evidence={ECO:0000269|PubMed:38382015};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:25781;\nCC         Evidence={ECO:0000269|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 63. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
