# catalytic_activity_0072

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0072.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSVSPQSTMARIPERRVRTLDFAQFRHGEPSGSRGFCRELVDCLSSVGFVKIRNHGISGQEIENVFVMSQLFFSLPQAAKGKAAHPPEANPHRGYSYVGQEKLSRVKDYEKGKREITDVYDIKHYPIDRDARQESYDQGAAVDNLYPNRWPDEQDIPGFRVLMETFYERCHEVHQDILRAIAIGFDLSPSFLTDLCCQNTSELRLNHYPSVHPSSLRKGAKRISEHTDFGTVTLLFQDSVGGLEIEDQNTPGTYFPVLSERKSDIIVNIGDCIQRWTNDKIHSTSHRVVLPEDTDALTKDRYSVAYFGKPSRSQLVGSLREFVKEGEKPKYNDISAWQYNQEKLVLTY

[Multiple Choices]
A. dopamine + S-adenosyl-L-methionine = N-methyl-dopamine + S-adenosyl-L-homocysteine + H(+)
B. L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2
C. beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)
D. 2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2 H2O
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

> The sequence-matched UniProt entry annotates this reaction as L-proline hydroxylation to trans-4-hydroxy-L-proline and cites experimental evidence (ECO:0000269, PubMed 38578094). This supports B, though the evidence here is a curated database annotation rather than an independent review of the experiment.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is compatible with a soluble Fe(II)/2-oxoglutarate oxygenase, including a plausible His/carboxylate metal-binding pattern. Transferable knowledge of this enzyme class predicts use of 2-oxoglutarate and O2 in an oxidation or hydroxylation reaction. Among the choices, B is the matching 2-oxoglutarate-dependent hydroxylation; A is a SAM-dependent methyl transfer, C is an ATP-dependent NAD-forming reaction, and D is indigoidine formation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level enzyme recognition and the reaction cofactors distinguish B from the offered alternatives without requiring recall of this exact protein's database entry. The sequence-based class inference does not by itself prove proline substrate specificity or the precise hydroxylation position, but those finer details are not needed to distinguish B from these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B among the offered choices matches the predicted Fe(II)/2-oxoglutarate oxygenase chemistry.


### Important caveats

