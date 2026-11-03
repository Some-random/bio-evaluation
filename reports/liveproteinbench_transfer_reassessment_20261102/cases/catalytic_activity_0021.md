# catalytic_activity_0021: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0021.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **A** — Hydrolysis of alpha-(2-&gt;3)-, alpha-(2-&gt;6)-, alpha-(2-&gt;8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQLSSIADKIRESATMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATIRTGKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYISMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPTGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGNQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.
B. 4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+)
C. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
D. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the Mumps orthorubulavirus hemagglutinin-neuraminidase entry, whose catalytic activity is the reaction in choice A. The annotation cites experimental evidence for EC 3.2.1.18, although the primary study was not independently assessed here.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a hydrophobic segment consistent with membrane anchoring and a large extracellular region, which may make a membrane-associated viral protein more plausible than the soluble enzymes in B–D. That broad inference does not establish sialidase activity or the specific linkages in A.


**Missing item-specific fact**

> The protein-specific identification as a hemagglutinin-neuraminidase with sialidase activity is absent from the input and is needed to select A confidently.


**Reason**

> The sequence and choices provide, at most, broad contextual clues. Distinguishing the specific catalytic reaction requires a protein-specific functional annotation or experimental knowledge, not merely general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports A for the sequence-matched protein; the other choices describe distinct reactions without comparable support.


### Important caveats

