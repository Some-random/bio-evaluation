# GO_biological_process_0052

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — saponin biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEPSKMEVKIISSETIKPSSPTPSHLRKYTLSLLDQKYTPIVVPAILFYERPQGVAPLDMDRLRTCLSQTLTAFYPLAGRAESRDVIICNDEGIPFVEAHVDCELSSVVKSLSSLGSDLRSFYPPRDGLLEGGIQFAIQMNVFSCGGFAFAWYCTHNVTDGTSTANFFRYWTALYAQRSEYAVQDLMDFNSVVTAFPPVPPRVPQEEKPVTTELKPEKQEGQEKEEKKKSSFNFSFQSHIVARSFLIKSKAVAELKAKSVSEEVPYPSRFEAVSAFLWKSIVSSSTTEGKTMINMPVNLRPRVDPPLPLDSVGNIFENALVQSEKKAELHEFVARIRGSISKMKDFATEYQGEKREEAKDAHWKRFIKAVIECKGKDAYVISPWYKSSGFTDIDFGFGTPIRVVPMDDVVNHNQRNTIMLMEFVDSDGDGFEAWMFLEEECIKFLESNPEFLAFASPNF

[Multiple Choices]
A. negative regulation of protein-containing complex assembly
B. mRNA splicing, via spliceosome
C. tRNA methylation
D. saponin biosynthetic process
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

> The supplied sequence exactly matches a soapwort BAHD acyltransferase annotated to the saponin biosynthetic process. The annotation is marked IDA and linked to a cited publication; the entry also describes a role in producing saponarioside B. This supports D, while noting that the cited experiment was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest an acyltransferase, but they do not establish which pathway this particular plant enzyme participates in. The supplied input contains no organism or pathway context.


**Missing item-specific fact**

> The protein-specific evidence that this soapwort acyltransferase acts in saponin biosynthesis, including its reported role in saponarioside B production.


**Reason**

> Selecting D over other possible roles for an acyltransferase requires the protein-specific pathway assignment, absent from the question. Recognizing the sequence or consulting its annotation would supply that missing fact, not constitute reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports D for the sequence-matched protein; no other listed choice is supported by the supplied evidence.


### Important caveats

