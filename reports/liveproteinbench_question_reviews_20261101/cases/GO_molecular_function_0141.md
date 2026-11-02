# GO_molecular_function_0141

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — heparan sulfate 2-sulfotransferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGLLRIMMPPKLQLLAVVAFAVAMLFLENQIQKLEESRAKLERAIARHEVREIEQRHTMDGPRQDAAVDEEEDIVIIYNRVPKTASTSFTNIAYDLCAKNRYHVLHINTTKNNPVMSLQDQVRFVKNITTWNEMKPGFYHGHISYLDFAKFGVKKKPIYINVIRDPIERLVSYYYFLRFGDDYRPGLRRRKQGDKKTFDECVAEGGSDCAPEKLWLQIPFFCGHSSECWNVGSRWAMDQAKYNLINEYFLVGVTEELEDFIMLLEAALPRFFRGATDLYRTGKKSHLRKTTEKKLPTKQTIAKLQQSDIWKMENEFYEFALEQFQFIRAHAVREKDGDLYILAQNFFYEKIYPKSN

[Multiple Choices]
A. nucleotide binding
B. RNA binding
C. heparan sulfate 2-sulfotransferase activity
D. nucleotidyltransferase activity
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

> The supplied sequence exactly matches the Chinese hamster HS2ST1 entry. That entry assigns heparan sulfate 2-sulfotransferase activity and describes transfer of a sulfo group to heparan sulfate. The annotation cites both similarity-based evidence and experimental literature; this supports choice C, though it does not establish that the cited experiment tested this exact hamster protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a membrane-associated protein, and a sulfotransferase-like sequence could suggest catalysis. But these features alone do not identify heparan sulfate as the substrate or the 2-O sulfation reaction.


**Missing item-specific fact**

> Identifying choice C requires the protein-specific HS2ST1 family/substrate assignment or equivalent annotation, which is not provided in the question.


**Reason**

> The sequence may support computational family recognition, but selecting this specific activity over the binding and transferase alternatives depends on item-specific functional knowledge; recognizing the sequence from an external database would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice A could describe a secondary nucleotide-binding activity, but the question asks for the primary function, for which the specific catalytic activity in C is the stronger description.


### Important caveats

