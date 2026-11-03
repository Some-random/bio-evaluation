# active_site_0112: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0112.txt)

**Task:** `active_site`  
**Author key, unchanged:** **C** — Position 511 (Proton acceptor)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | no saved label | no saved label | output error (invalid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. Position 2059 (For beta-ketoacyl synthase 2 activity)
B. Position 251 (Proton acceptor)
C. Position 511 (Proton acceptor)
D. Position 215 (Charge relay system)
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

> The sequence matches the 598-residue UniProt entry, which annotates position 511 as an active-site proton acceptor. The annotation is transferred by similarity from UniProtKB:P9WKJ5, so it supports the key but is not direct experimental evidence for this protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence length rules out position 2059, but sequence inspection and general biological knowledge do not establish which of positions 251 and 511 is the proton acceptor.


**Missing item-specific fact**

> The protein-specific active-site annotation or equivalent evidence mapping the proton-acceptor role to position 511.


**Reason**

> Choosing C requires an exact residue-to-function assignment absent from the prompt; recognizing or looking up the protein-specific annotation is not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only annotation supports C; it does not support B as an alternative. Without that annotation, the supplied sequence alone does not distinguish the two proton-acceptor choices.


### Important caveats

- The supporting site annotation is similarity-based, not shown here to derive from direct experimentation on this protein.
- The identity and sequence match are reviewer-only information and were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence length rules out position 2059, but sequence inspection and general biological knowledge do not establish which of positions 251 and 511 is the proton acceptor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific active-site annotation or equivalent evidence mapping the proton-acceptor role to position 511.",
    "reason": "Choosing C requires an exact residue-to-function assignment absent from the prompt; recognizing or looking up the protein-specific annotation is not sequence-based reasoning."
  },
  "case_id": "active_site_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the 598-residue UniProt entry, which annotates position 511 as an active-site proton acceptor. The annotation is transferred by similarity from UniProtKB:P9WKJ5, so it supports the key but is not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The supporting site annotation is similarity-based, not shown here to derive from direct experimentation on this protein.",
    "The identity and sequence match are reviewer-only information and were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports C; it does not support B as an alternative. Without that annotation, the supplied sequence alone does not distinguish the two proton-acceptor choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the 598-residue UniProt entry, which annotates position 511 as an active-site proton acceptor. The annotation is transferred by similarity from UniProtKB:P9WKJ5, so it supports the key but is not direct experimental evidence for this protein.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence length rules out position 2059, but sequence inspection and general biological knowledge do not establish which of positions 251 and 511 is the proton acceptor.",
    "missing_item_specific_fact": "The protein-specific active-site annotation or equivalent evidence mapping the proton-acceptor role to position 511.",
    "reason": "Choosing C requires an exact residue-to-function assignment absent from the prompt; recognizing or looking up the protein-specific annotation is not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports C; it does not support B as an alternative. Without that annotation, the supplied sequence alone does not distinguish the two proton-acceptor choices."
  },
  "important_caveats": [
    "The supporting site annotation is similarity-based, not shown here to derive from direct experimentation on this protein.",
    "The identity and sequence match are reviewer-only information and were not supplied to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q0CPG9 (sequence matched, 598 aa) annotates an Active site at position 511 with description 'Proton acceptor' (evidence C5/H3). The evidence code is ECO:0000250 (inferred by similarity from P9WKJ5), so this is a computational transfer annotation rather than direct experimental determination for this specific protein. Nonetheless, the database annotation directly supports the expected answer. The protein is 598 residues, making option A (position 2059) impossible; options B (251) and D (215) are not annotated as active sites.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Options A and D can be eliminated by general reasoning: position 2059 exceeds the 598-residue sequence length, and a 'charge relay system' is characteristic of serine proteases, not dihydroxy-acid dehydratases (which use a &#91;2Fe-2S&#93; cluster and Mg2+ cofactors). However, both remaining options B (position 251) and C (position 511) are labeled 'Proton acceptor,' the correct mechanistic description for DHAD. Distinguishing the exact catalytic position requires knowing which specific residue in this protein serves as the proton acceptor, which depends on structural alignment with a characterized DHAD (e.g., E. coli IlvD Cys444) or direct database lookup.


**Missing item-specific fact**

> The precise residue position (511 vs. 251) that acts as the proton acceptor in this specific mitochondrial DHAD from Aspergillus terreus, which requires either the UniProt annotation for Q0CPG9 or a detailed structural/sequence alignment with a characterized DHAD ortholog to map the catalytic cysteine.


**Reason**

> While general knowledge of DHAD mechanism (proton acceptor, Fe-S cluster, Mg2+) eliminates options A and D, the final choice between B and C—both labeled 'Proton acceptor' at different positions—cannot be resolved from the raw sequence alone without either recognizing this specific protein and recalling its annotation, or performing a detailed structural alignment. The sequence provides no obvious local motif that unambiguously marks position 511 over 251 as the catalytic residue.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both B and C are labeled 'Proton acceptor,' which is the correct mechanistic role for the DHAD active site. Without the specific position annotation or structural context, a knowledgeable model could argue for either position based on proximity to cofactor-binding residues. Options A (out-of-range position) and D (wrong mechanism for DHAD) are clearly eliminable. The question stem mentions 'amino acid residues (by their type and position)' but the options provide only position and functional description, not the residue identity, which is a minor inconsistency.


### Important caveats

- The active site annotation (position 511) carries evidence code ECO:0000250 (inferred by similarity from P9WKJ5), meaning it is a computational transfer, not a direct experimental measurement on this protein.
- The protein is annotated as a mitochondrial precursor; the numbering refers to the full precursor sequence including the targeting peptide.
- Option A (position 2059) is trivially impossible for a 598-residue protein and likely a template artifact or deliberate distractor.
- The UniProt annotation for Q0CPG9 was first integrated in April 2025 (Swiss-Prot), so the author's source snapshot timing is relevant to whether this annotation was available at question-construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A and D can be eliminated by general reasoning: position 2059 exceeds the 598-residue sequence length, and a 'charge relay system' is characteristic of serine proteases, not dihydroxy-acid dehydratases (which use a [2Fe-2S] cluster and Mg2+ cofactors). However, both remaining options B (position 251) and C (position 511) are labeled 'Proton acceptor,' the correct mechanistic description for DHAD. Distinguishing the exact catalytic position requires knowing which specific residue in this protein serves as the proton acceptor, which depends on structural alignment with a characterized DHAD (e.g., E. coli IlvD Cys444) or direct database lookup.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise residue position (511 vs. 251) that acts as the proton acceptor in this specific mitochondrial DHAD from Aspergillus terreus, which requires either the UniProt annotation for Q0CPG9 or a detailed structural/sequence alignment with a characterized DHAD ortholog to map the catalytic cysteine.",
    "reason": "While general knowledge of DHAD mechanism (proton acceptor, Fe-S cluster, Mg2+) eliminates options A and D, the final choice between B and C—both labeled 'Proton acceptor' at different positions—cannot be resolved from the raw sequence alone without either recognizing this specific protein and recalling its annotation, or performing a detailed structural alignment. The sequence provides no obvious local motif that unambiguously marks position 511 over 251 as the catalytic residue."
  },
  "case_id": "active_site_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG9 (sequence matched, 598 aa) annotates an Active site at position 511 with description 'Proton acceptor' (evidence C5/H3). The evidence code is ECO:0000250 (inferred by similarity from P9WKJ5), so this is a computational transfer annotation rather than direct experimental determination for this specific protein. Nonetheless, the database annotation directly supports the expected answer. The protein is 598 residues, making option A (position 2059) impossible; options B (251) and D (215) are not annotated as active sites."
  },
  "important_caveats": [
    "The active site annotation (position 511) carries evidence code ECO:0000250 (inferred by similarity from P9WKJ5), meaning it is a computational transfer, not a direct experimental measurement on this protein.",
    "The protein is annotated as a mitochondrial precursor; the numbering refers to the full precursor sequence including the targeting peptide.",
    "Option A (position 2059) is trivially impossible for a 598-residue protein and likely a template artifact or deliberate distractor.",
    "The UniProt annotation for Q0CPG9 was first integrated in April 2025 (Swiss-Prot), so the author's source snapshot timing is relevant to whether this annotation was available at question-construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both B and C are labeled 'Proton acceptor,' which is the correct mechanistic role for the DHAD active site. Without the specific position annotation or structural context, a knowledgeable model could argue for either position based on proximity to cofactor-binding residues. Options A (out-of-range position) and D (wrong mechanism for DHAD) are clearly eliminable. The question stem mentions 'amino acid residues (by their type and position)' but the options provide only position and functional description, not the residue identity, which is a minor inconsistency."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG9 (sequence matched, 598 aa) annotates an Active site at position 511 with description 'Proton acceptor' (evidence C5/H3). The evidence code is ECO:0000250 (inferred by similarity from P9WKJ5), so this is a computational transfer annotation rather than direct experimental determination for this specific protein. Nonetheless, the database annotation directly supports the expected answer. The protein is 598 residues, making option A (position 2059) impossible; options B (251) and D (215) are not annotated as active sites.",
    "evidence_ids": ["C5", "H3", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Options A and D can be eliminated by general reasoning: position 2059 exceeds the 598-residue sequence length, and a 'charge relay system' is characteristic of serine proteases, not dihydroxy-acid dehydratases (which use a [2Fe-2S] cluster and Mg2+ cofactors). However, both remaining options B (position 251) and C (position 511) are labeled 'Proton acceptor,' the correct mechanistic description for DHAD. Distinguishing the exact catalytic position requires knowing which specific residue in this protein serves as the proton acceptor, which depends on structural alignment with a characterized DHAD (e.g., E. coli IlvD Cys444) or direct database lookup.",
    "missing_item_specific_fact": "The precise residue position (511 vs. 251) that acts as the proton acceptor in this specific mitochondrial DHAD from Aspergillus terreus, which requires either the UniProt annotation for Q0CPG9 or a detailed structural/sequence alignment with a characterized DHAD ortholog to map the catalytic cysteine.",
    "reason": "While general knowledge of DHAD mechanism (proton acceptor, Fe-S cluster, Mg2+) eliminates options A and D, the final choice between B and C—both labeled 'Proton acceptor' at different positions—cannot be resolved from the raw sequence alone without either recognizing this specific protein and recalling its annotation, or performing a detailed structural alignment. The sequence provides no obvious local motif that unambiguously marks position 511 over 251 as the catalytic residue."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both B and C are labeled 'Proton acceptor,' which is the correct mechanistic role for the DHAD active site. Without the specific position annotation or structural context, a knowledgeable model could argue for either position based on proximity to cofactor-binding residues. Options A (out-of-range position) and D (wrong mechanism for DHAD) are clearly eliminable. The question stem mentions 'amino acid residues (by their type and position)' but the options provide only position and functional description, not the residue identity, which is a minor inconsistency."
  },
  "important_caveats": [
    "The active site annotation (position 511) carries evidence code ECO:0000250 (inferred by similarity from P9WKJ5), meaning it is a computational transfer, not a direct experimental measurement on this protein.",
    "The protein is annotated as a mitochondrial precursor; the numbering refers to the full precursor sequence including the targeting peptide.",
    "Option A (position 2059) is trivially impossible for a 598-residue protein and likely a template artifact or deliberate distractor.",
    "The UniProt annotation for Q0CPG9 was first integrated in April 2025 (Swiss-Prot), so the author's source snapshot timing is relevant to whether this annotation was available at question-construction time."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies residue 511 as a proton acceptor; the historical record also contains this annotation. Its evidence is transfer by similarity from another UniProt protein, so it supports the key as a homology-based annotation, not as direct experimental verification on this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the Fe-S-dependent dihydroxy-acid dehydratase/IlvD family. Transferable family knowledge and alignment to related enzymes can locate the conserved catalytic proton-accepting residue in the homologous C-terminal region, supporting position 511 rather than the other offered proton-acceptor position, 251. Position 2059 is outside this 598-residue sequence, and the charge-relay option does not fit this family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Selecting the exact coordinate requires family recognition and residue mapping, but those can be inferred from transferable knowledge of related dehydratases; the task is not necessarily dependent on recalling this protein's own database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although two options describe a proton acceptor, they specify different positions; the family-level residue mapping favors position 511.


### Important caveats

- The supplied evidence supports a similarity-transferred annotation, not direct experimental confirmation for this sequence.
- The reviewer-only source identification and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the Fe-S-dependent dihydroxy-acid dehydratase/IlvD family. Transferable family knowledge and alignment to related enzymes can locate the conserved catalytic proton-accepting residue in the homologous C-terminal region, supporting position 511 rather than the other offered proton-acceptor position, 251. Position 2059 is outside this 598-residue sequence, and the charge-relay option does not fit this family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Selecting the exact coordinate requires family recognition and residue mapping, but those can be inferred from transferable knowledge of related dehydratases; the task is not necessarily dependent on recalling this protein's own database record."
  },
  "case_id": "active_site_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 511 as a proton acceptor; the historical record also contains this annotation. Its evidence is transfer by similarity from another UniProt protein, so it supports the key as a homology-based annotation, not as direct experimental verification on this exact protein."
  },
  "important_caveats": [
    "The supplied evidence supports a similarity-transferred annotation, not direct experimental confirmation for this sequence.",
    "The reviewer-only source identification and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although two options describe a proton acceptor, they specify different positions; the family-level residue mapping favors position 511."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 511 as a proton acceptor; the historical record also contains this annotation. Its evidence is transfer by similarity from another UniProt protein, so it supports the key as a homology-based annotation, not as direct experimental verification on this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the Fe-S-dependent dihydroxy-acid dehydratase/IlvD family. Transferable family knowledge and alignment to related enzymes can locate the conserved catalytic proton-accepting residue in the homologous C-terminal region, supporting position 511 rather than the other offered proton-acceptor position, 251. Position 2059 is outside this 598-residue sequence, and the charge-relay option does not fit this family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "Selecting the exact coordinate requires family recognition and residue mapping, but those can be inferred from transferable knowledge of related dehydratases; the task is not necessarily dependent on recalling this protein's own database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although two options describe a proton acceptor, they specify different positions; the family-level residue mapping favors position 511."
  },
  "important_caveats": [
    "The supplied evidence supports a similarity-transferred annotation, not direct experimental confirmation for this sequence.",
    "The reviewer-only source identification and annotations were not part of the original model input."
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
  "requested_accession": "Q0CPG9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "benchmark_sequence_length": 598,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_source_sequence_length": 598,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 90,
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_source_sequence_length": 598,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":511},\"start\":{\"modifier\":\"EXACT\",\"value\":511}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:190135\",\"name\":\"[2Fe-2S] cluster\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":86},\"start\":{\"modifier\":\"EXACT\",\"value\":86}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":118},\"start\":{\"modifier\":\"EXACT\",\"value\":118}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/features/7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:190135\",\"name\":\"[2Fe-2S] cluster\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":159},\"start\":{\"modifier\":\"EXACT\",\"value\":159}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/features/8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":160},\"start\":{\"modifier\":\"EXACT\",\"value\":160}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/features/9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:190135\",\"name\":\"[2Fe-2S] cluster\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":232},\"start\":{\"modifier\":\"EXACT\",\"value\":232}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/features/10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WKJ5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":485},\"start\":{\"modifier\":\"EXACT\",\"value\":485}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 29-37",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 155-157",
  "excerpt": "FT   ACT_SITE        511\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 158-161",
  "excerpt": "FT   BINDING         86\nFT                   /ligand=\"[2Fe-2S] cluster\"\nFT                   /ligand_id=\"ChEBI:CHEBI:190135\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 162-165",
  "excerpt": "FT   BINDING         118\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 166-169",
  "excerpt": "FT   BINDING         159\nFT                   /ligand=\"[2Fe-2S] cluster\"\nFT                   /ligand_id=\"ChEBI:CHEBI:190135\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 170-173",
  "excerpt": "FT   BINDING         160\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 174-177",
  "excerpt": "FT   BINDING         232\nFT                   /ligand=\"[2Fe-2S] cluster\"\nFT                   /ligand_id=\"ChEBI:CHEBI:190135\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 178-181",
  "excerpt": "FT   BINDING         485\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P9WKJ5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
