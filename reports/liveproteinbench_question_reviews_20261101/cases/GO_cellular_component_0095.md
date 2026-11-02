# GO_cellular_component_0095

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — nuclear envelope

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | uncertain | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key differ; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MADKETLLKLREDFKMQNKSVFILGASGETGKVLLKEILGQNLFSKVTLIGRRKLTFEEEAYNNVNQEVVDFEKLDEYAPAFQGHDVGFCCLGTTRRKAGADGFVRVDRDYVLKSAELAKAGGCKHFNLLSSRGADKSSSFLYLQVKGEVEAKVEELKFDRLSVFRPGVLLCDRQESRPGEWLARKFFGSLPDSWASGYAVPVVTVVRAMLNNLVSPGSGQMELLENKAILHLGKDSDGPKL

[Multiple Choices]
A. replisome
B. periplasmic space
C. nuclear envelope
D. RNA polymerase II transcription regulator complex
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

### Expected-answer support: uncertain

> The sequence matches rat HTATIP2, but the supplied database excerpts annotate cytoplasm and cytosol, and the current entry also lists mitochondrion; none establishes nuclear-envelope localization. These annotations do not rule it out, and the excerpts may be incomplete. The key is therefore unresolved by the supplied evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a soluble-looking protein without an obvious signal peptide or transmembrane segment, which offers some broad context but does not distinguish nuclear-envelope association from the other intracellular complex choices.


**Missing item-specific fact**

> Protein-specific localization or complex-membership evidence is needed to select among the listed intracellular possibilities and establish which, if any, is the primary component.


**Reason**

> The sequence and choices provide no reliable biological feature that specifically supports nuclear-envelope localization over replisome or transcription-regulator-complex membership. Selecting a particular option depends on item-specific annotation or experimental evidence not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available evidence does not establish any listed option as the primary component. It also does not exclude nuclear-envelope localization; the annotations shown are not exhaustive.


### Important caveats

