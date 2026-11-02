# GO_cellular_component_0023

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — mitochondrion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNGNQIKQLKKLYRHILNEASKFENINYNVYFSNKAKEKFREFCSDTNFESEKLKTFQNECWDYLNMLKRQTIIHNLYHVDKPLVNK

[Multiple Choices]
A. mitochondrial [2Fe-2S] assembly complex
B. cytoplasm
C. virion component
D. mitochondrion
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

> The sequence-matched UniProt record identifies the protein as P. falciparum Isd11 and reports mitochondrial localization with experimental evidence (ECO:0000269); it also records a mitochondrion GO annotation with IDA evidence. This supports D, though the evidence is reviewer-only and does not establish what the original model could infer from sequence alone.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence does not provide a sufficiently unambiguous targeting signal to establish mitochondrial localization or distinguish the organelle from a specific mitochondrial complex. Its short length and composition alone do not resolve the choices.


**Missing item-specific fact**

> The protein-specific localization and complex membership of Isd11, established through annotation or experimental work, are not supplied in the question.


**Reason**

> Choosing the supported mitochondrial location depends on item-specific knowledge absent from the input. Recognizing the sequence or invoking an unspecified predictor would not constitute reasoning from the provided evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> D is supported as the organelle location. A is also potentially defensible because Isd11 is associated with mitochondrial iron-sulfur assembly machinery, and the reviewer-only record annotates it to a cysteine-desulfurase complex that is related in the supplied ontology to the mitochondrial &#91;2Fe-2S&#93; assembly complex. The question does not clarify whether it seeks a broad location or a specific complex.


### Important caveats

