# catalytic_activity_0020

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — tetrahydroalstonine + A + reduced &#91;NADPH--hemoprotein reductase&#93; + O2 = alstonine + AH2 + oxidized &#91;NADPH--hemoprotein reductase&#93; + 2 H2O + H(+)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: supported

> The supplied sequence exactly matches the annotated Alstonia scholaris alstonine synthase. UniProt records the reaction in choice A with experimental-evidence codes citing the 2022 study; the primary paper was not independently reviewed here.

Cited evidence: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal region and a conserved P450 heme-binding motif (including the conserved cysteine), supporting a membrane-associated cytochrome P450. Among the choices, A is the P450-type O2/reductase-dependent reaction, whereas B and C are SAM-dependent methylations and D is ATP-dependent adenylation.

**Missing item-specific fact**

> The sequence motifs support the enzyme class and distinguish the reaction classes, but do not independently establish the precise tetrahydroalstonine-to-alstonine transformation; that specific substrate/product assignment is supplied by the cited annotation and study.

**Reason**

> A concrete sequence-based family signature meaningfully favors A over the alternatives, although the exact substrate specificity is not derivable from the sequence alone.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The choices represent distinct catalytic classes, and the sequence supports the P450 class corresponding to A.

### Important caveats

- Reviewer-only database evidence was not available to the evaluated model.
- The exact reaction annotation is linked to experimental evidence, but the cited primary study was not independently examined.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated Alstonia scholaris alstonine synthase. UniProt records the reaction in choice A with experimental-evidence codes citing the 2022 study; the primary paper was not independently reviewed here.",
    "evidence_ids": [
      "C5",
      "C6",
      "H4"
    ]
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

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A9E7LUJ4`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 13. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 20). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
