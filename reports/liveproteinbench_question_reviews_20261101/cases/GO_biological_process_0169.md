# GO_biological_process_0169

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — alkaloid metabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAEKQQAVTEFYNNTSPRGAWEFLLGDHLHEGFYDPGTTATISGSQAAAARMIDEALRFANIYDDPSKKPKNMLDIGCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK

[Multiple Choices]
A. alkaloid metabolic process
B. DNA damage checkpoint signaling
C. regulation of response to food
D. ribosomal small subunit assembly
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the historical and current UniProt sequence for a norajmaline N-methyltransferase. UniProt reports experimentally supported methylation of norajmaline to ajmaline and identifies the pathway as alkaloid biosynthesis; its GO annotation includes alkaloid metabolic process. This supports choice A, while distinguishing the experimental functional evidence from the GO annotation's IEA evidence code.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a methyltransferase, which makes a metabolic role plausible, but methyltransferases act on many substrates and participate in diverse processes. The sequence alone does not establish alkaloid substrate specificity or distinguish alkaloid metabolism from the other listed processes.


**Missing item-specific fact**

> The protein's specific activity—N-methylation of norajmaline in ajmaline biosynthesis—or an equivalent protein-specific functional annotation is not supplied in the question.


**Reason**

> Identifying the correct process requires protein-specific functional knowledge not encoded unambiguously by the sequence features or the choices. Recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence functional evidence supports alkaloid metabolism; no evidence supplied supports another listed choice.


### Important caveats

