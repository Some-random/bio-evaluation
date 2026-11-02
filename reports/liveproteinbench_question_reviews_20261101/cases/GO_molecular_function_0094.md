# GO_molecular_function_0094

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — penicillin binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRVLALSAVFLVASIIGMPAVAKEWQENKSWNAHFTEHKSQGVVVLWNENKQQGFTNNLKRANQAFLPASTFKIPNSLIALDLGVVKDEHQVFKWDGQTRDIATWNRDHNLITAMKYSVVPVYQEFARQIGEARMSKMLHAFDYGNEDISGNVDSFWLDGGIRISATEQISFLRKLYHNKLHVSERSQRIVKQAMLTEANGDYIIRAKTGYSTRIEPKIGWWVGWVELDDNVWFFAMNMDMPTSDGLGLRQAITKEVLKQEKIIP

[Multiple Choices]
A. potassium channel regulator activity
B. penicillin binding
C. peptide hormone receptor binding
D. DNA nuclease activity
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

> The sequence-matched UniProt record assigns penicillin binding by InterPro inference (C8). Separately, experimental evidence reports beta-lactam hydrolysis, including amoxicillin, supporting the relevant substrate interaction, though it is not a direct binding measurement (C5, C6).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a signal-peptide-like N-terminus and an SxxK motif (STFK), consistent with a serine beta-lactamase active site. Such an enzyme acts on beta-lactam antibiotics, making penicillin binding the fitting choice among these options.


**Missing item-specific fact**

> The specific protein identity or an experimental binding annotation is not essential to distinguish these choices from the sequence-family clues.


**Reason**

> The sequence provides a defensible family-level clue that connects to beta-lactam substrate interaction; the choice need not rely solely on remembering this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the only option consistent with a beta-lactamase-like sequence. The other choices describe unrelated activities.


### Important caveats

