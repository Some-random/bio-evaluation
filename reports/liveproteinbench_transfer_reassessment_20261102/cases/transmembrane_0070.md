# transmembrane_0070

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0070.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 58..78; 85..105; 150..170; 171..191; 198..218; 252..272

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTSPGTVESTTPVSGQLRTVLSAGERPARATAVSATLTHLWRAMMAFKHFPVQLIDIVLMPLIFLLMFTYLFGGAFADSTEEYLQFYLPGVTVQAVVMMTVYTGTSLNTDIHKGVFDRFRTLPFWQPATLAGSLLGDVLRYVVALATTVFLGLLLGFRADGGFLGVVGAMLVLIVFGFSVSWIFAALGVVASEPERVSGTSMIVLYPLLFMSNIFVMPETMPGWMQAIVDANPMSHAATASRELMHGTAGFWDVGLVLCVSAGLVAVFAPLTMRLYRNKNAH

[Multiple Choices]
A. 58..78; 150..170; 171..191; 198..218; 252..272
B. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377
C. 58..78; 85..105; 147..171; 171..191; 198..218; 252..272
D. 58..78; 85..105; 150..170; 171..191; 198..218; 252..272
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

> The sequence-matched UniProt record lists all six regions in choice D. The historical record also has those coordinates. The evidence code ECO:0000255 indicates computational support, not experimental confirmation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains several hydrophobic stretches, and transferable knowledge of multipass transporter permeases supports recognizing multiple membrane-spanning helices. That can favor the six-region choices over options with missing or implausible regions, but it does not reliably distinguish C from D: their only difference is the precise boundaries assigned to the same predicted helix.


**Missing item-specific fact**

> The exact predicted boundary coordinates for the helix represented as 150..170 in D versus 147..171 in C.


**Reason**

> General sequence and family-level knowledge supports the broad topology, but not the small boundary difference that determines which of the otherwise similar choices is keyed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both choices identify the same six putative membrane-spanning regions. Their differing coordinates for one helix are plausible boundary variations for a predicted transmembrane segment, and the question gives no criterion for preferring one set of endpoints.


### Important caveats

