# EC_number_0049

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.1.1.129

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNTQPLERALAAFREVLGTAHVSTDESARAAAETATFATTHRIPAIISPGSAAEVEACVRIAREHGVPLYPVSTGKNWGYGSRVPTSDGAIVLSLARMNRILDFNEELAYVAIEPGVTMRQLVAYLNDRGSRLMLSVTGSTPDSSVVGNICDRGFGAGVNAERIAHICNIEVVLPNGERLNTGFGRFPGAQTASIHRWGIGPQLDGLFTQSNLGIVTRMTIWLAPRPRHHEIFYFRLRDERRVEAVTDIIRDLKLQGLPRASVSLWNDYKLVSMKGQYPWQEAAGKTPLPEALLAKLRRAWGGAAWLGGGAILAASQDQIAAERAVIRKALHPHVDKLSFVGQRAARVARLLQRPVQRLTGFDLSEVVRAYEQSPHLGIPMERNIRSAYWRKKAPPPEQTDPDRDRCGAIWLAPAVPSTGKHVGTALRIVRERALAHAFEPGISVIFATERCANIVVALMYDRELPGEDGRAMACYQDIFDRLAAQGYLPYRLGIQSQSALPAAQSSYGTVVGALKRALDPDDILAPGRYDFRHEWPPADN

[Multiple Choices]
A. 4.1.1.128
B. 2.7.4.9
C. 4.1.1.129
D. 5.3.1.16
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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the UniProt entry annotating EC 4.1.1.129, with catalytic-activity evidence attributed to a published study (ECO:0000269). The annotation specifies oxidative decarboxylation of 1′-carboxy-chondrochloren substrates.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include different enzyme classes, but the sequence alone does not provide a defensible basis for identifying the specific chondrochloren substrates and reaction required to distinguish EC 4.1.1.129.


**Missing item-specific fact**

> The protein-specific catalytic reaction or experimentally supported EC annotation.


**Reason**

> Choosing the exact EC number depends on a specific substrate and reaction assignment not supplied in the question; recognizing or retrieving the protein annotation is lookup, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports the keyed EC number; no competing option is supported by the supplied reviewer-only evidence.


### Important caveats

