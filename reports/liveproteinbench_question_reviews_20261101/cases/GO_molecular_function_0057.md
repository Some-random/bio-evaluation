# GO_molecular_function_0057

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — ATP binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPARKYKIHVPCTSANIGPGFDVCGIALSLSLSLVVTIPSVSSGAEPLPKIIYTGLDSDNVPLSPYKNLLTRVALYVLRANGITTFPPGVTIEARNEIPFGRGLGSSGAAVIAGVLLGDLLGNLSLPKSRLLDFALMVERHPDNVTAALMGGFVGSYLRELSPEDMSAASIPLAEVLPEYPPDAGPDWGKSPPQPPHGIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARSPPDPDLIYDAMGDRVHQPYRMTLIPGLPKILSTLTPTSHPGLLGICLSGAGPTILALATHNFEAIANEIERIFGDEQVLVDHKVLNIDEKGSWVEDITEA

[Multiple Choices]
A. N-acetylglucosamine-6-sulfatase activity
B. medium-chain fatty acyl-CoA dehydrogenase activity
C. ATP binding
D. nicotinamide phosphoribosyltransferase activity
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

> The exact-matched sequence is annotated with ATP binding (GO:0005524), though the cited ATP-binding annotation is computational. Its homoserine kinase function is supported by cited experimental evidence, and the associated reaction uses ATP, supporting ATP binding mechanistically.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> An ATP-dependent kinase would bind ATP, but the supplied sequence does not state its function or provide a clear, distinctive motif that establishes this protein as such; recognizing the relevant protein family would require protein-specific functional knowledge.


**Missing item-specific fact**

> That this sequence encodes homoserine kinase, whose reaction uses ATP.


**Reason**

> The reviewer evidence supports the key, but that evidence was not supplied to the evaluated model. Identifying the protein or its ATP-dependent reaction from this sequence requires item-specific functional identification, not simply the broad fact that many proteins bind ATP.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Of the listed choices, ATP binding is supported by the protein's ATP-dependent kinase function; the other options describe unrelated specific activities.


### Important caveats

