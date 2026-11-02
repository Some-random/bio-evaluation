# catalytic_activity_0087

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — 4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MSSTAPEDVARPLLALPAIEAFDAIVRGRRSVRSYADVQVPRRTVRDVLELAARAPSNSNVQPWHTYVLTGRHKRALTDSVLRYYDTIGRTVREFDYQPGPDGWEEPYKERRESFGEGLYGRALGLSLADVDDREFYHRRNYDFFAAPVGLIVTVARNPRLSALIDAGAYIQTILLSARSRGLSTCAQASFLDFHPAVRECLAIPTHRTIVCGISLGYEDAQHPIASNATTREPVDRHVTFLWDDDD

[Multiple Choices]
A. 3alpha(S)-strictosidine + H2O = strictosidine aglycone + D-glucose
B. L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)
C. 3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate
D. 4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O
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

> The supplied sequence exactly matches the sequence in the UniProt entry annotated with reaction D. The catalytic-activity annotation cites experimental evidence (ECO:0000269) linked to PubMed 34554625; the archived entry available by the historical cutoff also records reaction D.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options describe distinct enzyme chemistries, but the sequence alone offers no sufficiently specific, general argument for the particular 4-nitrobenzoate substrate and hydroxylaminobenzoate product in D. At most, sequence-based family recognition might suggest a broad enzyme class, not establish this precise reaction.

**Missing item-specific fact**

> The protein-specific functional annotation or experimental substrate/product evidence identifying this enzyme as a 4-nitrobenzoate reductase.

**Reason**

> Distinguishing D requires protein-specific substrate specificity not supplied in the question. The matching annotation and its experimental evidence support the key for this audit, but they were reviewer-only information and do not make the answer inferable from the model input.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The choices state chemically distinct reactions, and the sequence-matched annotation supports D; no alternative choice is supported by the supplied reviewer evidence.

### Important caveats

- The experimental-evidence designation is reported by UniProt and linked to the cited publication; the primary paper was not independently reviewed here.
- The actual author source snapshot is unknown, although a historical sequence-matched entry available by the stated cutoff contains the same reaction annotation.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the UniProt entry annotated with reaction D. The catalytic-activity annotation cites experimental evidence (ECO:0000269) linked to PubMed 34554625; the archived entry available by the historical cutoff also records reaction D.",
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H1",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options describe distinct enzyme chemistries, but the sequence alone offers no sufficiently specific, general argument for the particular 4-nitrobenzoate substrate and hydroxylaminobenzoate product in D. At most, sequence-based family recognition might suggest a broad enzyme class, not establish this precise reaction.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate/product evidence identifying this enzyme as a 4-nitrobenzoate reductase.",
    "reason": "Distinguishing D requires protein-specific substrate specificity not supplied in the question. The matching annotation and its experimental evidence support the key for this audit, but they were reviewer-only information and do not make the answer inferable from the model input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices state chemically distinct reactions, and the sequence-matched annotation supports D; no alternative choice is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The experimental-evidence designation is reported by UniProt and linked to the cited publication; the primary paper was not independently reviewed here.",
    "The actual author source snapshot is unknown, although a historical sequence-matched entry available by the stated cutoff contains the same reaction annotation."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `P0DXG6`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 3. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
"P0DXG6"
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"34554625","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:80196"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"34554625","source":"PubMed"}],"name":"4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80195"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:142863"},{"database":"ChEBI","id":"CHEBI:231457"}]}}
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
{"citation":{"authors":["Cheng M.","Qian Y.","Xing Z.","Zylstra G.J.","Huang X."],"citationCrossReferences":[{"database":"PubMed","id":"34554625"},{"database":"DOI","id":"10.1111/1462-2920.15787"}],"citationType":"journal article","firstPage":"7028","id":"34554625","journal":"Environ. Microbiol.","lastPage":"7041","publicationDate":"2021","title":"The low-nanomolar 4-nitrobenzoate-responsive repressor PnbX negatively regulates the actinomycete-derived 4-nitrobenzoate-degrading pnb locus.","volume":"23"},"referenceComments":[{"type":"STRAIN","value":"LMS-CY"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","INDUCTION"]}
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:31.939265+00:00.  

```text
ID   PNBA_NOCS0              Reviewed;         247 AA.
AC   P0DXG6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=4-nitrobenzoate reductase {ECO:0000303|PubMed:34554625};
DE            Short=4-NBA reductase {ECO:0000303|PubMed:34554625};
DE            EC=1.7.1.- {ECO:0000269|PubMed:34554625};
DE   AltName: Full=4-nitrobenzoate nitroreductase {ECO:0000303|PubMed:34554625};
DE            Short=4-NBA nitroreductase {ECO:0000303|PubMed:34554625};
GN   Name=pnbA {ECO:0000303|PubMed:34554625};
GN   ORFNames=KM427_00695 {ECO:0000312|EMBL:QWF22307.1};
OS   Nocardioides sp. (strain LMS-CY).
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Propionibacteriales;
OC   Nocardioidaceae; Nocardioides.
OX   NCBI_TaxID=2840457;
```

Source SHA-256: `6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)  
**Locator:** `lines 30-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:31.939265+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate +
CC         2 NADP(+) + H2O; Xref=Rhea:RHEA:80195, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,
CC         ChEBI:CHEBI:142863, ChEBI:CHEBI:231457;
CC         Evidence={ECO:0000269|PubMed:34554625};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80196;
CC         Evidence={ECO:0000269|PubMed:34554625};
```

Source SHA-256: `6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 87). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
