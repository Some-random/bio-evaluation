# GO_molecular_function_0175: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0175.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **B** — nucleoside transmembrane transporter activity

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
MSLKGGTAAPAPMAPPRKWYDMTSAEFYVYVVAFMCGISIMMPINAVFSAPSYMLEYYLYATKDPFLVPKMTNFWTNVMTYYNLISMVTSLVVEPLTLLKSFRKIPMLVRLLGGLSVLIIEIIVLMVVPARGTTEAGAVATMCIAGFIGGLGTSIFESTVYGMFGAFPPSFTSIMMGGVGISGVLTSLIQIIVKAALPDTYEGVKKQSYIYYSLDVGIQAATFIALIMMRFNSFAQLHFGDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY

[Multiple Choices]
A. DNA-binding transcription activator activity
B. nucleoside transmembrane transporter activity
C. RNA polymerase II transcription regulatory region sequence-specific DNA binding
D. cardiolipin synthase (CMP-forming)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the reviewed Crithidia fasciculata nucleoside transporter entry. That entry reports experimentally supported nucleoside transport, including adenosine transport, and assigns the matching GO term. This supports B for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C11](#evidence-c11), [H5](#evidence-h5), [H11](#evidence-h11).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments suggest a multipass membrane protein and make the transcription-related choices poor fits, but that feature alone does not establish nucleoside transport over another membrane-protein function such as cardiolipin synthesis.


**Missing item-specific fact**

> The protein's specific family identity or experimentally established substrate/function is needed to distinguish nucleoside transport from the other membrane-associated option.


**Reason**

> The reviewer evidence supports B, but the model input supplies only the sequence and choices. Generic topology is not sufficiently specific to establish the transported substrate or reliably exclude the membrane-enzyme distractor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-specific annotation and experimental evidence support B; no other listed option is supported by the supplied reviewer evidence.


### Important caveats

- The experimental annotation and accession match are reviewer-only evidence, not information supplied to the evaluated model.
- The sequence's multipass topology supports a membrane-protein inference but does not by itself prove nucleoside specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments suggest a multipass membrane protein and make the transcription-related choices poor fits, but that feature alone does not establish nucleoside transport over another membrane-protein function such as cardiolipin synthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific family identity or experimentally established substrate/function is needed to distinguish nucleoside transport from the other membrane-associated option.",
    "reason": "The reviewer evidence supports B, but the model input supplies only the sequence and choices. Generic topology is not sufficiently specific to establish the transported substrate or reliably exclude the membrane-enzyme distractor."
  },
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C11",
      "H5",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Crithidia fasciculata nucleoside transporter entry. That entry reports experimentally supported nucleoside transport, including adenosine transport, and assigns the matching GO term. This supports B for this sequence."
  },
  "important_caveats": [
    "The experimental annotation and accession match are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence's multipass topology supports a membrane-protein inference but does not by itself prove nucleoside specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-specific annotation and experimental evidence support B; no other listed option is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Crithidia fasciculata nucleoside transporter entry. That entry reports experimentally supported nucleoside transport, including adenosine transport, and assigns the matching GO term. This supports B for this sequence.",
    "evidence_ids": ["C1", "C5", "C6", "C11", "H5", "H11"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments suggest a multipass membrane protein and make the transcription-related choices poor fits, but that feature alone does not establish nucleoside transport over another membrane-protein function such as cardiolipin synthesis.",
    "missing_item_specific_fact": "The protein's specific family identity or experimentally established substrate/function is needed to distinguish nucleoside transport from the other membrane-associated option.",
    "reason": "The reviewer evidence supports B, but the model input supplies only the sequence and choices. Generic topology is not sufficiently specific to establish the transported substrate or reliably exclude the membrane-enzyme distractor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-specific annotation and experimental evidence support B; no other listed option is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The experimental annotation and accession match are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence's multipass topology supports a membrane-protein inference but does not by itself prove nucleoside specificity."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9GTP5 (NT1_CRIFA) is experimentally characterized (ECO:0000269, direct assay) as 'Nucleoside transporter 1' (CfNT1) from Crithidia fasciculata. The FUNCTION comment states it is a 'nucleoside transporter with broad substrate specificity' transporting adenosine, hypoxanthine, inosine, uridine, and cytidine across membranes. Multiple catalytic activity entries (adenosine(in)=adenosine(out), etc.) confirm transmembrane nucleoside transport. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (497 AA, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The provided 497-residue sequence contains approximately 11-12 hydrophobic segments consistent with multi-pass transmembrane domains, characteristic of membrane transporters (e.g., the equilibrative nucleoside transporter family). Options A (DNA-binding transcription activator) and C (RNA Pol II regulatory region DNA binding) describe soluble nuclear transcription-factor functions requiring DNA-binding domains (zinc fingers, helix-turn-helix, etc.) and nuclear localization signals—features entirely absent from this sequence. Option D (cardiolipin synthase, CMP-forming) is a transferase enzyme, typically a single-pass or peripheral membrane protein with specific catalytic motifs, not a multi-pass integral membrane protein. Only option B (nucleoside transmembrane transporter activity) is consistent with the observed multi-pass transmembrane architecture, making it the sole viable choice through general protein-architecture reasoning.


**Missing item-specific fact**

> None critical. While recognizing the specific ENT-family nucleoside transporter signature (vs. other transporter families) would require specialized knowledge, the question's option set contains only one transporter function, so the multi-pass TM architecture alone suffices to eliminate A, C, and D.


**Reason**

> The transmembrane topology of the sequence provides a concrete, general biological argument: a protein with ~11 TM helices cannot be a DNA-binding transcription factor or a soluble transferase enzyme. This eliminates three of four options without needing to identify the exact protein family. The remaining option B is the only transmembrane transporter function listed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different protein classes (transcription factor, membrane transporter, DNA-binding regulatory protein, transferase enzyme). The multi-pass transmembrane architecture of the sequence unambiguously points to a transporter, and only one option (B) describes a transmembrane transporter activity. No other option is defensible given the sequence architecture.


### Important caveats

- The GO annotation GO:0005337 carries evidence code IEA:InterPro (computational transfer), but the underlying function is experimentally validated via ECO:0000269 (direct assay) from three independent studies (PubMed:15694482, 20037157, 24120444).
- The protein is from Crithidia fasciculata, a trypanosomatid parasite; nucleoside transporters are well-studied in this organism due to their inability to synthesize purines de novo.
- Option D (cardiolipin synthase CMP-forming) has no matching GO term in the supplied ontology candidates, but this does not affect the reasoning since the sequence architecture already excludes it.
- The identity of the protein (Q9GTP5) was inferred from reviewer-only metadata absent from the model input; however, the sequence-architecture reasoning does not depend on this identification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The provided 497-residue sequence contains approximately 11-12 hydrophobic segments consistent with multi-pass transmembrane domains, characteristic of membrane transporters (e.g., the equilibrative nucleoside transporter family). Options A (DNA-binding transcription activator) and C (RNA Pol II regulatory region DNA binding) describe soluble nuclear transcription-factor functions requiring DNA-binding domains (zinc fingers, helix-turn-helix, etc.) and nuclear localization signals—features entirely absent from this sequence. Option D (cardiolipin synthase, CMP-forming) is a transferase enzyme, typically a single-pass or peripheral membrane protein with specific catalytic motifs, not a multi-pass integral membrane protein. Only option B (nucleoside transmembrane transporter activity) is consistent with the observed multi-pass transmembrane architecture, making it the sole viable choice through general protein-architecture reasoning.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While recognizing the specific ENT-family nucleoside transporter signature (vs. other transporter families) would require specialized knowledge, the question's option set contains only one transporter function, so the multi-pass TM architecture alone suffices to eliminate A, C, and D.",
    "reason": "The transmembrane topology of the sequence provides a concrete, general biological argument: a protein with ~11 TM helices cannot be a DNA-binding transcription factor or a soluble transferase enzyme. This eliminates three of four options without needing to identify the exact protein family. The remaining option B is the only transmembrane transporter function listed."
  },
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
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
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9GTP5 (NT1_CRIFA) is experimentally characterized (ECO:0000269, direct assay) as 'Nucleoside transporter 1' (CfNT1) from Crithidia fasciculata. The FUNCTION comment states it is a 'nucleoside transporter with broad substrate specificity' transporting adenosine, hypoxanthine, inosine, uridine, and cytidine across membranes. Multiple catalytic activity entries (adenosine(in)=adenosine(out), etc.) confirm transmembrane nucleoside transport. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (497 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The GO annotation GO:0005337 carries evidence code IEA:InterPro (computational transfer), but the underlying function is experimentally validated via ECO:0000269 (direct assay) from three independent studies (PubMed:15694482, 20037157, 24120444).",
    "The protein is from Crithidia fasciculata, a trypanosomatid parasite; nucleoside transporters are well-studied in this organism due to their inability to synthesize purines de novo.",
    "Option D (cardiolipin synthase CMP-forming) has no matching GO term in the supplied ontology candidates, but this does not affect the reasoning since the sequence architecture already excludes it.",
    "The identity of the protein (Q9GTP5) was inferred from reviewer-only metadata absent from the model input; however, the sequence-architecture reasoning does not depend on this identification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different protein classes (transcription factor, membrane transporter, DNA-binding regulatory protein, transferase enzyme). The multi-pass transmembrane architecture of the sequence unambiguously points to a transporter, and only one option (B) describes a transmembrane transporter activity. No other option is defensible given the sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9GTP5 (NT1_CRIFA) is experimentally characterized (ECO:0000269, direct assay) as 'Nucleoside transporter 1' (CfNT1) from Crithidia fasciculata. The FUNCTION comment states it is a 'nucleoside transporter with broad substrate specificity' transporting adenosine, hypoxanthine, inosine, uridine, and cytidine across membranes. Multiple catalytic activity entries (adenosine(in)=adenosine(out), etc.) confirm transmembrane nucleoside transport. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (497 AA, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The provided 497-residue sequence contains approximately 11-12 hydrophobic segments consistent with multi-pass transmembrane domains, characteristic of membrane transporters (e.g., the equilibrative nucleoside transporter family). Options A (DNA-binding transcription activator) and C (RNA Pol II regulatory region DNA binding) describe soluble nuclear transcription-factor functions requiring DNA-binding domains (zinc fingers, helix-turn-helix, etc.) and nuclear localization signals—features entirely absent from this sequence. Option D (cardiolipin synthase, CMP-forming) is a transferase enzyme, typically a single-pass or peripheral membrane protein with specific catalytic motifs, not a multi-pass integral membrane protein. Only option B (nucleoside transmembrane transporter activity) is consistent with the observed multi-pass transmembrane architecture, making it the sole viable choice through general protein-architecture reasoning.",
    "missing_item_specific_fact": "None critical. While recognizing the specific ENT-family nucleoside transporter signature (vs. other transporter families) would require specialized knowledge, the question's option set contains only one transporter function, so the multi-pass TM architecture alone suffices to eliminate A, C, and D.",
    "reason": "The transmembrane topology of the sequence provides a concrete, general biological argument: a protein with ~11 TM helices cannot be a DNA-binding transcription factor or a soluble transferase enzyme. This eliminates three of four options without needing to identify the exact protein family. The remaining option B is the only transmembrane transporter function listed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different protein classes (transcription factor, membrane transporter, DNA-binding regulatory protein, transferase enzyme). The multi-pass transmembrane architecture of the sequence unambiguously points to a transporter, and only one option (B) describes a transmembrane transporter activity. No other option is defensible given the sequence architecture."
  },
  "important_caveats": [
    "The GO annotation GO:0005337 carries evidence code IEA:InterPro (computational transfer), but the underlying function is experimentally validated via ECO:0000269 (direct assay) from three independent studies (PubMed:15694482, 20037157, 24120444).",
    "The protein is from Crithidia fasciculata, a trypanosomatid parasite; nucleoside transporters are well-studied in this organism due to their inability to synthesize purines de novo.",
    "Option D (cardiolipin synthase CMP-forming) has no matching GO term in the supplied ontology candidates, but this does not affect the reasoning since the sequence architecture already excludes it.",
    "The identity of the protein (Q9GTP5) was inferred from reviewer-only metadata absent from the model input; however, the sequence-architecture reasoning does not depend on this identification."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched protein record describes nucleoside transport and cites experimental evidence for transport of adenosine and other nucleosides; its GO annotation also assigns nucleoside transmembrane transporter activity. This supports choice B.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is dominated by long hydrophobic segments consistent with a multipass membrane protein. Transferable knowledge of equilibrative nucleoside transporter families makes nucleoside transport a credible inference from this architecture. That strongly favors B over the DNA-binding transcription functions in A and C; the sequence also does not suggest the catalytic cardiolipin synthase function in D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices make the family-level inference discriminating: a multipass transporter is a meaningful match for B, whereas A and C imply DNA-binding regulatory proteins. The sequence alone does not establish substrate specificity, but the alternatives do not require that finer distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered alternatives, B is the clear fit for a multipass nucleoside transporter.


### Important caveats

- The reviewer-only record supports the key but was not part of the original input; the answerability judgment rests on transferable sequence and family-level knowledge.
- Multipass topology alone cannot establish the exact transported substrates or experimentally confirm function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is dominated by long hydrophobic segments consistent with a multipass membrane protein. Transferable knowledge of equilibrative nucleoside transporter families makes nucleoside transport a credible inference from this architecture. That strongly favors B over the DNA-binding transcription functions in A and C; the sequence also does not suggest the catalytic cardiolipin synthase function in D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices make the family-level inference discriminating: a multipass transporter is a meaningful match for B, whereas A and C imply DNA-binding regulatory proteins. The sequence alone does not establish substrate specificity, but the alternatives do not require that finer distinction."
  },
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11"
    ],
    "judgment": "supported",
    "reason": "The matched protein record describes nucleoside transport and cites experimental evidence for transport of adenosine and other nucleosides; its GO annotation also assigns nucleoside transmembrane transporter activity. This supports choice B."
  },
  "important_caveats": [
    "The reviewer-only record supports the key but was not part of the original input; the answerability judgment rests on transferable sequence and family-level knowledge.",
    "Multipass topology alone cannot establish the exact transported substrates or experimentally confirm function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, B is the clear fit for a multipass nucleoside transporter."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein record describes nucleoside transport and cites experimental evidence for transport of adenosine and other nucleosides; its GO annotation also assigns nucleoside transmembrane transporter activity. This supports choice B.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is dominated by long hydrophobic segments consistent with a multipass membrane protein. Transferable knowledge of equilibrative nucleoside transporter families makes nucleoside transport a credible inference from this architecture. That strongly favors B over the DNA-binding transcription functions in A and C; the sequence also does not suggest the catalytic cardiolipin synthase function in D.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices make the family-level inference discriminating: a multipass transporter is a meaningful match for B, whereas A and C imply DNA-binding regulatory proteins. The sequence alone does not establish substrate specificity, but the alternatives do not require that finer distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, B is the clear fit for a multipass nucleoside transporter."
  },
  "important_caveats": [
    "The reviewer-only record supports the key but was not part of the original input; the answerability judgment rests on transferable sequence and family-level knowledge.",
    "Multipass topology alone cannot establish the exact transported substrates or experimentally confirm function."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9GTP5 is named 'Nucleoside transporter 1' (CfNT1) with experimental evidence (ECO:0000269, direct assay) from three independent PubMed studies demonstrating transport of adenosine, hypoxanthine, inosine, uridine, and cytidine. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (SHA-256 match, 497 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C11](#evidence-c11), [H5](#evidence-h5), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 497-residue sequence exhibits a clear multi-pass transmembrane topology: numerous hydrophobic stretches (~11-12 predicted TMs) interrupted by a large central hydrophilic loop (approximately residues 200-280: 'GDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY'). This 11-12 TM + large central loop architecture is the hallmark of the equilibrative nucleoside transporter (ENT/SLC29) family. This immediately eliminates options A and C (DNA-binding transcription factors require nuclear localization, DNA-binding motifs like zinc fingers or helix-turn-helix, and are not multi-pass membrane proteins). Option D (cardiolipin synthase, CMP-forming) belongs to the CDP-alcohol phosphatidyltransferase family, which has a distinct fold with fewer (~6-8) TMs and catalytic motifs (e.g., the conserved 'P...S...S' phosphatidyltransferase motif) absent here. The ENT-specific topology with the characteristic central loop and overall TM count meaningfully distinguishes B from D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the multi-pass membrane topology from the hydrophobicity pattern, identify the ENT-family signature (11-12 TMs with a large central hydrophilic loop), and use family-level knowledge to exclude DNA-binding activities (A, C) and the CDP-alcohol phosphatidyltransferase fold (D). This is a legitimate transferable inference from membrane protein family architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are clearly incompatible with a multi-pass membrane protein lacking any DNA-binding motif. Option D (cardiolipin synthase) has a fundamentally different fold and TM topology from the ENT-like architecture observed. Only B is consistent with the sequence features.


### Important caveats

- The GO annotation in UniProt is IEA:InterPro (computational by similarity), but the underlying experimental evidence (ECO:0000269) from three independent studies confirms the transporter function directly.
- The protein is from Crithidia fasciculata (a trypanosomatid), an organism whose nucleoside transporters are well-studied as drug targets; this biological context supports the ENT assignment.
- The sequence-to-topology argument relies on hydrophobicity analysis and family-level pattern recognition rather than a solved structure of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 497-residue sequence exhibits a clear multi-pass transmembrane topology: numerous hydrophobic stretches (~11-12 predicted TMs) interrupted by a large central hydrophilic loop (approximately residues 200-280: 'GDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY'). This 11-12 TM + large central loop architecture is the hallmark of the equilibrative nucleoside transporter (ENT/SLC29) family. This immediately eliminates options A and C (DNA-binding transcription factors require nuclear localization, DNA-binding motifs like zinc fingers or helix-turn-helix, and are not multi-pass membrane proteins). Option D (cardiolipin synthase, CMP-forming) belongs to the CDP-alcohol phosphatidyltransferase family, which has a distinct fold with fewer (~6-8) TMs and catalytic motifs (e.g., the conserved 'P...S...S' phosphatidyltransferase motif) absent here. The ENT-specific topology with the characteristic central loop and overall TM count meaningfully distinguishes B from D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the multi-pass membrane topology from the hydrophobicity pattern, identify the ENT-family signature (11-12 TMs with a large central hydrophilic loop), and use family-level knowledge to exclude DNA-binding activities (A, C) and the CDP-alcohol phosphatidyltransferase fold (D). This is a legitimate transferable inference from membrane protein family architecture."
  },
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C11",
      "H5",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP5 is named 'Nucleoside transporter 1' (CfNT1) with experimental evidence (ECO:0000269, direct assay) from three independent PubMed studies demonstrating transport of adenosine, hypoxanthine, inosine, uridine, and cytidine. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (SHA-256 match, 497 aa)."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA:InterPro (computational by similarity), but the underlying experimental evidence (ECO:0000269) from three independent studies confirms the transporter function directly.",
    "The protein is from Crithidia fasciculata (a trypanosomatid), an organism whose nucleoside transporters are well-studied as drug targets; this biological context supports the ENT assignment.",
    "The sequence-to-topology argument relies on hydrophobicity analysis and family-level pattern recognition rather than a solved structure of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly incompatible with a multi-pass membrane protein lacking any DNA-binding motif. Option D (cardiolipin synthase) has a fundamentally different fold and TM topology from the ENT-like architecture observed. Only B is consistent with the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP5 is named 'Nucleoside transporter 1' (CfNT1) with experimental evidence (ECO:0000269, direct assay) from three independent PubMed studies demonstrating transport of adenosine, hypoxanthine, inosine, uridine, and cytidine. The GO annotation GO:0005337 (nucleoside transmembrane transporter activity) is directly assigned. The sequence matches the benchmark input exactly (SHA-256 match, 497 aa).",
    "evidence_ids": ["C4", "C5", "C6", "C11", "H5", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 497-residue sequence exhibits a clear multi-pass transmembrane topology: numerous hydrophobic stretches (~11-12 predicted TMs) interrupted by a large central hydrophilic loop (approximately residues 200-280: 'GDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLAERELSEEESGDSRAVEAAGEAPTSNEILRATSVFSVLRSVKWMFVACGFNFLITLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRFSSAFRITWPRRYNQRWIIVAASFARVIFVPLLLLHSYHYIPSEAYGYVMQVVFGLSSGYIASMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRETY'). This 11-12 TM + large central loop architecture is the hallmark of the equilibrative nucleoside transporter (ENT/SLC29) family. This immediately eliminates options A and C (DNA-binding transcription factors require nuclear localization, DNA-binding motifs like zinc fingers or helix-turn-helix, and are not multi-pass membrane proteins). Option D (cardiolipin synthase, CMP-forming) belongs to the CDP-alcohol phosphatidyltransferase family, which has a distinct fold with fewer (~6-8) TMs and catalytic motifs (e.g., the conserved 'P...S...S' phosphatidyltransferase motif) absent here. The ENT-specific topology with the characteristic central loop and overall TM count meaningfully distinguishes B from D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the multi-pass membrane topology from the hydrophobicity pattern, identify the ENT-family signature (11-12 TMs with a large central hydrophilic loop), and use family-level knowledge to exclude DNA-binding activities (A, C) and the CDP-alcohol phosphatidyltransferase fold (D). This is a legitimate transferable inference from membrane protein family architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly incompatible with a multi-pass membrane protein lacking any DNA-binding motif. Option D (cardiolipin synthase) has a fundamentally different fold and TM topology from the ENT-like architecture observed. Only B is consistent with the sequence features."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA:InterPro (computational by similarity), but the underlying experimental evidence (ECO:0000269) from three independent studies confirms the transporter function directly.",
    "The protein is from Crithidia fasciculata (a trypanosomatid), an organism whose nucleoside transporters are well-studied as drug targets; this biological context supports the ENT assignment.",
    "The sequence-to-topology argument relies on hydrophobicity analysis and family-level pattern recognition rather than a solved structure of this exact protein."
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
  "requested_accession": "Q9GTP5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "3164fbc4f11b9d95188d1d240b8371851f4562adacc551b564f7e6157797e81d",
  "benchmark_sequence_length": 497,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 57,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2001-03-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "current_source_sequence_sha256": "3164fbc4f11b9d95188d1d240b8371851f4562adacc551b564f7e6157797e81d",
  "current_source_sequence_length": 497,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 57,
  "selected_historical_version": {
    "accession": "Q9GTP5",
    "database": "Swiss-Prot",
    "entryVersion": 57,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NT1_CRIFA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "selected_historical_source_sequence_sha256": "3164fbc4f11b9d95188d1d240b8371851f4562adacc551b564f7e6157797e81d",
  "selected_historical_source_sequence_length": 497,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 57,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9GTP5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":57,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2001-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAG22610.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Crithidia\"],\"scientificName\":\"Crithidia fasciculata\",\"taxonId\":5656}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"value\":\"CfNT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20037157\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter with broad substrate specificity (PubMed:15694482). Transports adenosine with high affinity (PubMed:15694482, PubMed:20037157, PubMed:24120444). Can also transport hypoxanthine, inosine, uridine and cytidine (PubMed:15694482)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20037157\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24120444\",\"source\":\"PubMed\"}],\"name\":\"adenosine(in) = adenosine(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75343\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16335\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"name\":\"hypoxanthine(out) = hypoxanthine(in)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:71515\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17368\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"name\":\"inosine(in) = inosine(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75375\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17596\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"name\":\"uridine(out) = uridine(in)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:71519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16704\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"name\":\"cytidine(in) = cytidine(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:75367\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17562\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005337\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:nucleoside transmembrane transporter activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu W.\",\"Arendt C.S.\",\"Gessford S.K.\",\"Ntaba D.\",\"Carter N.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15694482\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2004.11.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"15694482\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"12\",\"publicationDate\":\"2005\",\"title\":\"Identification and characterization of purine nucleoside transporters from Crithidia fasciculata.\",\"volume\":\"140\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"INDUCTION BY PUFINE STARVATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20037157\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.074351\"}],\"citationType\":\"journal article\",\"firstPage\":\"6024\",\"id\":\"20037157\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"6035\",\"publicationDate\":\"2010\",\"title\":\"Role of transmembrane domain 4 in ligand permeation by Crithidia fasciculata equilibrative nucleoside transporter 2 (CfNT2).\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP5.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP5.json",
  "source_sha256": "1543207ed03c551de730c893aa46260773725d011a3be50c53bd77787e5c817f",
  "retrieved_utc": "2026-11-01T06:25:26.527509+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24120444\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2013.09.007\"}],\"citationType\":\"journal article\",\"firstPage\":\"75\",\"id\":\"24120444\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"79\",\"publicationDate\":\"2013\",\"title\":\"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-affinity equilibrative nucleoside transporter specific for adenosine.\",\"volume\":\"191\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF THR-153\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 1-11",
  "excerpt": "ID   NT1_CRIFA               Reviewed;         497 AA.\nAC   Q9GTP5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2001, sequence version 1.\nDT   28-JAN-2026, entry version 57.\nDE   RecName: Full=Nucleoside transporter 1 {ECO:0000303|PubMed:15694482};\nDE            Short=CfNT1 {ECO:0000303|PubMed:15694482, ECO:0000303|PubMed:20037157, ECO:0000303|PubMed:24120444};\nOS   Crithidia fasciculata.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Crithidia.\nOX   NCBI_TaxID=5656 {ECO:0000312|EMBL:AAG22610.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 18-25",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   INDUCTION BY PUFINE STARVATION.\nRX   PubMed=15694482; DOI=10.1016/j.molbiopara.2004.11.018;\nRA   Liu W., Arendt C.S., Gessford S.K., Ntaba D., Carter N.S., Ullman B.;\nRT   \"Identification and characterization of purine nucleoside transporters from\nRT   Crithidia fasciculata.\";\nRL   Mol. Biochem. Parasitol. 140:1-12(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 26-32",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, AND SUBCELLULAR LOCATION.\nRX   PubMed=20037157; DOI=10.1074/jbc.m109.074351;\nRA   Arendt C.S., Ullman B.;\nRT   \"Role of transmembrane domain 4 in ligand permeation by Crithidia\nRT   fasciculata equilibrative nucleoside transporter 2 (CfNT2).\";\nRL   J. Biol. Chem. 285:6024-6035(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 33-40",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   MUTAGENESIS OF THR-153.\nRX   PubMed=24120444; DOI=10.1016/j.molbiopara.2013.09.007;\nRA   Arendt C.S.;\nRT   \"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-\nRT   affinity equilibrative nucleoside transporter specific for adenosine.\";\nRL   Mol. Biochem. Parasitol. 191:75-79(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 41-46",
  "excerpt": "CC   -!- FUNCTION: Nucleoside transporter with broad substrate specificity\nCC       (PubMed:15694482). Transports adenosine with high affinity\nCC       (PubMed:15694482, PubMed:20037157, PubMed:24120444). Can also transport\nCC       hypoxanthine, inosine, uridine and cytidine (PubMed:15694482).\nCC       {ECO:0000269|PubMed:15694482, ECO:0000269|PubMed:20037157,\nCC       ECO:0000269|PubMed:24120444}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 47-50",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=adenosine(in) = adenosine(out); Xref=Rhea:RHEA:75343,\nCC         ChEBI:CHEBI:16335; Evidence={ECO:0000269|PubMed:15694482,\nCC         ECO:0000269|PubMed:20037157, ECO:0000269|PubMed:24120444};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 51-53",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=hypoxanthine(out) = hypoxanthine(in); Xref=Rhea:RHEA:71515,\nCC         ChEBI:CHEBI:17368; Evidence={ECO:0000269|PubMed:15694482};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 54-56",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=inosine(in) = inosine(out); Xref=Rhea:RHEA:75375,\nCC         ChEBI:CHEBI:17596; Evidence={ECO:0000269|PubMed:15694482};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 57-59",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=uridine(out) = uridine(in); Xref=Rhea:RHEA:71519,\nCC         ChEBI:CHEBI:16704; Evidence={ECO:0000269|PubMed:15694482};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 60-62",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=cytidine(in) = cytidine(out); Xref=Rhea:RHEA:75367,\nCC         ChEBI:CHEBI:17562; Evidence={ECO:0000269|PubMed:15694482};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP5?format=txt&versions=57",
  "source_sha256": "7426320c762a09c28cce26459dfd7f6960cc0a07dde3142fc087281aecaff990",
  "retrieved_utc": "2026-11-01T06:28:47.063579+00:00",
  "source_locator": "lines 86-86",
  "excerpt": "DR   GO; GO:0005337; F:nucleoside transmembrane transporter activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 57,
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
  "source_locator": "lines 7116-7125",
  "excerpt": "[Term]\nid: GO:0000977\nname: RNA polymerase II transcription regulatory region sequence-specific DNA binding\nnamespace: molecular_function\nalt_id: GO:0001012\ndef: \"Binding to a specific sequence of DNA that is part of a regulatory region that controls the transcription of a gene or cistron by RNA polymerase II.\" [GOC:txnOH]\ncomment: To minimize ambiguity in the use of the word \"promoter\" in GO, we have chosen the phrase \"transcription regulatory region\" to refer to all of the regulatory regions. Regulatory regions in the DNA which control initiation may include the \"core promoter\" where the basal transcription machinery binds, the \"core promoter proximal region\" where regulatory factors other than the basal machinery bind. There are also additional regulatory regions, in both the DNA and the RNA transcript, which regulate elongation or termination of transcription.\nsynonym: \"RNA polymerase II regulatory region DNA binding\" RELATED []\nis_a: GO:0000976 ! transcription cis-regulatory region binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0000977"
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
  "source_locator": "lines 8558-8574",
  "excerpt": "[Term]\nid: GO:0001216\nname: DNA-binding transcription activator activity\nnamespace: molecular_function\nalt_id: GO:0001140\nalt_id: GO:0001215\ndef: \"A DNA-binding transcription factor activity that activates or increases transcription of specific gene sets.\" [GOC:txnOH-2018]\ncomment: For usage guidance, see comment in GO:0003700 ; DNA-binding transcription factor activity.\nsynonym: \"bacterial-type RNA polymerase core promoter proximal region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription\" RELATED []\nsynonym: \"bacterial-type RNA polymerase transcriptional activator activity, metal ion regulated sequence-specific DNA binding\" NARROW []\nsynonym: \"bacterial-type RNA polymerase transcriptional activator activity, sequence-specific DNA binding\" NARROW []\nsynonym: \"metal ion regulated sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"transcriptional activator activity, bacterial-type RNA polymerase core promoter proximal region sequence-specific binding\" NARROW []\nsynonym: \"transcriptional activator activity, bacterial-type RNA polymerase proximal promoter sequence-specific DNA binding\" RELATED []\nis_a: GO:0003700 ! DNA-binding transcription factor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0001216"
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
  "source_locator": "lines 55843-55864",
  "excerpt": "[Term]\nid: GO:0005337\nname: nucleoside transmembrane transporter activity\nnamespace: molecular_function\ndef: \"Enables the transfer of a nucleoside, a nucleobase linked to either beta-D-ribofuranose (ribonucleoside) or 2-deoxy-beta-D-ribofuranose, (a deoxyribonucleotide) from one side of a membrane to the other.\" [GOC:ai]\nsynonym: \"intracellular nucleoside transmembrane transporter activity\" NARROW []\nxref: Reactome:R-HSA-109527 \"Equilibrative transport (import) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 2\"\nxref: Reactome:R-HSA-109529 \"Equilibrative transport (export) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 2\"\nxref: Reactome:R-HSA-109534 \"Equilibrative transport (export) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 1\"\nxref: Reactome:R-HSA-109536 \"Equilibrative transport (import) of nucleosides and free bases by solute carrier family 29 (nucleoside transporters), member 1\"\nxref: Reactome:R-HSA-5628807 \"Defective SLC29A3 does not transport nucleosides from lysosomal lumen to cytosol\"\nxref: Reactome:R-HSA-727740 \"Equilibrative transport (import) of adenosine and biogenic amines by solute carrier family 29 (nucleoside transporters), member 4\"\nxref: Reactome:R-HSA-727749 \"SLC29A3 transports nucleosides from lysosomal lumen to cytosol\"\nxref: Reactome:R-HSA-727767 \"SLC29A3 transports nucleosides from cytosol to lysosomal lumen\"\nxref: Reactome:R-HSA-727768 \"Equilibrative transport (export) of adenosine and biogenic amines by solute carrier family 29 (nucleoside transporters), member 4\"\nxref: Reactome:R-HSA-9751024 \"SLC29A1,2 transport 6MP from extracellular region to cytosol\"\nxref: Reactome:R-HSA-9754929 \"SLC29A3 transports RBV,RBV-TP from cytosol to mitochondrial matrix\"\nxref: Reactome:R-HSA-9755015 \"SLC29A1 transports RBV from extracellular region to cytosol\"\nxref: Reactome:R-HSA-9755035 \"SLC29A1 transports RBV from cytosol to extracellular region\"\nis_a: GO:0015932 ! nucleobase-containing compound transmembrane transporter activity\nis_a: GO:1901505 ! carbohydrate derivative transmembrane transporter activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005337"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 175. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
