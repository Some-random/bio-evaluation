# GO_cellular_component_0146: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0146.txt)

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
MDTAPDHREPQEQGESRKWYEMTASEFYVYVVAFMCGVSMMMSVNAVFSAPAYIMTYYRYAMQDPEAVPLYTNFWNNVMTYYNLIGIVTSLIMEPLTLLSWFRRIPIKVRLLGGLVILIVEIIVLMVVPARGTSEAGAVATICCTGFIGGFGKSIFESTAYGMFGAFPSSFTSTMMGGVGMSGVLTSLLQIIVKAALPDSYEGVKKQSKIYYGLDVGIQGMTFVALILLRFNSFAQNYFGDLGAVKSKVDAGKLSAEALCHTDEHPTHDKEGRNSSSGKEVPALGEVQTAAAKSEGPDAVEESSWPHEVEGPTSNEILVATAIFSTLRRVKWMFVACAFNFLITLFLFPGIAVGMFPDSKWFSTIAVFIFNVFDVLGRFSPSLKLMWPRSYKQRWIIVAASFARVIFVPLLLLHSYHYIPGEAYGYVMEVIFGFSNGYVGSMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRERH

[Multiple Choices]
A. microvillus membrane
B. midbody
C. plasma membrane
D. membrane attack complex
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

> The exact sequence matches the UniProt entry for this protein. That entry annotates it to the cell membrane based on literature and assigns plasma membrane by computational GO inference. This supports choice C, while the evidence types should not be conflated.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments support that this is a multipass membrane protein, making midbody and membrane attack complex poor fits. That general inference does not establish plasma membrane rather than another membrane location or a specialized plasma-membrane domain.


**Missing item-specific fact**

> The protein-specific cell-membrane localization, or equivalent knowledge of this transporter’s localization, is needed to distinguish the offered membrane locations.


**Reason**

> The sequence offers a useful broad membrane-protein clue, but the choice between plasma membrane and microvillus membrane requires localization information not established by the sequence features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No supplied evidence establishes microvillus localization for this protein. However, the options are not strictly disjoint: a microvillus membrane is a portion of the plasma membrane.


### Important caveats