- The supporting annotation is computational; it does not establish experimentally measured membrane boundaries.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches, and transferable knowledge of multipass transporter permeases supports recognizing multiple membrane-spanning helices. That can favor the six-region choices over options with missing or implausible regions, but it does not reliably distinguish C from D: their only difference is the precise boundaries assigned to the same predicted helix.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact predicted boundary coordinates for the helix represented as 150..170 in D versus 147..171 in C.",
    "reason": "General sequence and family-level knowledge supports the broad topology, but not the small boundary difference that determines which of the otherwise similar choices is keyed."
  },
  "case_id": "transmembrane_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record lists all six regions in choice D. The historical record also has those coordinates. The evidence code ECO:0000255 indicates computational support, not experimental confirmation."
  },
  "important_caveats": [
    "The supporting annotation is computational; it does not establish experimentally measured membrane boundaries.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both choices identify the same six putative membrane-spanning regions. Their differing coordinates for one helix are plausible boundary variations for a predicted transmembrane segment, and the question gives no criterion for preferring one set of endpoints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record lists all six regions in choice D. The historical record also has those coordinates. The evidence code ECO:0000255 indicates computational support, not experimental confirmation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches, and transferable knowledge of multipass transporter permeases supports recognizing multiple membrane-spanning helices. That can favor the six-region choices over options with missing or implausible regions, but it does not reliably distinguish C from D: their only difference is the precise boundaries assigned to the same predicted helix.",
    "missing_item_specific_fact": "The exact predicted boundary coordinates for the helix represented as 150..170 in D versus 147..171 in C.",
    "reason": "General sequence and family-level knowledge supports the broad topology, but not the small boundary difference that determines which of the otherwise similar choices is keyed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both choices identify the same six putative membrane-spanning regions. Their differing coordinates for one helix are plausible boundary variations for a predicted transmembrane segment, and the question gives no criterion for preferring one set of endpoints."
  },
  "important_caveats": [
    "The supporting annotation is computational; it does not establish experimentally measured membrane boundaries.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU4 (Daunorubicin resistance ABC transporter permease protein DrrB1, Streptomyces coeruleorubidus) annotates exactly six transmembrane helices at 58..78, 85..105, 150..170, 171..191, 198..218, and 252..272, all with evidence code ECO:0000255 (by similarity). The benchmark sequence SHA256 matches the source. Option D lists precisely these six regions. The annotation is computational (by similarity), not experimentally validated, but it is the recorded annotation and it matches the expected answer exactly.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option B is trivially eliminated because it lists positions 327..347 and 357..377, which exceed the 283-residue protein length. Option A lists only five TM regions, omitting 85..105; ABC transporter permease subunits (ABC-B family, e.g., DrrB homologs such as P-gp, MDR1, and other bacterial ABC-B permeases) characteristically contain six TM helices in their transmembrane domain, so a model recognizing the ABC-permease fold from the sequence's hydrophobic pattern and overall length can rule out A. The remaining contest is D vs C, which differ only in the third TM boundary: C uses 147..171 while D uses 150..170. Residues 147-149 are A-T-T, which are small and relatively polar; standard TM-helix boundary conventions place the helix start at the first clearly hydrophobic residue (V150), not at the preceding polar ATT stretch. This is a general, transferable principle about TM helix boundary placement (avoiding polar residues at the membrane-water interface). The ending difference (G170 vs M171) is minor, but the start-boundary argument is sufficient to favor D. Thus, family-level topology (6 TM helices for ABC permeases) plus hydrophobic boundary conventions allow a knowledgeable model to select D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level knowledge that ABC transporter permeases have six TM helices eliminates A (five TMs) and B (wrong positions, out-of-range). The hydrophobicity of residues 147-149 (ATT, polar) versus V150 provides a transferable boundary-placement argument favoring D (start at 150) over C (start at 147). While the D-vs-C distinction is fine-grained, it rests on a well-established principle about TM helix boundaries and does not require recalling this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is eliminated by out-of-range positions. Option A is eliminated by the 6-TM ABC-permease family topology. The D-vs-C distinction, while subtle (3-residue shift), is resolved by the polar ATT residues at 147-149 being inappropriate for a TM helix start, favoring D's start at V150. No two options are equally defensible under standard TM prediction conventions.


### Important caveats

- All UniProt TM annotations here carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred by homology, not experimentally determined boundaries.
- The D-vs-C boundary difference (150..170 vs 147..171) is only 3 residues and is at the resolution limit of manual hydrophobicity inspection; a computational predictor (TMHMM, Phobius, DeepTMHMM) would be needed for high-confidence boundary assignment.
- The ABC-permease 6-TM topology is a strong family-level regularity but is not an absolute rule; some ABC permease variants deviate.
- The reviewer-only evidence confirmed sequence identity and annotation match, but this information was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B is trivially eliminated because it lists positions 327..347 and 357..377, which exceed the 283-residue protein length. Option A lists only five TM regions, omitting 85..105; ABC transporter permease subunits (ABC-B family, e.g., DrrB homologs such as P-gp, MDR1, and other bacterial ABC-B permeases) characteristically contain six TM helices in their transmembrane domain, so a model recognizing the ABC-permease fold from the sequence's hydrophobic pattern and overall length can rule out A. The remaining contest is D vs C, which differ only in the third TM boundary: C uses 147..171 while D uses 150..170. Residues 147-149 are A-T-T, which are small and relatively polar; standard TM-helix boundary conventions place the helix start at the first clearly hydrophobic residue (V150), not at the preceding polar ATT stretch. This is a general, transferable principle about TM helix boundary placement (avoiding polar residues at the membrane-water interface). The ending difference (G170 vs M171) is minor, but the start-boundary argument is sufficient to favor D. Thus, family-level topology (6 TM helices for ABC permeases) plus hydrophobic boundary conventions allow a knowledgeable model to select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level knowledge that ABC transporter permeases have six TM helices eliminates A (five TMs) and B (wrong positions, out-of-range). The hydrophobicity of residues 147-149 (ATT, polar) versus V150 provides a transferable boundary-placement argument favoring D (start at 150) over C (start at 147). While the D-vs-C distinction is fine-grained, it rests on a well-established principle about TM helix boundaries and does not require recalling this protein's specific annotation."
  },
  "case_id": "transmembrane_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU4 (Daunorubicin resistance ABC transporter permease protein DrrB1, Streptomyces coeruleorubidus) annotates exactly six transmembrane helices at 58..78, 85..105, 150..170, 171..191, 198..218, and 252..272, all with evidence code ECO:0000255 (by similarity). The benchmark sequence SHA256 matches the source. Option D lists precisely these six regions. The annotation is computational (by similarity), not experimentally validated, but it is the recorded annotation and it matches the expected answer exactly."
  },
  "important_caveats": [
    "All UniProt TM annotations here carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred by homology, not experimentally determined boundaries.",
    "The D-vs-C boundary difference (150..170 vs 147..171) is only 3 residues and is at the resolution limit of manual hydrophobicity inspection; a computational predictor (TMHMM, Phobius, DeepTMHMM) would be needed for high-confidence boundary assignment.",
    "The ABC-permease 6-TM topology is a strong family-level regularity but is not an absolute rule; some ABC permease variants deviate.",
    "The reviewer-only evidence confirmed sequence identity and annotation match, but this information was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is eliminated by out-of-range positions. Option A is eliminated by the 6-TM ABC-permease family topology. The D-vs-C distinction, while subtle (3-residue shift), is resolved by the polar ATT residues at 147-149 being inappropriate for a TM helix start, favoring D's start at V150. No two options are equally defensible under standard TM prediction conventions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU4 (Daunorubicin resistance ABC transporter permease protein DrrB1, Streptomyces coeruleorubidus) annotates exactly six transmembrane helices at 58..78, 85..105, 150..170, 171..191, 198..218, and 252..272, all with evidence code ECO:0000255 (by similarity). The benchmark sequence SHA256 matches the source. Option D lists precisely these six regions. The annotation is computational (by similarity), not experimentally validated, but it is the recorded annotation and it matches the expected answer exactly.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option B is trivially eliminated because it lists positions 327..347 and 357..377, which exceed the 283-residue protein length. Option A lists only five TM regions, omitting 85..105; ABC transporter permease subunits (ABC-B family, e.g., DrrB homologs such as P-gp, MDR1, and other bacterial ABC-B permeases) characteristically contain six TM helices in their transmembrane domain, so a model recognizing the ABC-permease fold from the sequence's hydrophobic pattern and overall length can rule out A. The remaining contest is D vs C, which differ only in the third TM boundary: C uses 147..171 while D uses 150..170. Residues 147-149 are A-T-T, which are small and relatively polar; standard TM-helix boundary conventions place the helix start at the first clearly hydrophobic residue (V150), not at the preceding polar ATT stretch. This is a general, transferable principle about TM helix boundary placement (avoiding polar residues at the membrane-water interface). The ending difference (G170 vs M171) is minor, but the start-boundary argument is sufficient to favor D. Thus, family-level topology (6 TM helices for ABC permeases) plus hydrophobic boundary conventions allow a knowledgeable model to select D.",
    "missing_item_specific_fact": "",
    "reason": "The family-level knowledge that ABC transporter permeases have six TM helices eliminates A (five TMs) and B (wrong positions, out-of-range). The hydrophobicity of residues 147-149 (ATT, polar) versus V150 provides a transferable boundary-placement argument favoring D (start at 150) over C (start at 147). While the D-vs-C distinction is fine-grained, it rests on a well-established principle about TM helix boundaries and does not require recalling this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is eliminated by out-of-range positions. Option A is eliminated by the 6-TM ABC-permease family topology. The D-vs-C distinction, while subtle (3-residue shift), is resolved by the polar ATT residues at 147-149 being inappropriate for a TM helix start, favoring D's start at V150. No two options are equally defensible under standard TM prediction conventions."
  },
  "important_caveats": [
    "All UniProt TM annotations here carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred by homology, not experimentally determined boundaries.",
    "The D-vs-C boundary difference (150..170 vs 147..171) is only 3 residues and is at the resolution limit of manual hydrophobicity inspection; a computational predictor (TMHMM, Phobius, DeepTMHMM) would be needed for high-confidence boundary assignment.",
    "The ABC-permease 6-TM topology is a strong family-level regularity but is not an absolute rule; some ABC permease variants deviate.",
    "The reviewer-only evidence confirmed sequence identity and annotation match, but this information was not available to the evaluated model."
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
  "benchmark_sequence_length": 283,
  "benchmark_sequence_sha256": "044fc3aafdd7290b8ba81d7a359f1000702344148420b3b5202673cb2206cc44",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 283,
  "current_source_sequence_sha256": "044fc3aafdd7290b8ba81d7a359f1000702344148420b3b5202673cb2206cc44",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXU4",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "selected_historical_source_sequence_length": 283,
  "selected_historical_source_sequence_sha256": "044fc3aafdd7290b8ba81d7a359f1000702344148420b3b5202673cb2206cc44",
  "selected_historical_version": {
    "accession": "P0DXU4",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRB1_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ABC transporter permease protein DrrB1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":78},\"start\":{\"modifier\":\"EXACT\",\"value\":58}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":105},\"start\":{\"modifier\":\"EXACT\",\"value\":85}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":170},\"start\":{\"modifier\":\"EXACT\",\"value\":150}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":191},\"start\":{\"modifier\":\"EXACT\",\"value\":171}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":218},\"start\":{\"modifier\":\"EXACT\",\"value\":198}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":272},\"start\":{\"modifier\":\"EXACT\",\"value\":252}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:29:38.291851+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRB1_STRC4             Reviewed;         283 AA.\nAC   P0DXU4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB1 {ECO:0000305};\nGN   Name=drrB1 {ECO:0000303|PubMed:39375957};\nGN   Synonyms=drrB {ECO:0000312|EMBL:WOT33551.1};\nGN   ORFNames=R5U08_05030 {ECO:0000312|EMBL:WOT33551.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        58..78\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        85..105\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        150..170\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        171..191\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        198..218\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        252..272\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.349229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f",
  "url": "https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
