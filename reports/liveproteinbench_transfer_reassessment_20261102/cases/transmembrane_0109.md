# transmembrane_0109: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0109.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **D** — 357..377; 397..419; 481..501; 506..526; 591..611; 619..639

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | no saved label | no saved label | output error (invalid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MRSFYNKCFTNKLISAHSLFCQHVSTLKNNKKECFEDVKRSNRISDEFYSSFLYHSYIENLKSTKEYVYFIYLQDIYYNINIFKNKGRLYISNNGLCNDKLKDNNNNNNINSNNFGNSYNAYTKKKSFYHSFNDLNEAKEIRKKRKNEKSEKNIVEYLLCNIINPNENYHIQNIYNHNLNNNVSIEIHKKNDSVMYHYNNEKKTKTSKMTTDIKLKQINNVYIKYVPYKNKIITLACPNKYYPTLYRYFSSHTNKKEDAEENDKNKNININNVDNRYKEDFMYGCENKNDSEKHKKTTNNNFGDEFEKLKVKELDKILNKLEMLYDNKNNKMNINVKILGYIFKNFLLKNKELKRKIFCSLFFLLCSKMAIIYTPILLSTFIENVNLQKSLSNNIDIYSTNKSSVLLLCAYVFSRVLSSTMNELRNSVFSNISQKISTFVSKLFFYKIHNLNLTYILSKKNGELSFIFNRGCKSITNLLNVMVFQIIPIIIEFILYLYILTYKIHYTVSLVTCFNMFLYVLFTTLITKRRTIIRKHMNKAEQNTFNIFLDSIQNVEQVKYYTNEIHELKKFIKEQKKYEKEAINVQKSLSFLNFGQQIILNTNLFLCMYLTYLNIANDIFPFSYLILVNTLLFQLAMPLNMFGTIYRETKLSLVDIESMIKILVKKIKSPDYGNQMLIKNGNIKFENVYFKYPLNEDINGLEQNYQAKEKDPNIINNINNINNINNINNINNINSINNIYTFESNVKNISSTNMITSSINKLKKWYLDKVKDNKKNVQYNNNDVKKTNPNITKNLNKEIKENINTHLKNHKIINNSPNYNNNNYLFQNFTCNIENGEKVAIIGKSGSGKSSLIKLLLKFYEVNSGNIYIDNKNIDDIDLYTLRKNISVVPQDTILFNNTISYNIKYGNFQCTDKQMIQASIKAELHDKIMKMENKYDTIVGERGTKLSIGEKQRICIARCFLKDSKIIVLDEHASNLDNENKKAIEKALTKLCMGKTTFIITHVMENLKHMDKIIFFCGKNIYVGSHKNLMDDNHFYREYYDSKNNKML

[Multiple Choices]
A. 357..377; 397..419; 481..501; 506..526; 619..639
B. 358..373; 397..419; 481..501; 506..526; 591..611; 619..639
C. 337..357
D. 357..377; 397..419; 481..501; 506..526; 591..611; 619..639
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

> The sequence matches the UniProt record, whose historical and current annotations list all six transmembrane regions in choice D. These are computational annotations based on PROSITE-ProRule, not experimental measurements.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has hydrophobic stretches consistent with multiple membrane-spanning helices, so their approximate locations can be inferred. That does not establish the exact annotated boundaries or uniquely resolve the narrower first interval in choice B.


**Missing item-specific fact**

> The protein-specific transmembrane-region annotations, particularly the exact boundaries and whether the 591..611 region is included.


**Reason**

> The sequence supports a multi-pass membrane-protein interpretation, but selecting the precise set of coordinate intervals depends on protein-specific annotation or prediction not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B"
]
```

> Choice B includes the same six candidate regions as D except that its first interval is narrower. Because membrane-helix boundaries are not intrinsically sharp, that interval could represent a predicted core, although D matches the cited annotation.


### Important caveats

- The supporting annotations are computational and do not establish experimental membrane-spanning boundaries.
- The annotation evidence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has hydrophobic stretches consistent with multiple membrane-spanning helices, so their approximate locations can be inferred. That does not establish the exact annotated boundaries or uniquely resolve the narrower first interval in choice B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotations, particularly the exact boundaries and whether the 591..611 region is included.",
    "reason": "The sequence supports a multi-pass membrane-protein interpretation, but selecting the precise set of coordinate intervals depends on protein-specific annotation or prediction not supplied in the question."
  },
  "case_id": "transmembrane_0109",
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
    "reason": "The sequence matches the UniProt record, whose historical and current annotations list all six transmembrane regions in choice D. These are computational annotations based on PROSITE-ProRule, not experimental measurements."
  },
  "important_caveats": [
    "The supporting annotations are computational and do not establish experimental membrane-spanning boundaries.",
    "The annotation evidence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B"
    ],
    "reason": "Choice B includes the same six candidate regions as D except that its first interval is narrower. Because membrane-helix boundaries are not intrinsically sharp, that interval could represent a predicted core, although D matches the cited annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, whose historical and current annotations list all six transmembrane regions in choice D. These are computational annotations based on PROSITE-ProRule, not experimental measurements.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has hydrophobic stretches consistent with multiple membrane-spanning helices, so their approximate locations can be inferred. That does not establish the exact annotated boundaries or uniquely resolve the narrower first interval in choice B.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotations, particularly the exact boundaries and whether the 591..611 region is included.",
    "reason": "The sequence supports a multi-pass membrane-protein interpretation, but selecting the precise set of coordinate intervals depends on protein-specific annotation or prediction not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B"],
    "reason": "Choice B includes the same six candidate regions as D except that its first interval is narrower. Because membrane-helix boundaries are not intrinsically sharp, that interval could represent a predicted core, although D matches the cited annotation."
  },
  "important_caveats": [
    "The supporting annotations are computational and do not establish experimental membrane-spanning boundaries.",
    "The annotation evidence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> All six transmembrane regions in Choice D (357..377; 397..419; 481..501; 506..526; 591..611; 619..639) exactly match the UniProt annotations for Q8IDH9 (PfATM1). The annotations are computationally predicted (ECO:0000255, PROSITE-ProRule PRU00441), not experimentally determined, but they are the canonical database annotation for this entry. The sequence in the question matches the UniProt sequence (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is an ABC transporter (ATM1/PfABCB6), whose transmembrane domain canonically contains six α-helical TM segments. This eliminates Choice C (a single TM region) and Choice A (only five TMs, missing 591..611). Between B and D, the first TM in B spans 358..373 (16 residues), which is below the ~20-residue minimum generally required for a hydrophobic α-helix to traverse the ~30 Å lipid-bilayer core, whereas D's 357..377 (21 residues) is consistent with a standard TM helix. These two arguments (6-TM ABC architecture and minimum helix length) provide concrete biological reasoning to select D.


**Missing item-specific fact**

> None strictly required. The precise single-residue boundaries (357 vs 358, 377 vs 373) fall within the inherent uncertainty of TM prediction algorithms, but the 16-vs-21-residue length difference is large enough for a general hydrophobicity-span argument to apply.


**Reason**

> General knowledge of ABC transporter topology (six TMs) and the biophysical requirement of ~20 hydrophobic residues per membrane-spanning helix provide defensible grounds to eliminate A, B, and C without recalling the specific UniProt entry. The remaining choice D is consistent with both constraints.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C is clearly wrong (single short TM for an ABC transporter). Choice A omits a TM region inconsistent with ABC transporter architecture. Choice B's 16-residue first TM is notably short for membrane spanning. Only D satisfies both the 6-TM requirement and the ~20-residue helix-length criterion.


### Important caveats

- The UniProt transmembrane annotations are computationally predicted (PROSITE-ProRule PRU00441), not experimentally validated by crystallography or cryo-EM.
- The exact single-residue boundaries of TM helices carry inherent uncertainty even among prediction tools; the question's distractors exploit this, but the 16-vs-21-residue gap in the B/D comparison is large enough to reason about.
- The protein is from Plasmodium falciparum (ATM1/PfABCB6), an ABC transporter involved in Fe-S cluster biogenesis; its 6-TM architecture is a family-level property, not an experimentally confirmed topology for this specific protein.
- The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning above relies on general biological knowledge accessible to a trained biologist.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is an ABC transporter (ATM1/PfABCB6), whose transmembrane domain canonically contains six α-helical TM segments. This eliminates Choice C (a single TM region) and Choice A (only five TMs, missing 591..611). Between B and D, the first TM in B spans 358..373 (16 residues), which is below the ~20-residue minimum generally required for a hydrophobic α-helix to traverse the ~30 Å lipid-bilayer core, whereas D's 357..377 (21 residues) is consistent with a standard TM helix. These two arguments (6-TM ABC architecture and minimum helix length) provide concrete biological reasoning to select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The precise single-residue boundaries (357 vs 358, 377 vs 373) fall within the inherent uncertainty of TM prediction algorithms, but the 16-vs-21-residue length difference is large enough for a general hydrophobicity-span argument to apply.",
    "reason": "General knowledge of ABC transporter topology (six TMs) and the biophysical requirement of ~20 hydrophobic residues per membrane-spanning helix provide defensible grounds to eliminate A, B, and C without recalling the specific UniProt entry. The remaining choice D is consistent with both constraints."
  },
  "case_id": "transmembrane_0109",
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
    "reason": "All six transmembrane regions in Choice D (357..377; 397..419; 481..501; 506..526; 591..611; 619..639) exactly match the UniProt annotations for Q8IDH9 (PfATM1). The annotations are computationally predicted (ECO:0000255, PROSITE-ProRule PRU00441), not experimentally determined, but they are the canonical database annotation for this entry. The sequence in the question matches the UniProt sequence (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations are computationally predicted (PROSITE-ProRule PRU00441), not experimentally validated by crystallography or cryo-EM.",
    "The exact single-residue boundaries of TM helices carry inherent uncertainty even among prediction tools; the question's distractors exploit this, but the 16-vs-21-residue gap in the B/D comparison is large enough to reason about.",
    "The protein is from Plasmodium falciparum (ATM1/PfABCB6), an ABC transporter involved in Fe-S cluster biogenesis; its 6-TM architecture is a family-level property, not an experimentally confirmed topology for this specific protein.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning above relies on general biological knowledge accessible to a trained biologist."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is clearly wrong (single short TM for an ABC transporter). Choice A omits a TM region inconsistent with ABC transporter architecture. Choice B's 16-residue first TM is notably short for membrane spanning. Only D satisfies both the 6-TM requirement and the ~20-residue helix-length criterion."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "All six transmembrane regions in Choice D (357..377; 397..419; 481..501; 506..526; 591..611; 619..639) exactly match the UniProt annotations for Q8IDH9 (PfATM1). The annotations are computationally predicted (ECO:0000255, PROSITE-ProRule PRU00441), not experimentally determined, but they are the canonical database annotation for this entry. The sequence in the question matches the UniProt sequence (SHA-256 confirmed).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is an ABC transporter (ATM1/PfABCB6), whose transmembrane domain canonically contains six α-helical TM segments. This eliminates Choice C (a single TM region) and Choice A (only five TMs, missing 591..611). Between B and D, the first TM in B spans 358..373 (16 residues), which is below the ~20-residue minimum generally required for a hydrophobic α-helix to traverse the ~30 Å lipid-bilayer core, whereas D's 357..377 (21 residues) is consistent with a standard TM helix. These two arguments (6-TM ABC architecture and minimum helix length) provide concrete biological reasoning to select D.",
    "missing_item_specific_fact": "None strictly required. The precise single-residue boundaries (357 vs 358, 377 vs 373) fall within the inherent uncertainty of TM prediction algorithms, but the 16-vs-21-residue length difference is large enough for a general hydrophobicity-span argument to apply.",
    "reason": "General knowledge of ABC transporter topology (six TMs) and the biophysical requirement of ~20 hydrophobic residues per membrane-spanning helix provide defensible grounds to eliminate A, B, and C without recalling the specific UniProt entry. The remaining choice D is consistent with both constraints."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is clearly wrong (single short TM for an ABC transporter). Choice A omits a TM region inconsistent with ABC transporter architecture. Choice B's 16-residue first TM is notably short for membrane spanning. Only D satisfies both the 6-TM requirement and the ~20-residue helix-length criterion."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations are computationally predicted (PROSITE-ProRule PRU00441), not experimentally validated by crystallography or cryo-EM.",
    "The exact single-residue boundaries of TM helices carry inherent uncertainty even among prediction tools; the question's distractors exploit this, but the 16-vs-21-residue gap in the B/D comparison is large enough to reason about.",
    "The protein is from Plasmodium falciparum (ATM1/PfABCB6), an ABC transporter involved in Fe-S cluster biogenesis; its 6-TM architecture is a family-level property, not an experimentally confirmed topology for this specific protein.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning above relies on general biological knowledge accessible to a trained biologist."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt records annotate all six regions in D as transmembrane helices. These annotations are computational, based on PROSITE-ProRule evidence, rather than direct experimental demonstrations of each boundary.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a hydrophobic membrane-domain region and a downstream ABC-transporter P-loop-like motif (…IGKSGSGKSS…). Transferable knowledge of ABC transporters supports a multi-helix membrane domain; among these choices, six candidate helices fit better than the five-region option A or the lone short region in C. The sequence and typical membrane-helix lengths also favor the full 357..377 span over B’s shorter 358..373 span.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level pattern and candidate hydrophobic spans provide a meaningful basis for choosing D without needing the target’s database record, though sequence-based boundary predictions are not exact and the inference is not experimental proof.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The boundaries of predicted helices can be uncertain, but the offered full-length spans and six-helix pattern make D the best-supported choice; the shorter first span in B is less plausible as a complete membrane crossing.


### Important caveats

- The supporting source annotations are computational PROSITE-ProRule annotations, not experimental measurements of the individual helix boundaries.
- The sequence matches the cited historical entry, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a hydrophobic membrane-domain region and a downstream ABC-transporter P-loop-like motif (…IGKSGSGKSS…). Transferable knowledge of ABC transporters supports a multi-helix membrane domain; among these choices, six candidate helices fit better than the five-region option A or the lone short region in C. The sequence and typical membrane-helix lengths also favor the full 357..377 span over B’s shorter 358..373 span.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level pattern and candidate hydrophobic spans provide a meaningful basis for choosing D without needing the target’s database record, though sequence-based boundary predictions are not exact and the inference is not experimental proof."
  },
  "case_id": "transmembrane_0109",
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
    "reason": "The sequence-matched UniProt records annotate all six regions in D as transmembrane helices. These annotations are computational, based on PROSITE-ProRule evidence, rather than direct experimental demonstrations of each boundary."
  },
  "important_caveats": [
    "The supporting source annotations are computational PROSITE-ProRule annotations, not experimental measurements of the individual helix boundaries.",
    "The sequence matches the cited historical entry, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The boundaries of predicted helices can be uncertain, but the offered full-length spans and six-helix pattern make D the best-supported choice; the shorter first span in B is less plausible as a complete membrane crossing."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate all six regions in D as transmembrane helices. These annotations are computational, based on PROSITE-ProRule evidence, rather than direct experimental demonstrations of each boundary.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a hydrophobic membrane-domain region and a downstream ABC-transporter P-loop-like motif (…IGKSGSGKSS…). Transferable knowledge of ABC transporters supports a multi-helix membrane domain; among these choices, six candidate helices fit better than the five-region option A or the lone short region in C. The sequence and typical membrane-helix lengths also favor the full 357..377 span over B’s shorter 358..373 span.",
    "missing_item_specific_fact": "",
    "reason": "The family-level pattern and candidate hydrophobic spans provide a meaningful basis for choosing D without needing the target’s database record, though sequence-based boundary predictions are not exact and the inference is not experimental proof."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The boundaries of predicted helices can be uncertain, but the offered full-length spans and six-helix pattern make D the best-supported choice; the shorter first span in B is less plausible as a complete membrane crossing."
  },
  "important_caveats": [
    "The supporting source annotations are computational PROSITE-ProRule annotations, not experimental measurements of the individual helix boundaries.",
    "The sequence matches the cited historical entry, but the author's exact source snapshot is unknown."
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
  "requested_accession": "Q8IDH9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "0e938c20743637e45d04227baafe55014e41bc01995ba516bab1cce5bc703a70",
  "benchmark_sequence_length": 1049,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 150,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "current_source_sequence_sha256": "0e938c20743637e45d04227baafe55014e41bc01995ba516bab1cce5bc703a70",
  "current_source_sequence_length": 1049,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 148,
  "selected_historical_version": {
    "accession": "Q8IDH9",
    "database": "Swiss-Prot",
    "entryVersion": 148,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ATM1_PLAF7",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "selected_historical_source_sequence_sha256": "0e938c20743637e45d04227baafe55014e41bc01995ba516bab1cce5bc703a70",
  "selected_historical_source_sequence_length": 1049,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 148,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q8IDH9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":150,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAD52642.1\",\"source\":\"EMBL\"}],\"value\":\"ABC transporter B family member 6, putative\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"PfABCB6\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"PfMDR6\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"7.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"ABC transporter ATM1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"PfATM1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":377},\"start\":{\"modifier\":\"EXACT\",\"value\":357}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":419},\"start\":{\"modifier\":\"EXACT\",\"value\":397}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":501},\"start\":{\"modifier\":\"EXACT\",\"value\":481}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":526},\"start\":{\"modifier\":\"EXACT\",\"value\":506}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":611},\"start\":{\"modifier\":\"EXACT\",\"value\":591}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":639},\"start\":{\"modifier\":\"EXACT\",\"value\":619}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Shrivastava D.\",\"Abboud E.\",\"Ramchandra J.P.\",\"Jha A.\",\"Marq J.B.\",\"Chaurasia A.\",\"Mitra K.\",\"Sadik M.\",\"Siddiqi M.I.\",\"Soldati-Favre D.\",\"Kloehn J.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39348385\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1012593\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1012593\",\"id\":\"39348385\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1012593\",\"publicationDate\":\"2024\",\"title\":\"ATM1, an essential conserved transporter in Apicomplexa, bridges mitochondrial and cytosolic [Fe-S] biogenesis.\",\"volume\":\"20\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"INTERACTION WITH ISCU; ISCA2; MHCF101/CFD1 AND NBP35\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF ARG-534 AND GLU-972\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "source_locator": "lines 1-18",
  "excerpt": "ID   ATM1_PLAF7              Reviewed;        1049 AA.\nAC   Q8IDH9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 148.\nDE   RecName: Full=ABC transporter ATM1 {ECO:0000305};\nDE            Short=PfATM1 {ECO:0000303|PubMed:39348385};\nDE            EC=7.-.-.- {ECO:0000269|PubMed:39348385};\nDE   AltName: Full=ABC transporter B family member 6, putative {ECO:0000312|EMBL:CAD52642.1};\nDE            Short=PfABCB6 {ECO:0000303|PubMed:39348385};\nDE   AltName: Full=PfMDR6 {ECO:0000303|PubMed:39348385};\nDE   Flags: Precursor;\nGN   Name=ABCB6 {ECO:0000305};\nGN   ORFNames=PF3D7_1352100 {ECO:0000312|EMBL:CAD52642.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 148,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "source_locator": "lines 53-64",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, SUBUNIT, INTERACTION WITH ISCU; ISCA2; MHCF101/CFD1 AND NBP35,\nRP   SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF ARG-534 AND\nRP   GLU-972.\nRX   PubMed=39348385; DOI=10.1371/journal.ppat.1012593;\nRA   Shrivastava D., Abboud E., Ramchandra J.P., Jha A., Marq J.B.,\nRA   Chaurasia A., Mitra K., Sadik M., Siddiqi M.I., Soldati-Favre D.,\nRA   Kloehn J., Habib S.;\nRT   \"ATM1, an essential conserved transporter in Apicomplexa, bridges\nRT   mitochondrial and cytosolic [Fe-S] biogenesis.\";\nRL   PLoS Pathog. 20:e1012593-e1012593(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 148,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "source_locator": "lines 155-158",
  "excerpt": "FT   TRANSMEM        357..377\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 148,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "source_locator": "lines 159-162",
  "excerpt": "FT   TRANSMEM        397..419\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 148,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "source_locator": "lines 163-166",
  "excerpt": "FT   TRANSMEM        481..501\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 148,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "source_locator": "lines 167-170",
  "excerpt": "FT   TRANSMEM        506..526\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 148,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "source_locator": "lines 171-174",
  "excerpt": "FT   TRANSMEM        591..611\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 148,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "source_locator": "lines 175-178",
  "excerpt": "FT   TRANSMEM        619..639\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 148,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
