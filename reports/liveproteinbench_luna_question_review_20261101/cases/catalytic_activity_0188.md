# catalytic_activity_0188

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK

[Multiple Choices]
A. inosine(in) + H(+)(in) = inosine(out) + H(+)(out)
B. 2,2-dihydroxyspheroidene = spheroiden-2-one + H2O
C. 2'-hydroxy-2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2',2'-dihydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
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

> The sequence exactly matches the rabbit UniProt entry annotated as L-fucose dehydrogenase. Its catalytic-activity annotation gives the reaction in choice D and cites experimental evidence (ECO:0000269, PubMed 38944119).

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich nucleotide-binding motif consistent with a soluble NAD-dependent oxidoreductase, and it lacks the hydrophobic segments expected of a membrane transporter. Among the choices, D is the NAD+-dependent oxidation; the other reactions describe transport, carotenoid chemistry, or an O2/ferredoxin-dependent oxidation.

**Missing item-specific fact**

> Identifying L-fucose as the substrate specifically would require protein-specific functional annotation or experimental knowledge; the sequence argument mainly distinguishes the broad reaction class.

**Reason**

> The sequence and choice wording provide meaningful grounds to favor an NAD-dependent dehydrogenase reaction over the other proposed reaction classes, even though they do not independently establish substrate specificity.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Choice D is the only option describing an NAD+-dependent oxidation compatible with the sequence’s apparent soluble oxidoreductase character.

### Important caveats

- The reviewer-only UniProt evidence is not information supplied to the evaluated model.
- The cited experimental evidence supports the annotation, but the primary paper was not independently reviewed here.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the rabbit UniProt entry annotated as L-fucose dehydrogenase. Its catalytic-activity annotation gives the reaction in choice D and cites experimental evidence (ECO:0000269, PubMed 38944119).",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich nucleotide-binding motif consistent with a soluble NAD-dependent oxidoreductase, and it lacks the hydrophobic segments expected of a membrane transporter. Among the choices, D is the NAD+-dependent oxidation; the other reactions describe transport, carotenoid chemistry, or an O2/ferredoxin-dependent oxidation.",
    "missing_item_specific_fact": "Identifying L-fucose as the substrate specifically would require protein-specific functional annotation or experimental knowledge; the sequence argument mainly distinguishes the broad reaction class.",
    "reason": "The sequence and choice wording provide meaningful grounds to favor an NAD-dependent dehydrogenase reaction over the other proposed reaction classes, even though they do not independently establish substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice D is the only option describing an NAD+-dependent oxidation compatible with the sequence’s apparent soluble oxidoreductase character."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence is not information supplied to the evaluated model.",
    "The cited experimental evidence supports the annotation, but the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0AAT9JA24`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 5. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
"A0AAT9JA24"
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Hydroxysteroid 17-beta dehydrogenase 14"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"value":"1.1.1.122"}],"fullName":{"value":"L-fucose dehydrogenase"}}}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.009007+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"38944119","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81516"}}],"reaction":{"ecNumber":"1.1.1.122","evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"name":"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81515"},{"database":"ChEBI","id":"CHEBI:2181"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:81457"}]}}
```

Source SHA-256: `b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)  
**Locator:** `lines 50-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 2.  
**Retrieved:** 2026-11-01T06:27:41.890371+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);
CC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;
CC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;
CC         Evidence={ECO:0000305|PubMed:38944119};
```

Source SHA-256: `fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 188). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
