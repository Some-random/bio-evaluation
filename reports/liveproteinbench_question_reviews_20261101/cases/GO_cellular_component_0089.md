# GO_cellular_component_0089

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — monoatomic ion channel complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDGSHCKVIAPLLTERHQRMVTKDGHSTLQMDGAQTGLAYLRDAWGILMDMRWRWMMLVFSASFVIHWLVFAVLWYILAEMNGDLGLDHDAPPENHTICVKYITSFTAAFSFSLETQLTIGYGTMFPSGDCPSAIALLAIQMLLGLMLEAFITGAFVAKIARPKNRAFSIRFTDLAVVAHIDGKPNLIFQVANTRPSPLTNVRVSAVLYQERENGKLYQTSVDFHLDGISSEECPFFIFPLTYYHSIIPSSPLATLLQHENPPHFELVVFLSAMQEGTGETCQRRTSYLPSEIMLHHCFASLLARGSKGEYQIKMENFDKTTPEFQTPLVSKSPNRTDLDIHINGQSIDNFQISETGLTE

[Multiple Choices]
A. neuron projection
B. H3 histone acetyltransferase complex
C. host cell mitochondrion
D. monoatomic ion channel complex
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

> The sequence-matched UniProt record annotates GO:0034702, “monoatomic ion channel complex,” although the archived annotation is IEA (keyword-based), not direct experimental evidence. The entry also identifies the protein as an inward-rectifier potassium channel; that name is supported by similarity evidence.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear multipass membrane-protein pattern, including hydrophobic transmembrane segments consistent with the architecture of an ion channel. Among the choices, an ion-channel complex is a substantially better fit than a neuron projection, a histone acetyltransferase complex, or a host-cell mitochondrion.


**Missing item-specific fact**

> The exact protein identity and its database GO annotation are not supplied, but are not necessary to distinguish D from these choices using the sequence and general biological knowledge.


**Reason**

> The sequence provides meaningful evidence for a membrane ion channel, while the alternatives describe unrelated cellular structures or complexes. This supports a defensible choice without relying on recall of the exact database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence’s membrane-channel features distinguish D from the offered alternatives; no other option is comparably supported.


### Important caveats