- The plasma-membrane GO annotation is computationally inferred; the cited UniProt cell-membrane annotation is literature-based, not presented here as a directly verified experimental measurement.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments support that this is a multipass membrane protein, making midbody and membrane attack complex poor fits. That general inference does not establish plasma membrane rather than another membrane location or a specialized plasma-membrane domain.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cell-membrane localization, or equivalent knowledge of this transporter’s localization, is needed to distinguish the offered membrane locations.",
    "reason": "The sequence offers a useful broad membrane-protein clue, but the choice between plasma membrane and microvillus membrane requires localization information not established by the sequence features alone."
  },
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for this protein. That entry annotates it to the cell membrane based on literature and assigns plasma membrane by computational GO inference. This supports choice C, while the evidence types should not be conflated."
  },
  "important_caveats": [
    "The plasma-membrane GO annotation is computationally inferred; the cited UniProt cell-membrane annotation is literature-based, not presented here as a directly verified experimental measurement.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No supplied evidence establishes microvillus localization for this protein. However, the options are not strictly disjoint: a microvillus membrane is a portion of the plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for this protein. That entry annotates it to the cell membrane based on literature and assigns plasma membrane by computational GO inference. This supports choice C, while the evidence types should not be conflated.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments support that this is a multipass membrane protein, making midbody and membrane attack complex poor fits. That general inference does not establish plasma membrane rather than another membrane location or a specialized plasma-membrane domain.",
    "missing_item_specific_fact": "The protein-specific cell-membrane localization, or equivalent knowledge of this transporter’s localization, is needed to distinguish the offered membrane locations.",
    "reason": "The sequence offers a useful broad membrane-protein clue, but the choice between plasma membrane and microvillus membrane requires localization information not established by the sequence features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No supplied evidence establishes microvillus localization for this protein. However, the options are not strictly disjoint: a microvillus membrane is a portion of the plasma membrane."
  },
  "important_caveats": [
    "The plasma-membrane GO annotation is computationally inferred; the cited UniProt cell-membrane annotation is literature-based, not presented here as a directly verified experimental measurement.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry O76269 (Nucleoside transporter 1.2, LdNT1.2 from Leishmania donovani) annotates the protein as 'Cell membrane; Multi-pass membrane protein' with evidence codes ECO:0000305 from PubMed:9707568 and PubMed:12835315. The GO cross-reference confirms GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym. The GO annotation evidence code is IEA (electronic), but the underlying subcellular location comment is curator-inferred from two experimental papers describing this as a plasma membrane nucleoside transporter. The sequence itself shows multiple hydrophobic transmembrane stretches consistent with a multi-pass integral membrane protein at the cell surface.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays numerous long hydrophobic stretches (at least 10-12 transmembrane segments), identifying it as a multi-pass integral membrane protein. General biological reasoning then distinguishes the options: (D) membrane attack complex is a mammalian complement-system pore-forming complex (C5b-C9), irrelevant to a Leishmania protozoan protein; (B) midbody is a transient cytokinetic bridge structure, not a residence for a constitutive transporter; (A) microvillus membrane is a highly specialized sub-domain of the plasma membrane found in polarized epithelial cells (e.g., intestinal brush border), and Leishmania donovani lacks this architecture; (C) plasma membrane is the logical primary location for a multi-pass membrane transporter that must access extracellular substrates. A nucleoside transporter must reside at the cell surface to import extracellular nucleosides, making plasma membrane the default and most general correct annotation.


**Missing item-specific fact**

> None critical. Identifying the protein specifically as a nucleoside transporter would strengthen the argument, but the multi-pass membrane topology visible in the sequence combined with general knowledge about membrane transporters and the biology of the distractor options suffices to select C over A, B, and D.


**Reason**

> The sequence clearly encodes a multi-pass membrane protein. Among the four choices, three can be eliminated by general biological reasoning: MAC is a mammalian complement complex, midbody is a cytokinesis structure, and microvillus membrane is a specialized epithelial sub-domain absent in protozoa. The remaining option (plasma membrane) is the expected primary location for any multi-pass membrane transporter. This reasoning path does not require memorizing the specific UniProt annotation for O76269.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While microvillus membrane (GO:0031528) is technically part_of plasma membrane (GO:0005886), it is a narrow sub-compartment restricted to specialized polarized cells. For a general nucleoside transporter in a protozoan, plasma membrane is unambiguously the correct primary cellular component. The other two options (midbody, membrane attack complex) are clearly incompatible with the protein's identity and organism.


### Important caveats

- The GO annotation for this protein carries evidence code IEA (Inferred from Electronic Annotation), meaning the plasma membrane assignment is computationally propagated. However, the underlying UniProt SUBCELLULAR LOCATION comment uses ECO:0000305 (curator inference from experimental literature), providing stronger support.
- The UniProt entry is flagged as 'Fragment,' so the full-length protein topology is not fully resolved, though the supplied 491-aa sequence still shows clear multi-pass membrane architecture.
- The organism is Leishmania donovani, a protozoan parasite. Microvillus membrane as a GO term is primarily used in the context of metazoan epithelial biology, making option A biologically implausible for this organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays numerous long hydrophobic stretches (at least 10-12 transmembrane segments), identifying it as a multi-pass integral membrane protein. General biological reasoning then distinguishes the options: (D) membrane attack complex is a mammalian complement-system pore-forming complex (C5b-C9), irrelevant to a Leishmania protozoan protein; (B) midbody is a transient cytokinetic bridge structure, not a residence for a constitutive transporter; (A) microvillus membrane is a highly specialized sub-domain of the plasma membrane found in polarized epithelial cells (e.g., intestinal brush border), and Leishmania donovani lacks this architecture; (C) plasma membrane is the logical primary location for a multi-pass membrane transporter that must access extracellular substrates. A nucleoside transporter must reside at the cell surface to import extracellular nucleosides, making plasma membrane the default and most general correct annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Identifying the protein specifically as a nucleoside transporter would strengthen the argument, but the multi-pass membrane topology visible in the sequence combined with general knowledge about membrane transporters and the biology of the distractor options suffices to select C over A, B, and D.",
    "reason": "The sequence clearly encodes a multi-pass membrane protein. Among the four choices, three can be eliminated by general biological reasoning: MAC is a mammalian complement complex, midbody is a cytokinesis structure, and microvillus membrane is a specialized epithelial sub-domain absent in protozoa. The remaining option (plasma membrane) is the expected primary location for any multi-pass membrane transporter. This reasoning path does not require memorizing the specific UniProt annotation for O76269."
  },
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry O76269 (Nucleoside transporter 1.2, LdNT1.2 from Leishmania donovani) annotates the protein as 'Cell membrane; Multi-pass membrane protein' with evidence codes ECO:0000305 from PubMed:9707568 and PubMed:12835315. The GO cross-reference confirms GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym. The GO annotation evidence code is IEA (electronic), but the underlying subcellular location comment is curator-inferred from two experimental papers describing this as a plasma membrane nucleoside transporter. The sequence itself shows multiple hydrophobic transmembrane stretches consistent with a multi-pass integral membrane protein at the cell surface."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code IEA (Inferred from Electronic Annotation), meaning the plasma membrane assignment is computationally propagated. However, the underlying UniProt SUBCELLULAR LOCATION comment uses ECO:0000305 (curator inference from experimental literature), providing stronger support.",
    "The UniProt entry is flagged as 'Fragment,' so the full-length protein topology is not fully resolved, though the supplied 491-aa sequence still shows clear multi-pass membrane architecture.",
    "The organism is Leishmania donovani, a protozoan parasite. Microvillus membrane as a GO term is primarily used in the context of metazoan epithelial biology, making option A biologically implausible for this organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While microvillus membrane (GO:0031528) is technically part_of plasma membrane (GO:0005886), it is a narrow sub-compartment restricted to specialized polarized cells. For a general nucleoside transporter in a protozoan, plasma membrane is unambiguously the correct primary cellular component. The other two options (midbody, membrane attack complex) are clearly incompatible with the protein's identity and organism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry O76269 (Nucleoside transporter 1.2, LdNT1.2 from Leishmania donovani) annotates the protein as 'Cell membrane; Multi-pass membrane protein' with evidence codes ECO:0000305 from PubMed:9707568 and PubMed:12835315. The GO cross-reference confirms GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym. The GO annotation evidence code is IEA (electronic), but the underlying subcellular location comment is curator-inferred from two experimental papers describing this as a plasma membrane nucleoside transporter. The sequence itself shows multiple hydrophobic transmembrane stretches consistent with a multi-pass integral membrane protein at the cell surface.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays numerous long hydrophobic stretches (at least 10-12 transmembrane segments), identifying it as a multi-pass integral membrane protein. General biological reasoning then distinguishes the options: (D) membrane attack complex is a mammalian complement-system pore-forming complex (C5b-C9), irrelevant to a Leishmania protozoan protein; (B) midbody is a transient cytokinetic bridge structure, not a residence for a constitutive transporter; (A) microvillus membrane is a highly specialized sub-domain of the plasma membrane found in polarized epithelial cells (e.g., intestinal brush border), and Leishmania donovani lacks this architecture; (C) plasma membrane is the logical primary location for a multi-pass membrane transporter that must access extracellular substrates. A nucleoside transporter must reside at the cell surface to import extracellular nucleosides, making plasma membrane the default and most general correct annotation.",
    "missing_item_specific_fact": "None critical. Identifying the protein specifically as a nucleoside transporter would strengthen the argument, but the multi-pass membrane topology visible in the sequence combined with general knowledge about membrane transporters and the biology of the distractor options suffices to select C over A, B, and D.",
    "reason": "The sequence clearly encodes a multi-pass membrane protein. Among the four choices, three can be eliminated by general biological reasoning: MAC is a mammalian complement complex, midbody is a cytokinesis structure, and microvillus membrane is a specialized epithelial sub-domain absent in protozoa. The remaining option (plasma membrane) is the expected primary location for any multi-pass membrane transporter. This reasoning path does not require memorizing the specific UniProt annotation for O76269."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While microvillus membrane (GO:0031528) is technically part_of plasma membrane (GO:0005886), it is a narrow sub-compartment restricted to specialized polarized cells. For a general nucleoside transporter in a protozoan, plasma membrane is unambiguously the correct primary cellular component. The other two options (midbody, membrane attack complex) are clearly incompatible with the protein's identity and organism."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code IEA (Inferred from Electronic Annotation), meaning the plasma membrane assignment is computationally propagated. However, the underlying UniProt SUBCELLULAR LOCATION comment uses ECO:0000305 (curator inference from experimental literature), providing stronger support.",
    "The UniProt entry is flagged as 'Fragment,' so the full-length protein topology is not fully resolved, though the supplied 491-aa sequence still shows clear multi-pass membrane architecture.",
    "The organism is Leishmania donovani, a protozoan parasite. Microvillus membrane as a GO term is primarily used in the context of metazoan epithelial biology, making option A biologically implausible for this organism."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence is annotated as a multi-pass cell-membrane protein, and the GO plasma-membrane annotation is consistent with the expected choice. The cellular-location annotation cites literature, while the GO annotation is computationally inferred; these support the answer but are not, by themselves, a direct experimental localization result.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has many hydrophobic transmembrane segments, consistent with a multi-pass transporter rather than a midbody component or a subunit of the membrane attack complex. Transferable knowledge of transporter families supports a cell-surface membrane location. A microvillus membrane is a specialized plasma-membrane subdomain, and the sequence offers no indication of that specialized localization; the general plasma-membrane choice is therefore meaningfully favored.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The membrane-spanning architecture and transporter-like sequence provide a credible family-level basis for choosing plasma membrane over the other offered locations, without needing the exact protein's database annotation. This is a probabilistic localization inference, not proof of the precise membrane subdomain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Microvillus membrane is a specialized plasma-membrane subdomain, but the input provides no reason to assign this protein to that subdomain rather than to the plasma membrane generally.