- The direct penicillin-binding GO assignment is computational (InterPro); the cited experimental evidence establishes beta-lactam hydrolysis rather than a standalone binding assay.
- Reviewer-only database evidence supports the key but was not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and an SxxK motif (STFK), consistent with a serine beta-lactamase active site. Such an enzyme acts on beta-lactam antibiotics, making penicillin binding the fitting choice among these options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific protein identity or an experimental binding annotation is not essential to distinguish these choices from the sequence-family clues.",
    "reason": "The sequence provides a defensible family-level clue that connects to beta-lactam substrate interaction; the choice need not rely solely on remembering this exact protein's database entry."
  },
  "case_id": "GO_molecular_function_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns penicillin binding by InterPro inference (C8). Separately, experimental evidence reports beta-lactam hydrolysis, including amoxicillin, supporting the relevant substrate interaction, though it is not a direct binding measurement (C5, C6)."
  },
  "important_caveats": [
    "The direct penicillin-binding GO assignment is computational (InterPro); the cited experimental evidence establishes beta-lactam hydrolysis rather than a standalone binding assay.",
    "Reviewer-only database evidence supports the key but was not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only option consistent with a beta-lactamase-like sequence. The other choices describe unrelated activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns penicillin binding by InterPro inference (C8). Separately, experimental evidence reports beta-lactam hydrolysis, including amoxicillin, supporting the relevant substrate interaction, though it is not a direct binding measurement (C5, C6).",
    "evidence_ids": ["C1", "C5", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and an SxxK motif (STFK), consistent with a serine beta-lactamase active site. Such an enzyme acts on beta-lactam antibiotics, making penicillin binding the fitting choice among these options.",
    "missing_item_specific_fact": "The specific protein identity or an experimental binding annotation is not essential to distinguish these choices from the sequence-family clues.",
    "reason": "The sequence provides a defensible family-level clue that connects to beta-lactam substrate interaction; the choice need not rely solely on remembering this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only option consistent with a beta-lactamase-like sequence. The other choices describe unrelated activities."
  },
  "important_caveats": [
    "The direct penicillin-binding GO assignment is computational (InterPro); the cited experimental evidence establishes beta-lactam hydrolysis rather than a standalone binding assay.",
    "Reviewer-only database evidence supports the key but was not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Beta-lactamase OXA-48 (Q6XEC0), a class D beta-lactamase (EC 3.5.2.6) from Klebsiella pneumoniae. UniProt annotates it with GO:0008658 (penicillin binding, IEA:InterPro) in addition to GO:0008800 (beta-lactamase activity, EXP). While the primary molecular function is catalytic hydrolysis of the beta-lactam ring (GO:0008800), which is not among the options, 'penicillin binding' is a valid secondary annotation and the only option consistent with the protein's identity. A beta-lactamase necessarily binds penicillin-class substrates as part of its catalytic mechanism. The other three options (potassium channel regulator, peptide hormone receptor binding, DNA nuclease) are entirely inconsistent with a secreted bacterial beta-lactamase.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal signal peptide (MRVLALSAVFLVASIIGMPAVAKE...) typical of Gram-negative bacterial secretion, and the overall composition is consistent with a bacterial protein. Among the four options: (A) potassium channel regulator activity requires interaction with eukaryotic membrane ion channels—incompatible with a bacterial secreted protein; (C) peptide hormone receptor binding is a eukaryotic endocrine signaling concept—inapplicable to bacteria; (D) DNA nuclease activity involves nucleic acid processing, typically intracellular—inconsistent with a secreted protein. Only (B) penicillin binding is biologically coherent for a secreted bacterial enzyme that interacts with small-molecule antibiotics. Additionally, the sequence contains recognizable class D beta-lactamase motifs (SxxK active-site serine motif, KTG triad visible as 'KTGYST'), which positively identify it as a beta-lactamase that binds and hydrolyzes penicillin-class substrates.


**Missing item-specific fact**

> None critical. The elimination of three clearly eukaryotic/intracellular functions from a bacterial secreted protein provides meaningful reasoning grounds. Positive identification of beta-lactamase motifs (SxxK, KTG) strengthens the case but is not strictly necessary given the elimination logic.


**Reason**

> General biological knowledge about bacterial vs. eukaryotic protein functions, secretion signals, and the incompatibility of eukaryotic signaling/membrane-channel functions with a bacterial secreted protein provides a concrete reasoning chain to eliminate A, C, and D. The remaining option B is the only biologically plausible function. Recognition of beta-lactamase sequence motifs (SxxK, KTG) further confirms the positive identification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option B is biologically consistent with a secreted bacterial beta-lactamase. Options A, C, and D describe functions that are fundamentally incompatible with the protein's organismal origin, subcellular localization, and enzymatic class. No ambiguity exists among the choices.


### Important caveats

- The true primary molecular function of this protein is GO:0008800 (beta-lactamase activity, EXP evidence), which is not offered as an option. 'Penicillin binding' (GO:0008658) is annotated only with IEA:InterPro (computational inference from domain match), not experimental evidence. The question is answerable because B is the only viable option, but it is a secondary rather than primary annotation.
- The GO term 'penicillin binding' describes binding to penicillin specifically; the protein also binds and hydrolyzes other beta-lactams (oxacillin, cephalothin, imipenem). The term is a reasonable proxy among the given choices.
- The identity of the protein as OXA-48 beta-lactamase was established by reviewer-only UniProt lookup; the evaluated model must infer this from sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MRVLALSAVFLVASIIGMPAVAKE...) typical of Gram-negative bacterial secretion, and the overall composition is consistent with a bacterial protein. Among the four options: (A) potassium channel regulator activity requires interaction with eukaryotic membrane ion channels—incompatible with a bacterial secreted protein; (C) peptide hormone receptor binding is a eukaryotic endocrine signaling concept—inapplicable to bacteria; (D) DNA nuclease activity involves nucleic acid processing, typically intracellular—inconsistent with a secreted protein. Only (B) penicillin binding is biologically coherent for a secreted bacterial enzyme that interacts with small-molecule antibiotics. Additionally, the sequence contains recognizable class D beta-lactamase motifs (SxxK active-site serine motif, KTG triad visible as 'KTGYST'), which positively identify it as a beta-lactamase that binds and hydrolyzes penicillin-class substrates.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The elimination of three clearly eukaryotic/intracellular functions from a bacterial secreted protein provides meaningful reasoning grounds. Positive identification of beta-lactamase motifs (SxxK, KTG) strengthens the case but is not strictly necessary given the elimination logic.",
    "reason": "General biological knowledge about bacterial vs. eukaryotic protein functions, secretion signals, and the incompatibility of eukaryotic signaling/membrane-channel functions with a bacterial secreted protein provides a concrete reasoning chain to eliminate A, C, and D. The remaining option B is the only biologically plausible function. Recognition of beta-lactamase sequence motifs (SxxK, KTG) further confirms the positive identification."
  },
  "case_id": "GO_molecular_function_0094",
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
      "H9",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein is Beta-lactamase OXA-48 (Q6XEC0), a class D beta-lactamase (EC 3.5.2.6) from Klebsiella pneumoniae. UniProt annotates it with GO:0008658 (penicillin binding, IEA:InterPro) in addition to GO:0008800 (beta-lactamase activity, EXP). While the primary molecular function is catalytic hydrolysis of the beta-lactam ring (GO:0008800), which is not among the options, 'penicillin binding' is a valid secondary annotation and the only option consistent with the protein's identity. A beta-lactamase necessarily binds penicillin-class substrates as part of its catalytic mechanism. The other three options (potassium channel regulator, peptide hormone receptor binding, DNA nuclease) are entirely inconsistent with a secreted bacterial beta-lactamase."
  },
  "important_caveats": [
    "The true primary molecular function of this protein is GO:0008800 (beta-lactamase activity, EXP evidence), which is not offered as an option. 'Penicillin binding' (GO:0008658) is annotated only with IEA:InterPro (computational inference from domain match), not experimental evidence. The question is answerable because B is the only viable option, but it is a secondary rather than primary annotation.",
    "The GO term 'penicillin binding' describes binding to penicillin specifically; the protein also binds and hydrolyzes other beta-lactams (oxacillin, cephalothin, imipenem). The term is a reasonable proxy among the given choices.",
    "The identity of the protein as OXA-48 beta-lactamase was established by reviewer-only UniProt lookup; the evaluated model must infer this from sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B is biologically consistent with a secreted bacterial beta-lactamase. Options A, C, and D describe functions that are fundamentally incompatible with the protein's organismal origin, subcellular localization, and enzymatic class. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Beta-lactamase OXA-48 (Q6XEC0), a class D beta-lactamase (EC 3.5.2.6) from Klebsiella pneumoniae. UniProt annotates it with GO:0008658 (penicillin binding, IEA:InterPro) in addition to GO:0008800 (beta-lactamase activity, EXP). While the primary molecular function is catalytic hydrolysis of the beta-lactam ring (GO:0008800), which is not among the options, 'penicillin binding' is a valid secondary annotation and the only option consistent with the protein's identity. A beta-lactamase necessarily binds penicillin-class substrates as part of its catalytic mechanism. The other three options (potassium channel regulator, peptide hormone receptor binding, DNA nuclease) are entirely inconsistent with a secreted bacterial beta-lactamase.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H6", "H7", "H8", "H9", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MRVLALSAVFLVASIIGMPAVAKE...) typical of Gram-negative bacterial secretion, and the overall composition is consistent with a bacterial protein. Among the four options: (A) potassium channel regulator activity requires interaction with eukaryotic membrane ion channels—incompatible with a bacterial secreted protein; (C) peptide hormone receptor binding is a eukaryotic endocrine signaling concept—inapplicable to bacteria; (D) DNA nuclease activity involves nucleic acid processing, typically intracellular—inconsistent with a secreted protein. Only (B) penicillin binding is biologically coherent for a secreted bacterial enzyme that interacts with small-molecule antibiotics. Additionally, the sequence contains recognizable class D beta-lactamase motifs (SxxK active-site serine motif, KTG triad visible as 'KTGYST'), which positively identify it as a beta-lactamase that binds and hydrolyzes penicillin-class substrates.",
    "missing_item_specific_fact": "None critical. The elimination of three clearly eukaryotic/intracellular functions from a bacterial secreted protein provides meaningful reasoning grounds. Positive identification of beta-lactamase motifs (SxxK, KTG) strengthens the case but is not strictly necessary given the elimination logic.",
    "reason": "General biological knowledge about bacterial vs. eukaryotic protein functions, secretion signals, and the incompatibility of eukaryotic signaling/membrane-channel functions with a bacterial secreted protein provides a concrete reasoning chain to eliminate A, C, and D. The remaining option B is the only biologically plausible function. Recognition of beta-lactamase sequence motifs (SxxK, KTG) further confirms the positive identification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B is biologically consistent with a secreted bacterial beta-lactamase. Options A, C, and D describe functions that are fundamentally incompatible with the protein's organismal origin, subcellular localization, and enzymatic class. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The true primary molecular function of this protein is GO:0008800 (beta-lactamase activity, EXP evidence), which is not offered as an option. 'Penicillin binding' (GO:0008658) is annotated only with IEA:InterPro (computational inference from domain match), not experimental evidence. The question is answerable because B is the only viable option, but it is a secondary rather than primary annotation.",
    "The GO term 'penicillin binding' describes binding to penicillin specifically; the protein also binds and hydrolyzes other beta-lactams (oxacillin, cephalothin, imipenem). The term is a reasonable proxy among the given choices.",
    "The identity of the protein as OXA-48 beta-lactamase was established by reviewer-only UniProt lookup; the evaluated model must infer this from sequence features alone."
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

