# GO_cellular_component_0059

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGSEPVRAEGETMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSTSASLHFIDRAAMPKDVILYTDDNEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTFMWNNPFTERHLISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGNGDI

[Multiple Choices]
A. NF-kappaB complex
B. protein-containing complex
C. spindle
D. nucleus
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

> The exact sequence matches the soybean HAL3a record, which reports nuclear localization and a nucleus GO annotation with IDA evidence. This supports D, although the record also reports cell-membrane localization and does not establish that the nucleus is the protein’s exclusive or primary location.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence encodes a soluble enzyme without an obvious sequence feature that specifically establishes nuclear localization over the listed alternatives. General sequence-based reasoning does not determine this protein’s reported cellular localization.


**Missing item-specific fact**

> The protein-specific localization evidence identifying HAL3a as occurring in the nucleus is absent from the question.


**Reason**

> Choosing D depends on a particular localization annotation or experimental result, not on a concrete distinction available from the supplied sequence and choices. Recognizing the sequence as a known protein would amount to lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> D is supported as a location, but the matched record also annotates the protein to a phosphopantothenoylcysteine decarboxylase complex, which is a subtype of B. The question gives no rule for selecting a single ‘primary’ GO component among different kinds of cellular-component annotations.


### Important caveats

- The sequence match is exact, and historical as well as current UniProt evidence is supplied, but the author’s exact source snapshot is unknown.
- The nuclear and cell-membrane localizations are reported with IDA evidence; the complex annotation uses IBA evidence.
- The evidence supports nuclear localization but does not by itself show that it is the protein’s uniquely primary location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a soluble enzyme without an obvious sequence feature that specifically establishes nuclear localization over the listed alternatives. General sequence-based reasoning does not determine this protein’s reported cellular localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization evidence identifying HAL3a as occurring in the nucleus is absent from the question.",
    "reason": "Choosing D depends on a particular localization annotation or experimental result, not on a concrete distinction available from the supplied sequence and choices. Recognizing the sequence as a known protein would amount to lookup or memorization."
  },
  "case_id": "GO_cellular_component_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the soybean HAL3a record, which reports nuclear localization and a nucleus GO annotation with IDA evidence. This supports D, although the record also reports cell-membrane localization and does not establish that the nucleus is the protein’s exclusive or primary location."
  },
  "important_caveats": [
    "The sequence match is exact, and historical as well as current UniProt evidence is supplied, but the author’s exact source snapshot is unknown.",
    "The nuclear and cell-membrane localizations are reported with IDA evidence; the complex annotation uses IBA evidence.",
    "The evidence supports nuclear localization but does not by itself show that it is the protein’s uniquely primary location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "D is supported as a location, but the matched record also annotates the protein to a phosphopantothenoylcysteine decarboxylase complex, which is a subtype of B. The question gives no rule for selecting a single ‘primary’ GO component among different kinds of cellular-component annotations."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the soybean HAL3a record, which reports nuclear localization and a nucleus GO annotation with IDA evidence. This supports D, although the record also reports cell-membrane localization and does not establish that the nucleus is the protein’s exclusive or primary location.",
    "evidence_ids": ["C1", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence encodes a soluble enzyme without an obvious sequence feature that specifically establishes nuclear localization over the listed alternatives. General sequence-based reasoning does not determine this protein’s reported cellular localization.",
    "missing_item_specific_fact": "The protein-specific localization evidence identifying HAL3a as occurring in the nucleus is absent from the question.",
    "reason": "Choosing D depends on a particular localization annotation or experimental result, not on a concrete distinction available from the supplied sequence and choices. Recognizing the sequence as a known protein would amount to lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "D is supported as a location, but the matched record also annotates the protein to a phosphopantothenoylcysteine decarboxylase complex, which is a subtype of B. The question gives no rule for selecting a single ‘primary’ GO component among different kinds of cellular-component annotations."
  },
  "important_caveats": [
    "The sequence match is exact, and historical as well as current UniProt evidence is supplied, but the author’s exact source snapshot is unknown.",
    "The nuclear and cell-membrane localizations are reported with IDA evidence; the complex annotation uses IBA evidence.",
    "The evidence supports nuclear localization but does not by itself show that it is the protein’s uniquely primary location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6SZ50 (HAL3A_SOYBN, PPCDC/HAL3a from Glycine max) annotates nucleus (GO:0005634) with IDA (Inferred from Direct Assay) evidence, confirmed by experimental Ref.4. The expected answer 'nucleus' is directly supported. However, the same entry also annotates cell membrane/plasma membrane (GO:0005886, IDA), so the protein is dual-localized. Among the four provided options, nucleus is the only specific compartment with direct experimental annotation; plasma membrane is not offered as a choice. The GO term 'phosphopantothenoylcysteine decarboxylase complex' (GO:0071513, IBA) is_a 'protein-containing complex' (GO:0032991), so option B is technically also supported by annotation, but nucleus is the more specific compartment-level answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Distractors A (NF-kappaB complex) and C (spindle) can be eliminated by general knowledge: NF-kappaB is an animal-specific immune signaling complex irrelevant to a plant enzyme, and spindle is a mitotic microtubule structure with no connection to a CoA-biosynthesis enzyme. Option B (protein-containing complex) is technically valid (PPCDC forms a homotrimer) but is an extremely broad GO category. The remaining choice is D (nucleus). However, the 211-aa sequence lacks a recognizable classical NLS (e.g., PKKKRKV-type motif), has no transmembrane helix, and no mitochondrial targeting peptide. Without knowing that HAL3/PPCDC orthologs (particularly the well-studied yeast HAL3 transcription factor) are nuclear, a model cannot confidently assign nucleus over cytoplasm or membrane from sequence features alone. The UniProt entry itself lists both nucleus AND cell membrane with equal IDA evidence, so 'primary' is not unambiguously derivable from the sequence.


**Missing item-specific fact**

> The specific experimental finding (Ref.4, ECO:0000269) that soybean HAL3a localizes to the nucleus, and the broader biological knowledge that HAL3 orthologs (yeast HAL3/CDC28) are nuclear transcription factors with PPCDC activity. The sequence alone provides no clear nuclear targeting signal to distinguish nucleus from cytoplasm or membrane.


**Reason**

> While general elimination removes A and C, and B is too generic, the positive assignment to nucleus over other possible compartments (cytoplasm, membrane) requires item-specific knowledge of HAL3/PPCDC biology. The sequence lacks a clear NLS, and the protein is experimentally dual-localized (nucleus + membrane), making 'nucleus as primary' a database-annotation fact rather than a sequence-derivable inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Option B (protein-containing complex) is technically supported: PPCDC forms a homotrimeric complex annotated as GO:0071513, which is_a GO:0032991 (protein-containing complex). In GO, 'protein-containing complex' is a valid cellular component term. However, it is an extremely broad assembly category, and the question asks for the 'primary' compartment, which conventionally favors a spatial location (nucleus) over a generic assembly type. Additionally, the protein is dual-localized (nucleus + cell membrane per IDA evidence), but membrane is not among the options, reducing ambiguity among the given choices.


### Important caveats

- The UniProt entry annotates BOTH nucleus and cell membrane with IDA evidence; neither is designated 'primary.' The question's phrasing 'primary Cellular Component' is not strictly resolved by the annotation.
- Option B (protein-containing complex) is a valid GO cellular component term and is supported by the PPCDC complex annotation (GO:0071513 is_a GO:0032991), though it is far more generic than a compartment.
- The protein was integrated into Swiss-Prot on 2025-04-09; the benchmark's exact construction date is unknown, so the annotation state at authoring time may differ from the current snapshot.
- The sequence lacks a canonical NLS motif, making nuclear assignment non-trivial from sequence alone.
- The GO term 'phosphopantothenoylcysteine decarboxylase complex' (GO:0071513) is annotated as part_of cytoplasm (GO:0005737), which could argue for a cytoplasmic location, though this is an IBA (inferred by biological aspect) annotation from GO_Central, not experimental.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Distractors A (NF-kappaB complex) and C (spindle) can be eliminated by general knowledge: NF-kappaB is an animal-specific immune signaling complex irrelevant to a plant enzyme, and spindle is a mitotic microtubule structure with no connection to a CoA-biosynthesis enzyme. Option B (protein-containing complex) is technically valid (PPCDC forms a homotrimer) but is an extremely broad GO category. The remaining choice is D (nucleus). However, the 211-aa sequence lacks a recognizable classical NLS (e.g., PKKKRKV-type motif), has no transmembrane helix, and no mitochondrial targeting peptide. Without knowing that HAL3/PPCDC orthologs (particularly the well-studied yeast HAL3 transcription factor) are nuclear, a model cannot confidently assign nucleus over cytoplasm or membrane from sequence features alone. The UniProt entry itself lists both nucleus AND cell membrane with equal IDA evidence, so 'primary' is not unambiguously derivable from the sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental finding (Ref.4, ECO:0000269) that soybean HAL3a localizes to the nucleus, and the broader biological knowledge that HAL3 orthologs (yeast HAL3/CDC28) are nuclear transcription factors with PPCDC activity. The sequence alone provides no clear nuclear targeting signal to distinguish nucleus from cytoplasm or membrane.",
    "reason": "While general elimination removes A and C, and B is too generic, the positive assignment to nucleus over other possible compartments (cytoplasm, membrane) requires item-specific knowledge of HAL3/PPCDC biology. The sequence lacks a clear NLS, and the protein is experimentally dual-localized (nucleus + membrane), making 'nucleus as primary' a database-annotation fact rather than a sequence-derivable inference."
  },
  "case_id": "GO_cellular_component_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 (HAL3A_SOYBN, PPCDC/HAL3a from Glycine max) annotates nucleus (GO:0005634) with IDA (Inferred from Direct Assay) evidence, confirmed by experimental Ref.4. The expected answer 'nucleus' is directly supported. However, the same entry also annotates cell membrane/plasma membrane (GO:0005886, IDA), so the protein is dual-localized. Among the four provided options, nucleus is the only specific compartment with direct experimental annotation; plasma membrane is not offered as a choice. The GO term 'phosphopantothenoylcysteine decarboxylase complex' (GO:0071513, IBA) is_a 'protein-containing complex' (GO:0032991), so option B is technically also supported by annotation, but nucleus is the more specific compartment-level answer."
  },
  "important_caveats": [
    "The UniProt entry annotates BOTH nucleus and cell membrane with IDA evidence; neither is designated 'primary.' The question's phrasing 'primary Cellular Component' is not strictly resolved by the annotation.",
    "Option B (protein-containing complex) is a valid GO cellular component term and is supported by the PPCDC complex annotation (GO:0071513 is_a GO:0032991), though it is far more generic than a compartment.",
    "The protein was integrated into Swiss-Prot on 2025-04-09; the benchmark's exact construction date is unknown, so the annotation state at authoring time may differ from the current snapshot.",
    "The sequence lacks a canonical NLS motif, making nuclear assignment non-trivial from sequence alone.",
    "The GO term 'phosphopantothenoylcysteine decarboxylase complex' (GO:0071513) is annotated as part_of cytoplasm (GO:0005737), which could argue for a cytoplasmic location, though this is an IBA (inferred by biological aspect) annotation from GO_Central, not experimental."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Option B (protein-containing complex) is technically supported: PPCDC forms a homotrimeric complex annotated as GO:0071513, which is_a GO:0032991 (protein-containing complex). In GO, 'protein-containing complex' is a valid cellular component term. However, it is an extremely broad assembly category, and the question asks for the 'primary' compartment, which conventionally favors a spatial location (nucleus) over a generic assembly type. Additionally, the protein is dual-localized (nucleus + cell membrane per IDA evidence), but membrane is not among the options, reducing ambiguity among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 (HAL3A_SOYBN, PPCDC/HAL3a from Glycine max) annotates nucleus (GO:0005634) with IDA (Inferred from Direct Assay) evidence, confirmed by experimental Ref.4. The expected answer 'nucleus' is directly supported. However, the same entry also annotates cell membrane/plasma membrane (GO:0005886, IDA), so the protein is dual-localized. Among the four provided options, nucleus is the only specific compartment with direct experimental annotation; plasma membrane is not offered as a choice. The GO term 'phosphopantothenoylcysteine decarboxylase complex' (GO:0071513, IBA) is_a 'protein-containing complex' (GO:0032991), so option B is technically also supported by annotation, but nucleus is the more specific compartment-level answer.",
    "evidence_ids": ["C5", "C6", "C8", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Distractors A (NF-kappaB complex) and C (spindle) can be eliminated by general knowledge: NF-kappaB is an animal-specific immune signaling complex irrelevant to a plant enzyme, and spindle is a mitotic microtubule structure with no connection to a CoA-biosynthesis enzyme. Option B (protein-containing complex) is technically valid (PPCDC forms a homotrimer) but is an extremely broad GO category. The remaining choice is D (nucleus). However, the 211-aa sequence lacks a recognizable classical NLS (e.g., PKKKRKV-type motif), has no transmembrane helix, and no mitochondrial targeting peptide. Without knowing that HAL3/PPCDC orthologs (particularly the well-studied yeast HAL3 transcription factor) are nuclear, a model cannot confidently assign nucleus over cytoplasm or membrane from sequence features alone. The UniProt entry itself lists both nucleus AND cell membrane with equal IDA evidence, so 'primary' is not unambiguously derivable from the sequence.",
    "missing_item_specific_fact": "The specific experimental finding (Ref.4, ECO:0000269) that soybean HAL3a localizes to the nucleus, and the broader biological knowledge that HAL3 orthologs (yeast HAL3/CDC28) are nuclear transcription factors with PPCDC activity. The sequence alone provides no clear nuclear targeting signal to distinguish nucleus from cytoplasm or membrane.",
    "reason": "While general elimination removes A and C, and B is too generic, the positive assignment to nucleus over other possible compartments (cytoplasm, membrane) requires item-specific knowledge of HAL3/PPCDC biology. The sequence lacks a clear NLS, and the protein is experimentally dual-localized (nucleus + membrane), making 'nucleus as primary' a database-annotation fact rather than a sequence-derivable inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Option B (protein-containing complex) is technically supported: PPCDC forms a homotrimeric complex annotated as GO:0071513, which is_a GO:0032991 (protein-containing complex). In GO, 'protein-containing complex' is a valid cellular component term. However, it is an extremely broad assembly category, and the question asks for the 'primary' compartment, which conventionally favors a spatial location (nucleus) over a generic assembly type. Additionally, the protein is dual-localized (nucleus + cell membrane per IDA evidence), but membrane is not among the options, reducing ambiguity among the given choices."
  },
  "important_caveats": [
    "The UniProt entry annotates BOTH nucleus and cell membrane with IDA evidence; neither is designated 'primary.' The question's phrasing 'primary Cellular Component' is not strictly resolved by the annotation.",
    "Option B (protein-containing complex) is a valid GO cellular component term and is supported by the PPCDC complex annotation (GO:0071513 is_a GO:0032991), though it is far more generic than a compartment.",
    "The protein was integrated into Swiss-Prot on 2025-04-09; the benchmark's exact construction date is unknown, so the annotation state at authoring time may differ from the current snapshot.",
    "The sequence lacks a canonical NLS motif, making nuclear assignment non-trivial from sequence alone.",
    "The GO term 'phosphopantothenoylcysteine decarboxylase complex' (GO:0071513) is annotated as part_of cytoplasm (GO:0005737), which could argue for a cytoplasmic location, though this is an IBA (inferred by biological aspect) annotation from GO_Central, not experimental."
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

**Accession:** `C6SZ50` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 84. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:34.573952+00:00.  

```json
"C6SZ50"
```

Source SHA-256: `d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:34.573952+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"Ref.4","source":"Reference"}],"id":"SL-0039","value":"Cell membrane"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"Ref.4","source":"Reference"}],"id":"SL-0191","value":"Nucleus"}}]}
```

Source SHA-256: `d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)  
**Locator:** `/uniProtKBCrossReferences/28`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:34.573952+00:00.  

```json
{"database":"GO","id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)  
**Locator:** `/uniProtKBCrossReferences/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:34.573952+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)  
**Locator:** `lines 78-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:36.741333+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|Ref.4}. Nucleus
CC       {ECO:0000269|Ref.4}.
```

Source SHA-256: `1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)  
**Locator:** `lines 122-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:36.741333+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; IDA:UniProtKB.
```

Source SHA-256: `1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)  
**Locator:** `lines 123-123`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:36.741333+00:00.  

```text
DR   GO; GO:0071513; C:phosphopantothenoylcysteine decarboxylase complex; IBA:GO_Central.
```

Source SHA-256: `1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)  
**Locator:** `lines 124-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:36.741333+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.
```

Source SHA-256: `1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 59. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