- The reviewer-only UniProt and publication-linked evidence was not supplied to the evaluated model.
- The actual author source snapshot is unknown, though the sequence matches the historical entry checked.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest an acyltransferase, but they do not establish which pathway this particular plant enzyme participates in. The supplied input contains no organism or pathway context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that this soapwort acyltransferase acts in saponin biosynthesis, including its reported role in saponarioside B production.",
    "reason": "Selecting D over other possible roles for an acyltransferase requires the protein-specific pathway assignment, absent from the question. Recognizing the sequence or consulting its annotation would supply that missing fact, not constitute reasoning from the provided input."
  },
  "case_id": "GO_biological_process_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a soapwort BAHD acyltransferase annotated to the saponin biosynthetic process. The annotation is marked IDA and linked to a cited publication; the entry also describes a role in producing saponarioside B. This supports D, while noting that the cited experiment was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt and publication-linked evidence was not supplied to the evaluated model.",
    "The actual author source snapshot is unknown, though the sequence matches the historical entry checked."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D for the sequence-matched protein; no other listed choice is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a soapwort BAHD acyltransferase annotated to the saponin biosynthetic process. The annotation is marked IDA and linked to a cited publication; the entry also describes a role in producing saponarioside B. This supports D, while noting that the cited experiment was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest an acyltransferase, but they do not establish which pathway this particular plant enzyme participates in. The supplied input contains no organism or pathway context.",
    "missing_item_specific_fact": "The protein-specific evidence that this soapwort acyltransferase acts in saponin biosynthesis, including its reported role in saponarioside B production.",
    "reason": "Selecting D over other possible roles for an acyltransferase requires the protein-specific pathway assignment, absent from the question. Recognizing the sequence or consulting its annotation would supply that missing fact, not constitute reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D for the sequence-matched protein; no other listed choice is supported by the supplied evidence."
  },
  "important_caveats": [
    "The reviewer-only UniProt and publication-linked evidence was not supplied to the evaluated model.",
    "The actual author source snapshot is unknown, though the sequence matches the historical entry checked."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt A0AAW1LG41 (BAHD1_SAPOF, 459 AA, sequence SHA256 matched). The UniProt entry carries GO:0016135 (saponin biosynthetic process) with IDA evidence (Inferred from Direct Assay, PubMed:39043959). The FUNCTION comment explicitly states the protein is 'Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway' and catalyzes acyl transfer to produce saponarioside B. The PATHWAY is listed as 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' This is experimentally supported annotation, not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmarks of a BAHD acyltransferase (plant-specific acyl-CoA-dependent transferase family): the conserved 'HxxDG/DHDD' catalytic region (visible as 'DSDGDG' and 'FGFGTPIRVVPMDD' motifs), the characteristic C-terminal 'FLE' pattern, and overall length (~459 AA) typical of BAHD members. BAHD acyltransferases are well-known enzymes in plant secondary metabolite biosynthesis. Among the four choices, only D (saponin biosynthetic process) is a secondary-metabolite biosynthetic pathway. A (negative regulation of protein complex assembly) is a regulatory process unrelated to enzymatic acyl transfer; B (mRNA splicing via spliceosome) involves spliceosomal snRNP proteins with entirely different domain architectures; C (tRNA methylation) involves RNA methyltransferases, not acyl-CoA-dependent acyltransferases. Thus, recognizing the BAHD family and its general role in plant secondary metabolism is sufficient to eliminate A, B, and C and select D.


**Missing item-specific fact**

> The specific substrate (QA-triF(Q)RXX → saponarioside B) and the organism (Saponaria officinalis) are item-specific facts not derivable from sequence alone. However, these are not needed to distinguish D from the three clearly unrelated distractors.


**Reason**

> The distractors are mechanistically incompatible with an acyltransferase involved in secondary metabolism. General knowledge of the BAHD family's biochemical role and the nature of the other three GO terms provides a concrete biological argument for selecting D without needing to recall the specific saponin pathway or organism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe processes (regulation of complex assembly, spliceosomal splicing, tRNA methylation) that are mechanistically incompatible with a BAHD acyltransferase. Only D is a biosynthetic process involving secondary metabolite acylation, consistent with the enzyme class. No ambiguity among the choices.


### Important caveats

- The specific identification as 'saponin' biosynthesis (rather than another secondary metabolite pathway) relies on D being the only biosynthetic option among the four; the sequence alone cannot distinguish saponin biosynthesis from, say, flavonoid acylation. However, no such alternative is offered.
- The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support from PubMed:39043959 (Nat. Chem. Biol. 2025), not merely computational prediction.
- The UniProt entry was first public on 2025-06-18; the benchmark's exact data-construction date is unknown, though the sequence matches the historical entry version 5 (released 2026-01-28).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmarks of a BAHD acyltransferase (plant-specific acyl-CoA-dependent transferase family): the conserved 'HxxDG/DHDD' catalytic region (visible as 'DSDGDG' and 'FGFGTPIRVVPMDD' motifs), the characteristic C-terminal 'FLE' pattern, and overall length (~459 AA) typical of BAHD members. BAHD acyltransferases are well-known enzymes in plant secondary metabolite biosynthesis. Among the four choices, only D (saponin biosynthetic process) is a secondary-metabolite biosynthetic pathway. A (negative regulation of protein complex assembly) is a regulatory process unrelated to enzymatic acyl transfer; B (mRNA splicing via spliceosome) involves spliceosomal snRNP proteins with entirely different domain architectures; C (tRNA methylation) involves RNA methyltransferases, not acyl-CoA-dependent acyltransferases. Thus, recognizing the BAHD family and its general role in plant secondary metabolism is sufficient to eliminate A, B, and C and select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate (QA-triF(Q)RXX → saponarioside B) and the organism (Saponaria officinalis) are item-specific facts not derivable from sequence alone. However, these are not needed to distinguish D from the three clearly unrelated distractors.",
    "reason": "The distractors are mechanistically incompatible with an acyltransferase involved in secondary metabolism. General knowledge of the BAHD family's biochemical role and the nature of the other three GO terms provides a concrete biological argument for selecting D without needing to recall the specific saponin pathway or organism."
  },
  "case_id": "GO_biological_process_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt A0AAW1LG41 (BAHD1_SAPOF, 459 AA, sequence SHA256 matched). The UniProt entry carries GO:0016135 (saponin biosynthetic process) with IDA evidence (Inferred from Direct Assay, PubMed:39043959). The FUNCTION comment explicitly states the protein is 'Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway' and catalyzes acyl transfer to produce saponarioside B. The PATHWAY is listed as 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' This is experimentally supported annotation, not merely computational inference."
  },
  "important_caveats": [
    "The specific identification as 'saponin' biosynthesis (rather than another secondary metabolite pathway) relies on D being the only biosynthetic option among the four; the sequence alone cannot distinguish saponin biosynthesis from, say, flavonoid acylation. However, no such alternative is offered.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support from PubMed:39043959 (Nat. Chem. Biol. 2025), not merely computational prediction.",
    "The UniProt entry was first public on 2025-06-18; the benchmark's exact data-construction date is unknown, though the sequence matches the historical entry version 5 (released 2026-01-28)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe processes (regulation of complex assembly, spliceosomal splicing, tRNA methylation) that are mechanistically incompatible with a BAHD acyltransferase. Only D is a biosynthetic process involving secondary metabolite acylation, consistent with the enzyme class. No ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt A0AAW1LG41 (BAHD1_SAPOF, 459 AA, sequence SHA256 matched). The UniProt entry carries GO:0016135 (saponin biosynthetic process) with IDA evidence (Inferred from Direct Assay, PubMed:39043959). The FUNCTION comment explicitly states the protein is 'Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway' and catalyzes acyl transfer to produce saponarioside B. The PATHWAY is listed as 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' This is experimentally supported annotation, not merely computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmarks of a BAHD acyltransferase (plant-specific acyl-CoA-dependent transferase family): the conserved 'HxxDG/DHDD' catalytic region (visible as 'DSDGDG' and 'FGFGTPIRVVPMDD' motifs), the characteristic C-terminal 'FLE' pattern, and overall length (~459 AA) typical of BAHD members. BAHD acyltransferases are well-known enzymes in plant secondary metabolite biosynthesis. Among the four choices, only D (saponin biosynthetic process) is a secondary-metabolite biosynthetic pathway. A (negative regulation of protein complex assembly) is a regulatory process unrelated to enzymatic acyl transfer; B (mRNA splicing via spliceosome) involves spliceosomal snRNP proteins with entirely different domain architectures; C (tRNA methylation) involves RNA methyltransferases, not acyl-CoA-dependent acyltransferases. Thus, recognizing the BAHD family and its general role in plant secondary metabolism is sufficient to eliminate A, B, and C and select D.",
    "missing_item_specific_fact": "The specific substrate (QA-triF(Q)RXX → saponarioside B) and the organism (Saponaria officinalis) are item-specific facts not derivable from sequence alone. However, these are not needed to distinguish D from the three clearly unrelated distractors.",
    "reason": "The distractors are mechanistically incompatible with an acyltransferase involved in secondary metabolism. General knowledge of the BAHD family's biochemical role and the nature of the other three GO terms provides a concrete biological argument for selecting D without needing to recall the specific saponin pathway or organism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe processes (regulation of complex assembly, spliceosomal splicing, tRNA methylation) that are mechanistically incompatible with a BAHD acyltransferase. Only D is a biosynthetic process involving secondary metabolite acylation, consistent with the enzyme class. No ambiguity among the choices."
  },
  "important_caveats": [
    "The specific identification as 'saponin' biosynthesis (rather than another secondary metabolite pathway) relies on D being the only biosynthetic option among the four; the sequence alone cannot distinguish saponin biosynthesis from, say, flavonoid acylation. However, no such alternative is offered.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support from PubMed:39043959 (Nat. Chem. Biol. 2025), not merely computational prediction.",
    "The UniProt entry was first public on 2025-06-18; the benchmark's exact data-construction date is unknown, though the sequence matches the historical entry version 5 (released 2026-01-28)."
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

**Accession:** `A0AAW1LG41` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.588231+00:00.  

```json
"A0AAW1LG41"
```

Source SHA-256: `4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.588231+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"2.3.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"BAHD acyltransferase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoBAHD1"}]}}
```

Source SHA-256: `4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.588231+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). An acyltransferase that catalyzes the transfer of an acyl moiety to QA-triF(Q)RXX to produce saponarioside B (PubMed:39043959)"}]}
```

Source SHA-256: `4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.588231+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.588231+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0016135","properties":[{"key":"GoTerm","value":"P:saponin biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)  
**Locator:** `lines 34-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:42.902980+00:00.  

```text
CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.
CC       saponarioside A and saponarioside B) biosynthetic pathway, leading to
CC       the production of natural products with detergent properties used as
CC       traditional sources of soap (PubMed:39043959). An acyltransferase that
CC       catalyzes the transfer of an acyl moiety to QA-triF(Q)RXX to produce
CC       saponarioside B (PubMed:39043959). {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)  
**Locator:** `lines 49-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:42.902980+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)  
**Locator:** `lines 72-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:42.902980+00:00.  

```text
DR   GO; GO:0016135; P:saponin biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 52. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
