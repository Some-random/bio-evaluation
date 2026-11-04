# catalytic_activity_0155

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0155.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — uridine in 28S rRNA + S-adenosyl-L-methionine = N(3)-methyluridine in 28S rRNA + S-adenosyl-L-homocysteine + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKTMLAAPTASSNGRPIGPHKSWKKVNEERKALKRQRKQDKLLKELQQAKEAESQAGKAANEVQAKDKPNPSTLSIAVPGSILENAQSNELRAYVAGQIARAACIFRVNEVIVFDDVGIATARETKRSYEADGEGSSTGTVRSSSLQLARILQYLECPQYLRKYFFPLHKDLKYSGLLNPLDTPHHLRQQSKFRYREGVICDKKAKEGHSYANVGLLNDVLVDKAIEPGVRVTVKMEPQSESCRKQRGTLVSPDEPRRETGVYWGYQVRIAHSMSEIFTKSPYATGYDVTVGTSDRGTNVHEVPNRSYNFNHMLIVFGGLQGLESALANDEKLTVDDPELLFDHYVNVLPRQGSRTIRTEEALLIALAALQEKLQPQVADVEIDLTDLLPKSEDSGIAVRRDVLVSKKQKKRKQVEDTPDETVVDEPSFSKPLPKVARLTANPFADSSEELAKNTPAQDDFEVVSSTTVSGTSHSCADDDLSRFD

[Multiple Choices]
A. cholesterol(in) = cholesterol(out)
B. N(6)-acetyl-L-lysyl-[alpha-tubulin] + H2O = L-lysyl-[alpha-tubulin] + acetate
C. uridine in 28S rRNA + S-adenosyl-L-methionine = N(3)-methyluridine in 28S rRNA + S-adenosyl-L-homocysteine + H(+)
D. O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence matches the reviewed UniProt entry, whose catalytic-activity annotation gives the reaction in choice C and cites experimental evidence (ECO:0000269). The cited paper title also describes deposition of an m3U modification on 28S rRNA. This supports the key, though the underlying paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble SAM-dependent methyltransferase: it has a globular enzyme-like core with glycine-rich regions compatible with a methyltransferase fold, rather than an evident membrane-spanning enzyme, phosphatase, or deacetylase. Transferable knowledge of RNA methyltransferases therefore makes C the meaningful choice among these alternatives. The sequence alone would not establish the precise RNA substrate and methylation site.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level and sequence-pattern inference meaningfully distinguishes the sole methyltransferase option from the offered cholesterol isomerization, lysine deacetylation, and protein dephosphorylation reactions. Exact 28S rRNA and N(3) specificity is not independently resolved by that inference, but no competing option offers another methyltransferase reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C describes a methyl-transfer reaction; the alternatives are chemically distinct activities.


### Important caveats

