# GO_molecular_function_0091

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — protein serine/threonine kinase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MADKETLLKLREDFKMQNKSVFILGASGETGKVLLKEILGQNLFSKVTLIGRRKLTFEEEAYNNVNQEVVDFEKLDEYAPAFQGHDVGFCCLGTTRRKAGADGFVRVDRDYVLKSAELAKAGGCKHFNLLSSRGADKSSSFLYLQVKGEVEAKVEELKFDRLSVFRPGVLLCDRQESRPGEWLARKFFGSLPDSWASGYAVPVVTVVRAMLNNLVSPGSGQMELLENKAILHLGKDSDGPKL

[Multiple Choices]
A. methionine gamma-lyase activity
B. dolichyl-phosphate-mannose-protein mannosyltransferase activity
C. protein kinase activity
D. protein serine/threonine kinase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched rat UniProt record assigns GO:0004674, protein serine/threonine kinase activity, with evidence code ISO:RGD. This is an orthology-based annotation, not direct experimental evidence. The record's stated function instead emphasizes translation repression and does not independently demonstrate kinase activity.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a defensible basis for identifying serine/threonine protein kinase activity over the alternatives; the P-loop-like segment is not sufficient to establish that specific activity.


**Missing item-specific fact**

> A sequence-matched functional annotation or experimental evidence establishing this protein's kinase activity and substrate class is absent from the input.


**Reason**

> Selecting D depends on protein-specific annotation or evidence not supplied to the evaluated model; recognizing the sequence from a database would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Protein serine/threonine kinase activity (D) is a subtype of protein kinase activity (C), so both describe the annotated activity; the wording does not explicitly require the most specific GO term.


### Important caveats