- The experimental localization evidence supports D; the exact author source snapshot is unknown.
- Reviewer-only annotations and source identity were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence does not provide a sufficiently unambiguous targeting signal to establish mitochondrial localization or distinguish the organelle from a specific mitochondrial complex. Its short length and composition alone do not resolve the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization and complex membership of Isd11, established through annotation or experimental work, are not supplied in the question.",
    "reason": "Choosing the supported mitochondrial location depends on item-specific knowledge absent from the input. Recognizing the sequence or invoking an unspecified predictor would not constitute reasoning from the provided evidence."
  },
  "case_id": "GO_cellular_component_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as P. falciparum Isd11 and reports mitochondrial localization with experimental evidence (ECO:0000269); it also records a mitochondrion GO annotation with IDA evidence. This supports D, though the evidence is reviewer-only and does not establish what the original model could infer from sequence alone."
  },
  "important_caveats": [
    "The experimental localization evidence supports D; the exact author source snapshot is unknown.",
    "Reviewer-only annotations and source identity were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "D is supported as the organelle location. A is also potentially defensible because Isd11 is associated with mitochondrial iron-sulfur assembly machinery, and the reviewer-only record annotates it to a cysteine-desulfurase complex that is related in the supplied ontology to the mitochondrial [2Fe-2S] assembly complex. The question does not clarify whether it seeks a broad location or a specific complex."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as P. falciparum Isd11 and reports mitochondrial localization with experimental evidence (ECO:0000269); it also records a mitochondrion GO annotation with IDA evidence. This supports D, though the evidence is reviewer-only and does not establish what the original model could infer from sequence alone.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence does not provide a sufficiently unambiguous targeting signal to establish mitochondrial localization or distinguish the organelle from a specific mitochondrial complex. Its short length and composition alone do not resolve the choices.",
    "missing_item_specific_fact": "The protein-specific localization and complex membership of Isd11, established through annotation or experimental work, are not supplied in the question.",
    "reason": "Choosing the supported mitochondrial location depends on item-specific knowledge absent from the input. Recognizing the sequence or invoking an unspecified predictor would not constitute reasoning from the provided evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "D is supported as the organelle location. A is also potentially defensible because Isd11 is associated with mitochondrial iron-sulfur assembly machinery, and the reviewer-only record annotates it to a cysteine-desulfurase complex that is related in the supplied ontology to the mitochondrial [2Fe-2S] assembly complex. The question does not clarify whether it seeks a broad location or a specific complex."
  },
  "important_caveats": [
    "The experimental localization evidence supports D; the exact author source snapshot is unknown.",
    "Reviewer-only annotations and source identity were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IEK7 (Isd11/PfIsd11 from Plasmodium falciparum) carries the experimental subcellular location annotation 'Mitochondrion' with evidence code ECO:0000269 (direct assay) from PubMed:24086138 (Gisselberg et al. 2013, PLoS Pathog). The GO annotation GO:0005739 (mitochondrion) is tagged IDA:GeneDB, indicating direct experimental evidence. The sequence matches the benchmark input exactly (87 aa, SHA256 confirmed). Option A (mitochondrial &#91;2Fe-2S&#93; assembly complex, GO:0099128) is defined for the human complex (ISCU, NFS1, LYRM4, NDUFAB1, FXN) and is not directly annotated to this protein; the related annotation GO:1990221 (L-cysteine desulfurase complex) is via IBA:GO_Central (inference), not direct evidence. Thus D (mitochondrion) is the best-supported primary cellular component.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2), [GO5](#evidence-go5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A general biologist might note that Fe-S cluster assembly occurs in mitochondria in eukaryotes and that Plasmodium retains a mitochondrion, but the 87-aa sequence lacks a canonical N-terminal mitochondrial targeting sequence (no amphipathic helix rich in Arg/Ser/Thr devoid of acidic residues; the N-terminus MNGNQIKQLKKLYRHILNEASK contains both basic and acidic residues). No cysteine-rich iron-binding motif or ISCU/Isd11-specific domain is discernible from the raw sequence. The distinction between option A (mitochondrial &#91;2Fe-2S&#93; assembly complex) and option D (mitochondrion) cannot be made from sequence features alone; it requires knowing that this protein is Isd11, a component of the ISC scaffold complex, and that its experimentally determined primary location is the mitochondrion rather than being specifically annotated to GO:0099128.


**Missing item-specific fact**

> The experimental subcellular localization of PfIsd11 by fluorescence microscopy/fractionation (Gisselberg et al. 2013, PubMed:24086138) and its identification as a component of the Plasmodium ISC scaffold complex (Sadik et al. 2021, PubMed:34032321) are required to confidently assign mitochondrion over cytoplasm and to distinguish the general organelle (D) from the specific complex (A). The 87-aa sequence provides no strong targeting signal for confident de novo prediction.


**Reason**

> The sequence is too short (87 aa) and lacks recognizable targeting motifs (no clear MTS, no signal peptide, no transmembrane helix, no NLS) to support reliable compartment prediction by general reasoning. Eliminating C (virion component) is trivial for a eukaryotic protein, but distinguishing A from D from B requires protein-specific knowledge of Isd11 identity and its experimental localization data.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (mitochondrial &#91;2Fe-2S&#93; assembly complex) and D (mitochondrion) point to the mitochondrial compartment. A knowledgeable model aware of Fe-S cluster biology might consider A plausible since Isd11 participates in ISC scaffold assembly. However, GO:0099128 is defined for the human complex and Isd11 is not annotated to it; the direct experimental annotation is to GO:0005739 (mitochondrion). The 'primary cellular component' framing favors D, but the overlap makes A a tempting near-miss distractor that tests specific annotation knowledge rather than reasoning.


### Important caveats

- The UniProt entry was first released 2025-04-09 (entry version 87); the benchmark's author source snapshot is unknown, though the historical version 85 (released 2026-01-28) also carries the same mitochondrial annotation.
- The identity origin (accession Q8IEK7) was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model sees only the 87-aa sequence.
- GO:0099128 (option A) is defined for the human complex (ISCU, NFS1, LYRM4, NDUFAB1, FXN); Plasmodium Isd11 participates in the ISC scaffold complex but is not annotated to this exact term.
- The annotation to GO:1990221 (L-cysteine desulfurase complex) is via IBA:GO_Central (inference by biological ancestor), not direct experimental evidence, weakening any argument for option A.
- Plasmodium falciparum also possesses an apicoplast; the cited 2013 paper links the suf pathway to apicoplast maintenance, but the experimental localization of Isd11 specifically is mitochondrial.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A general biologist might note that Fe-S cluster assembly occurs in mitochondria in eukaryotes and that Plasmodium retains a mitochondrion, but the 87-aa sequence lacks a canonical N-terminal mitochondrial targeting sequence (no amphipathic helix rich in Arg/Ser/Thr devoid of acidic residues; the N-terminus MNGNQIKQLKKLYRHILNEASK contains both basic and acidic residues). No cysteine-rich iron-binding motif or ISCU/Isd11-specific domain is discernible from the raw sequence. The distinction between option A (mitochondrial [2Fe-2S] assembly complex) and option D (mitochondrion) cannot be made from sequence features alone; it requires knowing that this protein is Isd11, a component of the ISC scaffold complex, and that its experimentally determined primary location is the mitochondrion rather than being specifically annotated to GO:0099128.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental subcellular localization of PfIsd11 by fluorescence microscopy/fractionation (Gisselberg et al. 2013, PubMed:24086138) and its identification as a component of the Plasmodium ISC scaffold complex (Sadik et al. 2021, PubMed:34032321) are required to confidently assign mitochondrion over cytoplasm and to distinguish the general organelle (D) from the specific complex (A). The 87-aa sequence provides no strong targeting signal for confident de novo prediction.",
    "reason": "The sequence is too short (87 aa) and lacks recognizable targeting motifs (no clear MTS, no signal peptide, no transmembrane helix, no NLS) to support reliable compartment prediction by general reasoning. Eliminating C (virion component) is trivial for a eukaryotic protein, but distinguishing A from D from B requires protein-specific knowledge of Isd11 identity and its experimental localization data."
  },
  "case_id": "GO_cellular_component_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "H4",
      "H6",
      "GO2",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IEK7 (Isd11/PfIsd11 from Plasmodium falciparum) carries the experimental subcellular location annotation 'Mitochondrion' with evidence code ECO:0000269 (direct assay) from PubMed:24086138 (Gisselberg et al. 2013, PLoS Pathog). The GO annotation GO:0005739 (mitochondrion) is tagged IDA:GeneDB, indicating direct experimental evidence. The sequence matches the benchmark input exactly (87 aa, SHA256 confirmed). Option A (mitochondrial [2Fe-2S] assembly complex, GO:0099128) is defined for the human complex (ISCU, NFS1, LYRM4, NDUFAB1, FXN) and is not directly annotated to this protein; the related annotation GO:1990221 (L-cysteine desulfurase complex) is via IBA:GO_Central (inference), not direct evidence. Thus D (mitochondrion) is the best-supported primary cellular component."
  },
  "important_caveats": [
    "The UniProt entry was first released 2025-04-09 (entry version 87); the benchmark's author source snapshot is unknown, though the historical version 85 (released 2026-01-28) also carries the same mitochondrial annotation.",
    "The identity origin (accession Q8IEK7) was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model sees only the 87-aa sequence.",
    "GO:0099128 (option A) is defined for the human complex (ISCU, NFS1, LYRM4, NDUFAB1, FXN); Plasmodium Isd11 participates in the ISC scaffold complex but is not annotated to this exact term.",
    "The annotation to GO:1990221 (L-cysteine desulfurase complex) is via IBA:GO_Central (inference by biological ancestor), not direct experimental evidence, weakening any argument for option A.",
    "Plasmodium falciparum also possesses an apicoplast; the cited 2013 paper links the suf pathway to apicoplast maintenance, but the experimental localization of Isd11 specifically is mitochondrial."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (mitochondrial [2Fe-2S] assembly complex) and D (mitochondrion) point to the mitochondrial compartment. A knowledgeable model aware of Fe-S cluster biology might consider A plausible since Isd11 participates in ISC scaffold assembly. However, GO:0099128 is defined for the human complex and Isd11 is not annotated to it; the direct experimental annotation is to GO:0005739 (mitochondrion). The 'primary cellular component' framing favors D, but the overlap makes A a tempting near-miss distractor that tests specific annotation knowledge rather than reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IEK7 (Isd11/PfIsd11 from Plasmodium falciparum) carries the experimental subcellular location annotation 'Mitochondrion' with evidence code ECO:0000269 (direct assay) from PubMed:24086138 (Gisselberg et al. 2013, PLoS Pathog). The GO annotation GO:0005739 (mitochondrion) is tagged IDA:GeneDB, indicating direct experimental evidence. The sequence matches the benchmark input exactly (87 aa, SHA256 confirmed). Option A (mitochondrial [2Fe-2S] assembly complex, GO:0099128) is defined for the human complex (ISCU, NFS1, LYRM4, NDUFAB1, FXN) and is not directly annotated to this protein; the related annotation GO:1990221 (L-cysteine desulfurase complex) is via IBA:GO_Central (inference), not direct evidence. Thus D (mitochondrion) is the best-supported primary cellular component.",
    "evidence_ids": ["C5", "C7", "C8", "H4", "H6", "GO2", "GO5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A general biologist might note that Fe-S cluster assembly occurs in mitochondria in eukaryotes and that Plasmodium retains a mitochondrion, but the 87-aa sequence lacks a canonical N-terminal mitochondrial targeting sequence (no amphipathic helix rich in Arg/Ser/Thr devoid of acidic residues; the N-terminus MNGNQIKQLKKLYRHILNEASK contains both basic and acidic residues). No cysteine-rich iron-binding motif or ISCU/Isd11-specific domain is discernible from the raw sequence. The distinction between option A (mitochondrial [2Fe-2S] assembly complex) and option D (mitochondrion) cannot be made from sequence features alone; it requires knowing that this protein is Isd11, a component of the ISC scaffold complex, and that its experimentally determined primary location is the mitochondrion rather than being specifically annotated to GO:0099128.",
    "missing_item_specific_fact": "The experimental subcellular localization of PfIsd11 by fluorescence microscopy/fractionation (Gisselberg et al. 2013, PubMed:24086138) and its identification as a component of the Plasmodium ISC scaffold complex (Sadik et al. 2021, PubMed:34032321) are required to confidently assign mitochondrion over cytoplasm and to distinguish the general organelle (D) from the specific complex (A). The 87-aa sequence provides no strong targeting signal for confident de novo prediction.",
    "reason": "The sequence is too short (87 aa) and lacks recognizable targeting motifs (no clear MTS, no signal peptide, no transmembrane helix, no NLS) to support reliable compartment prediction by general reasoning. Eliminating C (virion component) is trivial for a eukaryotic protein, but distinguishing A from D from B requires protein-specific knowledge of Isd11 identity and its experimental localization data."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (mitochondrial [2Fe-2S] assembly complex) and D (mitochondrion) point to the mitochondrial compartment. A knowledgeable model aware of Fe-S cluster biology might consider A plausible since Isd11 participates in ISC scaffold assembly. However, GO:0099128 is defined for the human complex and Isd11 is not annotated to it; the direct experimental annotation is to GO:0005739 (mitochondrion). The 'primary cellular component' framing favors D, but the overlap makes A a tempting near-miss distractor that tests specific annotation knowledge rather than reasoning."
  },
  "important_caveats": [
    "The UniProt entry was first released 2025-04-09 (entry version 87); the benchmark's author source snapshot is unknown, though the historical version 85 (released 2026-01-28) also carries the same mitochondrial annotation.",
    "The identity origin (accession Q8IEK7) was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model sees only the 87-aa sequence.",
    "GO:0099128 (option A) is defined for the human complex (ISCU, NFS1, LYRM4, NDUFAB1, FXN); Plasmodium Isd11 participates in the ISC scaffold complex but is not annotated to this exact term.",
    "The annotation to GO:1990221 (L-cysteine desulfurase complex) is via IBA:GO_Central (inference by biological ancestor), not direct experimental evidence, weakening any argument for option A.",
    "Plasmodium falciparum also possesses an apicoplast; the cited 2013 paper links the suf pathway to apicoplast maintenance, but the experimental localization of Isd11 specifically is mitochondrial."
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

**Accession:** `Q8IEK7` (recovered from dataset image-path metadata, not original question text).  
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.795774+00:00.  

```json
"Q8IEK7"
```

Source SHA-256: `dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.795774+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein Isd11"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34032321","source":"PubMed"}],"value":"PfIsd11"}]}}
```

Source SHA-256: `dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.795774+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"24086138","source":"PubMed"}],"id":"SL-0173","value":"Mitochondrion"}}]}
```

Source SHA-256: `dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)  
**Locator:** `/uniProtKBCrossReferences/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.795774+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"24086138","source":"PubMed"}],"id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IEK7.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.795774+00:00.  

