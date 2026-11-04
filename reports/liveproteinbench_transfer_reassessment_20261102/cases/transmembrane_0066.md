# transmembrane_0066

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0066.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDTAPDHREPQEQGESRKWYEMTASEFYVYVVAFMCGVSMMMSVNAVFSAPAYIMTYYRYAMQDPEAVPLYTNFWNNVMTYYNLIGIVTSLIMEPLTLLSWFRRIPIKVRLLGGLVILIVEIIVLMVVPARGTSEAGAVATICCTGFIGGFGKSIFESTAYGMFGAFPSSFTSTMMGGVGMSGVLTSLLQIIVKAALPDSYEGVKKQSKIYYGLDVGIQGMTFVALILLRFNSFAQNYFGDLGAVKSKVDAGKLSAEALCHTDEHPTHDKEGRNSSSGKEVPALGEVQTAAAKSEGPDAVEESSWPHEVEGPTSNEILVATAIFSTLRRVKWMFVACAFNFLITLFLFPGIAVGMFPDSKWFSTIAVFIFNVFDVLGRFSPSLKLMWPRSYKQRWIIVAASFARVIFVPLLLLHSYHYIPGEAYGYVMEVIFGFSNGYVGSMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRERH

[Multiple Choices]
A. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 460..480
B. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
C. 27..47; 80..106; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
D. 157..177; 412..432; 448..468; 478..498; 516..536; 545..565; 789..809; 986..1006; 1013..1033; 1037..1057; 1080..1100; 1114..1134
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence-matched historical UniProt record annotates all eleven regions in choice B as transmembrane helices. These annotations support the key, but their ECO:0000255 evidence is computational rather than direct experimental validation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The input sequence contains numerous long, hydrophobic stretches characteristic of membrane-spanning helices in a multipass transporter. In particular, the strongly hydrophobic stretch around 427..447 supports including the segment that distinguishes B from A; the broader 80..106 interval in C includes less hydrophobic residues around the expected helix, making B the more plausible choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Hydropathy and the repeated-helix pattern provide a concrete transferable basis for distinguishing the choices, even though they cannot establish every boundary with experimental certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is comparably supported by the sequence pattern and offered intervals.


### Important caveats

