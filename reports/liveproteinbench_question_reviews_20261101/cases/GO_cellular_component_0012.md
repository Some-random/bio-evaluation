# GO_cellular_component_0012

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — phosphopantothenoylcysteine decarboxylase complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGSEPVSAEGESMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSSSGSLHFIDRASMPKDVILYTDEDEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWNNPFTERHFISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGRAVVTLR

[Multiple Choices]
A. phosphopantothenoylcysteine decarboxylase complex
B. cell tip
C. mannosyltransferase complex
D. nuclear pore
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

> The exact sequence matches a soybean HAL3b/PPCDC protein, and the matched UniProt record annotates it to the phosphopantothenoylcysteine decarboxylase complex. This is computational phylogenetic inference (IBA), not direct experimental evidence for complex membership. The record also reports experimental nucleus and cell-membrane localization, so the complex annotation does not establish an exclusive or primary location.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence appears to encode a compact soluble protein, which may make some membrane-associated interpretations less likely, but it does not provide a clear signal that distinguishes the PPCDC complex from the other listed cellular locations.


**Missing item-specific fact**

> The protein-specific identity/function as HAL3b/PPCDC and its association with the PPCDC complex are needed to select A; those facts are not supplied in the question.


**Reason**

> Identifying the relevant complex requires protein-specific annotation or recognition of the sequence as this particular enzyme. Generic sequence features do not meaningfully distinguish A from the remaining choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is the only listed option directly supported by the matched record. However, the wording “primary” suggests a single exclusive location, which the evidence does not establish; the record also reports nucleus and cell-membrane localization, neither of which is a listed choice.


### Important caveats

