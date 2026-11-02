# GO_biological_process_0007

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — amino acid biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSYGESHGKAIGCVIDGFLSNIEINFDLIQKQLDRRRPNQSKLTSNRNEKDKLVILSGFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQVSKELENKNPPSRDLVDSYGTVRYNEKEKIFMDCFNRIYDMNASMLKTDEYNKNTLTIPSIDNTYINVKTNECNINQVDNNHNNYINDKDNTFNNSEKSDEWIYLQTRCPHPYTAVQICSYILKLKNKGDSVGGIATCIIQNPPIGIGEPIFDKLEAELAKMILSIPAVKGIEFGSGFNGTYMFGSMHNDIFIPVENMSTKKESDLLYDDKGECKNMSYHSTIQNNEDQILNSTKGFMPPKNDKNFNNIDDYNVTFNNNEEKLLITKTNNCGGILAGISTGNNIVFRSAIKPVSSIQIEKETSDFYGNMCNLKVQGRHDSCILPRLPPIIEASSSMVIGDLILRQISKYGDKKLPTLFRNM

[Multiple Choices]
A. amyloid fibril formation
B. regulation of gene expression
C. amino acid biosynthetic process
D. small molecule biosynthetic process
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

> The matched protein is annotated as chorismate synthase, and the cited functional evidence says it converts EPSP to chorismate. Chorismate is an intermediate in aromatic amino acid biosynthesis, supporting choice C. The specific GO annotation for amino acid biosynthesis is computational (IEA), while the more specific chorismate-biosynthesis annotation is experimental (IDA); these are distinct evidence types.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone supplies no clear, general biological clue that identifies this protein's pathway role or distinguishes amino acid biosynthesis from the broader small-molecule biosynthesis option. Identifying the enzyme family would require protein-specific recognition or sequence comparison.


**Missing item-specific fact**

> The protein's identity and function as chorismate synthase, including its role in chorismate production for aromatic amino acid biosynthesis, are not provided in the question.


**Reason**

> The reviewer-only evidence supports the key, but it was not supplied to the evaluated model. Exact-sequence recognition or access to protein-specific annotation would be needed to establish the pathway role; that is lookup or memorization, not reasoning from the supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Choice C is supported by the amino-acid-biosynthesis annotation and the enzyme's role in the aromatic amino acid pathway. Choice D is also defensible at a broader GO level: chorismate biosynthesis is a small-molecule biosynthetic process, and the specific chorismate-biosynthesis term has D as an ontology ancestor.


### Important caveats