**Accession:** `Q6XEC0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 136. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
"Q6XEC0"
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"14693513","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19477418","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"27073009","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38161376","source":"PubMed"}],"value":"3.5.2.6"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"14693513","source":"PubMed"}],"value":"Beta-lactamase OXA-48"}}}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"14693513","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19477418","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"27073009","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38161376","source":"PubMed"}],"value":"Class D beta-lactamase which confers resistance to the beta-lactam antibiotics, including amoxicillin, and moderate resistance to cephalosporins and carbapenems such as cephalothin and imipenem; in the DH10B strain of E.coli (PubMed:14693513). Acts via hydrolysis of the beta-lactam ring (PubMed:14693513, PubMed:19477418, PubMed:27073009, PubMed:38161376). Has oxacillin-, cephalothin- and imipenem-hydrolyzing activities (PubMed:14693513, PubMed:19477418, PubMed:27073009, PubMed:38161376)"}]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.5.2.6","evidences":[{"evidenceCode":"ECO:0000269","id":"14693513","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19477418","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"27073009","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38161376","source":"PubMed"}],"name":"a beta-lactam + H2O = a substituted beta-amino acid","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20401"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35627"},{"database":"ChEBI","id":"CHEBI:140347"}]}}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/uniProtKBCrossReferences/258`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"14693513","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19477418","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"27073009","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38161376","source":"PubMed"}],"id":"GO:0008800","properties":[{"key":"GoTerm","value":"F:beta-lactamase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/uniProtKBCrossReferences/259`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"database":"GO","id":"GO:0008658","properties":[{"key":"GoTerm","value":"F:penicillin binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 211-220`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
CC   -!- FUNCTION: Class D beta-lactamase which confers resistance to the beta-
CC       lactam antibiotics, including amoxicillin, and moderate resistance to
CC       cephalosporins and carbapenems such as cephalothin and imipenem; in the
CC       DH10B strain of E.coli (PubMed:14693513). Acts via hydrolysis of the
CC       beta-lactam ring (PubMed:14693513, PubMed:19477418, PubMed:27073009,
CC       PubMed:38161376). Has oxacillin-, cephalothin- and imipenem-hydrolyzing
CC       activities (PubMed:14693513, PubMed:19477418, PubMed:27073009,
CC       PubMed:38161376). {ECO:0000269|PubMed:14693513,
CC       ECO:0000269|PubMed:19477418, ECO:0000269|PubMed:27073009,
CC       ECO:0000269|PubMed:38161376}.
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 221-226`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a beta-lactam + H2O = a substituted beta-amino acid;
CC         Xref=Rhea:RHEA:20401, ChEBI:CHEBI:15377, ChEBI:CHEBI:35627,
CC         ChEBI:CHEBI:140347; EC=3.5.2.6;
CC         Evidence={ECO:0000269|PubMed:14693513, ECO:0000269|PubMed:19477418,
CC         ECO:0000269|PubMed:27073009, ECO:0000269|PubMed:38161376};
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 589-589`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
DR   GO; GO:0008800; F:beta-lactamase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 590-590`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
DR   GO; GO:0008658; F:penicillin binding; IEA:InterPro.
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 85882-85891`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008658
name: penicillin binding
namespace: molecular_function
def: "Binding to penicillin, an antibiotic that contains the condensed beta-lactamthiazolidine ring system." [GOC:ai]
subset: goslim_metagenomics
is_a: GO:0033293 ! monocarboxylic acid binding
is_a: GO:1901363 ! heterocyclic compound binding
is_a: GO:1901681 ! sulfur compound binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
