# GO_cellular_component_0033

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — mitochondrial inner membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASGQMAPSLLRRPITFVSSCPPALRSFGALCPPTGSTDLIGGTGRDILIAAAPARRAPLHATLPLLRSLHTSPAPQLSASHQHQAQQQQQQTKQPQQPYDPQQDQVPSTSTASSSKPAADPVYNLPNAVSVARLVSGPLIGYWLVQGHYEAATLALAVSGASDWLDGWLARRLGASSVFGSYLDPLADKVLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTSAAAAGAATGAANGVASGGGGGGEGVSFMRPLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK

[Multiple Choices]
A. egg coat
B. mitochondrial inner membrane
C. glutamatergic synapse
D. NF-kappaB p50/p65 complex
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

> The exact sequence matches a UniProt record annotated to the mitochondrial inner membrane and as a multipass membrane protein. The annotation is transferred from a homolog (ECO:0000250), and the GO assignment is ISS, so this supports the key as a database annotation but is not direct experimental localization evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's multiple hydrophobic regions support a multipass membrane protein, making the membrane option more plausible than the egg-coat or NF-kappaB-complex choices. But that feature alone does not establish mitochondrial localization or distinguish it from other membrane-associated locations.


**Missing item-specific fact**

> The protein-specific identification as cardiolipin synthase and its homolog-transferred mitochondrial inner-membrane localization are not supplied in the question.


**Reason**

> A broad sequence-based membrane inference does not resolve the organelle-specific location asked for. Selecting B with confidence depends on protein-specific annotation or equivalent external knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence does not reliably establish an alternative listed location; the main limitation is that it does not determine the mitochondrial location without protein-specific information.


### Important caveats

- The historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.
- The location evidence is homolog-transferred rather than direct experimental evidence for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's multiple hydrophobic regions support a multipass membrane protein, making the membrane option more plausible than the egg-coat or NF-kappaB-complex choices. But that feature alone does not establish mitochondrial localization or distinguish it from other membrane-associated locations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as cardiolipin synthase and its homolog-transferred mitochondrial inner-membrane localization are not supplied in the question.",
    "reason": "A broad sequence-based membrane inference does not resolve the organelle-specific location asked for. Selecting B with confidence depends on protein-specific annotation or equivalent external knowledge."
  },
  "case_id": "GO_cellular_component_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to the mitochondrial inner membrane and as a multipass membrane protein. The annotation is transferred from a homolog (ECO:0000250), and the GO assignment is ISS, so this supports the key as a database annotation but is not direct experimental localization evidence."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The location evidence is homolog-transferred rather than direct experimental evidence for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not reliably establish an alternative listed location; the main limitation is that it does not determine the mitochondrial location without protein-specific information."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to the mitochondrial inner membrane and as a multipass membrane protein. The annotation is transferred from a homolog (ECO:0000250), and the GO assignment is ISS, so this supports the key as a database annotation but is not direct experimental localization evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's multiple hydrophobic regions support a multipass membrane protein, making the membrane option more plausible than the egg-coat or NF-kappaB-complex choices. But that feature alone does not establish mitochondrial localization or distinguish it from other membrane-associated locations.",
    "missing_item_specific_fact": "The protein-specific identification as cardiolipin synthase and its homolog-transferred mitochondrial inner-membrane localization are not supplied in the question.",
    "reason": "A broad sequence-based membrane inference does not resolve the organelle-specific location asked for. Selecting B with confidence depends on protein-specific annotation or equivalent external knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not reliably establish an alternative listed location; the main limitation is that it does not determine the mitochondrial location without protein-specific information."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The location evidence is homolog-transferred rather than direct experimental evidence for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A2K3D1C8 annotates the protein as Cardiolipin synthase (CMP-forming, EC 2.7.8.41) from Chlamydomonas reinhardtii with subcellular location 'Mitochondrion inner membrane' and GO:0005743 (C:mitochondrial inner membrane). The evidence code is ISS (ECO:0000250), transferred by similarity to human CRLS1 (Q93YW7), not directly experimental for this protein. However, cardiolipin synthase is a well-characterized mitochondrial inner membrane enzyme across eukaryotes, and the sequence is consistent with a multi-pass membrane protein with a plausible N-terminal mitochondrial targeting region. The annotation is computationally inferred rather than experimentally validated for this specific protein, but the biological reasoning is strong.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches in the C-terminal ~250 residues (e.g., 'LIGYWLVQGHYEAATLALAVSGASDWLDGWLARR', 'VLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRT', 'PLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK'), indicating a multi-pass membrane protein. The N-terminal ~100 residues show features of a mitochondrial targeting signal (positively charged R/K residues interspersed with hydroxylated S/T residues, amphipathic character). Among the four options, only 'mitochondrial inner membrane' (B) is a membrane compartment. The other three are clearly incompatible: 'egg coat' (A) is an extracellular matrix of animal ova; 'glutamatergic synapse' (C) is an animal neural structure absent in green algae; 'NF-kappaB p50/p65 complex' (D) is a vertebrate immune-signaling protein complex, not a membrane. Elimination plus visible multi-pass membrane topology plus mitochondrial targeting signal features provide a defensible reasoning path to B.


