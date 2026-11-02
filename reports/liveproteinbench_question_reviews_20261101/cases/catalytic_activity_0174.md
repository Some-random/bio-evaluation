# catalytic_activity_0174

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATPSKKRCGVLGATGAVGTRFILLLSQHPLLELVAVGASDRSSGKKYRDAVRWKQSAPMPAKVADLTVRCCDPAEFSDCDIIFSGLDPDAAGEIEMAFLKANFAVFSNAKNYRLDPMVPLVVPLVNAGHIDVIPAQRKHFGLDKGMLVCNSNCAVVGLVVPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPYIPGEEGKISSEARKILGDLNSDLAGFSDQKPLQISVACNRVPVLDGHTVCASLRFVNRPPPTASQVREALREYKPEVQTLGCPSAPKMSIHVMDEVDRPQPRLDRETEGGYACTVGRIREDDSDVFDIQFVALSHNTVLGASGSSILNAESAILKGFV

[Multiple Choices]
A. L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)
B. L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)
C. 2-hydroxyspheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. a 14alpha-methyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact 362-residue sequence matches the UniProt entry annotated as aspartate-semialdehyde dehydrogenase, and that entry gives the reaction in choice B with ECO:0000269 evidence linked to a publication. This supports the key, though the evidence here is the database annotation and its cited evidence, not an independent review of the primary study.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains enzyme-like features, but the input gives no organism, enzyme-family label, or experimentally observed activity that links those features uniquely to the specific reaction in B. General sequence-based reasoning alone does not establish this substrate-product transformation.


**Missing item-specific fact**

> The sequence-specific functional assignment as aspartate-semialdehyde dehydrogenase, or equivalent evidence identifying its catalytic reaction, is absent from the model input.


**Reason**

> Choosing B requires a protein-specific functional annotation or a sufficiently distinctive known family assignment. Recognizing or retrieving the exact protein’s database entry would be lookup or memorization, not reasoning from information supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence matches the supplied sequence to an enzyme annotated with the reaction in B; none of the other listed reactions is supported for this sequence.


### Important caveats

