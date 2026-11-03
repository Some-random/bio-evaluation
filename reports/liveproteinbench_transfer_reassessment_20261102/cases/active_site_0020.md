# active_site_0020: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0020.txt)

**Task:** `active_site`  
**Author key, unchanged:** **D** — Position 120 (Nucleophile)

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
MRSSTISASAVVLLSGLASAQTFTDCNPTEKTCPSDPAIGGLQVTDFTAGKSSYWEVEDGTTMSYDGTLGAQFVISTATDAPTIKNIGYIMFGRIETWVRASAGTGIVSSFILESDDLDEIDWEWLGANNAEAENNFFGKGNTTTYDRAQYPAVATPIDTFHNYTIDWTAKSTIWYIDGVAVRTLLYDDKQTVGGKNYPQTPMLVKMGSWIGCASKAAETDSATAGTCSWAGGAVDLTQGPFTMYVKNVTIQDYGCATEYTYGDLTGDYTSIKATGGCSADGSAASPSASSSSAASGSSSSTKSSSGSSTLSTVTGTTSAIAVGTATGTATLSAGEKATAAAISGSTTSSSTIAKVTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM

[Multiple Choices]
A. Position 250 (Proton acceptor)
B. Position 95 (Nucleophile)
C. Position 1045 (Proton acceptor; for dehydratase activity)
D. Position 120 (Nucleophile)
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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched UniProt entry annotates position 120 as the nucleophile, consistent with choice D. This is a literature-supported database annotation; the supplied excerpts do not independently validate the underlying experiment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a sufficiently specific general biological basis for identifying residue 120 as the nucleophile rather than the other candidate positions.


**Missing item-specific fact**

> The protein-specific assignment of position 120 as the nucleophile, supported by the cited literature and recorded in UniProt, is absent from the model input.


**Reason**

> The exact residue position and catalytic role require protein-specific functional annotation or experimental knowledge. Recognizing the sequence or using a generic predictor would not make this a reasoning-supported distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the matched annotation supports D. The entry also annotates position 124 as a proton donor, but that role and position are not offered as a competing choice.


### Important caveats

