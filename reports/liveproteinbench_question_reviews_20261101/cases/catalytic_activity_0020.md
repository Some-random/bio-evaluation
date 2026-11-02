# catalytic_activity_0020

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — tetrahydroalstonine + A + reduced &#91;NADPH--hemoprotein reductase&#93; + O2 = alstonine + AH2 + oxidized &#91;NADPH--hemoprotein reductase&#93; + 2 H2O + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATPQFSCLLPAFFLLVVFLFLLIKELRRYKSPKTTQKLPPGPPMLPIIGNLHQMASSLPHQNLKKLADKYGPLMHLKLGEISAVAVSSPRLAKEVLQTRGLAFADRPQSVVAKLMLHNCLGVTFSRYGDYWRQLRQIFAMELLSSKSVQSFSTIMEDELFAMVKSIESEAGRPIILADKLISYLYATLSRATLGRVCKGKETLIEVTGETLALSGAQSLEDIFPSVKIFAYLNPLRPKVRKLFNRIDGVLEDIINQQEKKLLSARVDNDQLQPEENDMLSVLLKLRNGKDSKVQVTNNDIKAIIFELFLAGTVGSSTTVEWAMSEMMKNPKVMEKAQHEVREVLKGKKRICQSDIQKLSYLKLVVKETLRLHPPAPLLFPRECRGQCEVDGYTIPAKAMVMVNCWALGRDPEHWIEADKFEPERFKNSSIDFIGNHFEYIPFGAGRRICPGISFGATNVELLLAALLYHFDWELAGGMHPKDLDMLELFGPGCTRKNPLSVIPSICIPSHDDN

[Multiple Choices]
A. tetrahydroalstonine + A + reduced [NADPH--hemoprotein reductase] + O2 = alstonine + AH2 + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
B. deacetylisoipecoside + S-adenosyl-L-methionine = 6-O-methyldeacetylisoipecoside + S-adenosyl-L-homocysteine + H(+)
C. norcoclaurine + S-adenosyl-L-methionine = coclaurine + S-adenosyl-L-homocysteine + H(+)
D. [molybdopterin-synthase sulfur-carrier protein]-C-terminal Gly-Gly + ATP + H(+) = [molybdopterin-synthase sulfur-carrier protein]-C-terminal Gly-Gly-AMP + diphosphate
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

> The supplied sequence exactly matches the annotated Alstonia scholaris alstonine synthase. UniProt records the reaction in choice A with experimental-evidence codes citing the 2022 study; the primary paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal region and a conserved P450 heme-binding motif (including the conserved cysteine), supporting a membrane-associated cytochrome P450. Among the choices, A is the P450-type O2/reductase-dependent reaction, whereas B and C are SAM-dependent methylations and D is ATP-dependent adenylation.


**Missing item-specific fact**

> The sequence motifs support the enzyme class and distinguish the reaction classes, but do not independently establish the precise tetrahydroalstonine-to-alstonine transformation; that specific substrate/product assignment is supplied by the cited annotation and study.


**Reason**

> A concrete sequence-based family signature meaningfully favors A over the alternatives, although the exact substrate specificity is not derivable from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices represent distinct catalytic classes, and the sequence supports the P450 class corresponding to A.


### Important caveats

