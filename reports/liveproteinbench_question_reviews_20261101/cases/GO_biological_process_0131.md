# GO_biological_process_0131

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — fatty acid beta-oxidation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSGHIRVLELNRPKARNAISRALLASLREEVHSIARQYDAQTGEEIPTPSWNKRFGGIAGDSEKGPTRALVLASAVESSFCAGADLKERRGFTQEETNEFLANLRSTFAALDALPIPTISAISSRALGGGLELALCTHFRVLTSNAIVSLPETRLGIIPGAGGTHRLPRLIGLGRARDMIVTGRAVSGAEAYFLGLADRLVEVLPPDEQEAADTTDKDAALLSAAREAALTEAVRLASQICEGGPIGIRAALQAVQAPSQETENKMYERVIGTEDRNEALKAFAEKRKPVFKGR

[Multiple Choices]
A. endomitotic cell cycle
B. carboxylic acid metabolic process
C. fatty acid beta-oxidation
D. gluconeogenesis
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

### Expected-answer support: contradicted

> The sequence-matched UniProt record identifies the protein as mitochondrial methylglutaconyl-CoA hydratase, acting in leucine degradation. That supports branched-chain amino-acid catabolism, not fatty-acid beta-oxidation. The beta-oxidation annotation is explicitly computational (IEA:TreeGrafter) and conflicts with the stated enzyme function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> There is no clear sequence-only feature in the supplied input that establishes this particular enzyme's substrate or pathway. Once its methylglutaconyl-CoA hydratase activity is known, leucine degradation—and broadly carboxylic-acid metabolism—fits better than fatty-acid beta-oxidation.


**Missing item-specific fact**

> The protein-specific identity and activity as methylglutaconyl-CoA hydratase in leucine degradation, which is not supplied in the question.


**Reason**

