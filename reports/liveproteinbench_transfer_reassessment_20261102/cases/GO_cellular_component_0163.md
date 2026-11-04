# GO_cellular_component_0163

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0163.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — RQC complex

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSRRALRRLRGEQRGQEPLGPDALQFVLLDDDDAEEEGPKTGLGGRRPGGAGKEGVRVNNRFELINIEDLEDDLVVNGERSDCTLPDSASSGNKGRAKHGNPENKQDGDAAAKAGSSEQSNASGKLRKKKKKQKNKKSCTGESSENGLEDIDRILERIEDSSGFSHPGPPPLSSRKHVLYVEHRHLNPDTELKRYFGARAVLGEQRPRQRQRVYPKCTWLTTPKSTWPRYSKPGLSMRLLESKKGLSFFAFEHSEEYQQAQHKFLVAVESMEPNNIVALLQTSPYHVDSLLQLSDACRFQEDQEMARDLIGEPAYPHLLPMEKSWCRRPHWSFYLALYKQMSFLEKRGCPRTALEYCKLILSLEPDEDPLCMLLLIDHMALRARNYEYLIRLFQEWEAHRNLSQLPNFAFSVPLAYFLLSQQTDLPDHELSSARQQASLLIQQALTMFPGVLMPLLEYCSVRPDATVSNHRFFGPDAEISQPPALSQLVSLYLGRSHFLWKEPAIMSWLEENVHEVLEAVDSGDPAVEACENRRKVLYQRAPRNIHRHVILSEIKEAVAALPSDVTTQSVMGFDPLPPVDTIYSYVRPERLSPVSHGNTIALFFRSLLPNYTTEGERLEEGVAGGPNRNQGLNRLMLAVRDMMANFHFNDLEVPREDNPEGEGDWD

[Multiple Choices]
A. lipid droplet
B. RQC complex
C. ATP-binding cassette (ABC) transporter complex
D. other organism cell membrane
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches a record with a GO annotation to RQC complex (H6; also C8), supporting B as a cellular-component annotation. This is orthology-based inference (ISO:RGD), not direct experimental evidence for RQC association. The record separately reports experimentally supported mainly nuclear localization, so the evidence does not establish RQC complex as the protein's predominant location.