- The ATP-binding GO annotation is computationally inferred, not presented as direct experimental evidence of binding.
- The source record identifies this protein as homoserine kinase, a function not included among the options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "An ATP-dependent kinase would bind ATP, but the supplied sequence does not state its function or provide a clear, distinctive motif that establishes this protein as such; recognizing the relevant protein family would require protein-specific functional knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence encodes homoserine kinase, whose reaction uses ATP.",
    "reason": "The reviewer evidence supports the key, but that evidence was not supplied to the evaluated model. Identifying the protein or its ATP-dependent reaction from this sequence requires item-specific functional identification, not simply the broad fact that many proteins bind ATP."
  },
  "case_id": "GO_molecular_function_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated with ATP binding (GO:0005524), though the cited ATP-binding annotation is computational. Its homoserine kinase function is supported by cited experimental evidence, and the associated reaction uses ATP, supporting ATP binding mechanistically."
  },
  "important_caveats": [
    "The ATP-binding GO annotation is computationally inferred, not presented as direct experimental evidence of binding.",
    "The source record identifies this protein as homoserine kinase, a function not included among the options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Of the listed choices, ATP binding is supported by the protein's ATP-dependent kinase function; the other options describe unrelated specific activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated with ATP binding (GO:0005524), though the cited ATP-binding annotation is computational. Its homoserine kinase function is supported by cited experimental evidence, and the associated reaction uses ATP, supporting ATP binding mechanistically.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "An ATP-dependent kinase would bind ATP, but the supplied sequence does not state its function or provide a clear, distinctive motif that establishes this protein as such; recognizing the relevant protein family would require protein-specific functional knowledge.",
    "missing_item_specific_fact": "That this sequence encodes homoserine kinase, whose reaction uses ATP.",
    "reason": "The reviewer evidence supports the key, but that evidence was not supplied to the evaluated model. Identifying the protein or its ATP-dependent reaction from this sequence requires item-specific functional identification, not simply the broad fact that many proteins bind ATP."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Of the listed choices, ATP binding is supported by the protein's ATP-dependent kinase function; the other options describe unrelated specific activities."
  },
  "important_caveats": [
    "The ATP-binding GO annotation is computationally inferred, not presented as direct experimental evidence of binding.",
    "The source record identifies this protein as homoserine kinase, a function not included among the options."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9VU26 (Homoserine kinase, EC 2.7.1.39) carries GO:0005524 (ATP binding) annotated with IEA:InterPro and IEA:UniProtKB-KW evidence codes (C7, H5). The protein's catalytic reaction (L-homoserine + ATP → O-phospho-L-homoserine + ADP + H⁺) requires ATP binding. Although the primary function annotation is GO:0004413 (homoserine kinase activity, IGI evidence, C8/H6), that term is not among the choices. Among the four options, only 'ATP binding' is annotated to this protein. The other three options (sulfatase, dehydrogenase, phosphoribosyltransferase) have no annotation support for this entry. The answer is supported, albeit via a secondary IEA annotation rather than the primary IGI-annotated kinase activity.

Citations as saved: [C7](#evidence-c7), [C8](#evidence-c8), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs consistent with the GHMP kinase superfamily (e.g., the 'GAGPTILAL' glycine-rich P-loop-like region and the 'GIGHF' motif), which are hallmarks of nucleotide-dependent phosphate-transfer enzymes. A kinase by definition binds ATP to donate a phosphoryl group. Among the four choices: (A) N-acetylglucosamine-6-sulfatase is a hydrolase cleaving sulfate esters—no ATP involvement; (B) medium-chain fatty acyl-CoA dehydrogenase is an FAD-dependent oxidoreductase—no ATP; (D) nicotinamide phosphoribosyltransferase uses PRPP/PPi, not ATP, as its ribosyl donor. Only option C (ATP binding) is mechanistically compatible with a kinase. Thus, recognizing kinase-like sequence features and understanding the substrate requirements of each enzyme class allows elimination of A, B, and D.


**Missing item-specific fact**

> None critical. The reasoning requires knowledge of GHMP kinase family motifs and the substrate specificities of the four enzyme classes, which is general enzymology/biochemistry knowledge rather than a protein-specific database lookup.


**Reason**

> A model with knowledge of kinase family motifs and the mechanistic distinctions among hydrolases, oxidoreductases, phosphoribosyltransferases, and kinases can reason from the sequence to 'ATP binding' without needing to recall the specific UniProt entry. The distractors are mechanistically incompatible with a nucleotide-dependent phosphotransferase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the question asks for 'primary molecular function' and the true primary annotation (homoserine kinase activity, GO:0004413) is absent from the choices, only one option (C, ATP binding) is annotated to this protein. Options A, B, and D describe entirely different enzyme classes with no annotation or mechanistic support for this sequence. The wording is slightly imprecise (calling a secondary IEA annotation the 'primary' function), but this does not create ambiguity among the four provided choices.


### Important caveats

- The GO:0005524 (ATP binding) annotation is IEA (Inferred from Electronic Annotation), not experimental. The primary experimentally supported function is homoserine kinase activity (GO:0004413, IGI evidence from PubMed:18757810).
- The question asks for 'primary molecular function' but the correct answer among the choices is a secondary, computationally inferred annotation. The true primary function term is not offered.
- The sequence-to-GHMP-kinase identification, while supported by recognizable motifs, still benefits from family-level training data; a purely de novo motif analysis of a 357-aa sequence is non-trivial.
- The UniProt entry was first publicly released 2025-02-05 (entry version 51 archived), which may postdate the benchmark construction date; the author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs consistent with the GHMP kinase superfamily (e.g., the 'GAGPTILAL' glycine-rich P-loop-like region and the 'GIGHF' motif), which are hallmarks of nucleotide-dependent phosphate-transfer enzymes. A kinase by definition binds ATP to donate a phosphoryl group. Among the four choices: (A) N-acetylglucosamine-6-sulfatase is a hydrolase cleaving sulfate esters—no ATP involvement; (B) medium-chain fatty acyl-CoA dehydrogenase is an FAD-dependent oxidoreductase—no ATP; (D) nicotinamide phosphoribosyltransferase uses PRPP/PPi, not ATP, as its ribosyl donor. Only option C (ATP binding) is mechanistically compatible with a kinase. Thus, recognizing kinase-like sequence features and understanding the substrate requirements of each enzyme class allows elimination of A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The reasoning requires knowledge of GHMP kinase family motifs and the substrate specificities of the four enzyme classes, which is general enzymology/biochemistry knowledge rather than a protein-specific database lookup.",
    "reason": "A model with knowledge of kinase family motifs and the mechanistic distinctions among hydrolases, oxidoreductases, phosphoribosyltransferases, and kinases can reason from the sequence to 'ATP binding' without needing to recall the specific UniProt entry. The distractors are mechanistically incompatible with a nucleotide-dependent phosphotransferase."
  },
  "case_id": "GO_molecular_function_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C8",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry J9VU26 (Homoserine kinase, EC 2.7.1.39) carries GO:0005524 (ATP binding) annotated with IEA:InterPro and IEA:UniProtKB-KW evidence codes (C7, H5). The protein's catalytic reaction (L-homoserine + ATP → O-phospho-L-homoserine + ADP + H⁺) requires ATP binding. Although the primary function annotation is GO:0004413 (homoserine kinase activity, IGI evidence, C8/H6), that term is not among the choices. Among the four options, only 'ATP binding' is annotated to this protein. The other three options (sulfatase, dehydrogenase, phosphoribosyltransferase) have no annotation support for this entry. The answer is supported, albeit via a secondary IEA annotation rather than the primary IGI-annotated kinase activity."
  },
  "important_caveats": [
    "The GO:0005524 (ATP binding) annotation is IEA (Inferred from Electronic Annotation), not experimental. The primary experimentally supported function is homoserine kinase activity (GO:0004413, IGI evidence from PubMed:18757810).",
    "The question asks for 'primary molecular function' but the correct answer among the choices is a secondary, computationally inferred annotation. The true primary function term is not offered.",
    "The sequence-to-GHMP-kinase identification, while supported by recognizable motifs, still benefits from family-level training data; a purely de novo motif analysis of a 357-aa sequence is non-trivial.",
    "The UniProt entry was first publicly released 2025-02-05 (entry version 51 archived), which may postdate the benchmark construction date; the author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary annotation (homoserine kinase activity, GO:0004413) is absent from the choices, only one option (C, ATP binding) is annotated to this protein. Options A, B, and D describe entirely different enzyme classes with no annotation or mechanistic support for this sequence. The wording is slightly imprecise (calling a secondary IEA annotation the 'primary' function), but this does not create ambiguity among the four provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9VU26 (Homoserine kinase, EC 2.7.1.39) carries GO:0005524 (ATP binding) annotated with IEA:InterPro and IEA:UniProtKB-KW evidence codes (C7, H5). The protein's catalytic reaction (L-homoserine + ATP → O-phospho-L-homoserine + ADP + H⁺) requires ATP binding. Although the primary function annotation is GO:0004413 (homoserine kinase activity, IGI evidence, C8/H6), that term is not among the choices. Among the four options, only 'ATP binding' is annotated to this protein. The other three options (sulfatase, dehydrogenase, phosphoribosyltransferase) have no annotation support for this entry. The answer is supported, albeit via a secondary IEA annotation rather than the primary IGI-annotated kinase activity.",
    "evidence_ids": ["C7", "C8", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs consistent with the GHMP kinase superfamily (e.g., the 'GAGPTILAL' glycine-rich P-loop-like region and the 'GIGHF' motif), which are hallmarks of nucleotide-dependent phosphate-transfer enzymes. A kinase by definition binds ATP to donate a phosphoryl group. Among the four choices: (A) N-acetylglucosamine-6-sulfatase is a hydrolase cleaving sulfate esters—no ATP involvement; (B) medium-chain fatty acyl-CoA dehydrogenase is an FAD-dependent oxidoreductase—no ATP; (D) nicotinamide phosphoribosyltransferase uses PRPP/PPi, not ATP, as its ribosyl donor. Only option C (ATP binding) is mechanistically compatible with a kinase. Thus, recognizing kinase-like sequence features and understanding the substrate requirements of each enzyme class allows elimination of A, B, and D.",
    "missing_item_specific_fact": "None critical. The reasoning requires knowledge of GHMP kinase family motifs and the substrate specificities of the four enzyme classes, which is general enzymology/biochemistry knowledge rather than a protein-specific database lookup.",
    "reason": "A model with knowledge of kinase family motifs and the mechanistic distinctions among hydrolases, oxidoreductases, phosphoribosyltransferases, and kinases can reason from the sequence to 'ATP binding' without needing to recall the specific UniProt entry. The distractors are mechanistically incompatible with a nucleotide-dependent phosphotransferase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary annotation (homoserine kinase activity, GO:0004413) is absent from the choices, only one option (C, ATP binding) is annotated to this protein. Options A, B, and D describe entirely different enzyme classes with no annotation or mechanistic support for this sequence. The wording is slightly imprecise (calling a secondary IEA annotation the 'primary' function), but this does not create ambiguity among the four provided choices."
  },
  "important_caveats": [
    "The GO:0005524 (ATP binding) annotation is IEA (Inferred from Electronic Annotation), not experimental. The primary experimentally supported function is homoserine kinase activity (GO:0004413, IGI evidence from PubMed:18757810).",
    "The question asks for 'primary molecular function' but the correct answer among the choices is a secondary, computationally inferred annotation. The true primary function term is not offered.",
    "The sequence-to-GHMP-kinase identification, while supported by recognizable motifs, still benefits from family-level training data; a purely de novo motif analysis of a 357-aa sequence is non-trivial.",
    "The UniProt entry was first publicly released 2025-02-05 (entry version 51 archived), which may postdate the benchmark construction date; the author's source snapshot is unknown."
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

**Accession:** `J9VU26` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
"J9VU26"
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18757810","source":"PubMed"}],"value":"Commits homoserine to the threonine biosynthesis pathway by catalyzing its O-phosphorylation"}]}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P17423","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13986"}}],"reaction":{"ecNumber":"2.7.1.39","evidences":[{"evidenceCode":"ECO:0000250","id":"P17423","source":"UniProtKB"}],"name":"L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13985"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57476"},{"database":"ChEBI","id":"CHEBI:57590"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"database":"GO","id":"GO:0005524","properties":[{"key":"GoTerm","value":"F:ATP binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000316","id":"18757810","source":"PubMed"}],"id":"GO:0004413","properties":[{"key":"GoTerm","value":"F:homoserine kinase activity"},{"key":"GoEvidenceType","value":"IGI:UniProtKB"}]}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 43-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
CC   -!- FUNCTION: Commits homoserine to the threonine biosynthesis pathway by
CC       catalyzing its O-phosphorylation. {ECO:0000269|PubMed:18757810}.
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 45-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+);
CC         Xref=Rhea:RHEA:13985, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57476, ChEBI:CHEBI:57590, ChEBI:CHEBI:456216;
CC         EC=2.7.1.39; Evidence={ECO:0000250|UniProtKB:P17423};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13986;
CC         Evidence={ECO:0000250|UniProtKB:P17423};
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 76-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW.
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
DR   GO; GO:0004413; F:homoserine kinase activity; IGI:UniProtKB.
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
