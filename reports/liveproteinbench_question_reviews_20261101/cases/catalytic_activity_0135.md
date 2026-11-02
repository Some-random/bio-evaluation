# catalytic_activity_0135

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine

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
A. 3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
B. demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine
C. lanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 32-hydroxylanosterol + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
D. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
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

> The sequence exactly matches the UniProt entry for demethylluteothin O-methyltransferase, whose annotated catalytic reaction is choice B. The reaction annotation cites experimental evidence from a paper, though that primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices suggest distinct reaction classes, and sequence analysis might suggest an enzyme family, but the supplied sequence alone does not identify demethylluteothin as the substrate or establish this specific methylation reaction.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental identification linking this sequence to demethylluteothin O-methylation.


**Reason**

> Selecting B depends on a particular substrate-and-product assignment absent from the input. Recognizing the exact sequence or retrieving its annotation would be lookup, not reasoning from supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence does not distinguish the options, but the reviewer-only sequence-matched annotation supports B; no evidence here supports another option as the enzyme's reaction.


### Important caveats

- The supporting database reaction annotation cites experimental evidence, but the primary paper was not independently validated in this review.
- Reviewer-only identity and annotation evidence were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices suggest distinct reaction classes, and sequence analysis might suggest an enzyme family, but the supplied sequence alone does not identify demethylluteothin as the substrate or establish this specific methylation reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification linking this sequence to demethylluteothin O-methylation.",
    "reason": "Selecting B depends on a particular substrate-and-product assignment absent from the input. Recognizing the exact sequence or retrieving its annotation would be lookup, not reasoning from supplied evidence."
  },
  "case_id": "catalytic_activity_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for demethylluteothin O-methyltransferase, whose annotated catalytic reaction is choice B. The reaction annotation cites experimental evidence from a paper, though that primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The supporting database reaction annotation cites experimental evidence, but the primary paper was not independently validated in this review.",
    "Reviewer-only identity and annotation evidence were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not distinguish the options, but the reviewer-only sequence-matched annotation supports B; no evidence here supports another option as the enzyme's reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for demethylluteothin O-methyltransferase, whose annotated catalytic reaction is choice B. The reaction annotation cites experimental evidence from a paper, though that primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices suggest distinct reaction classes, and sequence analysis might suggest an enzyme family, but the supplied sequence alone does not identify demethylluteothin as the substrate or establish this specific methylation reaction.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification linking this sequence to demethylluteothin O-methylation.",
    "reason": "Selecting B depends on a particular substrate-and-product assignment absent from the input. Recognizing the exact sequence or retrieving its annotation would be lookup, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not distinguish the options, but the reviewer-only sequence-matched annotation supports B; no evidence here supports another option as the enzyme's reaction."
  },
  "important_caveats": [
    "The supporting database reaction annotation cites experimental evidence, but the primary paper was not independently validated in this review.",
    "Reviewer-only identity and annotation evidence were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q70KH3 (AURI_STRTU, Streptomyces thioluteus, 230 aa, sequence matched) explicitly annotates the catalytic activity as 'demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine' (EC 2.1.1.353) with experimental evidence (ECO:0000269, PubMed:16292785, Mueller et al. 2006, ChemBioChem). The protein is named 'Demethylluteothin O-methyltransferase.' The expected answer exactly matches the annotated reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General sequence analysis can reasonably eliminate C (no cytochrome P450 heme-binding CXXG motif, no P450 fold) and D (no GH18/GH19 chitinase catalytic domain, no CBM50/CBM12 carbohydrate-binding module). The sequence contains motifs suggestive of a SAM-dependent methyltransferase (e.g., a 'GATVL' region reminiscent of β-strand methyltransferase folds), which is consistent with both A and B. However, distinguishing a catechol O-methyltransferase (COMT-type, Choice A) from a pyrone O-methyltransferase (Choice B) requires knowledge of the specific active-site architecture for these very different substrates (catecholamine vs. γ-pyrone polyketide), which is not reliably derivable from the 230-aa sequence by general biological reasoning alone.


**Missing item-specific fact**

> The identity of this protein as AurI from the aureothin biosynthetic gene cluster of Streptomyces thioluteus, and its experimentally determined substrate specificity for demethylluteothin (a γ-pyrone polyketide intermediate) rather than a catecholamine, is an item-specific annotation/experimental fact not encoded in the sequence in a way distinguishable from other SAM-methyltransferases by general reasoning.


**Reason**

> While the sequence supports a methyltransferase assignment (eliminating C and D), the critical discrimination between A (catecholamine O-methyltransferase) and B (pyrone O-methyltransferase) depends on recognizing this exact protein or knowing its specific substrate from the literature. No organism context is provided in the question input, and the shared Rossmann-like methyltransferase fold does not encode substrate identity in a way resolvable by general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A and B describe SAM-dependent O-methyltransferase reactions. Without organism context (Streptomyces, polyketide biosynthesis) or specific structural knowledge of the active site, a model reasoning from sequence alone could plausibly assign either a catecholamine or a polyketide-pyrone substrate. The sequence does not contain a uniquely diagnostic motif that unambiguously selects B over A by general reasoning.


### Important caveats

- The UniProt annotation for this entry was first publicly released on 2025-02-05; the author's source snapshot date is unknown. If the benchmark was constructed before this date, the annotation may not have been available.
- The experimental evidence (PubMed:16292785) is from a 2006 paper dissecting aureothin biosynthesis; the functional characterization is well-established in the literature.
- The sequence match is exact (SHA256 identical, 230 aa), confirming the protein identity.
- Eliminating C and D by general reasoning is straightforward; the core difficulty is the A-vs-B discrimination, which is the crux of the lookup dependency.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General sequence analysis can reasonably eliminate C (no cytochrome P450 heme-binding CXXG motif, no P450 fold) and D (no GH18/GH19 chitinase catalytic domain, no CBM50/CBM12 carbohydrate-binding module). The sequence contains motifs suggestive of a SAM-dependent methyltransferase (e.g., a 'GATVL' region reminiscent of β-strand methyltransferase folds), which is consistent with both A and B. However, distinguishing a catechol O-methyltransferase (COMT-type, Choice A) from a pyrone O-methyltransferase (Choice B) requires knowledge of the specific active-site architecture for these very different substrates (catecholamine vs. γ-pyrone polyketide), which is not reliably derivable from the 230-aa sequence by general biological reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of this protein as AurI from the aureothin biosynthetic gene cluster of Streptomyces thioluteus, and its experimentally determined substrate specificity for demethylluteothin (a γ-pyrone polyketide intermediate) rather than a catecholamine, is an item-specific annotation/experimental fact not encoded in the sequence in a way distinguishable from other SAM-methyltransferases by general reasoning.",
    "reason": "While the sequence supports a methyltransferase assignment (eliminating C and D), the critical discrimination between A (catecholamine O-methyltransferase) and B (pyrone O-methyltransferase) depends on recognizing this exact protein or knowing its specific substrate from the literature. No organism context is provided in the question input, and the shared Rossmann-like methyltransferase fold does not encode substrate identity in a way resolvable by general biological reasoning."
  },
  "case_id": "catalytic_activity_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q70KH3 (AURI_STRTU, Streptomyces thioluteus, 230 aa, sequence matched) explicitly annotates the catalytic activity as 'demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine' (EC 2.1.1.353) with experimental evidence (ECO:0000269, PubMed:16292785, Mueller et al. 2006, ChemBioChem). The protein is named 'Demethylluteothin O-methyltransferase.' The expected answer exactly matches the annotated reaction."
  },
  "important_caveats": [
    "The UniProt annotation for this entry was first publicly released on 2025-02-05; the author's source snapshot date is unknown. If the benchmark was constructed before this date, the annotation may not have been available.",
    "The experimental evidence (PubMed:16292785) is from a 2006 paper dissecting aureothin biosynthesis; the functional characterization is well-established in the literature.",
    "The sequence match is exact (SHA256 identical, 230 aa), confirming the protein identity.",
    "Eliminating C and D by general reasoning is straightforward; the core difficulty is the A-vs-B discrimination, which is the crux of the lookup dependency."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A and B describe SAM-dependent O-methyltransferase reactions. Without organism context (Streptomyces, polyketide biosynthesis) or specific structural knowledge of the active site, a model reasoning from sequence alone could plausibly assign either a catecholamine or a polyketide-pyrone substrate. The sequence does not contain a uniquely diagnostic motif that unambiguously selects B over A by general reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q70KH3 (AURI_STRTU, Streptomyces thioluteus, 230 aa, sequence matched) explicitly annotates the catalytic activity as 'demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine' (EC 2.1.1.353) with experimental evidence (ECO:0000269, PubMed:16292785, Mueller et al. 2006, ChemBioChem). The protein is named 'Demethylluteothin O-methyltransferase.' The expected answer exactly matches the annotated reaction.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General sequence analysis can reasonably eliminate C (no cytochrome P450 heme-binding CXXG motif, no P450 fold) and D (no GH18/GH19 chitinase catalytic domain, no CBM50/CBM12 carbohydrate-binding module). The sequence contains motifs suggestive of a SAM-dependent methyltransferase (e.g., a 'GATVL' region reminiscent of β-strand methyltransferase folds), which is consistent with both A and B. However, distinguishing a catechol O-methyltransferase (COMT-type, Choice A) from a pyrone O-methyltransferase (Choice B) requires knowledge of the specific active-site architecture for these very different substrates (catecholamine vs. γ-pyrone polyketide), which is not reliably derivable from the 230-aa sequence by general biological reasoning alone.",
    "missing_item_specific_fact": "The identity of this protein as AurI from the aureothin biosynthetic gene cluster of Streptomyces thioluteus, and its experimentally determined substrate specificity for demethylluteothin (a γ-pyrone polyketide intermediate) rather than a catecholamine, is an item-specific annotation/experimental fact not encoded in the sequence in a way distinguishable from other SAM-methyltransferases by general reasoning.",
    "reason": "While the sequence supports a methyltransferase assignment (eliminating C and D), the critical discrimination between A (catecholamine O-methyltransferase) and B (pyrone O-methyltransferase) depends on recognizing this exact protein or knowing its specific substrate from the literature. No organism context is provided in the question input, and the shared Rossmann-like methyltransferase fold does not encode substrate identity in a way resolvable by general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A and B describe SAM-dependent O-methyltransferase reactions. Without organism context (Streptomyces, polyketide biosynthesis) or specific structural knowledge of the active site, a model reasoning from sequence alone could plausibly assign either a catecholamine or a polyketide-pyrone substrate. The sequence does not contain a uniquely diagnostic motif that unambiguously selects B over A by general reasoning."
  },
  "important_caveats": [
    "The UniProt annotation for this entry was first publicly released on 2025-02-05; the author's source snapshot date is unknown. If the benchmark was constructed before this date, the annotation may not have been available.",
    "The experimental evidence (PubMed:16292785) is from a 2006 paper dissecting aureothin biosynthesis; the functional characterization is well-established in the literature.",
    "The sequence match is exact (SHA256 identical, 230 aa), confirming the protein identity.",
    "Eliminating C and D by general reasoning is straightforward; the core difficulty is the A-vs-B discrimination, which is the crux of the lookup dependency."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 135. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
