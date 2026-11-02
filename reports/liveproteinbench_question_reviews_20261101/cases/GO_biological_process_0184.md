# GO_biological_process_0184

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — carboxylic acid metabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGSLDIKQESSPLMTNPLDSEEFRRQGYMVIDFLAEYYKNIQKFPVRSQVEPGYLRKRLPESAPYEPESIETILKDVHDDIVPGLTHWQSPNYYAYFPSSGSTAGLLGETLAAGFNVVGFNWISSPASTELESIVMDWLAEMLNLPKSFTFSGDGGGVMMGTTCEAILTTITAARDRILDRIGREHINKLVVYGSDQTHCSFFKSAKIAGISPNNFRQVKTSRVNAFSMRPDALRAAIQADVDAGLVPFFLCTTVGTTSTAAVDPVALLCEVAKDYGMWVHIDAAYAGNACICPEFRHMINGVENADSFSFNAHKWFLTTLDCCCLWVKDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQITLSRRFRSLKMWLVLRSYGVDYLRNFLRSHVDMAAYFEQLVRMDGRFEVVVPRSFALVCFRLSASAVIQRLYDSCHRHGHGQKFLEEETLNDVNAELLESVNSAGQIYMTHSLVDGVYMLRFAVGATLTQTHHVTYAWKQVQDHASAVLARRINSICNC

[Multiple Choices]
A. carboxylic acid metabolic process
B. response to cytokine
C. bone mineralization
D. coenzyme A biosynthetic process
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