- The source annotation reports experimental evidence associated with a 2024 publication and specifies strain 13V165E2; the primary paper was not comprehensively retrieved or independently validated.
- Reviewer-only accession and annotation evidence were not present in the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic segment consistent with membrane anchoring and a large extracellular region, which may make a membrane-associated viral protein more plausible than the soluble enzymes in B–D. That broad inference does not establish sialidase activity or the specific linkages in A.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as a hemagglutinin-neuraminidase with sialidase activity is absent from the input and is needed to select A confidently.",
    "reason": "The sequence and choices provide, at most, broad contextual clues. Distinguishing the specific catalytic reaction requires a protein-specific functional annotation or experimental knowledge, not merely general biological reasoning."
  },
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Mumps orthorubulavirus hemagglutinin-neuraminidase entry, whose catalytic activity is the reaction in choice A. The annotation cites experimental evidence for EC 3.2.1.18, although the primary study was not independently assessed here."
  },
  "important_caveats": [
    "The source annotation reports experimental evidence associated with a 2024 publication and specifies strain 13V165E2; the primary paper was not comprehensively retrieved or independently validated.",
    "Reviewer-only accession and annotation evidence were not present in the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A for the sequence-matched protein; the other choices describe distinct reactions without comparable support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Mumps orthorubulavirus hemagglutinin-neuraminidase entry, whose catalytic activity is the reaction in choice A. The annotation cites experimental evidence for EC 3.2.1.18, although the primary study was not independently assessed here.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a hydrophobic segment consistent with membrane anchoring and a large extracellular region, which may make a membrane-associated viral protein more plausible than the soluble enzymes in B–D. That broad inference does not establish sialidase activity or the specific linkages in A.",
    "missing_item_specific_fact": "The protein-specific identification as a hemagglutinin-neuraminidase with sialidase activity is absent from the input and is needed to select A confidently.",
    "reason": "The sequence and choices provide, at most, broad contextual clues. Distinguishing the specific catalytic reaction requires a protein-specific functional annotation or experimental knowledge, not merely general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A for the sequence-matched protein; the other choices describe distinct reactions without comparable support."
  },
  "important_caveats": [
    "The source annotation reports experimental evidence associated with a 2024 publication and specifies strain 13V165E2; the primary paper was not comprehensively retrieved or independently validated.",
    "Reviewer-only accession and annotation evidence were not present in the evaluated model input."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 582-aa sequence matches UniProt Q9WAF5 (Mumps orthorubulavirus Hemagglutinin-neuraminidase, HN_MUMPV) exactly (SHA-256 confirmed in both current and historical snapshots). The UniProt entry annotates EC 3.2.1.18 with the catalytic activity text identical to Choice A, supported by experimental evidence (ECO:0000269, PubMed:39088577, a 2024 Glycobiology paper on sialidase inhibitors suppressing mumps virus replication). The annotation is present in both the current entry (v132) and the archived entry (v130, first released 2026-01-28), so the key was available at the benchmark construction cutoff.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a hydrophobic stretch near the N-terminus (approx. residues 30–60) consistent with a type-II transmembrane anchor, multiple N-linked glycosylation sequons (N-X-S/T), and a length (~580 aa) typical of paramyxovirus surface glycoproteins. These features indicate a membrane-anchored viral surface glycoprotein that contacts host-cell surface glycans. Among the four choices, only A (neuraminidase/sialidase hydrolysis of sialic-acid linkages on cell-surface glycoconjugates) describes an activity mechanistically consistent with a membrane-tethered viral attachment protein. Choices B (radical-SAM taurine dioxygenase), C (soluble lipoxygenase), and D (soluble NAD-dependent fucose dehydrogenase) all describe activities of soluble, non-membrane enzymes with no plausible role for a type-II TM viral glycoprotein. Eliminating B, C, and D on the basis of membrane topology and biological context is a defensible general-knowledge argument that does not require exact sequence-to-database lookup.


**Missing item-specific fact**

> None strictly required. Full confidence that the specific sialidase linkages (α2→3, α2→6, α2→8) match this particular enzyme would benefit from recognizing the paramyxovirus HN family, but the coarse elimination of B/C/D via membrane-topology reasoning is sufficient to single out A among the given options.


**Reason**

> A model with general virology and membrane-biology knowledge can note the type-II TM domain, glycosylation pattern, and viral-glycoprotein architecture, then reason that only a cell-surface glycan-acting hydrolase (sialidase) fits among the four choices. The three distractors are all soluble enzymes whose catalytic mechanisms and cellular contexts are incompatible with a membrane-anchored viral surface protein. This constitutes a concrete biological argument grounded in the supplied sequence features rather than a pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices B, C, and D describe soluble enzymes (radical-SAM dioxygenase, lipoxygenase, NAD-dependent dehydrogenase) with no membrane-anchoring requirement, making them inconsistent with the observed type-II TM topology and viral glycoprotein context. Only A describes a membrane-associated glycan-acting hydrolase. No second option is defensible given the sequence features.


### Important caveats

- The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational, strengthening the key.
- The reasoning argument (TM domain → membrane protein → eliminates soluble enzymes) is a coarse but valid discriminator among these four specific choices; it would not, by itself, distinguish sialidase from other membrane glycosidases if such alternatives were present.
- The UniProt entry was first publicly released 2025-04-09 (entry v130 in UniSave, 2026-01-28); the benchmark's exact construction date is unknown, but the annotation was available well before the 2026-05-07 cutoff.
- Sequence match is exact (SHA-256 identical) across current and historical snapshots; no numbering or isoform ambiguity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a hydrophobic stretch near the N-terminus (approx. residues 30–60) consistent with a type-II transmembrane anchor, multiple N-linked glycosylation sequons (N-X-S/T), and a length (~580 aa) typical of paramyxovirus surface glycoproteins. These features indicate a membrane-anchored viral surface glycoprotein that contacts host-cell surface glycans. Among the four choices, only A (neuraminidase/sialidase hydrolysis of sialic-acid linkages on cell-surface glycoconjugates) describes an activity mechanistically consistent with a membrane-tethered viral attachment protein. Choices B (radical-SAM taurine dioxygenase), C (soluble lipoxygenase), and D (soluble NAD-dependent fucose dehydrogenase) all describe activities of soluble, non-membrane enzymes with no plausible role for a type-II TM viral glycoprotein. Eliminating B, C, and D on the basis of membrane topology and biological context is a defensible general-knowledge argument that does not require exact sequence-to-database lookup.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Full confidence that the specific sialidase linkages (α2→3, α2→6, α2→8) match this particular enzyme would benefit from recognizing the paramyxovirus HN family, but the coarse elimination of B/C/D via membrane-topology reasoning is sufficient to single out A among the given options.",
    "reason": "A model with general virology and membrane-biology knowledge can note the type-II TM domain, glycosylation pattern, and viral-glycoprotein architecture, then reason that only a cell-surface glycan-acting hydrolase (sialidase) fits among the four choices. The three distractors are all soluble enzymes whose catalytic mechanisms and cellular contexts are incompatible with a membrane-anchored viral surface protein. This constitutes a concrete biological argument grounded in the supplied sequence features rather than a pure database lookup."
  },
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 582-aa sequence matches UniProt Q9WAF5 (Mumps orthorubulavirus Hemagglutinin-neuraminidase, HN_MUMPV) exactly (SHA-256 confirmed in both current and historical snapshots). The UniProt entry annotates EC 3.2.1.18 with the catalytic activity text identical to Choice A, supported by experimental evidence (ECO:0000269, PubMed:39088577, a 2024 Glycobiology paper on sialidase inhibitors suppressing mumps virus replication). The annotation is present in both the current entry (v132) and the archived entry (v130, first released 2026-01-28), so the key was available at the benchmark construction cutoff."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational, strengthening the key.",
    "The reasoning argument (TM domain → membrane protein → eliminates soluble enzymes) is a coarse but valid discriminator among these four specific choices; it would not, by itself, distinguish sialidase from other membrane glycosidases if such alternatives were present.",
    "The UniProt entry was first publicly released 2025-04-09 (entry v130 in UniSave, 2026-01-28); the benchmark's exact construction date is unknown, but the annotation was available well before the 2026-05-07 cutoff.",
    "Sequence match is exact (SHA-256 identical) across current and historical snapshots; no numbering or isoform ambiguity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B, C, and D describe soluble enzymes (radical-SAM dioxygenase, lipoxygenase, NAD-dependent dehydrogenase) with no membrane-anchoring requirement, making them inconsistent with the observed type-II TM topology and viral glycoprotein context. Only A describes a membrane-associated glycan-acting hydrolase. No second option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 582-aa sequence matches UniProt Q9WAF5 (Mumps orthorubulavirus Hemagglutinin-neuraminidase, HN_MUMPV) exactly (SHA-256 confirmed in both current and historical snapshots). The UniProt entry annotates EC 3.2.1.18 with the catalytic activity text identical to Choice A, supported by experimental evidence (ECO:0000269, PubMed:39088577, a 2024 Glycobiology paper on sialidase inhibitors suppressing mumps virus replication). The annotation is present in both the current entry (v132) and the archived entry (v130, first released 2026-01-28), so the key was available at the benchmark construction cutoff.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a hydrophobic stretch near the N-terminus (approx. residues 30–60) consistent with a type-II transmembrane anchor, multiple N-linked glycosylation sequons (N-X-S/T), and a length (~580 aa) typical of paramyxovirus surface glycoproteins. These features indicate a membrane-anchored viral surface glycoprotein that contacts host-cell surface glycans. Among the four choices, only A (neuraminidase/sialidase hydrolysis of sialic-acid linkages on cell-surface glycoconjugates) describes an activity mechanistically consistent with a membrane-tethered viral attachment protein. Choices B (radical-SAM taurine dioxygenase), C (soluble lipoxygenase), and D (soluble NAD-dependent fucose dehydrogenase) all describe activities of soluble, non-membrane enzymes with no plausible role for a type-II TM viral glycoprotein. Eliminating B, C, and D on the basis of membrane topology and biological context is a defensible general-knowledge argument that does not require exact sequence-to-database lookup.",
    "missing_item_specific_fact": "None strictly required. Full confidence that the specific sialidase linkages (α2→3, α2→6, α2→8) match this particular enzyme would benefit from recognizing the paramyxovirus HN family, but the coarse elimination of B/C/D via membrane-topology reasoning is sufficient to single out A among the given options.",
    "reason": "A model with general virology and membrane-biology knowledge can note the type-II TM domain, glycosylation pattern, and viral-glycoprotein architecture, then reason that only a cell-surface glycan-acting hydrolase (sialidase) fits among the four choices. The three distractors are all soluble enzymes whose catalytic mechanisms and cellular contexts are incompatible with a membrane-anchored viral surface protein. This constitutes a concrete biological argument grounded in the supplied sequence features rather than a pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B, C, and D describe soluble enzymes (radical-SAM dioxygenase, lipoxygenase, NAD-dependent dehydrogenase) with no membrane-anchoring requirement, making them inconsistent with the observed type-II TM topology and viral glycoprotein context. Only A describes a membrane-associated glycan-acting hydrolase. No second option is defensible given the sequence features."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational, strengthening the key.",
    "The reasoning argument (TM domain → membrane protein → eliminates soluble enzymes) is a coarse but valid discriminator among these four specific choices; it would not, by itself, distinguish sialidase from other membrane glycosidases if such alternatives were present.",
    "The UniProt entry was first publicly released 2025-04-09 (entry v130 in UniSave, 2026-01-28); the benchmark's exact construction date is unknown, but the annotation was available well before the 2026-05-07 cutoff.",
    "Sequence match is exact (SHA-256 identical) across current and historical snapshots; no numbering or isoform ambiguity."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation assigns this protein the sialidase reaction in choice A and cites experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic membrane anchor followed by a long, glycosylation-rich extracellular protein region, consistent with a viral surface glycoprotein. Transferable knowledge of viral hemagglutinin-neuraminidase proteins links that kind of protein to removal of terminal sialic acid, as in A. This is a probabilistic family-level inference, not a definitive functional assignment from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence architecture and the known functions of related viral surface glycoproteins meaningfully favor A over the soluble Fe-S enzyme, lipid-transforming enzyme, and NAD-dependent sugar enzyme described in B-D; access to this exact protein's database entry is not required to distinguish the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed reactions, A is the one consistent with the inferred viral membrane glycoprotein function.


