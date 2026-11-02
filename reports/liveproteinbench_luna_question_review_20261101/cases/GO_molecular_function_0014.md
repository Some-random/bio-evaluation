# GO_molecular_function_0014

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — isomerase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MIRILYLLVKPESMSHEQFRKECVVHFQMSAGMPGLHKYEVRLVAGNPTDTHVPYLDVGRIDAIGECWFASEEQYQVYMESDIRKAWFEHGKYFIGQLKPFVTEELV

[Multiple Choices]
A. sequence-specific DNA binding
B. DNA nuclease activity
C. serine-type endopeptidase activity
D. isomerase activity
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

## Luna’s full visible review

### Expected-answer support: supported

> The exact sequence matches the annotated 4-carboxymethyl-4-methylbutenolide mutase. Its experimentally supported reaction is an isomerization, so the broader choice D, isomerase activity, is supported.

Cited evidence: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a small protein, but its length or general composition does not meaningfully distinguish isomerase activity from the listed DNA-binding or nuclease activities.

**Missing item-specific fact**

> The protein-specific identity or functional annotation linking this sequence to 4-carboxymethyl-4-methylbutenolide mutase activity.

**Reason**

> Choosing D depends on recognizing the sequence through homology or an external annotation; the supplied sequence and choices alone provide no concrete general biological argument that establishes this particular function.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The experimental reaction supports isomerase activity, and none of the other choices is supported by the supplied evidence.

### Important caveats

- The reviewer-only evidence identifies a sequence-matched UniProt record and cites experimental evidence codes and publications; those annotations were not supplied to the evaluated model.
- The cited primary papers were not independently retrieved and comprehensively validated here.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated 4-carboxymethyl-4-methylbutenolide mutase. Its experimentally supported reaction is an isomerization, so the broader choice D, isomerase activity, is supported.",
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a small protein, but its length or general composition does not meaningfully distinguish isomerase activity from the listed DNA-binding or nuclease activities.",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation linking this sequence to 4-carboxymethyl-4-methylbutenolide mutase activity.",
    "reason": "Choosing D depends on recognizing the sequence through homology or an external annotation; the supplied sequence and choices alone provide no concrete general biological argument that establishes this particular function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental reaction supports isomerase activity, and none of the other choices is supported by the supplied evidence."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched UniProt record and cites experimental evidence codes and publications; those annotations were not supplied to the evaluated model.",
    "The cited primary papers were not independently retrieved and comprehensively validated here."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `C5MR76`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 66. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"20061479","source":"PubMed"}],"value":"Isomerase involved in the degradation of 4-methylsalicylate and 5-methylsalicylate (PubMed:20061479). Catalyzes the isomerization of the dead-end metabolite 4-methylmuconolactone (4-ML) to 3-methylmuconolactone (3-ML), which can then be further degraded through a modified 3-oxoadipate pathway (PubMed:19801657). Can also use 1-methylbislactone but not 3-methyl-cis,cis-muconate (PubMed:19801657)"}]}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"19801657","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19238"}}],"reaction":{"ecNumber":"5.4.99.14","evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"}],"name":"4-methylmuconolactone = 3-methylmuconolactone","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19237"},{"database":"ChEBI","id":"CHEBI:57883"},{"database":"ChEBI","id":"CHEBI:57888"}]}}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"}],"id":"GO:0047469","properties":[{"key":"GoTerm","value":"F:4-carboxymethyl-4-methylbutenolide mutase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 56-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
CC   -!- FUNCTION: Isomerase involved in the degradation of 4-methylsalicylate
CC       and 5-methylsalicylate (PubMed:20061479). Catalyzes the isomerization
CC       of the dead-end metabolite 4-methylmuconolactone (4-ML) to 3-
CC       methylmuconolactone (3-ML), which can then be further degraded through
CC       a modified 3-oxoadipate pathway (PubMed:19801657). Can also use 1-
CC       methylbislactone but not 3-methyl-cis,cis-muconate (PubMed:19801657).
CC       {ECO:0000269|PubMed:19801657, ECO:0000269|PubMed:20061479}.
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 63-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-methylmuconolactone = 3-methylmuconolactone;
CC         Xref=Rhea:RHEA:19237, ChEBI:CHEBI:57883, ChEBI:CHEBI:57888;
CC         EC=5.4.99.14; Evidence={ECO:0000269|PubMed:19801657};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19238;
CC         Evidence={ECO:0000305|PubMed:19801657};
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 14). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
