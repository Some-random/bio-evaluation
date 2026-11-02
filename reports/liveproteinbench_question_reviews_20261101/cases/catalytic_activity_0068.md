# catalytic_activity_0068

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — Hydrolysis of (1-&gt;4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPLITNIYTADPSAHVFNGKLYIYPSHDRETDIQFNDNGDQYDMADYHVFSLDSLDPPSEVTDHGVVLKVEDIPWVSKQLWAPDAATKDGKYYLYFPARDKEGIFRIGVAVSDKPEGPFTPDPEPIKGSYSIDPAVFVDDDGSAYMYFGGLWGGQLQCYQKGNNIFDAEWSGPKEPSGSGAKALGPRVAKLTDDMRQFAEEVREIVILAPETGEPLAADDHDRRFFEAAWMHKYNGKYYFSYSTGDTHYLVYAVGDSPYGPFTYGGRILEPVLGWTTHHSIVEFQGRWWLFHHDCELSKGVDHLRSVKVKEIWYDKDGKIVTEKPE

[Multiple Choices]
A. spheroidene + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = spheroiden-2-one + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
B. Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.
C. deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose
D. Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction.
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

> The exact sequence matches UniProt entry V9TNS0. Its catalytic-activity annotation gives reaction B and cites PubMed 24262572 with experimental-evidence code ECO:0000269. The entry also reports alpha-L-arabinofuranosidase activity, which is not among the choices.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence’s length and enzyme-like composition may make a glycoside hydrolase more plausible than a DNA helicase or carotenoid oxygenase, but that does not establish the substrate specificity needed to choose B over another glycosidase reaction.


**Missing item-specific fact**

> The protein-specific identification and experimentally reported substrate activity as a beta-xylosidase are absent from the input.


**Reason**

> Selecting the specific xylan-derived reaction requires protein-specific functional or substrate-specificity information, not merely general sequence reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein annotation supports B among the listed reactions. The sequence-only input does not distinguish B from the other glycosidase choice, but that is a lookup dependence rather than evidence that multiple options describe this protein.


### Important caveats

- The supporting annotation is sequence-matched and cites experimental evidence, but the primary paper was not independently reviewed here.
- The source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s length and enzyme-like composition may make a glycoside hydrolase more plausible than a DNA helicase or carotenoid oxygenase, but that does not establish the substrate specificity needed to choose B over another glycosidase reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and experimentally reported substrate activity as a beta-xylosidase are absent from the input.",
    "reason": "Selecting the specific xylan-derived reaction requires protein-specific functional or substrate-specificity information, not merely general sequence reasoning."
  },
  "case_id": "catalytic_activity_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry V9TNS0. Its catalytic-activity annotation gives reaction B and cites PubMed 24262572 with experimental-evidence code ECO:0000269. The entry also reports alpha-L-arabinofuranosidase activity, which is not among the choices."
  },
  "important_caveats": [
    "The supporting annotation is sequence-matched and cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation supports B among the listed reactions. The sequence-only input does not distinguish B from the other glycosidase choice, but that is a lookup dependence rather than evidence that multiple options describe this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry V9TNS0. Its catalytic-activity annotation gives reaction B and cites PubMed 24262572 with experimental-evidence code ECO:0000269. The entry also reports alpha-L-arabinofuranosidase activity, which is not among the choices.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence’s length and enzyme-like composition may make a glycoside hydrolase more plausible than a DNA helicase or carotenoid oxygenase, but that does not establish the substrate specificity needed to choose B over another glycosidase reaction.",
    "missing_item_specific_fact": "The protein-specific identification and experimentally reported substrate activity as a beta-xylosidase are absent from the input.",
    "reason": "Selecting the specific xylan-derived reaction requires protein-specific functional or substrate-specificity information, not merely general sequence reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation supports B among the listed reactions. The sequence-only input does not distinguish B from the other glycosidase choice, but that is a lookup dependence rather than evidence that multiple options describe this protein."
  },
  "important_caveats": [
    "The supporting annotation is sequence-matched and cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry V9TNS0 (sequence exactly matched, 327 AA) annotates this protein as 'Xylosidase/arabinosidase 43A' from Humicola insolens with EC 3.2.1.37 catalytic activity described as 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.' The evidence code is ECO:0000269 (direct assay) from PubMed:24262572, confirming experimental validation. Choice B text matches the annotation verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated 'GKY' motifs (GKYYLYFP, GKYYFSYS) and 'GDS'/'DGS' motifs (DGSAYMYFGGLWGG, GDSPYGPFTYGG) characteristic of the five-bladed beta-propeller fold of Glycoside Hydrolase family 43 (GH43). GH43 members are known to act on xylan/arabinan hemicellulose substrates (xylosidases and arabinosidases), not on glucose polymers. This distinguishes Choice B (xylosidase) from Choice C (beta-glucosidase, typically GH1/GH3/GH5 with different folds). Choices A (carotenoid oxygenase) and D (DNA helicase) are eliminated by the absence of 4-His iron-binding motifs and Walker A/B helicase motifs respectively.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH43 beta-propeller sequence signature (repeated GKY and GDS motifs forming blade-like units) provides a concrete structural argument linking the sequence to a xylan-active glycoside hydrolase. While recognizing GH43 specifically requires specialized glycoside hydrolase knowledge, the reasoning chain from identifiable sequence motifs → GH43 family → xylan/xylose substrate specificity is a defensible biological argument that meaningfully distinguishes B from C, A, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is bifunctional (also EC 3.2.1.55 arabinosidase activity), only EC 3.2.1.37 (xylosidase, Choice B) appears among the four options. The other three choices describe entirely unrelated enzyme classes (carotenoid oxygenase, beta-glucosidase, DNA helicase) that cannot be confused with a GH43 xylosidase.


### Important caveats

- The protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55); the arabinosidase activity is not represented among the choices, but this does not create ambiguity since only the xylosidase activity is offered.
- Recognition of GH43 beta-propeller motifs from sequence alone requires specialized knowledge of glycoside hydrolase family signatures; this is domain expertise rather than general biology, but constitutes a legitimate reasoning pathway.
- All UniProt evidence is reviewer-only and was not available to the evaluated model; the model must rely on sequence-intrinsic features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated 'GKY' motifs (GKYYLYFP, GKYYFSYS) and 'GDS'/'DGS' motifs (DGSAYMYFGGLWGG, GDSPYGPFTYGG) characteristic of the five-bladed beta-propeller fold of Glycoside Hydrolase family 43 (GH43). GH43 members are known to act on xylan/arabinan hemicellulose substrates (xylosidases and arabinosidases), not on glucose polymers. This distinguishes Choice B (xylosidase) from Choice C (beta-glucosidase, typically GH1/GH3/GH5 with different folds). Choices A (carotenoid oxygenase) and D (DNA helicase) are eliminated by the absence of 4-His iron-binding motifs and Walker A/B helicase motifs respectively.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH43 beta-propeller sequence signature (repeated GKY and GDS motifs forming blade-like units) provides a concrete structural argument linking the sequence to a xylan-active glycoside hydrolase. While recognizing GH43 specifically requires specialized glycoside hydrolase knowledge, the reasoning chain from identifiable sequence motifs → GH43 family → xylan/xylose substrate specificity is a defensible biological argument that meaningfully distinguishes B from C, A, and D."
  },
  "case_id": "catalytic_activity_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry V9TNS0 (sequence exactly matched, 327 AA) annotates this protein as 'Xylosidase/arabinosidase 43A' from Humicola insolens with EC 3.2.1.37 catalytic activity described as 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.' The evidence code is ECO:0000269 (direct assay) from PubMed:24262572, confirming experimental validation. Choice B text matches the annotation verbatim."
  },
  "important_caveats": [
    "The protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55); the arabinosidase activity is not represented among the choices, but this does not create ambiguity since only the xylosidase activity is offered.",
    "Recognition of GH43 beta-propeller motifs from sequence alone requires specialized knowledge of glycoside hydrolase family signatures; this is domain expertise rather than general biology, but constitutes a legitimate reasoning pathway.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model; the model must rely on sequence-intrinsic features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (also EC 3.2.1.55 arabinosidase activity), only EC 3.2.1.37 (xylosidase, Choice B) appears among the four options. The other three choices describe entirely unrelated enzyme classes (carotenoid oxygenase, beta-glucosidase, DNA helicase) that cannot be confused with a GH43 xylosidase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry V9TNS0 (sequence exactly matched, 327 AA) annotates this protein as 'Xylosidase/arabinosidase 43A' from Humicola insolens with EC 3.2.1.37 catalytic activity described as 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.' The evidence code is ECO:0000269 (direct assay) from PubMed:24262572, confirming experimental validation. Choice B text matches the annotation verbatim.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated 'GKY' motifs (GKYYLYFP, GKYYFSYS) and 'GDS'/'DGS' motifs (DGSAYMYFGGLWGG, GDSPYGPFTYGG) characteristic of the five-bladed beta-propeller fold of Glycoside Hydrolase family 43 (GH43). GH43 members are known to act on xylan/arabinan hemicellulose substrates (xylosidases and arabinosidases), not on glucose polymers. This distinguishes Choice B (xylosidase) from Choice C (beta-glucosidase, typically GH1/GH3/GH5 with different folds). Choices A (carotenoid oxygenase) and D (DNA helicase) are eliminated by the absence of 4-His iron-binding motifs and Walker A/B helicase motifs respectively.",
    "missing_item_specific_fact": "",
    "reason": "The GH43 beta-propeller sequence signature (repeated GKY and GDS motifs forming blade-like units) provides a concrete structural argument linking the sequence to a xylan-active glycoside hydrolase. While recognizing GH43 specifically requires specialized glycoside hydrolase knowledge, the reasoning chain from identifiable sequence motifs → GH43 family → xylan/xylose substrate specificity is a defensible biological argument that meaningfully distinguishes B from C, A, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (also EC 3.2.1.55 arabinosidase activity), only EC 3.2.1.37 (xylosidase, Choice B) appears among the four options. The other three choices describe entirely unrelated enzyme classes (carotenoid oxygenase, beta-glucosidase, DNA helicase) that cannot be confused with a GH43 xylosidase."
  },
  "important_caveats": [
    "The protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55); the arabinosidase activity is not represented among the choices, but this does not create ambiguity since only the xylosidase activity is offered.",
    "Recognition of GH43 beta-propeller motifs from sequence alone requires specialized knowledge of glycoside hydrolase family signatures; this is domain expertise rather than general biology, but constitutes a legitimate reasoning pathway.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model; the model must rely on sequence-intrinsic features."
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

**Accession:** `V9TNS0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.909204+00:00.  

```json
"V9TNS0"
```

Source SHA-256: `4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.909204+00:00.  

```json
{"includes":[{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"1,4-beta-D-xylan xylohydrolase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Xylan 1,4-beta-xylosidase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"3.2.1.37"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Beta-xylosidase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"3.2.1.55"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Alpha-L-arabinofuranosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Arabinosidase"}]}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Xylosidase/arabinosidase 43A"}}}
```

Source SHA-256: `4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.909204+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.37","evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"name":"Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini."}}
```

Source SHA-256: `4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.909204+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.55","evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"name":"Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides."}}
```

Source SHA-256: `4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.909204+00:00.  

```json
{"citation":{"authors":["Yang X.","Shi P.","Huang H.","Luo H.","Wang Y.","Zhang W.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"24262572"},{"database":"DOI","id":"10.1016/j.foodchem.2013.10.062"}],"citationType":"journal article","firstPage":"381","id":"24262572","journal":"Food Chem.","lastPage":"387","publicationDate":"2014","title":"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and one GH11 xylanase from Humicola insolens and their synergy in the degradation of xylan.","volume":"148"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","SUBCELLULAR LOCATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)  
**Locator:** `lines 1-20`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:28:51.766326+00:00.  

```text
ID   XY43A_HUMIN             Reviewed;         327 AA.
AC   V9TNS0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-MAR-2014, sequence version 1.
DT   28-JAN-2026, entry version 21.
DE   RecName: Full=Xylosidase/arabinosidase 43A {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};
DE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};
DE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};
DE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};
GN   Name=XylL43A {ECO:0000303|PubMed:24262572};
OS   Humicola insolens (Soft-rot fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.
OX   NCBI_TaxID=85995;
```

Source SHA-256: `9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)  
**Locator:** `lines 6-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:28:51.766326+00:00.  

```text
DE   RecName: Full=Xylosidase/arabinosidase 43A {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};
DE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};
DE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};
DE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};
```

Source SHA-256: `9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)  
**Locator:** `lines 46-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:28:51.766326+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-
CC         xylose residues from the non-reducing termini.; EC=3.2.1.37;
CC         Evidence={ECO:0000269|PubMed:24262572};
```

Source SHA-256: `9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)  
**Locator:** `lines 50-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:28:51.766326+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside
CC         residues in alpha-L-arabinosides.; EC=3.2.1.55;
CC         Evidence={ECO:0000269|PubMed:24262572};
```

Source SHA-256: `9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 68. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