- The reviewer-only UniProt and literature-linked evidence was not available to the evaluated model.
- The GO annotation itself is marked IEA:UniProtKB-KW, whereas the cited functional description carries ECO:0000269 experimental evidence.
- The exact author data-source snapshot is unknown, although the historical and current records both match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a methyltransferase, which makes a metabolic role plausible, but methyltransferases act on many substrates and participate in diverse processes. The sequence alone does not establish alkaloid substrate specificity or distinguish alkaloid metabolism from the other listed processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific activity—N-methylation of norajmaline in ajmaline biosynthesis—or an equivalent protein-specific functional annotation is not supplied in the question.",
    "reason": "Identifying the correct process requires protein-specific functional knowledge not encoded unambiguously by the sequence features or the choices. Recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from the provided input."
  },
  "case_id": "GO_biological_process_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence for a norajmaline N-methyltransferase. UniProt reports experimentally supported methylation of norajmaline to ajmaline and identifies the pathway as alkaloid biosynthesis; its GO annotation includes alkaloid metabolic process. This supports choice A, while distinguishing the experimental functional evidence from the GO annotation's IEA evidence code."
  },
  "important_caveats": [
    "The reviewer-only UniProt and literature-linked evidence was not available to the evaluated model.",
    "The GO annotation itself is marked IEA:UniProtKB-KW, whereas the cited functional description carries ECO:0000269 experimental evidence.",
    "The exact author data-source snapshot is unknown, although the historical and current records both match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence functional evidence supports alkaloid metabolism; no evidence supplied supports another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence for a norajmaline N-methyltransferase. UniProt reports experimentally supported methylation of norajmaline to ajmaline and identifies the pathway as alkaloid biosynthesis; its GO annotation includes alkaloid metabolic process. This supports choice A, while distinguishing the experimental functional evidence from the GO annotation's IEA evidence code.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a methyltransferase, which makes a metabolic role plausible, but methyltransferases act on many substrates and participate in diverse processes. The sequence alone does not establish alkaloid substrate specificity or distinguish alkaloid metabolism from the other listed processes.",
    "missing_item_specific_fact": "The protein's specific activity—N-methylation of norajmaline in ajmaline biosynthesis—or an equivalent protein-specific functional annotation is not supplied in the question.",
    "reason": "Identifying the correct process requires protein-specific functional knowledge not encoded unambiguously by the sequence features or the choices. Recognizing the sequence or retrieving its database annotation would be lookup, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence functional evidence supports alkaloid metabolism; no evidence supplied supports another listed choice."
  },
  "important_caveats": [
    "The reviewer-only UniProt and literature-linked evidence was not available to the evaluated model.",
    "The GO annotation itself is marked IEA:UniProtKB-KW, whereas the cited functional description carries ECO:0000269 experimental evidence.",
    "The exact author data-source snapshot is unknown, although the historical and current records both match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A075D6M1, NNMT_RAUSE) is experimentally characterized (ECO:0000269, PubMed:27122470 and PubMed:38212296) as Norajmaline N-methyltransferase catalyzing indole N-methylation of norajmaline to ajmaline, a monoterpenoid indole alkaloid. The pathway is explicitly annotated as 'Alkaloid biosynthesis; ajmaline biosynthesis' and GO:0009820 (alkaloid metabolic process) is assigned. The GO term definition matches: 'chemical reactions and pathways involving alkaloids, nitrogen containing natural products.' The other three options (DNA damage checkpoint signaling, regulation of response to food, ribosomal small subunit assembly) have no supporting evidence for this plant methyltransferase.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable SAM-dependent methyltransferase motif (DIGCGVGGT, a glycine-rich Rossmann-fold loop), which could allow a knowledgeable reader to identify this as a methyltransferase. By elimination, DNA damage checkpoint signaling (kinases/scaffolds), regulation of response to food (animal neuronal/nutrient-sensing), and ribosomal small subunit assembly (assembly factors/P-loop proteins) are implausible for a small plant methyltransferase. However, this elimination only narrows to 'some metabolic methylation process'—it does not specifically identify 'alkaloid' metabolism over other possible methylation pathways (e.g., flavonoid, terpenoid, or tocopherol methylation).


**Missing item-specific fact**

> The specific substrate identity (norajmaline, an alkaloid) and the pathway assignment (ajmaline biosynthesis) are required to uniquely select 'alkaloid metabolic process' over other methylation-involving metabolic processes not listed as distractors. The sequence motif identifies the enzyme class (methyltransferase) but not the substrate class (alkaloid).


**Reason**

> While the methyltransferase motif provides a partial reasoning anchor and the distractors can be eliminated by general knowledge about what processes involve which protein classes, the specific identification as an 'alkaloid' methyltransferase (rather than, e.g., a tocopherol or phenylpropanoid methyltransferase) requires knowledge of the substrate or pathway that is not encoded in the sequence. The protein's alternative name 'Gamma-tocopherol-like methyltransferase' further illustrates that sequence similarity alone does not specify the alkaloid connection.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the four options, only A (alkaloid metabolic process) is consistent with a plant N-methyltransferase involved in secondary metabolism. Options B, C, and D are clearly implausible for this protein type, so no genuine ambiguity exists among the choices despite the reasoning gap in pinpointing 'alkaloid' specifically.


### Important caveats

- The GO:0009820 annotation carries evidence code IEA (Inferred from Electronic Annotation via UniProt keyword), though the underlying function is experimentally verified (ECO:0000269).
- The protein's alternative name 'Gamma-tocopherol-like methyltransferase' reflects evolutionary origin from a tocopherol methyltransferase gene family, which could confuse sequence-based reasoning.
- The reviewer-only evidence was not available to the evaluated model; the model must work from the 292-aa sequence alone.
- The sequence match is confirmed (SHA256 identical between benchmark and UniProt), so the annotation applies to the exact sequence presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable SAM-dependent methyltransferase motif (DIGCGVGGT, a glycine-rich Rossmann-fold loop), which could allow a knowledgeable reader to identify this as a methyltransferase. By elimination, DNA damage checkpoint signaling (kinases/scaffolds), regulation of response to food (animal neuronal/nutrient-sensing), and ribosomal small subunit assembly (assembly factors/P-loop proteins) are implausible for a small plant methyltransferase. However, this elimination only narrows to 'some metabolic methylation process'—it does not specifically identify 'alkaloid' metabolism over other possible methylation pathways (e.g., flavonoid, terpenoid, or tocopherol methylation).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (norajmaline, an alkaloid) and the pathway assignment (ajmaline biosynthesis) are required to uniquely select 'alkaloid metabolic process' over other methylation-involving metabolic processes not listed as distractors. The sequence motif identifies the enzyme class (methyltransferase) but not the substrate class (alkaloid).",
    "reason": "While the methyltransferase motif provides a partial reasoning anchor and the distractors can be eliminated by general knowledge about what processes involve which protein classes, the specific identification as an 'alkaloid' methyltransferase (rather than, e.g., a tocopherol or phenylpropanoid methyltransferase) requires knowledge of the substrate or pathway that is not encoded in the sequence. The protein's alternative name 'Gamma-tocopherol-like methyltransferase' further illustrates that sequence similarity alone does not specify the alkaloid connection."
  },
  "case_id": "GO_biological_process_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H4",
      "H5",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A075D6M1, NNMT_RAUSE) is experimentally characterized (ECO:0000269, PubMed:27122470 and PubMed:38212296) as Norajmaline N-methyltransferase catalyzing indole N-methylation of norajmaline to ajmaline, a monoterpenoid indole alkaloid. The pathway is explicitly annotated as 'Alkaloid biosynthesis; ajmaline biosynthesis' and GO:0009820 (alkaloid metabolic process) is assigned. The GO term definition matches: 'chemical reactions and pathways involving alkaloids, nitrogen containing natural products.' The other three options (DNA damage checkpoint signaling, regulation of response to food, ribosomal small subunit assembly) have no supporting evidence for this plant methyltransferase."
  },
  "important_caveats": [
    "The GO:0009820 annotation carries evidence code IEA (Inferred from Electronic Annotation via UniProt keyword), though the underlying function is experimentally verified (ECO:0000269).",
    "The protein's alternative name 'Gamma-tocopherol-like methyltransferase' reflects evolutionary origin from a tocopherol methyltransferase gene family, which could confuse sequence-based reasoning.",
    "The reviewer-only evidence was not available to the evaluated model; the model must work from the 292-aa sequence alone.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt), so the annotation applies to the exact sequence presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four options, only A (alkaloid metabolic process) is consistent with a plant N-methyltransferase involved in secondary metabolism. Options B, C, and D are clearly implausible for this protein type, so no genuine ambiguity exists among the choices despite the reasoning gap in pinpointing 'alkaloid' specifically."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A075D6M1, NNMT_RAUSE) is experimentally characterized (ECO:0000269, PubMed:27122470 and PubMed:38212296) as Norajmaline N-methyltransferase catalyzing indole N-methylation of norajmaline to ajmaline, a monoterpenoid indole alkaloid. The pathway is explicitly annotated as 'Alkaloid biosynthesis; ajmaline biosynthesis' and GO:0009820 (alkaloid metabolic process) is assigned. The GO term definition matches: 'chemical reactions and pathways involving alkaloids, nitrogen containing natural products.' The other three options (DNA damage checkpoint signaling, regulation of response to food, ribosomal small subunit assembly) have no supporting evidence for this plant methyltransferase.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H4", "H5", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable SAM-dependent methyltransferase motif (DIGCGVGGT, a glycine-rich Rossmann-fold loop), which could allow a knowledgeable reader to identify this as a methyltransferase. By elimination, DNA damage checkpoint signaling (kinases/scaffolds), regulation of response to food (animal neuronal/nutrient-sensing), and ribosomal small subunit assembly (assembly factors/P-loop proteins) are implausible for a small plant methyltransferase. However, this elimination only narrows to 'some metabolic methylation process'—it does not specifically identify 'alkaloid' metabolism over other possible methylation pathways (e.g., flavonoid, terpenoid, or tocopherol methylation).",
    "missing_item_specific_fact": "The specific substrate identity (norajmaline, an alkaloid) and the pathway assignment (ajmaline biosynthesis) are required to uniquely select 'alkaloid metabolic process' over other methylation-involving metabolic processes not listed as distractors. The sequence motif identifies the enzyme class (methyltransferase) but not the substrate class (alkaloid).",
    "reason": "While the methyltransferase motif provides a partial reasoning anchor and the distractors can be eliminated by general knowledge about what processes involve which protein classes, the specific identification as an 'alkaloid' methyltransferase (rather than, e.g., a tocopherol or phenylpropanoid methyltransferase) requires knowledge of the substrate or pathway that is not encoded in the sequence. The protein's alternative name 'Gamma-tocopherol-like methyltransferase' further illustrates that sequence similarity alone does not specify the alkaloid connection."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four options, only A (alkaloid metabolic process) is consistent with a plant N-methyltransferase involved in secondary metabolism. Options B, C, and D are clearly implausible for this protein type, so no genuine ambiguity exists among the choices despite the reasoning gap in pinpointing 'alkaloid' specifically."
  },
  "important_caveats": [
    "The GO:0009820 annotation carries evidence code IEA (Inferred from Electronic Annotation via UniProt keyword), though the underlying function is experimentally verified (ECO:0000269).",
    "The protein's alternative name 'Gamma-tocopherol-like methyltransferase' reflects evolutionary origin from a tocopherol methyltransferase gene family, which could confuse sequence-based reasoning.",
    "The reviewer-only evidence was not available to the evaluated model; the model must work from the 292-aa sequence alone.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt), so the annotation applies to the exact sequence presented."
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

**Accession:** `A0A075D6M1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 36. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
"A0A075D6M1"
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AHH02781.1","source":"EMBL"}],"value":"Gamma-tocopherol-like methyltransferase NNMT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"2.1.1.392"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Norajmaline N-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsNNMT"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"N-methyltransferase involved in the biosynthesis of ajmaline-type monoterpenoid indole alkaloids (MIAs) natural products, important plant-derived pharmaceuticals used in the therapy of heart disorders (PubMed:27122470, PubMed:38212296). Catalyzes the indole N-methylation of norajmaline to produce ajmaline (PubMed:27122470, PubMed:38212296). Also able, with a lower efficiency, to mediate the conversion of 4-methylnorajmaline to 4-methylajmaline (PubMed:27122470)"}]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"citation":{"authors":["Cazares-Flores P.","Levac D.","De Luca V."],"citationCrossReferences":[{"database":"PubMed","id":"27122470"},{"database":"DOI","id":"10.1111/tpj.13186"}],"citationType":"journal article","firstPage":"335","id":"27122470","journal":"Plant J.","lastPage":"342","publicationDate":"2016","title":"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.","volume":"87"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 43-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
CC   -!- FUNCTION: N-methyltransferase involved in the biosynthesis of ajmaline-
CC       type monoterpenoid indole alkaloids (MIAs) natural products, important
CC       plant-derived pharmaceuticals used in the therapy of heart disorders
CC       (PubMed:27122470, PubMed:38212296). Catalyzes the indole N-methylation
CC       of norajmaline to produce ajmaline (PubMed:27122470, PubMed:38212296).
CC       Also able, with a lower efficiency, to mediate the conversion of 4-
CC       methylnorajmaline to 4-methylajmaline (PubMed:27122470).
CC       {ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 83-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 113-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
DR   GO; GO:0009820; P:alkaloid metabolic process; IEA:UniProtKB-KW.
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 99940-99948`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009820
name: alkaloid metabolic process
namespace: biological_process
def: "The chemical reactions and pathways involving alkaloids, nitrogen containing natural products which are not otherwise classified as peptides, nonprotein amino acids, amines, cyanogenic glycosides, glucosinolates, cofactors, phytohormones or primary metabolites (such as purine or pyrimidine bases)." [GOC:lr, ISBN:0122146743]
subset: goslim_chembl
synonym: "alkaloid metabolism" EXACT []
is_a: GO:0008152 ! metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 169. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
