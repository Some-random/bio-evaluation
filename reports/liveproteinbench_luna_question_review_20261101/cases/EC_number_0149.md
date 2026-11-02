# EC_number_0149

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.3.1.312

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MIETPYLLFLGDAPDMLAAKVAIGIRDWRPDHAVGQISLPGCGANLGLTEMTLEEAKAAGAKTLVIGVANRGGKISQEWKKVLVQALEEGFDLASGLHNLLRDEPDLAAVAEATGRTLHDVRVPSVQYPIADGVKRRGKRCLAVGTDCSVGKMYTALAMDAEMQARGIKSTFRATGQTGILITGDGVPLDAVIADFMAGSIEYLTPDNDDDHWDLIEGQGSLFHVSYSGVTMALVHGGQPDALILCHEPTRTHMRGLPDYDVPSLEELRDVALPLAQRANKDCKIVGISVNTQHLGEEEAVAYLKEVEGRMGLPAVDPYRHGAGRLVDALAAV

[Multiple Choices]
A. 2.3.1.322
B. 2.7.7.43
C. 2.3.1.312
D. 5.4.99.14
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312. The annotation links the catalytic activity to PubMed evidence code ECO:0000269; the cited reaction is D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+). This supports choice C, although the primary paper was not independently reviewed here.

Cited evidence: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include different enzyme reaction classifications, but the sequence and options alone provide no sufficiently specific biological argument for identifying this protein's exact substrate and reaction. Broad sequence-based functional inference would not establish the complete EC number.

**Missing item-specific fact**

> The protein-specific functional assignment identifying the sequence as D-glutamate N-acetyltransferase, and its catalyzed reaction, is needed to select EC 2.3.1.312.

**Reason**

> The reviewer evidence supports the key, but that annotation and its cited experimental evidence were not provided to the evaluated model. Recognizing or retrieving the exact protein entry would be lookup, not reasoning from the supplied input.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The reviewer-only sequence-matched annotation specifies EC 2.3.1.312; no supplied evidence supports another listed choice.

### Important caveats

- The UniProt evidence links the functional assignment to a cited publication, but that publication was not independently assessed.
- The exact source snapshot used by the benchmark author is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312. The annotation links the catalytic activity to PubMed evidence code ECO:0000269; the cited reaction is D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+). This supports choice C, although the primary paper was not independently reviewed here.",
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include different enzyme reaction classifications, but the sequence and options alone provide no sufficiently specific biological argument for identifying this protein's exact substrate and reaction. Broad sequence-based functional inference would not establish the complete EC number.",
    "missing_item_specific_fact": "The protein-specific functional assignment identifying the sequence as D-glutamate N-acetyltransferase, and its catalyzed reaction, is needed to select EC 2.3.1.312.",
    "reason": "The reviewer evidence supports the key, but that annotation and its cited experimental evidence were not provided to the evaluated model. Recognizing or retrieving the exact protein entry would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation specifies EC 2.3.1.312; no supplied evidence supports another listed choice."
  },
  "important_caveats": [
    "The UniProt evidence links the functional assignment to a cited publication, but that publication was not independently assessed.",
    "The exact source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A2T1AE85`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 17. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"value":"2.3.1.312"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"D-glutamate N-acetyltransferase"}}}
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"36690779","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:76496"}}],"reaction":{"ecNumber":"2.3.1.312","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"name":"D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:76495"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29986"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:195260"}]}}
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
{"citation":{"authors":["Yu Y.","Wang P.","Cao H.Y.","Teng Z.J.","Zhu Y.","Wang M.","McMinn A.","Chen Y.","Xiang H.","Zhang Y.Z.","Chen X.L.","Zhang Y.Q."],"citationCrossReferences":[{"database":"PubMed","id":"36690779"},{"database":"DOI","id":"10.1038/s41396-023-01364-6"}],"citationType":"journal article","firstPage":"537","id":"36690779","journal":"ISME J.","lastPage":"548","publicationDate":"2023","title":"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.","volume":"17"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7XRJ","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 25328 / CCUG 55858 / LMG 24367 / R-28751"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190"]}
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)  
**Locator:** `lines 36-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:54.258050+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+);
CC         Xref=Rhea:RHEA:76495, ChEBI:CHEBI:15378, ChEBI:CHEBI:29986,
CC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195260;
CC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76496;
CC         Evidence={ECO:0000305|PubMed:36690779};
```

Source SHA-256: `4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json) (zero-based source row 149). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
