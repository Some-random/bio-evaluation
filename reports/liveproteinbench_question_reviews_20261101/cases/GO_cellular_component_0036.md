# GO_cellular_component_0036

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — extracellular space

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNFNRLFILVLVAVLVVLGQQQCGVEAAPRWKFGKKLEKVGKNVFNAAKKALPVVAGYKALG

[Multiple Choices]
A. transcription regulator complex
B. extracellular space
C. endomembrane system
D. phosphopantothenoylcysteine decarboxylase complex
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

> The sequence has a strongly hydrophobic N-terminal stretch consistent with a secretion signal, followed by a short cationic peptide. The sequence-matched UniProt record annotates it as secreted; the historical GO annotation assigns extracellular space, though that GO assignment is computational rather than direct experimental evidence.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is a recognizable secretion signal. For this short peptide, that supports entry into the secretory pathway and an extracellular destination, distinguishing B from intracellular complexes and from the endomembrane system as a transit route.


**Missing item-specific fact**

> No protein-specific fact is necessary to make the likely choice. Direct experimental localization would strengthen confirmation, but is not required for this sequence-based inference.


**Reason**

> The supplied sequence provides a concrete, biologically meaningful localization clue; the answer need not depend solely on recognizing the exact protein or looking up its annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The signal peptide supports secretion and thus extracellular space as the best listed primary location. Temporary passage through endomembrane compartments does not make the endomembrane system an equally defensible primary destination.


### Important caveats

