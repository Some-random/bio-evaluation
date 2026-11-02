# GO_molecular_function_0030

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPISIPKGEKLMDLLSMKGKVTIVTGASGPRGMGIEAARGIAEMGGNVALTYAGRKEGGEKNAAALEKEYGIKAKAYKLDVANYESCCQLVKDVIADFGQIDAFVANAGKTADSGVLDGEISAFEEVIQTDLLGVAYCAKAVGHHFKERQTGSFVITASMSGHIANFPQEQTSYNVAKAGCIHMARSLANEWRDFARVNSISPGYIDTGLSDFVDKETQKLWHSMIPMGRDGDAKELKAAYVYFCSDASTYTTGSDLVIDGGYCAR

[Multiple Choices]
A. glycolipid mannosyltransferase activity
B. transcription coregulator activity
C. cysteine desulfurase activity
D. oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor
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

### Expected-answer support: contradicted

> The exact sequence match is annotated as an NADP-dependent mannitol dehydrogenase, catalyzing D-mannitol + NADP(+) = D-fructose + NADPH + H(+). That reaction uses NADP(+) as the electron acceptor, not oxygen as required by option D. The D-term annotation is computational (IEA:TreeGrafter), whereas the cited catalytic activity has ECO:0000305 evidence.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich sequence is compatible with a nucleotide-binding oxidoreductase, making an enzyme more plausible than a transcription coregulator. But that general clue does not establish oxygen as the acceptor or distinguish the protein's actual substrate-specific activity.


**Missing item-specific fact**

> The protein-specific catalytic reaction: mannitol/fructose interconversion with NADP(+)/NADPH, rather than an oxygen-accepting NAD(P)H oxidoreductase reaction.


**Reason**

> The sequence alone does not supply enough evidence for the precise acceptor specified in D. Identifying the enzyme's reaction requires protein-specific functional information; moreover, the characterized reaction does not match D's wording.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the options accurately states the supported mannitol dehydrogenase activity. D is broadly oxidoreductase-related, but its oxygen-acceptor specification conflicts with the reported NADP-dependent reaction; A, B, and C do not describe that reaction.


### Important caveats