- The cited GO annotation is computationally inferred, not experimental confirmation of complex membership.
- The subcellular-location annotation in the matched record is also supported by similarity evidence; the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear multipass membrane-protein pattern, including hydrophobic transmembrane segments consistent with the architecture of an ion channel. Among the choices, an ion-channel complex is a substantially better fit than a neuron projection, a histone acetyltransferase complex, or a host-cell mitochondrion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein identity and its database GO annotation are not supplied, but are not necessary to distinguish D from these choices using the sequence and general biological knowledge.",
    "reason": "The sequence provides meaningful evidence for a membrane ion channel, while the alternatives describe unrelated cellular structures or complexes. This supports a defensible choice without relying on recall of the exact database entry."
  },
  "case_id": "GO_cellular_component_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates GO:0034702, “monoatomic ion channel complex,” although the archived annotation is IEA (keyword-based), not direct experimental evidence. The entry also identifies the protein as an inward-rectifier potassium channel; that name is supported by similarity evidence."
  },
  "important_caveats": [
    "The cited GO annotation is computationally inferred, not experimental confirmation of complex membership.",
    "The subcellular-location annotation in the matched record is also supported by similarity evidence; the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence’s membrane-channel features distinguish D from the offered alternatives; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates GO:0034702, “monoatomic ion channel complex,” although the archived annotation is IEA (keyword-based), not direct experimental evidence. The entry also identifies the protein as an inward-rectifier potassium channel; that name is supported by similarity evidence.",
    "evidence_ids": ["H1", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear multipass membrane-protein pattern, including hydrophobic transmembrane segments consistent with the architecture of an ion channel. Among the choices, an ion-channel complex is a substantially better fit than a neuron projection, a histone acetyltransferase complex, or a host-cell mitochondrion.",
    "missing_item_specific_fact": "The exact protein identity and its database GO annotation are not supplied, but are not necessary to distinguish D from these choices using the sequence and general biological knowledge.",
    "reason": "The sequence provides meaningful evidence for a membrane ion channel, while the alternatives describe unrelated cellular structures or complexes. This supports a defensible choice without relying on recall of the exact database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence’s membrane-channel features distinguish D from the offered alternatives; no other option is comparably supported."
  },
  "important_caveats": [
    "The cited GO annotation is computationally inferred, not experimental confirmation of complex membership.",
    "The subcellular-location annotation in the matched record is also supported by similarity evidence; the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is UniProt E1BN00, annotated as 'Inward rectifier potassium channel 13' (Kir7.1) from Bos taurus. A potassium channel is by definition a monoatomic ion channel complex (GO:0034702), and this GO term is present in the UniProt record (evidence C6/H3, IEA:UniProtKB-KW). The protein's identity as a potassium channel is well-established (it is in the recommended name, supported by similarity to O60928). While the GO annotation evidence code is IEA (electronic/keyword-based inference rather than direct experiment on this bovine ortholog), the protein's classification as a Kir-family channel is robust and the GO term accurately describes its molecular identity.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches (~20+ residues) consistent with multi-pass transmembrane topology, which could help rule out B (nuclear histone acetyltransferase complex) and partially C (host cell mitochondrion, which typically requires an N-terminal amphipathic mitochondrial targeting sequence absent here). However, distinguishing 'monoatomic ion channel complex' (D) from 'neuron projection' (A) cannot be resolved by general sequence reasoning: both could host membrane proteins, and the hydrophobic pattern does not uniquely identify an ion channel versus a transporter, receptor, or other membrane protein. Recognizing the Kir-specific two-TM + pore-loop architecture from raw sequence without database context is not reliably achievable.


**Missing item-specific fact**

> The specific identity of this 360-aa sequence as Kir7.1 (KCNJ13), a member of the inward rectifier potassium channel family, which is required to confidently assign 'monoatomic ion channel complex' over 'neuron projection' or other membrane-associated options.


**Reason**

> General sequence analysis reveals a small multi-pass membrane protein, which is suggestive but not diagnostic of an ion channel complex specifically. The critical step—identifying the Kir channel fold and thus the GO term 'monoatomic ion channel complex'—depends on recognizing this exact protein or its family from training data or database lookup, not on a deductive argument from the sequence features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> From sequence alone, a multi-pass membrane protein could plausibly reside in a neuron projection (A), as many ion channels and membrane proteins are localized to axons/dendrites. Without knowing the protein is Kir7.1 in retinal pigmented epithelium, the sequence does not exclude neuronal localization. Additionally, GO:0034702 describes a molecular complex rather than a spatial compartment, making 'primary cellular component' slightly ambiguous when compared to location-type terms like A and C.


### Important caveats

- The GO annotation for 'monoatomic ion channel complex' carries IEA (Inferred from Electronic Annotation) evidence, not direct experimental proof for this bovine ortholog; the protein's channel identity is inferred by similarity to human Kir7.1 (O60928).
- The subcellular location annotation (C5/H2) specifies 'Cell membrane, Multi-pass membrane protein' localized at RPE apical microvilli, which is a spatial location distinct from the complex-level term in choice D.
- The UniProt entry was first publicly released 2025-06-18; the benchmark construction date and whether this entry existed in the author's source snapshot are unknown.
- Choice C ('host cell mitochondrion') is a GO term relevant to pathogen-host interactions and is not applicable to a bovine endogenous protein, making it a clearly wrong distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (~20+ residues) consistent with multi-pass transmembrane topology, which could help rule out B (nuclear histone acetyltransferase complex) and partially C (host cell mitochondrion, which typically requires an N-terminal amphipathic mitochondrial targeting sequence absent here). However, distinguishing 'monoatomic ion channel complex' (D) from 'neuron projection' (A) cannot be resolved by general sequence reasoning: both could host membrane proteins, and the hydrophobic pattern does not uniquely identify an ion channel versus a transporter, receptor, or other membrane protein. Recognizing the Kir-specific two-TM + pore-loop architecture from raw sequence without database context is not reliably achievable.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this 360-aa sequence as Kir7.1 (KCNJ13), a member of the inward rectifier potassium channel family, which is required to confidently assign 'monoatomic ion channel complex' over 'neuron projection' or other membrane-associated options.",
    "reason": "General sequence analysis reveals a small multi-pass membrane protein, which is suggestive but not diagnostic of an ion channel complex specifically. The critical step—identifying the Kir channel fold and thus the GO term 'monoatomic ion channel complex'—depends on recognizing this exact protein or its family from training data or database lookup, not on a deductive argument from the sequence features alone."
  },
  "case_id": "GO_cellular_component_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "H1",
      "H3",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein is UniProt E1BN00, annotated as 'Inward rectifier potassium channel 13' (Kir7.1) from Bos taurus. A potassium channel is by definition a monoatomic ion channel complex (GO:0034702), and this GO term is present in the UniProt record (evidence C6/H3, IEA:UniProtKB-KW). The protein's identity as a potassium channel is well-established (it is in the recommended name, supported by similarity to O60928). While the GO annotation evidence code is IEA (electronic/keyword-based inference rather than direct experiment on this bovine ortholog), the protein's classification as a Kir-family channel is robust and the GO term accurately describes its molecular identity."
  },
  "important_caveats": [
    "The GO annotation for 'monoatomic ion channel complex' carries IEA (Inferred from Electronic Annotation) evidence, not direct experimental proof for this bovine ortholog; the protein's channel identity is inferred by similarity to human Kir7.1 (O60928).",
    "The subcellular location annotation (C5/H2) specifies 'Cell membrane, Multi-pass membrane protein' localized at RPE apical microvilli, which is a spatial location distinct from the complex-level term in choice D.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date and whether this entry existed in the author's source snapshot are unknown.",
    "Choice C ('host cell mitochondrion') is a GO term relevant to pathogen-host interactions and is not applicable to a bovine endogenous protein, making it a clearly wrong distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "From sequence alone, a multi-pass membrane protein could plausibly reside in a neuron projection (A), as many ion channels and membrane proteins are localized to axons/dendrites. Without knowing the protein is Kir7.1 in retinal pigmented epithelium, the sequence does not exclude neuronal localization. Additionally, GO:0034702 describes a molecular complex rather than a spatial compartment, making 'primary cellular component' slightly ambiguous when compared to location-type terms like A and C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is UniProt E1BN00, annotated as 'Inward rectifier potassium channel 13' (Kir7.1) from Bos taurus. A potassium channel is by definition a monoatomic ion channel complex (GO:0034702), and this GO term is present in the UniProt record (evidence C6/H3, IEA:UniProtKB-KW). The protein's identity as a potassium channel is well-established (it is in the recommended name, supported by similarity to O60928). While the GO annotation evidence code is IEA (electronic/keyword-based inference rather than direct experiment on this bovine ortholog), the protein's classification as a Kir-family channel is robust and the GO term accurately describes its molecular identity.",
    "evidence_ids": ["C4", "C6", "H1", "H3", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (~20+ residues) consistent with multi-pass transmembrane topology, which could help rule out B (nuclear histone acetyltransferase complex) and partially C (host cell mitochondrion, which typically requires an N-terminal amphipathic mitochondrial targeting sequence absent here). However, distinguishing 'monoatomic ion channel complex' (D) from 'neuron projection' (A) cannot be resolved by general sequence reasoning: both could host membrane proteins, and the hydrophobic pattern does not uniquely identify an ion channel versus a transporter, receptor, or other membrane protein. Recognizing the Kir-specific two-TM + pore-loop architecture from raw sequence without database context is not reliably achievable.",
    "missing_item_specific_fact": "The specific identity of this 360-aa sequence as Kir7.1 (KCNJ13), a member of the inward rectifier potassium channel family, which is required to confidently assign 'monoatomic ion channel complex' over 'neuron projection' or other membrane-associated options.",
    "reason": "General sequence analysis reveals a small multi-pass membrane protein, which is suggestive but not diagnostic of an ion channel complex specifically. The critical step—identifying the Kir channel fold and thus the GO term 'monoatomic ion channel complex'—depends on recognizing this exact protein or its family from training data or database lookup, not on a deductive argument from the sequence features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "From sequence alone, a multi-pass membrane protein could plausibly reside in a neuron projection (A), as many ion channels and membrane proteins are localized to axons/dendrites. Without knowing the protein is Kir7.1 in retinal pigmented epithelium, the sequence does not exclude neuronal localization. Additionally, GO:0034702 describes a molecular complex rather than a spatial compartment, making 'primary cellular component' slightly ambiguous when compared to location-type terms like A and C."
  },
  "important_caveats": [
    "The GO annotation for 'monoatomic ion channel complex' carries IEA (Inferred from Electronic Annotation) evidence, not direct experimental proof for this bovine ortholog; the protein's channel identity is inferred by similarity to human Kir7.1 (O60928).",
    "The subcellular location annotation (C5/H2) specifies 'Cell membrane, Multi-pass membrane protein' localized at RPE apical microvilli, which is a spatial location distinct from the complex-level term in choice D.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date and whether this entry existed in the author's source snapshot are unknown.",
    "Choice C ('host cell mitochondrion') is a GO term relevant to pathogen-host interactions and is not applicable to a bovine endogenous protein, making it a clearly wrong distractor."
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

**Accession:** `E1BN00` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 85. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:00.720540+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"O60928","source":"UniProtKB"}],"value":"Inward rectifier K(+) channel Kir7.1"}},{"fullName":{"value":"Potassium channel, inwardly rectifying subfamily J member 13"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"O60928","source":"UniProtKB"}],"value":"Inward rectifier potassium channel 13"}}}
```

Source SHA-256: `7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:00.720540+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P86046","source":"UniProtKB"}],"value":"Localized at the retinal pigmented epithelium (RPE) apical microvilli"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-0162","value":"Membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P86046","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"}}]}
```

Source SHA-256: `7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)  
**Locator:** `/uniProtKBCrossReferences/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:00.720540+00:00.  

```json
{"database":"GO","id":"GO:0034702","properties":[{"key":"GoTerm","value":"C:monoatomic ion channel complex"},{"key":"GoEvidenceType","value":"IEA:Ensembl"}]}
```

Source SHA-256: `7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:28:05.462686+00:00.  

