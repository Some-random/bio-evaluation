# GO_cellular_component_0084

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAKTPIPFTTLNDLPDVILSNIIAAVSDTRSRNATALVCHKWLVLERSTRTSLTLRGNIRDLFMLPTCFRSITYLDLSLISPWGHPLLASRATDAPDNDSALIAHLLRHTFPSVTSLTLYARDPNTIQFLPAQWAHTLKHIKLVRWHQRAQLASGDELNLLFIGTPQITSLDLSNFYCWTDDVPPALQSNPNVACNLTRFNLLNASFPEGFKTDEIKVITKCCPNLKEFKVACMFDPRYIGFIGDEALVCLATNCPKLSVLHLADTSVLSNCRGDPNDEGFTVEDAQFSVSTLIEVFSGLSLLEELVFDVCNNVRDSGPALEILKTKCPKLRSLKLGQFHGISMPIESKLDGVALCQGLLSLSIRSVGDLDDMGLIGIGRGCSRLTKFEIECCKKITMRGMRTLASLLRKSLVDVTISCCKNLGASSSLKALEPIQDRIQRLHIDCVWDTVEEFENLDGVEYGFDLNEASGGEASSNPAGFGDTFGSMDDDLMNNRNKRCKYSYDLNSVYVENNGHGNGFCGRTWDRLQYLSLWIGVGELLTPLAAAGLQDCPKLEEIKIKVEGDCRLWSKPSERAFGLSTLIQYPKLVKMHLDCGDIIGYAHTAPSGQMDLSLWERFYLMGIRHLNLRELDYWPPQDRDVNQRSLSLPAAGLLQECVTLRKLFIHGTAHEHFMMFLLRIPNLRDVQLREDYYPAPENDMSTEMRADSLSRFEVALNRRQICD

[Multiple Choices]
A. nucleus
B. glutamatergic synapse
C. membrane
D. microneme
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record reports experimentally supported localization in both the nucleus and cytoplasm, with IDA annotations for each. Thus nucleus is supported, although the evidence does not establish it as the exclusive or primary site.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence does not show an obvious membrane-spanning region, and micronemes and glutamatergic synapses are specialized compartments not meaningfully indicated by the sequence. But those exclusions do not establish nuclear localization over other non-membrane locations.


**Missing item-specific fact**

> The protein-specific experimental localization showing presence in the nucleus (and cytoplasm) is needed to distinguish the keyed option.


**Reason**

> General sequence-based reasoning can make some distractors unlikely, but it cannot reliably establish nucleus as the primary location for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Nucleus is supported among the listed choices. However, the protein is also annotated in the cytoplasm, which is not offered, so the wording 'primary' is not resolved by the supplied options or evidence.


### Important caveats

