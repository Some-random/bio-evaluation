# transmembrane_0001

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0001.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLKKLYFTVLSFIAIVGVISLYIRLSEGMKMSALTSYSSWGLWIVFYIYFIGLSAGSFLLSTMVYVFNMKQFERIGKLALFTAFFSLMAGLLFVLIDLGHPERFWHTLVYRQPNSILSWEIQFYLIYMLLIVAEIWFLMREEFAQRAQSTKGLTKLFNRTLTLGYKVPNSQQKLEFHREQSHKWMKILGIAGIPTAVGVHGGTGSLFGVVMAKEYWFSGLTPIIFLVSALVSGAALMLFLYSFFGGAKKNGDSLLKELGTLLTLFIGIDLLLMIAEFLIGLYNPIHHERMTFNEILFGDRWFIFWIGQIGMVIILPILLITISKGKRLLMGLAGLSVVLGIVCVRWILVIPAYVAPHFDGLDSAYNSSRLLYEYSPNLLEWSSSVGLIGIVILLFSITVQLVPVFNKQKEVHQTHGKPTPEIHIKA

[Multiple Choices]
A. 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 302..322; 330..350; 385..405
B. 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 326..352; 385..405
C. 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405
D. 27..47; 59..79; 109..129; 142..162; 168..188; 225..245
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

> The sequence-matched UniProt record annotates all ten intervals in choice C as helical transmembrane regions. These annotations carry computational evidence code ECO:0000255, so they support the key but should not be represented as direct experimental confirmation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated, roughly membrane-length hydrophobic stretches, a transferable hallmark of transmembrane alpha helices in multipass membrane proteins. Their locations support the shared intervals in the choices and the additional hydrophobic span at 261..281, favoring C over A and D. Around the final differing interval, C gives a 21-residue hydrophobic core at 330..350; B extends that interval to 326..352, including less hydrophobic flanking residues, making C the more plausible membrane-spanning segment.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides a meaningful hydropathy-based distinction among the offered sets. Exact boundaries can be uncertain from sequence alone, but the alternatives differ in ways that the hydrophobic cores and typical transmembrane-helix lengths help resolve.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although predicted helix boundaries are not absolute, the offered differences are meaningfully resolved here by the long hydrophobic span omitted by A and by the less hydrophobic flanks included in B.


### Important caveats