```json
{"citation":{"authors":["Gisselberg J.E.","Dellibovi-Ragheb T.A.","Matthews K.A.","Bosch G.","Prigge S.T."],"citationCrossReferences":[{"database":"PubMed","id":"24086138"},{"database":"DOI","id":"10.1371/journal.ppat.1003655"}],"citationType":"journal article","firstPage":"e1003655","id":"24086138","journal":"PLoS Pathog.","lastPage":"e1003655","publicationDate":"2013","title":"The suf iron-sulfur cluster synthesis pathway is required for apicoplast maintenance in malaria parasites.","volume":"9"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["SUBCELLULAR LOCATION"]}
```

Source SHA-256: `dfa2d75ca3fdb086280360b23ddf1875ba7918f7721401a7b327d705fda13007`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)  
**Locator:** `lines 73-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-01T06:28:39.775629+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:24086138}.
```

Source SHA-256: `18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IEK7?format=txt&versions=85)  
**Locator:** `lines 100-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-01T06:28:39.775629+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IDA:GeneDB.
```

Source SHA-256: `18fdec44d773d33a5e2664d2cf997d80ce20de391821c4bd520cd8ae8e074c4d`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58975-58998`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005739
name: mitochondrion
namespace: cellular_component
def: "A semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration." [GOC:giardia, ISBN:0198506732]
comment: Some anaerobic or microaerophilic organisms (e.g. Entamoeba histolytica, Giardia intestinalis and several Microsporidia species) do not have mitochondria, and contain mitochondrion-related organelles (MROs) instead, called mitosomes or hydrogenosomes, very likely derived from mitochondria. To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "mitochondria" EXACT []
xref: NIF_Subcellular:sao1860313010
xref: Wikipedia:Mitochondrion
is_a: GO:0043231 ! intracellular membrane-bounded organelle
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 413997-414007`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0099128
name: mitochondrial [2Fe-2S] assembly complex
namespace: cellular_component
def: "A protein complex capable of forming 2Fe-2S clusters in mitochondria. In humans it consists of ISCU, NFS1, LYRM4, NDUFAB1 and FXN." [PMID:31101807, PMID:34660592]
synonym: "mitochondrial iron-sulfur cluster assembly complex" RELATED []
synonym: "mitochondrial ISCU complex" EXACT []
is_a: GO:0098798 ! mitochondrial protein-containing complex
is_a: GO:1990221 ! L-cysteine desulfurase complex
is_a: GO:1990229 ! iron-sulfur cluster assembly complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
