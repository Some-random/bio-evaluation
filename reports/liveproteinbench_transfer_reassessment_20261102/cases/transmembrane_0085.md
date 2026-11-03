# transmembrane_0085: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0085.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **C** — 5..25

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | no saved label | no saved label | output error (invalid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MLFQDLSFPAAIGAVFGAVAISVAARCIYDLFFHPLRNFPGPKRAAIWSFYEFYYDVIRDGTYLWEIEKMHQKYGPIVRINSRSLHIHDPEYFNTIYAGSGRKVNKELSAVSGYTFPHSTISTLDHDLHRKRRAIVSPYFSKRAIAEIEPVIHERLNVLISRLAEAKGSIVDLTSAFSAYTADVVTYHFYGTHANYIGSKDFKYGLKDALTVLLNLYNLTRFLPVPANTLKNLPLPILGLINPNFPLVVSAREANKKMVLGYLNKPDEDKKAMKDARSKSVIVSALTDPNVPDAEKTLDRLLDEGETIIFAGIDTTARTLGVALFHLLNNKDVLMKLRKELQAVAKPDGQQWTTTELEAVPYMRGVVQEAIRLAYGLVVRIPRISPHEALRYNGFVIPPGTPVSQSTYLVNNDPSVFPNPQVFDPERWVKAAQDGVSLDKYMVSFSKGSRGCLGINLAYAKLYLGIARVATSLDMELFETTAKAISVYHTRGFAFPKEGDGAVKARVMGLCK

[Multiple Choices]
A. 7..27
B. 10..23
C. 5..25
D. 5..25; 508..529
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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence has a UniProt transmembrane annotation at 5..25, agreeing with choice C. The annotation is computational (ECO:0000255), so it supports the predicted region but is not experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminus contains a strongly hydrophobic stretch around residues 10–25, which supports a membrane-spanning helix in that region.


**Missing item-specific fact**

> The exact annotated boundaries 5..25 are not uniquely derivable from the sequence; choosing those endpoints over other overlapping boundaries requires a protein-specific prediction or annotation.


**Reason**

> Sequence composition gives a meaningful basis to predict a transmembrane helix, but does not robustly distinguish the keyed boundaries from the other choices that overlap its hydrophobic core.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "C"
]
```

> All three options overlap the same N-terminal hydrophobic stretch and could describe a segment spanning the membrane; the prompt does not specify a boundary convention that selects 5..25.


### Important caveats

- The supporting annotation is computational, not evidence of an experimentally measured membrane-spanning boundary.
- Choice D adds a second proposed segment, which is not supported by the cited annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains a strongly hydrophobic stretch around residues 10–25, which supports a membrane-spanning helix in that region.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated boundaries 5..25 are not uniquely derivable from the sequence; choosing those endpoints over other overlapping boundaries requires a protein-specific prediction or annotation.",
    "reason": "Sequence composition gives a meaningful basis to predict a transmembrane helix, but does not robustly distinguish the keyed boundaries from the other choices that overlap its hydrophobic core."
  },
  "case_id": "transmembrane_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt transmembrane annotation at 5..25, agreeing with choice C. The annotation is computational (ECO:0000255), so it supports the predicted region but is not experimental confirmation."
  },
  "important_caveats": [
    "The supporting annotation is computational, not evidence of an experimentally measured membrane-spanning boundary.",
    "Choice D adds a second proposed segment, which is not supported by the cited annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "C"
    ],
    "reason": "All three options overlap the same N-terminal hydrophobic stretch and could describe a segment spanning the membrane; the prompt does not specify a boundary convention that selects 5..25."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt transmembrane annotation at 5..25, agreeing with choice C. The annotation is computational (ECO:0000255), so it supports the predicted region but is not experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminus contains a strongly hydrophobic stretch around residues 10–25, which supports a membrane-spanning helix in that region.",
    "missing_item_specific_fact": "The exact annotated boundaries 5..25 are not uniquely derivable from the sequence; choosing those endpoints over other overlapping boundaries requires a protein-specific prediction or annotation.",
    "reason": "Sequence composition gives a meaningful basis to predict a transmembrane helix, but does not robustly distinguish the keyed boundaries from the other choices that overlap its hydrophobic core."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "C"],
    "reason": "All three options overlap the same N-terminal hydrophobic stretch and could describe a segment spanning the membrane; the prompt does not specify a boundary convention that selects 5..25."
  },
  "important_caveats": [
    "The supporting annotation is computational, not evidence of an experimentally measured membrane-spanning boundary.",
    "Choice D adds a second proposed segment, which is not supported by the cited annotation."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry Q0CPG7 (Cytochrome P450 monooxygenase astB, Aspergillus terreus) annotates a single transmembrane helical region at positions 5..25 (evidence C5, H3). The annotation is present in both the current (v86) and historical (v84) entries with sequence match confirmed. The evidence code is ECO:0000255 (inferred by similarity), indicating computational/transfer annotation rather than experimental determination, but the annotation is consistent and directly supports choice C.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options B (10..23, 14 residues) and D (includes 508..529, extending beyond the 512-residue protein) are eliminable by general biological knowledge: 14 residues is too short for a transmembrane α-helix (typically 18–25 residues), and a region extending past the C-terminus is physically impossible. Between A (7..27) and C (5..25), both are 21-residue stretches, but option A includes Arg(26) and Cys(27) within its range. Arginine's guanidinium group is extremely unfavorable in the hydrophobic membrane interior, making its inclusion within a TM helix boundary biologically implausible. Option C ends at Ala(25), a hydrophobic residue, and while it includes Asp(5) at the N-terminal edge, a single polar residue at the helix terminus (near the membrane-water interface) is more tolerable than a strongly charged Arg embedded within the helix. Additionally, P450 enzymes characteristically have an N-terminal TM anchor of ~20–25 residues, consistent with C.


**Missing item-specific fact**

> The exact boundary precision (5 vs. 7 start, 25 vs. 27 end) is algorithm-dependent; the UniProt annotation uses ECO:0000255 (similarity-based inference), not experimental determination. A hydropathy plot tool might place boundaries at slightly different positions.


**Reason**

> The elimination of B and D relies on clear general principles (helix length, protein length). The A-vs-C distinction rests on the well-established biological principle that strongly charged residues (especially Arg) are highly unfavorable within the TM helix core, while a single Asp at the helix edge near the membrane interface is more tolerable. This provides a defensible general-knowledge argument, though the exact boundary is somewhat algorithm-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is eliminable (too short), D is eliminable (extends beyond protein). Between A and C, the inclusion of Arg(26) in A provides a clear biological disqualifier. While the exact boundary (5 vs 7) is not perfectly sharp, the presence of a strongly charged residue within the TM span of A makes C the more defensible choice. No other option is equally defensible.


### Important caveats

- The UniProt TM annotation carries evidence code ECO:0000255 (similarity-based inference), not experimental validation. The 'ground truth' boundary is itself a computational prediction.
- The distinction between starting at position 5 (D) vs. 7 (S) is subtle; both include one polar/charged residue at the helix edge. The stronger argument is the exclusion of Arg(26) in option C.
- The protein is a fungal P450 with a well-known N-terminal membrane anchor; the general location is predictable from protein family knowledge, but exact boundaries vary by prediction tool.
- Option D's second region (508..529) extends 17 residues beyond the 512-residue protein, making it trivially eliminable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (10..23, 14 residues) and D (includes 508..529, extending beyond the 512-residue protein) are eliminable by general biological knowledge: 14 residues is too short for a transmembrane α-helix (typically 18–25 residues), and a region extending past the C-terminus is physically impossible. Between A (7..27) and C (5..25), both are 21-residue stretches, but option A includes Arg(26) and Cys(27) within its range. Arginine's guanidinium group is extremely unfavorable in the hydrophobic membrane interior, making its inclusion within a TM helix boundary biologically implausible. Option C ends at Ala(25), a hydrophobic residue, and while it includes Asp(5) at the N-terminal edge, a single polar residue at the helix terminus (near the membrane-water interface) is more tolerable than a strongly charged Arg embedded within the helix. Additionally, P450 enzymes characteristically have an N-terminal TM anchor of ~20–25 residues, consistent with C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary precision (5 vs. 7 start, 25 vs. 27 end) is algorithm-dependent; the UniProt annotation uses ECO:0000255 (similarity-based inference), not experimental determination. A hydropathy plot tool might place boundaries at slightly different positions.",
    "reason": "The elimination of B and D relies on clear general principles (helix length, protein length). The A-vs-C distinction rests on the well-established biological principle that strongly charged residues (especially Arg) are highly unfavorable within the TM helix core, while a single Asp at the helix edge near the membrane interface is more tolerable. This provides a defensible general-knowledge argument, though the exact boundary is somewhat algorithm-dependent."
  },
  "case_id": "transmembrane_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry Q0CPG7 (Cytochrome P450 monooxygenase astB, Aspergillus terreus) annotates a single transmembrane helical region at positions 5..25 (evidence C5, H3). The annotation is present in both the current (v86) and historical (v84) entries with sequence match confirmed. The evidence code is ECO:0000255 (inferred by similarity), indicating computational/transfer annotation rather than experimental determination, but the annotation is consistent and directly supports choice C."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (similarity-based inference), not experimental validation. The 'ground truth' boundary is itself a computational prediction.",
    "The distinction between starting at position 5 (D) vs. 7 (S) is subtle; both include one polar/charged residue at the helix edge. The stronger argument is the exclusion of Arg(26) in option C.",
    "The protein is a fungal P450 with a well-known N-terminal membrane anchor; the general location is predictable from protein family knowledge, but exact boundaries vary by prediction tool.",
    "Option D's second region (508..529) extends 17 residues beyond the 512-residue protein, making it trivially eliminable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is eliminable (too short), D is eliminable (extends beyond protein). Between A and C, the inclusion of Arg(26) in A provides a clear biological disqualifier. While the exact boundary (5 vs 7) is not perfectly sharp, the presence of a strongly charged residue within the TM span of A makes C the more defensible choice. No other option is equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry Q0CPG7 (Cytochrome P450 monooxygenase astB, Aspergillus terreus) annotates a single transmembrane helical region at positions 5..25 (evidence C5, H3). The annotation is present in both the current (v86) and historical (v84) entries with sequence match confirmed. The evidence code is ECO:0000255 (inferred by similarity), indicating computational/transfer annotation rather than experimental determination, but the annotation is consistent and directly supports choice C.",
    "evidence_ids": ["C5", "H3", "C1", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options B (10..23, 14 residues) and D (includes 508..529, extending beyond the 512-residue protein) are eliminable by general biological knowledge: 14 residues is too short for a transmembrane α-helix (typically 18–25 residues), and a region extending past the C-terminus is physically impossible. Between A (7..27) and C (5..25), both are 21-residue stretches, but option A includes Arg(26) and Cys(27) within its range. Arginine's guanidinium group is extremely unfavorable in the hydrophobic membrane interior, making its inclusion within a TM helix boundary biologically implausible. Option C ends at Ala(25), a hydrophobic residue, and while it includes Asp(5) at the N-terminal edge, a single polar residue at the helix terminus (near the membrane-water interface) is more tolerable than a strongly charged Arg embedded within the helix. Additionally, P450 enzymes characteristically have an N-terminal TM anchor of ~20–25 residues, consistent with C.",
    "missing_item_specific_fact": "The exact boundary precision (5 vs. 7 start, 25 vs. 27 end) is algorithm-dependent; the UniProt annotation uses ECO:0000255 (similarity-based inference), not experimental determination. A hydropathy plot tool might place boundaries at slightly different positions.",
    "reason": "The elimination of B and D relies on clear general principles (helix length, protein length). The A-vs-C distinction rests on the well-established biological principle that strongly charged residues (especially Arg) are highly unfavorable within the TM helix core, while a single Asp at the helix edge near the membrane interface is more tolerable. This provides a defensible general-knowledge argument, though the exact boundary is somewhat algorithm-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is eliminable (too short), D is eliminable (extends beyond protein). Between A and C, the inclusion of Arg(26) in A provides a clear biological disqualifier. While the exact boundary (5 vs 7) is not perfectly sharp, the presence of a strongly charged residue within the TM span of A makes C the more defensible choice. No other option is equally defensible."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (similarity-based inference), not experimental validation. The 'ground truth' boundary is itself a computational prediction.",
    "The distinction between starting at position 5 (D) vs. 7 (S) is subtle; both include one polar/charged residue at the helix edge. The stronger argument is the exclusion of Arg(26) in option C.",
    "The protein is a fungal P450 with a well-known N-terminal membrane anchor; the general location is predictable from protein family knowledge, but exact boundaries vary by prediction tool.",
    "Option D's second region (508..529) extends 17 residues beyond the 512-residue protein, making it trivially eliminable."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched archived UniProt record annotates residues 5–25 as a helical transmembrane region, supporting choice C. The annotation carries computational evidence code ECO:0000255, so it supports the predicted region but is not experimental confirmation.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal sequence contains a strongly hydrophobic stretch, especially around residues 10–25, making an N-terminal membrane-spanning helix a credible transferable inference and arguing against the additional distant segment in D. But that feature does not establish whether the span should be reported as 5–25 or 7–27; both include essentially the same hydrophobic stretch.


**Missing item-specific fact**

> The exact predicted boundary convention or residue endpoints for this sequence are needed to distinguish choice C from the similarly plausible choice A.


**Reason**

> General sequence and membrane-helix knowledge supports the location of a likely N-terminal transmembrane segment, but does not meaningfully resolve the small endpoint differences among the plausible single-segment choices. Matching the keyed coordinates therefore depends on a target-specific boundary annotation or prediction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both ranges encompass the same N-terminal hydrophobic segment and could reasonably describe its transmembrane extent; the wording provides no boundary convention that distinguishes them.


### Important caveats

- The hydrophobic segment supports a predicted transmembrane helix, but sequence evidence alone does not establish experimentally measured membrane boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence contains a strongly hydrophobic stretch, especially around residues 10–25, making an N-terminal membrane-spanning helix a credible transferable inference and arguing against the additional distant segment in D. But that feature does not establish whether the span should be reported as 5–25 or 7–27; both include essentially the same hydrophobic stretch.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact predicted boundary convention or residue endpoints for this sequence are needed to distinguish choice C from the similarly plausible choice A.",
    "reason": "General sequence and membrane-helix knowledge supports the location of a likely N-terminal transmembrane segment, but does not meaningfully resolve the small endpoint differences among the plausible single-segment choices. Matching the keyed coordinates therefore depends on a target-specific boundary annotation or prediction."
  },
  "case_id": "transmembrane_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt record annotates residues 5–25 as a helical transmembrane region, supporting choice C. The annotation carries computational evidence code ECO:0000255, so it supports the predicted region but is not experimental confirmation."
  },
  "important_caveats": [
    "The hydrophobic segment supports a predicted transmembrane helix, but sequence evidence alone does not establish experimentally measured membrane boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both ranges encompass the same N-terminal hydrophobic segment and could reasonably describe its transmembrane extent; the wording provides no boundary convention that distinguishes them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt record annotates residues 5–25 as a helical transmembrane region, supporting choice C. The annotation carries computational evidence code ECO:0000255, so it supports the predicted region but is not experimental confirmation.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal sequence contains a strongly hydrophobic stretch, especially around residues 10–25, making an N-terminal membrane-spanning helix a credible transferable inference and arguing against the additional distant segment in D. But that feature does not establish whether the span should be reported as 5–25 or 7–27; both include essentially the same hydrophobic stretch.",
    "missing_item_specific_fact": "The exact predicted boundary convention or residue endpoints for this sequence are needed to distinguish choice C from the similarly plausible choice A.",
    "reason": "General sequence and membrane-helix knowledge supports the location of a likely N-terminal transmembrane segment, but does not meaningfully resolve the small endpoint differences among the plausible single-segment choices. Matching the keyed coordinates therefore depends on a target-specific boundary annotation or prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both ranges encompass the same N-terminal hydrophobic segment and could reasonably describe its transmembrane extent; the wording provides no boundary convention that distinguishes them."
  },
  "important_caveats": [
    "The hydrophobic segment supports a predicted transmembrane helix, but sequence evidence alone does not establish experimentally measured membrane boundaries."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

No visible final review text was saved. Internal model reasoning is not a substitute for a visible review and is not published. The final-content extraction failed because the saved final content was not text.

**Saved parsed visible review:** `null`.

**Exact saved visible final text:** empty string (`""`). No visible final is synthesized from private reasoning.

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q0CPG7",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "2c0bb03809de07e14ce59b3c4ee4bb0d2d933e55b39228675336ddae248b6fa1",
  "benchmark_sequence_length": 512,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc",
  "current_source_sequence_sha256": "2c0bb03809de07e14ce59b3c4ee4bb0d2d933e55b39228675336ddae248b6fa1",
  "current_source_sequence_length": 512,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 84,
  "selected_historical_version": {
    "accession": "Q0CPG7",
    "database": "Swiss-Prot",
    "entryVersion": 84,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTB_ASPTN",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "af10b808e0591f68545ada812b145c7d6e3f216b49d49121ac583c1305af66ce",
  "selected_historical_source_sequence_sha256": "2c0bb03809de07e14ce59b3c4ee4bb0d2d933e55b39228675336ddae248b6fa1",
  "selected_historical_source_sequence_length": 512,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 84,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG7.json",
  "source_sha256": "86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc",
  "retrieved_utc": "2026-11-02T04:30:23.383605+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q0CPG7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG7.json",
  "source_sha256": "86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc",
  "retrieved_utc": "2026-11-02T04:30:23.383605+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG7.json",
  "source_sha256": "86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc",
  "retrieved_utc": "2026-11-02T04:30:23.383605+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG7.json",
  "source_sha256": "86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc",
  "retrieved_utc": "2026-11-02T04:30:23.383605+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein B\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase astB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG7.json",
  "source_sha256": "86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc",
  "retrieved_utc": "2026-11-02T04:30:23.383605+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":25},\"start\":{\"modifier\":\"EXACT\",\"value\":5}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG7.json",
  "source_sha256": "86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc",
  "retrieved_utc": "2026-11-02T04:30:23.383605+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG7?format=txt&versions=84)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG7?format=txt&versions=84",
  "source_sha256": "af10b808e0591f68545ada812b145c7d6e3f216b49d49121ac583c1305af66ce",
  "retrieved_utc": "2026-11-02T04:30:28.173476+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   ASTB_ASPTN              Reviewed;         512 AA.\nAC   Q0CPG7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 84.\nDE   RecName: Full=Cytochrome P450 monooxygenase astB {ECO:0000303|PubMed:29995859};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein B {ECO:0000303|PubMed:29995859};\nGN   Name=astB {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04417;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG7?format=txt&versions=84)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG7?format=txt&versions=84",
  "source_sha256": "af10b808e0591f68545ada812b145c7d6e3f216b49d49121ac583c1305af66ce",
  "retrieved_utc": "2026-11-02T04:30:28.173476+00:00",
  "source_locator": "lines 27-34",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG7?format=txt&versions=84)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG7?format=txt&versions=84",
  "source_sha256": "af10b808e0591f68545ada812b145c7d6e3f216b49d49121ac583c1305af66ce",
  "retrieved_utc": "2026-11-02T04:30:28.173476+00:00",
  "source_locator": "lines 115-117",
  "excerpt": "FT   TRANSMEM        5..25\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 84,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
