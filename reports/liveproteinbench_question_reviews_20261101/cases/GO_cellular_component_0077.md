# GO_cellular_component_0077

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — protein-DNA complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | uncertain | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSEKIVVVDDEKEIADLVTTFLQNEGFSVQPFYDGTSAIAYIEKEAIDLAVLDVMLPDIDGFQLLQQIRKTHFFPVLMLTAKGEDLDKITGLSLGADDYVTKPFNPLEVVARVKTQLRRYQRYNHSTASPTVEEYEKDGLILKINSHQCILYGKEVFLTPIEFKILLYLFEHQGSVVSSETLFEAVWKEKYLDNNNTVMAHIARLREKLHEEPRKPKLIKTVWGVGYIIEK

[Multiple Choices]
A. host cell cytoplasm
B. protein-DNA complex
C. host cell
D. cell leading edge
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

> The exact sequence matches a UniProt record annotated to protein-DNA complex (GO:0032993), supporting B as a database-assigned answer. This assignment is computational (IEA:TreeGrafter), not experimental evidence that the protein is predominantly present in that complex. The same record also includes cytoplasm/cytosol annotations.

Citations as saved: [C8](#evidence-c8), [H5](#evidence-h5), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A response-regulator-like protein with a DNA-binding function could plausibly associate with DNA, but that does not establish that its primary cellular component is a protein-DNA complex rather than the cytoplasm.


**Missing item-specific fact**

> The protein-specific GO annotation to protein-DNA complex, or experimental evidence about its association with DNA in the relevant context, is absent from the question input.


**Reason**

> The sequence may support a broad functional inference, but distinguishing a protein-DNA complex from cytoplasmic residence as the primary component requires an item-specific annotation or measurement.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The record also annotates cytoplasm/cytosol, but the listed alternative is specifically host cell cytoplasm, not generic bacterial cytoplasm. The two recorded annotations indicate that cellular residence and complex membership can coexist, so the singular word “primary” is not established experimentally; however, no other listed option is directly supported by the supplied reviewer evidence.


### Important caveats

- The protein-DNA complex annotation is computationally inferred, not shown here to be experimentally validated.
- The UniProt cytoplasm annotation is transferred by similarity, and the cytosol annotation is computationally inferred.
- The source snapshot used by the original author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A response-regulator-like protein with a DNA-binding function could plausibly associate with DNA, but that does not establish that its primary cellular component is a protein-DNA complex rather than the cytoplasm.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific GO annotation to protein-DNA complex, or experimental evidence about its association with DNA in the relevant context, is absent from the question input.",
    "reason": "The sequence may support a broad functional inference, but distinguishing a protein-DNA complex from cytoplasmic residence as the primary component requires an item-specific annotation or measurement."
  },
  "case_id": "GO_cellular_component_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H5",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to protein-DNA complex (GO:0032993), supporting B as a database-assigned answer. This assignment is computational (IEA:TreeGrafter), not experimental evidence that the protein is predominantly present in that complex. The same record also includes cytoplasm/cytosol annotations."
  },
  "important_caveats": [
    "The protein-DNA complex annotation is computationally inferred, not shown here to be experimentally validated.",
    "The UniProt cytoplasm annotation is transferred by similarity, and the cytosol annotation is computationally inferred.",
    "The source snapshot used by the original author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also annotates cytoplasm/cytosol, but the listed alternative is specifically host cell cytoplasm, not generic bacterial cytoplasm. The two recorded annotations indicate that cellular residence and complex membership can coexist, so the singular word “primary” is not established experimentally; however, no other listed option is directly supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to protein-DNA complex (GO:0032993), supporting B as a database-assigned answer. This assignment is computational (IEA:TreeGrafter), not experimental evidence that the protein is predominantly present in that complex. The same record also includes cytoplasm/cytosol annotations.",
    "evidence_ids": ["C8", "H5", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A response-regulator-like protein with a DNA-binding function could plausibly associate with DNA, but that does not establish that its primary cellular component is a protein-DNA complex rather than the cytoplasm.",
    "missing_item_specific_fact": "The protein-specific GO annotation to protein-DNA complex, or experimental evidence about its association with DNA in the relevant context, is absent from the question input.",
    "reason": "The sequence may support a broad functional inference, but distinguishing a protein-DNA complex from cytoplasmic residence as the primary component requires an item-specific annotation or measurement."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also annotates cytoplasm/cytosol, but the listed alternative is specifically host cell cytoplasm, not generic bacterial cytoplasm. The two recorded annotations indicate that cellular residence and complex membership can coexist, so the singular word “primary” is not established experimentally; however, no other listed option is directly supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The protein-DNA complex annotation is computationally inferred, not shown here to be experimentally validated.",
    "The UniProt cytoplasm annotation is transferred by similarity, and the cytosol annotation is computationally inferred.",
    "The source snapshot used by the original author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: uncertain

> GO:0032993 (protein-DNA complex) IS annotated to Q9KJT4 (evidence C8, H5), but only via IEA:TreeGrafter (automated). The UniProt primary subcellular location comment states 'Cytoplasm' (C5, H3, ECO:0000250). Critically, the GO term definition (GO3) explicitly states: 'Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here.' VanRc is a DNA-binding response regulator (transcription factor), which the GO definition excludes from this term. The annotation exists but is automated and conflicts with the term's own usage guidelines. The primary annotation (cytoplasm) is not among the choices, making the 'correct' answer ambiguous relative to the underlying biology.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5), [GO3](#evidence-go3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a bacterial response regulator (receiver domain + HTH DNA-binding domain, confirmed by annotation as VanRc transcription factor). Options A ('host cell cytoplasm', GO:0030430) and C ('host cell', GO:0043657) refer to proteins located within a HOST organism's cell — inappropriate for a protein functioning within its own bacterial cell. Option D ('cell leading edge', GO:0031252) describes the front of a motile eukaryotic cell, irrelevant to a Gram-positive bacterium. By elimination, B ('protein-DNA complex') is the only option compatible with a DNA-binding bacterial transcription factor. A model can reason: bacterial protein → not in a 'host cell'; not a motile eukaryote → not 'leading edge'; DNA-binding factor → 'protein-DNA complex' is the only remaining plausible compartment.


**Missing item-specific fact**

> None strictly required for elimination, but a strong positive argument for 'protein-DNA complex' as the PRIMARY location (vs. cytoplasm) is absent from the sequence; the annotation is automated (IEA) and the GO definition itself discourages this classification for transcription factors.


**Reason**

> The elimination logic from general biology (bacterial protein, transcription factor, not in a host, not a motile eukaryote) meaningfully narrows to B without needing to recall the specific UniProt annotation. However, the positive justification is weak because the true primary location is cytoplasm, and the protein-DNA complex annotation is automated and arguably misapplied per the GO definition.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B"
]
```

> While B is the only non-absurd option by elimination, the question asks for the 'primary' cellular component. A bacterial transcription factor's primary location is the cytoplasm (as stated in UniProt), and it only transiently forms protein-DNA complexes. The GO definition of GO:0032993 explicitly excludes transcription factor complexes. If 'cytoplasm' were an option, it would be the stronger answer. Among the given choices, B is the least wrong, but the framing as 'primary' location is misleading for a complex-level GO term applied to a transiently DNA-bound protein.


### Important caveats

- The GO:0032993 annotation is IEA:TreeGrafter (automated), not experimental or curated.
- The GO term definition explicitly states transcription factor complexes should NOT be classified under protein-DNA complex, creating a contradiction with the applied annotation.
- The UniProt primary subcellular location is 'Cytoplasm' (ECO:0000250, inferred from similar protein Q06239), which is not offered as an option.
- The identity of the protein (VanRc, response regulator) was inferred by the reviewer from accession metadata not available to the evaluated model; the model must rely on sequence features alone.
- Options A and C use 'host cell' terminology appropriate for pathogen proteins in eukaryotic hosts, not for a bacterium's own proteins — making them clearly wrong distractors.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a bacterial response regulator (receiver domain + HTH DNA-binding domain, confirmed by annotation as VanRc transcription factor). Options A ('host cell cytoplasm', GO:0030430) and C ('host cell', GO:0043657) refer to proteins located within a HOST organism's cell — inappropriate for a protein functioning within its own bacterial cell. Option D ('cell leading edge', GO:0031252) describes the front of a motile eukaryotic cell, irrelevant to a Gram-positive bacterium. By elimination, B ('protein-DNA complex') is the only option compatible with a DNA-binding bacterial transcription factor. A model can reason: bacterial protein → not in a 'host cell'; not a motile eukaryote → not 'leading edge'; DNA-binding factor → 'protein-DNA complex' is the only remaining plausible compartment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination, but a strong positive argument for 'protein-DNA complex' as the PRIMARY location (vs. cytoplasm) is absent from the sequence; the annotation is automated (IEA) and the GO definition itself discourages this classification for transcription factors.",
    "reason": "The elimination logic from general biology (bacterial protein, transcription factor, not in a host, not a motile eukaryote) meaningfully narrows to B without needing to recall the specific UniProt annotation. However, the positive justification is weak because the true primary location is cytoplasm, and the protein-DNA complex annotation is automated and arguably misapplied per the GO definition."
  },
  "case_id": "GO_cellular_component_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H3",
      "H5",
      "GO3",
      "C4"
    ],
    "judgment": "cannot_determine",
    "reason": "GO:0032993 (protein-DNA complex) IS annotated to Q9KJT4 (evidence C8, H5), but only via IEA:TreeGrafter (automated). The UniProt primary subcellular location comment states 'Cytoplasm' (C5, H3, ECO:0000250). Critically, the GO term definition (GO3) explicitly states: 'Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here.' VanRc is a DNA-binding response regulator (transcription factor), which the GO definition excludes from this term. The annotation exists but is automated and conflicts with the term's own usage guidelines. The primary annotation (cytoplasm) is not among the choices, making the 'correct' answer ambiguous relative to the underlying biology."
  },
  "important_caveats": [
    "The GO:0032993 annotation is IEA:TreeGrafter (automated), not experimental or curated.",
    "The GO term definition explicitly states transcription factor complexes should NOT be classified under protein-DNA complex, creating a contradiction with the applied annotation.",
    "The UniProt primary subcellular location is 'Cytoplasm' (ECO:0000250, inferred from similar protein Q06239), which is not offered as an option.",
    "The identity of the protein (VanRc, response regulator) was inferred by the reviewer from accession metadata not available to the evaluated model; the model must rely on sequence features alone.",
    "Options A and C use 'host cell' terminology appropriate for pathogen proteins in eukaryotic hosts, not for a bacterium's own proteins — making them clearly wrong distractors."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B"
    ],
    "reason": "While B is the only non-absurd option by elimination, the question asks for the 'primary' cellular component. A bacterial transcription factor's primary location is the cytoplasm (as stated in UniProt), and it only transiently forms protein-DNA complexes. The GO definition of GO:0032993 explicitly excludes transcription factor complexes. If 'cytoplasm' were an option, it would be the stronger answer. Among the given choices, B is the least wrong, but the framing as 'primary' location is misleading for a complex-level GO term applied to a transiently DNA-bound protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0077",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "GO:0032993 (protein-DNA complex) IS annotated to Q9KJT4 (evidence C8, H5), but only via IEA:TreeGrafter (automated). The UniProt primary subcellular location comment states 'Cytoplasm' (C5, H3, ECO:0000250). Critically, the GO term definition (GO3) explicitly states: 'Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here.' VanRc is a DNA-binding response regulator (transcription factor), which the GO definition excludes from this term. The annotation exists but is automated and conflicts with the term's own usage guidelines. The primary annotation (cytoplasm) is not among the choices, making the 'correct' answer ambiguous relative to the underlying biology.",
    "evidence_ids": ["C5", "C8", "H3", "H5", "GO3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a bacterial response regulator (receiver domain + HTH DNA-binding domain, confirmed by annotation as VanRc transcription factor). Options A ('host cell cytoplasm', GO:0030430) and C ('host cell', GO:0043657) refer to proteins located within a HOST organism's cell — inappropriate for a protein functioning within its own bacterial cell. Option D ('cell leading edge', GO:0031252) describes the front of a motile eukaryotic cell, irrelevant to a Gram-positive bacterium. By elimination, B ('protein-DNA complex') is the only option compatible with a DNA-binding bacterial transcription factor. A model can reason: bacterial protein → not in a 'host cell'; not a motile eukaryote → not 'leading edge'; DNA-binding factor → 'protein-DNA complex' is the only remaining plausible compartment.",
    "missing_item_specific_fact": "None strictly required for elimination, but a strong positive argument for 'protein-DNA complex' as the PRIMARY location (vs. cytoplasm) is absent from the sequence; the annotation is automated (IEA) and the GO definition itself discourages this classification for transcription factors.",
    "reason": "The elimination logic from general biology (bacterial protein, transcription factor, not in a host, not a motile eukaryote) meaningfully narrows to B without needing to recall the specific UniProt annotation. However, the positive justification is weak because the true primary location is cytoplasm, and the protein-DNA complex annotation is automated and arguably misapplied per the GO definition."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B"],
    "reason": "While B is the only non-absurd option by elimination, the question asks for the 'primary' cellular component. A bacterial transcription factor's primary location is the cytoplasm (as stated in UniProt), and it only transiently forms protein-DNA complexes. The GO definition of GO:0032993 explicitly excludes transcription factor complexes. If 'cytoplasm' were an option, it would be the stronger answer. Among the given choices, B is the least wrong, but the framing as 'primary' location is misleading for a complex-level GO term applied to a transiently DNA-bound protein."
  },
  "important_caveats": [
    "The GO:0032993 annotation is IEA:TreeGrafter (automated), not experimental or curated.",
    "The GO term definition explicitly states transcription factor complexes should NOT be classified under protein-DNA complex, creating a contradiction with the applied annotation.",
    "The UniProt primary subcellular location is 'Cytoplasm' (ECO:0000250, inferred from similar protein Q06239), which is not offered as an option.",
    "The identity of the protein (VanRc, response regulator) was inferred by the reviewer from accession metadata not available to the evaluated model; the model must rely on sequence features alone.",
    "Options A and C use 'host cell' terminology appropriate for pathogen proteins in eukaryotic hosts, not for a bacterium's own proteins — making them clearly wrong distractors."
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

**Accession:** `Q9KJT4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 146. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:58.674575+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAY67971.1","source":"EMBL"}],"value":"Response regulator"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAF86641.1","source":"EMBL"}],"value":"Response regulator VanRc"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"MXS24890.1","source":"EMBL"}],"value":"VanC-type vancomycin resistance DNA-binding response regulator VanRc"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10817725","source":"PubMed"}],"value":"Regulatory protein VanRc"}}}
```

Source SHA-256: `e1e5f5c5b28e1d55b8bb917fe74a3df4a30a960e3a92ec54b207ef13ad606564`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:58.674575+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q06239","source":"UniProtKB"}],"id":"SL-0086","value":"Cytoplasm"}}]}
```