- The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.
- The database annotation is linked to a publication; the provided evidence does not include the primary experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific general biological basis for identifying residue 120 as the nucleophile rather than the other candidate positions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of position 120 as the nucleophile, supported by the cited literature and recorded in UniProt, is absent from the model input.",
    "reason": "The exact residue position and catalytic role require protein-specific functional annotation or experimental knowledge. Recognizing the sequence or using a generic predictor would not make this a reasoning-supported distinction."
  },
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates position 120 as the nucleophile, consistent with choice D. This is a literature-supported database annotation; the supplied excerpts do not independently validate the underlying experiment."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The database annotation is linked to a publication; the provided evidence does not include the primary experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched annotation supports D. The entry also annotates position 124 as a proton donor, but that role and position are not offered as a competing choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates position 120 as the nucleophile, consistent with choice D. This is a literature-supported database annotation; the supplied excerpts do not independently validate the underlying experiment.",
    "evidence_ids": ["C5", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific general biological basis for identifying residue 120 as the nucleophile rather than the other candidate positions.",
    "missing_item_specific_fact": "The protein-specific assignment of position 120 as the nucleophile, supported by the cited literature and recorded in UniProt, is absent from the model input.",
    "reason": "The exact residue position and catalytic role require protein-specific functional annotation or experimental knowledge. Recognizing the sequence or using a generic predictor would not make this a reasoning-supported distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched annotation supports D. The entry also annotates position 124 as a proton donor, but that role and position are not offered as a competing choice."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The database annotation is linked to a publication; the provided evidence does not include the primary experimental results."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384J6C4 annotates ACT_SITE at position 120 as 'Nucleophile' with evidence code ECO:0000305 (inferred by direct assay) from PubMed:33846308 (Bi et al., Nat. Commun. 2021), indicating experimental support. The sequence at position 120 is Glu (E), chemically consistent with a nucleophile in a glycoside hydrolase/transglycosylase. The protein is 391 AA, so choice C (position 1045) is impossible. Position 95 is Ile (not a nucleophile), and position 250 is Thr (not a typical proton acceptor in this enzyme class). The expected answer D is directly confirmed by the database annotation with experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [C11](#evidence-c11), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a Crh-like chitin transglycosylase (GH18-related). A model recognizing glycoside hydrolase/transglycosylase function can identify the DxxDxxxE-like catalytic motif in the region ~116–124 (D-D-L-D-E-I-D-W-E). Among the four choices: (C) position 1045 is impossible for a 391-AA protein; (B) position 95 is Ile, not a viable nucleophile; (A) position 250 is Thr, not a typical proton acceptor in glycosidases. Only choice D (Glu at 120, nucleophile) presents a chemically plausible catalytic residue within the identified motif region. Glu is the canonical nucleophile in GH18-family glycosidases, and its position within the DxxDxxxE-like cluster provides a concrete biochemical argument favoring D over the other options.


**Missing item-specific fact**

> The precise mechanistic distinction between E(120) as nucleophile versus E(124) as proton donor (or vice versa) in this Crh-like subfamily is not trivially derivable from the canonical GH18 DxxDxxxE motif alone, since the canonical motif would predict the terminal E (124) as nucleophile. The exact role assignment for E(120) benefits from knowledge of Crh-specific mechanism reported in PubMed:33846308.


**Reason**

> Although the exact nucleophile-vs-proton-donor assignment for this non-canonical Crh variant requires some specific mechanistic knowledge, the multiple-choice format allows elimination of three clearly implausible options (out-of-range position, non-catalytic residues) leaving only the chemically sensible Glu-in-motif answer. This elimination plus recognition of the GH18 catalytic motif provides meaningful reasoning grounds to select D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one choice (D) presents a chemically plausible catalytic residue (Glu) at a position within the identified active-site motif. The other three options are eliminated by basic constraints: C is out of range, B is an isoleucine, A is a threonine not typically serving as proton acceptor in this enzyme class. No genuine ambiguity exists among the options.


### Important caveats

- The EC-number assignments (chitinase, transglycosylase) for this entry are by similarity (ECO:0000250|UniProtKB:Q8J0P4), not direct experiment; however, the active-site annotations at 120 and 124 carry experimental evidence (ECO:0000305).
- The canonical GH18 DxxDxxxE motif would nominally predict the terminal Glu (position 124) as nucleophile, whereas the experimental annotation assigns nucleophile role to Glu-120 in this Crh-like protein. A model relying solely on the canonical motif template might misassign the nucleophile position, but the multiple-choice format still permits correct selection by elimination.
- The UniProt entry was first public in June 2025; the author's construction date is unknown, so the annotation may not have existed when the benchmark was built.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a Crh-like chitin transglycosylase (GH18-related). A model recognizing glycoside hydrolase/transglycosylase function can identify the DxxDxxxE-like catalytic motif in the region ~116–124 (D-D-L-D-E-I-D-W-E). Among the four choices: (C) position 1045 is impossible for a 391-AA protein; (B) position 95 is Ile, not a viable nucleophile; (A) position 250 is Thr, not a typical proton acceptor in glycosidases. Only choice D (Glu at 120, nucleophile) presents a chemically plausible catalytic residue within the identified motif region. Glu is the canonical nucleophile in GH18-family glycosidases, and its position within the DxxDxxxE-like cluster provides a concrete biochemical argument favoring D over the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise mechanistic distinction between E(120) as nucleophile versus E(124) as proton donor (or vice versa) in this Crh-like subfamily is not trivially derivable from the canonical GH18 DxxDxxxE motif alone, since the canonical motif would predict the terminal E (124) as nucleophile. The exact role assignment for E(120) benefits from knowledge of Crh-specific mechanism reported in PubMed:33846308.",
    "reason": "Although the exact nucleophile-vs-proton-donor assignment for this non-canonical Crh variant requires some specific mechanistic knowledge, the multiple-choice format allows elimination of three clearly implausible options (out-of-range position, non-catalytic residues) leaving only the chemically sensible Glu-in-motif answer. This elimination plus recognition of the GH18 catalytic motif provides meaningful reasoning grounds to select D."
  },
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4",
      "C11",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384J6C4 annotates ACT_SITE at position 120 as 'Nucleophile' with evidence code ECO:0000305 (inferred by direct assay) from PubMed:33846308 (Bi et al., Nat. Commun. 2021), indicating experimental support. The sequence at position 120 is Glu (E), chemically consistent with a nucleophile in a glycoside hydrolase/transglycosylase. The protein is 391 AA, so choice C (position 1045) is impossible. Position 95 is Ile (not a nucleophile), and position 250 is Thr (not a typical proton acceptor in this enzyme class). The expected answer D is directly confirmed by the database annotation with experimental evidence."
  },
  "important_caveats": [
    "The EC-number assignments (chitinase, transglycosylase) for this entry are by similarity (ECO:0000250|UniProtKB:Q8J0P4), not direct experiment; however, the active-site annotations at 120 and 124 carry experimental evidence (ECO:0000305).",
    "The canonical GH18 DxxDxxxE motif would nominally predict the terminal Glu (position 124) as nucleophile, whereas the experimental annotation assigns nucleophile role to Glu-120 in this Crh-like protein. A model relying solely on the canonical motif template might misassign the nucleophile position, but the multiple-choice format still permits correct selection by elimination.",
    "The UniProt entry was first public in June 2025; the author's construction date is unknown, so the annotation may not have existed when the benchmark was built."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one choice (D) presents a chemically plausible catalytic residue (Glu) at a position within the identified active-site motif. The other three options are eliminated by basic constraints: C is out of range, B is an isoleucine, A is a threonine not typically serving as proton acceptor in this enzyme class. No genuine ambiguity exists among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384J6C4 annotates ACT_SITE at position 120 as 'Nucleophile' with evidence code ECO:0000305 (inferred by direct assay) from PubMed:33846308 (Bi et al., Nat. Commun. 2021), indicating experimental support. The sequence at position 120 is Glu (E), chemically consistent with a nucleophile in a glycoside hydrolase/transglycosylase. The protein is 391 AA, so choice C (position 1045) is impossible. Position 95 is Ile (not a nucleophile), and position 250 is Thr (not a typical proton acceptor in this enzyme class). The expected answer D is directly confirmed by the database annotation with experimental evidence.",
    "evidence_ids": ["C5", "H3", "C6", "H4", "C11", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a Crh-like chitin transglycosylase (GH18-related). A model recognizing glycoside hydrolase/transglycosylase function can identify the DxxDxxxE-like catalytic motif in the region ~116–124 (D-D-L-D-E-I-D-W-E). Among the four choices: (C) position 1045 is impossible for a 391-AA protein; (B) position 95 is Ile, not a viable nucleophile; (A) position 250 is Thr, not a typical proton acceptor in glycosidases. Only choice D (Glu at 120, nucleophile) presents a chemically plausible catalytic residue within the identified motif region. Glu is the canonical nucleophile in GH18-family glycosidases, and its position within the DxxDxxxE-like cluster provides a concrete biochemical argument favoring D over the other options.",
    "missing_item_specific_fact": "The precise mechanistic distinction between E(120) as nucleophile versus E(124) as proton donor (or vice versa) in this Crh-like subfamily is not trivially derivable from the canonical GH18 DxxDxxxE motif alone, since the canonical motif would predict the terminal E (124) as nucleophile. The exact role assignment for E(120) benefits from knowledge of Crh-specific mechanism reported in PubMed:33846308.",
    "reason": "Although the exact nucleophile-vs-proton-donor assignment for this non-canonical Crh variant requires some specific mechanistic knowledge, the multiple-choice format allows elimination of three clearly implausible options (out-of-range position, non-catalytic residues) leaving only the chemically sensible Glu-in-motif answer. This elimination plus recognition of the GH18 catalytic motif provides meaningful reasoning grounds to select D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one choice (D) presents a chemically plausible catalytic residue (Glu) at a position within the identified active-site motif. The other three options are eliminated by basic constraints: C is out of range, B is an isoleucine, A is a threonine not typically serving as proton acceptor in this enzyme class. No genuine ambiguity exists among the options."
  },
  "important_caveats": [
    "The EC-number assignments (chitinase, transglycosylase) for this entry are by similarity (ECO:0000250|UniProtKB:Q8J0P4), not direct experiment; however, the active-site annotations at 120 and 124 carry experimental evidence (ECO:0000305).",
    "The canonical GH18 DxxDxxxE motif would nominally predict the terminal Glu (position 124) as nucleophile, whereas the experimental annotation assigns nucleophile role to Glu-120 in this Crh-like protein. A model relying solely on the canonical motif template might misassign the nucleophile position, but the multiple-choice format still permits correct selection by elimination.",
    "The UniProt entry was first public in June 2025; the author's construction date is unknown, so the annotation may not have existed when the benchmark was built."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> For the sequence-matched protein, the UniProt active-site annotation identifies position 120 as the nucleophile and cites PubMed 33846308; the historical record gives the same annotation. This supports choice D, though the source annotation is not an independent review of the underlying experiment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Position 120 is a glutamate in the sequence's acidic E...E motif around residues 120–124. In retaining glycosidases, a catalytic carboxylate can act as the nucleophile, with a nearby carboxylate serving as the acid/base partner. That makes the glutamate at 120 a credible nucleophile candidate; the other listed positions are inconsistent with this motif, and position 1045 exceeds the sequence length.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable glycosidase catalytic principles provide a meaningful basis for selecting position 120 as the nucleophile, without needing the exact protein's recorded annotation. This is a family-level, probabilistic inference rather than proof of the residue's experimentally assigned role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is comparably supported: the position-1045 choice is outside the 391-residue sequence, and the other proposed positions do not fit the catalytic acidic-residue motif.


### Important caveats

- The reviewer-only record supports the answer but was not part of the original model input.
- The database annotation cites literature, but the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Position 120 is a glutamate in the sequence's acidic E...E motif around residues 120–124. In retaining glycosidases, a catalytic carboxylate can act as the nucleophile, with a nearby carboxylate serving as the acid/base partner. That makes the glutamate at 120 a credible nucleophile candidate; the other listed positions are inconsistent with this motif, and position 1045 exceeds the sequence length.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable glycosidase catalytic principles provide a meaningful basis for selecting position 120 as the nucleophile, without needing the exact protein's recorded annotation. This is a family-level, probabilistic inference rather than proof of the residue's experimentally assigned role."
  },
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "For the sequence-matched protein, the UniProt active-site annotation identifies position 120 as the nucleophile and cites PubMed 33846308; the historical record gives the same annotation. This supports choice D, though the source annotation is not an independent review of the underlying experiment."
  },
  "important_caveats": [
    "The reviewer-only record supports the answer but was not part of the original model input.",
    "The database annotation cites literature, but the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported: the position-1045 choice is outside the 391-residue sequence, and the other proposed positions do not fit the catalytic acidic-residue motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "For the sequence-matched protein, the UniProt active-site annotation identifies position 120 as the nucleophile and cites PubMed 33846308; the historical record gives the same annotation. This supports choice D, though the source annotation is not an independent review of the underlying experiment.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Position 120 is a glutamate in the sequence's acidic E...E motif around residues 120–124. In retaining glycosidases, a catalytic carboxylate can act as the nucleophile, with a nearby carboxylate serving as the acid/base partner. That makes the glutamate at 120 a credible nucleophile candidate; the other listed positions are inconsistent with this motif, and position 1045 exceeds the sequence length.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable glycosidase catalytic principles provide a meaningful basis for selecting position 120 as the nucleophile, without needing the exact protein's recorded annotation. This is a family-level, probabilistic inference rather than proof of the residue's experimentally assigned role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported: the position-1045 choice is outside the 391-residue sequence, and the other proposed positions do not fit the catalytic acidic-residue motif."
  },
  "important_caveats": [
    "The reviewer-only record supports the answer but was not part of the original model input.",
    "The database annotation cites literature, but the primary study was not independently reviewed here."
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
  "requested_accession": "A0A384J6C4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "45397ff42b669bfa8d792796bca49c6799638f51b62028337c71133258f86793",
  "benchmark_sequence_length": 391,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "current_source_sequence_sha256": "45397ff42b669bfa8d792796bca49c6799638f51b62028337c71133258f86793",
  "current_source_sequence_length": 391,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 30,
  "selected_historical_version": {
    "accession": "A0A384J6C4",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH1_BOTFB",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "selected_historical_source_sequence_sha256": "45397ff42b669bfa8d792796bca49c6799638f51b62028337c71133258f86793",
  "selected_historical_source_sequence_length": 391,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A384J6C4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitinase crh1\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitin transglycosylase crh1\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":120},\"start\":{\"modifier\":\"EXACT\",\"value\":120}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":124},\"start\":{\"modifier\":\"EXACT\",\"value\":124}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":124},\"start\":{\"modifier\":\"EXACT\",\"value\":124}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":206},\"start\":{\"modifier\":\"EXACT\",\"value\":206}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/features/11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":210},\"start\":{\"modifier\":\"EXACT\",\"value\":210}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":227},\"start\":{\"modifier\":\"EXACT\",\"value\":227}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Bi K.\",\"Scalschi L.\",\"Jaiswal N.\",\"Mengiste T.\",\"Fried R.\",\"Sanz A.B.\",\"Arroyo J.\",\"Zhu W.\",\"Masrati G.\",\"Sharon A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33846308\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-021-22436-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"2166\",\"id\":\"33846308\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2166\",\"publicationDate\":\"2021\",\"title\":\"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.\",\"volume\":\"12\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"DOMAIN\",\"MUTAGENESIS OF CYS-33; GLU-120; ASP-122 AND GLU-124\",\"SUBUNIT\",\"INTERACTION WITH CRH2 AND CRH3\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "source_locator": "lines 1-19",
  "excerpt": "ID   CRH1_BOTFB              Reviewed;         391 AA.\nAC   A0A384J6C4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=Crh-like protein 1 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh1 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh1 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\nGN   Name=crh1 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_01g06010;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "source_locator": "lines 56-65",
  "excerpt": "RN   [4]\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, DOMAIN, MUTAGENESIS\nRP   OF CYS-33; GLU-120; ASP-122 AND GLU-124, SUBUNIT, AND INTERACTION WITH CRH2\nRP   AND CRH3.\nRX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;\nRA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,\nRA   Arroyo J., Zhu W., Masrati G., Sharon A.;\nRT   \"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector\nRT   triggering plant cell death and defense response.\";\nRL   Nat. Commun. 12:2166-2166(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "source_locator": "lines 169-171",
  "excerpt": "FT   ACT_SITE        120\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000305|PubMed:33846308\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "source_locator": "lines 172-174",
  "excerpt": "FT   ACT_SITE        124\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000305|PubMed:33846308\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "source_locator": "lines 175-178",
  "excerpt": "FT   BINDING         124\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "source_locator": "lines 179-182",
  "excerpt": "FT   BINDING         206\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "source_locator": "lines 183-186",
  "excerpt": "FT   BINDING         210\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "source_locator": "lines 187-190",
  "excerpt": "FT   BINDING         227\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 30,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
