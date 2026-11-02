# GO_molecular_function_0115

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — phosphopantothenoylcysteine decarboxylase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSSEPASPEIEQQANSAPRRPRILLAASGSVAAIKFGNLCHSFSEWAEVKAVATRASLHFIDRASLPKDVILYTEEDEWSTWNKVGDSVLHIELRSWADILVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWKNPFTEQHIMSIDELGVSLIPPVTKRLACGDYGNGAMAEPSVIYSTVRLFFESRVQQSGNIVQQPV

[Multiple Choices]
A. ATP hydrolysis activity
B. phosphopantothenoylcysteine decarboxylase activity
C. potassium channel regulator activity
D. peroxidase inhibitor activity
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

> The exact sequence matches the apple HAL3 protein, annotated with phosphopantothenoylcysteine decarboxylase activity. The record links the catalytic reaction to experimental evidence (ECO:0000269) and the GO activity annotation to IDA evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence does not provide a clear general biological clue that uniquely identifies this specific catalytic activity. Its apparent soluble-enzyme character may make some choices less plausible, but does not distinguish PPCDC activity from other enzyme functions.


**Missing item-specific fact**

> The protein's identity as HAL3/PPCDC, or equivalent protein-family or functional annotation, is needed to identify the specific activity.


**Reason**

> The expected answer is supported by reviewer-only, sequence-matched annotation and experimental evidence, but that protein-specific fact is absent from the question input. Knowing or recognizing the sequence's database entry would be lookup or memorization, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein-specific evidence supports option B; the other choices describe distinct activities and are not supported by the supplied sequence alone.


### Important caveats