- The exact substrate and modification site are supported by reviewer-only annotation and its cited evidence, not established from sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble SAM-dependent methyltransferase: it has a globular enzyme-like core with glycine-rich regions compatible with a methyltransferase fold, rather than an evident membrane-spanning enzyme, phosphatase, or deacetylase. Transferable knowledge of RNA methyltransferases therefore makes C the meaningful choice among these alternatives. The sequence alone would not establish the precise RNA substrate and methylation site.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-pattern inference meaningfully distinguishes the sole methyltransferase option from the offered cholesterol isomerization, lysine deacetylation, and protein dephosphorylation reactions. Exact 28S rRNA and N(3) specificity is not independently resolved by that inference, but no competing option offers another methyltransferase reaction."
  },
  "case_id": "catalytic_activity_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the reviewed UniProt entry, whose catalytic-activity annotation gives the reaction in choice C and cites experimental evidence (ECO:0000269). The cited paper title also describes deposition of an m3U modification on 28S rRNA. This supports the key, though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The exact substrate and modification site are supported by reviewer-only annotation and its cited evidence, not established from sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C describes a methyl-transfer reaction; the alternatives are chemically distinct activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the reviewed UniProt entry, whose catalytic-activity annotation gives the reaction in choice C and cites experimental evidence (ECO:0000269). The cited paper title also describes deposition of an m3U modification on 28S rRNA. This supports the key, though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble SAM-dependent methyltransferase: it has a globular enzyme-like core with glycine-rich regions compatible with a methyltransferase fold, rather than an evident membrane-spanning enzyme, phosphatase, or deacetylase. Transferable knowledge of RNA methyltransferases therefore makes C the meaningful choice among these alternatives. The sequence alone would not establish the precise RNA substrate and methylation site.",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-pattern inference meaningfully distinguishes the sole methyltransferase option from the offered cholesterol isomerization, lysine deacetylation, and protein dephosphorylation reactions. Exact 28S rRNA and N(3) specificity is not independently resolved by that inference, but no competing option offers another methyltransferase reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C describes a methyl-transfer reaction; the alternatives are chemically distinct activities."
  },
  "important_caveats": [
    "The exact substrate and modification site are supported by reviewer-only annotation and its cited evidence, not established from sequence features alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A1Z830 (sequence matched, 485 AA) is annotated as '28S rRNA (uridine-N(3))-methyltransferase' (EC 2.1.1.-) with the exact catalytic reaction in option C, supported by experimental evidence (ECO:0000269, PubMed:39671501, Chen et al. 2024 Sci. Adv.). The Rhea reaction RHEA:83635 matches option C verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable SPOUT-domain motifs (e.g., the 'VYWGYQVRI' aromatic-rich region and the 'GTSDRGT' / 'VTVGTSDRGT' stretches around residues ~280-310). The SPOUT domain is a well-characterized RNA methyltransferase fold found across many proteins (bacterial spoU/trmD, eukaryotic SPOUT1/SPOUT2, and numerous bacterial RNA methyltransferases), all of which catalyze SAM-dependent methylation of RNA nucleotides. Recognizing this family immediately identifies the enzyme as an RNA methyltransferase using SAM, which uniquely matches option C among the four choices. Option A (cholesterol transport) requires a multi-pass transmembrane transporter architecture absent here. Option B (tubulin deacetylase) requires HDAC-like catalytic motifs (e.g., the conserved His-Asp-His and Zn-binding motifs) not present. Option D (protein phosphatase) requires PPP/PPM catalytic motifs (e.g., DXD, HG, or binuclear metal-binding residues) not present. The SPOUT-domain recognition is a legitimate family-level transfer from numerous characterized homologs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the SPOUT-domain fold from conserved motifs in the sequence, infer RNA methyltransferase activity from the well-studied SPOUT protein family, and eliminate the transporter, deacetylase, and phosphatase alternatives based on the absence of their signature catalytic/structural features. This is a concrete, transferable family-level inference that meaningfully distinguishes option C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is the only methyltransferase reaction among the four choices. SPOUT-domain recognition unambiguously points to an RNA methyltransferase, and no other option fits. The specific target (28S rRNA) and position (N3-uridine) are harder to pin down from sequence alone, but since C is the sole methyltransferase option, no other choice is defensible.


### Important caveats

- The specific RNA substrate (28S rRNA vs. other rRNAs/tRNAs) and the exact methylation position (N3 of uridine) are not trivially deducible from sequence motifs alone; however, the question only requires selecting among the four provided options, and C is the only SAM-dependent RNA methylation option.
- The SPOUT-domain annotation for this specific protein was experimentally confirmed in 2024 (PubMed:39671501); prior to that, the family assignment was based on homology. The transferable knowledge about the SPOUT family as RNA methyltransferases predates this specific characterization.
- Reviewer-only evidence (UniProt accession, organism, PubMed reference) was not available to the evaluated model; the reasoning above relies solely on sequence motifs and general family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable SPOUT-domain motifs (e.g., the 'VYWGYQVRI' aromatic-rich region and the 'GTSDRGT' / 'VTVGTSDRGT' stretches around residues ~280-310). The SPOUT domain is a well-characterized RNA methyltransferase fold found across many proteins (bacterial spoU/trmD, eukaryotic SPOUT1/SPOUT2, and numerous bacterial RNA methyltransferases), all of which catalyze SAM-dependent methylation of RNA nucleotides. Recognizing this family immediately identifies the enzyme as an RNA methyltransferase using SAM, which uniquely matches option C among the four choices. Option A (cholesterol transport) requires a multi-pass transmembrane transporter architecture absent here. Option B (tubulin deacetylase) requires HDAC-like catalytic motifs (e.g., the conserved His-Asp-His and Zn-binding motifs) not present. Option D (protein phosphatase) requires PPP/PPM catalytic motifs (e.g., DXD, HG, or binuclear metal-binding residues) not present. The SPOUT-domain recognition is a legitimate family-level transfer from numerous characterized homologs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the SPOUT-domain fold from conserved motifs in the sequence, infer RNA methyltransferase activity from the well-studied SPOUT protein family, and eliminate the transporter, deacetylase, and phosphatase alternatives based on the absence of their signature catalytic/structural features. This is a concrete, transferable family-level inference that meaningfully distinguishes option C."
  },
  "case_id": "catalytic_activity_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A1Z830 (sequence matched, 485 AA) is annotated as '28S rRNA (uridine-N(3))-methyltransferase' (EC 2.1.1.-) with the exact catalytic reaction in option C, supported by experimental evidence (ECO:0000269, PubMed:39671501, Chen et al. 2024 Sci. Adv.). The Rhea reaction RHEA:83635 matches option C verbatim."
  },
  "important_caveats": [
    "The specific RNA substrate (28S rRNA vs. other rRNAs/tRNAs) and the exact methylation position (N3 of uridine) are not trivially deducible from sequence motifs alone; however, the question only requires selecting among the four provided options, and C is the only SAM-dependent RNA methylation option.",
    "The SPOUT-domain annotation for this specific protein was experimentally confirmed in 2024 (PubMed:39671501); prior to that, the family assignment was based on homology. The transferable knowledge about the SPOUT family as RNA methyltransferases predates this specific characterization.",
    "Reviewer-only evidence (UniProt accession, organism, PubMed reference) was not available to the evaluated model; the reasoning above relies solely on sequence motifs and general family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is the only methyltransferase reaction among the four choices. SPOUT-domain recognition unambiguously points to an RNA methyltransferase, and no other option fits. The specific target (28S rRNA) and position (N3-uridine) are harder to pin down from sequence alone, but since C is the sole methyltransferase option, no other choice is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A1Z830 (sequence matched, 485 AA) is annotated as '28S rRNA (uridine-N(3))-methyltransferase' (EC 2.1.1.-) with the exact catalytic reaction in option C, supported by experimental evidence (ECO:0000269, PubMed:39671501, Chen et al. 2024 Sci. Adv.). The Rhea reaction RHEA:83635 matches option C verbatim.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable SPOUT-domain motifs (e.g., the 'VYWGYQVRI' aromatic-rich region and the 'GTSDRGT' / 'VTVGTSDRGT' stretches around residues ~280-310). The SPOUT domain is a well-characterized RNA methyltransferase fold found across many proteins (bacterial spoU/trmD, eukaryotic SPOUT1/SPOUT2, and numerous bacterial RNA methyltransferases), all of which catalyze SAM-dependent methylation of RNA nucleotides. Recognizing this family immediately identifies the enzyme as an RNA methyltransferase using SAM, which uniquely matches option C among the four choices. Option A (cholesterol transport) requires a multi-pass transmembrane transporter architecture absent here. Option B (tubulin deacetylase) requires HDAC-like catalytic motifs (e.g., the conserved His-Asp-His and Zn-binding motifs) not present. Option D (protein phosphatase) requires PPP/PPM catalytic motifs (e.g., DXD, HG, or binuclear metal-binding residues) not present. The SPOUT-domain recognition is a legitimate family-level transfer from numerous characterized homologs.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the SPOUT-domain fold from conserved motifs in the sequence, infer RNA methyltransferase activity from the well-studied SPOUT protein family, and eliminate the transporter, deacetylase, and phosphatase alternatives based on the absence of their signature catalytic/structural features. This is a concrete, transferable family-level inference that meaningfully distinguishes option C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is the only methyltransferase reaction among the four choices. SPOUT-domain recognition unambiguously points to an RNA methyltransferase, and no other option fits. The specific target (28S rRNA) and position (N3-uridine) are harder to pin down from sequence alone, but since C is the sole methyltransferase option, no other choice is defensible."
  },
  "important_caveats": [
    "The specific RNA substrate (28S rRNA vs. other rRNAs/tRNAs) and the exact methylation position (N3 of uridine) are not trivially deducible from sequence motifs alone; however, the question only requires selecting among the four provided options, and C is the only SAM-dependent RNA methylation option.",
    "The SPOUT-domain annotation for this specific protein was experimentally confirmed in 2024 (PubMed:39671501); prior to that, the family assignment was based on homology. The transferable knowledge about the SPOUT family as RNA methyltransferases predates this specific characterization.",
    "Reviewer-only evidence (UniProt accession, organism, PubMed reference) was not available to the evaluated model; the reasoning above relies solely on sequence motifs and general family knowledge."
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
  "benchmark_sequence_length": 485,
  "benchmark_sequence_sha256": "4f2ef6e6072d9758a23d9c485c14bc69df5f879c14058136a5103951746d6c1a",
  "current_entry_audit": {
    "entryVersion": 124,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-02-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 485,
  "current_source_sequence_sha256": "4f2ef6e6072d9758a23d9c485c14bc69df5f879c14058136a5103951746d6c1a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 122,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A1Z830",
  "selected_historical_entry_version": 122,
  "selected_historical_record_sha256": "104e9d6a622cdc871df72441a8a1c4c9cdae0ef3e255b6a18cf6297f273fb42c",
  "selected_historical_source_sequence_length": 485,
  "selected_historical_source_sequence_sha256": "4f2ef6e6072d9758a23d9c485c14bc69df5f879c14058136a5103951746d6c1a",
  "selected_historical_version": {
    "accession": "A1Z830",
    "database": "Swiss-Prot",
    "entryVersion": 122,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SPOUT_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1Z830.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A1Z830\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:46.725323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac",
  "url": "https://rest.uniprot.org/uniprotkb/A1Z830.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1Z830.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":124,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-02-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:46.725323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac",
  "url": "https://rest.uniprot.org/uniprotkb/A1Z830.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1Z830.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:46.725323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac",
  "url": "https://rest.uniprot.org/uniprotkb/A1Z830.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1Z830.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39671501\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"value\":\"28S rRNA (uridine-N(3))-methyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:46.725323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac",
  "url": "https://rest.uniprot.org/uniprotkb/A1Z830.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1Z830.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39671501\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:83636\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39671501\",\"source\":\"PubMed\"}],\"name\":\"uridine in 28S rRNA + S-adenosyl-L-methionine = N(3)-methyluridine in 28S rRNA + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83635\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:20178\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:20181\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74502\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:46.725323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac",
  "url": "https://rest.uniprot.org/uniprotkb/A1Z830.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1Z830.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Chen J.\",\"Bai Y.\",\"Huang Y.\",\"Cui M.\",\"Wang Y.\",\"Gu Z.\",\"Wu X.\",\"Li Y.\",\"Rong Y.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39671501\"},{\"database\":\"DOI\",\"id\":\"10.1126/sciadv.adr1743\"}],\"citationType\":\"journal article\",\"firstPage\":\"eadr1743\",\"id\":\"39671501\",\"journal\":\"Sci. Adv.\",\"lastPage\":\"eadr1743\",\"publicationDate\":\"2024\",\"title\":\"The Ptch/SPOUT1 methyltransferase deposits an m3U modification on 28S rRNA for normal ribosomal function in flies and humans.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:26:46.725323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4de9be795c2a99805d6ce7ac0a27b66607b8b069286e0594a016112d990fb2ac",
  "url": "https://rest.uniprot.org/uniprotkb/A1Z830.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H1",
  "excerpt": "ID   SPOUT_DROME             Reviewed;         485 AA.\nAC   A1Z830;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-FEB-2007, sequence version 1.\nDT   28-JAN-2026, entry version 122.\nDE   RecName: Full=28S rRNA (uridine-N(3))-methyltransferase;\nDE            EC=2.1.1.- {ECO:0000269|PubMed:39671501};\nGN   Name=ptch {ECO:0000303|PubMed:39671501};\nGN   ORFNames=CG12128 {ECO:0000312|EMBL:AAF58861.1};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.361895+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "104e9d6a622cdc871df72441a8a1c4c9cdae0ef3e255b6a18cf6297f273fb42c",
  "url": "https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=28S rRNA (uridine-N(3))-methyltransferase;\nDE            EC=2.1.1.- {ECO:0000269|PubMed:39671501};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.361895+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "104e9d6a622cdc871df72441a8a1c4c9cdae0ef3e255b6a18cf6297f273fb42c",
  "url": "https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND SUBCELLULAR LOCATION.\nRX   PubMed=39671501; DOI=10.1126/sciadv.adr1743;\nRA   Chen J., Bai Y., Huang Y., Cui M., Wang Y., Gu Z., Wu X., Li Y., Rong Y.S.;\nRT   \"The Ptch/SPOUT1 methyltransferase deposits an m3U modification on 28S rRNA\nRT   for normal ribosomal function in flies and humans.\";\nRL   Sci. Adv. 10:eadr1743-eadr1743(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.361895+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "104e9d6a622cdc871df72441a8a1c4c9cdae0ef3e255b6a18cf6297f273fb42c",
  "url": "https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=uridine in 28S rRNA + S-adenosyl-L-methionine = N(3)-\nCC         methyluridine in 28S rRNA + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:83635, Rhea:RHEA-COMP:20178, Rhea:RHEA-COMP:20181,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:65315, ChEBI:CHEBI:74502;\nCC         Evidence={ECO:0000269|PubMed:39671501};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83636;\nCC         Evidence={ECO:0000305|PubMed:39671501};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.361895+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "104e9d6a622cdc871df72441a8a1c4c9cdae0ef3e255b6a18cf6297f273fb42c",
  "url": "https://rest.uniprot.org/unisave/A1Z830?format=txt&versions=122"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 155. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