### Important caveats

- The source annotation supports cell-membrane localization, but the evidence supplied does not independently establish direct experimental localization or rule out every other membrane subdomain.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many hydrophobic transmembrane segments, consistent with a multi-pass transporter rather than a midbody component or a subunit of the membrane attack complex. Transferable knowledge of transporter families supports a cell-surface membrane location. A microvillus membrane is a specialized plasma-membrane subdomain, and the sequence offers no indication of that specialized localization; the general plasma-membrane choice is therefore meaningfully favored.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The membrane-spanning architecture and transporter-like sequence provide a credible family-level basis for choosing plasma membrane over the other offered locations, without needing the exact protein's database annotation. This is a probabilistic localization inference, not proof of the precise membrane subdomain."
  },
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a multi-pass cell-membrane protein, and the GO plasma-membrane annotation is consistent with the expected choice. The cellular-location annotation cites literature, while the GO annotation is computationally inferred; these support the answer but are not, by themselves, a direct experimental localization result."
  },
  "important_caveats": [
    "The source annotation supports cell-membrane localization, but the evidence supplied does not independently establish direct experimental localization or rule out every other membrane subdomain."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Microvillus membrane is a specialized plasma-membrane subdomain, but the input provides no reason to assign this protein to that subdomain rather than to the plasma membrane generally."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a multi-pass cell-membrane protein, and the GO plasma-membrane annotation is consistent with the expected choice. The cellular-location annotation cites literature, while the GO annotation is computationally inferred; these support the answer but are not, by themselves, a direct experimental localization result.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has many hydrophobic transmembrane segments, consistent with a multi-pass transporter rather than a midbody component or a subunit of the membrane attack complex. Transferable knowledge of transporter families supports a cell-surface membrane location. A microvillus membrane is a specialized plasma-membrane subdomain, and the sequence offers no indication of that specialized localization; the general plasma-membrane choice is therefore meaningfully favored.",
    "missing_item_specific_fact": "",
    "reason": "The membrane-spanning architecture and transporter-like sequence provide a credible family-level basis for choosing plasma membrane over the other offered locations, without needing the exact protein's database annotation. This is a probabilistic localization inference, not proof of the precise membrane subdomain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Microvillus membrane is a specialized plasma-membrane subdomain, but the input provides no reason to assign this protein to that subdomain rather than to the plasma membrane generally."
  },
  "important_caveats": [
    "The source annotation supports cell-membrane localization, but the evidence supplied does not independently establish direct experimental localization or rule out every other membrane subdomain."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry O76269 (LdNT1.2, nucleoside transporter 1.2 from Leishmania donovani) explicitly annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000305) from two PubMed papers (9707568 and 12835315). The GO cross-reference GO:0005886 (plasma membrane) has EXACT synonym 'cell membrane' per the ontology definition. The sequence shows ~11-12 hydrophobic transmembrane segments consistent with a multi-pass membrane transporter. The answer C (plasma membrane) is directly supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays approximately 11-12 long hydrophobic stretches characteristic of a multi-pass membrane protein with the topology of the equilibrative nucleoside transporter (ENT) family. ENT family members (human ENT1/ENT2, yeast Nrt1, etc.) are universally characterized as plasma membrane transporters that move nucleosides across the cell boundary. This family-level knowledge immediately favors 'plasma membrane.' Among the alternatives: (B) midbody is a transient cytokinetic bridge, incompatible with a constitutive transporter; (D) membrane attack complex is the specific C5b-C9 complement pore-forming assembly, unrelated to nucleoside transport; (A) microvillus membrane is a specialized epithelial sub-compartment of the plasma membrane, not a feature of the protozoan Leishmania (which lacks true microvilli). The combination of family recognition (ENT = plasma membrane), sequence topology (multi-pass TM), and elimination of clearly incompatible alternatives provides a strong, transferable inference favoring C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model trained on general biology can recognize the multi-pass TM architecture, associate it with the well-known ENT/nucleoside transporter family (plasma membrane in all characterized organisms), and eliminate the other three options using basic cell biology (midbody is transient, MAC is complement-specific, microvillus membrane is epithelial-specific and absent in protozoa). No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While microvillus membrane (A) is technically a sub-compartment of the plasma membrane, it is an epithelial-specific structure not applicable to a protozoan parasite like Leishmania. The other options (B, D) are clearly incompatible with a nucleoside transporter. Only C is defensible.