### Important caveats

- The sequence-based family and function inference is not conclusive on its own; the reviewer-only annotation provides direct support for the key.
- The cited annotation is experimental-evidence-coded, but the underlying primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane anchor followed by a long, glycosylation-rich extracellular protein region, consistent with a viral surface glycoprotein. Transferable knowledge of viral hemagglutinin-neuraminidase proteins links that kind of protein to removal of terminal sialic acid, as in A. This is a probabilistic family-level inference, not a definitive functional assignment from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and the known functions of related viral surface glycoproteins meaningfully favor A over the soluble Fe-S enzyme, lipid-transforming enzyme, and NAD-dependent sugar enzyme described in B-D; access to this exact protein's database entry is not required to distinguish the offered choices."
  },
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein the sialidase reaction in choice A and cites experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The sequence-based family and function inference is not conclusive on its own; the reviewer-only annotation provides direct support for the key.",
    "The cited annotation is experimental-evidence-coded, but the underlying primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, A is the one consistent with the inferred viral membrane glycoprotein function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein the sialidase reaction in choice A and cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane anchor followed by a long, glycosylation-rich extracellular protein region, consistent with a viral surface glycoprotein. Transferable knowledge of viral hemagglutinin-neuraminidase proteins links that kind of protein to removal of terminal sialic acid, as in A. This is a probabilistic family-level inference, not a definitive functional assignment from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and the known functions of related viral surface glycoproteins meaningfully favor A over the soluble Fe-S enzyme, lipid-transforming enzyme, and NAD-dependent sugar enzyme described in B-D; access to this exact protein's database entry is not required to distinguish the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, A is the one consistent with the inferred viral membrane glycoprotein function."
  },
  "important_caveats": [
    "The sequence-based family and function inference is not conclusive on its own; the reviewer-only annotation provides direct support for the key.",
    "The cited annotation is experimental-evidence-coded, but the underlying primary study was not independently reviewed here."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9WAF5 (HN_MUMPV, Mumps orthorubulavirus Hemagglutinin-neuraminidase, EC 3.2.1.18) matches the supplied 582-aa sequence exactly (SHA-256 confirmed). The catalytic activity annotation (C5, H4) is stated verbatim as option A, supported by experimental evidence (ECO:0000269|PubMed:39088577). The sequence comparison is 'matched' in both current and historical snapshots.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a type II membrane protein topology: an N-terminal signal peptide (MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQ) immediately followed by a hydrophobic transmembrane anchor. This topology is characteristic of paramyxovirus HN and F surface glycoproteins. The total length (~582 AA) matches paramyxovirus HN (influenza NA is ~470 AA; bacterial sialidases are typically soluble). In the C-terminal domain, the conserved 'RLLYY' motif (part of the neuraminidase active site in paramyxovirus HN) is clearly present, along with the characteristic C-terminal domain architecture of paramyxovirus neuraminidases. These features collectively identify the protein as a viral neuraminidase/sialidase (option A). Option B (taurine dioxygenase) requires Fe-S cluster motifs and is a small soluble enzyme. Option C (lipoxygenase-like) requires a different domain architecture and is typically >700 AA. Option D (fucose dehydrogenase) requires a Rossmann-fold NAD-binding motif (GxGxxG) and is a soluble cytoplasmic enzyme. None of these features are present. The type II membrane topology + ~580 AA length + RLLYY neuraminidase motif is a family-level pattern transferable from knowledge of other paramyxovirus HN proteins (NDV, measles, human parainfluenza) that meaningfully distinguishes A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the type II membrane protein topology, the characteristic length, and the conserved neuraminidase catalytic motifs (RLLYY) from general knowledge of paramyxovirus HN proteins (e.g., NDV HN, measles HN). These family-level features are sufficient to select the sialidase/neuraminidase option over the three non-membrane, non-sialidase alternatives without recalling the specific UniProt entry for mumps HN.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (B, C, D) describe enzymes with fundamentally different topologies, sizes, and cofactor requirements that are clearly incompatible with the observed sequence features. Only option A is consistent with a type II membrane glycoprotein of ~580 AA bearing neuraminidase motifs.


### Important caveats

- The 'NPPY' catalytic tetrad characteristic of NDV HN is not perfectly conserved in mumps HN; however, the RLLYY motif and overall domain architecture are sufficient for family-level identification.
- The evidence for EC 3.2.1.18 assignment is experimental (PubMed:39088577, 2024), which is relatively recent; older annotations of mumps HN neuraminidase activity were primarily based on sequence similarity to other paramyxovirus HN proteins.
- The reviewer-only evidence confirms the identity but was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable knowledge of paramyxovirus HN proteins.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a type II membrane protein topology: an N-terminal signal peptide (MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQ) immediately followed by a hydrophobic transmembrane anchor. This topology is characteristic of paramyxovirus HN and F surface glycoproteins. The total length (~582 AA) matches paramyxovirus HN (influenza NA is ~470 AA; bacterial sialidases are typically soluble). In the C-terminal domain, the conserved 'RLLYY' motif (part of the neuraminidase active site in paramyxovirus HN) is clearly present, along with the characteristic C-terminal domain architecture of paramyxovirus neuraminidases. These features collectively identify the protein as a viral neuraminidase/sialidase (option A). Option B (taurine dioxygenase) requires Fe-S cluster motifs and is a small soluble enzyme. Option C (lipoxygenase-like) requires a different domain architecture and is typically >700 AA. Option D (fucose dehydrogenase) requires a Rossmann-fold NAD-binding motif (GxGxxG) and is a soluble cytoplasmic enzyme. None of these features are present. The type II membrane topology + ~580 AA length + RLLYY neuraminidase motif is a family-level pattern transferable from knowledge of other paramyxovirus HN proteins (NDV, measles, human parainfluenza) that meaningfully distinguishes A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the type II membrane protein topology, the characteristic length, and the conserved neuraminidase catalytic motifs (RLLYY) from general knowledge of paramyxovirus HN proteins (e.g., NDV HN, measles HN). These family-level features are sufficient to select the sialidase/neuraminidase option over the three non-membrane, non-sialidase alternatives without recalling the specific UniProt entry for mumps HN."
  },
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9WAF5 (HN_MUMPV, Mumps orthorubulavirus Hemagglutinin-neuraminidase, EC 3.2.1.18) matches the supplied 582-aa sequence exactly (SHA-256 confirmed). The catalytic activity annotation (C5, H4) is stated verbatim as option A, supported by experimental evidence (ECO:0000269|PubMed:39088577). The sequence comparison is 'matched' in both current and historical snapshots."
  },
  "important_caveats": [
    "The 'NPPY' catalytic tetrad characteristic of NDV HN is not perfectly conserved in mumps HN; however, the RLLYY motif and overall domain architecture are sufficient for family-level identification.",
    "The evidence for EC 3.2.1.18 assignment is experimental (PubMed:39088577, 2024), which is relatively recent; older annotations of mumps HN neuraminidase activity were primarily based on sequence similarity to other paramyxovirus HN proteins.",
    "The reviewer-only evidence confirms the identity but was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable knowledge of paramyxovirus HN proteins."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B, C, D) describe enzymes with fundamentally different topologies, sizes, and cofactor requirements that are clearly incompatible with the observed sequence features. Only option A is consistent with a type II membrane glycoprotein of ~580 AA bearing neuraminidase motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9WAF5 (HN_MUMPV, Mumps orthorubulavirus Hemagglutinin-neuraminidase, EC 3.2.1.18) matches the supplied 582-aa sequence exactly (SHA-256 confirmed). The catalytic activity annotation (C5, H4) is stated verbatim as option A, supported by experimental evidence (ECO:0000269|PubMed:39088577). The sequence comparison is 'matched' in both current and historical snapshots.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a type II membrane protein topology: an N-terminal signal peptide (MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQ) immediately followed by a hydrophobic transmembrane anchor. This topology is characteristic of paramyxovirus HN and F surface glycoproteins. The total length (~582 AA) matches paramyxovirus HN (influenza NA is ~470 AA; bacterial sialidases are typically soluble). In the C-terminal domain, the conserved 'RLLYY' motif (part of the neuraminidase active site in paramyxovirus HN) is clearly present, along with the characteristic C-terminal domain architecture of paramyxovirus neuraminidases. These features collectively identify the protein as a viral neuraminidase/sialidase (option A). Option B (taurine dioxygenase) requires Fe-S cluster motifs and is a small soluble enzyme. Option C (lipoxygenase-like) requires a different domain architecture and is typically >700 AA. Option D (fucose dehydrogenase) requires a Rossmann-fold NAD-binding motif (GxGxxG) and is a soluble cytoplasmic enzyme. None of these features are present. The type II membrane topology + ~580 AA length + RLLYY neuraminidase motif is a family-level pattern transferable from knowledge of other paramyxovirus HN proteins (NDV, measles, human parainfluenza) that meaningfully distinguishes A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the type II membrane protein topology, the characteristic length, and the conserved neuraminidase catalytic motifs (RLLYY) from general knowledge of paramyxovirus HN proteins (e.g., NDV HN, measles HN). These family-level features are sufficient to select the sialidase/neuraminidase option over the three non-membrane, non-sialidase alternatives without recalling the specific UniProt entry for mumps HN."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B, C, D) describe enzymes with fundamentally different topologies, sizes, and cofactor requirements that are clearly incompatible with the observed sequence features. Only option A is consistent with a type II membrane glycoprotein of ~580 AA bearing neuraminidase motifs."
  },
  "important_caveats": [
    "The 'NPPY' catalytic tetrad characteristic of NDV HN is not perfectly conserved in mumps HN; however, the RLLYY motif and overall domain architecture are sufficient for family-level identification.",
    "The evidence for EC 3.2.1.18 assignment is experimental (PubMed:39088577, 2024), which is relatively recent; older annotations of mumps HN neuraminidase activity were primarily based on sequence similarity to other paramyxovirus HN proteins.",
    "The reviewer-only evidence confirms the identity but was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable knowledge of paramyxovirus HN proteins."
  ]
}
```

</details>

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
  "requested_accession": "Q9WAF5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "903285284685ee37c0a70a6ba79dd624a84cc06b08d9bb4d3922857c63fe2e31",
  "benchmark_sequence_length": 582,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 132,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1999-11-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "current_source_sequence_sha256": "903285284685ee37c0a70a6ba79dd624a84cc06b08d9bb4d3922857c63fe2e31",
  "current_source_sequence_length": 582,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 130,
  "selected_historical_version": {
    "accession": "Q9WAF5",
    "database": "Swiss-Prot",
    "entryVersion": 130,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HN_MUMPV",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "selected_historical_source_sequence_sha256": "903285284685ee37c0a70a6ba79dd624a84cc06b08d9bb4d3922857c63fe2e31",
  "selected_historical_source_sequence_length": 582,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 130,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9WAF5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":132,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1999-11-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\"],\"scientificName\":\"Mumps orthorubulavirus\",\"taxonId\":2560602}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39088577\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.18\"}],\"fullName\":{\"value\":\"Hemagglutinin-neuraminidase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39088577\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9WAF5.json",
  "source_sha256": "f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508",
  "retrieved_utc": "2026-11-02T04:33:53.145631+00:00",
  "json_pointer": "/references/5",
  "excerpt": "{\"citation\":{\"authors\":[\"Takahashi T.\",\"Kurebayashi Y.\",\"Otsubo T.\",\"Ikeda K.\",\"Konagaya K.\",\"Suzuki S.\",\"Yamazaki M.\",\"Suzuki K.\",\"Narimichi Y.\",\"Minami A.\",\"Takeuchi H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39088577\"},{\"database\":\"DOI\",\"id\":\"10.1093/glycob/cwae059\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"39088577\",\"journal\":\"Glycobiology\",\"lastPage\":\"0\",\"publicationDate\":\"2024\",\"title\":\"Novel sialidase inhibitors suppress mumps virus replication and infection.\",\"volume\":\"34\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"13V165E2\"}],\"referenceNumber\":6,\"referencePositions\":[\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   HN_MUMPV                Reviewed;         582 AA.\nAC   Q9WAF5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-NOV-1999, sequence version 1.\nDT   28-JAN-2026, entry version 130.\nDE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000269|PubMed:39088577};\nGN   Name=HN {ECO:0000312|EMBL:BAG84572.1};\nOS   Mumps orthorubulavirus (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis.\nOX   NCBI_TaxID=2560602;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 130,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "source_locator": "lines 6-7",
  "excerpt": "DE   RecName: Full=Hemagglutinin-neuraminidase;\nDE            EC=3.2.1.18 {ECO:0000269|PubMed:39088577};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 130,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "source_locator": "lines 54-62",
  "excerpt": "RN   [6]\nRP   CATALYTIC ACTIVITY.\nRC   STRAIN=13V165E2;\nRX   PubMed=39088577; DOI=10.1093/glycob/cwae059;\nRA   Takahashi T., Kurebayashi Y., Otsubo T., Ikeda K., Konagaya K., Suzuki S.,\nRA   Yamazaki M., Suzuki K., Narimichi Y., Minami A., Takeuchi H.;\nRT   \"Novel sialidase inhibitors suppress mumps virus replication and\nRT   infection.\";\nRL   Glycobiology 34:0-0(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 130,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130",
  "source_sha256": "eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7",
  "retrieved_utc": "2026-11-02T04:33:57.899829+00:00",
  "source_locator": "lines 93-98",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-\nCC         (2->8)- glycosidic linkages of terminal sialic acid residues in\nCC         oligosaccharides, glycoproteins, glycolipids, colominic acid and\nCC         synthetic substrates.; EC=3.2.1.18;\nCC         Evidence={ECO:0000269|PubMed:39088577};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 130,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
