# active_site_0077

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0077.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 254 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
METVESSSSAELLRAQMHFSTQLFGFHYTAALKCAVKLGIPDAIKQHGKPMNLSELNSALSINPSKAPCIHRLMRILVTAGYFAQENECFSLTSAGRHFLKDDPLNIRALVLLELHPALVKPWIALGEWFQNDDVSPFATAHGKSFWDYVTSDPELRKLFDESMADDSQLIAKALVTEFRYVFEGLKSLVDVGGGSGTLARAIAKAFPNLKCTVCDLPDAVANEHGDGNLDFVAGDMFERVPSADSILLKHILHDWSDEKCVEILKKCREAIPKNGGKVIIVDKLLKNRGHGHAENEHDEATESPLSCDMEMLVLVNGKERDEKEWAKLFSGAGFNDYKYNITPVLGSTSLIEVNFYN

[Multiple Choices]
A. Position 117 (Charge relay)
B. Position 254 (Proton acceptor)
C. Position 205 (For beta-ketoacyl synthase activity)
D. Position 216 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies position 254 as the proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental evidence for that residue's role.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features consistent with a SAM-dependent plant O-methyltransferase, including a glycine-rich region associated with SAM binding and a histidine-containing region near position 254. Transferable knowledge of this enzyme family supports a conserved catalytic histidine acting as a proton acceptor, distinguishing B from the beta-ketoacyl-synthase distractor and the other proposed residue roles.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features and the known chemistry of SAM-dependent O-methyltransferases provide a meaningful basis for selecting the catalytic proton acceptor. The exact residue assignment is still an inference from family conservation, not something proven from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, position 254 as proton acceptor is the defensible family-based assignment; the alternatives describe different or incompatible roles.


### Important caveats

