# catalytic_activity_0048

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSGHIRVLELNRPKARNAISRALLASLREEVHSIARQYDAQTGEEIPTPSWNKRFGGIAGDSEKGPTRALVLASAVESSFCAGADLKERRGFTQEETNEFLANLRSTFAALDALPIPTISAISSRALGGGLELALCTHFRVLTSNAIVSLPETRLGIIPGAGGTHRLPRLIGLGRARDMIVTGRAVSGAEAYFLGLADRLVEVLPPDEQEAADTTDKDAALLSAAREAALTEAVRLASQICEGGPIGIRAALQAVQAPSQETENKMYERVIGTEDRNEALKAFAEKRKPVFKGR

[Multiple Choices]
A. N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2
B. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
C. (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O
D. cytidine(in) = cytidine(out)
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

> The supplied sequence exactly matches the 349-aa UniProt entry annotated as mitochondrial methylglutaconyl-CoA hydratase 1, and that entry assigns EC 4.2.1.18 and the reaction in choice C. This supports the key as a database annotation; the cited evidence does not establish that the reaction was directly measured experimentally.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe very different reaction classes, but the sequence alone provides no clear, general feature that identifies this particular enzyme's substrate and reaction. Recognizing the exact sequence or relying on an unstated protein-specific annotation would be lookup or memorization, not reasoning from the supplied input.


**Missing item-specific fact**

> The protein-specific functional assignment as methylglutaconyl-CoA hydratase (EC 4.2.1.18), or equivalent experimental evidence identifying its catalytic reaction.


**Reason**

> The input supplies only a sequence and candidate reactions; distinguishing the exact substrate-product transformation requires a protein-specific function assignment absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the matched database annotation specifically corresponds to C.


### Important caveats

- The supporting UniProt catalytic-activity annotation cites a paper whose title describes the enzyme as putative; the excerpts do not independently demonstrate direct experimental measurement of the reaction.
- The reviewer evidence matches the sequence but does not establish which database snapshot the benchmark author used.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe very different reaction classes, but the sequence alone provides no clear, general feature that identifies this particular enzyme's substrate and reaction. Recognizing the exact sequence or relying on an unstated protein-specific annotation would be lookup or memorization, not reasoning from the supplied input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment as methylglutaconyl-CoA hydratase (EC 4.2.1.18), or equivalent experimental evidence identifying its catalytic reaction.",
    "reason": "The input supplies only a sequence and candidate reactions; distinguishing the exact substrate-product transformation requires a protein-specific function assignment absent from the question."
  },
  "case_id": "catalytic_activity_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 349-aa UniProt entry annotated as mitochondrial methylglutaconyl-CoA hydratase 1, and that entry assigns EC 4.2.1.18 and the reaction in choice C. This supports the key as a database annotation; the cited evidence does not establish that the reaction was directly measured experimentally."
  },
  "important_caveats": [
    "The supporting UniProt catalytic-activity annotation cites a paper whose title describes the enzyme as putative; the excerpts do not independently demonstrate direct experimental measurement of the reaction.",
    "The reviewer evidence matches the sequence but does not establish which database snapshot the benchmark author used."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched database annotation specifically corresponds to C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 349-aa UniProt entry annotated as mitochondrial methylglutaconyl-CoA hydratase 1, and that entry assigns EC 4.2.1.18 and the reaction in choice C. This supports the key as a database annotation; the cited evidence does not establish that the reaction was directly measured experimentally.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe very different reaction classes, but the sequence alone provides no clear, general feature that identifies this particular enzyme's substrate and reaction. Recognizing the exact sequence or relying on an unstated protein-specific annotation would be lookup or memorization, not reasoning from the supplied input.",
    "missing_item_specific_fact": "The protein-specific functional assignment as methylglutaconyl-CoA hydratase (EC 4.2.1.18), or equivalent experimental evidence identifying its catalytic reaction.",
    "reason": "The input supplies only a sequence and candidate reactions; distinguishing the exact substrate-product transformation requires a protein-specific function assignment absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched database annotation specifically corresponds to C."
  },
  "important_caveats": [
    "The supporting UniProt catalytic-activity annotation cites a paper whose title describes the enzyme as putative; the excerpts do not independently demonstrate direct experimental measurement of the reaction.",
    "The reviewer evidence matches the sequence but does not establish which database snapshot the benchmark author used."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G4N954 (AUH1_PYRO7, Pyricularia oryzae) explicitly annotates the catalytic activity as '(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O' (EC 4.2.1.18), matching Choice C verbatim. The benchmark sequence (349 aa, SHA256 5e891c…) matches the UniProt sequence exactly. However, the evidence code is ECO:0000305 (inferred from electronic annotation), and the cited paper (PubMed:32431008) describes the gene as a 'putative 3-methylglutaconyl-CoA hydratase.' The annotation is thus a computational/inferred assignment supported by a functional-genomics study rather than direct in vitro enzymatic characterization of this specific reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options represent four fundamentally different enzyme classes: A is an oxidoreductase (histone JmjC demethylase), B is a hydrolase (α-glucosidase), C is a lyase/hydratase (EC 4.2.1.18), and D is a membrane transporter. The supplied sequence (~349 aa) contains motifs characteristic of the crotonase superfamily of hydratases/dehydratases: tandem 'GGG' and 'GAGG' glycine-rich stretches (e.g., 'GGGLELALCTHFRVLTS…', 'GAGGTHRLPRLIGLGRARDMIVTG'), a helix-rich C-terminal region with CoA-binding-like hydrophobic stretches, and an overall α/β architecture consistent with the crotonase fold. Recognizing the protein as a hydratase/lyase of the crotonase superfamily eliminates A (oxidoreductase), B (hydrolase), and D (transporter), leaving C as the only lyase reaction among the choices.


**Missing item-specific fact**

> The specific substrate identity (methylglutaconyl-CoA vs. other crotonase-superfamily substrates such as enoyl-CoA or 3-hydroxyacyl-CoA) cannot be determined from the sequence by general reasoning alone; that level of specificity depends on database annotation or detailed subfamily motif analysis. However, because no competing hydratase option is present among the distractors, the class-level identification is sufficient to select C.


**Reason**

> The question is answerable through general biological reasoning: identifying the enzyme as a hydratase/lyase (crotonase superfamily) from sequence motifs and selecting the sole lyase reaction among the four options. The specific EC-number-level substrate assignment is not derivable from the sequence, but it is not required to discriminate the given choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four distractors span four unrelated enzyme classes (oxidoreductase, hydrolase, lyase, transporter), so only one option (C) is consistent with a hydratase/lyase. No ambiguity exists among the provided choices once the general enzyme class is recognized.


### Important caveats

- The UniProt annotation for this reaction carries evidence code ECO:0000305 (inferred from electronic annotation), meaning the specific EC assignment is a computational prediction, not a direct experimental measurement of the enzymatic reaction.
- The primary paper (PubMed:32431008) describes the gene as encoding a 'putative' 3-methylglutaconyl-CoA hydratase and focuses on its role in mitochondrial dynamics and infectious growth rather than on in vitro kinetic characterization of the hydration reaction.
- The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model; the model must rely solely on the 349-aa sequence and the four choices.
- The specific substrate-level identification (methylglutaconyl-CoA vs. other CoA-ester substrates of the crotonase superfamily) is not derivable from the sequence by general reasoning; the question is answerable only because no competing hydratase option is offered.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options represent four fundamentally different enzyme classes: A is an oxidoreductase (histone JmjC demethylase), B is a hydrolase (α-glucosidase), C is a lyase/hydratase (EC 4.2.1.18), and D is a membrane transporter. The supplied sequence (~349 aa) contains motifs characteristic of the crotonase superfamily of hydratases/dehydratases: tandem 'GGG' and 'GAGG' glycine-rich stretches (e.g., 'GGGLELALCTHFRVLTS…', 'GAGGTHRLPRLIGLGRARDMIVTG'), a helix-rich C-terminal region with CoA-binding-like hydrophobic stretches, and an overall α/β architecture consistent with the crotonase fold. Recognizing the protein as a hydratase/lyase of the crotonase superfamily eliminates A (oxidoreductase), B (hydrolase), and D (transporter), leaving C as the only lyase reaction among the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (methylglutaconyl-CoA vs. other crotonase-superfamily substrates such as enoyl-CoA or 3-hydroxyacyl-CoA) cannot be determined from the sequence by general reasoning alone; that level of specificity depends on database annotation or detailed subfamily motif analysis. However, because no competing hydratase option is present among the distractors, the class-level identification is sufficient to select C.",
    "reason": "The question is answerable through general biological reasoning: identifying the enzyme as a hydratase/lyase (crotonase superfamily) from sequence motifs and selecting the sole lyase reaction among the four options. The specific EC-number-level substrate assignment is not derivable from the sequence, but it is not required to discriminate the given choices."
  },
  "case_id": "catalytic_activity_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G4N954 (AUH1_PYRO7, Pyricularia oryzae) explicitly annotates the catalytic activity as '(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O' (EC 4.2.1.18), matching Choice C verbatim. The benchmark sequence (349 aa, SHA256 5e891c…) matches the UniProt sequence exactly. However, the evidence code is ECO:0000305 (inferred from electronic annotation), and the cited paper (PubMed:32431008) describes the gene as a 'putative 3-methylglutaconyl-CoA hydratase.' The annotation is thus a computational/inferred assignment supported by a functional-genomics study rather than direct in vitro enzymatic characterization of this specific reaction."
  },
  "important_caveats": [
    "The UniProt annotation for this reaction carries evidence code ECO:0000305 (inferred from electronic annotation), meaning the specific EC assignment is a computational prediction, not a direct experimental measurement of the enzymatic reaction.",
    "The primary paper (PubMed:32431008) describes the gene as encoding a 'putative' 3-methylglutaconyl-CoA hydratase and focuses on its role in mitochondrial dynamics and infectious growth rather than on in vitro kinetic characterization of the hydration reaction.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model; the model must rely solely on the 349-aa sequence and the four choices.",
    "The specific substrate-level identification (methylglutaconyl-CoA vs. other CoA-ester substrates of the crotonase superfamily) is not derivable from the sequence by general reasoning; the question is answerable only because no competing hydratase option is offered."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four distractors span four unrelated enzyme classes (oxidoreductase, hydrolase, lyase, transporter), so only one option (C) is consistent with a hydratase/lyase. No ambiguity exists among the provided choices once the general enzyme class is recognized."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G4N954 (AUH1_PYRO7, Pyricularia oryzae) explicitly annotates the catalytic activity as '(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O' (EC 4.2.1.18), matching Choice C verbatim. The benchmark sequence (349 aa, SHA256 5e891c…) matches the UniProt sequence exactly. However, the evidence code is ECO:0000305 (inferred from electronic annotation), and the cited paper (PubMed:32431008) describes the gene as a 'putative 3-methylglutaconyl-CoA hydratase.' The annotation is thus a computational/inferred assignment supported by a functional-genomics study rather than direct in vitro enzymatic characterization of this specific reaction.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options represent four fundamentally different enzyme classes: A is an oxidoreductase (histone JmjC demethylase), B is a hydrolase (α-glucosidase), C is a lyase/hydratase (EC 4.2.1.18), and D is a membrane transporter. The supplied sequence (~349 aa) contains motifs characteristic of the crotonase superfamily of hydratases/dehydratases: tandem 'GGG' and 'GAGG' glycine-rich stretches (e.g., 'GGGLELALCTHFRVLTS…', 'GAGGTHRLPRLIGLGRARDMIVTG'), a helix-rich C-terminal region with CoA-binding-like hydrophobic stretches, and an overall α/β architecture consistent with the crotonase fold. Recognizing the protein as a hydratase/lyase of the crotonase superfamily eliminates A (oxidoreductase), B (hydrolase), and D (transporter), leaving C as the only lyase reaction among the choices.",
    "missing_item_specific_fact": "The specific substrate identity (methylglutaconyl-CoA vs. other crotonase-superfamily substrates such as enoyl-CoA or 3-hydroxyacyl-CoA) cannot be determined from the sequence by general reasoning alone; that level of specificity depends on database annotation or detailed subfamily motif analysis. However, because no competing hydratase option is present among the distractors, the class-level identification is sufficient to select C.",
    "reason": "The question is answerable through general biological reasoning: identifying the enzyme as a hydratase/lyase (crotonase superfamily) from sequence motifs and selecting the sole lyase reaction among the four options. The specific EC-number-level substrate assignment is not derivable from the sequence, but it is not required to discriminate the given choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four distractors span four unrelated enzyme classes (oxidoreductase, hydrolase, lyase, transporter), so only one option (C) is consistent with a hydratase/lyase. No ambiguity exists among the provided choices once the general enzyme class is recognized."
  },
  "important_caveats": [
    "The UniProt annotation for this reaction carries evidence code ECO:0000305 (inferred from electronic annotation), meaning the specific EC assignment is a computational prediction, not a direct experimental measurement of the enzymatic reaction.",
    "The primary paper (PubMed:32431008) describes the gene as encoding a 'putative' 3-methylglutaconyl-CoA hydratase and focuses on its role in mitochondrial dynamics and infectious growth rather than on in vitro kinetic characterization of the hydration reaction.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model; the model must rely solely on the 349-aa sequence and the four choices.",
    "The specific substrate-level identification (methylglutaconyl-CoA vs. other CoA-ester substrates of the crotonase superfamily) is not derivable from the sequence by general reasoning; the question is answerable only because no competing hydratase option is offered."
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

**Accession:** `G4N954` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
"G4N954"
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"4.2.1.18","evidences":[{"evidenceCode":"ECO:0000305","id":"32431008","source":"PubMed"}],"name":"(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:21536"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:43074"},{"database":"ChEBI","id":"CHEBI:57346"}]}}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
ID   AUH1_PYRO7              Reviewed;         349 AA.
AC   G4N954;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-DEC-2011, sequence version 1.
DT   28-JAN-2026, entry version 54.
DE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};
DE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};
DE   Flags: Precursor;
GN   Name=AUH1 {ECO:0000303|PubMed:32431008}; ORFNames=MGG_03335;
OS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast
OS   fungus) (Magnaporthe oryzae).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.
OX   NCBI_TaxID=242507;
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
DE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};
DE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};
DE   Flags: Precursor;
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 27-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
RN   [2]
RP   FUNCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.
RX   PubMed=32431008; DOI=10.1111/1462-2920.15088;
RA   Xiao Y., Liu L., Zhang T., Zhou R., Ren Y., Li X., Shu H., Ye W., Zheng X.,
RA   Zhang Z., Zhang H.;
RT   "Transcription factor MoMsn2 targets the putative 3-methylglutaconyl-CoA
RT   hydratase-encoding gene MoAUH1 to govern infectious growth via
RT   mitochondrial fusion/fission balance in Magnaporthe oryzae.";
RL   Environ. Microbiol. 23:774-790(2021).
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 44-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-
CC         glutaconyl-CoA + H2O; Xref=Rhea:RHEA:21536, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:43074, ChEBI:CHEBI:57346; EC=4.2.1.18;
CC         Evidence={ECO:0000305|PubMed:32431008};
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
