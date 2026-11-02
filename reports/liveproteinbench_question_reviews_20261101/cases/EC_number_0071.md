# EC_number_0071

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.1.1.353

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTTSASTTDHLIDQQVIDGQAGYTKSFLNIYDLAVFKGTAPLAWHCSPAVSRQMYDTCLGANHVEIGVGTGYLLDNATFPVADPKITLVDLNPNSLAHTAQRLNRYDVTTVRANVLEPLPLEERAYDSVGMSYLLHCVPGSIKEKGIALKHAAAVVRPGGVVFGATVLSSGVPVSARGRWTMNYLNKRGDFHNQEDNYDDLRDQLAQYFPRFQLTSRGCVGIWRAWTTD

[Multiple Choices]
A. 2.1.1.395
B. 2.1.1.34
C. 2.1.1.353
D. 1.14.15.9
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

> The exact sequence matches UniProt entry Q70KH3, annotated as demethylluteothin O-methyltransferase with EC 2.1.1.353. The catalytic-activity annotation assigns that reaction and EC number experimental evidence (ECO:0000269, PubMed 16292785), supporting choice C.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices identify methyltransferase EC numbers and an oxidoreductase EC number; broad sequence or enzyme-class inference might help distinguish the latter, but does not identify the specific substrate reaction needed to select among the methyltransferase options.


**Missing item-specific fact**

> The protein’s specific catalytic activity—methylation of demethylluteothin to luteothin, corresponding to EC 2.1.1.353—is absent from the input.


**Reason**