> Choosing among the metabolic options requires identifying the sequence-specific enzyme function; general sequence inspection does not meaningfully establish that function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B"
]
```

> Carboxylic acid metabolic process is a broad parent category that includes branched-chain amino-acid metabolism and catabolism in the supplied ontology paths. It is less specific than the protein's actual leucine-catabolic role, but is biologically defensible among the choices. C has a computational annotation, but it conflicts with the sequence-matched functional description.


### Important caveats

- The functional description cites similarity evidence for the enzyme reaction; the cited paper is associated with phenotypic and mitochondrial effects, not presented here as a direct assay of that reaction.
- The beta-oxidation GO annotation is computational, not experimental evidence, and the exact author annotation snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "There is no clear sequence-only feature in the supplied input that establishes this particular enzyme's substrate or pathway. Once its methylglutaconyl-CoA hydratase activity is known, leucine degradation—and broadly carboxylic-acid metabolism—fits better than fatty-acid beta-oxidation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and activity as methylglutaconyl-CoA hydratase in leucine degradation, which is not supplied in the question.",
    "reason": "Choosing among the metabolic options requires identifying the sequence-specific enzyme function; general sequence inspection does not meaningfully establish that function."
  },
  "case_id": "GO_biological_process_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched UniProt record identifies the protein as mitochondrial methylglutaconyl-CoA hydratase, acting in leucine degradation. That supports branched-chain amino-acid catabolism, not fatty-acid beta-oxidation. The beta-oxidation annotation is explicitly computational (IEA:TreeGrafter) and conflicts with the stated enzyme function."
  },
  "important_caveats": [
    "The functional description cites similarity evidence for the enzyme reaction; the cited paper is associated with phenotypic and mitochondrial effects, not presented here as a direct assay of that reaction.",
    "The beta-oxidation GO annotation is computational, not experimental evidence, and the exact author annotation snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B"
    ],
    "reason": "Carboxylic acid metabolic process is a broad parent category that includes branched-chain amino-acid metabolism and catabolism in the supplied ontology paths. It is less specific than the protein's actual leucine-catabolic role, but is biologically defensible among the choices. C has a computational annotation, but it conflicts with the sequence-matched functional description."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0131",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched UniProt record identifies the protein as mitochondrial methylglutaconyl-CoA hydratase, acting in leucine degradation. That supports branched-chain amino-acid catabolism, not fatty-acid beta-oxidation. The beta-oxidation annotation is explicitly computational (IEA:TreeGrafter) and conflicts with the stated enzyme function.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "There is no clear sequence-only feature in the supplied input that establishes this particular enzyme's substrate or pathway. Once its methylglutaconyl-CoA hydratase activity is known, leucine degradation—and broadly carboxylic-acid metabolism—fits better than fatty-acid beta-oxidation.",
    "missing_item_specific_fact": "The protein-specific identity and activity as methylglutaconyl-CoA hydratase in leucine degradation, which is not supplied in the question.",
    "reason": "Choosing among the metabolic options requires identifying the sequence-specific enzyme function; general sequence inspection does not meaningfully establish that function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B"],
    "reason": "Carboxylic acid metabolic process is a broad parent category that includes branched-chain amino-acid metabolism and catabolism in the supplied ontology paths. It is less specific than the protein's actual leucine-catabolic role, but is biologically defensible among the choices. C has a computational annotation, but it conflicts with the sequence-matched functional description."
  },
  "important_caveats": [
    "The functional description cites similarity evidence for the enzyme reaction; the cited paper is associated with phenotypic and mitochondrial effects, not presented here as a direct assay of that reaction.",
    "The beta-oxidation GO annotation is computational, not experimental evidence, and the exact author annotation snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein (G4N954, AUH1_PYRO7) is experimentally characterized (PubMed:32431008, ECO:0000269) as a 3-methylglutaconyl-CoA hydratase (EC 4.2.1.18) that catalyzes the fifth step of the L-leucine degradation pathway. The UniProt PATHWAY annotation explicitly states 'Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3' (ECO:0000305|PubMed:32431008). The GO:0006635 (fatty acid beta-oxidation) annotation carries evidence code IEA:TreeGrafter, a purely computational phylogenetic propagation that appears to be an error arising from structural homology to enoyl-CoA hydratase within the crotonase superfamily. The experimental evidence and UniPathway annotation (GO:0006552, L-leucine catabolic process) directly contradict the claim that this protein's primary biological process is fatty acid beta-oxidation. Its actual primary role is in branched-chain amino acid (leucine) catabolism.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable crotonase-superfamily motif (the 'GADLKERRGFTQEE' region), which is shared by enoyl-CoA hydratase (fatty acid beta-oxidation) and methylglutaconyl-CoA hydratase (leucine degradation). From the sequence alone, a model can identify the superfamily but cannot reliably determine which specific sub-pathway the enzyme serves. Distinguishing these requires knowledge of the specific protein identity (AUH1 vs. enoyl-CoA hydratase) or its substrate specificity, which is not derivable from general biological reasoning on the bare sequence.


**Missing item-specific fact**

> The specific identity of this protein as methylglutaconyl-CoA hydratase (AUH1) in the leucine degradation pathway, rather than an enoyl-CoA hydratase in fatty acid beta-oxidation. Additionally, the benchmark's 'correct' answer relies on an IEA:TreeGrafter annotation that contradicts the experimentally verified pathway, so even with lookup, the 'correct' answer is not the biologically accurate one.


**Reason**

> Recognizing the crotonase superfamily fold from sequence is possible, but assigning the specific biological process (beta-oxidation vs. leucine catabolism) requires protein-specific knowledge. The expected answer C is further problematic because it is supported only by a computational TreeGrafter annotation that contradicts the experimental evidence placing this enzyme in leucine degradation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Option B (carboxylic acid metabolic process, GO:0019752) is an is_a ancestor of both L-leucine catabolic process (GO:0006552→GO:0006551→GO:0009081→GO:0019752) and fatty acid beta-oxidation (GO:0006635→GO:0009062→GO:0006631→GO:0032787→GO:0019752). Since the protein's verified function is in leucine catabolism, B is a correct ancestor term. Option C is supported only by a questionable TreeGrafter annotation. The question asks for the 'primary biological process,' but the true primary process (L-leucine catabolic process) is not among the choices, making both B and C defensible depending on interpretation.


### Important caveats

- The GO:0006635 annotation is IEA:TreeGrafter (computational, not experimental) and appears to be an erroneous propagation from structural similarity to enoyl-CoA hydratase within the crotonase superfamily.
- The experimentally verified function (PubMed:32431008, ECO:0000269) is 3-methylglutaconyl-CoA hydratase in L-leucine degradation, not fatty acid beta-oxidation.
- The UniProt entry was first publicly released 2025-06-18; the benchmark's author source snapshot is unknown, but the sequence has been unchanged since 2011.
- The correct GO term (GO:0006552, L-leucine catabolic process) is not offered as a choice, forcing an imperfect answer.
- Option B (carboxylic acid metabolic process) is a valid ancestor of the protein's actual pathway and cannot be excluded as incorrect.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable crotonase-superfamily motif (the 'GADLKERRGFTQEE' region), which is shared by enoyl-CoA hydratase (fatty acid beta-oxidation) and methylglutaconyl-CoA hydratase (leucine degradation). From the sequence alone, a model can identify the superfamily but cannot reliably determine which specific sub-pathway the enzyme serves. Distinguishing these requires knowledge of the specific protein identity (AUH1 vs. enoyl-CoA hydratase) or its substrate specificity, which is not derivable from general biological reasoning on the bare sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as methylglutaconyl-CoA hydratase (AUH1) in the leucine degradation pathway, rather than an enoyl-CoA hydratase in fatty acid beta-oxidation. Additionally, the benchmark's 'correct' answer relies on an IEA:TreeGrafter annotation that contradicts the experimentally verified pathway, so even with lookup, the 'correct' answer is not the biologically accurate one.",
    "reason": "Recognizing the crotonase superfamily fold from sequence is possible, but assigning the specific biological process (beta-oxidation vs. leucine catabolism) requires protein-specific knowledge. The expected answer C is further problematic because it is supported only by a computational TreeGrafter annotation that contradicts the experimental evidence placing this enzyme in leucine degradation."
  },
  "case_id": "GO_biological_process_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The protein (G4N954, AUH1_PYRO7) is experimentally characterized (PubMed:32431008, ECO:0000269) as a 3-methylglutaconyl-CoA hydratase (EC 4.2.1.18) that catalyzes the fifth step of the L-leucine degradation pathway. The UniProt PATHWAY annotation explicitly states 'Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3' (ECO:0000305|PubMed:32431008). The GO:0006635 (fatty acid beta-oxidation) annotation carries evidence code IEA:TreeGrafter, a purely computational phylogenetic propagation that appears to be an error arising from structural homology to enoyl-CoA hydratase within the crotonase superfamily. The experimental evidence and UniPathway annotation (GO:0006552, L-leucine catabolic process) directly contradict the claim that this protein's primary biological process is fatty acid beta-oxidation. Its actual primary role is in branched-chain amino acid (leucine) catabolism."
  },
  "important_caveats": [
    "The GO:0006635 annotation is IEA:TreeGrafter (computational, not experimental) and appears to be an erroneous propagation from structural similarity to enoyl-CoA hydratase within the crotonase superfamily.",
    "The experimentally verified function (PubMed:32431008, ECO:0000269) is 3-methylglutaconyl-CoA hydratase in L-leucine degradation, not fatty acid beta-oxidation.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark's author source snapshot is unknown, but the sequence has been unchanged since 2011.",
    "The correct GO term (GO:0006552, L-leucine catabolic process) is not offered as a choice, forcing an imperfect answer.",
    "Option B (carboxylic acid metabolic process) is a valid ancestor of the protein's actual pathway and cannot be excluded as incorrect."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Option B (carboxylic acid metabolic process, GO:0019752) is an is_a ancestor of both L-leucine catabolic process (GO:0006552→GO:0006551→GO:0009081→GO:0019752) and fatty acid beta-oxidation (GO:0006635→GO:0009062→GO:0006631→GO:0032787→GO:0019752). Since the protein's verified function is in leucine catabolism, B is a correct ancestor term. Option C is supported only by a questionable TreeGrafter annotation. The question asks for the 'primary biological process,' but the true primary process (L-leucine catabolic process) is not among the choices, making both B and C defensible depending on interpretation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0131",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein (G4N954, AUH1_PYRO7) is experimentally characterized (PubMed:32431008, ECO:0000269) as a 3-methylglutaconyl-CoA hydratase (EC 4.2.1.18) that catalyzes the fifth step of the L-leucine degradation pathway. The UniProt PATHWAY annotation explicitly states 'Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3' (ECO:0000305|PubMed:32431008). The GO:0006635 (fatty acid beta-oxidation) annotation carries evidence code IEA:TreeGrafter, a purely computational phylogenetic propagation that appears to be an error arising from structural homology to enoyl-CoA hydratase within the crotonase superfamily. The experimental evidence and UniPathway annotation (GO:0006552, L-leucine catabolic process) directly contradict the claim that this protein's primary biological process is fatty acid beta-oxidation. Its actual primary role is in branched-chain amino acid (leucine) catabolism.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable crotonase-superfamily motif (the 'GADLKERRGFTQEE' region), which is shared by enoyl-CoA hydratase (fatty acid beta-oxidation) and methylglutaconyl-CoA hydratase (leucine degradation). From the sequence alone, a model can identify the superfamily but cannot reliably determine which specific sub-pathway the enzyme serves. Distinguishing these requires knowledge of the specific protein identity (AUH1 vs. enoyl-CoA hydratase) or its substrate specificity, which is not derivable from general biological reasoning on the bare sequence.",
    "missing_item_specific_fact": "The specific identity of this protein as methylglutaconyl-CoA hydratase (AUH1) in the leucine degradation pathway, rather than an enoyl-CoA hydratase in fatty acid beta-oxidation. Additionally, the benchmark's 'correct' answer relies on an IEA:TreeGrafter annotation that contradicts the experimentally verified pathway, so even with lookup, the 'correct' answer is not the biologically accurate one.",
    "reason": "Recognizing the crotonase superfamily fold from sequence is possible, but assigning the specific biological process (beta-oxidation vs. leucine catabolism) requires protein-specific knowledge. The expected answer C is further problematic because it is supported only by a computational TreeGrafter annotation that contradicts the experimental evidence placing this enzyme in leucine degradation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Option B (carboxylic acid metabolic process, GO:0019752) is an is_a ancestor of both L-leucine catabolic process (GO:0006552→GO:0006551→GO:0009081→GO:0019752) and fatty acid beta-oxidation (GO:0006635→GO:0009062→GO:0006631→GO:0032787→GO:0019752). Since the protein's verified function is in leucine catabolism, B is a correct ancestor term. Option C is supported only by a questionable TreeGrafter annotation. The question asks for the 'primary biological process,' but the true primary process (L-leucine catabolic process) is not among the choices, making both B and C defensible depending on interpretation."
  },
  "important_caveats": [
    "The GO:0006635 annotation is IEA:TreeGrafter (computational, not experimental) and appears to be an erroneous propagation from structural similarity to enoyl-CoA hydratase within the crotonase superfamily.",
    "The experimentally verified function (PubMed:32431008, ECO:0000269) is 3-methylglutaconyl-CoA hydratase in L-leucine degradation, not fatty acid beta-oxidation.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark's author source snapshot is unknown, but the sequence has been unchanged since 2011.",
    "The correct GO term (GO:0006552, L-leucine catabolic process) is not offered as a choice, forcing an imperfect answer.",
    "Option B (carboxylic acid metabolic process) is a valid ancestor of the protein's actual pathway and cannot be excluded as incorrect."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `mixed_annotations_require_qualification`.

> C5/H3 describe the leucine-degradation reaction by similarity, C6/H4 list leucine degradation, and C7/H6 also explicitly assign fatty-acid beta-oxidation via IEA:TreeGrafter.

**Remaining uncertainty:** The experimental citation in the function block also concerns growth/mitochondrial phenotypes; do not portray the similarity-transferred reaction as a directly assayed exclusion of beta-oxidation.

Evidence checked: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `G4N954` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"32431008","source":"PubMed"}],"value":"4.2.1.18"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32431008","source":"PubMed"}],"value":"Methylglutaconyl-CoA hydratase 1, mitochondrial"}}}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q13825","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"32431008","source":"PubMed"}],"value":"3-methylglutaconyl-CoA hydratase that catalyzes the fifth step in the leucine degradation pathway, the reversible hydration of 3-methylglutaconyl-CoA (3-MG-CoA) to 3-hydroxy-3-methylglutaryl-CoA (HMG-CoA) (By similarity). Involved in vegetative growth, conidiation and in the stress response (PubMed:32431008). Controls mitochondrial morphology and mitophagy, which are critical for the infectious growth of the pathogen (PubMed:32431008)"}]}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"32431008","source":"PubMed"}],"value":"Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3"}]}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"database":"GO","id":"GO:0006635","properties":[{"key":"GoTerm","value":"P:fatty acid beta-oxidation"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"database":"GO","id":"GO:0006552","properties":[{"key":"GoTerm","value":"P:L-leucine catabolic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniPathway"}]}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 36-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
CC   -!- FUNCTION: 3-methylglutaconyl-CoA hydratase that catalyzes the fifth
CC       step in the leucine degradation pathway, the reversible hydration of 3-
CC       methylglutaconyl-CoA (3-MG-CoA) to 3-hydroxy-3-methylglutaryl-CoA (HMG-
CC       CoA) (By similarity). Involved in vegetative growth, conidiation and in
CC       the stress response (PubMed:32431008). Controls mitochondrial
CC       morphology and mitophagy, which are critical for the infectious growth
CC       of the pathogen (PubMed:32431008). {ECO:0000250|UniProtKB:Q13825,
CC       ECO:0000269|PubMed:32431008}.
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 49-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
CC   -!- PATHWAY: Amino-acid degradation; L-leucine degradation; (S)-3-hydroxy-
CC       3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3.
CC       {ECO:0000305|PubMed:32431008}.
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 83-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
DR   GO; GO:0009083; P:branched-chain amino acid catabolic process; IEA:UniProtKB-KW.
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 84-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
DR   GO; GO:0006635; P:fatty acid beta-oxidation; IEA:TreeGrafter.
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