- The reviewer-only annotations are computational and support, but do not experimentally prove, the precise boundaries.
- The annotation source sequence matches the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The input sequence contains numerous long, hydrophobic stretches characteristic of membrane-spanning helices in a multipass transporter. In particular, the strongly hydrophobic stretch around 427..447 supports including the segment that distinguishes B from A; the broader 80..106 interval in C includes less hydrophobic residues around the expected helix, making B the more plausible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Hydropathy and the repeated-helix pattern provide a concrete transferable basis for distinguishing the choices, even though they cannot establish every boundary with experimental certainty."
  },
  "case_id": "transmembrane_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all eleven regions in choice B as transmembrane helices. These annotations support the key, but their ECO:0000255 evidence is computational rather than direct experimental validation."
  },
  "important_caveats": [
    "The reviewer-only annotations are computational and support, but do not experimentally prove, the precise boundaries.",
    "The annotation source sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence pattern and offered intervals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all eleven regions in choice B as transmembrane helices. These annotations support the key, but their ECO:0000255 evidence is computational rather than direct experimental validation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The input sequence contains numerous long, hydrophobic stretches characteristic of membrane-spanning helices in a multipass transporter. In particular, the strongly hydrophobic stretch around 427..447 supports including the segment that distinguishes B from A; the broader 80..106 interval in C includes less hydrophobic residues around the expected helix, making B the more plausible choice.",
    "missing_item_specific_fact": "",
    "reason": "Hydropathy and the repeated-helix pattern provide a concrete transferable basis for distinguishing the choices, even though they cannot establish every boundary with experimental certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence pattern and offered intervals."
  },
  "important_caveats": [
    "The reviewer-only annotations are computational and support, but do not experimentally prove, the precise boundaries.",
    "The annotation source sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry O76269 (Leishmania donovani Nucleoside transporter 1.2, 491 AA, sequence matched) annotates exactly 11 transmembrane helices at positions 27..47, 82..102, 109..129, 136..156, 173..193, 209..229, 333..353, 361..381, 395..415, 427..447, 460..480, all with ECO:0000255 (automatic annotation). Choice B matches this annotation exactly. The annotation is computational (ECO:0000255), not experimentally derived, but it is the recorded database annotation and is consistent with the ENT family topology.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice D is immediately eliminated because its coordinates (up to 1134) exceed the 491-residue sequence length. The protein sequence exhibits a polytopic membrane transporter topology with multiple hydrophobic stretches, and the pattern is recognizable as belonging to the equilibrative nucleoside transporter (ENT/SLC29) family, which is well-established to have 11 transmembrane helices (confirmed by crystal structures of human ENT1/ENT2 and family-wide annotation). This eliminates Choice A, which lists only 10 TM segments and would leave a 45-residue gap between TM9 (395..415) and TM11 (460..480), inconsistent with the compact ENT fold. Between B and C, the standard alpha-helical TM segment in a lipid bilayer is approximately 20-22 residues; B's 82..102 (21 residues) fits this convention, while C's 80..106 (27 residues) extends into positions 103-104 containing two arginine residues (charged, incompatible with the hydrophobic membrane core) and position 106 (Pro, helix-breaking). The charged Arg residues at 103-104 are a clear boundary marker for the TM helix, favoring the 82..102 definition. Additionally, the 427..447 segment, while containing some polar residues, is consistent with the pore-lining TM helices observed in ENT crystal structures, and its inclusion maintains the regular inter-helix spacing (~12-13 residues) characteristic of the ENT topology.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate D by length, eliminate A using the well-known 11-TM topology of the ENT family (learned from human ENT1/ENT2 structures and family annotation), and distinguish B from C using standard TM helix length conventions (~21 residues) and the presence of charged Arg residues at positions 103-104 that mark the membrane-water interface. These are all transferable inferences from other ENT-family proteins and general membrane-protein biophysics.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B and C differ by only a few residues in one segment, the charged Arg residues at 103-104 and the Pro at 106 provide a clear biophysical argument for the 21-residue definition (82..102). The ENT family 11-TM topology cleanly separates B from A. D is eliminated by sequence length. No ambiguity remains among the offered choices.


### Important caveats

- All 11 TM annotations in UniProt carry evidence code ECO:0000255 (automatic annotation by similarity/analysis), not experimental determination.
- The UniProt entry is flagged as a 'Fragment', though the 491-residue sequence matches the benchmark input.
- The 427..447 segment contains several polar residues (E, S, N, S, P, Q) and is the most borderline of the 11 helices; its inclusion relies on ENT-family structural precedent rather than pure hydrophobicity.
- The reviewer-only evidence (accession, organism, annotation details) was not available to the evaluated model; the answerability assessment relies solely on what a model could infer from the sequence and general ENT-family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice D is immediately eliminated because its coordinates (up to 1134) exceed the 491-residue sequence length. The protein sequence exhibits a polytopic membrane transporter topology with multiple hydrophobic stretches, and the pattern is recognizable as belonging to the equilibrative nucleoside transporter (ENT/SLC29) family, which is well-established to have 11 transmembrane helices (confirmed by crystal structures of human ENT1/ENT2 and family-wide annotation). This eliminates Choice A, which lists only 10 TM segments and would leave a 45-residue gap between TM9 (395..415) and TM11 (460..480), inconsistent with the compact ENT fold. Between B and C, the standard alpha-helical TM segment in a lipid bilayer is approximately 20-22 residues; B's 82..102 (21 residues) fits this convention, while C's 80..106 (27 residues) extends into positions 103-104 containing two arginine residues (charged, incompatible with the hydrophobic membrane core) and position 106 (Pro, helix-breaking). The charged Arg residues at 103-104 are a clear boundary marker for the TM helix, favoring the 82..102 definition. Additionally, the 427..447 segment, while containing some polar residues, is consistent with the pore-lining TM helices observed in ENT crystal structures, and its inclusion maintains the regular inter-helix spacing (~12-13 residues) characteristic of the ENT topology.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate D by length, eliminate A using the well-known 11-TM topology of the ENT family (learned from human ENT1/ENT2 structures and family annotation), and distinguish B from C using standard TM helix length conventions (~21 residues) and the presence of charged Arg residues at positions 103-104 that mark the membrane-water interface. These are all transferable inferences from other ENT-family proteins and general membrane-protein biophysics."
  },
  "case_id": "transmembrane_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry O76269 (Leishmania donovani Nucleoside transporter 1.2, 491 AA, sequence matched) annotates exactly 11 transmembrane helices at positions 27..47, 82..102, 109..129, 136..156, 173..193, 209..229, 333..353, 361..381, 395..415, 427..447, 460..480, all with ECO:0000255 (automatic annotation). Choice B matches this annotation exactly. The annotation is computational (ECO:0000255), not experimentally derived, but it is the recorded database annotation and is consistent with the ENT family topology."
  },
  "important_caveats": [
    "All 11 TM annotations in UniProt carry evidence code ECO:0000255 (automatic annotation by similarity/analysis), not experimental determination.",
    "The UniProt entry is flagged as a 'Fragment', though the 491-residue sequence matches the benchmark input.",
    "The 427..447 segment contains several polar residues (E, S, N, S, P, Q) and is the most borderline of the 11 helices; its inclusion relies on ENT-family structural precedent rather than pure hydrophobicity.",
    "The reviewer-only evidence (accession, organism, annotation details) was not available to the evaluated model; the answerability assessment relies solely on what a model could infer from the sequence and general ENT-family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and C differ by only a few residues in one segment, the charged Arg residues at 103-104 and the Pro at 106 provide a clear biophysical argument for the 21-residue definition (82..102). The ENT family 11-TM topology cleanly separates B from A. D is eliminated by sequence length. No ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry O76269 (Leishmania donovani Nucleoside transporter 1.2, 491 AA, sequence matched) annotates exactly 11 transmembrane helices at positions 27..47, 82..102, 109..129, 136..156, 173..193, 209..229, 333..353, 361..381, 395..415, 427..447, 460..480, all with ECO:0000255 (automatic annotation). Choice B matches this annotation exactly. The annotation is computational (ECO:0000255), not experimentally derived, but it is the recorded database annotation and is consistent with the ENT family topology.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Choice D is immediately eliminated because its coordinates (up to 1134) exceed the 491-residue sequence length. The protein sequence exhibits a polytopic membrane transporter topology with multiple hydrophobic stretches, and the pattern is recognizable as belonging to the equilibrative nucleoside transporter (ENT/SLC29) family, which is well-established to have 11 transmembrane helices (confirmed by crystal structures of human ENT1/ENT2 and family-wide annotation). This eliminates Choice A, which lists only 10 TM segments and would leave a 45-residue gap between TM9 (395..415) and TM11 (460..480), inconsistent with the compact ENT fold. Between B and C, the standard alpha-helical TM segment in a lipid bilayer is approximately 20-22 residues; B's 82..102 (21 residues) fits this convention, while C's 80..106 (27 residues) extends into positions 103-104 containing two arginine residues (charged, incompatible with the hydrophobic membrane core) and position 106 (Pro, helix-breaking). The charged Arg residues at 103-104 are a clear boundary marker for the TM helix, favoring the 82..102 definition. Additionally, the 427..447 segment, while containing some polar residues, is consistent with the pore-lining TM helices observed in ENT crystal structures, and its inclusion maintains the regular inter-helix spacing (~12-13 residues) characteristic of the ENT topology.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate D by length, eliminate A using the well-known 11-TM topology of the ENT family (learned from human ENT1/ENT2 structures and family annotation), and distinguish B from C using standard TM helix length conventions (~21 residues) and the presence of charged Arg residues at positions 103-104 that mark the membrane-water interface. These are all transferable inferences from other ENT-family proteins and general membrane-protein biophysics."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and C differ by only a few residues in one segment, the charged Arg residues at 103-104 and the Pro at 106 provide a clear biophysical argument for the 21-residue definition (82..102). The ENT family 11-TM topology cleanly separates B from A. D is eliminated by sequence length. No ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "All 11 TM annotations in UniProt carry evidence code ECO:0000255 (automatic annotation by similarity/analysis), not experimental determination.",
    "The UniProt entry is flagged as a 'Fragment', though the 491-residue sequence matches the benchmark input.",
    "The 427..447 segment contains several polar residues (E, S, N, S, P, Q) and is the most borderline of the 11 helices; its inclusion relies on ENT-family structural precedent rather than pure hydrophobicity.",
    "The reviewer-only evidence (accession, organism, annotation details) was not available to the evaluated model; the answerability assessment relies solely on what a model could infer from the sequence and general ENT-family knowledge."
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
  "benchmark_sequence_length": 491,
  "benchmark_sequence_sha256": "192e356b57159ee69c6287591ae9b71d5c65f6e1d7fe21a8299687927176107d",
  "current_entry_audit": {
    "entryVersion": 69,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-11-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 491,
  "current_source_sequence_sha256": "192e356b57159ee69c6287591ae9b71d5c65f6e1d7fe21a8299687927176107d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O76269",
  "selected_historical_entry_version": 67,
  "selected_historical_record_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "selected_historical_source_sequence_length": 491,
  "selected_historical_source_sequence_sha256": "192e356b57159ee69c6287591ae9b71d5c65f6e1d7fe21a8299687927176107d",
  "selected_historical_version": {
    "accession": "O76269",
    "database": "Swiss-Prot",
    "entryVersion": 67,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NT12_LEIDO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O76269\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":69,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-11-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32315.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Leishmania\"],\"scientificName\":\"Leishmania donovani\",\"taxonId\":5661}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"value\":\"Equilibrative nucleoside transporter 1.2\"}}],\"flag\":\"Fragment\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 1.2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"value\":\"LdNT1.2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":47},\"start\":{\"modifier\":\"EXACT\",\"value\":27}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":102},\"start\":{\"modifier\":\"EXACT\",\"value\":82}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":129},\"start\":{\"modifier\":\"EXACT\",\"value\":109}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":136}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":173}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":229},\"start\":{\"modifier\":\"EXACT\",\"value\":209}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":333}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":381},\"start\":{\"modifier\":\"EXACT\",\"value\":361}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":415},\"start\":{\"modifier\":\"EXACT\",\"value\":395}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":447},\"start\":{\"modifier\":\"EXACT\",\"value\":427}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":480},\"start\":{\"modifier\":\"EXACT\",\"value\":460}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Vasudevan G.\",\"Carter N.S.\",\"Drew M.E.\",\"Beverley S.M.\",\"Sanchez M.A.\",\"Seyfang A.\",\"Ullman B.\",\"Landfear S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9707568\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.95.17.9873\"}],\"citationType\":\"journal article\",\"firstPage\":\"9873\",\"id\":\"9707568\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"9878\",\"publicationDate\":\"1998\",\"title\":\"Cloning of Leishmania nucleoside transporter genes by rescue of a transport-deficient mutant.\",\"volume\":\"95\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32315.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H1",
  "excerpt": "ID   NT12_LEIDO              Reviewed;         491 AA.\nAC   O76269;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-NOV-1998, sequence version 1.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Nucleoside transporter 1.2 {ECO:0000303|PubMed:9707568};\nDE            Short=LdNT1.2 {ECO:0000303|PubMed:9707568};\nDE   AltName: Full=Equilibrative nucleoside transporter 1.2 {ECO:0000303|Ref.2};\nDE   Flags: Fragment;\nGN   Name=NT1.2 {ECO:0000303|PubMed:9707568};\nGN   ORFNames=CGC20_30425 {ECO:0000312|EMBL:TPP53189.1},\nGN   LDHU3_15.1540 {ECO:0000312|EMBL:CAC5428820.1};\nOS   Leishmania donovani.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Leishmania.\nOX   NCBI_TaxID=5661 {ECO:0000312|EMBL:AAC32315.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAC32315.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, TRANSPORTER ACTIVITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=9707568; DOI=10.1073/pnas.95.17.9873;\nRA   Vasudevan G., Carter N.S., Drew M.E., Beverley S.M., Sanchez M.A.,\nRA   Seyfang A., Ullman B., Landfear S.M.;\nRT   \"Cloning of Leishmania nucleoside transporter genes by rescue of a\nRT   transport-deficient mutant.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 95:9873-9878(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        27..47\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        82..102\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        109..129\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        136..156\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        173..193\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        209..229\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        333..353\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        361..381\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        395..415\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        427..447\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "entry_version": 67,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        460..480\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 66. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