**Missing item-specific fact**

> Precise identification of the enzyme as cardiolipin synthase (CDP-alcohol transferase family) from sequence motifs alone would require database lookup, but is not strictly necessary given the strong elimination of non-membrane and animal-specific distractors.


**Reason**

> A model with general knowledge of membrane protein topology, mitochondrial targeting signals, and the biology of the distractor compartments can distinguish B from A, C, and D without memorizing this specific protein's annotation. The distractors are very clearly wrong for a multi-pass membrane protein from a unicellular green alga.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are all strongly incompatible with the observed sequence features: A (egg coat) is an extracellular animal structure, C (glutamatergic synapse) is an animal neural structure, D (NF-kappaB complex) is a vertebrate protein complex. None are membrane compartments. Only B is a membrane compartment, and the sequence clearly encodes a multi-pass membrane protein. No ambiguity exists among the options.


### Important caveats

- The mitochondrial inner membrane localization annotation carries evidence code ISS (inferred from sequence similarity to human CRLS1/Q93YW7), not direct experimental evidence for this Chlamydomonas protein.
- The N-terminal region (~100 aa) is unusually long and compositionally atypical for a canonical mitochondrial targeting signal; it may include a disordered linker in addition to the targeting peptide.
- The protein is from Chlamydomonas reinhardtii (green alga), making the animal-specific distractors (egg coat, glutamatergic synapse, NF-kappaB) particularly easy to eliminate for a knowledgeable reasoner.
- The GO annotation is ISS:UniProtKB, meaning it was propagated by computational similarity rather than direct subcellular fractionation or fluorescence microscopy in this organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches in the C-terminal ~250 residues (e.g., 'LIGYWLVQGHYEAATLALAVSGASDWLDGWLARR', 'VLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRT', 'PLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK'), indicating a multi-pass membrane protein. The N-terminal ~100 residues show features of a mitochondrial targeting signal (positively charged R/K residues interspersed with hydroxylated S/T residues, amphipathic character). Among the four options, only 'mitochondrial inner membrane' (B) is a membrane compartment. The other three are clearly incompatible: 'egg coat' (A) is an extracellular matrix of animal ova; 'glutamatergic synapse' (C) is an animal neural structure absent in green algae; 'NF-kappaB p50/p65 complex' (D) is a vertebrate immune-signaling protein complex, not a membrane. Elimination plus visible multi-pass membrane topology plus mitochondrial targeting signal features provide a defensible reasoning path to B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the enzyme as cardiolipin synthase (CDP-alcohol transferase family) from sequence motifs alone would require database lookup, but is not strictly necessary given the strong elimination of non-membrane and animal-specific distractors.",
    "reason": "A model with general knowledge of membrane protein topology, mitochondrial targeting signals, and the biology of the distractor compartments can distinguish B from A, C, and D without memorizing this specific protein's annotation. The distractors are very clearly wrong for a multi-pass membrane protein from a unicellular green alga."
  },
  "case_id": "GO_cellular_component_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A2K3D1C8 annotates the protein as Cardiolipin synthase (CMP-forming, EC 2.7.8.41) from Chlamydomonas reinhardtii with subcellular location 'Mitochondrion inner membrane' and GO:0005743 (C:mitochondrial inner membrane). The evidence code is ISS (ECO:0000250), transferred by similarity to human CRLS1 (Q93YW7), not directly experimental for this protein. However, cardiolipin synthase is a well-characterized mitochondrial inner membrane enzyme across eukaryotes, and the sequence is consistent with a multi-pass membrane protein with a plausible N-terminal mitochondrial targeting region. The annotation is computationally inferred rather than experimentally validated for this specific protein, but the biological reasoning is strong."
  },
  "important_caveats": [
    "The mitochondrial inner membrane localization annotation carries evidence code ISS (inferred from sequence similarity to human CRLS1/Q93YW7), not direct experimental evidence for this Chlamydomonas protein.",
    "The N-terminal region (~100 aa) is unusually long and compositionally atypical for a canonical mitochondrial targeting signal; it may include a disordered linker in addition to the targeting peptide.",
    "The protein is from Chlamydomonas reinhardtii (green alga), making the animal-specific distractors (egg coat, glutamatergic synapse, NF-kappaB) particularly easy to eliminate for a knowledgeable reasoner.",
    "The GO annotation is ISS:UniProtKB, meaning it was propagated by computational similarity rather than direct subcellular fractionation or fluorescence microscopy in this organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are all strongly incompatible with the observed sequence features: A (egg coat) is an extracellular animal structure, C (glutamatergic synapse) is an animal neural structure, D (NF-kappaB complex) is a vertebrate protein complex. None are membrane compartments. Only B is a membrane compartment, and the sequence clearly encodes a multi-pass membrane protein. No ambiguity exists among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A2K3D1C8 annotates the protein as Cardiolipin synthase (CMP-forming, EC 2.7.8.41) from Chlamydomonas reinhardtii with subcellular location 'Mitochondrion inner membrane' and GO:0005743 (C:mitochondrial inner membrane). The evidence code is ISS (ECO:0000250), transferred by similarity to human CRLS1 (Q93YW7), not directly experimental for this protein. However, cardiolipin synthase is a well-characterized mitochondrial inner membrane enzyme across eukaryotes, and the sequence is consistent with a multi-pass membrane protein with a plausible N-terminal mitochondrial targeting region. The annotation is computationally inferred rather than experimentally validated for this specific protein, but the biological reasoning is strong.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches in the C-terminal ~250 residues (e.g., 'LIGYWLVQGHYEAATLALAVSGASDWLDGWLARR', 'VLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRT', 'PLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK'), indicating a multi-pass membrane protein. The N-terminal ~100 residues show features of a mitochondrial targeting signal (positively charged R/K residues interspersed with hydroxylated S/T residues, amphipathic character). Among the four options, only 'mitochondrial inner membrane' (B) is a membrane compartment. The other three are clearly incompatible: 'egg coat' (A) is an extracellular matrix of animal ova; 'glutamatergic synapse' (C) is an animal neural structure absent in green algae; 'NF-kappaB p50/p65 complex' (D) is a vertebrate immune-signaling protein complex, not a membrane. Elimination plus visible multi-pass membrane topology plus mitochondrial targeting signal features provide a defensible reasoning path to B.",
    "missing_item_specific_fact": "Precise identification of the enzyme as cardiolipin synthase (CDP-alcohol transferase family) from sequence motifs alone would require database lookup, but is not strictly necessary given the strong elimination of non-membrane and animal-specific distractors.",
    "reason": "A model with general knowledge of membrane protein topology, mitochondrial targeting signals, and the biology of the distractor compartments can distinguish B from A, C, and D without memorizing this specific protein's annotation. The distractors are very clearly wrong for a multi-pass membrane protein from a unicellular green alga."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are all strongly incompatible with the observed sequence features: A (egg coat) is an extracellular animal structure, C (glutamatergic synapse) is an animal neural structure, D (NF-kappaB complex) is a vertebrate protein complex. None are membrane compartments. Only B is a membrane compartment, and the sequence clearly encodes a multi-pass membrane protein. No ambiguity exists among the options."
  },
  "important_caveats": [
    "The mitochondrial inner membrane localization annotation carries evidence code ISS (inferred from sequence similarity to human CRLS1/Q93YW7), not direct experimental evidence for this Chlamydomonas protein.",
    "The N-terminal region (~100 aa) is unusually long and compositionally atypical for a canonical mitochondrial targeting signal; it may include a disordered linker in addition to the targeting peptide.",
    "The protein is from Chlamydomonas reinhardtii (green alga), making the animal-specific distractors (egg coat, glutamatergic synapse, NF-kappaB) particularly easy to eliminate for a knowledgeable reasoner.",
    "The GO annotation is ISS:UniProtKB, meaning it was propagated by computational similarity rather than direct subcellular fractionation or fluorescence microscopy in this organism."
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

**Accession:** `A0A2K3D1C8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"26793177","source":"PubMed"}],"value":"2.7.8.41"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cardiolipin synthase (CMP-forming)"},"shortNames":[{"value":"CLS"}]}}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q93YW7","source":"UniProtKB"}],"id":"SL-0168","value":"Mitochondrion inner membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q93YW7","source":"UniProtKB"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"database":"GO","id":"GO:0005743","properties":[{"key":"GoTerm","value":"C:mitochondrial inner membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 69-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion inner membrane
CC       {ECO:0000250|UniProtKB:Q93YW7}; Multi-pass membrane protein
CC       {ECO:0000250|UniProtKB:Q93YW7}.
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 94-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
DR   GO; GO:0005743; C:mitochondrial inner membrane; ISS:UniProtKB.
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 95-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IBA:GO_Central.
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