> For the sequence-matched protein, experimental annotations report decarboxylation of L-tyrosine and L-DOPA. These are carboxylic-acid-containing substrates, so their metabolism supports option A as a broad process, though more specific annotated processes are also available.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [H8](#evidence-h8), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a soluble enzyme, but the input does not establish its substrate or biological role. Inferring that it acts on amino-acid carboxyl groups rather than participating in another process requires identifying its protein-specific function.


**Missing item-specific fact**

> The absent fact is that this protein catalyzes aromatic amino acid decarboxylation, including decarboxylation of tyrosine and L-DOPA; this substrate-specific functional assignment is needed to select A.


**Reason**

> The sequence alone does not make a sufficiently specific case for the substrate or process among the options. The protein-specific functional assignment is not supplied, and merely recognizing or retrieving it would be lookup or memorization rather than reasoning from the provided context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is broad but is supported by the reported metabolism of carboxylic-acid-containing amino-acid substrates. The other choices do not have comparable support in the supplied input.


### Important caveats

- The reviewer-only evidence matches the supplied sequence; the accession and functional annotation were not provided to the evaluated model.
- The protein also has more specific annotations for alkaloid and phenylethylamine biosynthesis, neither of which is offered as a choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme, but the input does not establish its substrate or biological role. Inferring that it acts on amino-acid carboxyl groups rather than participating in another process requires identifying its protein-specific function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The absent fact is that this protein catalyzes aromatic amino acid decarboxylation, including decarboxylation of tyrosine and L-DOPA; this substrate-specific functional assignment is needed to select A.",
    "reason": "The sequence alone does not make a sufficiently specific case for the substrate or process among the options. The protein-specific functional assignment is not supplied, and merely recognizing or retrieving it would be lookup or memorization rather than reasoning from the provided context."
  },
  "case_id": "GO_biological_process_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "H8",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "For the sequence-matched protein, experimental annotations report decarboxylation of L-tyrosine and L-DOPA. These are carboxylic-acid-containing substrates, so their metabolism supports option A as a broad process, though more specific annotated processes are also available."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence; the accession and functional annotation were not provided to the evaluated model.",
    "The protein also has more specific annotations for alkaloid and phenylethylamine biosynthesis, neither of which is offered as a choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is broad but is supported by the reported metabolism of carboxylic-acid-containing amino-acid substrates. The other choices do not have comparable support in the supplied input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "For the sequence-matched protein, experimental annotations report decarboxylation of L-tyrosine and L-DOPA. These are carboxylic-acid-containing substrates, so their metabolism supports option A as a broad process, though more specific annotated processes are also available.",
    "evidence_ids": ["C5", "H4", "H8", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme, but the input does not establish its substrate or biological role. Inferring that it acts on amino-acid carboxyl groups rather than participating in another process requires identifying its protein-specific function.",
    "missing_item_specific_fact": "The absent fact is that this protein catalyzes aromatic amino acid decarboxylation, including decarboxylation of tyrosine and L-DOPA; this substrate-specific functional assignment is needed to select A.",
    "reason": "The sequence alone does not make a sufficiently specific case for the substrate or process among the options. The protein-specific functional assignment is not supplied, and merely recognizing or retrieving it would be lookup or memorization rather than reasoning from the provided context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is broad but is supported by the reported metabolism of carboxylic-acid-containing amino-acid substrates. The other choices do not have comparable support in the supplied input."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence; the accession and functional annotation were not provided to the evaluated model.",
    "The protein also has more specific annotations for alkaloid and phenylethylamine biosynthesis, neither of which is offered as a choice."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (A0AA51Z3J4, LwTyDC2) is an experimentally validated L-tyrosine/L-DOPA decarboxylase (EC 4.1.1.25/4.1.1.28, ECO:0000269). Decarboxylation of L-tyrosine and L-DOPA is a chemical reaction involving carboxylic acids (both substrates contain COOH groups), which falls within the definition of GO:0019752 'carboxylic acid metabolic process' ('The chemical reactions and pathways involving carboxylic acids, any organic acid containing one or more carboxyl (COOH) groups'). Among the four choices, A is the only option with any biochemical connection to this enzyme. However, the term is flagged 'do_not_annotate' in GO and is extremely broad; the protein's actual direct annotations are more specific (amino acid metabolic process IEA:InterPro, alkaloid biosynthetic process IDA, phenylethylamine biosynthetic process IDA). The answer is defensible as the best available option but is not the most precise description.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains motifs characteristic of PLP-dependent aromatic amino acid decarboxylases. Recognizing this enzyme class establishes that it catalyzes removal of a carboxyl group from amino acid substrates. Since amino acids are by definition carboxylic acids (containing COOH groups), their decarboxylation is a carboxylic acid metabolic reaction. The three distractors are clearly incompatible: 'response to cytokine' (B) and 'bone mineralization' (C) are animal-specific processes irrelevant to a plant enzyme, and 'coenzyme A biosynthetic process' (D) involves a completely different enzymatic pathway (pantothenate/CoA synthesis) unrelated to aromatic amino acid decarboxylation.


**Missing item-specific fact**

> None strictly required. General knowledge that (1) this is a plant protein (ruling out B, C), (2) decarboxylases act on carboxylic acid substrates, and (3) CoA biosynthesis involves entirely different enzymes (pantothenate kinases, etc., ruling out D) suffices to eliminate distractors and select A.


**Reason**

> A model with general biochemistry knowledge can identify the enzyme as a decarboxylase from sequence motifs, recognize that amino acids are carboxylic acids, and eliminate the three clearly incompatible distractors. The reasoning path does not require memorizing a specific database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are unambiguously incompatible with a plant aromatic amino acid decarboxylase. Only A has any biochemical relevance. While 'amino acid metabolic process' or 'alkaloid biosynthetic process' would be more precise terms (and are the actual GO annotations), they are not offered, leaving A as the sole defensible choice among the given options.


### Important caveats

- GO:0019752 is flagged 'gocheck_do_not_annotate' in the ontology, meaning curators deliberately avoid using it for direct annotation due to excessive breadth. The protein's actual annotations are more specific (GO:0006520 amino acid metabolic process, GO:0009821 alkaloid biosynthetic process).
- The expected answer is the broadest possible correct category rather than the most informative one. A more precise benchmark would offer 'amino acid metabolic process' or 'alkaloid biosynthetic process' as the correct option.
- The sequence-match is confirmed (SHA256 match between benchmark and UniProt entry A0AA51Z3J4, 522 aa).
- The reviewer-only evidence confirms experimental (IDA) annotations for alkaloid/phenylethylamine/tyramine biosynthetic processes, but none of these specific terms appear among the answer choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains motifs characteristic of PLP-dependent aromatic amino acid decarboxylases. Recognizing this enzyme class establishes that it catalyzes removal of a carboxyl group from amino acid substrates. Since amino acids are by definition carboxylic acids (containing COOH groups), their decarboxylation is a carboxylic acid metabolic reaction. The three distractors are clearly incompatible: 'response to cytokine' (B) and 'bone mineralization' (C) are animal-specific processes irrelevant to a plant enzyme, and 'coenzyme A biosynthetic process' (D) involves a completely different enzymatic pathway (pantothenate/CoA synthesis) unrelated to aromatic amino acid decarboxylation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. General knowledge that (1) this is a plant protein (ruling out B, C), (2) decarboxylases act on carboxylic acid substrates, and (3) CoA biosynthesis involves entirely different enzymes (pantothenate kinases, etc., ruling out D) suffices to eliminate distractors and select A.",
    "reason": "A model with general biochemistry knowledge can identify the enzyme as a decarboxylase from sequence motifs, recognize that amino acids are carboxylic acids, and eliminate the three clearly incompatible distractors. The reasoning path does not require memorizing a specific database annotation."
  },
  "case_id": "GO_biological_process_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein (A0AA51Z3J4, LwTyDC2) is an experimentally validated L-tyrosine/L-DOPA decarboxylase (EC 4.1.1.25/4.1.1.28, ECO:0000269). Decarboxylation of L-tyrosine and L-DOPA is a chemical reaction involving carboxylic acids (both substrates contain COOH groups), which falls within the definition of GO:0019752 'carboxylic acid metabolic process' ('The chemical reactions and pathways involving carboxylic acids, any organic acid containing one or more carboxyl (COOH) groups'). Among the four choices, A is the only option with any biochemical connection to this enzyme. However, the term is flagged 'do_not_annotate' in GO and is extremely broad; the protein's actual direct annotations are more specific (amino acid metabolic process IEA:InterPro, alkaloid biosynthetic process IDA, phenylethylamine biosynthetic process IDA). The answer is defensible as the best available option but is not the most precise description."
  },
  "important_caveats": [
    "GO:0019752 is flagged 'gocheck_do_not_annotate' in the ontology, meaning curators deliberately avoid using it for direct annotation due to excessive breadth. The protein's actual annotations are more specific (GO:0006520 amino acid metabolic process, GO:0009821 alkaloid biosynthetic process).",
    "The expected answer is the broadest possible correct category rather than the most informative one. A more precise benchmark would offer 'amino acid metabolic process' or 'alkaloid biosynthetic process' as the correct option.",
    "The sequence-match is confirmed (SHA256 match between benchmark and UniProt entry A0AA51Z3J4, 522 aa).",
    "The reviewer-only evidence confirms experimental (IDA) annotations for alkaloid/phenylethylamine/tyramine biosynthetic processes, but none of these specific terms appear among the answer choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are unambiguously incompatible with a plant aromatic amino acid decarboxylase. Only A has any biochemical relevance. While 'amino acid metabolic process' or 'alkaloid biosynthetic process' would be more precise terms (and are the actual GO annotations), they are not offered, leaving A as the sole defensible choice among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (A0AA51Z3J4, LwTyDC2) is an experimentally validated L-tyrosine/L-DOPA decarboxylase (EC 4.1.1.25/4.1.1.28, ECO:0000269). Decarboxylation of L-tyrosine and L-DOPA is a chemical reaction involving carboxylic acids (both substrates contain COOH groups), which falls within the definition of GO:0019752 'carboxylic acid metabolic process' ('The chemical reactions and pathways involving carboxylic acids, any organic acid containing one or more carboxyl (COOH) groups'). Among the four choices, A is the only option with any biochemical connection to this enzyme. However, the term is flagged 'do_not_annotate' in GO and is extremely broad; the protein's actual direct annotations are more specific (amino acid metabolic process IEA:InterPro, alkaloid biosynthetic process IDA, phenylethylamine biosynthetic process IDA). The answer is defensible as the best available option but is not the most precise description.",
    "evidence_ids": ["C4", "C5", "C9", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains motifs characteristic of PLP-dependent aromatic amino acid decarboxylases. Recognizing this enzyme class establishes that it catalyzes removal of a carboxyl group from amino acid substrates. Since amino acids are by definition carboxylic acids (containing COOH groups), their decarboxylation is a carboxylic acid metabolic reaction. The three distractors are clearly incompatible: 'response to cytokine' (B) and 'bone mineralization' (C) are animal-specific processes irrelevant to a plant enzyme, and 'coenzyme A biosynthetic process' (D) involves a completely different enzymatic pathway (pantothenate/CoA synthesis) unrelated to aromatic amino acid decarboxylation.",
    "missing_item_specific_fact": "None strictly required. General knowledge that (1) this is a plant protein (ruling out B, C), (2) decarboxylases act on carboxylic acid substrates, and (3) CoA biosynthesis involves entirely different enzymes (pantothenate kinases, etc., ruling out D) suffices to eliminate distractors and select A.",
    "reason": "A model with general biochemistry knowledge can identify the enzyme as a decarboxylase from sequence motifs, recognize that amino acids are carboxylic acids, and eliminate the three clearly incompatible distractors. The reasoning path does not require memorizing a specific database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are unambiguously incompatible with a plant aromatic amino acid decarboxylase. Only A has any biochemical relevance. While 'amino acid metabolic process' or 'alkaloid biosynthetic process' would be more precise terms (and are the actual GO annotations), they are not offered, leaving A as the sole defensible choice among the given options."
  },
  "important_caveats": [
    "GO:0019752 is flagged 'gocheck_do_not_annotate' in the ontology, meaning curators deliberately avoid using it for direct annotation due to excessive breadth. The protein's actual annotations are more specific (GO:0006520 amino acid metabolic process, GO:0009821 alkaloid biosynthetic process).",
    "The expected answer is the broadest possible correct category rather than the most informative one. A more precise benchmark would offer 'amino acid metabolic process' or 'alkaloid biosynthetic process' as the correct option.",
    "The sequence-match is confirmed (SHA256 match between benchmark and UniProt entry A0AA51Z3J4, 522 aa).",
    "The reviewer-only evidence confirms experimental (IDA) annotations for alkaloid/phenylethylamine/tyramine biosynthetic processes, but none of these specific terms appear among the answer choices."
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

**Accession:** `A0AA51Z3J4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 9. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37675639","source":"PubMed"}],"value":"Aromatic amino acid decarboxylase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"37675639","source":"PubMed"}],"value":"LwTyDC1"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"value":"4.1.1.25"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"value":"4.1.1.28"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38835170","source":"PubMed"}],"value":"L-tyrosine/L-DOPA decarboxylase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38835170","source":"PubMed"}],"value":"LwTyDC2"}]}}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"value":"Aromatic amino acid decarboxylase participating in the biosynthesis of natural products derived from phenylethylamine, including mescaline, a natural hallucinogen potentially used in psychotherapeutic treatments (PubMed:37675639, PubMed:38835170). Catalyzes the decarboxylation of L-tyrosine and L-DOPA (PubMed:37675639, PubMed:38835170)"}]}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"database":"GO","id":"GO:0006520","properties":[{"key":"GoTerm","value":"P:amino acid metabolic process"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 39-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
CC   -!- FUNCTION: Aromatic amino acid decarboxylase participating in the
CC       biosynthesis of natural products derived from phenylethylamine,
CC       including mescaline, a natural hallucinogen potentially used in
CC       psychotherapeutic treatments (PubMed:37675639, PubMed:38835170).
CC       Catalyzes the decarboxylation of L-tyrosine and L-DOPA
CC       (PubMed:37675639, PubMed:38835170). {ECO:0000269|PubMed:37675639,
CC       ECO:0000269|PubMed:38835170}.
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 93-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
DR   GO; GO:1903184; P:L-dopa metabolic process; IDA:UniProtKB.
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 152755-152764`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0019752
name: carboxylic acid metabolic process
namespace: biological_process
def: "The chemical reactions and pathways involving carboxylic acids, any organic acid containing one or more carboxyl (COOH) groups or anions (COO-)." [ISBN:0198506732]
subset: gocheck_do_not_annotate
synonym: "carboxylic acid metabolism" EXACT []
xref: Reactome:R-HSA-389661 "Glyoxylate metabolism and glycine degradation"
is_a: GO:0043436 ! oxoacid metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