Source SHA-256: `e1e5f5c5b28e1d55b8bb917fe74a3df4a30a960e3a92ec54b207ef13ad606564`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT4.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:58.674575+00:00.  

```json
{"database":"GO","id":"GO:0005737","properties":[{"key":"GoTerm","value":"C:cytoplasm"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `e1e5f5c5b28e1d55b8bb917fe74a3df4a30a960e3a92ec54b207ef13ad606564`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT4.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:58.674575+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `e1e5f5c5b28e1d55b8bb917fe74a3df4a30a960e3a92ec54b207ef13ad606564`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT4.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:58.674575+00:00.  

```json
{"database":"GO","id":"GO:0032993","properties":[{"key":"GoTerm","value":"C:protein-DNA complex"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `e1e5f5c5b28e1d55b8bb917fe74a3df4a30a960e3a92ec54b207ef13ad606564`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT4?format=txt&versions=146)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 146 / 1.  
**Retrieved:** 2026-11-02T04:33:03.044169+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250|UniProtKB:Q06239}.
```

Source SHA-256: `8018664985e7a94c9aa5bb4def546a23321f86a8c94ed18429a60c9fa498d9c2`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT4?format=txt&versions=146)  
**Locator:** `lines 100-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 146 / 1.  
**Retrieved:** 2026-11-02T04:33:03.044169+00:00.  

```text
DR   GO; GO:0032993; C:protein-DNA complex; IEA:TreeGrafter.
```

Source SHA-256: `8018664985e7a94c9aa5bb4def546a23321f86a8c94ed18429a60c9fa498d9c2`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 192695-192704`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0032993
name: protein-DNA complex
namespace: cellular_component
def: "A macromolecular complex containing both protein and DNA molecules." [GOC:mah]
comment: Note that this term is intended to classify complexes that have DNA as one of the members of the complex, that is, the complex does not exist if DNA is not present. Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here.
subset: goslim_pir
synonym: "DNA-protein complex" EXACT [GOC:mah]
is_a: GO:0032991 ! protein-containing complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 77. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