- The supplied evidence includes database annotations, not a retrieved primary experimental localization result. In particular, the historical GO extracellular-space annotation is IEA:TreeGrafter.
- A secretion signal predicts secretory routing but alone does not prove the final localization; the sequence-matched secreted annotation provides additional support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is a recognizable secretion signal. For this short peptide, that supports entry into the secretory pathway and an extracellular destination, distinguishing B from intracellular complexes and from the endomembrane system as a transit route.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific fact is necessary to make the likely choice. Direct experimental localization would strengthen confirmation, but is not required for this sequence-based inference.",
    "reason": "The supplied sequence provides a concrete, biologically meaningful localization clue; the answer need not depend solely on recognizing the exact protein or looking up its annotation."
  },
  "case_id": "GO_cellular_component_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence has a strongly hydrophobic N-terminal stretch consistent with a secretion signal, followed by a short cationic peptide. The sequence-matched UniProt record annotates it as secreted; the historical GO annotation assigns extracellular space, though that GO assignment is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The supplied evidence includes database annotations, not a retrieved primary experimental localization result. In particular, the historical GO extracellular-space annotation is IEA:TreeGrafter.",
    "A secretion signal predicts secretory routing but alone does not prove the final localization; the sequence-matched secreted annotation provides additional support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide supports secretion and thus extracellular space as the best listed primary location. Temporary passage through endomembrane compartments does not make the endomembrane system an equally defensible primary destination."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence has a strongly hydrophobic N-terminal stretch consistent with a secretion signal, followed by a short cationic peptide. The sequence-matched UniProt record annotates it as secreted; the historical GO annotation assigns extracellular space, though that GO assignment is computational rather than direct experimental evidence.",
    "evidence_ids": ["H3", "H4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is a recognizable secretion signal. For this short peptide, that supports entry into the secretory pathway and an extracellular destination, distinguishing B from intracellular complexes and from the endomembrane system as a transit route.",
    "missing_item_specific_fact": "No protein-specific fact is necessary to make the likely choice. Direct experimental localization would strengthen confirmation, but is not required for this sequence-based inference.",
    "reason": "The supplied sequence provides a concrete, biologically meaningful localization clue; the answer need not depend solely on recognizing the exact protein or looking up its annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide supports secretion and thus extracellular space as the best listed primary location. Temporary passage through endomembrane compartments does not make the endomembrane system an equally defensible primary destination."
  },
  "important_caveats": [
    "The supplied evidence includes database annotations, not a retrieved primary experimental localization result. In particular, the historical GO extracellular-space annotation is IEA:TreeGrafter.",
    "A secretion signal predicts secretory routing but alone does not prove the final localization; the sequence-matched secreted annotation provides additional support."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q17NR4 (Cecropin-N, Aedes aegypti) explicitly annotates SUBCELLULAR LOCATION as 'Secreted' (ECO:0000305), and the GO cross-reference includes GO:0005615 (extracellular space, IEA:TreeGrafter) and GO:0005576 (extracellular region, IEA:UniProtKB-SubCell). Cecropins are well-characterized secreted antimicrobial peptides in insects. The sequence (62 aa) contains a clear N-terminal signal peptide (MNFNRLFILVLVAVLVVLG) followed by a short cationic mature peptide, consistent with secretion into the extracellular/hemolymph compartment. The evidence supports choice B.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [C7](#evidence-c7), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region (MNFNRLFILVLVAVLVVLG, residues ~2-19) is a canonical hydrophobic signal peptide that directs the nascent chain into the ER secretory pathway. The mature peptide (residues ~20-62) is very short (~43 aa), highly cationic (rich in K, R), and lacks any transmembrane domain, nuclear localization signal, or catalytic motifs. This pattern—signal peptide + small cationic mature peptide—is the hallmark of secreted antimicrobial peptides (cecropin family). A signal peptide mandates transit through the secretory pathway, and the absence of retention/retrieval signals (e.g., KDEL, KKXX) or transmembrane anchors means the protein is released extracellularly rather than retained in the endomembrane system. Options A (transcription regulator complex) and D (phosphopantothenoylcysteine decarboxylase complex) require nuclear or cytoplasmic catalytic complexes with no supporting sequence features. Option C (endomembrane system) is a plausible distractor because the signal peptide routes through ER/Golgi, but the protein lacks membrane anchors or retention signals and is too small to be an endomembrane resident; it is a cargo that passes through and is secreted.


**Missing item-specific fact**

> None strictly required. Recognizing the sequence as a cecropin would strengthen confidence but is not necessary; the signal-peptide-plus-cationic-peptide pattern is sufficient for general reasoning toward secretion.


**Reason**

> The signal peptide is directly readable from the sequence, and the inference 'signal peptide → secretory pathway → secreted → extracellular' is standard cell biology. The small size and cationic character further exclude endomembrane residency and nuclear/cytoplasmic complex membership. A model with general knowledge of secretory pathway biology and antimicrobial peptide structure can distinguish B from the distractors without memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C (endomembrane system) is the closest distractor because the signal peptide routes the protein through ER/Golgi. However, the GO definition of endomembrane system refers to members that are integral components (ER, Golgi, vesicles, membranes), not transient cargo. A 43-aa cationic peptide with no membrane anchor is not an endomembrane system member. Options A and D are clearly incompatible with the sequence. The wording 'primary Cellular Component' further favors the final destination (extracellular space) over the transit pathway.


### Important caveats

- The 'Secreted' annotation carries evidence code ECO:0000305 (curator inference from published statement), not direct experimental localization data. The GO:0005615 annotation is IEA:TreeGrafter (computational transfer).
- The identity of the protein (Q17NR4, Cecropin-N) was inferred from dataset metadata by the reviewer and was not provided to the evaluated model.
- The sequence is 62 aa and matches both the current and historical UniProt entries exactly.
- Cecropins are well-studied insect antimicrobial peptides secreted into hemolymph; the 'extracellular space' designation is biologically well-founded even though the GO evidence code is computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region (MNFNRLFILVLVAVLVVLG, residues ~2-19) is a canonical hydrophobic signal peptide that directs the nascent chain into the ER secretory pathway. The mature peptide (residues ~20-62) is very short (~43 aa), highly cationic (rich in K, R), and lacks any transmembrane domain, nuclear localization signal, or catalytic motifs. This pattern—signal peptide + small cationic mature peptide—is the hallmark of secreted antimicrobial peptides (cecropin family). A signal peptide mandates transit through the secretory pathway, and the absence of retention/retrieval signals (e.g., KDEL, KKXX) or transmembrane anchors means the protein is released extracellularly rather than retained in the endomembrane system. Options A (transcription regulator complex) and D (phosphopantothenoylcysteine decarboxylase complex) require nuclear or cytoplasmic catalytic complexes with no supporting sequence features. Option C (endomembrane system) is a plausible distractor because the signal peptide routes through ER/Golgi, but the protein lacks membrane anchors or retention signals and is too small to be an endomembrane resident; it is a cargo that passes through and is secreted.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Recognizing the sequence as a cecropin would strengthen confidence but is not necessary; the signal-peptide-plus-cationic-peptide pattern is sufficient for general reasoning toward secretion.",
    "reason": "The signal peptide is directly readable from the sequence, and the inference 'signal peptide → secretory pathway → secreted → extracellular' is standard cell biology. The small size and cationic character further exclude endomembrane residency and nuclear/cytoplasmic complex membership. A model with general knowledge of secretory pathway biology and antimicrobial peptide structure can distinguish B from the distractors without memorizing this specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "C7",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q17NR4 (Cecropin-N, Aedes aegypti) explicitly annotates SUBCELLULAR LOCATION as 'Secreted' (ECO:0000305), and the GO cross-reference includes GO:0005615 (extracellular space, IEA:TreeGrafter) and GO:0005576 (extracellular region, IEA:UniProtKB-SubCell). Cecropins are well-characterized secreted antimicrobial peptides in insects. The sequence (62 aa) contains a clear N-terminal signal peptide (MNFNRLFILVLVAVLVVLG) followed by a short cationic mature peptide, consistent with secretion into the extracellular/hemolymph compartment. The evidence supports choice B."
  },
  "important_caveats": [
    "The 'Secreted' annotation carries evidence code ECO:0000305 (curator inference from published statement), not direct experimental localization data. The GO:0005615 annotation is IEA:TreeGrafter (computational transfer).",
    "The identity of the protein (Q17NR4, Cecropin-N) was inferred from dataset metadata by the reviewer and was not provided to the evaluated model.",
    "The sequence is 62 aa and matches both the current and historical UniProt entries exactly.",
    "Cecropins are well-studied insect antimicrobial peptides secreted into hemolymph; the 'extracellular space' designation is biologically well-founded even though the GO evidence code is computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (endomembrane system) is the closest distractor because the signal peptide routes the protein through ER/Golgi. However, the GO definition of endomembrane system refers to members that are integral components (ER, Golgi, vesicles, membranes), not transient cargo. A 43-aa cationic peptide with no membrane anchor is not an endomembrane system member. Options A and D are clearly incompatible with the sequence. The wording 'primary Cellular Component' further favors the final destination (extracellular space) over the transit pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q17NR4 (Cecropin-N, Aedes aegypti) explicitly annotates SUBCELLULAR LOCATION as 'Secreted' (ECO:0000305), and the GO cross-reference includes GO:0005615 (extracellular space, IEA:TreeGrafter) and GO:0005576 (extracellular region, IEA:UniProtKB-SubCell). Cecropins are well-characterized secreted antimicrobial peptides in insects. The sequence (62 aa) contains a clear N-terminal signal peptide (MNFNRLFILVLVAVLVVLG) followed by a short cationic mature peptide, consistent with secretion into the extracellular/hemolymph compartment. The evidence supports choice B.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "C7", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region (MNFNRLFILVLVAVLVVLG, residues ~2-19) is a canonical hydrophobic signal peptide that directs the nascent chain into the ER secretory pathway. The mature peptide (residues ~20-62) is very short (~43 aa), highly cationic (rich in K, R), and lacks any transmembrane domain, nuclear localization signal, or catalytic motifs. This pattern—signal peptide + small cationic mature peptide—is the hallmark of secreted antimicrobial peptides (cecropin family). A signal peptide mandates transit through the secretory pathway, and the absence of retention/retrieval signals (e.g., KDEL, KKXX) or transmembrane anchors means the protein is released extracellularly rather than retained in the endomembrane system. Options A (transcription regulator complex) and D (phosphopantothenoylcysteine decarboxylase complex) require nuclear or cytoplasmic catalytic complexes with no supporting sequence features. Option C (endomembrane system) is a plausible distractor because the signal peptide routes through ER/Golgi, but the protein lacks membrane anchors or retention signals and is too small to be an endomembrane resident; it is a cargo that passes through and is secreted.",
    "missing_item_specific_fact": "None strictly required. Recognizing the sequence as a cecropin would strengthen confidence but is not necessary; the signal-peptide-plus-cationic-peptide pattern is sufficient for general reasoning toward secretion.",
    "reason": "The signal peptide is directly readable from the sequence, and the inference 'signal peptide → secretory pathway → secreted → extracellular' is standard cell biology. The small size and cationic character further exclude endomembrane residency and nuclear/cytoplasmic complex membership. A model with general knowledge of secretory pathway biology and antimicrobial peptide structure can distinguish B from the distractors without memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (endomembrane system) is the closest distractor because the signal peptide routes the protein through ER/Golgi. However, the GO definition of endomembrane system refers to members that are integral components (ER, Golgi, vesicles, membranes), not transient cargo. A 43-aa cationic peptide with no membrane anchor is not an endomembrane system member. Options A and D are clearly incompatible with the sequence. The wording 'primary Cellular Component' further favors the final destination (extracellular space) over the transit pathway."
  },
  "important_caveats": [
    "The 'Secreted' annotation carries evidence code ECO:0000305 (curator inference from published statement), not direct experimental localization data. The GO:0005615 annotation is IEA:TreeGrafter (computational transfer).",
    "The identity of the protein (Q17NR4, Cecropin-N) was inferred from dataset metadata by the reviewer and was not provided to the evaluated model.",
    "The sequence is 62 aa and matches both the current and historical UniProt entries exactly.",
    "Cecropins are well-studied insect antimicrobial peptides secreted into hemolymph; the 'extracellular space' designation is biologically well-founded even though the GO evidence code is computational."
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

**Accession:** `Q17NR4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 116. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.756541+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0243","value":"Secreted"}}]}
```

Source SHA-256: `5dd5228d85be4155ffeecd2aebc759d532ca9eff89a37d10111f7c7704f7b27e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR4.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.756541+00:00.  

```json
{"database":"GO","id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `5dd5228d85be4155ffeecd2aebc759d532ca9eff89a37d10111f7c7704f7b27e`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR4.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.756541+00:00.  

```json
{"citation":{"authors":["Wei L.","Yang Y.","Zhou Y.","Li M.","Yang H.","Mu L.","Qian Q.","Wu J.","Xu W."],"citationCrossReferences":[{"database":"PubMed","id":"30107813"},{"database":"DOI","id":"10.1186/s13071-018-3000-8"}],"citationType":"journal article","firstPage":"470","id":"30107813","journal":"Parasit. Vectors","lastPage":"470","publicationDate":"2018","title":"Anti-inflammatory activities of Aedes aegypti cecropins and their protection against murine endotoxin shock.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `5dd5228d85be4155ffeecd2aebc759d532ca9eff89a37d10111f7c7704f7b27e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q17NR4?format=txt&versions=116)  
**Locator:** `lines 29-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-01T06:28:29.854070+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION.
RX   PubMed=30107813; DOI=10.1186/s13071-018-3000-8;
RA   Wei L., Yang Y., Zhou Y., Li M., Yang H., Mu L., Qian Q., Wu J., Xu W.;
RT   "Anti-inflammatory activities of Aedes aegypti cecropins and their
RT   protection against murine endotoxin shock.";
RL   Parasit. Vectors 11:470-470(2018).
```

Source SHA-256: `d6ec678e9f74a2840167360e83614a6e35275d974e8fa612780550f8a53569f1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q17NR4?format=txt&versions=116)  
**Locator:** `lines 44-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-01T06:28:29.854070+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305}.
```

Source SHA-256: `d6ec678e9f74a2840167360e83614a6e35275d974e8fa612780550f8a53569f1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q17NR4?format=txt&versions=116)  
**Locator:** `lines 64-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-01T06:28:29.854070+00:00.  

```text
DR   GO; GO:0005615; C:extracellular space; IEA:TreeGrafter.
```

Source SHA-256: `d6ec678e9f74a2840167360e83614a6e35275d974e8fa612780550f8a53569f1`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 36. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