- The supporting database features are computationally evidenced annotations, not established here as experimental measurements.
- The exact residue boundaries are predictions and may be less certain than the identification of the hydrophobic membrane-spanning segments.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated, roughly membrane-length hydrophobic stretches, a transferable hallmark of transmembrane alpha helices in multipass membrane proteins. Their locations support the shared intervals in the choices and the additional hydrophobic span at 261..281, favoring C over A and D. Around the final differing interval, C gives a 21-residue hydrophobic core at 330..350; B extends that interval to 326..352, including less hydrophobic flanking residues, making C the more plausible membrane-spanning segment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful hydropathy-based distinction among the offered sets. Exact boundaries can be uncertain from sequence alone, but the alternatives differ in ways that the hydrophobic cores and typical transmembrane-helix lengths help resolve."
  },
  "case_id": "transmembrane_0001",
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
      "H12"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all ten intervals in choice C as helical transmembrane regions. These annotations carry computational evidence code ECO:0000255, so they support the key but should not be represented as direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting database features are computationally evidenced annotations, not established here as experimental measurements.",
    "The exact residue boundaries are predictions and may be less certain than the identification of the hydrophobic membrane-spanning segments."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although predicted helix boundaries are not absolute, the offered differences are meaningfully resolved here by the long hydrophobic span omitted by A and by the less hydrophobic flanks included in B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all ten intervals in choice C as helical transmembrane regions. These annotations carry computational evidence code ECO:0000255, so they support the key but should not be represented as direct experimental confirmation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated, roughly membrane-length hydrophobic stretches, a transferable hallmark of transmembrane alpha helices in multipass membrane proteins. Their locations support the shared intervals in the choices and the additional hydrophobic span at 261..281, favoring C over A and D. Around the final differing interval, C gives a 21-residue hydrophobic core at 330..350; B extends that interval to 326..352, including less hydrophobic flanking residues, making C the more plausible membrane-spanning segment.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful hydropathy-based distinction among the offered sets. Exact boundaries can be uncertain from sequence alone, but the alternatives differ in ways that the hydrophobic cores and typical transmembrane-helix lengths help resolve."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although predicted helix boundaries are not absolute, the offered differences are meaningfully resolved here by the long hydrophobic span omitted by A and by the less hydrophobic flanks included in B."
  },
  "important_caveats": [
    "The supporting database features are computationally evidenced annotations, not established here as experimental measurements.",
    "The exact residue boundaries are predictions and may be less certain than the identification of the hydrophobic membrane-spanning segments."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0A8X338 annotates exactly 10 transmembrane helical segments at positions 5..25, 40..60, 78..98, 119..139, 187..207, 223..243, 261..281, 302..322, 330..350, and 385..405, which matches Choice C precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination, but the annotation is consistent and complete.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A model can apply hydrophobicity scanning to the 426-residue sequence to identify approximately 10 hydrophobic stretches of ~20 residues, immediately eliminating D (only 6 segments at shifted positions). Comparing A vs C, the region around 261..281 (LLTLFIGIDLLLMIAEFLIGL) contains a clear hydrophobic stretch that a hydrophobicity scan would flag, eliminating A which omits it. Distinguishing B (326..352) from C (330..350): positions 326-327 are K and R (lysine and arginine), two consecutive charged residues at the start of a proposed TM helix, which is energetically unfavorable in the hydrophobic membrane core per well-established membrane protein biophysics. Additionally, position 351 is P (proline), a known helix breaker, making an endpoint at 352 (including P) less favorable than 350. Choice C's boundaries (330..350) avoid both the charged-residue start and the proline-containing end, consistent with general principles of TM helix boundary assignment learned from many membrane proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of D relies on counting hydrophobic stretches; elimination of A relies on identifying the 261..281 hydrophobic segment; and the B-vs-C distinction relies on general membrane biology principles (charged residues unfavorable at TM helix boundaries, proline as helix breaker) that are transferable knowledge from many other membrane proteins. No fact specific to this exact protein's experimental measurement is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While TM helix boundaries are inherently fuzzy (±3-5 residues), the specific differences between the offered choices are large enough to be resolved by standard hydrophobicity analysis and well-known biophysical constraints. The charged-residue and proline arguments provide a meaningful preference for C over B, and the missing segment in A is identifiable from sequence.


### Important caveats

- All UniProt TM annotations here use evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. Exact boundaries carry inherent uncertainty.
- The B-vs-C distinction (4-residue shift) is within the typical fuzziness of TM boundary prediction, though the charged-residue argument at 326-327 provides a principled preference.
- The annotations were added to this entry in 2025 (entry first public 2025-02-05); the author's source snapshot is unknown but the sequence matches across versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can apply hydrophobicity scanning to the 426-residue sequence to identify approximately 10 hydrophobic stretches of ~20 residues, immediately eliminating D (only 6 segments at shifted positions). Comparing A vs C, the region around 261..281 (LLTLFIGIDLLLMIAEFLIGL) contains a clear hydrophobic stretch that a hydrophobicity scan would flag, eliminating A which omits it. Distinguishing B (326..352) from C (330..350): positions 326-327 are K and R (lysine and arginine), two consecutive charged residues at the start of a proposed TM helix, which is energetically unfavorable in the hydrophobic membrane core per well-established membrane protein biophysics. Additionally, position 351 is P (proline), a known helix breaker, making an endpoint at 352 (including P) less favorable than 350. Choice C's boundaries (330..350) avoid both the charged-residue start and the proline-containing end, consistent with general principles of TM helix boundary assignment learned from many membrane proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of D relies on counting hydrophobic stretches; elimination of A relies on identifying the 261..281 hydrophobic segment; and the B-vs-C distinction relies on general membrane biology principles (charged residues unfavorable at TM helix boundaries, proline as helix breaker) that are transferable knowledge from many other membrane proteins. No fact specific to this exact protein's experimental measurement is required."
  },
  "case_id": "transmembrane_0001",
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
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0A8X338 annotates exactly 10 transmembrane helical segments at positions 5..25, 40..60, 78..98, 119..139, 187..207, 223..243, 261..281, 302..322, 330..350, and 385..405, which matches Choice C precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination, but the annotation is consistent and complete."
  },
  "important_caveats": [
    "All UniProt TM annotations here use evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. Exact boundaries carry inherent uncertainty.",
    "The B-vs-C distinction (4-residue shift) is within the typical fuzziness of TM boundary prediction, though the charged-residue argument at 326-327 provides a principled preference.",
    "The annotations were added to this entry in 2025 (entry first public 2025-02-05); the author's source snapshot is unknown but the sequence matches across versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While TM helix boundaries are inherently fuzzy (±3-5 residues), the specific differences between the offered choices are large enough to be resolved by standard hydrophobicity analysis and well-known biophysical constraints. The charged-residue and proline arguments provide a meaningful preference for C over B, and the missing segment in A is identifiable from sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0A8X338 annotates exactly 10 transmembrane helical segments at positions 5..25, 40..60, 78..98, 119..139, 187..207, 223..243, 261..281, 302..322, 330..350, and 385..405, which matches Choice C precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination, but the annotation is consistent and complete.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A model can apply hydrophobicity scanning to the 426-residue sequence to identify approximately 10 hydrophobic stretches of ~20 residues, immediately eliminating D (only 6 segments at shifted positions). Comparing A vs C, the region around 261..281 (LLTLFIGIDLLLMIAEFLIGL) contains a clear hydrophobic stretch that a hydrophobicity scan would flag, eliminating A which omits it. Distinguishing B (326..352) from C (330..350): positions 326-327 are K and R (lysine and arginine), two consecutive charged residues at the start of a proposed TM helix, which is energetically unfavorable in the hydrophobic membrane core per well-established membrane protein biophysics. Additionally, position 351 is P (proline), a known helix breaker, making an endpoint at 352 (including P) less favorable than 350. Choice C's boundaries (330..350) avoid both the charged-residue start and the proline-containing end, consistent with general principles of TM helix boundary assignment learned from many membrane proteins.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of D relies on counting hydrophobic stretches; elimination of A relies on identifying the 261..281 hydrophobic segment; and the B-vs-C distinction relies on general membrane biology principles (charged residues unfavorable at TM helix boundaries, proline as helix breaker) that are transferable knowledge from many other membrane proteins. No fact specific to this exact protein's experimental measurement is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While TM helix boundaries are inherently fuzzy (±3-5 residues), the specific differences between the offered choices are large enough to be resolved by standard hydrophobicity analysis and well-known biophysical constraints. The charged-residue and proline arguments provide a meaningful preference for C over B, and the missing segment in A is identifiable from sequence."
  },
  "important_caveats": [
    "All UniProt TM annotations here use evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. Exact boundaries carry inherent uncertainty.",
    "The B-vs-C distinction (4-residue shift) is within the typical fuzziness of TM boundary prediction, though the charged-residue argument at 326-327 provides a principled preference.",
    "The annotations were added to this entry in 2025 (entry first public 2025-02-05); the author's source snapshot is unknown but the sequence matches across versions."
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
  "benchmark_sequence_length": 426,
  "benchmark_sequence_sha256": "218a8fc8c9a5550707cff8e4e71529fa4d0cadfec3371e5a9738f79c411a7e67",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-03-04",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 426,
  "current_source_sequence_sha256": "218a8fc8c9a5550707cff8e4e71529fa4d0cadfec3371e5a9738f79c411a7e67",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0A8X338",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "selected_historical_source_sequence_length": 426,
  "selected_historical_source_sequence_sha256": "218a8fc8c9a5550707cff8e4e71529fa4d0cadfec3371e5a9738f79c411a7e67",
  "selected_historical_version": {
    "accession": "A0A0A8X338",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SRDC_MESS1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0A8X338\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-03-04\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Mesobacillus\"],\"scientificName\":\"Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431 / SF-1)\",\"taxonId\":1321606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Selenate reductase membrane anchor subunit\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21357486\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Selenate reductase subunit C\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":25},\"start\":{\"modifier\":\"EXACT\",\"value\":5}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":60},\"start\":{\"modifier\":\"EXACT\",\"value\":40}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":98},\"start\":{\"modifier\":\"EXACT\",\"value\":78}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":139},\"start\":{\"modifier\":\"EXACT\",\"value\":119}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":207},\"start\":{\"modifier\":\"EXACT\",\"value\":187}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":243},\"start\":{\"modifier\":\"EXACT\",\"value\":223}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":281},\"start\":{\"modifier\":\"EXACT\",\"value\":261}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":322},\"start\":{\"modifier\":\"EXACT\",\"value\":302}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":350},\"start\":{\"modifier\":\"EXACT\",\"value\":330}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":405},\"start\":{\"modifier\":\"EXACT\",\"value\":385}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"citation\":{\"authors\":[\"Kuroda M.\",\"Yamashita M.\",\"Miwa E.\",\"Imao K.\",\"Fujimoto N.\",\"Ono H.\",\"Nagano K.\",\"Sei K.\",\"Ike M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21357486\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.01197-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"2141\",\"id\":\"21357486\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"2148\",\"publicationDate\":\"2011\",\"title\":\"Molecular cloning and characterization of the srdBCA operon, encoding the respiratory selenate reductase complex, from the selenate-reducing bacterium Bacillus selenatarsenatis SF-1.\",\"volume\":\"193\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ83593.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 18680 / JCM 14380 / FERM P-15431 / SF-1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION AS A SELENATE REDUCTASE\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   SRDC_MESS1              Reviewed;         426 AA.\nAC   A0A0A8X338; E9RFD0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   04-MAR-2015, sequence version 1.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Selenate reductase subunit C {ECO:0000305};\nDE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};\nDE   AltName: Full=Selenate reductase membrane anchor subunit {ECO:0000305};\nGN   Name=srdC {ECO:0000303|PubMed:21357486};\nGN   ORFNames=SAMD00020551_1551 {ECO:0000312|EMBL:GAM13407.1};\nOS   Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431\nOS   / SF-1).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;\nOC   Mesobacillus.\nOX   NCBI_TaxID=1321606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAJ83593.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION AS A SELENATE REDUCTASE, AND\nRP   SUBUNIT.\nRC   STRAIN=DSM 18680 / JCM 14380 / FERM P-15431 / SF-1;\nRX   PubMed=21357486; DOI=10.1128/jb.01197-10;\nRA   Kuroda M., Yamashita M., Miwa E., Imao K., Fujimoto N., Ono H., Nagano K.,\nRA   Sei K., Ike M.;\nRT   \"Molecular cloning and characterization of the srdBCA operon, encoding the\nRT   respiratory selenate reductase complex, from the selenate-reducing\nRT   bacterium Bacillus selenatarsenatis SF-1.\";\nRL   J. Bacteriol. 193:2141-2148(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        5..25\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        40..60\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        78..98\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        119..139\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        187..207\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        223..243\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        261..281\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        302..322\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        330..350\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        385..405\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
