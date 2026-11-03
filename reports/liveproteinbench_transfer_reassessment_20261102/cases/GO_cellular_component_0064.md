# GO_cellular_component_0064: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0064.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **C** — plasma membrane

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
MQTATALEDSANAPSPAASSQGQFDREIVPIDTADAGNSTKRSPLKVALIMVALCCAVFLHALDNTIITTALPTITAAFDLDAAYTWIGSTYLLAVAASTMVWAKISDVFGRKPIILSANLCFFTGSLIAALSANFAMLIAARAIQGIGGAGVNVLANICVGDLFSQRKRGLYYGVIGGVWAVALSLGPVVGGSLTESISWRWCFYINLPLCAVVFVIIILLLDVKTPKTPFGKGIAAIDWVGAALSIGSTLMILLALSLGGQTEPWNSATVICLVVFGFIGWILCFSWEASLAKYPLLPVSIFKQIPTLAVLAACFIQSYAFVASAYYLPLYFQAVLGATPILSGVYLLPTAVSISISSTATGVYMRKTGQYLTPIYIGFVLQTLGYGLFIDLGPTANWAKIIVFQIIGGLGVGFNFQAPMVALQAFISPRELAMATSAYNFMRNVSGAISVVIGQTVFQNEMSKHQESLATILGPQLAAKLAGTGASASTDLIRSLPSPQRDVVHGVFANSMKSMWIMYTAFSAAALVVCPFLGKMVLREDHTETVTGLAAENAAREERLRQEKEKKDAKIRKCQVN

[Multiple Choices]
A. heterotrimeric G-protein complex
B. food vacuole
C. plasma membrane
D. cell outer membrane
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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a UniProt entry with a plasma-membrane GO annotation, but that annotation is computational (IEA:TreeGrafter), not direct experimental localization evidence. The entry also predicts only a multipass membrane location, which is consistent with but does not independently establish the plasma membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic stretches support a multipass membrane protein and make a heterotrimeric G-protein complex a poor fit. They do not, by themselves, identify which membrane the protein occupies.


**Missing item-specific fact**

> The sequence-specific localization annotation or other protein-specific evidence distinguishing plasma membrane from an internal membrane such as a food-vacuole membrane.


**Reason**

> The supplied sequence supports membrane association, but choosing the primary compartment requires a localization fact not supplied in the question. Recognizing the exact sequence or consulting its annotation would supply that fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> From the supplied sequence alone, a multipass transporter could be at the plasma membrane or an internal membrane; the sequence does not establish the specific destination. The other choices are less consistent with the predicted protein architecture.


### Important caveats