- The reviewed annotation is sequence-matched to the supplied protein, but some functional support is transferred by similarity; the cited experimental evidence should not be assumed to come from this exact Chinese hamster protein.
- The entry also annotates PAPS binding, which is consistent with nucleotide binding but does not displace the more specific catalytic function as the primary answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a membrane-associated protein, and a sulfotransferase-like sequence could suggest catalysis. But these features alone do not identify heparan sulfate as the substrate or the 2-O sulfation reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying choice C requires the protein-specific HS2ST1 family/substrate assignment or equivalent annotation, which is not provided in the question.",
    "reason": "The sequence may support computational family recognition, but selecting this specific activity over the binding and transferase alternatives depends on item-specific functional knowledge; recognizing the sequence from an external database would be lookup, not reasoning from the supplied input."
  },
  "case_id": "GO_molecular_function_0141",
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
    "reason": "The supplied sequence exactly matches the Chinese hamster HS2ST1 entry. That entry assigns heparan sulfate 2-sulfotransferase activity and describes transfer of a sulfo group to heparan sulfate. The annotation cites both similarity-based evidence and experimental literature; this supports choice C, though it does not establish that the cited experiment tested this exact hamster protein."
  },
  "important_caveats": [
    "The reviewed annotation is sequence-matched to the supplied protein, but some functional support is transferred by similarity; the cited experimental evidence should not be assumed to come from this exact Chinese hamster protein.",
    "The entry also annotates PAPS binding, which is consistent with nucleotide binding but does not displace the more specific catalytic function as the primary answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A could describe a secondary nucleotide-binding activity, but the question asks for the primary function, for which the specific catalytic activity in C is the stronger description."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Chinese hamster HS2ST1 entry. That entry assigns heparan sulfate 2-sulfotransferase activity and describes transfer of a sulfo group to heparan sulfate. The annotation cites both similarity-based evidence and experimental literature; this supports choice C, though it does not establish that the cited experiment tested this exact hamster protein.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a membrane-associated protein, and a sulfotransferase-like sequence could suggest catalysis. But these features alone do not identify heparan sulfate as the substrate or the 2-O sulfation reaction.",
    "missing_item_specific_fact": "Identifying choice C requires the protein-specific HS2ST1 family/substrate assignment or equivalent annotation, which is not provided in the question.",
    "reason": "The sequence may support computational family recognition, but selecting this specific activity over the binding and transferase alternatives depends on item-specific functional knowledge; recognizing the sequence from an external database would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A could describe a secondary nucleotide-binding activity, but the question asks for the primary function, for which the specific catalytic activity in C is the stronger description."
  },
  "important_caveats": [
    "The reviewed annotation is sequence-matched to the supplied protein, but some functional support is transferred by similarity; the cited experimental evidence should not be assumed to come from this exact Chinese hamster protein.",
    "The entry also annotates PAPS binding, which is consistent with nucleotide binding but does not displace the more specific catalytic function as the primary answer."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A8C2LVE3 (sequence matched exactly) annotates this protein with GO:0004394 'heparan sulfate 2-sulfotransferase activity' under evidence code ECO:0000314 (direct assay, IDA:UniProtKB), supported by PubMed:17227754 (Xu et al., JBC 2007). The FUNCTION comment (H3/C5) describes catalysis of sulfo-group transfer from PAPS to the 2-OH of IdoA/GlcA in heparan sulfate, with experimental evidence (ECO:0000269). The protein is named 'Heparan sulfate 2-O-sulfotransferase 1' (EC 2.8.2.-). Option A (nucleotide binding) is technically also annotated via PAPS binding (GO:0050656, an is_a child of GO:0000166), but the question asks for the primary molecular function, which is the catalytic sulfotransferase activity. Options B (RNA binding) and D (nucleotidyltransferase, EC 2.7.7.-) are not supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A weak localization-based argument exists: the N-terminal signal peptide (MGLLRIMMPPKLQLLAVVAFAVAMLFLENQ...) suggests a secreted/Golgi protein, consistent with Golgi-resident sulfotransferases and inconsistent with typical cytoplasmic/nuclear RNA-binding proteins (B) or nucleotidyltransferases (D). However, this does not uniquely identify the protein as a heparan sulfate 2-sulfotransferase versus other sulfotransferases or other secreted enzymes. Recognizing the sulfotransferase superfamily fold from a raw 356-aa sequence without structural context or database comparison is not a straightforward general-biology inference.


**Missing item-specific fact**

> Identification of the sulfotransferase superfamily fold and, more critically, the specific substrate specificity (heparan sulfate, 2-O position) requires either database annotation lookup, recognition of the exact sequence from training data, or knowledge of the sulfotransferase structural motifs that are not obvious from the linear sequence alone. No provided context (organism, gene name, pathway) disambiguates the options.


**Reason**

> The sequence is a 356-aa protein with a signal peptide but no immediately recognizable, unique catalytic motifs that a general biologist could use to assign 'heparan sulfate 2-sulfotransferase activity' over 'nucleotide binding' or 'nucleotidyltransferase activity' without prior knowledge of this specific protein or the sulfotransferase fold. The correct answer depends on recognizing the protein's identity or its sulfotransferase classification, which is an item-specific annotation fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Option A (nucleotide binding, GO:0000166) is technically also an annotated molecular function of this protein via PAPS binding (GO:0050656, IDA evidence, which is_a GO:0000166). A model could argue that nucleotide binding is a valid molecular function. However, the question asks for the 'primary molecular function,' and the catalytic sulfotransferase activity (C) is the defining enzymatic function, making C the clearly superior answer. The ambiguity is minor and resolvable by the 'primary' qualifier.


### Important caveats

- The UniProt annotation for GO:0004394 carries IDA (Inferred from Direct Assay) evidence linked to PubMed:17227754, indicating experimental support, though the protein description name itself is transferred by similarity (ECO:0000250|UniProtKB:Q7LGA3).
- The sequence match is exact (SHA256 match) between the benchmark input and UniProt A0A8C2LVE3, so the annotation applies to the supplied sequence.
- The protein is from Cricetulus griseus (Chinese hamster), not human; the human ortholog is HS2ST1 (Q8R3H7). The functional annotation is conserved.
- PAPS binding (GO:0050656) is annotated with IDA evidence and is an is_a descendant of nucleotide binding (GO:0000166), so option A is not strictly false but is a secondary/substrate-binding annotation rather than the primary catalytic function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A weak localization-based argument exists: the N-terminal signal peptide (MGLLRIMMPPKLQLLAVVAFAVAMLFLENQ...) suggests a secreted/Golgi protein, consistent with Golgi-resident sulfotransferases and inconsistent with typical cytoplasmic/nuclear RNA-binding proteins (B) or nucleotidyltransferases (D). However, this does not uniquely identify the protein as a heparan sulfate 2-sulfotransferase versus other sulfotransferases or other secreted enzymes. Recognizing the sulfotransferase superfamily fold from a raw 356-aa sequence without structural context or database comparison is not a straightforward general-biology inference.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identification of the sulfotransferase superfamily fold and, more critically, the specific substrate specificity (heparan sulfate, 2-O position) requires either database annotation lookup, recognition of the exact sequence from training data, or knowledge of the sulfotransferase structural motifs that are not obvious from the linear sequence alone. No provided context (organism, gene name, pathway) disambiguates the options.",
    "reason": "The sequence is a 356-aa protein with a signal peptide but no immediately recognizable, unique catalytic motifs that a general biologist could use to assign 'heparan sulfate 2-sulfotransferase activity' over 'nucleotide binding' or 'nucleotidyltransferase activity' without prior knowledge of this specific protein or the sulfotransferase fold. The correct answer depends on recognizing the protein's identity or its sulfotransferase classification, which is an item-specific annotation fact."
  },
  "case_id": "GO_molecular_function_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H3",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A8C2LVE3 (sequence matched exactly) annotates this protein with GO:0004394 'heparan sulfate 2-sulfotransferase activity' under evidence code ECO:0000314 (direct assay, IDA:UniProtKB), supported by PubMed:17227754 (Xu et al., JBC 2007). The FUNCTION comment (H3/C5) describes catalysis of sulfo-group transfer from PAPS to the 2-OH of IdoA/GlcA in heparan sulfate, with experimental evidence (ECO:0000269). The protein is named 'Heparan sulfate 2-O-sulfotransferase 1' (EC 2.8.2.-). Option A (nucleotide binding) is technically also annotated via PAPS binding (GO:0050656, an is_a child of GO:0000166), but the question asks for the primary molecular function, which is the catalytic sulfotransferase activity. Options B (RNA binding) and D (nucleotidyltransferase, EC 2.7.7.-) are not supported."
  },
  "important_caveats": [
    "The UniProt annotation for GO:0004394 carries IDA (Inferred from Direct Assay) evidence linked to PubMed:17227754, indicating experimental support, though the protein description name itself is transferred by similarity (ECO:0000250|UniProtKB:Q7LGA3).",
    "The sequence match is exact (SHA256 match) between the benchmark input and UniProt A0A8C2LVE3, so the annotation applies to the supplied sequence.",
    "The protein is from Cricetulus griseus (Chinese hamster), not human; the human ortholog is HS2ST1 (Q8R3H7). The functional annotation is conserved.",
    "PAPS binding (GO:0050656) is annotated with IDA evidence and is an is_a descendant of nucleotide binding (GO:0000166), so option A is not strictly false but is a secondary/substrate-binding annotation rather than the primary catalytic function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Option A (nucleotide binding, GO:0000166) is technically also an annotated molecular function of this protein via PAPS binding (GO:0050656, IDA evidence, which is_a GO:0000166). A model could argue that nucleotide binding is a valid molecular function. However, the question asks for the 'primary molecular function,' and the catalytic sulfotransferase activity (C) is the defining enzymatic function, making C the clearly superior answer. The ambiguity is minor and resolvable by the 'primary' qualifier."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A8C2LVE3 (sequence matched exactly) annotates this protein with GO:0004394 'heparan sulfate 2-sulfotransferase activity' under evidence code ECO:0000314 (direct assay, IDA:UniProtKB), supported by PubMed:17227754 (Xu et al., JBC 2007). The FUNCTION comment (H3/C5) describes catalysis of sulfo-group transfer from PAPS to the 2-OH of IdoA/GlcA in heparan sulfate, with experimental evidence (ECO:0000269). The protein is named 'Heparan sulfate 2-O-sulfotransferase 1' (EC 2.8.2.-). Option A (nucleotide binding) is technically also annotated via PAPS binding (GO:0050656, an is_a child of GO:0000166), but the question asks for the primary molecular function, which is the catalytic sulfotransferase activity. Options B (RNA binding) and D (nucleotidyltransferase, EC 2.7.7.-) are not supported.",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H3", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A weak localization-based argument exists: the N-terminal signal peptide (MGLLRIMMPPKLQLLAVVAFAVAMLFLENQ...) suggests a secreted/Golgi protein, consistent with Golgi-resident sulfotransferases and inconsistent with typical cytoplasmic/nuclear RNA-binding proteins (B) or nucleotidyltransferases (D). However, this does not uniquely identify the protein as a heparan sulfate 2-sulfotransferase versus other sulfotransferases or other secreted enzymes. Recognizing the sulfotransferase superfamily fold from a raw 356-aa sequence without structural context or database comparison is not a straightforward general-biology inference.",
    "missing_item_specific_fact": "Identification of the sulfotransferase superfamily fold and, more critically, the specific substrate specificity (heparan sulfate, 2-O position) requires either database annotation lookup, recognition of the exact sequence from training data, or knowledge of the sulfotransferase structural motifs that are not obvious from the linear sequence alone. No provided context (organism, gene name, pathway) disambiguates the options.",
    "reason": "The sequence is a 356-aa protein with a signal peptide but no immediately recognizable, unique catalytic motifs that a general biologist could use to assign 'heparan sulfate 2-sulfotransferase activity' over 'nucleotide binding' or 'nucleotidyltransferase activity' without prior knowledge of this specific protein or the sulfotransferase fold. The correct answer depends on recognizing the protein's identity or its sulfotransferase classification, which is an item-specific annotation fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Option A (nucleotide binding, GO:0000166) is technically also an annotated molecular function of this protein via PAPS binding (GO:0050656, IDA evidence, which is_a GO:0000166). A model could argue that nucleotide binding is a valid molecular function. However, the question asks for the 'primary molecular function,' and the catalytic sulfotransferase activity (C) is the defining enzymatic function, making C the clearly superior answer. The ambiguity is minor and resolvable by the 'primary' qualifier."
  },
  "important_caveats": [
    "The UniProt annotation for GO:0004394 carries IDA (Inferred from Direct Assay) evidence linked to PubMed:17227754, indicating experimental support, though the protein description name itself is transferred by similarity (ECO:0000250|UniProtKB:Q7LGA3).",
    "The sequence match is exact (SHA256 match) between the benchmark input and UniProt A0A8C2LVE3, so the annotation applies to the supplied sequence.",
    "The protein is from Cricetulus griseus (Chinese hamster), not human; the human ortholog is HS2ST1 (Q8R3H7). The functional annotation is conserved.",
    "PAPS binding (GO:0050656) is annotated with IDA evidence and is an is_a descendant of nucleotide binding (GO:0000166), so option A is not strictly false but is a secondary/substrate-binding annotation rather than the primary catalytic function."
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

**Accession:** `A0A8C2LVE3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:56.866768+00:00.  

```json
"A0A8C2LVE3"
```

Source SHA-256: `0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:56.866768+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"2-O-sulfotransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"2-OST"},{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q76KB1","source":"UniProtKB"}],"value":"2OST"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"HS 2-O-sulfotransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"Heparan sulfate 2-sulfotransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"}],"value":"2.8.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q7LGA3","source":"UniProtKB"}],"value":"Heparan sulfate 2-O-sulfotransferase 1"}}}
```

Source SHA-256: `0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:56.866768+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8R3H7","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"17227754","source":"PubMed"}],"value":"Catalyzes the transfer of a sulfo group from 3'-phospho-5'-adenylyl sulfate (PAPS) to the 2-OH position of iduronic acid (IdoA) or glucuronic acid (GlcA) within the heparan sulfate (HS) chain and participates in HS biosynthesis (PubMed:17227754). Required for metanephric development of kidney formation, suggesting that 2-O-sulfation within HS is essential for signaling between ureteric bud and metanephric mesenchyme (By similarity)"}]}
```

Source SHA-256: `0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:56.866768+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"17227754","source":"PubMed"}],"id":"GO:0004394","properties":[{"key":"GoTerm","value":"F:heparan sulfate 2-sulfotransferase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.260576+00:00.  

```text
ID   HS2ST_CRIGR             Reviewed;         356 AA.
AC   A0A8C2LVE3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-JAN-2022, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=Heparan sulfate 2-O-sulfotransferase 1 {ECO:0000250|UniProtKB:Q7LGA3};
DE            EC=2.8.2.- {ECO:0000250|UniProtKB:Q8R3H7};
DE   AltName: Full=2-O-sulfotransferase {ECO:0000250|UniProtKB:Q8R3H7};
DE            Short=2-OST {ECO:0000250|UniProtKB:Q8R3H7};
DE            Short=2OST {ECO:0000250|UniProtKB:Q76KB1};
DE   AltName: Full=HS 2-O-sulfotransferase {ECO:0000250|UniProtKB:Q8R3H7};
DE   AltName: Full=Heparan sulfate 2-sulfotransferase {ECO:0000250|UniProtKB:Q8R3H7};
GN   Name=HS2ST1 {ECO:0000250|UniProtKB:Q7LGA3}; Synonyms=LOC100760748;
OS   Cricetulus griseus (Chinese hamster) (Cricetulus barabensis griseus).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea;
OC   Cricetidae; Cricetinae; Cricetulus.
OX   NCBI_TaxID=10029 {ECO:0000312|Proteomes:UP001108280};
```

Source SHA-256: `c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)  
**Locator:** `lines 45-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.260576+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the transfer of a sulfo group from 3'-phospho-5'-
CC       adenylyl sulfate (PAPS) to the 2-OH position of iduronic acid (IdoA) or
CC       glucuronic acid (GlcA) within the heparan sulfate (HS) chain and
CC       participates in HS biosynthesis (PubMed:17227754). Required for
CC       metanephric development of kidney formation, suggesting that 2-O-
CC       sulfation within HS is essential for signaling between ureteric bud and
CC       metanephric mesenchyme (By similarity). {ECO:0000250|UniProtKB:Q8R3H7,
CC       ECO:0000269|PubMed:17227754}.
```

Source SHA-256: `c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)  
**Locator:** `lines 75-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.260576+00:00.  

```text
DR   GO; GO:0004394; F:heparan sulfate 2-sulfotransferase activity; IDA:UniProtKB.
```

Source SHA-256: `c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 41261-41273`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004394
name: heparan sulfate 2-sulfotransferase activity
namespace: molecular_function
def: "Catalysis of the reaction: 3'-phosphoadenosine 5'-phosphosulfate + heparan sulfate = adenosine 3',5'-bisphosphate + heparan sulfate 2-O-sulfate; results in 2-O-sulfation of iduronic acid residues in heparan sulfate." [PMID:9153262]
synonym: "heparan sulfate 2-O-sulfotransferase activity" EXACT []
synonym: "heparan-sulfate 2-O-sulphotransferase activity" EXACT []
synonym: "heparin 2-sulfotransferase activity" RELATED []
synonym: "heparin-sulphate 2-sulphotransferase activity" RELATED []
xref: MetaCyc:RXN-11558
xref: Reactome:R-HSA-2076508 "HS2ST1 trimer sulfates IdoA at C2 in heparan sulfate"
is_a: GO:0034483 ! heparan sulfate sulfotransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