- The UniProt kinase-function assignment is ISO:RGD, an inferred-by-orthology annotation, and should not be treated as experimental validation.
- The sequence matches the rat HTATIP2 record; the cited record's function description emphasizes translation repression and does not independently confirm kinase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a defensible basis for identifying serine/threonine protein kinase activity over the alternatives; the P-loop-like segment is not sufficient to establish that specific activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A sequence-matched functional annotation or experimental evidence establishing this protein's kinase activity and substrate class is absent from the input.",
    "reason": "Selecting D depends on protein-specific annotation or evidence not supplied to the evaluated model; recognizing the sequence from a database would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "GO_molecular_function_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched rat UniProt record assigns GO:0004674, protein serine/threonine kinase activity, with evidence code ISO:RGD. This is an orthology-based annotation, not direct experimental evidence. The record's stated function instead emphasizes translation repression and does not independently demonstrate kinase activity."
  },
  "important_caveats": [
    "The UniProt kinase-function assignment is ISO:RGD, an inferred-by-orthology annotation, and should not be treated as experimental validation.",
    "The sequence matches the rat HTATIP2 record; the cited record's function description emphasizes translation repression and does not independently confirm kinase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Protein serine/threonine kinase activity (D) is a subtype of protein kinase activity (C), so both describe the annotated activity; the wording does not explicitly require the most specific GO term."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched rat UniProt record assigns GO:0004674, protein serine/threonine kinase activity, with evidence code ISO:RGD. This is an orthology-based annotation, not direct experimental evidence. The record's stated function instead emphasizes translation repression and does not independently demonstrate kinase activity.",
    "evidence_ids": ["C6", "H4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a defensible basis for identifying serine/threonine protein kinase activity over the alternatives; the P-loop-like segment is not sufficient to establish that specific activity.",
    "missing_item_specific_fact": "A sequence-matched functional annotation or experimental evidence establishing this protein's kinase activity and substrate class is absent from the input.",
    "reason": "Selecting D depends on protein-specific annotation or evidence not supplied to the evaluated model; recognizing the sequence from a database would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Protein serine/threonine kinase activity (D) is a subtype of protein kinase activity (C), so both describe the annotated activity; the wording does not explicitly require the most specific GO term."
  },
  "important_caveats": [
    "The UniProt kinase-function assignment is ISO:RGD, an inferred-by-orthology annotation, and should not be treated as experimental validation.",
    "The sequence matches the rat HTATIP2 record; the cited record's function description emphasizes translation repression and does not independently confirm kinase activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B0BNF8 (Protein HTATIP2, rat) carries GO:0004674 (protein serine/threonine kinase activity) as an explicit annotation (evidence_id C6/H4). However, the evidence code is ISO:RGD (Inferred from Sequence/Residue Orthology from RGD), meaning the kinase annotation is transferred by orthology rather than directly experimentally validated. The FUNCTION comment (C5/H3) describes translation repression via eEF1A interaction and does not mention kinase activity. The annotation is present in the database and matches the expected answer, but its evidentiary basis is computational inference from an orthologous annotation in RGD, not a direct experimental measurement on this protein.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence (242 aa, TIP30/HTATIP2) lacks clear canonical protein-kinase motifs (no unambiguous VAIK, HRD, or DFG triad). A GxGxxG-like pattern (GASGETG) and a possible catalytic lysine are present, but these are weak and insufficient to confidently assign kinase activity, let alone distinguish serine/threonine specificity (D) from general protein kinase activity (C). The actual experimentally supported function (PubMed:31468715) is translation repression via eEF1A interaction, not kinase catalysis. The GO:0004674 annotation is ISO:RGD, i.e., inferred by orthology from RGD, not derived from sequence-visible motifs.


**Missing item-specific fact**

> The specific orthology-based annotation from RGD assigning GO:0004674 to this protein, and the rationale for choosing the child term (serine/threonine kinase) over the parent term (protein kinase activity). Without knowing this protein-specific database annotation, the sequence alone does not provide grounds to prefer D over C.


**Reason**

> Distinguishing option D (protein serine/threonine kinase activity) from option C (protein kinase activity) requires knowing the specific substrate specificity annotation for this protein. The sequence does not display canonical kinase motifs that would let a model infer serine/threonine specificity. The annotation is ISO:RGD (inferred from orthology), not experimentally determined. Recognizing the sequence as TIP30 and recalling its UniProt annotation is memorization, not reasoning from the sequence. Options A and B are reasonably eliminable as non-kinase/non-glycosyltransferase activities, but the C-vs-D distinction depends on an item-specific database annotation absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> GO:0004674 (D) is_a GO:0004672 (C) in the ontology hierarchy. If the protein has serine/threonine kinase activity, it also has protein kinase activity. The question asks for the 'primary' or 'best' molecular function, which could justify choosing the more specific term (D). However, since the kinase annotation itself is only inferred by orthology (ISO:RGD) and the experimentally supported function is translation repression, neither C nor D is strongly supported by direct evidence. A model could reasonably argue for C as the safer, more general term, or for D as the more specific annotated term. The sequence provides no clear basis to prefer one over the other.


### Important caveats

- The GO:0004674 annotation carries evidence code ISO:RGD (inferred from orthology from RGD), not experimental evidence (IDA, IMP, etc.). The FUNCTION comment for this protein does not mention kinase activity.
- The UniProt entry was only integrated into Swiss-Prot on 2025-06-18, making this a relatively recent annotation. The actual author data-construction snapshot is unknown.
- The protein's experimentally supported molecular function (PubMed:31468715) is repression of translational elongation via eEF1A interaction, which is not reflected in any of the four options.
- The sequence at 242 aa is at the lower boundary for a typical kinase domain (~250-300 aa), and no canonical kinase catalytic motifs are clearly identifiable, making the kinase assignment itself questionable from sequence alone.
- Options A (methionine gamma-lyase) and B (mannosyltransferase) are clearly eliminable as the sequence shows no lyase or glycosyltransferase signatures, but this does not help resolve C vs D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (242 aa, TIP30/HTATIP2) lacks clear canonical protein-kinase motifs (no unambiguous VAIK, HRD, or DFG triad). A GxGxxG-like pattern (GASGETG) and a possible catalytic lysine are present, but these are weak and insufficient to confidently assign kinase activity, let alone distinguish serine/threonine specificity (D) from general protein kinase activity (C). The actual experimentally supported function (PubMed:31468715) is translation repression via eEF1A interaction, not kinase catalysis. The GO:0004674 annotation is ISO:RGD, i.e., inferred by orthology from RGD, not derived from sequence-visible motifs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific orthology-based annotation from RGD assigning GO:0004674 to this protein, and the rationale for choosing the child term (serine/threonine kinase) over the parent term (protein kinase activity). Without knowing this protein-specific database annotation, the sequence alone does not provide grounds to prefer D over C.",
    "reason": "Distinguishing option D (protein serine/threonine kinase activity) from option C (protein kinase activity) requires knowing the specific substrate specificity annotation for this protein. The sequence does not display canonical kinase motifs that would let a model infer serine/threonine specificity. The annotation is ISO:RGD (inferred from orthology), not experimentally determined. Recognizing the sequence as TIP30 and recalling its UniProt annotation is memorization, not reasoning from the sequence. Options A and B are reasonably eliminable as non-kinase/non-glycosyltransferase activities, but the C-vs-D distinction depends on an item-specific database annotation absent from the input."
  },
  "case_id": "GO_molecular_function_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B0BNF8 (Protein HTATIP2, rat) carries GO:0004674 (protein serine/threonine kinase activity) as an explicit annotation (evidence_id C6/H4). However, the evidence code is ISO:RGD (Inferred from Sequence/Residue Orthology from RGD), meaning the kinase annotation is transferred by orthology rather than directly experimentally validated. The FUNCTION comment (C5/H3) describes translation repression via eEF1A interaction and does not mention kinase activity. The annotation is present in the database and matches the expected answer, but its evidentiary basis is computational inference from an orthologous annotation in RGD, not a direct experimental measurement on this protein."
  },
  "important_caveats": [
    "The GO:0004674 annotation carries evidence code ISO:RGD (inferred from orthology from RGD), not experimental evidence (IDA, IMP, etc.). The FUNCTION comment for this protein does not mention kinase activity.",
    "The UniProt entry was only integrated into Swiss-Prot on 2025-06-18, making this a relatively recent annotation. The actual author data-construction snapshot is unknown.",
    "The protein's experimentally supported molecular function (PubMed:31468715) is repression of translational elongation via eEF1A interaction, which is not reflected in any of the four options.",
    "The sequence at 242 aa is at the lower boundary for a typical kinase domain (~250-300 aa), and no canonical kinase catalytic motifs are clearly identifiable, making the kinase assignment itself questionable from sequence alone.",
    "Options A (methionine gamma-lyase) and B (mannosyltransferase) are clearly eliminable as the sequence shows no lyase or glycosyltransferase signatures, but this does not help resolve C vs D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "GO:0004674 (D) is_a GO:0004672 (C) in the ontology hierarchy. If the protein has serine/threonine kinase activity, it also has protein kinase activity. The question asks for the 'primary' or 'best' molecular function, which could justify choosing the more specific term (D). However, since the kinase annotation itself is only inferred by orthology (ISO:RGD) and the experimentally supported function is translation repression, neither C nor D is strongly supported by direct evidence. A model could reasonably argue for C as the safer, more general term, or for D as the more specific annotated term. The sequence provides no clear basis to prefer one over the other."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B0BNF8 (Protein HTATIP2, rat) carries GO:0004674 (protein serine/threonine kinase activity) as an explicit annotation (evidence_id C6/H4). However, the evidence code is ISO:RGD (Inferred from Sequence/Residue Orthology from RGD), meaning the kinase annotation is transferred by orthology rather than directly experimentally validated. The FUNCTION comment (C5/H3) describes translation repression via eEF1A interaction and does not mention kinase activity. The annotation is present in the database and matches the expected answer, but its evidentiary basis is computational inference from an orthologous annotation in RGD, not a direct experimental measurement on this protein.",
    "evidence_ids": ["C6", "H4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence (242 aa, TIP30/HTATIP2) lacks clear canonical protein-kinase motifs (no unambiguous VAIK, HRD, or DFG triad). A GxGxxG-like pattern (GASGETG) and a possible catalytic lysine are present, but these are weak and insufficient to confidently assign kinase activity, let alone distinguish serine/threonine specificity (D) from general protein kinase activity (C). The actual experimentally supported function (PubMed:31468715) is translation repression via eEF1A interaction, not kinase catalysis. The GO:0004674 annotation is ISO:RGD, i.e., inferred by orthology from RGD, not derived from sequence-visible motifs.",
    "missing_item_specific_fact": "The specific orthology-based annotation from RGD assigning GO:0004674 to this protein, and the rationale for choosing the child term (serine/threonine kinase) over the parent term (protein kinase activity). Without knowing this protein-specific database annotation, the sequence alone does not provide grounds to prefer D over C.",
    "reason": "Distinguishing option D (protein serine/threonine kinase activity) from option C (protein kinase activity) requires knowing the specific substrate specificity annotation for this protein. The sequence does not display canonical kinase motifs that would let a model infer serine/threonine specificity. The annotation is ISO:RGD (inferred from orthology), not experimentally determined. Recognizing the sequence as TIP30 and recalling its UniProt annotation is memorization, not reasoning from the sequence. Options A and B are reasonably eliminable as non-kinase/non-glycosyltransferase activities, but the C-vs-D distinction depends on an item-specific database annotation absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "GO:0004674 (D) is_a GO:0004672 (C) in the ontology hierarchy. If the protein has serine/threonine kinase activity, it also has protein kinase activity. The question asks for the 'primary' or 'best' molecular function, which could justify choosing the more specific term (D). However, since the kinase annotation itself is only inferred by orthology (ISO:RGD) and the experimentally supported function is translation repression, neither C nor D is strongly supported by direct evidence. A model could reasonably argue for C as the safer, more general term, or for D as the more specific annotated term. The sequence provides no clear basis to prefer one over the other."
  },
  "important_caveats": [
    "The GO:0004674 annotation carries evidence code ISO:RGD (inferred from orthology from RGD), not experimental evidence (IDA, IMP, etc.). The FUNCTION comment for this protein does not mention kinase activity.",
    "The UniProt entry was only integrated into Swiss-Prot on 2025-06-18, making this a relatively recent annotation. The actual author data-construction snapshot is unknown.",
    "The protein's experimentally supported molecular function (PubMed:31468715) is repression of translational elongation via eEF1A interaction, which is not reflected in any of the four options.",
    "The sequence at 242 aa is at the lower boundary for a typical kinase domain (~250-300 aa), and no canonical kinase catalytic motifs are clearly identifiable, making the kinase assignment itself questionable from sequence alone.",
    "Options A (methionine gamma-lyase) and B (mannosyltransferase) are clearly eliminable as the sequence shows no lyase or glycosyltransferase signatures, but this does not help resolve C vs D."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `ontology_parent_relation_traced_with_evidence_qualification`.

> The supplied ontology path has GO:0004674 is_a GO:0004672, so the serine/threonine-kinase term is nested under protein kinase. C6/H4 assign the specific term via ISO:RGD; C5/H3 instead describe translation repression.

**Remaining uncertainty:** The hierarchy establishes the relationship between terms, not experimental kinase activity of this protein. Orthology-based support and the functional-description qualification remain explicit.

Evidence checked: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3).

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

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:12.867856+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BUP3","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"31468715","source":"PubMed"}],"value":"Represses translation by preventing reactivation of elongation factor eEF1A (PubMed:31468715). May also inhibit nuclear import by competing with nuclear import substrates for binding to a subset of nuclear transport receptors (By similarity). Has additionally been proposed to act as a redox sensor involved in cellular oxidative stress surveillance (By similarity). May bind NADPH (By similarity)"}]}
```

Source SHA-256: `5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)  
**Locator:** `/uniProtKBCrossReferences/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:12.867856+00:00.  

```json
{"database":"GO","id":"GO:0004674","properties":[{"key":"GoTerm","value":"F:protein serine/threonine kinase activity"},{"key":"GoEvidenceType","value":"ISO:RGD"}]}
```

Source SHA-256: `5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)  
**Locator:** `lines 89-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:27:16.468432+00:00.  

```text
CC   -!- FUNCTION: Represses translation by preventing reactivation of
CC       elongation factor eEF1A (PubMed:31468715). May also inhibit nuclear
CC       import by competing with nuclear import substrates for binding to a
CC       subset of nuclear transport receptors (By similarity). Has additionally
CC       been proposed to act as a redox sensor involved in cellular oxidative
CC       stress surveillance (By similarity). May bind NADPH (By similarity).
CC       {ECO:0000250|UniProtKB:Q9BUP3, ECO:0000269|PubMed:31468715}.
```

Source SHA-256: `c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)  
**Locator:** `lines 131-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:27:16.468432+00:00.  

```text
DR   GO; GO:0004674; F:protein serine/threonine kinase activity; ISO:RGD.
```

Source SHA-256: `c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