- The PPCDC-complex annotation is IBA (phylogenetic inference), whereas nucleus and cell-membrane annotations are reported with IDA evidence.
- The exact author source snapshot is unknown, although the matching historical record contains the complex annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence appears to encode a compact soluble protein, which may make some membrane-associated interpretations less likely, but it does not provide a clear signal that distinguishes the PPCDC complex from the other listed cellular locations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity/function as HAL3b/PPCDC and its association with the PPCDC complex are needed to select A; those facts are not supplied in the question.",
    "reason": "Identifying the relevant complex requires protein-specific annotation or recognition of the sequence as this particular enzyme. Generic sequence features do not meaningfully distinguish A from the remaining choices."
  },
  "case_id": "GO_cellular_component_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a soybean HAL3b/PPCDC protein, and the matched UniProt record annotates it to the phosphopantothenoylcysteine decarboxylase complex. This is computational phylogenetic inference (IBA), not direct experimental evidence for complex membership. The record also reports experimental nucleus and cell-membrane localization, so the complex annotation does not establish an exclusive or primary location."
  },
  "important_caveats": [
    "The PPCDC-complex annotation is IBA (phylogenetic inference), whereas nucleus and cell-membrane annotations are reported with IDA evidence.",
    "The exact author source snapshot is unknown, although the matching historical record contains the complex annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the only listed option directly supported by the matched record. However, the wording “primary” suggests a single exclusive location, which the evidence does not establish; the record also reports nucleus and cell-membrane localization, neither of which is a listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a soybean HAL3b/PPCDC protein, and the matched UniProt record annotates it to the phosphopantothenoylcysteine decarboxylase complex. This is computational phylogenetic inference (IBA), not direct experimental evidence for complex membership. The record also reports experimental nucleus and cell-membrane localization, so the complex annotation does not establish an exclusive or primary location.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence appears to encode a compact soluble protein, which may make some membrane-associated interpretations less likely, but it does not provide a clear signal that distinguishes the PPCDC complex from the other listed cellular locations.",
    "missing_item_specific_fact": "The protein-specific identity/function as HAL3b/PPCDC and its association with the PPCDC complex are needed to select A; those facts are not supplied in the question.",
    "reason": "Identifying the relevant complex requires protein-specific annotation or recognition of the sequence as this particular enzyme. Generic sequence features do not meaningfully distinguish A from the remaining choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the only listed option directly supported by the matched record. However, the wording “primary” suggests a single exclusive location, which the evidence does not establish; the record also reports nucleus and cell-membrane localization, neither of which is a listed choice."
  },
  "important_caveats": [
    "The PPCDC-complex annotation is IBA (phylogenetic inference), whereas nucleus and cell-membrane annotations are reported with IDA evidence.",
    "The exact author source snapshot is unknown, although the matching historical record contains the complex annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (C6TA59, HAL3B_SOYBN) is annotated in UniProt with GO:0071513 (phosphopantothenoylcysteine decarboxylase complex) via IBA:GO_Central evidence (C7, H4). The protein's recommended name is 'Phosphopantothenoylcysteine decarboxylase HAL3b' with EC 4.1.1.36, and the GO term defines the complex that catalyzes this exact reaction. While the evidence code is computational inference (IBA) rather than experimental, the annotation is present in the database and is biologically coherent: a PPCDC enzyme would logically be a member of the PPCDC complex. The experimental subcellular location data (Cell membrane, Nucleus; ECO:0000269) does not correspond to any other listed option, so A remains the best-supported choice among the four.

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 214-aa sequence lacks any obvious nuclear localization signal, transmembrane helix, FG-repeat pattern (nuclear pore), mannosyltransferase catalytic domain, or cell-tip-specific targeting motif. One might weakly argue by elimination that the absence of these features disfavors B, C, and D, but this does not positively identify the protein as PPCDC or justify membership in the PPCDC complex. Recognizing the sequence as a phosphopantothenoylcysteine decarboxylase requires homology knowledge of the PPCDC/CoaE enzyme family, and knowing that PPCDC forms a homotrimeric complex annotated as GO:0071513 requires item-specific database knowledge.


**Missing item-specific fact**

> The specific identification of this sequence as a PPCDC enzyme (EC 4.1.1.36) and the knowledge that PPCDC enzymes assemble into the homotrimeric 'phosphopantothenoylcysteine decarboxylase complex' (GO:0071513) are not derivable from general biological reasoning applied to the raw sequence alone.


**Reason**

> Distinguishing option A from B, C, and D requires recognizing the protein's enzymatic identity from its sequence (a lookup/homology task) and then knowing the specific GO complex annotation. No general biological principle applied to the sequence alone meaningfully separates 'PPCDC complex' from 'mannosyltransferase complex' or 'nuclear pore' without prior identification of the protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimental subcellular location annotations (Cell membrane, Nucleus) do not match any option. 'Nuclear pore' (D) is a distinct structure from 'nucleus' and is not annotated for this protein. 'Cell tip' (B) and 'mannosyltransferase complex' (C) have no annotation support. Only option A has a GO annotation (GO:0071513, IBA) in the database for this protein, making it the sole defensible choice among the four.


### Important caveats

- The GO:0071513 annotation carries evidence code IBA:GO_Central (computational inference), not experimental evidence. The experimental (IDA) annotations point to nucleus and plasma membrane, neither of which appears as a standalone option.
- The protein was first publicly released in UniProt on 2025-04-09; the benchmark author's data-construction date and source snapshot are unknown, so the annotation may not have existed when the question was authored.
- The sequence lacks canonical PPCDC motifs that would be immediately recognizable without prior knowledge of the enzyme family; the 214-aa length is consistent with plant PPCDC but does not uniquely identify it from sequence alone.
- GO:0071513 is defined as 'part_of cytoplasm' in the ontology, creating a slight tension with the experimental location data showing cell membrane and nucleus, though complex membership and physical location are distinct GO aspects.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 214-aa sequence lacks any obvious nuclear localization signal, transmembrane helix, FG-repeat pattern (nuclear pore), mannosyltransferase catalytic domain, or cell-tip-specific targeting motif. One might weakly argue by elimination that the absence of these features disfavors B, C, and D, but this does not positively identify the protein as PPCDC or justify membership in the PPCDC complex. Recognizing the sequence as a phosphopantothenoylcysteine decarboxylase requires homology knowledge of the PPCDC/CoaE enzyme family, and knowing that PPCDC forms a homotrimeric complex annotated as GO:0071513 requires item-specific database knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this sequence as a PPCDC enzyme (EC 4.1.1.36) and the knowledge that PPCDC enzymes assemble into the homotrimeric 'phosphopantothenoylcysteine decarboxylase complex' (GO:0071513) are not derivable from general biological reasoning applied to the raw sequence alone.",
    "reason": "Distinguishing option A from B, C, and D requires recognizing the protein's enzymatic identity from its sequence (a lookup/homology task) and then knowing the specific GO complex annotation. No general biological principle applied to the sequence alone meaningfully separates 'PPCDC complex' from 'mannosyltransferase complex' or 'nuclear pore' without prior identification of the protein."
  },
  "case_id": "GO_cellular_component_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein (C6TA59, HAL3B_SOYBN) is annotated in UniProt with GO:0071513 (phosphopantothenoylcysteine decarboxylase complex) via IBA:GO_Central evidence (C7, H4). The protein's recommended name is 'Phosphopantothenoylcysteine decarboxylase HAL3b' with EC 4.1.1.36, and the GO term defines the complex that catalyzes this exact reaction. While the evidence code is computational inference (IBA) rather than experimental, the annotation is present in the database and is biologically coherent: a PPCDC enzyme would logically be a member of the PPCDC complex. The experimental subcellular location data (Cell membrane, Nucleus; ECO:0000269) does not correspond to any other listed option, so A remains the best-supported choice among the four."
  },
  "important_caveats": [
    "The GO:0071513 annotation carries evidence code IBA:GO_Central (computational inference), not experimental evidence. The experimental (IDA) annotations point to nucleus and plasma membrane, neither of which appears as a standalone option.",
    "The protein was first publicly released in UniProt on 2025-04-09; the benchmark author's data-construction date and source snapshot are unknown, so the annotation may not have existed when the question was authored.",
    "The sequence lacks canonical PPCDC motifs that would be immediately recognizable without prior knowledge of the enzyme family; the 214-aa length is consistent with plant PPCDC but does not uniquely identify it from sequence alone.",
    "GO:0071513 is defined as 'part_of cytoplasm' in the ontology, creating a slight tension with the experimental location data showing cell membrane and nucleus, though complex membership and physical location are distinct GO aspects."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental subcellular location annotations (Cell membrane, Nucleus) do not match any option. 'Nuclear pore' (D) is a distinct structure from 'nucleus' and is not annotated for this protein. 'Cell tip' (B) and 'mannosyltransferase complex' (C) have no annotation support. Only option A has a GO annotation (GO:0071513, IBA) in the database for this protein, making it the sole defensible choice among the four."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (C6TA59, HAL3B_SOYBN) is annotated in UniProt with GO:0071513 (phosphopantothenoylcysteine decarboxylase complex) via IBA:GO_Central evidence (C7, H4). The protein's recommended name is 'Phosphopantothenoylcysteine decarboxylase HAL3b' with EC 4.1.1.36, and the GO term defines the complex that catalyzes this exact reaction. While the evidence code is computational inference (IBA) rather than experimental, the annotation is present in the database and is biologically coherent: a PPCDC enzyme would logically be a member of the PPCDC complex. The experimental subcellular location data (Cell membrane, Nucleus; ECO:0000269) does not correspond to any other listed option, so A remains the best-supported choice among the four.",
    "evidence_ids": ["C4", "C7", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The 214-aa sequence lacks any obvious nuclear localization signal, transmembrane helix, FG-repeat pattern (nuclear pore), mannosyltransferase catalytic domain, or cell-tip-specific targeting motif. One might weakly argue by elimination that the absence of these features disfavors B, C, and D, but this does not positively identify the protein as PPCDC or justify membership in the PPCDC complex. Recognizing the sequence as a phosphopantothenoylcysteine decarboxylase requires homology knowledge of the PPCDC/CoaE enzyme family, and knowing that PPCDC forms a homotrimeric complex annotated as GO:0071513 requires item-specific database knowledge.",
    "missing_item_specific_fact": "The specific identification of this sequence as a PPCDC enzyme (EC 4.1.1.36) and the knowledge that PPCDC enzymes assemble into the homotrimeric 'phosphopantothenoylcysteine decarboxylase complex' (GO:0071513) are not derivable from general biological reasoning applied to the raw sequence alone.",
    "reason": "Distinguishing option A from B, C, and D requires recognizing the protein's enzymatic identity from its sequence (a lookup/homology task) and then knowing the specific GO complex annotation. No general biological principle applied to the sequence alone meaningfully separates 'PPCDC complex' from 'mannosyltransferase complex' or 'nuclear pore' without prior identification of the protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental subcellular location annotations (Cell membrane, Nucleus) do not match any option. 'Nuclear pore' (D) is a distinct structure from 'nucleus' and is not annotated for this protein. 'Cell tip' (B) and 'mannosyltransferase complex' (C) have no annotation support. Only option A has a GO annotation (GO:0071513, IBA) in the database for this protein, making it the sole defensible choice among the four."
  },
  "important_caveats": [
    "The GO:0071513 annotation carries evidence code IBA:GO_Central (computational inference), not experimental evidence. The experimental (IDA) annotations point to nucleus and plasma membrane, neither of which appears as a standalone option.",
    "The protein was first publicly released in UniProt on 2025-04-09; the benchmark author's data-construction date and source snapshot are unknown, so the annotation may not have existed when the question was authored.",
    "The sequence lacks canonical PPCDC motifs that would be immediately recognizable without prior knowledge of the enzyme family; the 214-aa length is consistent with plant PPCDC but does not uniquely identify it from sequence alone.",
    "GO:0071513 is defined as 'part_of cytoplasm' in the ontology, creating a slight tension with the experimental location data showing cell membrane and nucleus, though complex membership and physical location are distinct GO aspects."
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

**Accession:** `C6TA59` (recovered from dataset image-path metadata, not original question text).  
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
"C6TA59"
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.3","source":"Reference"},{"evidenceCode":"ECO:0000303","id":"Ref.4","source":"Reference"}],"value":"Halotolerance protein 3b"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.3","source":"Reference"},{"evidenceCode":"ECO:0000303","id":"Ref.4","source":"Reference"}],"value":"GmHAL3b"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9SWE5","source":"UniProtKB"}],"value":"4.1.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Phosphopantothenoylcysteine decarboxylase HAL3b"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PPCDC"}]}}
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"Ref.4","source":"Reference"}],"id":"SL-0039","value":"Cell membrane"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"Ref.4","source":"Reference"}],"id":"SL-0191","value":"Nucleus"}}]}
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)  
**Locator:** `/uniProtKBCrossReferences/25`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.244012+00:00.  

```json
{"database":"GO","id":"GO:0071513","properties":[{"key":"GoTerm","value":"C:phosphopantothenoylcysteine decarboxylase complex"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)  
**Locator:** `lines 78-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:37.263279+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|Ref.4}. Nucleus
CC       {ECO:0000269|Ref.4}.
```

Source SHA-256: `9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)  
**Locator:** `lines 119-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:27:37.263279+00:00.  

```text
DR   GO; GO:0071513; C:phosphopantothenoylcysteine decarboxylase complex; IBA:GO_Central.
```

Source SHA-256: `9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 377848-377856`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0071513
name: phosphopantothenoylcysteine decarboxylase complex
namespace: cellular_component
def: "A protein complex that catalyzes decarboxylation of 4'-phosphopantothenoylcysteine to yield 4'-phosphopantetheine; this is the third step in the biosynthesis of Coenzyme A. The complex is homotrimeric in many eukaryotes, but is a heterotrimer in Saccharomyces." [GOC:jh, PMID:19915539]
comment: See also the molecular function term 'acetolactate synthase activity ; GO:0003984'.
is_a: GO:1902494 ! catalytic complex
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
