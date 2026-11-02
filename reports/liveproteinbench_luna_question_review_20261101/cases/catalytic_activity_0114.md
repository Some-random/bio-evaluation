# catalytic_activity_0114

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MGFAPLLVFSLFVFAGTTKGFICSFDSIYQLGDSFSDTGNLIRQPPDGPTFCSAHFPYGETFPGMPTGRCSDGRLIIDFIATALNLPLLNPYLQQNVSFRHGVNFAVGGATALDLSFLAARGVQVYDVHSPLSTQLKWFRTYLGSICSSPKECSNKLKNALFILGNIGNNDVNYAFPNRSIEEIRAYLPFITEAVANATREIIRLGGTRVIVPGMFPLGCLARNLYFFPDGDKDDLGCLSSLNDLSIYFNSLIQQALASLRIEFPQAVIIYADYYNAWGFLFRNGPALGFNSTTMLKCCCGIGGPYNYDPDRECASQGVPVCSNPTEYIQWDGTHFTQAAYRRVAEYIIPDIIKELKCSYSSIQHLTEGREALHINERE

[Multiple Choices]
A. D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)
B. 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)
C. D-ribose 5-phosphate + uracil = psi-UMP + H2O
D. Fe(2+)(in) = Fe(2+)(out)
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

> The sequence exactly matches the 379-aa UniProt entry for acetylajmalan esterase 1. That entry assigns the reaction in choice B and cites ECO:0000269 evidence linked to a PubMed article. This supports the key as an experimentally attributed annotation, though the cited study was not independently reviewed here.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-peptide-like region and a GxSxG-like serine-hydrolase motif (GDSFS). These features are consistent with a soluble secretory-pathway esterase, making the ester hydrolysis in B a meaningful fit over the acetyltransferase, pseudouridine-forming reaction, or iron transport choices.

**Missing item-specific fact**

> The exact physiological substrate and product specificity—17-O-acetylnorajmaline to norajmaline—is not established by those sequence features alone; that specific assignment requires protein-specific annotation or experimental evidence.

**Reason**

> The choices differ substantially in reaction class, and the sequence gives a defensible biological basis for favoring an esterase reaction. It does not independently reveal the precise alkaloid substrate, but the broad chemistry meaningfully distinguishes B among the listed options.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The esterase-like sequence features favor B over the other listed reaction classes; no other choice is comparably supported by the supplied sequence.

### Important caveats

- Reviewer-only database evidence supports the expected answer but was not available to the evaluated model.
- The sequence-based argument supports the reaction class, not the exact substrate specificity.
- The cited experimental attribution and database annotation were not independently validated against the primary paper.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the 379-aa UniProt entry for acetylajmalan esterase 1. That entry assigns the reaction in choice B and cites ECO:0000269 evidence linked to a PubMed article. This supports the key as an experimentally attributed annotation, though the cited study was not independently reviewed here.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and a GxSxG-like serine-hydrolase motif (GDSFS). These features are consistent with a soluble secretory-pathway esterase, making the ester hydrolysis in B a meaningful fit over the acetyltransferase, pseudouridine-forming reaction, or iron transport choices.",
    "missing_item_specific_fact": "The exact physiological substrate and product specificity—17-O-acetylnorajmaline to norajmaline—is not established by those sequence features alone; that specific assignment requires protein-specific annotation or experimental evidence.",
    "reason": "The choices differ substantially in reaction class, and the sequence gives a defensible biological basis for favoring an esterase reaction. It does not independently reveal the precise alkaloid substrate, but the broad chemistry meaningfully distinguishes B among the listed options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The esterase-like sequence features favor B over the other listed reaction classes; no other choice is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the expected answer but was not available to the evaluated model.",
    "The sequence-based argument supports the reaction class, not the exact substrate specificity.",
    "The cited experimental attribution and database annotation were not independently validated against the primary paper."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `P0DXJ4`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 2. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.205752+00:00.  

```json
"P0DXJ4"
```

Source SHA-256: `bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.205752+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"3.1.1.80"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Acetylajmalan esterase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsAAE1"}]}}
```

Source SHA-256: `bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.205752+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23797"}}],"reaction":{"ecNumber":"3.1.1.80","evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"name":"17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23796"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30089"},{"database":"ChEBI","id":"CHEBI:77618"},{"database":"ChEBI","id":"CHEBI:77725"}]}}
```

Source SHA-256: `bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:19.289362+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+);
CC         Xref=Rhea:RHEA:23796, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30089, ChEBI:CHEBI:77618, ChEBI:CHEBI:77725; EC=3.1.1.80;
CC         Evidence={ECO:0000269|PubMed:38212296};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23797;
CC         Evidence={ECO:0000269|PubMed:38212296};
```

Source SHA-256: `e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 114). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