- The supporting plasma-membrane annotation is computational, not experimental.
- Reviewer-only evidence identifies this sequence as a fungal MFS-type transporter, but that identity and organism are not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic stretches support a multipass membrane protein and make a heterotrimeric G-protein complex a poor fit. They do not, by themselves, identify which membrane the protein occupies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific localization annotation or other protein-specific evidence distinguishing plasma membrane from an internal membrane such as a food-vacuole membrane.",
    "reason": "The supplied sequence supports membrane association, but choosing the primary compartment requires a localization fact not supplied in the question. Recognizing the exact sequence or consulting its annotation would supply that fact."
  },
  "case_id": "GO_cellular_component_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry with a plasma-membrane GO annotation, but that annotation is computational (IEA:TreeGrafter), not direct experimental localization evidence. The entry also predicts only a multipass membrane location, which is consistent with but does not independently establish the plasma membrane."
  },
  "important_caveats": [
    "The supporting plasma-membrane annotation is computational, not experimental.",
    "Reviewer-only evidence identifies this sequence as a fungal MFS-type transporter, but that identity and organism are not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "From the supplied sequence alone, a multipass transporter could be at the plasma membrane or an internal membrane; the sequence does not establish the specific destination. The other choices are less consistent with the predicted protein architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry with a plasma-membrane GO annotation, but that annotation is computational (IEA:TreeGrafter), not direct experimental localization evidence. The entry also predicts only a multipass membrane location, which is consistent with but does not independently establish the plasma membrane.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic stretches support a multipass membrane protein and make a heterotrimeric G-protein complex a poor fit. They do not, by themselves, identify which membrane the protein occupies.",
    "missing_item_specific_fact": "The sequence-specific localization annotation or other protein-specific evidence distinguishing plasma membrane from an internal membrane such as a food-vacuole membrane.",
    "reason": "The supplied sequence supports membrane association, but choosing the primary compartment requires a localization fact not supplied in the question. Recognizing the exact sequence or consulting its annotation would supply that fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "From the supplied sequence alone, a multipass transporter could be at the plasma membrane or an internal membrane; the sequence does not establish the specific destination. The other choices are less consistent with the predicted protein architecture."
  },
  "important_caveats": [
    "The supporting plasma-membrane annotation is computational, not experimental.",
    "Reviewer-only evidence identifies this sequence as a fungal MFS-type transporter, but that identity and organism are not provided to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A455ZIM6) annotates this protein as a 'Multi-pass membrane protein' (ECO:0000255, computational) and assigns GO:0005886 (plasma membrane) via IEA:TreeGrafter. The protein is identified as an MFS-type transporter (ppz2) from Metarhizium majus, a fungus. MFS transporters are multi-pass membrane proteins, and the GO plasma membrane assignment, while computational (TreeGrafter), is consistent with the known biology of MFS transporters in fungi. The answer is supported by database annotation, though the evidence is computational rather than experimental.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains approximately 12 long hydrophobic stretches (~20-25 residues each) characteristic of a multi-pass membrane transporter. This topology eliminates option A (heterotrimeric G-protein complex is a peripheral membrane complex, not a multi-pass membrane protein; its subunits have distinct folds like GTPase domains or WD40 repeats). Option B (food vacuole) is defined in GO as specific to Apicomplexa parasites, not a general fungal compartment. Option D (cell outer membrane) is explicitly defined as a prokaryotic structure enriched in lipopolysaccharide (GO:0009279 is in goslim_prokaryote). By elimination of these three clearly incompatible options, and given that multi-pass membrane transporters in eukaryotes most commonly reside at the plasma membrane, option C is the most defensible choice.


**Missing item-specific fact**

> None critical. The precise distinction between plasma membrane and internal membranes (ER, Golgi, vacuolar membrane) for MFS transporters could benefit from experimental localization data, but the four choices are sufficiently distinct that the answer is reachable by elimination using general biological knowledge.


**Reason**

> The multi-pass membrane topology is directly readable from the hydrophobic segments in the sequence. The three distractors are eliminable through general biological knowledge: G-protein complexes are not multi-pass membrane proteins, food vacuoles are Apicomplexan-specific, and cell outer membranes are prokaryotic structures. This leaves plasma membrane as the only viable option for a eukaryotic multi-pass membrane transporter.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct biological categories (peripheral protein complex, parasite-specific organelle, eukaryotic plasma membrane, prokaryotic outer membrane). The multi-pass membrane topology visible in the sequence, combined with general knowledge about these compartments, cleanly distinguishes C from A, B, and D. No two options are equally defensible given the sequence features.


### Important caveats

- The GO:plasma membrane annotation is IEA:TreeGrafter (computational phylogenetic transfer), not experimental localization data. The UniProt subcellular location simply states 'Membrane; Multi-pass membrane protein' without specifying which membrane.
- MFS transporters can occasionally localize to internal membranes (e.g., vacuolar, ER). The plasma membrane assignment, while the most common and default location for MFS transporters in fungi, is not experimentally confirmed for this specific protein.
- The organism (Metarhizium majus, a fungus) is not stated in the question input. Eliminating option D (prokaryotic cell outer membrane) requires either recognizing fungal sequence characteristics or applying general knowledge that the sequence lacks bacterial-specific features.
- The UniProt entry was first public in 2025-02-05, which may postdate the benchmark construction. The sequence match is confirmed, but the annotation available to the question author may have differed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains approximately 12 long hydrophobic stretches (~20-25 residues each) characteristic of a multi-pass membrane transporter. This topology eliminates option A (heterotrimeric G-protein complex is a peripheral membrane complex, not a multi-pass membrane protein; its subunits have distinct folds like GTPase domains or WD40 repeats). Option B (food vacuole) is defined in GO as specific to Apicomplexa parasites, not a general fungal compartment. Option D (cell outer membrane) is explicitly defined as a prokaryotic structure enriched in lipopolysaccharide (GO:0009279 is in goslim_prokaryote). By elimination of these three clearly incompatible options, and given that multi-pass membrane transporters in eukaryotes most commonly reside at the plasma membrane, option C is the most defensible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The precise distinction between plasma membrane and internal membranes (ER, Golgi, vacuolar membrane) for MFS transporters could benefit from experimental localization data, but the four choices are sufficiently distinct that the answer is reachable by elimination using general biological knowledge.",
    "reason": "The multi-pass membrane topology is directly readable from the hydrophobic segments in the sequence. The three distractors are eliminable through general biological knowledge: G-protein complexes are not multi-pass membrane proteins, food vacuoles are Apicomplexan-specific, and cell outer membranes are prokaryotic structures. This leaves plasma membrane as the only viable option for a eukaryotic multi-pass membrane transporter."
  },
  "case_id": "GO_cellular_component_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A455ZIM6) annotates this protein as a 'Multi-pass membrane protein' (ECO:0000255, computational) and assigns GO:0005886 (plasma membrane) via IEA:TreeGrafter. The protein is identified as an MFS-type transporter (ppz2) from Metarhizium majus, a fungus. MFS transporters are multi-pass membrane proteins, and the GO plasma membrane assignment, while computational (TreeGrafter), is consistent with the known biology of MFS transporters in fungi. The answer is supported by database annotation, though the evidence is computational rather than experimental."
  },
  "important_caveats": [
    "The GO:plasma membrane annotation is IEA:TreeGrafter (computational phylogenetic transfer), not experimental localization data. The UniProt subcellular location simply states 'Membrane; Multi-pass membrane protein' without specifying which membrane.",
    "MFS transporters can occasionally localize to internal membranes (e.g., vacuolar, ER). The plasma membrane assignment, while the most common and default location for MFS transporters in fungi, is not experimentally confirmed for this specific protein.",
    "The organism (Metarhizium majus, a fungus) is not stated in the question input. Eliminating option D (prokaryotic cell outer membrane) requires either recognizing fungal sequence characteristics or applying general knowledge that the sequence lacks bacterial-specific features.",
    "The UniProt entry was first public in 2025-02-05, which may postdate the benchmark construction. The sequence match is confirmed, but the annotation available to the question author may have differed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct biological categories (peripheral protein complex, parasite-specific organelle, eukaryotic plasma membrane, prokaryotic outer membrane). The multi-pass membrane topology visible in the sequence, combined with general knowledge about these compartments, cleanly distinguishes C from A, B, and D. No two options are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A455ZIM6) annotates this protein as a 'Multi-pass membrane protein' (ECO:0000255, computational) and assigns GO:0005886 (plasma membrane) via IEA:TreeGrafter. The protein is identified as an MFS-type transporter (ppz2) from Metarhizium majus, a fungus. MFS transporters are multi-pass membrane proteins, and the GO plasma membrane assignment, while computational (TreeGrafter), is consistent with the known biology of MFS transporters in fungi. The answer is supported by database annotation, though the evidence is computational rather than experimental.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains approximately 12 long hydrophobic stretches (~20-25 residues each) characteristic of a multi-pass membrane transporter. This topology eliminates option A (heterotrimeric G-protein complex is a peripheral membrane complex, not a multi-pass membrane protein; its subunits have distinct folds like GTPase domains or WD40 repeats). Option B (food vacuole) is defined in GO as specific to Apicomplexa parasites, not a general fungal compartment. Option D (cell outer membrane) is explicitly defined as a prokaryotic structure enriched in lipopolysaccharide (GO:0009279 is in goslim_prokaryote). By elimination of these three clearly incompatible options, and given that multi-pass membrane transporters in eukaryotes most commonly reside at the plasma membrane, option C is the most defensible choice.",
    "missing_item_specific_fact": "None critical. The precise distinction between plasma membrane and internal membranes (ER, Golgi, vacuolar membrane) for MFS transporters could benefit from experimental localization data, but the four choices are sufficiently distinct that the answer is reachable by elimination using general biological knowledge.",
    "reason": "The multi-pass membrane topology is directly readable from the hydrophobic segments in the sequence. The three distractors are eliminable through general biological knowledge: G-protein complexes are not multi-pass membrane proteins, food vacuoles are Apicomplexan-specific, and cell outer membranes are prokaryotic structures. This leaves plasma membrane as the only viable option for a eukaryotic multi-pass membrane transporter."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct biological categories (peripheral protein complex, parasite-specific organelle, eukaryotic plasma membrane, prokaryotic outer membrane). The multi-pass membrane topology visible in the sequence, combined with general knowledge about these compartments, cleanly distinguishes C from A, B, and D. No two options are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The GO:plasma membrane annotation is IEA:TreeGrafter (computational phylogenetic transfer), not experimental localization data. The UniProt subcellular location simply states 'Membrane; Multi-pass membrane protein' without specifying which membrane.",
    "MFS transporters can occasionally localize to internal membranes (e.g., vacuolar, ER). The plasma membrane assignment, while the most common and default location for MFS transporters in fungi, is not experimentally confirmed for this specific protein.",
    "The organism (Metarhizium majus, a fungus) is not stated in the question input. Eliminating option D (prokaryotic cell outer membrane) requires either recognizing fungal sequence characteristics or applying general knowledge that the sequence lacks bacterial-specific features.",
    "The UniProt entry was first public in 2025-02-05, which may postdate the benchmark construction. The sequence match is confirmed, but the annotation available to the question author may have differed."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns plasma membrane by IEA:TreeGrafter, and also describes the protein as a computationally annotated multipass membrane protein. This supports the key, though the cited localization is computational rather than experimental and the broader membrane annotation alone does not establish the precise membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains many hydrophobic segments consistent with a multipass transporter, unlike a heterotrimeric G-protein complex, whose components are not such a multipass transporter. Transferable knowledge of eukaryotic membrane transporters makes plasma membrane a credible choice. A cell outer membrane is characteristic of particular prokaryotic envelopes, while a food vacuole is a specialized compartment not suggested by this sequence or the choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The membrane-protein pattern and biological distinctions among the offered choices provide a meaningful basis for selecting plasma membrane without needing the exact protein's database annotation. The sequence alone does not prove its precise membrane destination, so this is a plausible comparative inference rather than certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although multipass topology alone cannot prove plasma-membrane localization, none of the other offered choices is comparably supported by the sequence and general biology.


### Important caveats

- The supplied GO plasma-membrane annotation is computationally inferred (IEA:TreeGrafter), not experimental evidence.
- A multipass membrane sequence does not by itself distinguish the plasma membrane from all intracellular membranes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains many hydrophobic segments consistent with a multipass transporter, unlike a heterotrimeric G-protein complex, whose components are not such a multipass transporter. Transferable knowledge of eukaryotic membrane transporters makes plasma membrane a credible choice. A cell outer membrane is characteristic of particular prokaryotic envelopes, while a food vacuole is a specialized compartment not suggested by this sequence or the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The membrane-protein pattern and biological distinctions among the offered choices provide a meaningful basis for selecting plasma membrane without needing the exact protein's database annotation. The sequence alone does not prove its precise membrane destination, so this is a plausible comparative inference rather than certainty."
  },
  "case_id": "GO_cellular_component_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns plasma membrane by IEA:TreeGrafter, and also describes the protein as a computationally annotated multipass membrane protein. This supports the key, though the cited localization is computational rather than experimental and the broader membrane annotation alone does not establish the precise membrane."
  },
  "important_caveats": [
    "The supplied GO plasma-membrane annotation is computationally inferred (IEA:TreeGrafter), not experimental evidence.",
    "A multipass membrane sequence does not by itself distinguish the plasma membrane from all intracellular membranes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although multipass topology alone cannot prove plasma-membrane localization, none of the other offered choices is comparably supported by the sequence and general biology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns plasma membrane by IEA:TreeGrafter, and also describes the protein as a computationally annotated multipass membrane protein. This supports the key, though the cited localization is computational rather than experimental and the broader membrane annotation alone does not establish the precise membrane.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains many hydrophobic segments consistent with a multipass transporter, unlike a heterotrimeric G-protein complex, whose components are not such a multipass transporter. Transferable knowledge of eukaryotic membrane transporters makes plasma membrane a credible choice. A cell outer membrane is characteristic of particular prokaryotic envelopes, while a food vacuole is a specialized compartment not suggested by this sequence or the choices.",
    "missing_item_specific_fact": "",
    "reason": "The membrane-protein pattern and biological distinctions among the offered choices provide a meaningful basis for selecting plasma membrane without needing the exact protein's database annotation. The sequence alone does not prove its precise membrane destination, so this is a plausible comparative inference rather than certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although multipass topology alone cannot prove plasma-membrane localization, none of the other offered choices is comparably supported by the sequence and general biology."
  },
  "important_caveats": [
    "The supplied GO plasma-membrane annotation is computationally inferred (IEA:TreeGrafter), not experimental evidence.",
    "A multipass membrane sequence does not by itself distinguish the plasma membrane from all intracellular membranes."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein as a multi-pass membrane protein (ECO:0000255, inferred by similarity) and assigns GO:0005886 (plasma membrane) via IEA:TreeGrafter. The protein is identified as an MFS-type transporter, a family well-known to reside in the plasma membrane. The evidence is computational (similarity-based and TreeGrafter inference) rather than experimental, but it does support the expected answer. The multi-pass alpha-helical membrane architecture visible in the sequence is consistent with this annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 579-aa sequence contains approximately 12+ hydrophobic segments of 20-25 residues each, characteristic of a multi-pass alpha-helical membrane transporter (e.g., MFS, ABC, or similar families). This architecture immediately distinguishes the options: (1) A heterotrimeric G-protein complex subunit (Gα ~350-400 aa with GTPase domain, Gβ ~340 aa with WD40 repeats, Gγ ~70 aa) has a completely different size and fold — ruled out. (2) A food vacuole is a parasite-specific digestive compartment (Apicomplexa); no vacuolar targeting signals are present, and multi-pass transporters are not food-vacuole residents — ruled out. (3) 'Cell outer membrane' (GO:0009279) is defined as the LPS-enriched outermost membrane of the prokaryotic cell envelope; outer membrane proteins are beta-barrels, not multi-pass alpha-helical proteins — ruled out by architecture. (4) Plasma membrane is the canonical location for multi-pass alpha-helical transporters in both prokaryotic (inner/plasma membrane) and eukaryotic cells. The absence of a cleavable signal peptide and the presence of a short C-terminal cytoplasmic tail further support plasma membrane residency. Thus, transferable knowledge of membrane protein families and GO term definitions meaningfully selects C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobicity pattern (12+ TM helices, alpha-helical topology) combined with knowledge that MFS/ABC-type multi-pass transporters localize to the plasma membrane, that G-protein subunits have entirely different architectures, that food vacuoles are parasite-specific, and that 'cell outer membrane' is a prokaryotic LPS-containing beta-barrel compartment, provides a concrete and credible inference chain to select plasma membrane without needing the specific UniProt record for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated by protein architecture and GO term definitions. Multi-pass alpha-helical membrane proteins are inconsistent with G-protein subunits (wrong fold/size), food vacuoles (wrong compartment, parasite-specific), and the prokaryotic outer membrane (beta-barrel, LPS-enriched). No two options are genuinely defensible for this sequence.


### Important caveats

- The UniProt plasma membrane annotation is based on computational inference (IEA:TreeGrafter and ECO:0000255 similarity), not direct experimental localization. The actual subcellular distribution of ppz2 in Metarhizium has not been experimentally confirmed in the provided evidence.
- The specific identification as an MFS-type transporter requires either sequence-family recognition or the UniProt record; however, the general multi-pass alpha-helical transporter architecture is discernible from hydrophobicity analysis alone.
- The organism (a fungus) is not stated in the original input; the reasoning that rules out 'cell outer membrane' relies on the GO definition (prokaryotic-specific) rather than organism knowledge, so this remains valid from sequence features alone (alpha-helical vs. beta-barrel architecture).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 579-aa sequence contains approximately 12+ hydrophobic segments of 20-25 residues each, characteristic of a multi-pass alpha-helical membrane transporter (e.g., MFS, ABC, or similar families). This architecture immediately distinguishes the options: (1) A heterotrimeric G-protein complex subunit (Gα ~350-400 aa with GTPase domain, Gβ ~340 aa with WD40 repeats, Gγ ~70 aa) has a completely different size and fold — ruled out. (2) A food vacuole is a parasite-specific digestive compartment (Apicomplexa); no vacuolar targeting signals are present, and multi-pass transporters are not food-vacuole residents — ruled out. (3) 'Cell outer membrane' (GO:0009279) is defined as the LPS-enriched outermost membrane of the prokaryotic cell envelope; outer membrane proteins are beta-barrels, not multi-pass alpha-helical proteins — ruled out by architecture. (4) Plasma membrane is the canonical location for multi-pass alpha-helical transporters in both prokaryotic (inner/plasma membrane) and eukaryotic cells. The absence of a cleavable signal peptide and the presence of a short C-terminal cytoplasmic tail further support plasma membrane residency. Thus, transferable knowledge of membrane protein families and GO term definitions meaningfully selects C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity pattern (12+ TM helices, alpha-helical topology) combined with knowledge that MFS/ABC-type multi-pass transporters localize to the plasma membrane, that G-protein subunits have entirely different architectures, that food vacuoles are parasite-specific, and that 'cell outer membrane' is a prokaryotic LPS-containing beta-barrel compartment, provides a concrete and credible inference chain to select plasma membrane without needing the specific UniProt record for this protein."
  },
  "case_id": "GO_cellular_component_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein as a multi-pass membrane protein (ECO:0000255, inferred by similarity) and assigns GO:0005886 (plasma membrane) via IEA:TreeGrafter. The protein is identified as an MFS-type transporter, a family well-known to reside in the plasma membrane. The evidence is computational (similarity-based and TreeGrafter inference) rather than experimental, but it does support the expected answer. The multi-pass alpha-helical membrane architecture visible in the sequence is consistent with this annotation."
  },
  "important_caveats": [
    "The UniProt plasma membrane annotation is based on computational inference (IEA:TreeGrafter and ECO:0000255 similarity), not direct experimental localization. The actual subcellular distribution of ppz2 in Metarhizium has not been experimentally confirmed in the provided evidence.",
    "The specific identification as an MFS-type transporter requires either sequence-family recognition or the UniProt record; however, the general multi-pass alpha-helical transporter architecture is discernible from hydrophobicity analysis alone.",
    "The organism (a fungus) is not stated in the original input; the reasoning that rules out 'cell outer membrane' relies on the GO definition (prokaryotic-specific) rather than organism knowledge, so this remains valid from sequence features alone (alpha-helical vs. beta-barrel architecture)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by protein architecture and GO term definitions. Multi-pass alpha-helical membrane proteins are inconsistent with G-protein subunits (wrong fold/size), food vacuoles (wrong compartment, parasite-specific), and the prokaryotic outer membrane (beta-barrel, LPS-enriched). No two options are genuinely defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein as a multi-pass membrane protein (ECO:0000255, inferred by similarity) and assigns GO:0005886 (plasma membrane) via IEA:TreeGrafter. The protein is identified as an MFS-type transporter, a family well-known to reside in the plasma membrane. The evidence is computational (similarity-based and TreeGrafter inference) rather than experimental, but it does support the expected answer. The multi-pass alpha-helical membrane architecture visible in the sequence is consistent with this annotation.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 579-aa sequence contains approximately 12+ hydrophobic segments of 20-25 residues each, characteristic of a multi-pass alpha-helical membrane transporter (e.g., MFS, ABC, or similar families). This architecture immediately distinguishes the options: (1) A heterotrimeric G-protein complex subunit (Gα ~350-400 aa with GTPase domain, Gβ ~340 aa with WD40 repeats, Gγ ~70 aa) has a completely different size and fold — ruled out. (2) A food vacuole is a parasite-specific digestive compartment (Apicomplexa); no vacuolar targeting signals are present, and multi-pass transporters are not food-vacuole residents — ruled out. (3) 'Cell outer membrane' (GO:0009279) is defined as the LPS-enriched outermost membrane of the prokaryotic cell envelope; outer membrane proteins are beta-barrels, not multi-pass alpha-helical proteins — ruled out by architecture. (4) Plasma membrane is the canonical location for multi-pass alpha-helical transporters in both prokaryotic (inner/plasma membrane) and eukaryotic cells. The absence of a cleavable signal peptide and the presence of a short C-terminal cytoplasmic tail further support plasma membrane residency. Thus, transferable knowledge of membrane protein families and GO term definitions meaningfully selects C.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity pattern (12+ TM helices, alpha-helical topology) combined with knowledge that MFS/ABC-type multi-pass transporters localize to the plasma membrane, that G-protein subunits have entirely different architectures, that food vacuoles are parasite-specific, and that 'cell outer membrane' is a prokaryotic LPS-containing beta-barrel compartment, provides a concrete and credible inference chain to select plasma membrane without needing the specific UniProt record for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by protein architecture and GO term definitions. Multi-pass alpha-helical membrane proteins are inconsistent with G-protein subunits (wrong fold/size), food vacuoles (wrong compartment, parasite-specific), and the prokaryotic outer membrane (beta-barrel, LPS-enriched). No two options are genuinely defensible for this sequence."
  },
  "important_caveats": [
    "The UniProt plasma membrane annotation is based on computational inference (IEA:TreeGrafter and ECO:0000255 similarity), not direct experimental localization. The actual subcellular distribution of ppz2 in Metarhizium has not been experimentally confirmed in the provided evidence.",
    "The specific identification as an MFS-type transporter requires either sequence-family recognition or the UniProt record; however, the general multi-pass alpha-helical transporter architecture is discernible from hydrophobicity analysis alone.",
    "The organism (a fungus) is not stated in the original input; the reasoning that rules out 'cell outer membrane' relies on the GO definition (prokaryotic-specific) rather than organism knowledge, so this remains valid from sequence features alone (alpha-helical vs. beta-barrel architecture)."
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
  "requested_accession": "A0A455ZIM6",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "351b6c74b4c2221103ffe06ad649dd3d536e0edd19c3a314131076b2cd6dfa5d",
  "benchmark_sequence_length": 579,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "current_source_sequence_sha256": "351b6c74b4c2221103ffe06ad649dd3d536e0edd19c3a314131076b2cd6dfa5d",
  "current_source_sequence_length": 579,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 20,
  "selected_historical_version": {
    "accession": "A0A455ZIM6",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_03/2026_03",
    "lastReleaseDate": "02-Sep-2026",
    "name": "PPZ2_METMF",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "selected_historical_source_sequence_sha256": "351b6c74b4c2221103ffe06ad649dd3d536e0edd19c3a314131076b2cd6dfa5d",
  "selected_historical_source_sequence_length": 579,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 20,
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A455ZIM6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein 2\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"MFS-type transporter ppz2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-0162\",\"value\":\"Membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   PPZ2_METMF              Reviewed;         579 AA.\nAC   A0A455ZIM6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=MFS-type transporter ppz2 {ECO:0000303|PubMed:30452111};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein 2 {ECO:0000303|PubMed:30452111};\nGN   Name=ppz2 {ECO:0000303|PubMed:38578094};\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 20,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "source_locator": "lines 14-22",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 20,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "source_locator": "lines 23-29",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND PATHWAY.\nRX   PubMed=38578094; DOI=10.1021/jacs.4c01419;\nRA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;\nRT   \"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ\nRT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\";\nRL   J. Am. Chem. Soc. 146:10263-10267(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 20,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "source_locator": "lines 36-37",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Multi-pass membrane\nCC       protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 20,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "source_locator": "lines 47-47",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 20,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 59981-59994",
  "excerpt": "[Term]\nid: GO:0005834\nname: heterotrimeric G-protein complex\nnamespace: cellular_component\ndef: \"Any of a family of heterotrimeric GTP-binding and hydrolyzing proteins; they belong to a superfamily of GTPases that includes monomeric proteins such as EF-Tu and RAS. Heterotrimeric G-proteins consist of three subunits; the alpha subunit contains the guanine nucleotide binding site and possesses GTPase activity; the beta and gamma subunits are tightly associated and function as a beta-gamma heterodimer; extrinsic plasma membrane proteins (cytoplasmic face) that function as a complex to transduce signals from G protein-coupled receptors to an effector protein.\" [ISBN:0198547684]\ncomment: See also the molecular function term 'G protein-coupled receptor activity ; GO:0004930'.\nsynonym: \"heterotrimeric G-protein GTPase activity\" RELATED []\nsynonym: \"heterotrimeric G-protein GTPase, alpha-subunit\" NARROW []\nsynonym: \"heterotrimeric G-protein GTPase, beta-subunit\" NARROW []\nsynonym: \"heterotrimeric G-protein GTPase, gamma-subunit\" NARROW []\nis_a: GO:0098797 ! plasma membrane protein complex\nis_a: GO:1905360 ! GTPase complex\nrelationship: part_of GO:0031234 ! extrinsic component of cytoplasmic side of plasma membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005834"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 60420-60454",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005886"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 94785-94797",
  "excerpt": "[Term]\nid: GO:0009279\nname: cell outer membrane\nnamespace: cellular_component\ndef: \"A lipid bilayer that forms the outermost membrane of the cell envelope; enriched in polysaccharide and protein; the outer leaflet of the membrane contains specific lipopolysaccharide structures.\" [GOC:md, GOC:mtg_sensu, ISBN:0135712254]\ncomment: To annotate the plasma (cytoplasmic) membrane, see instead GO:0005886.\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsynonym: \"outer membrane of cell\" EXACT []\nis_a: GO:0019867 ! outer membrane\nis_a: GO:0030312 ! external encapsulating structure\nrelationship: part_of GO:0030313 ! cell envelope\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0009279"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 155270-155278",
  "excerpt": "[Term]\nid: GO:0020020\nname: food vacuole\nnamespace: cellular_component\nalt_id: GO:0005772\ndef: \"Vacuole within a parasite used for digestion of the host cell cytoplasm. An example of this component is found in the Apicomplexa.\" [GOC:mb]\nsynonym: \"digestive vacuole\" EXACT []\nis_a: GO:0032010 ! phagolysosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0020020"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