- The reviewer-only sequence match and functional annotation were not supplied to the evaluated model.
- The cited publication is identified as evidence for catalytic activity, but its primary data were not independently retrieved or assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains enzyme-like features, but the input gives no organism, enzyme-family label, or experimentally observed activity that links those features uniquely to the specific reaction in B. General sequence-based reasoning alone does not establish this substrate-product transformation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific functional assignment as aspartate-semialdehyde dehydrogenase, or equivalent evidence identifying its catalytic reaction, is absent from the model input.",
    "reason": "Choosing B requires a protein-specific functional annotation or a sufficiently distinctive known family assignment. Recognizing or retrieving the exact protein’s database entry would be lookup or memorization, not reasoning from information supplied in the question."
  },
  "case_id": "catalytic_activity_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 362-residue sequence matches the UniProt entry annotated as aspartate-semialdehyde dehydrogenase, and that entry gives the reaction in choice B with ECO:0000269 evidence linked to a publication. This supports the key, though the evidence here is the database annotation and its cited evidence, not an independent review of the primary study."
  },
  "important_caveats": [
    "The reviewer-only sequence match and functional annotation were not supplied to the evaluated model.",
    "The cited publication is identified as evidence for catalytic activity, but its primary data were not independently retrieved or assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence matches the supplied sequence to an enzyme annotated with the reaction in B; none of the other listed reactions is supported for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 362-residue sequence matches the UniProt entry annotated as aspartate-semialdehyde dehydrogenase, and that entry gives the reaction in choice B with ECO:0000269 evidence linked to a publication. This supports the key, though the evidence here is the database annotation and its cited evidence, not an independent review of the primary study.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains enzyme-like features, but the input gives no organism, enzyme-family label, or experimentally observed activity that links those features uniquely to the specific reaction in B. General sequence-based reasoning alone does not establish this substrate-product transformation.",
    "missing_item_specific_fact": "The sequence-specific functional assignment as aspartate-semialdehyde dehydrogenase, or equivalent evidence identifying its catalytic reaction, is absent from the model input.",
    "reason": "Choosing B requires a protein-specific functional annotation or a sufficiently distinctive known family assignment. Recognizing or retrieving the exact protein’s database entry would be lookup or memorization, not reasoning from information supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence matches the supplied sequence to an enzyme annotated with the reaction in B; none of the other listed reactions is supported for this sequence."
  },
  "important_caveats": [
    "The reviewer-only sequence match and functional annotation were not supplied to the evaluated model.",
    "The cited publication is identified as evidence for catalytic activity, but its primary data were not independently retrieved or assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (SHA256 ecc9f93b...) matches UniProt A0A080WMA9 exactly. The entry is annotated as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)' supported by experimental evidence (ECO:0000269, PubMed:26869335, X-ray crystallography PDB 4ZHS/4ZIC). The expected answer B matches the annotated reaction verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 362-aa sequence contains a canonical Rossmann-fold NAD(P)-binding motif (GVLGATGAV near the N-terminus) and a catalytic Cys-Glu-Arg triad region (CNSNC…EGGYACTVGRIRE), characteristic of a simple NAD(P)-dependent dehydrogenase. This eliminates option C (ferredoxin-dependent oxidase requiring iron-sulfur cluster and membrane-association motifs absent here), option D (cytochrome P450 requiring a conserved heme-ligating Cys in an FxxGxxxCxG motif and typically 450–550 aa), and option A (tyrosine-activation chemistry involving AMP/diphosphate, inconsistent with the observed Rossmann-fold dehydrogenase architecture). Among the four choices, only B—a NADP(+)-dependent dehydrogenase with phosphoryl transfer on a small amino-aldehyde substrate—is consistent with the observed fold, size, and catalytic-residue pattern.


**Missing item-specific fact**

> Precise substrate identification (aspartate 4-semialdehyde vs. glutamate 5-semialdehyde or other semialdehydes) would require detailed active-site geometry or database annotation, but this distinction is not needed because no competing semialdehyde-dehydrogenase reaction appears among the four choices.


**Reason**

> General enzymology knowledge (Rossmann fold → NAD(P) dehydrogenase; absence of heme/ferredoxin motifs; protein size) meaningfully eliminates three of the four choices without requiring recognition of this specific Trichophyton rubrum ASADH entry. The remaining choice B is the only simple NAD(P)-dependent dehydrogenase reaction listed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different enzyme classes (aminotransferase/nucleotide-activating enzyme, NAD(P) dehydrogenase, ferredoxin oxidase, P450 monooxygenase). The sequence's Rossmann fold, size, and absence of heme or ferredoxin motifs leave only B as a defensible match.


### Important caveats

- The physiological direction of EC 1.2.1.11 is right-to-left (reduction of 4-phospho-L-aspartate to aspartate semialdehyde); the written reaction in choice B is the reverse (oxidative) direction, which is the thermodynamically unfavorable direction but is the standard EC notation. This is a convention issue, not a correctness issue.
- Distinguishing ASADH from the closely related glutamate-5-semialdehyde dehydrogenase (EC 1.2.1.41) purely from sequence is difficult; however, that alternative is not among the choices, so it does not affect answerability here.
- The evidence is experimental (ECO:0000269, X-ray crystallography at 2.55 Å in complex with NADP+), not merely computational or similarity-transferred.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 362-aa sequence contains a canonical Rossmann-fold NAD(P)-binding motif (GVLGATGAV near the N-terminus) and a catalytic Cys-Glu-Arg triad region (CNSNC…EGGYACTVGRIRE), characteristic of a simple NAD(P)-dependent dehydrogenase. This eliminates option C (ferredoxin-dependent oxidase requiring iron-sulfur cluster and membrane-association motifs absent here), option D (cytochrome P450 requiring a conserved heme-ligating Cys in an FxxGxxxCxG motif and typically 450–550 aa), and option A (tyrosine-activation chemistry involving AMP/diphosphate, inconsistent with the observed Rossmann-fold dehydrogenase architecture). Among the four choices, only B—a NADP(+)-dependent dehydrogenase with phosphoryl transfer on a small amino-aldehyde substrate—is consistent with the observed fold, size, and catalytic-residue pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise substrate identification (aspartate 4-semialdehyde vs. glutamate 5-semialdehyde or other semialdehydes) would require detailed active-site geometry or database annotation, but this distinction is not needed because no competing semialdehyde-dehydrogenase reaction appears among the four choices.",
    "reason": "General enzymology knowledge (Rossmann fold → NAD(P) dehydrogenase; absence of heme/ferredoxin motifs; protein size) meaningfully eliminates three of the four choices without requiring recognition of this specific Trichophyton rubrum ASADH entry. The remaining choice B is the only simple NAD(P)-dependent dehydrogenase reaction listed."
  },
  "case_id": "catalytic_activity_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence (SHA256 ecc9f93b...) matches UniProt A0A080WMA9 exactly. The entry is annotated as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)' supported by experimental evidence (ECO:0000269, PubMed:26869335, X-ray crystallography PDB 4ZHS/4ZIC). The expected answer B matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The physiological direction of EC 1.2.1.11 is right-to-left (reduction of 4-phospho-L-aspartate to aspartate semialdehyde); the written reaction in choice B is the reverse (oxidative) direction, which is the thermodynamically unfavorable direction but is the standard EC notation. This is a convention issue, not a correctness issue.",
    "Distinguishing ASADH from the closely related glutamate-5-semialdehyde dehydrogenase (EC 1.2.1.41) purely from sequence is difficult; however, that alternative is not among the choices, so it does not affect answerability here.",
    "The evidence is experimental (ECO:0000269, X-ray crystallography at 2.55 Å in complex with NADP+), not merely computational or similarity-transferred."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (aminotransferase/nucleotide-activating enzyme, NAD(P) dehydrogenase, ferredoxin oxidase, P450 monooxygenase). The sequence's Rossmann fold, size, and absence of heme or ferredoxin motifs leave only B as a defensible match."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (SHA256 ecc9f93b...) matches UniProt A0A080WMA9 exactly. The entry is annotated as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the catalytic activity 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)' supported by experimental evidence (ECO:0000269, PubMed:26869335, X-ray crystallography PDB 4ZHS/4ZIC). The expected answer B matches the annotated reaction verbatim.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 362-aa sequence contains a canonical Rossmann-fold NAD(P)-binding motif (GVLGATGAV near the N-terminus) and a catalytic Cys-Glu-Arg triad region (CNSNC…EGGYACTVGRIRE), characteristic of a simple NAD(P)-dependent dehydrogenase. This eliminates option C (ferredoxin-dependent oxidase requiring iron-sulfur cluster and membrane-association motifs absent here), option D (cytochrome P450 requiring a conserved heme-ligating Cys in an FxxGxxxCxG motif and typically 450–550 aa), and option A (tyrosine-activation chemistry involving AMP/diphosphate, inconsistent with the observed Rossmann-fold dehydrogenase architecture). Among the four choices, only B—a NADP(+)-dependent dehydrogenase with phosphoryl transfer on a small amino-aldehyde substrate—is consistent with the observed fold, size, and catalytic-residue pattern.",
    "missing_item_specific_fact": "Precise substrate identification (aspartate 4-semialdehyde vs. glutamate 5-semialdehyde or other semialdehydes) would require detailed active-site geometry or database annotation, but this distinction is not needed because no competing semialdehyde-dehydrogenase reaction appears among the four choices.",
    "reason": "General enzymology knowledge (Rossmann fold → NAD(P) dehydrogenase; absence of heme/ferredoxin motifs; protein size) meaningfully eliminates three of the four choices without requiring recognition of this specific Trichophyton rubrum ASADH entry. The remaining choice B is the only simple NAD(P)-dependent dehydrogenase reaction listed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (aminotransferase/nucleotide-activating enzyme, NAD(P) dehydrogenase, ferredoxin oxidase, P450 monooxygenase). The sequence's Rossmann fold, size, and absence of heme or ferredoxin motifs leave only B as a defensible match."
  },
  "important_caveats": [
    "The physiological direction of EC 1.2.1.11 is right-to-left (reduction of 4-phospho-L-aspartate to aspartate semialdehyde); the written reaction in choice B is the reverse (oxidative) direction, which is the thermodynamically unfavorable direction but is the standard EC notation. This is a convention issue, not a correctness issue.",
    "Distinguishing ASADH from the closely related glutamate-5-semialdehyde dehydrogenase (EC 1.2.1.41) purely from sequence is difficult; however, that alternative is not among the choices, so it does not affect answerability here.",
    "The evidence is experimental (ECO:0000269, X-ray crystallography at 2.55 Å in complex with NADP+), not merely computational or similarity-transferred."
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

**Accession:** `A0A080WMA9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26869335","source":"PubMed"}],"value":"TrASADH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26869335","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"26869335","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24286"}}],"reaction":{"ecNumber":"1.2.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"26869335","source":"PubMed"}],"name":"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24284"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:537519"}]}}
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:57.418115+00:00.  

```text
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:26869335};
DE   AltName: Full=TrASADH {ECO:0000303|PubMed:26869335};
```

Source SHA-256: `319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)  
**Locator:** `lines 44-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:57.418115+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-
CC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;
CC         Evidence={ECO:0000269|PubMed:26869335};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;
CC         Evidence={ECO:0000269|PubMed:26869335};
```

Source SHA-256: `319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