- The reviewer-only evidence identifies the sequence as Petunia hybrida F-box protein MAX2 homolog B; that identity and its annotations were absent from the evaluated input.
- The cited localization annotations are direct-assay evidence, but the underlying paper was not independently reviewed here.
- The actual author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence does not show an obvious membrane-spanning region, and micronemes and glutamatergic synapses are specialized compartments not meaningfully indicated by the sequence. But those exclusions do not establish nuclear localization over other non-membrane locations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental localization showing presence in the nucleus (and cytoplasm) is needed to distinguish the keyed option.",
    "reason": "General sequence-based reasoning can make some distractors unlikely, but it cannot reliably establish nucleus as the primary location for this protein."
  },
  "case_id": "GO_cellular_component_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimentally supported localization in both the nucleus and cytoplasm, with IDA annotations for each. Thus nucleus is supported, although the evidence does not establish it as the exclusive or primary site."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies the sequence as Petunia hybrida F-box protein MAX2 homolog B; that identity and its annotations were absent from the evaluated input.",
    "The cited localization annotations are direct-assay evidence, but the underlying paper was not independently reviewed here.",
    "The actual author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Nucleus is supported among the listed choices. However, the protein is also annotated in the cytoplasm, which is not offered, so the wording 'primary' is not resolved by the supplied options or evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimentally supported localization in both the nucleus and cytoplasm, with IDA annotations for each. Thus nucleus is supported, although the evidence does not establish it as the exclusive or primary site.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence does not show an obvious membrane-spanning region, and micronemes and glutamatergic synapses are specialized compartments not meaningfully indicated by the sequence. But those exclusions do not establish nuclear localization over other non-membrane locations.",
    "missing_item_specific_fact": "The protein-specific experimental localization showing presence in the nucleus (and cytoplasm) is needed to distinguish the keyed option.",
    "reason": "General sequence-based reasoning can make some distractors unlikely, but it cannot reliably establish nucleus as the primary location for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Nucleus is supported among the listed choices. However, the protein is also annotated in the cytoplasm, which is not offered, so the wording 'primary' is not resolved by the supplied options or evidence."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies the sequence as Petunia hybrida F-box protein MAX2 homolog B; that identity and its annotations were absent from the evaluated input.",
    "The cited localization annotations are direct-assay evidence, but the underlying paper was not independently reviewed here.",
    "The actual author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry I1SSI6 (PhMAX2B, F-box protein MAX2 homolog B from Petunia hybrida) carries experimentally determined subcellular location annotations (ECO:0000269, IDA) listing Nucleus first and Cytoplasm second. The GO annotation GO:0005634 (nucleus) is supported by IDA evidence from PubMed:38513014. The protein is an F-box/LRR protein functioning as a substrate receptor in SCF ubiquitin ligase complexes, which primarily operate in the nucleus to ubiquitinate transcription factors. The expected answer 'nucleus' is consistent with both the experimental annotation and the general biology of F-box proteins. Although cytoplasm is also annotated with equal evidence strength, it is not among the answer choices, so 'nucleus' is the best-supported option.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is from Petunia hybrida (a plant), which immediately eliminates 'glutamatergic synapse' (B, requires animal neurons) and 'microneme' (D, exclusive to apicomplexan parasites). The sequence contains repeated LRR motifs (multiple LDLS patterns) and an F-box domain, characteristic of SCF ubiquitin ligase substrate receptors. SCF complexes function predominantly in the nucleus to target transcription factors for proteasomal degradation. The sequence lacks obvious transmembrane helices, arguing against 'membrane' (C). These general biological arguments—organism type, domain architecture, and SCF pathway biology—meaningfully distinguish nucleus from the other three options without requiring item-specific lookup.


**Missing item-specific fact**

> None critical. The distinction between nucleus and the three distractors can be made from organism identity (plant), domain architecture (F-box + LRR → SCF → nuclear), and absence of TM domains. The nucleus-vs-cytoplasm ambiguity within the annotation is moot because cytoplasm is not an answer option.


**Reason**

> A knowledgeable model can identify the organism as a plant (eliminating B and D), recognize F-box/LRR architecture pointing to SCF complex function (predominantly nuclear), and note the absence of transmembrane segments (eliminating C). This constitutes a concrete biological reasoning chain from the sequence and general knowledge to the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is annotated in both nucleus and cytoplasm with equal experimental evidence, cytoplasm is not among the four options. Among the given choices (nucleus, glutamatergic synapse, membrane, microneme), only nucleus is biologically defensible for a plant F-box/LRR protein. Options B and D are taxonomically impossible for a plant, and C is inconsistent with the soluble SCF-receptor architecture.


### Important caveats