> The sequence alone supplies no defensible basis for assigning this particular substrate-specific EC number. Selecting C requires a protein-specific annotation or experimental fact; recognizing the exact sequence from an external database would be lookup, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "C"
]
```

> The sequence does not distinguish among the three methyltransferase EC choices at the substrate-specific level. Reviewer-only evidence supports C as the actual answer, but the input itself does not resolve those choices.


### Important caveats

- The supporting UniProt evidence is reviewer-only and was not supplied to the evaluated model.
- The exact sequence match and experimental evidence code support the annotation; the cited primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices identify methyltransferase EC numbers and an oxidoreductase EC number; broad sequence or enzyme-class inference might help distinguish the latter, but does not identify the specific substrate reaction needed to select among the methyltransferase options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein’s specific catalytic activity—methylation of demethylluteothin to luteothin, corresponding to EC 2.1.1.353—is absent from the input.",
    "reason": "The sequence alone supplies no defensible basis for assigning this particular substrate-specific EC number. Selecting C requires a protein-specific annotation or experimental fact; recognizing the exact sequence from an external database would be lookup, not reasoning from the supplied information."
  },
  "case_id": "EC_number_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q70KH3, annotated as demethylluteothin O-methyltransferase with EC 2.1.1.353. The catalytic-activity annotation assigns that reaction and EC number experimental evidence (ECO:0000269, PubMed 16292785), supporting choice C."
  },
  "important_caveats": [
    "The supporting UniProt evidence is reviewer-only and was not supplied to the evaluated model.",
    "The exact sequence match and experimental evidence code support the annotation; the cited primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "C"
    ],
    "reason": "The sequence does not distinguish among the three methyltransferase EC choices at the substrate-specific level. Reviewer-only evidence supports C as the actual answer, but the input itself does not resolve those choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q70KH3, annotated as demethylluteothin O-methyltransferase with EC 2.1.1.353. The catalytic-activity annotation assigns that reaction and EC number experimental evidence (ECO:0000269, PubMed 16292785), supporting choice C.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices identify methyltransferase EC numbers and an oxidoreductase EC number; broad sequence or enzyme-class inference might help distinguish the latter, but does not identify the specific substrate reaction needed to select among the methyltransferase options.",
    "missing_item_specific_fact": "The protein’s specific catalytic activity—methylation of demethylluteothin to luteothin, corresponding to EC 2.1.1.353—is absent from the input.",
    "reason": "The sequence alone supplies no defensible basis for assigning this particular substrate-specific EC number. Selecting C requires a protein-specific annotation or experimental fact; recognizing the exact sequence from an external database would be lookup, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "C"],
    "reason": "The sequence does not distinguish among the three methyltransferase EC choices at the substrate-specific level. Reviewer-only evidence supports C as the actual answer, but the input itself does not resolve those choices."
  },
  "important_caveats": [
    "The supporting UniProt evidence is reviewer-only and was not supplied to the evaluated model.",
    "The exact sequence match and experimental evidence code support the annotation; the cited primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q70KH3 (AURI_STRTU, Streptomyces thioluteus) is annotated with EC 2.1.1.353 (Demethylluteothin O-methyltransferase) with evidence code ECO:0000269 (inferred from direct assay) from PubMed:16292785 (Mueller, He, Hertweck 2006). The catalytic reaction (demethylluteothin + SAM → luteothin + SAH) is experimentally characterized. The supplied sequence matches the UniProt entry exactly (SHA256 confirmed, 230 aa). The annotation was first public 2025-02-05.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains SAM-binding Rossmann-like motifs (GxGxG patterns) consistent with a class I methyltransferase fold, which reasonably eliminates option D (1.14.15.9, a copper monooxygenase/oxidoreductase). Option B (2.1.1.34, catechol O-methyltransferase) is a well-characterized mammalian enzyme with a distinct sequence profile that this bacterial protein does not match. However, distinguishing option A (2.1.1.395) from option C (2.1.1.353) requires knowing the exact natural-product substrate (demethylluteothin vs. whatever substrate EC 2.1.1.395 acts on). Both are SAM-dependent O-methyltransferases acting on specific polyketide/natural-product intermediates; no general sequence heuristic uniquely identifies the demethylluteothin substrate from the 230-aa sequence alone.


**Missing item-specific fact**

> The specific substrate identity (demethylluteothin) and the experimental demonstration that this particular methyltransferase catalyzes the O-methylation of demethylluteothin to luteothin (from the aureothin biosynthetic gene cluster of S. thioluteus). Additionally, knowledge of what EC 2.1.1.395 targets is needed to confirm it is not a better match.


**Reason**

> While general reasoning can narrow the answer to 'a SAM-dependent methyltransferase' (eliminating D) and likely away from COMT (B), the final distinction between two highly specific EC numbers (A vs C) depends on item-specific experimental knowledge of substrate specificity that cannot be derived from the sequence alone. The UniProt entry was only first public in February 2025, further emphasizing its lookup dependence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (2.1.1.395) and C (2.1.1.353) are SAM-dependent O-methyltransferases acting on specific natural-product substrates. Without knowing the exact substrate or having access to the biosynthetic gene cluster context, a model cannot definitively distinguish between these two EC numbers from the sequence alone. The elimination of D (oxidoreductase) and B (COMT) is reasonable, but the A-vs-C distinction is not resolvable by general biological reasoning from the provided sequence.


### Important caveats

- The UniProt entry Q70KH3 was first public on 2025-02-05, making this a very recent annotation; the author's source snapshot is unknown but the sequence has been stable since 2004.
- The EC annotation carries ECO:0000269 (inferred from direct assay), indicating experimental support, not mere computational prediction.
- The sequence is from the aureothin/luteothin biosynthetic gene cluster; knowing this genomic context would aid reasoning but is not provided in the question.
- EC 2.1.1.395 is a very specific and recently assigned EC number; its exact substrate and relationship to the presented sequence were not independently verified in this audit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains SAM-binding Rossmann-like motifs (GxGxG patterns) consistent with a class I methyltransferase fold, which reasonably eliminates option D (1.14.15.9, a copper monooxygenase/oxidoreductase). Option B (2.1.1.34, catechol O-methyltransferase) is a well-characterized mammalian enzyme with a distinct sequence profile that this bacterial protein does not match. However, distinguishing option A (2.1.1.395) from option C (2.1.1.353) requires knowing the exact natural-product substrate (demethylluteothin vs. whatever substrate EC 2.1.1.395 acts on). Both are SAM-dependent O-methyltransferases acting on specific polyketide/natural-product intermediates; no general sequence heuristic uniquely identifies the demethylluteothin substrate from the 230-aa sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (demethylluteothin) and the experimental demonstration that this particular methyltransferase catalyzes the O-methylation of demethylluteothin to luteothin (from the aureothin biosynthetic gene cluster of S. thioluteus). Additionally, knowledge of what EC 2.1.1.395 targets is needed to confirm it is not a better match.",
    "reason": "While general reasoning can narrow the answer to 'a SAM-dependent methyltransferase' (eliminating D) and likely away from COMT (B), the final distinction between two highly specific EC numbers (A vs C) depends on item-specific experimental knowledge of substrate specificity that cannot be derived from the sequence alone. The UniProt entry was only first public in February 2025, further emphasizing its lookup dependence."
  },
  "case_id": "EC_number_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt Q70KH3 (AURI_STRTU, Streptomyces thioluteus) is annotated with EC 2.1.1.353 (Demethylluteothin O-methyltransferase) with evidence code ECO:0000269 (inferred from direct assay) from PubMed:16292785 (Mueller, He, Hertweck 2006). The catalytic reaction (demethylluteothin + SAM → luteothin + SAH) is experimentally characterized. The supplied sequence matches the UniProt entry exactly (SHA256 confirmed, 230 aa). The annotation was first public 2025-02-05."
  },
  "important_caveats": [
    "The UniProt entry Q70KH3 was first public on 2025-02-05, making this a very recent annotation; the author's source snapshot is unknown but the sequence has been stable since 2004.",
    "The EC annotation carries ECO:0000269 (inferred from direct assay), indicating experimental support, not mere computational prediction.",
    "The sequence is from the aureothin/luteothin biosynthetic gene cluster; knowing this genomic context would aid reasoning but is not provided in the question.",
    "EC 2.1.1.395 is a very specific and recently assigned EC number; its exact substrate and relationship to the presented sequence were not independently verified in this audit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (2.1.1.395) and C (2.1.1.353) are SAM-dependent O-methyltransferases acting on specific natural-product substrates. Without knowing the exact substrate or having access to the biosynthetic gene cluster context, a model cannot definitively distinguish between these two EC numbers from the sequence alone. The elimination of D (oxidoreductase) and B (COMT) is reasonable, but the A-vs-C distinction is not resolvable by general biological reasoning from the provided sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q70KH3 (AURI_STRTU, Streptomyces thioluteus) is annotated with EC 2.1.1.353 (Demethylluteothin O-methyltransferase) with evidence code ECO:0000269 (inferred from direct assay) from PubMed:16292785 (Mueller, He, Hertweck 2006). The catalytic reaction (demethylluteothin + SAM → luteothin + SAH) is experimentally characterized. The supplied sequence matches the UniProt entry exactly (SHA256 confirmed, 230 aa). The annotation was first public 2025-02-05.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains SAM-binding Rossmann-like motifs (GxGxG patterns) consistent with a class I methyltransferase fold, which reasonably eliminates option D (1.14.15.9, a copper monooxygenase/oxidoreductase). Option B (2.1.1.34, catechol O-methyltransferase) is a well-characterized mammalian enzyme with a distinct sequence profile that this bacterial protein does not match. However, distinguishing option A (2.1.1.395) from option C (2.1.1.353) requires knowing the exact natural-product substrate (demethylluteothin vs. whatever substrate EC 2.1.1.395 acts on). Both are SAM-dependent O-methyltransferases acting on specific polyketide/natural-product intermediates; no general sequence heuristic uniquely identifies the demethylluteothin substrate from the 230-aa sequence alone.",
    "missing_item_specific_fact": "The specific substrate identity (demethylluteothin) and the experimental demonstration that this particular methyltransferase catalyzes the O-methylation of demethylluteothin to luteothin (from the aureothin biosynthetic gene cluster of S. thioluteus). Additionally, knowledge of what EC 2.1.1.395 targets is needed to confirm it is not a better match.",
    "reason": "While general reasoning can narrow the answer to 'a SAM-dependent methyltransferase' (eliminating D) and likely away from COMT (B), the final distinction between two highly specific EC numbers (A vs C) depends on item-specific experimental knowledge of substrate specificity that cannot be derived from the sequence alone. The UniProt entry was only first public in February 2025, further emphasizing its lookup dependence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (2.1.1.395) and C (2.1.1.353) are SAM-dependent O-methyltransferases acting on specific natural-product substrates. Without knowing the exact substrate or having access to the biosynthetic gene cluster context, a model cannot definitively distinguish between these two EC numbers from the sequence alone. The elimination of D (oxidoreductase) and B (COMT) is reasonable, but the A-vs-C distinction is not resolvable by general biological reasoning from the provided sequence."
  },
  "important_caveats": [
    "The UniProt entry Q70KH3 was first public on 2025-02-05, making this a very recent annotation; the author's source snapshot is unknown but the sequence has been stable since 2004.",
    "The EC annotation carries ECO:0000269 (inferred from direct assay), indicating experimental support, not mere computational prediction.",
    "The sequence is from the aureothin/luteothin biosynthetic gene cluster; knowing this genomic context would aid reasoning but is not provided in the question.",
    "EC 2.1.1.395 is a very specific and recently assigned EC number; its exact substrate and relationship to the presented sequence were not independently verified in this audit."
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

**Accession:** `Q70KH3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 58. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
"Q70KH3"
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16292785","source":"PubMed"}],"value":"Gamma-pyrone methyltransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16292785","source":"PubMed"}],"value":"SAM-dependent pyrone methyltransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16292785","source":"PubMed"}],"value":"2.1.1.353"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Demethylluteothin O-methyltransferase"}}}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"16292785","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:59065"}}],"reaction":{"ecNumber":"2.1.1.353","evidences":[{"evidenceCode":"ECO:0000269","id":"16292785","source":"PubMed"}],"name":"demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:59064"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:142840"},{"database":"ChEBI","id":"CHEBI:142870"}]}}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"citation":{"authors":["Mueller M.","He J.","Hertweck C."],"citationCrossReferences":[{"database":"PubMed","id":"16292785"},{"database":"DOI","id":"10.1002/cbic.200500161"}],"citationType":"journal article","firstPage":"37","id":"16292785","journal":"ChemBioChem","lastPage":"39","publicationDate":"2006","title":"Dissection of the late steps in aureothin biosynthesis.","volume":"7"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH3?format=txt&versions=58)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 1.  
**Retrieved:** 2026-11-02T04:31:49.122851+00:00.  

```text
ID   AURI_STRTU              Reviewed;         230 AA.
AC   Q70KH3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2004, sequence version 1.
DT   09-APR-2025, entry version 58.
DE   RecName: Full=Demethylluteothin O-methyltransferase {ECO:0000305};
DE            EC=2.1.1.353 {ECO:0000269|PubMed:16292785};
DE   AltName: Full=Gamma-pyrone methyltransferase {ECO:0000303|PubMed:16292785};
DE   AltName: Full=SAM-dependent pyrone methyltransferase {ECO:0000303|PubMed:16292785};
GN   Name=aurI {ECO:0000303|PubMed:14700630};
OS   Streptomyces thioluteus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=66431;
```

Source SHA-256: `ecdac3ea83c9b526b46a0656f9bc8ad6168658ba01edaa0f5f3f90bf6b40cc09`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH3?format=txt&versions=58)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 1.  
**Retrieved:** 2026-11-02T04:31:49.122851+00:00.  