- Reviewer-only database evidence was not available to the evaluated model.
- The exact reaction annotation is linked to experimental evidence, but the cited primary study was not independently examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal region and a conserved P450 heme-binding motif (including the conserved cysteine), supporting a membrane-associated cytochrome P450. Among the choices, A is the P450-type O2/reductase-dependent reaction, whereas B and C are SAM-dependent methylations and D is ATP-dependent adenylation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence motifs support the enzyme class and distinguish the reaction classes, but do not independently establish the precise tetrahydroalstonine-to-alstonine transformation; that specific substrate/product assignment is supplied by the cited annotation and study.",
    "reason": "A concrete sequence-based family signature meaningfully favors A over the alternatives, although the exact substrate specificity is not derivable from the sequence alone."
  },
  "case_id": "catalytic_activity_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated Alstonia scholaris alstonine synthase. UniProt records the reaction in choice A with experimental-evidence codes citing the 2022 study; the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The exact reaction annotation is linked to experimental evidence, but the cited primary study was not independently examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices represent distinct catalytic classes, and the sequence supports the P450 class corresponding to A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated Alstonia scholaris alstonine synthase. UniProt records the reaction in choice A with experimental-evidence codes citing the 2022 study; the primary paper was not independently reviewed here.",
    "evidence_ids": ["C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal region and a conserved P450 heme-binding motif (including the conserved cysteine), supporting a membrane-associated cytochrome P450. Among the choices, A is the P450-type O2/reductase-dependent reaction, whereas B and C are SAM-dependent methylations and D is ATP-dependent adenylation.",
    "missing_item_specific_fact": "The sequence motifs support the enzyme class and distinguish the reaction classes, but do not independently establish the precise tetrahydroalstonine-to-alstonine transformation; that specific substrate/product assignment is supplied by the cited annotation and study.",
    "reason": "A concrete sequence-based family signature meaningfully favors A over the alternatives, although the exact substrate specificity is not derivable from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices represent distinct catalytic classes, and the sequence supports the P450 class corresponding to A."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The exact reaction annotation is linked to experimental evidence, but the cited primary study was not independently examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A9E7LUJ4 (sequence matched, 514 AA) annotates this protein as 'Alstonine synthase' (AsAS), a Cytochrome P450 (EC 1.14.19.-) from Alstonia scholaris. The catalytic activity is annotated with ECO:0000269 (inferred from direct assay) evidence from PubMed:36349266, and the reaction text exactly matches Choice A: tetrahydroalstonine + A + reduced &#91;NADPH--hemoprotein reductase&#93; + O2 = alstonine + AH2 + oxidized &#91;NADPH--hemoprotein reductase&#93; + 2 H2O + H(+). The sequence contains canonical P450 heme-binding motifs (FGAGRRICPG and HFDWELAGG with the axial histidine), consistent with the annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable cytochrome P450 signature motifs: the FxxGxRxCxG heme-binding motif (FGAGRRICPG) and the conserved I-helix/Meander region with the axial histidine (HFDWELAGG). These identify the protein as a P450 monooxygenase. Among the four choices, only A is a P450-type reaction (involving O2, NADPH, and a hemoprotein reductase). Choices B and C are SAM-dependent methyltransferase reactions (EC 2.1.-), and Choice D is an ATP-dependent adenylylation reaction. A P450 scaffold cannot catalyze methyltransfer or adenylylation chemistry. Thus, identifying the enzyme class from sequence motifs is sufficient to eliminate B, C, and D and select A.


**Missing item-specific fact**

> The specific substrate identity (tetrahydroalstonine → alstonine) is an item-specific experimental fact. However, it is not needed to select the correct answer because the reaction-type elimination (P450 vs. methyltransferase vs. adenylylation) uniquely identifies A among the four options.


**Reason**

> A model that recognizes the P450 heme-binding motifs in the sequence can deduce the enzyme class and eliminate the three non-P450 reaction types without memorizing this particular enzyme's substrate. The reasoning chain (P450 motifs → monooxygenase requiring O2/NADPH/hemoprotein reductase → only Choice A fits) is a concrete, generalizable biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices B and C are methyltransferase reactions, D is an adenylylation reaction, and A is a P450 monooxygenase reaction. These represent three distinct enzyme classes, so a correct identification of the P450 scaffold eliminates all distractors unambiguously.


### Important caveats

- The specific substrate/product pair (tetrahydroalstonine → alstonine) is an experimentally determined fact (PubMed:36349266) that a model cannot derive from sequence alone, but it is not required to select A given the reaction-type elimination.
- The UniProt annotation carries ECO:0000269 (direct assay) evidence, indicating experimental validation rather than computational prediction.
- The sequence was integrated into Swiss-Prot on 2025-06-18; the author's source snapshot date is unknown, but the sequence has been stable since 2023-05-03.
- Reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what is derivable from the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable cytochrome P450 signature motifs: the FxxGxRxCxG heme-binding motif (FGAGRRICPG) and the conserved I-helix/Meander region with the axial histidine (HFDWELAGG). These identify the protein as a P450 monooxygenase. Among the four choices, only A is a P450-type reaction (involving O2, NADPH, and a hemoprotein reductase). Choices B and C are SAM-dependent methyltransferase reactions (EC 2.1.-), and Choice D is an ATP-dependent adenylylation reaction. A P450 scaffold cannot catalyze methyltransfer or adenylylation chemistry. Thus, identifying the enzyme class from sequence motifs is sufficient to eliminate B, C, and D and select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (tetrahydroalstonine → alstonine) is an item-specific experimental fact. However, it is not needed to select the correct answer because the reaction-type elimination (P450 vs. methyltransferase vs. adenylylation) uniquely identifies A among the four options.",
    "reason": "A model that recognizes the P450 heme-binding motifs in the sequence can deduce the enzyme class and eliminate the three non-P450 reaction types without memorizing this particular enzyme's substrate. The reasoning chain (P450 motifs → monooxygenase requiring O2/NADPH/hemoprotein reductase → only Choice A fits) is a concrete, generalizable biological argument."
  },
  "case_id": "catalytic_activity_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A9E7LUJ4 (sequence matched, 514 AA) annotates this protein as 'Alstonine synthase' (AsAS), a Cytochrome P450 (EC 1.14.19.-) from Alstonia scholaris. The catalytic activity is annotated with ECO:0000269 (inferred from direct assay) evidence from PubMed:36349266, and the reaction text exactly matches Choice A: tetrahydroalstonine + A + reduced [NADPH--hemoprotein reductase] + O2 = alstonine + AH2 + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+). The sequence contains canonical P450 heme-binding motifs (FGAGRRICPG and HFDWELAGG with the axial histidine), consistent with the annotation."
  },
  "important_caveats": [
    "The specific substrate/product pair (tetrahydroalstonine → alstonine) is an experimentally determined fact (PubMed:36349266) that a model cannot derive from sequence alone, but it is not required to select A given the reaction-type elimination.",
    "The UniProt annotation carries ECO:0000269 (direct assay) evidence, indicating experimental validation rather than computational prediction.",
    "The sequence was integrated into Swiss-Prot on 2025-06-18; the author's source snapshot date is unknown, but the sequence has been stable since 2023-05-03.",
    "Reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what is derivable from the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B and C are methyltransferase reactions, D is an adenylylation reaction, and A is a P450 monooxygenase reaction. These represent three distinct enzyme classes, so a correct identification of the P450 scaffold eliminates all distractors unambiguously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A9E7LUJ4 (sequence matched, 514 AA) annotates this protein as 'Alstonine synthase' (AsAS), a Cytochrome P450 (EC 1.14.19.-) from Alstonia scholaris. The catalytic activity is annotated with ECO:0000269 (inferred from direct assay) evidence from PubMed:36349266, and the reaction text exactly matches Choice A: tetrahydroalstonine + A + reduced [NADPH--hemoprotein reductase] + O2 = alstonine + AH2 + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+). The sequence contains canonical P450 heme-binding motifs (FGAGRRICPG and HFDWELAGG with the axial histidine), consistent with the annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable cytochrome P450 signature motifs: the FxxGxRxCxG heme-binding motif (FGAGRRICPG) and the conserved I-helix/Meander region with the axial histidine (HFDWELAGG). These identify the protein as a P450 monooxygenase. Among the four choices, only A is a P450-type reaction (involving O2, NADPH, and a hemoprotein reductase). Choices B and C are SAM-dependent methyltransferase reactions (EC 2.1.-), and Choice D is an ATP-dependent adenylylation reaction. A P450 scaffold cannot catalyze methyltransfer or adenylylation chemistry. Thus, identifying the enzyme class from sequence motifs is sufficient to eliminate B, C, and D and select A.",
    "missing_item_specific_fact": "The specific substrate identity (tetrahydroalstonine → alstonine) is an item-specific experimental fact. However, it is not needed to select the correct answer because the reaction-type elimination (P450 vs. methyltransferase vs. adenylylation) uniquely identifies A among the four options.",
    "reason": "A model that recognizes the P450 heme-binding motifs in the sequence can deduce the enzyme class and eliminate the three non-P450 reaction types without memorizing this particular enzyme's substrate. The reasoning chain (P450 motifs → monooxygenase requiring O2/NADPH/hemoprotein reductase → only Choice A fits) is a concrete, generalizable biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B and C are methyltransferase reactions, D is an adenylylation reaction, and A is a P450 monooxygenase reaction. These represent three distinct enzyme classes, so a correct identification of the P450 scaffold eliminates all distractors unambiguously."
  },
  "important_caveats": [
    "The specific substrate/product pair (tetrahydroalstonine → alstonine) is an experimentally determined fact (PubMed:36349266) that a model cannot derive from sequence alone, but it is not required to select A given the reaction-type elimination.",
    "The UniProt annotation carries ECO:0000269 (direct assay) evidence, indicating experimental validation rather than computational prediction.",
    "The sequence was integrated into Swiss-Prot on 2025-06-18; the author's source snapshot date is unknown, but the sequence has been stable since 2023-05-03.",
    "Reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what is derivable from the sequence and general biological knowledge."
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

**Accession:** `A0A9E7LUJ4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
"A0A9E7LUJ4"
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Cytochrome P450 AS"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.14.19.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Alstonine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsAS"}]}}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:58129"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"name":"tetrahydroalstonine + A + reduced [NADPH--hemoprotein reductase] + O2 = alstonine + AH2 + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58128"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:13193"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:17499"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:142526"},{"database":"ChEBI","id":"CHEBI:142530"}]}}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65382.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.040905+00:00.  

```text
ID   AS_ALSSC                Reviewed;         514 AA.
AC   A0A9E7LUJ4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 13.
DE   RecName: Full=Alstonine synthase {ECO:0000303|PubMed:36349266};
DE            Short=AsAS {ECO:0000303|PubMed:36349266};
DE            EC=1.14.19.- {ECO:0000269|PubMed:36349266};
DE   AltName: Full=Cytochrome P450 AS {ECO:0000303|PubMed:36349266};
GN   Name=AS {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.040905+00:00.  

```text
DE   RecName: Full=Alstonine synthase {ECO:0000303|PubMed:36349266};
DE            Short=AsAS {ECO:0000303|PubMed:36349266};
DE            EC=1.14.19.- {ECO:0000269|PubMed:36349266};
DE   AltName: Full=Cytochrome P450 AS {ECO:0000303|PubMed:36349266};
```

Source SHA-256: `cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)  
**Locator:** `lines 30-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.040905+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=tetrahydroalstonine + A + reduced [NADPH--hemoprotein
CC         reductase] + O2 = alstonine + AH2 + oxidized [NADPH--hemoprotein
CC         reductase] + 2 H2O + H(+); Xref=Rhea:RHEA:58128, Rhea:RHEA-
CC         COMP:11964, Rhea:RHEA-COMP:11965, ChEBI:CHEBI:13193,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:17499, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,
CC         ChEBI:CHEBI:142526, ChEBI:CHEBI:142530;
CC         Evidence={ECO:0000269|PubMed:36349266};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58129;
CC         Evidence={ECO:0000269|PubMed:36349266};
```

Source SHA-256: `cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