```text
ID   KCJ13_BOVIN             Reviewed;         360 AA.
AC   E1BN00;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-NOV-2010, sequence version 1.
DT   28-JAN-2026, entry version 85.
DE   RecName: Full=Inward rectifier potassium channel 13 {ECO:0000250|UniProtKB:O60928};
DE   AltName: Full=Inward rectifier K(+) channel Kir7.1 {ECO:0000250|UniProtKB:O60928};
DE   AltName: Full=Potassium channel, inwardly rectifying subfamily J member 13;
GN   Name=KCNJ13;
OS   Bos taurus (Bovine).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Laurasiatheria; Artiodactyla; Ruminantia; Pecora; Bovidae;
OC   Bovinae; Bos.
OX   NCBI_TaxID=9913;
```

Source SHA-256: `4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)  
**Locator:** `lines 52-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:28:05.462686+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Multi-pass membrane
CC       protein {ECO:0000255}. Cell membrane {ECO:0000250|UniProtKB:P86046}.
CC       Note=Localized at the retinal pigmented epithelium (RPE) apical
CC       microvilli. {ECO:0000250|UniProtKB:P86046}.
```

Source SHA-256: `4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)  
**Locator:** `lines 87-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:28:05.462686+00:00.  

```text
DR   GO; GO:0034702; C:monoatomic ion channel complex; IEA:UniProtKB-KW.
```

Source SHA-256: `4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 211424-211430`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0034702
name: monoatomic ion channel complex
namespace: cellular_component
def: "A protein complex that spans a membrane and forms a water-filled channel across the phospholipid bilayer allowing selective monoatomic ion transport down its electrochemical gradient." [GOC:mah, ISBN:071673706X]
is_a: GO:1902495 ! transmembrane transporter complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 89. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