```text
DE   RecName: Full=Demethylluteothin O-methyltransferase {ECO:0000305};
DE            EC=2.1.1.353 {ECO:0000269|PubMed:16292785};
DE   AltName: Full=Gamma-pyrone methyltransferase {ECO:0000303|PubMed:16292785};
DE   AltName: Full=SAM-dependent pyrone methyltransferase {ECO:0000303|PubMed:16292785};
```

Source SHA-256: `ecdac3ea83c9b526b46a0656f9bc8ad6168658ba01edaa0f5f3f90bf6b40cc09`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH3?format=txt&versions=58)  
**Locator:** `lines 30-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 1.  
**Retrieved:** 2026-11-02T04:31:49.122851+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.
RX   PubMed=16292785; DOI=10.1002/cbic.200500161;
RA   Mueller M., He J., Hertweck C.;
RT   "Dissection of the late steps in aureothin biosynthesis.";
RL   ChemBioChem 7:37-39(2006).
```

Source SHA-256: `ecdac3ea83c9b526b46a0656f9bc8ad6168658ba01edaa0f5f3f90bf6b40cc09`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH3?format=txt&versions=58)  
**Locator:** `lines 43-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 1.  
**Retrieved:** 2026-11-02T04:31:49.122851+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=demethylluteothin + S-adenosyl-L-methionine = luteothin + S-
CC         adenosyl-L-homocysteine; Xref=Rhea:RHEA:59064, ChEBI:CHEBI:57856,
CC         ChEBI:CHEBI:59789, ChEBI:CHEBI:142840, ChEBI:CHEBI:142870;
CC         EC=2.1.1.353; Evidence={ECO:0000269|PubMed:16292785};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:59065;
CC         Evidence={ECO:0000269|PubMed:16292785};
```

Source SHA-256: `ecdac3ea83c9b526b46a0656f9bc8ad6168658ba01edaa0f5f3f90bf6b40cc09`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 71. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
