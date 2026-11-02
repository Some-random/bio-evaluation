# catalytic_activity_0123

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MPQVRNPILPGFNPDPSILRVGEDYYIATSTFEWYPGVQIHHSRDLANWELVARPLNRKSQLDMRGNPDSCGIWAPCLSHDGERFWLVYTDVKRKDGSFKDTPNYIVTAEKIEGPWSDPIYINSSGFDPSLFHDDDGRKWFVNMLWDHRRRPQLFEGIVLQEFDPKAGKLVGPRKNIFTGTDLALVEGPHLYKRNGWYYLLTAEGGTGYEHACTFARSRNIWGPYEVHPQKYILTSKDHPHAALQRAGHGDIVDTPDGRTYLVHLTGRPTTQFRRCVLGRETAIQEAYWGDDDWLYVKNGPVPSLWVDLPAARDDTKYWEEKRYTFESGLHKDFQWLRTPETDRIFRTREDGKLTLIGRESIGSWFEQALVARRQTHFSCDAETVIDFSPEDQRQFAGLTAYYCRYNFFYLAVSAHSDGQRELFIMASEASWPLGELRYPVPEGVRIPNEGKVRLALTIRGRELQFYYALEGEELKKIGPVLDASIVSDECGGHQKHGSFTGAFVGVAASDLNGTAAEATFDYFIYRPVQHPSDRYEI

[Multiple Choices]
A. Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.
B. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
C. 5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O
D. UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)
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

> The supplied sequence exactly matches the 538-aa UniProt sequence annotated with the reaction in choice A. The annotation cites ECO:0000269 and PubMed:24262572, and the historical record available by the stated cutoff contains the same reaction annotation. This supports the key, though the cited paper was not independently reviewed here.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support recognizing a glycoside-hydrolase-like protein, which would make the carbohydrate-hydrolysis option more plausible than the listed oxidation or transfer reactions. But that broad inference does not establish xylan as the substrate or the specific exo-hydrolysis described in A.

**Missing item-specific fact**

> The protein-specific functional annotation or experimental substrate-specificity evidence linking this sequence to beta-xylosidase activity is absent from the input.

**Reason**

> Selecting A at the stated reaction specificity depends on a protein-specific function not supplied in the question; broad sequence-based enzyme-family inference is not enough to establish that exact reaction.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The matched-sequence annotation supports A, and the other choices describe chemically distinct reactions without comparable support from the supplied information.

### Important caveats

- The reviewer-only accession and database annotations were not available to the evaluated model.
- The cited evidence code indicates experimental evidence in the annotation, but the underlying publication was not independently validated here.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 538-aa UniProt sequence annotated with the reaction in choice A. The annotation cites ECO:0000269 and PubMed:24262572, and the historical record available by the stated cutoff contains the same reaction annotation. This supports the key, though the cited paper was not independently reviewed here.",
    "evidence_ids": [
      "C1",
      "C5",
      "H4",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support recognizing a glycoside-hydrolase-like protein, which would make the carbohydrate-hydrolysis option more plausible than the listed oxidation or transfer reactions. But that broad inference does not establish xylan as the substrate or the specific exo-hydrolysis described in A.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate-specificity evidence linking this sequence to beta-xylosidase activity is absent from the input.",
    "reason": "Selecting A at the stated reaction specificity depends on a protein-specific function not supplied in the question; broad sequence-based enzyme-family inference is not enough to establish that exact reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports A, and the other choices describe chemically distinct reactions without comparable support from the supplied information."
  },
  "important_caveats": [
    "The reviewer-only accession and database annotations were not available to the evaluated model.",
    "The cited evidence code indicates experimental evidence in the annotation, but the underlying publication was not independently validated here."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `V9TT49`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 19. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
"V9TT49"
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.37","evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"name":"Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini."}}
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)  
**Locator:** `lines 21-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:28:54.377134+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,
RP   SUBCELLULAR LOCATION, AND BIOTECHNOLOGY.
RC   STRAIN=Y1;
RX   PubMed=24262572; DOI=10.1016/j.foodchem.2013.10.062;
RA   Yang X., Shi P., Huang H., Luo H., Wang Y., Zhang W., Yao B.;
RT   "Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and
RT   one GH11 xylanase from Humicola insolens and their synergy in the
RT   degradation of xylan.";
RL   Food Chem. 148:381-387(2014).
```

Source SHA-256: `7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)  
**Locator:** `lines 46-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:28:54.377134+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-
CC         xylose residues from the non-reducing termini.; EC=3.2.1.37;
CC         Evidence={ECO:0000269|PubMed:24262572};
```

Source SHA-256: `7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 123). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