- The reviewer-only UniProt records match the supplied 266-aa sequence, but the author's exact source snapshot is unknown.
- The catalytic reaction evidence is cited to a publication but was not independently checked here; the GO annotation supporting D is explicitly computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich sequence is compatible with a nucleotide-binding oxidoreductase, making an enzyme more plausible than a transcription coregulator. But that general clue does not establish oxygen as the acceptor or distinguish the protein's actual substrate-specific activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic reaction: mannitol/fructose interconversion with NADP(+)/NADPH, rather than an oxygen-accepting NAD(P)H oxidoreductase reaction.",
    "reason": "The sequence alone does not supply enough evidence for the precise acceptor specified in D. Identifying the enzyme's reaction requires protein-specific functional information; moreover, the characterized reaction does not match D's wording."
  },
  "case_id": "GO_molecular_function_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "C8",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The exact sequence match is annotated as an NADP-dependent mannitol dehydrogenase, catalyzing D-mannitol + NADP(+) = D-fructose + NADPH + H(+). That reaction uses NADP(+) as the electron acceptor, not oxygen as required by option D. The D-term annotation is computational (IEA:TreeGrafter), whereas the cited catalytic activity has ECO:0000305 evidence."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied 266-aa sequence, but the author's exact source snapshot is unknown.",
    "The catalytic reaction evidence is cited to a publication but was not independently checked here; the GO annotation supporting D is explicitly computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the options accurately states the supported mannitol dehydrogenase activity. D is broadly oxidoreductase-related, but its oxygen-acceptor specification conflicts with the reported NADP-dependent reaction; A, B, and C do not describe that reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0030",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The exact sequence match is annotated as an NADP-dependent mannitol dehydrogenase, catalyzing D-mannitol + NADP(+) = D-fructose + NADPH + H(+). That reaction uses NADP(+) as the electron acceptor, not oxygen as required by option D. The D-term annotation is computational (IEA:TreeGrafter), whereas the cited catalytic activity has ECO:0000305 evidence.",
    "evidence_ids": ["C4", "C6", "C8", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich sequence is compatible with a nucleotide-binding oxidoreductase, making an enzyme more plausible than a transcription coregulator. But that general clue does not establish oxygen as the acceptor or distinguish the protein's actual substrate-specific activity.",
    "missing_item_specific_fact": "The protein-specific catalytic reaction: mannitol/fructose interconversion with NADP(+)/NADPH, rather than an oxygen-accepting NAD(P)H oxidoreductase reaction.",
    "reason": "The sequence alone does not supply enough evidence for the precise acceptor specified in D. Identifying the enzyme's reaction requires protein-specific functional information; moreover, the characterized reaction does not match D's wording."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the options accurately states the supported mannitol dehydrogenase activity. D is broadly oxidoreductase-related, but its oxygen-acceptor specification conflicts with the reported NADP-dependent reaction; A, B, and C do not describe that reaction."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied 266-aa sequence, but the author's exact source snapshot is unknown.",
    "The catalytic reaction evidence is cited to a publication but was not independently checked here; the GO annotation supporting D is explicitly computational."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein is experimentally characterized (ECO:0000269, PubMed:32003433) as NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, catalyzing D-mannitol + NADP(+) = D-fructose + NADPH + H(+). GO:0050664 is defined as 'Catalysis of an oxidation-reduction (redox) reaction in which NADH or NADPH acts as a hydrogen or electron donor and reduces an oxygen molecule' (EC 1.6.3.-). This protein's reaction involves no oxygen as acceptor; NADP+ is the electron acceptor, placing it in EC 1.1.1.- (acting on CH-OH group, NAD/NADP as acceptor), not EC 1.6.3.-. The correct specific annotation is GO:0050085 (mannitol 2-dehydrogenase (NADP+) activity, IEA:UniProtKB-EC). The GO:0050664 annotation is an IEA:TreeGrafter computational inference that contradicts the experimental EC assignment and the GO term's own definition.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [GO3](#evidence-go3), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A Rossmann-fold-like motif (GxGxxG in 'GASGPRGMGIE') and overall 266-aa dehydrogenase architecture allow elimination of A (glycosyltransferase), B (transcription coregulator), and C (PLP-dependent cysteine desulfurase), leaving D as the only oxidoreductase option. However, arriving at the specific GO:0050664 subclass ('acting on NAD(P)H, oxygen as acceptor', EC 1.6.3.-) rather than the correct subclass ('acting on CH-OH group, NAD or NADP as acceptor', EC 1.1.1.-) cannot be derived from sequence reasoning alone.


**Missing item-specific fact**

> The TreeGrafter IEA annotation of GO:0050664 to this protein (C8/H6), which is a computational phylogenetic propagation that is inconsistent with the experimentally determined EC 1.1.1.138. Without this specific (erroneous) database annotation, no sequence-based reasoning would select GO:0050664 over the correct EC 1.1.1.- branch terms.


**Reason**

> Elimination reasoning narrows to 'some oxidoreductase activity' but cannot distinguish GO:0050664 (EC 1.6.3.- oxidase) from GO:0050085 or its EC 1.1.1.- parents. Selection of the exact GO term in D depends on the specific TreeGrafter annotation present in the database, not on general biological reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only D falls within the oxidoreductase superfamily, so elimination reasoning uniquely selects D. However, D's specific GO term is scientifically incorrect for this protein; the question has no fully correct option. The ambiguity is not between two defensible choices but between a technically wrong answer (D) and clearly wrong answers (A, B, C).


### Important caveats

- The GO:0050664 annotation is IEA:TreeGrafter (computational), while the protein's actual function is supported by experimental evidence (ECO:0000269, PubMed:32003433). The expected answer rests on a computational inference contradicted by experimental data.
- The protein's correct molecular function is 'mannitol 2-dehydrogenase (NADP+) activity' (GO:0050085, IEA:UniProtKB-EC), not 'oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor' (GO:0050664, IEA:TreeGrafter).
- GO:0050664 and GO:0050085 are in different branches of the oxidoreductase hierarchy (EC 1.6.3.- vs EC 1.1.1.-); neither is an ancestor of the other.
- The benchmark question effectively tests whether a model reproduces a specific database annotation (including a TreeGrafter error) rather than whether it can correctly classify molecular function from sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A Rossmann-fold-like motif (GxGxxG in 'GASGPRGMGIE') and overall 266-aa dehydrogenase architecture allow elimination of A (glycosyltransferase), B (transcription coregulator), and C (PLP-dependent cysteine desulfurase), leaving D as the only oxidoreductase option. However, arriving at the specific GO:0050664 subclass ('acting on NAD(P)H, oxygen as acceptor', EC 1.6.3.-) rather than the correct subclass ('acting on CH-OH group, NAD or NADP as acceptor', EC 1.1.1.-) cannot be derived from sequence reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The TreeGrafter IEA annotation of GO:0050664 to this protein (C8/H6), which is a computational phylogenetic propagation that is inconsistent with the experimentally determined EC 1.1.1.138. Without this specific (erroneous) database annotation, no sequence-based reasoning would select GO:0050664 over the correct EC 1.1.1.- branch terms.",
    "reason": "Elimination reasoning narrows to 'some oxidoreductase activity' but cannot distinguish GO:0050664 (EC 1.6.3.- oxidase) from GO:0050085 or its EC 1.1.1.- parents. Selection of the exact GO term in D depends on the specific TreeGrafter annotation present in the database, not on general biological reasoning from the sequence."
  },
  "case_id": "GO_molecular_function_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "GO3",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The protein is experimentally characterized (ECO:0000269, PubMed:32003433) as NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, catalyzing D-mannitol + NADP(+) = D-fructose + NADPH + H(+). GO:0050664 is defined as 'Catalysis of an oxidation-reduction (redox) reaction in which NADH or NADPH acts as a hydrogen or electron donor and reduces an oxygen molecule' (EC 1.6.3.-). This protein's reaction involves no oxygen as acceptor; NADP+ is the electron acceptor, placing it in EC 1.1.1.- (acting on CH-OH group, NAD/NADP as acceptor), not EC 1.6.3.-. The correct specific annotation is GO:0050085 (mannitol 2-dehydrogenase (NADP+) activity, IEA:UniProtKB-EC). The GO:0050664 annotation is an IEA:TreeGrafter computational inference that contradicts the experimental EC assignment and the GO term's own definition."
  },
  "important_caveats": [
    "The GO:0050664 annotation is IEA:TreeGrafter (computational), while the protein's actual function is supported by experimental evidence (ECO:0000269, PubMed:32003433). The expected answer rests on a computational inference contradicted by experimental data.",
    "The protein's correct molecular function is 'mannitol 2-dehydrogenase (NADP+) activity' (GO:0050085, IEA:UniProtKB-EC), not 'oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor' (GO:0050664, IEA:TreeGrafter).",
    "GO:0050664 and GO:0050085 are in different branches of the oxidoreductase hierarchy (EC 1.6.3.- vs EC 1.1.1.-); neither is an ancestor of the other.",
    "The benchmark question effectively tests whether a model reproduces a specific database annotation (including a TreeGrafter error) rather than whether it can correctly classify molecular function from sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D falls within the oxidoreductase superfamily, so elimination reasoning uniquely selects D. However, D's specific GO term is scientifically incorrect for this protein; the question has no fully correct option. The ambiguity is not between two defensible choices but between a technically wrong answer (D) and clearly wrong answers (A, B, C)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0030",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein is experimentally characterized (ECO:0000269, PubMed:32003433) as NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, catalyzing D-mannitol + NADP(+) = D-fructose + NADPH + H(+). GO:0050664 is defined as 'Catalysis of an oxidation-reduction (redox) reaction in which NADH or NADPH acts as a hydrogen or electron donor and reduces an oxygen molecule' (EC 1.6.3.-). This protein's reaction involves no oxygen as acceptor; NADP+ is the electron acceptor, placing it in EC 1.1.1.- (acting on CH-OH group, NAD/NADP as acceptor), not EC 1.6.3.-. The correct specific annotation is GO:0050085 (mannitol 2-dehydrogenase (NADP+) activity, IEA:UniProtKB-EC). The GO:0050664 annotation is an IEA:TreeGrafter computational inference that contradicts the experimental EC assignment and the GO term's own definition.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "GO3", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A Rossmann-fold-like motif (GxGxxG in 'GASGPRGMGIE') and overall 266-aa dehydrogenase architecture allow elimination of A (glycosyltransferase), B (transcription coregulator), and C (PLP-dependent cysteine desulfurase), leaving D as the only oxidoreductase option. However, arriving at the specific GO:0050664 subclass ('acting on NAD(P)H, oxygen as acceptor', EC 1.6.3.-) rather than the correct subclass ('acting on CH-OH group, NAD or NADP as acceptor', EC 1.1.1.-) cannot be derived from sequence reasoning alone.",
    "missing_item_specific_fact": "The TreeGrafter IEA annotation of GO:0050664 to this protein (C8/H6), which is a computational phylogenetic propagation that is inconsistent with the experimentally determined EC 1.1.1.138. Without this specific (erroneous) database annotation, no sequence-based reasoning would select GO:0050664 over the correct EC 1.1.1.- branch terms.",
    "reason": "Elimination reasoning narrows to 'some oxidoreductase activity' but cannot distinguish GO:0050664 (EC 1.6.3.- oxidase) from GO:0050085 or its EC 1.1.1.- parents. Selection of the exact GO term in D depends on the specific TreeGrafter annotation present in the database, not on general biological reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D falls within the oxidoreductase superfamily, so elimination reasoning uniquely selects D. However, D's specific GO term is scientifically incorrect for this protein; the question has no fully correct option. The ambiguity is not between two defensible choices but between a technically wrong answer (D) and clearly wrong answers (A, B, C)."
  },
  "important_caveats": [
    "The GO:0050664 annotation is IEA:TreeGrafter (computational), while the protein's actual function is supported by experimental evidence (ECO:0000269, PubMed:32003433). The expected answer rests on a computational inference contradicted by experimental data.",
    "The protein's correct molecular function is 'mannitol 2-dehydrogenase (NADP+) activity' (GO:0050085, IEA:UniProtKB-EC), not 'oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor' (GO:0050664, IEA:TreeGrafter).",
    "GO:0050664 and GO:0050085 are in different branches of the oxidoreductase hierarchy (EC 1.6.3.- vs EC 1.1.1.-); neither is an ancestor of the other.",
    "The benchmark question effectively tests whether a model reproduces a specific database annotation (including a TreeGrafter error) rather than whether it can correctly classify molecular function from sequence."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_definition_difference_traced`.

> C6/H4 describe mannitol plus NADP+ yielding fructose plus NADPH, while C8/H6 carry the oxygen-acceptor term via IEA:TreeGrafter.

**Remaining uncertainty:** The cited reaction is ECO:0000305 and reversible; neither direction uses oxygen as acceptor. Additional oxidase activity is not exhaustively tested by these excerpts.

Evidence checked: [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H6](#evidence-h6).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A223HDI5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 15. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32003433","source":"PubMed"}],"value":"1.1.1.138"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"NADP-dependent mannitol dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"MtDH"}]}}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32003433","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"32003433","source":"PubMed"}],"value":"Catalyzes the interconversion between D-mannitol and D-fructose (Probable). Plays a key role in liamocins biosynthesis by providing the mannitol moity that is linked to 3,5-dihydroxydecanoic acid (provided by the HR-PKS PKS1) via ester bond formation catalyzed by the esterase EST1 (PubMed:32003433)"}]}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"32003433","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:16766"}},{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000305","id":"32003433","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:16767"}}],"reaction":{"ecNumber":"1.1.1.138","evidences":[{"evidenceCode":"ECO:0000305","id":"32003433","source":"PubMed"}],"name":"D-mannitol + NADP(+) = D-fructose + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:16765"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16899"},{"database":"ChEBI","id":"CHEBI:37721"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/uniProtKBCrossReferences/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"database":"GO","id":"GO:0050085","properties":[{"key":"GoTerm","value":"F:mannitol 2-dehydrogenase (NADP+) activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"database":"GO","id":"GO:0050664","properties":[{"key":"GoTerm","value":"F:oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)  
**Locator:** `lines 46-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.627063+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the interconversion between D-mannitol and D-
CC       fructose (Probable). Plays a key role in liamocins biosynthesis by
CC       providing the mannitol moity that is linked to 3,5-dihydroxydecanoic
CC       acid (provided by the HR-PKS PKS1) via ester bond formation catalyzed
CC       by the esterase EST1 (PubMed:32003433). {ECO:0000269|PubMed:32003433,
CC       ECO:0000305|PubMed:32003433}.
```

Source SHA-256: `cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)  
**Locator:** `lines 52-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.627063+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-mannitol + NADP(+) = D-fructose + NADPH + H(+);
CC         Xref=Rhea:RHEA:16765, ChEBI:CHEBI:15378, ChEBI:CHEBI:16899,
CC         ChEBI:CHEBI:37721, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;
CC         EC=1.1.1.138; Evidence={ECO:0000305|PubMed:32003433};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16766;
CC         Evidence={ECO:0000305|PubMed:32003433};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:16767;
CC         Evidence={ECO:0000305|PubMed:32003433};
```

Source SHA-256: `cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)  
**Locator:** `lines 83-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.627063+00:00.  

```text
DR   GO; GO:0050085; F:mannitol 2-dehydrogenase (NADP+) activity; IEA:UniProtKB-EC.
```

Source SHA-256: `cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)  
**Locator:** `lines 84-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.627063+00:00.  

```text
DR   GO; GO:0050664; F:oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor; IEA:TreeGrafter.
```

Source SHA-256: `cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 318421-318430`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0050664
name: oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor
namespace: molecular_function
def: "Catalysis of an oxidation-reduction (redox) reaction in which NADH or NADPH acts as a hydrogen or electron donor and reduces an oxygen molecule." [EC:1.6.3.-]
synonym: "oxidoreductase activity, acting on NADH or NADPH, oxygen as acceptor" RELATED []
xref: EC:1.6.3.-
is_a: GO:0016651 ! oxidoreductase activity, acting on NAD(P)H
property_value: skos:exactMatch EC:1.6.3.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 30. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
