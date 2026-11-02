# catalytic_activity_0082

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MRSIALALAAAPAVLAQSQLWGQCGGIGWNGPTTCVSGATCTKINDWYHQCLPGGNNNNPPPATTSQWTPPPAQTSSNPPPNNGGGGGNTLHEKFKARGKQYFGTEIDHYHLNNNQLMEIARREFGQITHENSMKWDATEPSRGSFSFGNADRVVDWATSNGKLIRGHTLLWHSQLPQWVQNINDRNTLTQVIENHVKTIMTRYKGKIFHYDVVNEILDENGGLRNSVFSRVLGEDFVGIAFRAARATDPDAKLYINDYNLDSANYAKTRGMINLVNKWVSQGVPIDGIGTQAHLAGPGGWNPASGVPAALQALAGANVKEVAITELDIQGAGANDYVTVANACLNVQKCVGITVWGVSDRDSWRSNENPLLYDGSYRPKAAYNALMNAL

[Multiple Choices]
A. cytidine(in) = cytidine(out)
B. tetrahydroalstonine + A + reduced [NADPH--hemoprotein reductase] + O2 = alstonine + AH2 + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
C. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
D. FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-dione + FMNH2 + AMP + diphosphate
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

> The supplied sequence exactly matches the UniProt sequence annotated as endo-1,4-beta-xylanase C, and the matched record assigns the stated reaction with experimental evidence linked to PubMed 23306124.

Cited evidence: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal signal peptide and lack of multiple transmembrane segments favor a secreted soluble enzyme, making a transporter or intracellular enzyme less plausible. These features do not establish xylan as the substrate or identify the precise reaction.

**Missing item-specific fact**

> The sequence-specific identification as an endo-1,4-beta-xylanase, or equivalent evidence of its substrate specificity and catalytic activity.

**Reason**

> The supplied sequence gives broad clues about secretion and protein type, but distinguishing xylan hydrolysis from other possible extracellular enzyme activities requires protein-specific family or activity information not stated in the input.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The reviewer-only matched-sequence annotation supports C; none of the other listed reactions is supported by the supplied evidence.

### Important caveats

- The UniProt catalytic-activity annotation cites experimental evidence, but the primary paper was not independently retrieved and validated here.
- The historical sequence match is established, but the author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as endo-1,4-beta-xylanase C, and the matched record assigns the stated reaction with experimental evidence linked to PubMed 23306124.",
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal signal peptide and lack of multiple transmembrane segments favor a secreted soluble enzyme, making a transporter or intracellular enzyme less plausible. These features do not establish xylan as the substrate or identify the precise reaction.",
    "missing_item_specific_fact": "The sequence-specific identification as an endo-1,4-beta-xylanase, or equivalent evidence of its substrate specificity and catalytic activity.",
    "reason": "The supplied sequence gives broad clues about secretion and protein type, but distinguishing xylan hydrolysis from other possible extracellular enzyme activities requires protein-specific family or activity information not stated in the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports C; none of the other listed reactions is supported by the supplied evidence."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation cites experimental evidence, but the primary paper was not independently retrieved and validated here.",
    "The historical sequence match is established, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `M4MEY9`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 41. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.429543+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1,4-beta-D-xylan xylanohydrolase C"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23306124","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase C"}}}
```

Source SHA-256: `d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.429543+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.429543+00:00.  

```json
{"citation":{"authors":["Du Y.","Shi P.","Huang H.","Zhang X.","Luo H.","Wang Y.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"23306124"},{"database":"DOI","id":"10.1016/j.biortech.2012.12.067"}],"citationType":"journal article","firstPage":"161","id":"23306124","journal":"Bioresour. Technol.","lastPage":"167","publicationDate":"2013","title":"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.","volume":"130"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)  
**Locator:** `lines 49-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:28:15.495114+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:23306124};
```

Source SHA-256: `9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 82). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