- Reviewer-only accession and database evidence were not present in the evaluated model input.
- The sequence match identifies rat HTATIP2, but database localization annotations do not by themselves prove exclusive or primary localization.
- The current mitochondrial annotation uses IBA evidence; the cytoplasm and cytosol annotations use ISO:RGD evidence. The historical excerpts show cytoplasm and cytosol annotations.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble-looking protein without an obvious signal peptide or transmembrane segment, which offers some broad context but does not distinguish nuclear-envelope association from the other intracellular complex choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Protein-specific localization or complex-membership evidence is needed to select among the listed intracellular possibilities and establish which, if any, is the primary component.",
    "reason": "The sequence and choices provide no reliable biological feature that specifically supports nuclear-envelope localization over replisome or transcription-regulator-complex membership. Selecting a particular option depends on item-specific annotation or experimental evidence not supplied to the evaluated model."
  },
  "case_id": "GO_cellular_component_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "cannot_determine",
    "reason": "The sequence matches rat HTATIP2, but the supplied database excerpts annotate cytoplasm and cytosol, and the current entry also lists mitochondrion; none establishes nuclear-envelope localization. These annotations do not rule it out, and the excerpts may be incomplete. The key is therefore unresolved by the supplied evidence."
  },
  "important_caveats": [
    "Reviewer-only accession and database evidence were not present in the evaluated model input.",
    "The sequence match identifies rat HTATIP2, but database localization annotations do not by themselves prove exclusive or primary localization.",
    "The current mitochondrial annotation uses IBA evidence; the cytoplasm and cytosol annotations use ISO:RGD evidence. The historical excerpts show cytoplasm and cytosol annotations.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available evidence does not establish any listed option as the primary component. It also does not exclude nuclear-envelope localization; the annotations shown are not exhaustive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0095",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The sequence matches rat HTATIP2, but the supplied database excerpts annotate cytoplasm and cytosol, and the current entry also lists mitochondrion; none establishes nuclear-envelope localization. These annotations do not rule it out, and the excerpts may be incomplete. The key is therefore unresolved by the supplied evidence.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a soluble-looking protein without an obvious signal peptide or transmembrane segment, which offers some broad context but does not distinguish nuclear-envelope association from the other intracellular complex choices.",
    "missing_item_specific_fact": "Protein-specific localization or complex-membership evidence is needed to select among the listed intracellular possibilities and establish which, if any, is the primary component.",
    "reason": "The sequence and choices provide no reliable biological feature that specifically supports nuclear-envelope localization over replisome or transcription-regulator-complex membership. Selecting a particular option depends on item-specific annotation or experimental evidence not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available evidence does not establish any listed option as the primary component. It also does not exclude nuclear-envelope localization; the annotations shown are not exhaustive."
  },
  "important_caveats": [
    "Reviewer-only accession and database evidence were not present in the evaluated model input.",
    "The sequence match identifies rat HTATIP2, but database localization annotations do not by themselves prove exclusive or primary localization.",
    "The current mitochondrial annotation uses IBA evidence; the cytoplasm and cytosol annotations use ISO:RGD evidence. The historical excerpts show cytoplasm and cytosol annotations.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The UniProt annotations for B0BNF8 (HTATIP2/TIP30, rat) show cellular component GO terms for cytoplasm (GO:0005737, ISO:RGD), cytosol (GO:0005829, ISO:RGD), and mitochondrion (GO:0005739, IBA:GO_Central). No nuclear envelope (GO:0005635) annotation appears in either the current entry or the historical entry (version 117). The positive ISO:RGD annotations for cytoplasm/cytosol are incompatible with the primary localization being the nuclear envelope. HTATIP2/TIP30 is a well-characterized cytoplasmic/cytosolic protein with reported mitochondrial association, not a nuclear envelope resident.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option B (periplasmic space) can be eliminated by general knowledge since this is a eukaryotic (rat) protein and periplasmic space is a bacterial/fungal compartment. However, among the remaining options (replisome, nuclear envelope, RNA Pol II transcription regulator complex), the sequence provides no clear targeting signals (no obvious NLS, no transmembrane domains, no DNA-binding or polymerase motifs) that would distinguish one from the others. The sequence lacks features that would specifically predict nuclear envelope localization over the other nuclear-associated complexes.


**Missing item-specific fact**

> The specific UniProt/GO annotation of HTATIP2 (B0BNF8) is needed, and even that annotation does not support 'nuclear envelope'—it supports cytoplasm/cytosol/mitochondrion. No sequence-derived feature in the provided input distinguishes nuclear envelope from the other options.


**Reason**

> The question cannot be resolved by reasoning from the sequence alone. The expected answer is not supported by the protein's actual annotations, and no sequence feature (NLS, transmembrane helix, replication factor motif, transcription factor domain) points specifically to the nuclear envelope. Selection among A, C, D requires item-specific annotation knowledge that is absent from the input and, when consulted, contradicts the expected answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C",
  "D"
]
```

> All three remaining options (replisome, nuclear envelope, RNA Pol II transcription regulator complex) are nuclear or nuclear-associated complexes. Without a clear targeting signal or functional domain in the sequence, none can be confidently selected over the others by reasoning alone. Option B is eliminable (periplasmic space is prokaryotic/fungal). The expected answer C is not supported by the protein's actual GO annotations (cytoplasm/cytosol/mitochondrion), making the question defective in its key.


### Important caveats

- The expected answer 'nuclear envelope' is contradicted by the available UniProt annotations (cytoplasm, cytosol, mitochondrion with ISO:RGD and IBA evidence codes).
- The correct primary localization based on annotations (cytoplasm/cytosol) is not among the answer choices, suggesting a possible error in question construction.
- The accession B0BNF8 was inferred from dataset metadata (reviewer-only); the evaluated model had only the raw sequence.
- Evidence excerpts may be incomplete, but the ISO:RGD annotations for cytoplasm/cytosol are strong positive annotations that argue against nuclear envelope as the primary location.
- The GO ontology definition for nuclear envelope (GO:0005635) describes a double lipid bilayer structure—this is a structural compartment, not a protein complex, further distinguishing it from options A and D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B (periplasmic space) can be eliminated by general knowledge since this is a eukaryotic (rat) protein and periplasmic space is a bacterial/fungal compartment. However, among the remaining options (replisome, nuclear envelope, RNA Pol II transcription regulator complex), the sequence provides no clear targeting signals (no obvious NLS, no transmembrane domains, no DNA-binding or polymerase motifs) that would distinguish one from the others. The sequence lacks features that would specifically predict nuclear envelope localization over the other nuclear-associated complexes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt/GO annotation of HTATIP2 (B0BNF8) is needed, and even that annotation does not support 'nuclear envelope'—it supports cytoplasm/cytosol/mitochondrion. No sequence-derived feature in the provided input distinguishes nuclear envelope from the other options.",
    "reason": "The question cannot be resolved by reasoning from the sequence alone. The expected answer is not supported by the protein's actual annotations, and no sequence feature (NLS, transmembrane helix, replication factor motif, transcription factor domain) points specifically to the nuclear envelope. Selection among A, C, D requires item-specific annotation knowledge that is absent from the input and, when consulted, contradicts the expected answer."
  },
  "case_id": "GO_cellular_component_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H2",
      "H3"
    ],
    "judgment": "contradicted",
    "reason": "The UniProt annotations for B0BNF8 (HTATIP2/TIP30, rat) show cellular component GO terms for cytoplasm (GO:0005737, ISO:RGD), cytosol (GO:0005829, ISO:RGD), and mitochondrion (GO:0005739, IBA:GO_Central). No nuclear envelope (GO:0005635) annotation appears in either the current entry or the historical entry (version 117). The positive ISO:RGD annotations for cytoplasm/cytosol are incompatible with the primary localization being the nuclear envelope. HTATIP2/TIP30 is a well-characterized cytoplasmic/cytosolic protein with reported mitochondrial association, not a nuclear envelope resident."
  },
  "important_caveats": [
    "The expected answer 'nuclear envelope' is contradicted by the available UniProt annotations (cytoplasm, cytosol, mitochondrion with ISO:RGD and IBA evidence codes).",
    "The correct primary localization based on annotations (cytoplasm/cytosol) is not among the answer choices, suggesting a possible error in question construction.",
    "The accession B0BNF8 was inferred from dataset metadata (reviewer-only); the evaluated model had only the raw sequence.",
    "Evidence excerpts may be incomplete, but the ISO:RGD annotations for cytoplasm/cytosol are strong positive annotations that argue against nuclear envelope as the primary location.",
    "The GO ontology definition for nuclear envelope (GO:0005635) describes a double lipid bilayer structure—this is a structural compartment, not a protein complex, further distinguishing it from options A and D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C",
      "D"
    ],
    "reason": "All three remaining options (replisome, nuclear envelope, RNA Pol II transcription regulator complex) are nuclear or nuclear-associated complexes. Without a clear targeting signal or functional domain in the sequence, none can be confidently selected over the others by reasoning alone. Option B is eliminable (periplasmic space is prokaryotic/fungal). The expected answer C is not supported by the protein's actual GO annotations (cytoplasm/cytosol/mitochondrion), making the question defective in its key."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0095",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The UniProt annotations for B0BNF8 (HTATIP2/TIP30, rat) show cellular component GO terms for cytoplasm (GO:0005737, ISO:RGD), cytosol (GO:0005829, ISO:RGD), and mitochondrion (GO:0005739, IBA:GO_Central). No nuclear envelope (GO:0005635) annotation appears in either the current entry or the historical entry (version 117). The positive ISO:RGD annotations for cytoplasm/cytosol are incompatible with the primary localization being the nuclear envelope. HTATIP2/TIP30 is a well-characterized cytoplasmic/cytosolic protein with reported mitochondrial association, not a nuclear envelope resident.",
    "evidence_ids": ["C5", "C6", "C7", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option B (periplasmic space) can be eliminated by general knowledge since this is a eukaryotic (rat) protein and periplasmic space is a bacterial/fungal compartment. However, among the remaining options (replisome, nuclear envelope, RNA Pol II transcription regulator complex), the sequence provides no clear targeting signals (no obvious NLS, no transmembrane domains, no DNA-binding or polymerase motifs) that would distinguish one from the others. The sequence lacks features that would specifically predict nuclear envelope localization over the other nuclear-associated complexes.",
    "missing_item_specific_fact": "The specific UniProt/GO annotation of HTATIP2 (B0BNF8) is needed, and even that annotation does not support 'nuclear envelope'—it supports cytoplasm/cytosol/mitochondrion. No sequence-derived feature in the provided input distinguishes nuclear envelope from the other options.",
    "reason": "The question cannot be resolved by reasoning from the sequence alone. The expected answer is not supported by the protein's actual annotations, and no sequence feature (NLS, transmembrane helix, replication factor motif, transcription factor domain) points specifically to the nuclear envelope. Selection among A, C, D requires item-specific annotation knowledge that is absent from the input and, when consulted, contradicts the expected answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C", "D"],
    "reason": "All three remaining options (replisome, nuclear envelope, RNA Pol II transcription regulator complex) are nuclear or nuclear-associated complexes. Without a clear targeting signal or functional domain in the sequence, none can be confidently selected over the others by reasoning alone. Option B is eliminable (periplasmic space is prokaryotic/fungal). The expected answer C is not supported by the protein's actual GO annotations (cytoplasm/cytosol/mitochondrion), making the question defective in its key."
  },
  "important_caveats": [
    "The expected answer 'nuclear envelope' is contradicted by the available UniProt annotations (cytoplasm, cytosol, mitochondrion with ISO:RGD and IBA evidence codes).",
    "The correct primary localization based on annotations (cytoplasm/cytosol) is not among the answer choices, suggesting a possible error in question construction.",
    "The accession B0BNF8 was inferred from dataset metadata (reviewer-only); the evaluated model had only the raw sequence.",
    "Evidence excerpts may be incomplete, but the ISO:RGD annotations for cytoplasm/cytosol are strong positive annotations that argue against nuclear envelope as the primary location.",
    "The GO ontology definition for nuclear envelope (GO:0005635) describes a double lipid bilayer structure—this is a structural compartment, not a protein complex, further distinguishing it from options A and D."
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

**Accession:** `B0BNF8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 117. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:12.867856+00:00.  