- The experimental evidence is reported through UniProt with a literature citation; the primary paper was not independently retrieved and validated here.
- The exact author data-source snapshot is unknown, though the sequence-matched historical record also lists EC 4.1.1.129.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include different enzyme classes, but the sequence alone does not provide a defensible basis for identifying the specific chondrochloren substrates and reaction required to distinguish EC 4.1.1.129.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic reaction or experimentally supported EC annotation.",
    "reason": "Choosing the exact EC number depends on a specific substrate and reaction assignment not supplied in the question; recognizing or retrieving the protein annotation is lookup, not sequence-based reasoning."
  },
  "case_id": "EC_number_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotating EC 4.1.1.129, with catalytic-activity evidence attributed to a published study (ECO:0000269). The annotation specifies oxidative decarboxylation of 1′-carboxy-chondrochloren substrates."
  },
  "important_caveats": [
    "The experimental evidence is reported through UniProt with a literature citation; the primary paper was not independently retrieved and validated here.",
    "The exact author data-source snapshot is unknown, though the sequence-matched historical record also lists EC 4.1.1.129."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports the keyed EC number; no competing option is supported by the supplied reviewer-only evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotating EC 4.1.1.129, with catalytic-activity evidence attributed to a published study (ECO:0000269). The annotation specifies oxidative decarboxylation of 1′-carboxy-chondrochloren substrates.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include different enzyme classes, but the sequence alone does not provide a defensible basis for identifying the specific chondrochloren substrates and reaction required to distinguish EC 4.1.1.129.",
    "missing_item_specific_fact": "The protein-specific catalytic reaction or experimentally supported EC annotation.",
    "reason": "Choosing the exact EC number depends on a specific substrate and reaction assignment not supplied in the question; recognizing or retrieving the protein annotation is lookup, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports the keyed EC number; no competing option is supported by the supplied reviewer-only evidence."
  },
  "important_caveats": [
    "The experimental evidence is reported through UniProt with a literature citation; the primary paper was not independently retrieved and validated here.",
    "The exact author data-source snapshot is unknown, though the sequence-matched historical record also lists EC 4.1.1.129."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B9ZUK6 (CNDG_CHOCO, 541 AA) matches the supplied sequence exactly. EC 4.1.1.129 (1'-carboxy-chondrochloren decarboxylase) is annotated with evidence code ECO:0000269|PubMed:20080978, indicating direct experimental characterization (Rachid et al., J. Biol. Chem. 2010). Two catalytic-activity comments confirm FAD-dependent oxidative decarboxylation of 1'-carboxy-chondrochloren A and B. The key is well-supported by experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains two recognizable FAD-binding Rossmann-like motifs (STGKNWGYGSR and PSTGKHVGTALR), which are hallmarks of FAD-dependent oxidative decarboxylases. This observation can reasonably eliminate choice B (EC 2.7.4.9, a nucleotidyltransferase with no FAD requirement) and choice D (EC 5.3.1.16, an intramolecular oxidoreductase/isomerase with no FAD requirement), narrowing the field to the two carboxy-lyases A (4.1.1.128) and C (4.1.1.129).


**Missing item-specific fact**

> Distinguishing EC 4.1.1.128 from EC 4.1.1.129 requires knowing the exact substrate identity (1'-carboxy-chondrochloren for .129 vs. the substrate of .128). Both are carboxy-lyases within the same sub-subclass; no general sequence feature or motif differentiates their substrate specificities. The protein's identity as CndG from the chondrochloren biosynthetic pathway in Chondromyces crocatus is a protein-specific database fact not derivable from the sequence by general biological reasoning.


**Reason**

> The FAD-binding motifs provide a genuine, sequence-grounded argument that narrows four choices to two, but the final A-vs-C decision hinges on knowing which specific carboxy-lyase EC number corresponds to this exact protein's substrate. That is an item-specific annotation fact, not something inferable from general biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both 4.1.1.128 and 4.1.1.129 are carboxy-lyases (EC 4.1.1.x). Without database lookup or organism/pathway context supplied in the question, a knowledgeable model could argue for either based on the FAD-binding motifs alone, since both sub-subclass members could plausibly be FAD-dependent oxidative decarboxylases. The FAD motifs do not uniquely select .129 over .128.


### Important caveats

- The UniProt accession B9ZUK6 and the organism Chondromyces crocatus were not provided to the evaluated model; they were inferred by the reviewer from dataset metadata. The model sees only the 541-aa sequence and four EC numbers.
- The EC 4.1.1.129 annotation carries experimental evidence (ECO:0000269), but this does not make the A-vs-C choice reasoning-derivable from the sequence alone.
- The FAD-binding motif observation is a legitimate sequence-based narrowing step but is insufficient to resolve the final binary choice between two adjacent carboxy-lyase EC numbers.
- The author source snapshot for the benchmark construction date is unknown; the historical entry version 61 (first released 2026-01) already carries the EC 4.1.1.129 annotation, so timing is unlikely to be an issue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two recognizable FAD-binding Rossmann-like motifs (STGKNWGYGSR and PSTGKHVGTALR), which are hallmarks of FAD-dependent oxidative decarboxylases. This observation can reasonably eliminate choice B (EC 2.7.4.9, a nucleotidyltransferase with no FAD requirement) and choice D (EC 5.3.1.16, an intramolecular oxidoreductase/isomerase with no FAD requirement), narrowing the field to the two carboxy-lyases A (4.1.1.128) and C (4.1.1.129).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing EC 4.1.1.128 from EC 4.1.1.129 requires knowing the exact substrate identity (1'-carboxy-chondrochloren for .129 vs. the substrate of .128). Both are carboxy-lyases within the same sub-subclass; no general sequence feature or motif differentiates their substrate specificities. The protein's identity as CndG from the chondrochloren biosynthetic pathway in Chondromyces crocatus is a protein-specific database fact not derivable from the sequence by general biological reasoning.",
    "reason": "The FAD-binding motifs provide a genuine, sequence-grounded argument that narrows four choices to two, but the final A-vs-C decision hinges on knowing which specific carboxy-lyase EC number corresponds to this exact protein's substrate. That is an item-specific annotation fact, not something inferable from general biochemistry."
  },
  "case_id": "EC_number_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B9ZUK6 (CNDG_CHOCO, 541 AA) matches the supplied sequence exactly. EC 4.1.1.129 (1'-carboxy-chondrochloren decarboxylase) is annotated with evidence code ECO:0000269|PubMed:20080978, indicating direct experimental characterization (Rachid et al., J. Biol. Chem. 2010). Two catalytic-activity comments confirm FAD-dependent oxidative decarboxylation of 1'-carboxy-chondrochloren A and B. The key is well-supported by experimental evidence."
  },
  "important_caveats": [
    "The UniProt accession B9ZUK6 and the organism Chondromyces crocatus were not provided to the evaluated model; they were inferred by the reviewer from dataset metadata. The model sees only the 541-aa sequence and four EC numbers.",
    "The EC 4.1.1.129 annotation carries experimental evidence (ECO:0000269), but this does not make the A-vs-C choice reasoning-derivable from the sequence alone.",
    "The FAD-binding motif observation is a legitimate sequence-based narrowing step but is insufficient to resolve the final binary choice between two adjacent carboxy-lyase EC numbers.",
    "The author source snapshot for the benchmark construction date is unknown; the historical entry version 61 (first released 2026-01) already carries the EC 4.1.1.129 annotation, so timing is unlikely to be an issue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both 4.1.1.128 and 4.1.1.129 are carboxy-lyases (EC 4.1.1.x). Without database lookup or organism/pathway context supplied in the question, a knowledgeable model could argue for either based on the FAD-binding motifs alone, since both sub-subclass members could plausibly be FAD-dependent oxidative decarboxylases. The FAD motifs do not uniquely select .129 over .128."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B9ZUK6 (CNDG_CHOCO, 541 AA) matches the supplied sequence exactly. EC 4.1.1.129 (1'-carboxy-chondrochloren decarboxylase) is annotated with evidence code ECO:0000269|PubMed:20080978, indicating direct experimental characterization (Rachid et al., J. Biol. Chem. 2010). Two catalytic-activity comments confirm FAD-dependent oxidative decarboxylation of 1'-carboxy-chondrochloren A and B. The key is well-supported by experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains two recognizable FAD-binding Rossmann-like motifs (STGKNWGYGSR and PSTGKHVGTALR), which are hallmarks of FAD-dependent oxidative decarboxylases. This observation can reasonably eliminate choice B (EC 2.7.4.9, a nucleotidyltransferase with no FAD requirement) and choice D (EC 5.3.1.16, an intramolecular oxidoreductase/isomerase with no FAD requirement), narrowing the field to the two carboxy-lyases A (4.1.1.128) and C (4.1.1.129).",
    "missing_item_specific_fact": "Distinguishing EC 4.1.1.128 from EC 4.1.1.129 requires knowing the exact substrate identity (1'-carboxy-chondrochloren for .129 vs. the substrate of .128). Both are carboxy-lyases within the same sub-subclass; no general sequence feature or motif differentiates their substrate specificities. The protein's identity as CndG from the chondrochloren biosynthetic pathway in Chondromyces crocatus is a protein-specific database fact not derivable from the sequence by general biological reasoning.",
    "reason": "The FAD-binding motifs provide a genuine, sequence-grounded argument that narrows four choices to two, but the final A-vs-C decision hinges on knowing which specific carboxy-lyase EC number corresponds to this exact protein's substrate. That is an item-specific annotation fact, not something inferable from general biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both 4.1.1.128 and 4.1.1.129 are carboxy-lyases (EC 4.1.1.x). Without database lookup or organism/pathway context supplied in the question, a knowledgeable model could argue for either based on the FAD-binding motifs alone, since both sub-subclass members could plausibly be FAD-dependent oxidative decarboxylases. The FAD motifs do not uniquely select .129 over .128."
  },
  "important_caveats": [
    "The UniProt accession B9ZUK6 and the organism Chondromyces crocatus were not provided to the evaluated model; they were inferred by the reviewer from dataset metadata. The model sees only the 541-aa sequence and four EC numbers.",
    "The EC 4.1.1.129 annotation carries experimental evidence (ECO:0000269), but this does not make the A-vs-C choice reasoning-derivable from the sequence alone.",
    "The FAD-binding motif observation is a legitimate sequence-based narrowing step but is insufficient to resolve the final binary choice between two adjacent carboxy-lyase EC numbers.",
    "The author source snapshot for the benchmark construction date is unknown; the historical entry version 61 (first released 2026-01) already carries the EC 4.1.1.129 annotation, so timing is unlikely to be an issue."
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

**Accession:** `B9ZUK6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 61. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
"B9ZUK6"
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20080978","source":"PubMed"}],"value":"Oxidative decarboxylase CndG"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"}],"value":"4.1.1.129"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1'-carboxy-chondrochloren decarboxylase"}}}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81492"}}],"reaction":{"ecNumber":"4.1.1.129","evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"}],"name":"1'-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A + FADH2 + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81491"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:57692"},{"database":"ChEBI","id":"CHEBI:58307"},{"database":"ChEBI","id":"CHEBI:132426"},{"database":"ChEBI","id":"CHEBI:231889"}]}}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81496"}}],"reaction":{"ecNumber":"4.1.1.129","evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"}],"name":"1'-carboxy-chondrochloren B + FAD + 2 H(+) = chondrochloren B + FADH2 + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81495"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:57692"},{"database":"ChEBI","id":"CHEBI:58307"},{"database":"ChEBI","id":"CHEBI:132442"},{"database":"ChEBI","id":"CHEBI:231890"}]}}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"citation":{"authors":["Rachid S.","Revermann O.","Dauth C.","Kazmaier U.","Mueller R."],"citationCrossReferences":[{"database":"PubMed","id":"20080978"},{"database":"DOI","id":"10.1074/jbc.m109.079707"}],"citationType":"journal article","firstPage":"12482","id":"20080978","journal":"J. Biol. Chem.","lastPage":"12489","publicationDate":"2010","title":"Characterization of a novel type of oxidative decarboxylase involved in the biosynthesis of the styryl moiety of chondrochloren from an acylated tyrosine.","volume":"285"},"referenceComments":[{"type":"STRAIN","value":"DSM 14714 / JCM 12616 / Cm c5"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","MASS SPECTROMETRY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
ID   CNDG_CHOCO              Reviewed;         541 AA.
AC   B9ZUK6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-APR-2009, sequence version 1.
DT   28-JAN-2026, entry version 61.
DE   RecName: Full=1'-carboxy-chondrochloren decarboxylase {ECO:0000305};
DE            EC=4.1.1.129 {ECO:0000269|PubMed:20080978};
DE   AltName: Full=Oxidative decarboxylase CndG {ECO:0000303|PubMed:20080978};
GN   Name=cndG {ECO:0000303|PubMed:19171307};
GN   ORFNames=CMC5_053350 {ECO:0000312|EMBL:AKT41174.1};
OS   Chondromyces crocatus.
OC   Bacteria; Pseudomonadati; Myxococcota; Polyangia; Polyangiales;
OC   Polyangiaceae; Chondromyces.
OX   NCBI_TaxID=52;
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
DE   RecName: Full=1'-carboxy-chondrochloren decarboxylase {ECO:0000305};
DE            EC=4.1.1.129 {ECO:0000269|PubMed:20080978};
DE   AltName: Full=Oxidative decarboxylase CndG {ECO:0000303|PubMed:20080978};
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 48-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=1'-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A
CC         + FADH2 + CO2; Xref=Rhea:RHEA:81491, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:16526, ChEBI:CHEBI:57692, ChEBI:CHEBI:58307,
CC         ChEBI:CHEBI:132426, ChEBI:CHEBI:231889; EC=4.1.1.129;
CC         Evidence={ECO:0000269|PubMed:20080978};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81492;
CC         Evidence={ECO:0000269|PubMed:20080978};
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 56-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=1'-carboxy-chondrochloren B + FAD + 2 H(+) = chondrochloren B
CC         + FADH2 + CO2; Xref=Rhea:RHEA:81495, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:16526, ChEBI:CHEBI:57692, ChEBI:CHEBI:58307,
CC         ChEBI:CHEBI:132442, ChEBI:CHEBI:231890; EC=4.1.1.129;
CC         Evidence={ECO:0000269|PubMed:20080978};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81496;
CC         Evidence={ECO:0000269|PubMed:20080978};
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