Citations as saved: [H6](#evidence-h6), [C8](#evidence-c8), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Whether this particular protein is associated with the RQC complex; the sequence alone does not establish that specific complex membership.


**Reason**

> The sequence lacks obvious membrane-spanning segments and recognizable ABC-transporter ATP-binding features, which weigh against C and D. But those general features do not meaningfully separate RQC complex membership from lipid-droplet association, and no clear sequence feature here identifies an RQC component. Choosing B therefore depends on the protein-specific association annotation rather than a transferable inference from the provided sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second offered option is supported by the supplied evidence. However, 'primary' localization is potentially misleading: the evidence reports mainly nuclear localization, which is not an option, while B is an inferred complex annotation.


### Important caveats

- The RQC complex assignment is an orthology-based GO annotation, not direct experimental evidence for this sequence.
- The source's mainly nuclear localization is experimentally supported, so the evidence does not show that RQC complex is the protein's predominant cellular location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular protein is associated with the RQC complex; the sequence alone does not establish that specific complex membership.",
    "reason": "The sequence lacks obvious membrane-spanning segments and recognizable ABC-transporter ATP-binding features, which weigh against C and D. But those general features do not meaningfully separate RQC complex membership from lipid-droplet association, and no clear sequence feature here identifies an RQC component. Choosing B therefore depends on the protein-specific association annotation rather than a transferable inference from the provided sequence."
  },
  "case_id": "GO_cellular_component_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "C8",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a record with a GO annotation to RQC complex (H6; also C8), supporting B as a cellular-component annotation. This is orthology-based inference (ISO:RGD), not direct experimental evidence for RQC association. The record separately reports experimentally supported mainly nuclear localization, so the evidence does not establish RQC complex as the protein's predominant location."
  },
  "important_caveats": [
    "The RQC complex assignment is an orthology-based GO annotation, not direct experimental evidence for this sequence.",
    "The source's mainly nuclear localization is experimentally supported, so the evidence does not show that RQC complex is the protein's predominant cellular location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered option is supported by the supplied evidence. However, 'primary' localization is potentially misleading: the evidence reports mainly nuclear localization, which is not an option, while B is an inferred complex annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a record with a GO annotation to RQC complex (H6; also C8), supporting B as a cellular-component annotation. This is orthology-based inference (ISO:RGD), not direct experimental evidence for RQC association. The record separately reports experimentally supported mainly nuclear localization, so the evidence does not establish RQC complex as the protein's predominant location.",
    "evidence_ids": ["H6", "C8", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Whether this particular protein is associated with the RQC complex; the sequence alone does not establish that specific complex membership.",
    "reason": "The sequence lacks obvious membrane-spanning segments and recognizable ABC-transporter ATP-binding features, which weigh against C and D. But those general features do not meaningfully separate RQC complex membership from lipid-droplet association, and no clear sequence feature here identifies an RQC component. Choosing B therefore depends on the protein-specific association annotation rather than a transferable inference from the provided sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered option is supported by the supplied evidence. However, 'primary' localization is potentially misleading: the evidence reports mainly nuclear localization, which is not an option, while B is an inferred complex annotation."
  },
  "important_caveats": [
    "The RQC complex assignment is an orthology-based GO annotation, not direct experimental evidence for this sequence.",
    "The source's mainly nuclear localization is experimentally supported, so the evidence does not show that RQC complex is the protein's predominant cellular location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A8I6ASZ5 (TCF25_RAT) carries GO:1990112 (C:RQC complex) with ISO:RGD evidence (C8, H6), and the recommended protein name is 'Ribosome quality control complex subunit TCF25' (C4, H1). The RQC complex annotation is present in the database. However, the experimental subcellular location evidence (PubMed:32805187) states 'Mainly nuclear' and 'Cytoplasm, cytosol' rather than directly confirming RQC complex membership; the RQC annotation is inferred from orthology (ISO:RGD), not experimentally verified for this exact protein. Nonetheless, the annotation and protein naming directly support choice B.

Citations as saved: [C4](#evidence-c4), [C8](#evidence-c8), [H1](#evidence-h1), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks any transmembrane helices or ABC signature motifs (e.g., LSGGQ, multiple hydrophobic TM segments), which are hallmarks of ABC transporter complex components (option C) and membrane proteins (option D). It also lacks lipid droplet targeting motifs (option A). The sequence contains a strong basic NLS region (KKKKKQKNKKS) and zinc-finger-like domains (CXXC/CCHC motifs in the C-terminal region), consistent with a soluble nuclear/cytoplasmic protein complex component. The RQC complex (GO:1990112) is a well-characterized nuclear/cytoplasmic multiprotein complex (including AAA-ATPases, E3 ligases, zinc-finger proteins). By elimination of A, C, and D based on clear negative sequence evidence, and positive features (NLS, zinc fingers, soluble architecture) consistent with a nuclear protein complex, B is the most defensible choice. This is a standard elimination-plus-consistency argument using well-known structural requirements of the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C (no TM domains or ABC motifs), D (no membrane targeting, implausible for rat protein), and A (no lipid droplet targeting sequences) based on well-established sequence features of those compartments. The remaining option B (RQC complex) is a nuclear/cytoplasmic protein complex whose components commonly contain zinc fingers and NLS signals, matching the observed sequence. This is transferable knowledge about protein families and compartment requirements.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (lipid droplet, ABC transporter complex, other organism cell membrane) are clearly inconsistent with the sequence features (no TM helices, no lipid targeting, no membrane signals), leaving B as the only viable option among the four. No other choice is defensible given the sequence.


### Important caveats

- The RQC complex annotation (GO:1990112) for this protein carries ISO:RGD (inferred from orthology) evidence, not direct experimental validation for this specific rat protein.
- The experimental subcellular location evidence states 'Mainly nuclear' and 'Cytoplasm, cytosol' rather than explicitly confirming RQC complex membership.
- The Swiss-Prot entry was first public in April 2025; the benchmark construction date is unknown, so the annotation timeline relative to the question is uncertain.
- The reasoning relies primarily on elimination of the three clearly incompatible options rather than positive identification of RQC complex-specific sequence signatures.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks any transmembrane helices or ABC signature motifs (e.g., LSGGQ, multiple hydrophobic TM segments), which are hallmarks of ABC transporter complex components (option C) and membrane proteins (option D). It also lacks lipid droplet targeting motifs (option A). The sequence contains a strong basic NLS region (KKKKKQKNKKS) and zinc-finger-like domains (CXXC/CCHC motifs in the C-terminal region), consistent with a soluble nuclear/cytoplasmic protein complex component. The RQC complex (GO:1990112) is a well-characterized nuclear/cytoplasmic multiprotein complex (including AAA-ATPases, E3 ligases, zinc-finger proteins). By elimination of A, C, and D based on clear negative sequence evidence, and positive features (NLS, zinc fingers, soluble architecture) consistent with a nuclear protein complex, B is the most defensible choice. This is a standard elimination-plus-consistency argument using well-known structural requirements of the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C (no TM domains or ABC motifs), D (no membrane targeting, implausible for rat protein), and A (no lipid droplet targeting sequences) based on well-established sequence features of those compartments. The remaining option B (RQC complex) is a nuclear/cytoplasmic protein complex whose components commonly contain zinc fingers and NLS signals, matching the observed sequence. This is transferable knowledge about protein families and compartment requirements."
  },
  "case_id": "GO_cellular_component_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C8",
      "H1",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A8I6ASZ5 (TCF25_RAT) carries GO:1990112 (C:RQC complex) with ISO:RGD evidence (C8, H6), and the recommended protein name is 'Ribosome quality control complex subunit TCF25' (C4, H1). The RQC complex annotation is present in the database. However, the experimental subcellular location evidence (PubMed:32805187) states 'Mainly nuclear' and 'Cytoplasm, cytosol' rather than directly confirming RQC complex membership; the RQC annotation is inferred from orthology (ISO:RGD), not experimentally verified for this exact protein. Nonetheless, the annotation and protein naming directly support choice B."
  },
  "important_caveats": [
    "The RQC complex annotation (GO:1990112) for this protein carries ISO:RGD (inferred from orthology) evidence, not direct experimental validation for this specific rat protein.",
    "The experimental subcellular location evidence states 'Mainly nuclear' and 'Cytoplasm, cytosol' rather than explicitly confirming RQC complex membership.",
    "The Swiss-Prot entry was first public in April 2025; the benchmark construction date is unknown, so the annotation timeline relative to the question is uncertain.",
    "The reasoning relies primarily on elimination of the three clearly incompatible options rather than positive identification of RQC complex-specific sequence signatures."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (lipid droplet, ABC transporter complex, other organism cell membrane) are clearly inconsistent with the sequence features (no TM helices, no lipid targeting, no membrane signals), leaving B as the only viable option among the four. No other choice is defensible given the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A8I6ASZ5 (TCF25_RAT) carries GO:1990112 (C:RQC complex) with ISO:RGD evidence (C8, H6), and the recommended protein name is 'Ribosome quality control complex subunit TCF25' (C4, H1). The RQC complex annotation is present in the database. However, the experimental subcellular location evidence (PubMed:32805187) states 'Mainly nuclear' and 'Cytoplasm, cytosol' rather than directly confirming RQC complex membership; the RQC annotation is inferred from orthology (ISO:RGD), not experimentally verified for this exact protein. Nonetheless, the annotation and protein naming directly support choice B.",
    "evidence_ids": ["C4", "C8", "H1", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence lacks any transmembrane helices or ABC signature motifs (e.g., LSGGQ, multiple hydrophobic TM segments), which are hallmarks of ABC transporter complex components (option C) and membrane proteins (option D). It also lacks lipid droplet targeting motifs (option A). The sequence contains a strong basic NLS region (KKKKKQKNKKS) and zinc-finger-like domains (CXXC/CCHC motifs in the C-terminal region), consistent with a soluble nuclear/cytoplasmic protein complex component. The RQC complex (GO:1990112) is a well-characterized nuclear/cytoplasmic multiprotein complex (including AAA-ATPases, E3 ligases, zinc-finger proteins). By elimination of A, C, and D based on clear negative sequence evidence, and positive features (NLS, zinc fingers, soluble architecture) consistent with a nuclear protein complex, B is the most defensible choice. This is a standard elimination-plus-consistency argument using well-known structural requirements of the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C (no TM domains or ABC motifs), D (no membrane targeting, implausible for rat protein), and A (no lipid droplet targeting sequences) based on well-established sequence features of those compartments. The remaining option B (RQC complex) is a nuclear/cytoplasmic protein complex whose components commonly contain zinc fingers and NLS signals, matching the observed sequence. This is transferable knowledge about protein families and compartment requirements."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (lipid droplet, ABC transporter complex, other organism cell membrane) are clearly inconsistent with the sequence features (no TM helices, no lipid targeting, no membrane signals), leaving B as the only viable option among the four. No other choice is defensible given the sequence."
  },
  "important_caveats": [
    "The RQC complex annotation (GO:1990112) for this protein carries ISO:RGD (inferred from orthology) evidence, not direct experimental validation for this specific rat protein.",
    "The experimental subcellular location evidence states 'Mainly nuclear' and 'Cytoplasm, cytosol' rather than explicitly confirming RQC complex membership.",
    "The Swiss-Prot entry was first public in April 2025; the benchmark construction date is unknown, so the annotation timeline relative to the question is uncertain.",
    "The reasoning relies primarily on elimination of the three clearly incompatible options rather than positive identification of RQC complex-specific sequence signatures."
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
  "benchmark_sequence_length": 666,
  "benchmark_sequence_sha256": "b55974f94d7023b0272ef4481deb49ef24f44353401608946b1b04f7aa3eb040",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-05-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 666,
  "current_source_sequence_sha256": "b55974f94d7023b0272ef4481deb49ef24f44353401608946b1b04f7aa3eb040",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A8I6ASZ5",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef",
  "selected_historical_source_sequence_length": 666,
  "selected_historical_source_sequence_sha256": "b55974f94d7023b0272ef4481deb49ef24f44353401608946b1b04f7aa3eb040",
  "selected_historical_version": {
    "accession": "A0A8I6ASZ5",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TCF25_RAT",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A8I6ASZ5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:51.287559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-05-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:51.287559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002494\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:51.287559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BQ70\",\"source\":\"UniProtKB\"}],\"value\":\"Nuclear localized protein 1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"1309054\",\"source\":\"RGD\"}],\"value\":\"Transcription factor 25\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"TCF-25\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ribosome quality control complex subunit TCF25\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:51.287559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32805187\",\"source\":\"PubMed\"}],\"value\":\"Mainly nuclear\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32805187\",\"source\":\"PubMed\"}],\"id\":\"SL-0191\",\"value\":\"Nucleus\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BQ70\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0091\",\"value\":\"Cytoplasm, cytosol\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:51.287559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005829\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosol\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "retrieved_utc": "2026-11-01T06:24:51.287559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32805187\",\"source\":\"PubMed\"}],\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "retrieved_utc": "2026-11-01T06:24:51.287559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:1990112\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:RQC complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:RGD\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-01T06:24:51.287559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang X.\",\"Lei F.\",\"Wang X.M.\",\"Deng K.Q.\",\"Ji Y.X.\",\"Zhang Y.\",\"Li H.\",\"Zhang X.D.\",\"Lu Z.\",\"Zhang P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32805187\"},{\"database\":\"DOI\",\"id\":\"10.1161/jaha.120.016419\"}],\"citationType\":\"journal article\",\"firstPage\":\"e016419\",\"id\":\"32805187\",\"journal\":\"J. Am. Heart Assoc.\",\"lastPage\":\"e016419\",\"publicationDate\":\"2020\",\"title\":\"NULP1 Alleviates Cardiac Hypertrophy by Suppressing NFAT3 Transcriptional Activity.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH NFATC4\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:51.287559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   TCF25_RAT               Reviewed;         666 AA.\nAC   A0A8I6ASZ5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-MAY-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Ribosome quality control complex subunit TCF25 {ECO:0000305};\nDE   AltName: Full=Nuclear localized protein 1 {ECO:0000250|UniProtKB:Q9BQ70};\nDE   AltName: Full=Transcription factor 25 {ECO:0000312|RGD:1309054};\nDE            Short=TCF-25 {ECO:0000305};\nGN   Name=Tcf25 {ECO:0000312|RGD:1309054};\nGN   Synonyms=Nulp1 {ECO:0000303|PubMed:32805187};\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116 {ECO:0000312|Proteomes:UP000002494};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.894954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef",
  "url": "https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH NFATC4, AND SUBCELLULAR LOCATION.\nRX   PubMed=32805187; DOI=10.1161/jaha.120.016419;\nRA   Zhang X., Lei F., Wang X.M., Deng K.Q., Ji Y.X., Zhang Y., Li H.,\nRA   Zhang X.D., Lu Z., Zhang P.;\nRT   \"NULP1 Alleviates Cardiac Hypertrophy by Suppressing NFAT3 Transcriptional\nRT   Activity.\";\nRL   J. Am. Heart Assoc. 9:e016419-e016419(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.894954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef",
  "url": "https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:32805187}. Cytoplasm,\nCC       cytosol {ECO:0000250|UniProtKB:Q9BQ70}. Note=Mainly nuclear.\nCC       {ECO:0000269|PubMed:32805187}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.894954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef",
  "url": "https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005829; C:cytosol; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.894954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef",
  "url": "https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.894954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef",
  "url": "https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:1990112; C:RQC complex; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.894954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef",
  "url": "https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005811\nname: lipid droplet\nnamespace: cellular_component\ndef: \"An intracellular non-membrane-bounded organelle comprising a matrix of coalesced lipids surrounded by a phospholipid monolayer. May include associated proteins.\" [GOC:mah, GOC:tb]\ncomment: Note that this term does not refer to vesicles, but instead to structures in which lipids do not necessarily form bilayers.\nsubset: goslim_chembl\nsubset: goslim_generic\nsynonym: \"adiposome\" EXACT []\nsynonym: \"lipid body\" EXACT []\nsynonym: \"lipid particle\" EXACT []\nis_a: GO:0043232 ! intracellular membraneless organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005811",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59777-59789",
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
  "excerpt": "[Term]\nid: GO:0043190\nname: ATP-binding cassette (ABC) transporter complex\nnamespace: cellular_component\nalt_id: GO:0043191\nalt_id: GO:0043192\ndef: \"A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter.\" [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"ABC-type efflux permease complex\" NARROW []\nsynonym: \"ABC-type efflux porter complex\" NARROW []\nsynonym: \"ABC-type uptake permease complex\" NARROW []\nsynonym: \"mating pheromone exporter\" NARROW []\nis_a: GO:0098533 ! ATPase dependent transmembrane transport complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043190",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 244782-244797",
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
  "excerpt": "[Term]\nid: GO:0044218\nname: other organism cell membrane\nnamespace: cellular_component\nalt_id: GO:0044279\ndef: \"The cell membrane of a secondary organism with which the first organism is interacting.\" [GOC:jl]\nsynonym: \"foreign membrane\" RELATED []\nsynonym: \"other organism membrane\" BROAD []\nis_a: GO:0044217 ! other organism part\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044218",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 255298-255307",
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
  "excerpt": "[Term]\nid: GO:1990112\nname: RQC complex\nnamespace: cellular_component\ndef: \"A multiprotein complex that forms a stable complex with large ribosomal subunits (60S in eukaryotes and 50S in prokaryotes) containing stalled polypeptides and triggers their degradation (ribosomal quality control). In budding yeast, this complex includes Cdc48p, Rkr1p, Tae2p, Rqc1p, Npl4p and Ufd1p proteins.\" [GOC:rb, PMID:23178123, PMID:23232563]\nsynonym: \"ribosome quality control complex\" EXACT [PMID:23178123, PMID:23232563]\nsynonym: \"ribosome-bound quality control complex\" EXACT []\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990112",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 549333-549341",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 163. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