```json
"B0BNF8"
```

Source SHA-256: `5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:12.867856+00:00.  

```json
{"database":"GO","id":"GO:0005737","properties":[{"key":"GoTerm","value":"C:cytoplasm"},{"key":"GoEvidenceType","value":"ISO:RGD"}]}
```

Source SHA-256: `5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)  
**Locator:** `/uniProtKBCrossReferences/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:12.867856+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"ISO:RGD"}]}
```

Source SHA-256: `5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)  
**Locator:** `/uniProtKBCrossReferences/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:12.867856+00:00.  

```json
{"database":"GO","id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:27:16.468432+00:00.  

```text
ID   HTAI2_RAT               Reviewed;         242 AA.
AC   B0BNF8; A0A8I6AEZ6; G3V8Y4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-FEB-2008, sequence version 1.
DT   28-JAN-2026, entry version 117.
DE   RecName: Full=Protein HTATIP2 {ECO:0000305};
GN   Name=Htatip2 {ECO:0000312|RGD:1309941};
OS   Rattus norvegicus (Rat).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Rattus.
OX   NCBI_TaxID=10116 {ECO:0000312|Proteomes:UP000002494};
```

Source SHA-256: `c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)  
**Locator:** `lines 129-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:27:16.468432+00:00.  

```text
DR   GO; GO:0005737; C:cytoplasm; ISO:RGD.
```

Source SHA-256: `c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)  
**Locator:** `lines 130-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:27:16.468432+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; ISO:RGD.
```

Source SHA-256: `c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 95. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