### Important caveats

- The UniProt GO annotation for plasma membrane carries IEA (inferred from electronic annotation) evidence, but the underlying subcellular location comment carries experimental evidence codes (ECO:0000305) from two independent publications.
- The sequence is flagged as a 'Fragment' in UniProt, but the provided 491-aa sequence matches the current entry exactly.
- Microvillus membrane (GO:0031528) is a part_of microvillus and a cell projection membrane; it would be a valid sub-localization for some plasma membrane proteins in epithelial cells but is not applicable to a protozoan parasite.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays approximately 11-12 long hydrophobic stretches characteristic of a multi-pass membrane protein with the topology of the equilibrative nucleoside transporter (ENT) family. ENT family members (human ENT1/ENT2, yeast Nrt1, etc.) are universally characterized as plasma membrane transporters that move nucleosides across the cell boundary. This family-level knowledge immediately favors 'plasma membrane.' Among the alternatives: (B) midbody is a transient cytokinetic bridge, incompatible with a constitutive transporter; (D) membrane attack complex is the specific C5b-C9 complement pore-forming assembly, unrelated to nucleoside transport; (A) microvillus membrane is a specialized epithelial sub-compartment of the plasma membrane, not a feature of the protozoan Leishmania (which lacks true microvilli). The combination of family recognition (ENT = plasma membrane), sequence topology (multi-pass TM), and elimination of clearly incompatible alternatives provides a strong, transferable inference favoring C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model trained on general biology can recognize the multi-pass TM architecture, associate it with the well-known ENT/nucleoside transporter family (plasma membrane in all characterized organisms), and eliminate the other three options using basic cell biology (midbody is transient, MAC is complement-specific, microvillus membrane is epithelial-specific and absent in protozoa). No target-specific database lookup is required."
  },
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry O76269 (LdNT1.2, nucleoside transporter 1.2 from Leishmania donovani) explicitly annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000305) from two PubMed papers (9707568 and 12835315). The GO cross-reference GO:0005886 (plasma membrane) has EXACT synonym 'cell membrane' per the ontology definition. The sequence shows ~11-12 hydrophobic transmembrane segments consistent with a multi-pass membrane transporter. The answer C (plasma membrane) is directly supported."
  },
  "important_caveats": [
    "The UniProt GO annotation for plasma membrane carries IEA (inferred from electronic annotation) evidence, but the underlying subcellular location comment carries experimental evidence codes (ECO:0000305) from two independent publications.",
    "The sequence is flagged as a 'Fragment' in UniProt, but the provided 491-aa sequence matches the current entry exactly.",
    "Microvillus membrane (GO:0031528) is a part_of microvillus and a cell projection membrane; it would be a valid sub-localization for some plasma membrane proteins in epithelial cells but is not applicable to a protozoan parasite."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While microvillus membrane (A) is technically a sub-compartment of the plasma membrane, it is an epithelial-specific structure not applicable to a protozoan parasite like Leishmania. The other options (B, D) are clearly incompatible with a nucleoside transporter. Only C is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry O76269 (LdNT1.2, nucleoside transporter 1.2 from Leishmania donovani) explicitly annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000305) from two PubMed papers (9707568 and 12835315). The GO cross-reference GO:0005886 (plasma membrane) has EXACT synonym 'cell membrane' per the ontology definition. The sequence shows ~11-12 hydrophobic transmembrane segments consistent with a multi-pass membrane transporter. The answer C (plasma membrane) is directly supported.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays approximately 11-12 long hydrophobic stretches characteristic of a multi-pass membrane protein with the topology of the equilibrative nucleoside transporter (ENT) family. ENT family members (human ENT1/ENT2, yeast Nrt1, etc.) are universally characterized as plasma membrane transporters that move nucleosides across the cell boundary. This family-level knowledge immediately favors 'plasma membrane.' Among the alternatives: (B) midbody is a transient cytokinetic bridge, incompatible with a constitutive transporter; (D) membrane attack complex is the specific C5b-C9 complement pore-forming assembly, unrelated to nucleoside transport; (A) microvillus membrane is a specialized epithelial sub-compartment of the plasma membrane, not a feature of the protozoan Leishmania (which lacks true microvilli). The combination of family recognition (ENT = plasma membrane), sequence topology (multi-pass TM), and elimination of clearly incompatible alternatives provides a strong, transferable inference favoring C.",
    "missing_item_specific_fact": "",
    "reason": "A model trained on general biology can recognize the multi-pass TM architecture, associate it with the well-known ENT/nucleoside transporter family (plasma membrane in all characterized organisms), and eliminate the other three options using basic cell biology (midbody is transient, MAC is complement-specific, microvillus membrane is epithelial-specific and absent in protozoa). No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While microvillus membrane (A) is technically a sub-compartment of the plasma membrane, it is an epithelial-specific structure not applicable to a protozoan parasite like Leishmania. The other options (B, D) are clearly incompatible with a nucleoside transporter. Only C is defensible."
  },
  "important_caveats": [
    "The UniProt GO annotation for plasma membrane carries IEA (inferred from electronic annotation) evidence, but the underlying subcellular location comment carries experimental evidence codes (ECO:0000305) from two independent publications.",
    "The sequence is flagged as a 'Fragment' in UniProt, but the provided 491-aa sequence matches the current entry exactly.",
    "Microvillus membrane (GO:0031528) is a part_of microvillus and a cell projection membrane; it would be a valid sub-localization for some plasma membrane proteins in epithelial cells but is not applicable to a protozoan parasite."
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
  "requested_accession": "O76269",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "192e356b57159ee69c6287591ae9b71d5c65f6e1d7fe21a8299687927176107d",
  "benchmark_sequence_length": 491,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 69,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-11-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "current_source_sequence_sha256": "192e356b57159ee69c6287591ae9b71d5c65f6e1d7fe21a8299687927176107d",
  "current_source_sequence_length": 491,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 67,
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
  },
  "selected_historical_record_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "selected_historical_source_sequence_sha256": "192e356b57159ee69c6287591ae9b71d5c65f6e1d7fe21a8299687927176107d",
  "selected_historical_source_sequence_length": 491,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 67,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"O76269\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":69,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-11-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32315.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Leishmania\"],\"scientificName\":\"Leishmania donovani\",\"taxonId\":5661}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.2\",\"source\":\"Reference\"}],\"value\":\"Equilibrative nucleoside transporter 1.2\"}}],\"flag\":\"Fragment\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 1.2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"value\":\"LdNT1.2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"12835315\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"9707568\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Vasudevan G.\",\"Carter N.S.\",\"Drew M.E.\",\"Beverley S.M.\",\"Sanchez M.A.\",\"Seyfang A.\",\"Ullman B.\",\"Landfear S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9707568\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.95.17.9873\"}],\"citationType\":\"journal article\",\"firstPage\":\"9873\",\"id\":\"9707568\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"9878\",\"publicationDate\":\"1998\",\"title\":\"Cloning of Leishmania nucleoside transporter genes by rescue of a transport-deficient mutant.\",\"volume\":\"95\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAC32315.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/O76269.json",
  "source_sha256": "8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f",
  "retrieved_utc": "2026-11-02T04:29:16.869968+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Stein A.\",\"Vaseduvan G.\",\"Carter N.S.\",\"Ullman B.\",\"Landfear S.M.\",\"Kavanaugh M.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12835315\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m306188200\"}],\"citationType\":\"journal article\",\"firstPage\":\"35127\",\"id\":\"12835315\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"35134\",\"publicationDate\":\"2003\",\"title\":\"Equilibrative nucleoside transporter family members from Leishmania donovani are electrogenic proton symporters.\",\"volume\":\"278\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   NT12_LEIDO              Reviewed;         491 AA.\nAC   O76269;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-NOV-1998, sequence version 1.\nDT   28-JAN-2026, entry version 67.\nDE   RecName: Full=Nucleoside transporter 1.2 {ECO:0000303|PubMed:9707568};\nDE            Short=LdNT1.2 {ECO:0000303|PubMed:9707568};\nDE   AltName: Full=Equilibrative nucleoside transporter 1.2 {ECO:0000303|Ref.2};\nDE   Flags: Fragment;\nGN   Name=NT1.2 {ECO:0000303|PubMed:9707568};\nGN   ORFNames=CGC20_30425 {ECO:0000312|EMBL:TPP53189.1},\nGN   LDHU3_15.1540 {ECO:0000312|EMBL:CAC5428820.1};\nOS   Leishmania donovani.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Leishmania.\nOX   NCBI_TaxID=5661 {ECO:0000312|EMBL:AAC32315.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "source_locator": "lines 17-25",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAC32315.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, TRANSPORTER ACTIVITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=9707568; DOI=10.1073/pnas.95.17.9873;\nRA   Vasudevan G., Carter N.S., Drew M.E., Beverley S.M., Sanchez M.A.,\nRA   Seyfang A., Ullman B., Landfear S.M.;\nRT   \"Cloning of Leishmania nucleoside transporter genes by rescue of a\nRT   transport-deficient mutant.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 95:9873-9878(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "source_locator": "lines 41-48",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND TRANSPORTER ACTIVITY.\nRX   PubMed=12835315; DOI=10.1074/jbc.m306188200;\nRA   Stein A., Vaseduvan G., Carter N.S., Ullman B., Landfear S.M.,\nRA   Kavanaugh M.P.;\nRT   \"Equilibrative nucleoside transporter family members from Leishmania\nRT   donovani are electrogenic proton symporters.\";\nRL   J. Biol. Chem. 278:35127-35134(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "source_locator": "lines 66-67",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:12835315,\nCC       ECO:0000305|PubMed:9707568}; Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/O76269?format=txt&versions=67",
  "source_sha256": "c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7",
  "retrieved_utc": "2026-11-02T04:29:18.847742+00:00",
  "source_locator": "lines 86-86",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 67,
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
  "source_locator": "lines 57517-57530",
  "excerpt": "[Term]\nid: GO:0005579\nname: membrane attack complex\nnamespace: cellular_component\ndef: \"A protein complex produced by sequentially activated components of the complement cascade inserted into a target cell membrane and forming a pore leading to cell lysis via ion and water flow.\" [GOC:add, ISBN:0198547684, ISBN:068340007X, ISBN:0781735149]\nsynonym: \"MAC\" EXACT []\nsynonym: \"membrane attack complex protein alphaM chain\" NARROW []\nsynonym: \"membrane attack complex protein beta2 chain\" NARROW []\nsynonym: \"TCC\" EXACT []\nsynonym: \"terminal complement complex\" EXACT []\nxref: Wikipedia:Complement_membrane_attack_complex\nis_a: GO:0046930 ! pore complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005579"
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
  "source_locator": "lines 166648-166656",
  "excerpt": "[Term]\nid: GO:0030496\nname: midbody\nnamespace: cellular_component\ndef: \"A thin cytoplasmic bridge formed between daughter cells at the end of cytokinesis. The midbody forms where the contractile ring constricts, and may persist for some time before finally breaking to complete cytokinesis.\" [ISBN:0815316194]\nsubset: goslim_pir\nxref: Wikipedia:Midbody_(cell_biology)\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0030496"
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
  "source_locator": "lines 177423-177430",
  "excerpt": "[Term]\nid: GO:0031528\nname: microvillus membrane\nnamespace: cellular_component\ndef: \"The portion of the plasma membrane surrounding a microvillus.\" [GOC:mah]\nis_a: GO:0031253 ! cell projection membrane\nrelationship: part_of GO:0005902 ! microvillus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0031528"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