- The residue-level source annotation is computationally rule-based; the supplied evidence does not independently establish experimental validation of the catalytic role.
- The reviewer-only source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a SAM-dependent plant O-methyltransferase, including a glycine-rich region associated with SAM binding and a histidine-containing region near position 254. Transferable knowledge of this enzyme family supports a conserved catalytic histidine acting as a proton acceptor, distinguishing B from the beta-ketoacyl-synthase distractor and the other proposed residue roles.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features and the known chemistry of SAM-dependent O-methyltransferases provide a meaningful basis for selecting the catalytic proton acceptor. The exact residue assignment is still an inference from family conservation, not something proven from the sequence alone."
  },
  "case_id": "active_site_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 254 as the proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental evidence for that residue's role."
  },
  "important_caveats": [
    "The residue-level source annotation is computationally rule-based; the supplied evidence does not independently establish experimental validation of the catalytic role.",
    "The reviewer-only source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, position 254 as proton acceptor is the defensible family-based assignment; the alternatives describe different or incompatible roles."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 254 as the proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental evidence for that residue's role.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features consistent with a SAM-dependent plant O-methyltransferase, including a glycine-rich region associated with SAM binding and a histidine-containing region near position 254. Transferable knowledge of this enzyme family supports a conserved catalytic histidine acting as a proton acceptor, distinguishing B from the beta-ketoacyl-synthase distractor and the other proposed residue roles.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features and the known chemistry of SAM-dependent O-methyltransferases provide a meaningful basis for selecting the catalytic proton acceptor. The exact residue assignment is still an inference from family conservation, not something proven from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, position 254 as proton acceptor is the defensible family-based assignment; the alternatives describe different or incompatible roles."
  },
  "important_caveats": [
    "The residue-level source annotation is computationally rule-based; the supplied evidence does not independently establish experimental validation of the catalytic role.",
    "The reviewer-only source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) explicitly lists position 254 as 'Active site' with description 'Proton acceptor', annotated via PROSITE-ProRule PRU01020 (SAM-dependent methyltransferase profile). The residue at position 254 in the supplied sequence is Histidine (H), consistent with the well-characterized catalytic general base in plant O-methyltransferases. The evidence code ECO:0000255 indicates a profile-based computational annotation rather than direct mutagenesis on this specific protein, but the mechanism is strongly supported by structural and biochemical studies of homologous plant OMTs.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark GGGSG SAM-binding motif (positions ~193-197) and the conserved FSGAGFNDY motif near the C-terminus, identifying this as a class I SAM-dependent O-methyltransferase. In plant O-methyltransferases (e.g., caffeic acid O-methyltransferase, isoflavone O-methyltransferase, and numerous other plant OMTs), the catalytic mechanism involves a conserved histidine acting as a general base (proton acceptor) that deprotonates the substrate hydroxyl to generate a nucleophilic alkoxide for methyl transfer from SAM. Position 254 is a Histidine located in the expected catalytic region. The distractors are eliminable by family knowledge: (A) 'charge relay' describes the Ser-His-Asp triad of serine proteases, not methyltransferases, and position 117 is Proline; (C) 'beta-ketoacyl synthase activity' is a fatty-acid synthase function entirely unrelated to methyltransferases; (D) position 216 (Asp) falls within the SAM-binding region (part of the conserved motif around the GGGSG block), and the mechanistic role in OMTs is proton ACCEPTOR not proton donor. Thus family-level recognition plus mechanistic knowledge of plant OMT catalysis distinguishes B from the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the enzyme family from the GGGSG and FSGAGFNDY motifs, recall that plant OMTs use a catalytic His as proton acceptor (well-established from COMT, IOMT, and many homologs), and eliminate the clearly mismatched distractors (charge relay, beta-ketoacyl synthase, proton donor) using general mechanistic knowledge. No fact specific to this exact protein beyond family-level features is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mechanistically and functionally distinct. Only position 254 (His, proton acceptor) is consistent with the catalytic mechanism of a SAM-dependent O-methyltransferase. The other options invoke unrelated enzyme mechanisms (charge relay, beta-ketoacyl synthase) or misassign the mechanistic role (proton donor for a SAM-binding Asp).


### Important caveats

- The active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a profile-based computational assignment rather than direct experimental mutagenesis on this specific protein. However, the catalytic His mechanism is well-supported across the plant OMT family by structural and biochemical data on homologs.
- The reviewer-only evidence confirms the protein is D3KYA0 (IpeOMT3 from Carapichea ipecacuanha), but this identity was not provided to the evaluated model; the reasoning relies on recognizing methyltransferase motifs in the sequence itself.
- The annotation was first integrated into Swiss-Prot in June 2025; the historical entry version 55 (January 2026) already contains the active-site annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark GGGSG SAM-binding motif (positions ~193-197) and the conserved FSGAGFNDY motif near the C-terminus, identifying this as a class I SAM-dependent O-methyltransferase. In plant O-methyltransferases (e.g., caffeic acid O-methyltransferase, isoflavone O-methyltransferase, and numerous other plant OMTs), the catalytic mechanism involves a conserved histidine acting as a general base (proton acceptor) that deprotonates the substrate hydroxyl to generate a nucleophilic alkoxide for methyl transfer from SAM. Position 254 is a Histidine located in the expected catalytic region. The distractors are eliminable by family knowledge: (A) 'charge relay' describes the Ser-His-Asp triad of serine proteases, not methyltransferases, and position 117 is Proline; (C) 'beta-ketoacyl synthase activity' is a fatty-acid synthase function entirely unrelated to methyltransferases; (D) position 216 (Asp) falls within the SAM-binding region (part of the conserved motif around the GGGSG block), and the mechanistic role in OMTs is proton ACCEPTOR not proton donor. Thus family-level recognition plus mechanistic knowledge of plant OMT catalysis distinguishes B from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the enzyme family from the GGGSG and FSGAGFNDY motifs, recall that plant OMTs use a catalytic His as proton acceptor (well-established from COMT, IOMT, and many homologs), and eliminate the clearly mismatched distractors (charge relay, beta-ketoacyl synthase, proton donor) using general mechanistic knowledge. No fact specific to this exact protein beyond family-level features is needed."
  },
  "case_id": "active_site_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly lists position 254 as 'Active site' with description 'Proton acceptor', annotated via PROSITE-ProRule PRU01020 (SAM-dependent methyltransferase profile). The residue at position 254 in the supplied sequence is Histidine (H), consistent with the well-characterized catalytic general base in plant O-methyltransferases. The evidence code ECO:0000255 indicates a profile-based computational annotation rather than direct mutagenesis on this specific protein, but the mechanism is strongly supported by structural and biochemical studies of homologous plant OMTs."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a profile-based computational assignment rather than direct experimental mutagenesis on this specific protein. However, the catalytic His mechanism is well-supported across the plant OMT family by structural and biochemical data on homologs.",
    "The reviewer-only evidence confirms the protein is D3KYA0 (IpeOMT3 from Carapichea ipecacuanha), but this identity was not provided to the evaluated model; the reasoning relies on recognizing methyltransferase motifs in the sequence itself.",
    "The annotation was first integrated into Swiss-Prot in June 2025; the historical entry version 55 (January 2026) already contains the active-site annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mechanistically and functionally distinct. Only position 254 (His, proton acceptor) is consistent with the catalytic mechanism of a SAM-dependent O-methyltransferase. The other options invoke unrelated enzyme mechanisms (charge relay, beta-ketoacyl synthase) or misassign the mechanistic role (proton donor for a SAM-binding Asp)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly lists position 254 as 'Active site' with description 'Proton acceptor', annotated via PROSITE-ProRule PRU01020 (SAM-dependent methyltransferase profile). The residue at position 254 in the supplied sequence is Histidine (H), consistent with the well-characterized catalytic general base in plant O-methyltransferases. The evidence code ECO:0000255 indicates a profile-based computational annotation rather than direct mutagenesis on this specific protein, but the mechanism is strongly supported by structural and biochemical studies of homologous plant OMTs.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark GGGSG SAM-binding motif (positions ~193-197) and the conserved FSGAGFNDY motif near the C-terminus, identifying this as a class I SAM-dependent O-methyltransferase. In plant O-methyltransferases (e.g., caffeic acid O-methyltransferase, isoflavone O-methyltransferase, and numerous other plant OMTs), the catalytic mechanism involves a conserved histidine acting as a general base (proton acceptor) that deprotonates the substrate hydroxyl to generate a nucleophilic alkoxide for methyl transfer from SAM. Position 254 is a Histidine located in the expected catalytic region. The distractors are eliminable by family knowledge: (A) 'charge relay' describes the Ser-His-Asp triad of serine proteases, not methyltransferases, and position 117 is Proline; (C) 'beta-ketoacyl synthase activity' is a fatty-acid synthase function entirely unrelated to methyltransferases; (D) position 216 (Asp) falls within the SAM-binding region (part of the conserved motif around the GGGSG block), and the mechanistic role in OMTs is proton ACCEPTOR not proton donor. Thus family-level recognition plus mechanistic knowledge of plant OMT catalysis distinguishes B from the other options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the enzyme family from the GGGSG and FSGAGFNDY motifs, recall that plant OMTs use a catalytic His as proton acceptor (well-established from COMT, IOMT, and many homologs), and eliminate the clearly mismatched distractors (charge relay, beta-ketoacyl synthase, proton donor) using general mechanistic knowledge. No fact specific to this exact protein beyond family-level features is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mechanistically and functionally distinct. Only position 254 (His, proton acceptor) is consistent with the catalytic mechanism of a SAM-dependent O-methyltransferase. The other options invoke unrelated enzyme mechanisms (charge relay, beta-ketoacyl synthase) or misassign the mechanistic role (proton donor for a SAM-binding Asp)."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a profile-based computational assignment rather than direct experimental mutagenesis on this specific protein. However, the catalytic His mechanism is well-supported across the plant OMT family by structural and biochemical data on homologs.",
    "The reviewer-only evidence confirms the protein is D3KYA0 (IpeOMT3 from Carapichea ipecacuanha), but this identity was not provided to the evaluated model; the reasoning relies on recognizing methyltransferase motifs in the sequence itself.",
    "The annotation was first integrated into Swiss-Prot in June 2025; the historical entry version 55 (January 2026) already contains the active-site annotation."
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
  "benchmark_sequence_length": 358,
  "benchmark_sequence_sha256": "b42926ade645f070c913bd00eaccaa6a9eecc7a916f573ff2ef68122889f81c1",
  "current_entry_audit": {
    "entryVersion": 57,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-04-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 358,
  "current_source_sequence_sha256": "b42926ade645f070c913bd00eaccaa6a9eecc7a916f573ff2ef68122889f81c1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D3KYA0",
  "selected_historical_entry_version": 55,
  "selected_historical_record_sha256": "b2752ed70781d19baf56582001780d450973cdc5bdf7404b99bcf5d3ef0488be",
  "selected_historical_source_sequence_length": 358,
  "selected_historical_source_sequence_sha256": "b42926ade645f070c913bd00eaccaa6a9eecc7a916f573ff2ef68122889f81c1",
  "selected_historical_version": {
    "accession": "D3KYA0",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OMT3_CARIP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D3KYA0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":57,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-04-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"(S)-norreticuline 7-O-methyltransferase IpeOMT1\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Ipecac/benzylisoquinoline alkaloid O-methyltransferase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI79245.1\",\"source\":\"EMBL\"}],\"value\":\"IpeOMT3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"3-O-methylredipecamine 2-O-methyltransferase IpeOMT3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":254},\"start\":{\"modifier\":\"EXACT\",\"value\":254}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":193}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":216},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":236},\"start\":{\"modifier\":\"EXACT\",\"value\":236}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":237},\"start\":{\"modifier\":\"EXACT\",\"value\":237}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":250},\"start\":{\"modifier\":\"EXACT\",\"value\":250}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KYA0.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Nomura T.\",\"Kutchan T.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20061395\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.086157\"}],\"citationType\":\"journal article\",\"firstPage\":\"7722\",\"id\":\"20061395\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"7738\",\"publicationDate\":\"2010\",\"title\":\"Three new O-methyltransferases are sufficient for all O-methylation reactions of ipecac alkaloid biosynthesis in root culture of Psychotria ipecacuanha.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI79245.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:05.017010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8911ef7ad13ac56e9c6773425d0a513fcd7261f04f5d354fbd82723603276578",
  "url": "https://rest.uniprot.org/uniprotkb/D3KYA0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H1",
  "excerpt": "ID   OMT3_CARIP              Reviewed;         358 AA.\nAC   D3KYA0;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-APR-2010, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=3-O-methylredipecamine 2-O-methyltransferase IpeOMT3 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=(S)-norreticuline 7-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=Ipecac/benzylisoquinoline alkaloid O-methyltransferase 3 {ECO:0000303|PubMed:20061395};\nDE            Short=IpeOMT3 {ECO:0000303|PubMed:20061395, ECO:0000312|EMBL:BAI79245.1};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nGN   Name=OMT3 {ECO:0000312|EMBL:BAI79245.1};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.691295+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b2752ed70781d19baf56582001780d450973cdc5bdf7404b99bcf5d3ef0488be",
  "url": "https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAI79245.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, PATHWAY, AND TISSUE\nRP   SPECIFICITY.\nRC   TISSUE=Root;\nRX   PubMed=20061395; DOI=10.1074/jbc.m109.086157;\nRA   Nomura T., Kutchan T.M.;\nRT   \"Three new O-methyltransferases are sufficient for all O-methylation\nRT   reactions of ipecac alkaloid biosynthesis in root culture of Psychotria\nRT   ipecacuanha.\";\nRL   J. Biol. Chem. 285:7722-7738(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.691295+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b2752ed70781d19baf56582001780d450973cdc5bdf7404b99bcf5d3ef0488be",
  "url": "https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        254\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.691295+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b2752ed70781d19baf56582001780d450973cdc5bdf7404b99bcf5d3ef0488be",
  "url": "https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         193\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.691295+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b2752ed70781d19baf56582001780d450973cdc5bdf7404b99bcf5d3ef0488be",
  "url": "https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         216\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.691295+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b2752ed70781d19baf56582001780d450973cdc5bdf7404b99bcf5d3ef0488be",
  "url": "https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         236\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.691295+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b2752ed70781d19baf56582001780d450973cdc5bdf7404b99bcf5d3ef0488be",
  "url": "https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         237\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.691295+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b2752ed70781d19baf56582001780d450973cdc5bdf7404b99bcf5d3ef0488be",
  "url": "https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         250\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.691295+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b2752ed70781d19baf56582001780d450973cdc5bdf7404b99bcf5d3ef0488be",
  "url": "https://rest.uniprot.org/unisave/D3KYA0?format=txt&versions=55"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 77. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