- The source also annotates other proline hydroxylation reactions for this protein, but those alternatives are not among the choices.
- The sequence supports an enzyme-family inference more strongly than the exact substrate and product assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble Fe(II)/2-oxoglutarate oxygenase, including a plausible His/carboxylate metal-binding pattern. Transferable knowledge of this enzyme class predicts use of 2-oxoglutarate and O2 in an oxidation or hydroxylation reaction. Among the choices, B is the matching 2-oxoglutarate-dependent hydroxylation; A is a SAM-dependent methyl transfer, C is an ATP-dependent NAD-forming reaction, and D is indigoidine formation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level enzyme recognition and the reaction cofactors distinguish B from the offered alternatives without requiring recall of this exact protein's database entry. The sequence-based class inference does not by itself prove proline substrate specificity or the precise hydroxylation position, but those finer details are not needed to distinguish B from these choices."
  },
  "case_id": "catalytic_activity_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this reaction as L-proline hydroxylation to trans-4-hydroxy-L-proline and cites experimental evidence (ECO:0000269, PubMed 38578094). This supports B, though the evidence here is a curated database annotation rather than an independent review of the experiment."
  },
  "important_caveats": [
    "The source also annotates other proline hydroxylation reactions for this protein, but those alternatives are not among the choices.",
    "The sequence supports an enzyme-family inference more strongly than the exact substrate and product assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B among the offered choices matches the predicted Fe(II)/2-oxoglutarate oxygenase chemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this reaction as L-proline hydroxylation to trans-4-hydroxy-L-proline and cites experimental evidence (ECO:0000269, PubMed 38578094). This supports B, though the evidence here is a curated database annotation rather than an independent review of the experiment.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is compatible with a soluble Fe(II)/2-oxoglutarate oxygenase, including a plausible His/carboxylate metal-binding pattern. Transferable knowledge of this enzyme class predicts use of 2-oxoglutarate and O2 in an oxidation or hydroxylation reaction. Among the choices, B is the matching 2-oxoglutarate-dependent hydroxylation; A is a SAM-dependent methyl transfer, C is an ATP-dependent NAD-forming reaction, and D is indigoidine formation.",
    "missing_item_specific_fact": "",
    "reason": "Family-level enzyme recognition and the reaction cofactors distinguish B from the offered alternatives without requiring recall of this exact protein's database entry. The sequence-based class inference does not by itself prove proline substrate specificity or the precise hydroxylation position, but those finer details are not needed to distinguish B from these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B among the offered choices matches the predicted Fe(II)/2-oxoglutarate oxygenase chemistry."
  },
  "important_caveats": [
    "The source also annotates other proline hydroxylation reactions for this protein, but those alternatives are not among the choices.",
    "The sequence supports an enzyme-family inference more strongly than the exact substrate and product assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A455ZMR3 (PPZD_METMF) assigns EC 1.14.11.57 with the reaction 'L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2', supported by experimental evidence (ECO:0000269, PubMed:38578094). The benchmark sequence matches the source sequence exactly (SHA256 confirmed). The expected answer B reproduces this reaction verbatim. While the entry also lists trans-3-hydroxy-L-proline and cis-4-hydroxy-D-proline as secondary activities, the primary EC assignment (1.14.11.57, prolyl-4-hydroxylase) corresponds to option B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable HxD motif (His-Thr-Asp in the segment 'ISEHTDFGTVTLLF') followed by a downstream His (in 'IHSTSHRVV'), constituting the 2-His-1-carboxylate facial triad diagnostic of Fe(II)/2-oxoglutarate-dependent dioxygenases. This is a well-established, transferable sequence signature learned from hundreds of characterized 2OG oxygenases (e.g., prolyl hydroxylases, phyH, ALKBH, taurine dioxygenase). The 349-residue length and β-sheet-rich character are consistent with the jelly-roll fold of 2OG oxygenase domains. Among the four choices, only option B (prolyl hydroxylase, EC 1.14.11.57) is a 2OG oxygenase reaction requiring the HxD facial triad and 2-oxoglutarate co-substrate. Option A (methyltransferase) would show a Rossmann-like fold with SAM-binding motifs (e.g., VLDLGCGxL). Option C (NAD synthetase) has a completely different architecture. Option D (flavin-dependent oxidase) lacks the HxD triad and 2OG requirement. Thus, recognizing the HxD facial triad as a 2OG oxygenase hallmark meaningfully and uniquely selects B over the other three alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HxD facial triad motif is a canonical, widely taught sequence feature of 2OG-dependent dioxygenases, transferable from knowledge of many other family members. It is sufficient to distinguish option B (the only 2OG oxygenase reaction among the choices) from the methyltransferase, NAD synthetase, and flavin oxidase alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry lists three catalytic activities (trans-4-hydroxy-L-proline, trans-3-hydroxy-L-proline, cis-4-hydroxy-D-proline), only the trans-4-hydroxy-L-proline reaction (option B) appears among the choices. No other option is a 2OG oxygenase reaction, so there is no ambiguity in selecting B from the offered alternatives.


### Important caveats

- The HxD motif identification (H-T-D in 'ISEHTDFG') is a reasonable but not absolutely unambiguous sequence-level inference; some 2OG oxygenases use HxE or have slightly variant spacing. However, the overall pattern and context strongly support the 2OG oxygenase assignment.
- The UniProt entry was first publicly released in Feb 2025; the author's source snapshot date is unknown. If the benchmark was constructed before this annotation existed, the expected answer may have been derived from a different source or computational prediction.
- The entry also documents trans-3-hydroxy-L-proline and D-proline activities, but these are not offered as answer choices, so they do not create ambiguity among the given options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable HxD motif (His-Thr-Asp in the segment 'ISEHTDFGTVTLLF') followed by a downstream His (in 'IHSTSHRVV'), constituting the 2-His-1-carboxylate facial triad diagnostic of Fe(II)/2-oxoglutarate-dependent dioxygenases. This is a well-established, transferable sequence signature learned from hundreds of characterized 2OG oxygenases (e.g., prolyl hydroxylases, phyH, ALKBH, taurine dioxygenase). The 349-residue length and β-sheet-rich character are consistent with the jelly-roll fold of 2OG oxygenase domains. Among the four choices, only option B (prolyl hydroxylase, EC 1.14.11.57) is a 2OG oxygenase reaction requiring the HxD facial triad and 2-oxoglutarate co-substrate. Option A (methyltransferase) would show a Rossmann-like fold with SAM-binding motifs (e.g., VLDLGCGxL). Option C (NAD synthetase) has a completely different architecture. Option D (flavin-dependent oxidase) lacks the HxD triad and 2OG requirement. Thus, recognizing the HxD facial triad as a 2OG oxygenase hallmark meaningfully and uniquely selects B over the other three alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HxD facial triad motif is a canonical, widely taught sequence feature of 2OG-dependent dioxygenases, transferable from knowledge of many other family members. It is sufficient to distinguish option B (the only 2OG oxygenase reaction among the choices) from the methyltransferase, NAD synthetase, and flavin oxidase alternatives."
  },
  "case_id": "catalytic_activity_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZMR3 (PPZD_METMF) assigns EC 1.14.11.57 with the reaction 'L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2', supported by experimental evidence (ECO:0000269, PubMed:38578094). The benchmark sequence matches the source sequence exactly (SHA256 confirmed). The expected answer B reproduces this reaction verbatim. While the entry also lists trans-3-hydroxy-L-proline and cis-4-hydroxy-D-proline as secondary activities, the primary EC assignment (1.14.11.57, prolyl-4-hydroxylase) corresponds to option B."
  },
  "important_caveats": [
    "The HxD motif identification (H-T-D in 'ISEHTDFG') is a reasonable but not absolutely unambiguous sequence-level inference; some 2OG oxygenases use HxE or have slightly variant spacing. However, the overall pattern and context strongly support the 2OG oxygenase assignment.",
    "The UniProt entry was first publicly released in Feb 2025; the author's source snapshot date is unknown. If the benchmark was constructed before this annotation existed, the expected answer may have been derived from a different source or computational prediction.",
    "The entry also documents trans-3-hydroxy-L-proline and D-proline activities, but these are not offered as answer choices, so they do not create ambiguity among the given options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry lists three catalytic activities (trans-4-hydroxy-L-proline, trans-3-hydroxy-L-proline, cis-4-hydroxy-D-proline), only the trans-4-hydroxy-L-proline reaction (option B) appears among the choices. No other option is a 2OG oxygenase reaction, so there is no ambiguity in selecting B from the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZMR3 (PPZD_METMF) assigns EC 1.14.11.57 with the reaction 'L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2', supported by experimental evidence (ECO:0000269, PubMed:38578094). The benchmark sequence matches the source sequence exactly (SHA256 confirmed). The expected answer B reproduces this reaction verbatim. While the entry also lists trans-3-hydroxy-L-proline and cis-4-hydroxy-D-proline as secondary activities, the primary EC assignment (1.14.11.57, prolyl-4-hydroxylase) corresponds to option B.",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable HxD motif (His-Thr-Asp in the segment 'ISEHTDFGTVTLLF') followed by a downstream His (in 'IHSTSHRVV'), constituting the 2-His-1-carboxylate facial triad diagnostic of Fe(II)/2-oxoglutarate-dependent dioxygenases. This is a well-established, transferable sequence signature learned from hundreds of characterized 2OG oxygenases (e.g., prolyl hydroxylases, phyH, ALKBH, taurine dioxygenase). The 349-residue length and β-sheet-rich character are consistent with the jelly-roll fold of 2OG oxygenase domains. Among the four choices, only option B (prolyl hydroxylase, EC 1.14.11.57) is a 2OG oxygenase reaction requiring the HxD facial triad and 2-oxoglutarate co-substrate. Option A (methyltransferase) would show a Rossmann-like fold with SAM-binding motifs (e.g., VLDLGCGxL). Option C (NAD synthetase) has a completely different architecture. Option D (flavin-dependent oxidase) lacks the HxD triad and 2OG requirement. Thus, recognizing the HxD facial triad as a 2OG oxygenase hallmark meaningfully and uniquely selects B over the other three alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The HxD facial triad motif is a canonical, widely taught sequence feature of 2OG-dependent dioxygenases, transferable from knowledge of many other family members. It is sufficient to distinguish option B (the only 2OG oxygenase reaction among the choices) from the methyltransferase, NAD synthetase, and flavin oxidase alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry lists three catalytic activities (trans-4-hydroxy-L-proline, trans-3-hydroxy-L-proline, cis-4-hydroxy-D-proline), only the trans-4-hydroxy-L-proline reaction (option B) appears among the choices. No other option is a 2OG oxygenase reaction, so there is no ambiguity in selecting B from the offered alternatives."
  },
  "important_caveats": [
    "The HxD motif identification (H-T-D in 'ISEHTDFG') is a reasonable but not absolutely unambiguous sequence-level inference; some 2OG oxygenases use HxE or have slightly variant spacing. However, the overall pattern and context strongly support the 2OG oxygenase assignment.",
    "The UniProt entry was first publicly released in Feb 2025; the author's source snapshot date is unknown. If the benchmark was constructed before this annotation existed, the expected answer may have been derived from a different source or computational prediction.",
    "The entry also documents trans-3-hydroxy-L-proline and D-proline activities, but these are not offered as answer choices, so they do not create ambiguity among the given options."
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
  "benchmark_sequence_sha256": "c00401d878260e5a5c15ceaae3e9851159bc2fc996a8543018238eee1e7f810e",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 349,
  "current_source_sequence_sha256": "c00401d878260e5a5c15ceaae3e9851159bc2fc996a8543018238eee1e7f810e",
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
  "requested_accession": "A0A455ZMR3",
  "selected_historical_entry_version": 20,
  "selected_historical_record_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "selected_historical_source_sequence_length": 349,
  "selected_historical_source_sequence_sha256": "c00401d878260e5a5c15ceaae3e9851159bc2fc996a8543018238eee1e7f810e",
  "selected_historical_version": {
    "accession": "A0A455ZMR3",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PPZD_METMF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZMR3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein D\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"1.14.11.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"1.14.11.57\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"2-oxoglutarate-Fe(II) type oxidoreductase ppzD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:51509\"}}],\"reaction\":{\"ecNumber\":\"1.14.11.57\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"name\":\"L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:51508\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16810\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58375\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60039\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82160\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"name\":\"L-proline + 2-oxoglutarate + O2 = trans-3-hydroxy-L-proline + succinate + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82159\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16810\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57938\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60039\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:82164\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"name\":\"D-proline + 2-oxoglutarate + O2 = cis-4-hydroxy-D-proline + succinate + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82163\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16810\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57690\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57726\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Rothchild K.W.\",\"Hagar M.\",\"Berry D.\",\"Ryan K.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38578094\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.4c01419\"}],\"citationType\":\"journal article\",\"firstPage\":\"10263\",\"id\":\"38578094\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"10267\",\"publicationDate\":\"2024\",\"title\":\"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\",\"volume\":\"146\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:18.557115+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "598c1818172f7f30ea279f4fe101b5f4a0a099aae626d2185ce8aa32a90a0e60",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZMR3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H1",
  "excerpt": "ID   PPZD_METMF              Reviewed;         349 AA.\nAC   A0A455ZMR3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzD {ECO:0000303|PubMed:30452111};\nDE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};\nDE            EC=1.14.11.57 {ECO:0000269|PubMed:38578094};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein D {ECO:0000303|PubMed:30452111};\nGN   Name=ppzD;\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=2-oxoglutarate-Fe(II) type oxidoreductase ppzD {ECO:0000303|PubMed:30452111};\nDE            EC=1.14.11.- {ECO:0000269|PubMed:38578094};\nDE            EC=1.14.11.57 {ECO:0000269|PubMed:38578094};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein D {ECO:0000303|PubMed:30452111};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=38578094; DOI=10.1021/jacs.4c01419;\nRA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;\nRT   \"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ\nRT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\";\nRL   J. Am. Chem. Soc. 146:10263-10267(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline +\nCC         succinate + CO2; Xref=Rhea:RHEA:51508, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:16526, ChEBI:CHEBI:16810, ChEBI:CHEBI:30031,\nCC         ChEBI:CHEBI:58375, ChEBI:CHEBI:60039; EC=1.14.11.57;\nCC         Evidence={ECO:0000269|PubMed:38578094};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:51509;\nCC         Evidence={ECO:0000269|PubMed:38578094};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-proline + 2-oxoglutarate + O2 = trans-3-hydroxy-L-proline +\nCC         succinate + CO2; Xref=Rhea:RHEA:82159, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:16526, ChEBI:CHEBI:16810, ChEBI:CHEBI:30031,\nCC         ChEBI:CHEBI:57938, ChEBI:CHEBI:60039;\nCC         Evidence={ECO:0000269|PubMed:38578094};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82160;\nCC         Evidence={ECO:0000269|PubMed:38578094};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-proline + 2-oxoglutarate + O2 = cis-4-hydroxy-D-proline +\nCC         succinate + CO2; Xref=Rhea:RHEA:82163, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:16526, ChEBI:CHEBI:16810, ChEBI:CHEBI:30031,\nCC         ChEBI:CHEBI:57690, ChEBI:CHEBI:57726;\nCC         Evidence={ECO:0000269|PubMed:38578094};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:82164;\nCC         Evidence={ECO:0000269|PubMed:38578094};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:22.046089+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1bbc826a341c3dbaed93f443586405373a3f1335605f903bf72936633a33119d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZMR3?format=txt&versions=20"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