- The protein is annotated in both nucleus AND cytoplasm with identical evidence strength (IDA from PubMed:38513014). The question's use of 'primary' is somewhat imprecise, but since cytoplasm is not an option, this does not affect answerability.
- The GO annotation for SCF ubiquitin ligase complex (GO:0019005) is IEA:TreeGrafter (computational inference), not experimental, but this is consistent with the well-established nuclear role of F-box proteins.
- The UniProt entry was first released 2025-02-05; the benchmark construction date is unknown. The sequence match is confirmed across all checked versions.
- Recognition of the F-box domain from sequence alone requires some training on domain architectures; however, the LRR repeats are visually apparent and the overall logic (plant + no TM + signaling protein → nuclear) is accessible through general biological reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is from Petunia hybrida (a plant), which immediately eliminates 'glutamatergic synapse' (B, requires animal neurons) and 'microneme' (D, exclusive to apicomplexan parasites). The sequence contains repeated LRR motifs (multiple LDLS patterns) and an F-box domain, characteristic of SCF ubiquitin ligase substrate receptors. SCF complexes function predominantly in the nucleus to target transcription factors for proteasomal degradation. The sequence lacks obvious transmembrane helices, arguing against 'membrane' (C). These general biological arguments—organism type, domain architecture, and SCF pathway biology—meaningfully distinguish nucleus from the other three options without requiring item-specific lookup.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The distinction between nucleus and the three distractors can be made from organism identity (plant), domain architecture (F-box + LRR → SCF → nuclear), and absence of TM domains. The nucleus-vs-cytoplasm ambiguity within the annotation is moot because cytoplasm is not an answer option.",
    "reason": "A knowledgeable model can identify the organism as a plant (eliminating B and D), recognize F-box/LRR architecture pointing to SCF complex function (predominantly nuclear), and note the absence of transmembrane segments (eliminating C). This constitutes a concrete biological reasoning chain from the sequence and general knowledge to the answer."
  },
  "case_id": "GO_cellular_component_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry I1SSI6 (PhMAX2B, F-box protein MAX2 homolog B from Petunia hybrida) carries experimentally determined subcellular location annotations (ECO:0000269, IDA) listing Nucleus first and Cytoplasm second. The GO annotation GO:0005634 (nucleus) is supported by IDA evidence from PubMed:38513014. The protein is an F-box/LRR protein functioning as a substrate receptor in SCF ubiquitin ligase complexes, which primarily operate in the nucleus to ubiquitinate transcription factors. The expected answer 'nucleus' is consistent with both the experimental annotation and the general biology of F-box proteins. Although cytoplasm is also annotated with equal evidence strength, it is not among the answer choices, so 'nucleus' is the best-supported option."
  },
  "important_caveats": [
    "The protein is annotated in both nucleus AND cytoplasm with identical evidence strength (IDA from PubMed:38513014). The question's use of 'primary' is somewhat imprecise, but since cytoplasm is not an option, this does not affect answerability.",
    "The GO annotation for SCF ubiquitin ligase complex (GO:0019005) is IEA:TreeGrafter (computational inference), not experimental, but this is consistent with the well-established nuclear role of F-box proteins.",
    "The UniProt entry was first released 2025-02-05; the benchmark construction date is unknown. The sequence match is confirmed across all checked versions.",
    "Recognition of the F-box domain from sequence alone requires some training on domain architectures; however, the LRR repeats are visually apparent and the overall logic (plant + no TM + signaling protein → nuclear) is accessible through general biological reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is annotated in both nucleus and cytoplasm with equal experimental evidence, cytoplasm is not among the four options. Among the given choices (nucleus, glutamatergic synapse, membrane, microneme), only nucleus is biologically defensible for a plant F-box/LRR protein. Options B and D are taxonomically impossible for a plant, and C is inconsistent with the soluble SCF-receptor architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry I1SSI6 (PhMAX2B, F-box protein MAX2 homolog B from Petunia hybrida) carries experimentally determined subcellular location annotations (ECO:0000269, IDA) listing Nucleus first and Cytoplasm second. The GO annotation GO:0005634 (nucleus) is supported by IDA evidence from PubMed:38513014. The protein is an F-box/LRR protein functioning as a substrate receptor in SCF ubiquitin ligase complexes, which primarily operate in the nucleus to ubiquitinate transcription factors. The expected answer 'nucleus' is consistent with both the experimental annotation and the general biology of F-box proteins. Although cytoplasm is also annotated with equal evidence strength, it is not among the answer choices, so 'nucleus' is the best-supported option.",
    "evidence_ids": ["C5", "C7", "H4", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is from Petunia hybrida (a plant), which immediately eliminates 'glutamatergic synapse' (B, requires animal neurons) and 'microneme' (D, exclusive to apicomplexan parasites). The sequence contains repeated LRR motifs (multiple LDLS patterns) and an F-box domain, characteristic of SCF ubiquitin ligase substrate receptors. SCF complexes function predominantly in the nucleus to target transcription factors for proteasomal degradation. The sequence lacks obvious transmembrane helices, arguing against 'membrane' (C). These general biological arguments—organism type, domain architecture, and SCF pathway biology—meaningfully distinguish nucleus from the other three options without requiring item-specific lookup.",
    "missing_item_specific_fact": "None critical. The distinction between nucleus and the three distractors can be made from organism identity (plant), domain architecture (F-box + LRR → SCF → nuclear), and absence of TM domains. The nucleus-vs-cytoplasm ambiguity within the annotation is moot because cytoplasm is not an answer option.",
    "reason": "A knowledgeable model can identify the organism as a plant (eliminating B and D), recognize F-box/LRR architecture pointing to SCF complex function (predominantly nuclear), and note the absence of transmembrane segments (eliminating C). This constitutes a concrete biological reasoning chain from the sequence and general knowledge to the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is annotated in both nucleus and cytoplasm with equal experimental evidence, cytoplasm is not among the four options. Among the given choices (nucleus, glutamatergic synapse, membrane, microneme), only nucleus is biologically defensible for a plant F-box/LRR protein. Options B and D are taxonomically impossible for a plant, and C is inconsistent with the soluble SCF-receptor architecture."
  },
  "important_caveats": [
    "The protein is annotated in both nucleus AND cytoplasm with identical evidence strength (IDA from PubMed:38513014). The question's use of 'primary' is somewhat imprecise, but since cytoplasm is not an option, this does not affect answerability.",
    "The GO annotation for SCF ubiquitin ligase complex (GO:0019005) is IEA:TreeGrafter (computational inference), not experimental, but this is consistent with the well-established nuclear role of F-box proteins.",
    "The UniProt entry was first released 2025-02-05; the benchmark construction date is unknown. The sequence match is confirmed across all checked versions.",
    "Recognition of the F-box domain from sequence alone requires some training on domain architectures; however, the LRR repeats are visually apparent and the overall logic (plant + no TM + signaling protein → nuclear) is accessible through general biological reasoning."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `I1SSI6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 20. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:51.337813+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38513014","source":"PubMed"}],"id":"SL-0191","value":"Nucleus"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38513014","source":"PubMed"}],"id":"SL-0086","value":"Cytoplasm"}}]}
```

Source SHA-256: `15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)  
**Locator:** `/uniProtKBCrossReferences/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:51.337813+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38513014","source":"PubMed"}],"id":"GO:0005737","properties":[{"key":"GoTerm","value":"C:cytoplasm"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1SSI6.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:51.337813+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38513014","source":"PubMed"}],"id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `15cd9b34157dff5afbb2bfafb1c7c1aa0365c7b7253c6df6aad61e54293d5636`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)  
**Locator:** `lines 48-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:28:53.521456+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:38513014}. Cytoplasm
CC       {ECO:0000269|PubMed:38513014}.
```

Source SHA-256: `a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)  
**Locator:** `lines 62-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:28:53.521456+00:00.  

```text
DR   GO; GO:0005737; C:cytoplasm; IDA:UniProtKB.
```

Source SHA-256: `a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)  
**Locator:** `lines 63-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:28:53.521456+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; IDA:UniProtKB.
```

Source SHA-256: `a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1SSI6?format=txt&versions=20)  
**Locator:** `lines 64-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:28:53.521456+00:00.  

```text
DR   GO; GO:0019005; C:SCF ubiquitin ligase complex; IEA:TreeGrafter.
```

Source SHA-256: `a92b1a2fb6779638a77c9c3017a595351f921a5ea47afb6f28009f6fc6e042ab`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