- The exact sequence matches the current and historical UniProt entry, but the author's source snapshot is unknown.
- The function evidence for chorismate synthesis is cited as experimental; the broad amino acid biosynthesis GO annotation is IEA, and the aromatic amino acid family annotation is IBA.
- Choice C is supported, but the wording asks for a primary process without specifying whether to prefer a more specific pathway term or a broader GO parent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone supplies no clear, general biological clue that identifies this protein's pathway role or distinguishes amino acid biosynthesis from the broader small-molecule biosynthesis option. Identifying the enzyme family would require protein-specific recognition or sequence comparison.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and function as chorismate synthase, including its role in chorismate production for aromatic amino acid biosynthesis, are not provided in the question.",
    "reason": "The reviewer-only evidence supports the key, but it was not supplied to the evaluated model. Exact-sequence recognition or access to protein-specific annotation would be needed to establish the pathway role; that is lookup or memorization, not reasoning from the supplied context."
  },
  "case_id": "GO_biological_process_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "C8",
      "H4",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The matched protein is annotated as chorismate synthase, and the cited functional evidence says it converts EPSP to chorismate. Chorismate is an intermediate in aromatic amino acid biosynthesis, supporting choice C. The specific GO annotation for amino acid biosynthesis is computational (IEA), while the more specific chorismate-biosynthesis annotation is experimental (IDA); these are distinct evidence types."
  },
  "important_caveats": [
    "The exact sequence matches the current and historical UniProt entry, but the author's source snapshot is unknown.",
    "The function evidence for chorismate synthesis is cited as experimental; the broad amino acid biosynthesis GO annotation is IEA, and the aromatic amino acid family annotation is IBA.",
    "Choice C is supported, but the wording asks for a primary process without specifying whether to prefer a more specific pathway term or a broader GO parent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Choice C is supported by the amino-acid-biosynthesis annotation and the enzyme's role in the aromatic amino acid pathway. Choice D is also defensible at a broader GO level: chorismate biosynthesis is a small-molecule biosynthetic process, and the specific chorismate-biosynthesis term has D as an ontology ancestor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein is annotated as chorismate synthase, and the cited functional evidence says it converts EPSP to chorismate. Chorismate is an intermediate in aromatic amino acid biosynthesis, supporting choice C. The specific GO annotation for amino acid biosynthesis is computational (IEA), while the more specific chorismate-biosynthesis annotation is experimental (IDA); these are distinct evidence types.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "C8", "H4", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone supplies no clear, general biological clue that identifies this protein's pathway role or distinguishes amino acid biosynthesis from the broader small-molecule biosynthesis option. Identifying the enzyme family would require protein-specific recognition or sequence comparison.",
    "missing_item_specific_fact": "The protein's identity and function as chorismate synthase, including its role in chorismate production for aromatic amino acid biosynthesis, are not provided in the question.",
    "reason": "The reviewer-only evidence supports the key, but it was not supplied to the evaluated model. Exact-sequence recognition or access to protein-specific annotation would be needed to establish the pathway role; that is lookup or memorization, not reasoning from the supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Choice C is supported by the amino-acid-biosynthesis annotation and the enzyme's role in the aromatic amino acid pathway. Choice D is also defensible at a broader GO level: chorismate biosynthesis is a small-molecule biosynthetic process, and the specific chorismate-biosynthesis term has D as an ontology ancestor."
  },
  "important_caveats": [
    "The exact sequence matches the current and historical UniProt entry, but the author's source snapshot is unknown.",
    "The function evidence for chorismate synthesis is cited as experimental; the broad amino acid biosynthesis GO annotation is IEA, and the aromatic amino acid family annotation is IBA.",
    "Choice C is supported, but the wording asks for a primary process without specifying whether to prefer a more specific pathway term or a broader GO parent."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is chorismate synthase (C6KT66, AROC_PLAF7) from Plasmodium falciparum, the last step (7/7) of the shikimate pathway producing chorismate, the precursor to aromatic amino acids (Phe, Tyr, Trp). UniProt annotates GO:0008652 'amino acid biosynthetic process' (IEA:UniProtKB-KW) and GO:0009073 'aromatic amino acid family biosynthetic process' (IBA). The more specific experimental annotation (IDA) is GO:0009423 'chorismate biosynthetic process.' Among the four choices, C is the most biologically meaningful description of the overall objective of the shikimate pathway. The IEA evidence code is weak, but the annotation is consistent with the well-established biochemistry of the shikimate pathway leading to aromatic amino acid synthesis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If one knew the protein is chorismate synthase (a shikimate pathway enzyme), one could reason that the pathway's ultimate purpose is aromatic amino acid biosynthesis, distinguishing C from D. However, this identification requires recognizing the specific enzyme from a 527-aa sequence with no obvious universally recognizable motifs for a general biologist.


**Missing item-specific fact**

> The identification of this sequence as chorismate synthase (or at minimum a shikimate pathway enzyme) is required to connect the catalytic activity (EPSP → chorismate) to amino acid biosynthesis rather than generic small molecule biosynthesis. The sequence alone does not provide sufficient distinguishing features to separate 'amino acid biosynthetic process' from 'small molecule biosynthetic process' without knowing the specific substrate/product identity.


**Reason**

> Distinguishing C (amino acid biosynthetic process) from D (small molecule biosynthetic process) requires knowing that chorismate is specifically an amino acid precursor rather than just any small molecule. This is an item-specific fact about this enzyme's role in the shikimate pathway. The sequence provides no obvious general-biology reasoning chain that would lead a solver from raw amino acid letters to 'this enzyme makes a precursor for amino acids' rather than 'this enzyme makes a small molecule.' Identification of the protein as chorismate synthase is essentially a lookup or memorization task.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Chorismate is itself a small molecule, and the GO hierarchy places 'chorismate biosynthetic process' under 'small molecule biosynthetic process' (GO:0044283). Option D is technically valid from the ontology structure. However, the question asks for the 'overall biological objective' or 'primary biological process,' which favors C because the shikimate pathway's biological purpose is amino acid production. The distinction between C and D depends on whether one interprets the question as asking about the immediate product (chorismate = small molecule) or the pathway's biological objective (amino acid synthesis). The 'primary biological process' framing in the system prompt tips toward C, but D is not strictly wrong.


### Important caveats

- The GO:0008652 annotation is IEA (inferred from electronic annotation/keyword), the weakest evidence code. The experimentally supported annotation (IDA) is for 'chorismate biosynthetic process' (GO:0009423), not directly for 'amino acid biosynthetic process.'
- The sequence identity to C6KT66 is confirmed by SHA-256 match, but the author's source snapshot is unknown; the entry was first publicly released 2025-06-18.
- The protein is bifunctional (chorismate synthase + flavin reductase per PubMed:31381947), but the primary biological process annotation focuses on the chorismate synthase role.
- Option D is not strictly incorrect given the GO hierarchy, but is less specific to the biological objective of the pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If one knew the protein is chorismate synthase (a shikimate pathway enzyme), one could reason that the pathway's ultimate purpose is aromatic amino acid biosynthesis, distinguishing C from D. However, this identification requires recognizing the specific enzyme from a 527-aa sequence with no obvious universally recognizable motifs for a general biologist.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this sequence as chorismate synthase (or at minimum a shikimate pathway enzyme) is required to connect the catalytic activity (EPSP → chorismate) to amino acid biosynthesis rather than generic small molecule biosynthesis. The sequence alone does not provide sufficient distinguishing features to separate 'amino acid biosynthetic process' from 'small molecule biosynthetic process' without knowing the specific substrate/product identity.",
    "reason": "Distinguishing C (amino acid biosynthetic process) from D (small molecule biosynthetic process) requires knowing that chorismate is specifically an amino acid precursor rather than just any small molecule. This is an item-specific fact about this enzyme's role in the shikimate pathway. The sequence provides no obvious general-biology reasoning chain that would lead a solver from raw amino acid letters to 'this enzyme makes a precursor for amino acids' rather than 'this enzyme makes a small molecule.' Identification of the protein as chorismate synthase is essentially a lookup or memorization task."
  },
  "case_id": "GO_biological_process_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H6",
      "H7",
      "H8",
      "GO1",
      "GO2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The protein is chorismate synthase (C6KT66, AROC_PLAF7) from Plasmodium falciparum, the last step (7/7) of the shikimate pathway producing chorismate, the precursor to aromatic amino acids (Phe, Tyr, Trp). UniProt annotates GO:0008652 'amino acid biosynthetic process' (IEA:UniProtKB-KW) and GO:0009073 'aromatic amino acid family biosynthetic process' (IBA). The more specific experimental annotation (IDA) is GO:0009423 'chorismate biosynthetic process.' Among the four choices, C is the most biologically meaningful description of the overall objective of the shikimate pathway. The IEA evidence code is weak, but the annotation is consistent with the well-established biochemistry of the shikimate pathway leading to aromatic amino acid synthesis."
  },
  "important_caveats": [
    "The GO:0008652 annotation is IEA (inferred from electronic annotation/keyword), the weakest evidence code. The experimentally supported annotation (IDA) is for 'chorismate biosynthetic process' (GO:0009423), not directly for 'amino acid biosynthetic process.'",
    "The sequence identity to C6KT66 is confirmed by SHA-256 match, but the author's source snapshot is unknown; the entry was first publicly released 2025-06-18.",
    "The protein is bifunctional (chorismate synthase + flavin reductase per PubMed:31381947), but the primary biological process annotation focuses on the chorismate synthase role.",
    "Option D is not strictly incorrect given the GO hierarchy, but is less specific to the biological objective of the pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Chorismate is itself a small molecule, and the GO hierarchy places 'chorismate biosynthetic process' under 'small molecule biosynthetic process' (GO:0044283). Option D is technically valid from the ontology structure. However, the question asks for the 'overall biological objective' or 'primary biological process,' which favors C because the shikimate pathway's biological purpose is amino acid production. The distinction between C and D depends on whether one interprets the question as asking about the immediate product (chorismate = small molecule) or the pathway's biological objective (amino acid synthesis). The 'primary biological process' framing in the system prompt tips toward C, but D is not strictly wrong."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is chorismate synthase (C6KT66, AROC_PLAF7) from Plasmodium falciparum, the last step (7/7) of the shikimate pathway producing chorismate, the precursor to aromatic amino acids (Phe, Tyr, Trp). UniProt annotates GO:0008652 'amino acid biosynthetic process' (IEA:UniProtKB-KW) and GO:0009073 'aromatic amino acid family biosynthetic process' (IBA). The more specific experimental annotation (IDA) is GO:0009423 'chorismate biosynthetic process.' Among the four choices, C is the most biologically meaningful description of the overall objective of the shikimate pathway. The IEA evidence code is weak, but the annotation is consistent with the well-established biochemistry of the shikimate pathway leading to aromatic amino acid synthesis.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H6", "H7", "H8", "GO1", "GO2", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If one knew the protein is chorismate synthase (a shikimate pathway enzyme), one could reason that the pathway's ultimate purpose is aromatic amino acid biosynthesis, distinguishing C from D. However, this identification requires recognizing the specific enzyme from a 527-aa sequence with no obvious universally recognizable motifs for a general biologist.",
    "missing_item_specific_fact": "The identification of this sequence as chorismate synthase (or at minimum a shikimate pathway enzyme) is required to connect the catalytic activity (EPSP → chorismate) to amino acid biosynthesis rather than generic small molecule biosynthesis. The sequence alone does not provide sufficient distinguishing features to separate 'amino acid biosynthetic process' from 'small molecule biosynthetic process' without knowing the specific substrate/product identity.",
    "reason": "Distinguishing C (amino acid biosynthetic process) from D (small molecule biosynthetic process) requires knowing that chorismate is specifically an amino acid precursor rather than just any small molecule. This is an item-specific fact about this enzyme's role in the shikimate pathway. The sequence provides no obvious general-biology reasoning chain that would lead a solver from raw amino acid letters to 'this enzyme makes a precursor for amino acids' rather than 'this enzyme makes a small molecule.' Identification of the protein as chorismate synthase is essentially a lookup or memorization task."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Chorismate is itself a small molecule, and the GO hierarchy places 'chorismate biosynthetic process' under 'small molecule biosynthetic process' (GO:0044283). Option D is technically valid from the ontology structure. However, the question asks for the 'overall biological objective' or 'primary biological process,' which favors C because the shikimate pathway's biological purpose is amino acid production. The distinction between C and D depends on whether one interprets the question as asking about the immediate product (chorismate = small molecule) or the pathway's biological objective (amino acid synthesis). The 'primary biological process' framing in the system prompt tips toward C, but D is not strictly wrong."
  },
  "important_caveats": [
    "The GO:0008652 annotation is IEA (inferred from electronic annotation/keyword), the weakest evidence code. The experimentally supported annotation (IDA) is for 'chorismate biosynthetic process' (GO:0009423), not directly for 'amino acid biosynthetic process.'",
    "The sequence identity to C6KT66 is confirmed by SHA-256 match, but the author's source snapshot is unknown; the entry was first publicly released 2025-06-18.",
    "The protein is bifunctional (chorismate synthase + flavin reductase per PubMed:31381947), but the primary biological process annotation focuses on the chorismate synthase role.",
    "Option D is not strictly incorrect given the GO hierarchy, but is less specific to the biological objective of the pathway."
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

**Accession:** `C6KT66` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 89. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
"C6KT66"
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"31381947","source":"PubMed"}],"value":"1.5.1.38"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"value":"4.2.3.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"31381947","source":"PubMed"}],"value":"Chorismate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"}],"value":"PfCS"}]}}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"value":"Bifunctional chorismate synthase and flavin reductase (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate 3-phosphate (EPSP) to form chorismate (PubMed:11298276, PubMed:31381947). Acts also as a flavin reductase (FR) able to generate reduced flavin mononucleotide in the presence of NADPH (PubMed:31381947)"}]}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q12640","source":"UniProtKB"}],"value":"Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7"}]}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/uniProtKBCrossReferences/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"database":"GO","id":"GO:0009073","properties":[{"key":"GoTerm","value":"P:aromatic amino acid family biosynthetic process"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/uniProtKBCrossReferences/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"11298276","source":"PubMed"}],"id":"GO:0009423","properties":[{"key":"GoTerm","value":"P:chorismate biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 65-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
CC   -!- FUNCTION: Bifunctional chorismate synthase and flavin reductase
CC       (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate
CC       3-phosphate (EPSP) to form chorismate (PubMed:11298276,
CC       PubMed:31381947). Acts also as a flavin reductase (FR) able to generate
CC       reduced flavin mononucleotide in the presence of NADPH
CC       (PubMed:31381947). {ECO:0000269|PubMed:11298276,
CC       ECO:0000269|PubMed:31381947}.
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 124-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
DR   GO; GO:0008652; P:amino acid biosynthetic process; IEA:UniProtKB-KW.
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 125-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
DR   GO; GO:0009073; P:aromatic amino acid family biosynthetic process; IBA:GO_Central.
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 126-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
DR   GO; GO:0009423; P:chorismate biosynthetic process; IDA:GeneDB.
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 85809-85822`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008652
name: amino acid biosynthetic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the formation of amino acids, organic acids containing one or more amino substituents." [ISBN:0198506732]
synonym: "amino acid anabolism" EXACT []
synonym: "amino acid biosynthesis" EXACT []
synonym: "amino acid formation" EXACT []
synonym: "amino acid synthesis" EXACT []
synonym: "cellular amino acid biosynthetic process" EXACT []
xref: Wikipedia:Amino_acid_synthesis
is_a: GO:0006520 ! amino acid metabolic process
is_a: GO:0009058 ! biosynthetic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 92425-92439`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009073
name: aromatic amino acid biosynthetic process
namespace: biological_process
alt_id: GO:0016089
def: "The chemical reactions and pathways resulting in the formation of an amino acid whose structure includes an aromatic ring." [GOC:curators]
synonym: "aromatic amino acid family anabolism" EXACT []
synonym: "aromatic amino acid family biosynthesis" EXACT []
synonym: "aromatic amino acid family biosynthetic process, shikimate pathway" RELATED []
synonym: "aromatic amino acid family formation" EXACT []
synonym: "aromatic amino acid family synthesis" EXACT []
xref: MetaCyc:COMPLETE-ARO-PWY
is_a: GO:0009072 ! aromatic amino acid metabolic process
is_a: GO:0046394 ! carboxylic acid biosynthetic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 96113-96136`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009423
name: chorismate biosynthetic process
namespace: biological_process
alt_id: GO:0033587
def: "The chemical reactions and pathways resulting in the formation of the unsymmetrical ether derived from phosphoenolpyruvate and 5-phosphoshikimic acid formed as an intermediate in the biosynthesis of aromatic amino acids and many other compounds." [GOC:sm, ISBN:0198547684]
synonym: "chorismate anabolism" EXACT []
synonym: "chorismate biosynthesis" EXACT []
synonym: "chorismate formation" EXACT []
synonym: "chorismate synthesis" EXACT []
synonym: "shikimate anabolism" RELATED []
synonym: "shikimate biosynthesis" RELATED []
synonym: "shikimate biosynthetic process" RELATED []
synonym: "shikimate pathway" EXACT []
synonym: "shikimate synthesis" RELATED []
xref: MetaCyc:ARO-PWY
xref: MetaCyc:PWY-6163
xref: MetaCyc:PWY-6165
is_a: GO:0043650 ! dicarboxylic acid biosynthetic process
is_a: GO:0046417 ! chorismate metabolic process
property_value: skos:narrowMatch MetaCyc:ARO-PWY
property_value: skos:narrowMatch MetaCyc:PWY-6163
property_value: skos:narrowMatch MetaCyc:PWY-6165

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