- The evidence supports the activity for the matched apple HAL3 sequence; the author’s exact source snapshot is unknown.
- The experimental evidence is reported through the UniProt record and cited publication; the primary study was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence does not provide a clear general biological clue that uniquely identifies this specific catalytic activity. Its apparent soluble-enzyme character may make some choices less plausible, but does not distinguish PPCDC activity from other enzyme functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as HAL3/PPCDC, or equivalent protein-family or functional annotation, is needed to identify the specific activity.",
    "reason": "The expected answer is supported by reviewer-only, sequence-matched annotation and experimental evidence, but that protein-specific fact is absent from the question input. Knowing or recognizing the sequence's database entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "case_id": "GO_molecular_function_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C6",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the apple HAL3 protein, annotated with phosphopantothenoylcysteine decarboxylase activity. The record links the catalytic reaction to experimental evidence (ECO:0000269) and the GO activity annotation to IDA evidence."
  },
  "important_caveats": [
    "The evidence supports the activity for the matched apple HAL3 sequence; the author’s exact source snapshot is unknown.",
    "The experimental evidence is reported through the UniProt record and cited publication; the primary study was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein-specific evidence supports option B; the other choices describe distinct activities and are not supported by the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the apple HAL3 protein, annotated with phosphopantothenoylcysteine decarboxylase activity. The record links the catalytic reaction to experimental evidence (ECO:0000269) and the GO activity annotation to IDA evidence.",
    "evidence_ids": ["C1", "C4", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence does not provide a clear general biological clue that uniquely identifies this specific catalytic activity. Its apparent soluble-enzyme character may make some choices less plausible, but does not distinguish PPCDC activity from other enzyme functions.",
    "missing_item_specific_fact": "The protein's identity as HAL3/PPCDC, or equivalent protein-family or functional annotation, is needed to identify the specific activity.",
    "reason": "The expected answer is supported by reviewer-only, sequence-matched annotation and experimental evidence, but that protein-specific fact is absent from the question input. Knowing or recognizing the sequence's database entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein-specific evidence supports option B; the other choices describe distinct activities and are not supported by the supplied sequence alone."
  },
  "important_caveats": [
    "The evidence supports the activity for the matched apple HAL3 sequence; the author’s exact source snapshot is unknown.",
    "The experimental evidence is reported through the UniProt record and cited publication; the primary study was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A498JQK2 (sequence sha256 matched) annotates this protein as Phosphopantothenoylcysteine decarboxylase HAL3 (EC 4.1.1.36) with GO:0004633 'phosphopantothenoylcysteine decarboxylase activity' supported by IDA (Inferred by Direct Assay) evidence from PubMed:32761275. The catalytic activity, function, and EC number are all confirmed by experimental (ECO:0000269) evidence. The GO term definition in GO1 exactly matches option B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A, C, and D each require specific structural features absent from this 214-aa sequence: (A) ATP hydrolysis requires a Walker A/P-loop motif (GxxxxGK&#91;T/S&#93;) and associated nucleotide-binding architecture not present; (C) potassium channel regulator activity requires channel-interacting regulatory domains (e.g., TID/RID domains) absent here; (D) peroxidase inhibitor activity requires specific peroxidase-binding surfaces not evident. The sequence shows glycine-rich regions (e.g., 'GSVAA') and an overall fold consistent with an FMN-dependent decarboxylase family (PF03746), making B the only option compatible with the observed sequence architecture. Elimination of A, C, D by their required structural prerequisites, combined with FMN-binding-like features in the sequence, provides a defensible reasoning path to B.


**Missing item-specific fact**

> Positive identification of the exact PPCDC family (vs. other FMN-dependent enzymes) relies on family-level motif recognition that borders on database lookup; however, the elimination argument for A, C, D is independently valid.


**Reason**

> A model with general knowledge of enzyme structural requirements can eliminate ATPase (no P-loop), potassium channel regulator (no channel-regulatory domain), and peroxidase inhibitor (no binding domain) from a 214-aa sequence lacking these features. The remaining option B is consistent with the observed FMN-binding-like motifs and family-appropriate length. This constitutes a meaningful biological reasoning chain, though the positive identification of PPCDC specifically rather than 'some FMN-dependent enzyme' adds a lookup element.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent structurally and mechanistically distinct molecular functions. ATP hydrolysis, potassium channel regulation, peroxidase inhibition, and phosphopantothenoylcysteine decarboxylase activity require mutually incompatible structural features. The sequence is compatible with only one of these four functions, so no two options are simultaneously defensible.


### Important caveats

- The positive identification of PPCDC (as opposed to any FMN-dependent enzyme) from sequence alone is at the boundary of family-level recognition and database lookup; the elimination argument for A/C/D is stronger than the positive argument for B.
- The GO:0010181 (FMN binding) annotation is only IEA:TreeGrafter (computational), not experimental, so the FMN-dependence inference from the sequence is itself an inference.
- The sequence is from Malus domestica (apple) HAL3, a plant protein; the 214-aa length matches the bacterial-type PPCDC fold rather than the longer eukaryotic PPCDC, which is consistent with the annotation but requires family-level knowledge to appreciate.
- Reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what a model could infer from the sequence and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A, C, and D each require specific structural features absent from this 214-aa sequence: (A) ATP hydrolysis requires a Walker A/P-loop motif (GxxxxGK[T/S]) and associated nucleotide-binding architecture not present; (C) potassium channel regulator activity requires channel-interacting regulatory domains (e.g., TID/RID domains) absent here; (D) peroxidase inhibitor activity requires specific peroxidase-binding surfaces not evident. The sequence shows glycine-rich regions (e.g., 'GSVAA') and an overall fold consistent with an FMN-dependent decarboxylase family (PF03746), making B the only option compatible with the observed sequence architecture. Elimination of A, C, D by their required structural prerequisites, combined with FMN-binding-like features in the sequence, provides a defensible reasoning path to B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of the exact PPCDC family (vs. other FMN-dependent enzymes) relies on family-level motif recognition that borders on database lookup; however, the elimination argument for A, C, D is independently valid.",
    "reason": "A model with general knowledge of enzyme structural requirements can eliminate ATPase (no P-loop), potassium channel regulator (no channel-regulatory domain), and peroxidase inhibitor (no binding domain) from a 214-aa sequence lacking these features. The remaining option B is consistent with the observed FMN-binding-like motifs and family-appropriate length. This constitutes a meaningful biological reasoning chain, though the positive identification of PPCDC specifically rather than 'some FMN-dependent enzyme' adds a lookup element."
  },
  "case_id": "GO_molecular_function_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H1",
      "H3",
      "H4",
      "H6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A498JQK2 (sequence sha256 matched) annotates this protein as Phosphopantothenoylcysteine decarboxylase HAL3 (EC 4.1.1.36) with GO:0004633 'phosphopantothenoylcysteine decarboxylase activity' supported by IDA (Inferred by Direct Assay) evidence from PubMed:32761275. The catalytic activity, function, and EC number are all confirmed by experimental (ECO:0000269) evidence. The GO term definition in GO1 exactly matches option B."
  },
  "important_caveats": [
    "The positive identification of PPCDC (as opposed to any FMN-dependent enzyme) from sequence alone is at the boundary of family-level recognition and database lookup; the elimination argument for A/C/D is stronger than the positive argument for B.",
    "The GO:0010181 (FMN binding) annotation is only IEA:TreeGrafter (computational), not experimental, so the FMN-dependence inference from the sequence is itself an inference.",
    "The sequence is from Malus domestica (apple) HAL3, a plant protein; the 214-aa length matches the bacterial-type PPCDC fold rather than the longer eukaryotic PPCDC, which is consistent with the annotation but requires family-level knowledge to appreciate.",
    "Reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what a model could infer from the sequence and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and mechanistically distinct molecular functions. ATP hydrolysis, potassium channel regulation, peroxidase inhibition, and phosphopantothenoylcysteine decarboxylase activity require mutually incompatible structural features. The sequence is compatible with only one of these four functions, so no two options are simultaneously defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A498JQK2 (sequence sha256 matched) annotates this protein as Phosphopantothenoylcysteine decarboxylase HAL3 (EC 4.1.1.36) with GO:0004633 'phosphopantothenoylcysteine decarboxylase activity' supported by IDA (Inferred by Direct Assay) evidence from PubMed:32761275. The catalytic activity, function, and EC number are all confirmed by experimental (ECO:0000269) evidence. The GO term definition in GO1 exactly matches option B.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H1", "H3", "H4", "H6", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A, C, and D each require specific structural features absent from this 214-aa sequence: (A) ATP hydrolysis requires a Walker A/P-loop motif (GxxxxGK[T/S]) and associated nucleotide-binding architecture not present; (C) potassium channel regulator activity requires channel-interacting regulatory domains (e.g., TID/RID domains) absent here; (D) peroxidase inhibitor activity requires specific peroxidase-binding surfaces not evident. The sequence shows glycine-rich regions (e.g., 'GSVAA') and an overall fold consistent with an FMN-dependent decarboxylase family (PF03746), making B the only option compatible with the observed sequence architecture. Elimination of A, C, D by their required structural prerequisites, combined with FMN-binding-like features in the sequence, provides a defensible reasoning path to B.",
    "missing_item_specific_fact": "Positive identification of the exact PPCDC family (vs. other FMN-dependent enzymes) relies on family-level motif recognition that borders on database lookup; however, the elimination argument for A, C, D is independently valid.",
    "reason": "A model with general knowledge of enzyme structural requirements can eliminate ATPase (no P-loop), potassium channel regulator (no channel-regulatory domain), and peroxidase inhibitor (no binding domain) from a 214-aa sequence lacking these features. The remaining option B is consistent with the observed FMN-binding-like motifs and family-appropriate length. This constitutes a meaningful biological reasoning chain, though the positive identification of PPCDC specifically rather than 'some FMN-dependent enzyme' adds a lookup element."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and mechanistically distinct molecular functions. ATP hydrolysis, potassium channel regulation, peroxidase inhibition, and phosphopantothenoylcysteine decarboxylase activity require mutually incompatible structural features. The sequence is compatible with only one of these four functions, so no two options are simultaneously defensible."
  },
  "important_caveats": [
    "The positive identification of PPCDC (as opposed to any FMN-dependent enzyme) from sequence alone is at the boundary of family-level recognition and database lookup; the elimination argument for A/C/D is stronger than the positive argument for B.",
    "The GO:0010181 (FMN binding) annotation is only IEA:TreeGrafter (computational), not experimental, so the FMN-dependence inference from the sequence is itself an inference.",
    "The sequence is from Malus domestica (apple) HAL3, a plant protein; the 214-aa length matches the bacterial-type PPCDC fold rather than the longer eukaryotic PPCDC, which is consistent with the annotation but requires family-level knowledge to appreciate.",
    "Reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what a model could infer from the sequence and general biology."
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

**Accession:** `A0A498JQK2` (recovered from dataset image-path metadata, not original question text).  
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
"A0A498JQK2"
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32761275","source":"PubMed"}],"value":"Halotolerance protein 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32761275","source":"PubMed"}],"value":"MdHAL3"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32761275","source":"PubMed"}],"value":"4.1.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Phosphopantothenoylcysteine decarboxylase HAL3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32761275","source":"PubMed"}],"value":"PPCDC"}]}}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32761275","source":"PubMed"}],"value":"Involved in plant growth, and promotes salt and osmotic tolerance, probably via coenzyme A (CoA) accumulation and endogenous proline accumulation (PubMed:32761275). Catalyzes the decarboxylation of 4'-phosphopantothenoylcysteine to 4'-phosphopantetheine, a key step in coenzyme A biosynthesis (PubMed:32761275). Required for roots development (PubMed:32761275)"}]}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"32761275","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:16794"}}],"reaction":{"ecNumber":"4.1.1.36","evidences":[{"evidenceCode":"ECO:0000269","id":"32761275","source":"PubMed"}],"name":"N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:16793"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:59458"},{"database":"ChEBI","id":"CHEBI:61723"}]}}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.295142+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"32761275","source":"PubMed"}],"id":"GO:0004633","properties":[{"key":"GoTerm","value":"F:phosphopantothenoylcysteine decarboxylase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:31.570388+00:00.  

```text
ID   HAL3_MALDO              Reviewed;         214 AA.
AC   A0A498JQK2;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUN-2019, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3 {ECO:0000305};
DE            Short=PPCDC {ECO:0000303|PubMed:32761275};
DE            EC=4.1.1.36 {ECO:0000269|PubMed:32761275};
DE   AltName: Full=Halotolerance protein 3 {ECO:0000303|PubMed:32761275};
DE            Short=MdHAL3 {ECO:0000303|PubMed:32761275};
GN   Name=HAL3 {ECO:0000303|PubMed:32761275};
GN   ORFNames=DVH24_008624 {ECO:0000312|EMBL:RXH96124.1};
OS   Malus domestica (Apple) (Pyrus malus).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   rosids; fabids; Rosales; Rosaceae; Amygdaloideae; Maleae; Malus.
OX   NCBI_TaxID=3750;
```

Source SHA-256: `0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)  
**Locator:** `lines 38-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:31.570388+00:00.  

```text
CC   -!- FUNCTION: Involved in plant growth, and promotes salt and osmotic
CC       tolerance, probably via coenzyme A (CoA) accumulation and endogenous
CC       proline accumulation (PubMed:32761275). Catalyzes the decarboxylation
CC       of 4'-phosphopantothenoylcysteine to 4'-phosphopantetheine, a key step
CC       in coenzyme A biosynthesis (PubMed:32761275). Required for roots
CC       development (PubMed:32761275). {ECO:0000269|PubMed:32761275}.
```

Source SHA-256: `0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)  
**Locator:** `lines 44-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:31.570388+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-
CC         phosphopantetheine + CO2; Xref=Rhea:RHEA:16793, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:16526, ChEBI:CHEBI:59458, ChEBI:CHEBI:61723; EC=4.1.1.36;
CC         Evidence={ECO:0000269|PubMed:32761275};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16794;
CC         Evidence={ECO:0000269|PubMed:32761275};
```

Source SHA-256: `0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)  
**Locator:** `lines 85-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:31.570388+00:00.  

```text
DR   GO; GO:0004633; F:phosphopantothenoylcysteine decarboxylase activity; IDA:UniProtKB.
```

Source SHA-256: `0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 45927-45946`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004633
name: phosphopantothenoylcysteine decarboxylase activity
namespace: molecular_function
def: "Catalysis of the reaction: N-[(R)-4-phosphonatopantothenoyl]-L-cysteinate + H+ = CO2 + pantetheine 4'-phosphate." [EC:4.1.1.36, RHEA:16793]
synonym: "4-phosphopantothenoyl-L-cysteine decarboxylase activity" RELATED [EC:4.1.1.36]
synonym: "4-phosphopantotheoylcysteine decarboxylase activity" RELATED [EC:4.1.1.36]
synonym: "N-((R)-4'-phosphopantothenoyl)-L-cysteine carboxy-lyase activity" RELATED [EC:4.1.1.36]
synonym: "N-[(R)-4'-phosphopantothenoyl]-L-cysteine carboxy-lyase (pantotheine-4'-phosphate-forming)" RELATED [EC:4.1.1.36]
synonym: "N-[(R)-4'-phosphopantothenoyl]-L-cysteine carboxy-lyase activity" RELATED [EC:4.1.1.36]
synonym: "PPC-decarboxylase activity" RELATED [EC:4.1.1.36]
xref: EC:4.1.1.36
xref: KEGG_REACTION:R03269
xref: MetaCyc:P-PANTOCYSDECARB-RXN
xref: Reactome:R-HSA-196840 "3xPPCDC:3FMN decarboxylates PPC"
xref: RHEA:16793
is_a: GO:0016831 ! carboxy-lyase activity
property_value: skos:exactMatch EC:4.1.1.36
property_value: skos:exactMatch RHEA:16793

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
