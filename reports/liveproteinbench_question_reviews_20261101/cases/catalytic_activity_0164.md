# catalytic_activity_0164

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNKVKVGDAQVSYCIDGKGPGLVLVHGTGGDSETNWGHLMPALTNDWTVVRPDYSGSGITSDEGKQLEVKEIAAQVVAAAEAARVVPFDLVGFSLGSAVVIAIAADYPHLVRRIVLLGAFLSSRDIRQKTQFELWRDLIRTDRAALSRLILLTGFSPDFISKQGHDGVSVIINSFVSEINWEGMARQVELDLSIDVSEAARRIEKPTLVIGCSHDHIVPSSQAKSVVRIIRGAQYTELHTGHLAHIENPEEFILLLRSFLLSEDVP

[Multiple Choices]
A. L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)
B. pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)
C. L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)
D. Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.
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

> The exact supplied sequence matches the UniProt entry annotated as pyrrolizixenacetamide deacetylase. Its catalytic-activity annotation gives choice B and cites PubMed evidence (ECO:0000269); the evidence also links the entry to a relevant publication. This supports the key, though the supplied evidence is an annotation and citation rather than an independent assessment of the experiment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The reaction in B is a hydrolysis, so broad enzyme-class reasoning may make it plausible among these choices. But the sequence and choices do not establish that this protein recognizes the unusual substrate pyrrolizixenacetamide rather than catalyzing another reaction.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence identifying this sequence as a pyrrolizixenacetamide deacetylase and establishing its substrate and products.


**Reason**

> Identifying the precise reaction requires a specific enzyme-function assignment absent from the input; recognizing the sequence or its database entry would be lookup or memorization, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone does not distinguish the exact activity, but the reviewer evidence supports B as the annotated reaction. No alternative choice is supported by the supplied reviewer evidence.


### Important caveats

- The exact sequence match supports applicability of the cited UniProt annotation to this protein.
- The author’s exact source snapshot is unknown; the archived annotation establishes that the reaction was recorded by the historical cutoff, not which source the author used.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The reaction in B is a hydrolysis, so broad enzyme-class reasoning may make it plausible among these choices. But the sequence and choices do not establish that this protein recognizes the unusual substrate pyrrolizixenacetamide rather than catalyzing another reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence identifying this sequence as a pyrrolizixenacetamide deacetylase and establishing its substrate and products.",
    "reason": "Identifying the precise reaction requires a specific enzyme-function assignment absent from the input; recognizing the sequence or its database entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "case_id": "catalytic_activity_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as pyrrolizixenacetamide deacetylase. Its catalytic-activity annotation gives choice B and cites PubMed evidence (ECO:0000269); the evidence also links the entry to a relevant publication. This supports the key, though the supplied evidence is an annotation and citation rather than an independent assessment of the experiment."
  },
  "important_caveats": [
    "The exact sequence match supports applicability of the cited UniProt annotation to this protein.",
    "The author’s exact source snapshot is unknown; the archived annotation establishes that the reaction was recorded by the historical cutoff, not which source the author used."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not distinguish the exact activity, but the reviewer evidence supports B as the annotated reaction. No alternative choice is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as pyrrolizixenacetamide deacetylase. Its catalytic-activity annotation gives choice B and cites PubMed evidence (ECO:0000269); the evidence also links the entry to a relevant publication. This supports the key, though the supplied evidence is an annotation and citation rather than an independent assessment of the experiment.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The reaction in B is a hydrolysis, so broad enzyme-class reasoning may make it plausible among these choices. But the sequence and choices do not establish that this protein recognizes the unusual substrate pyrrolizixenacetamide rather than catalyzing another reaction.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence identifying this sequence as a pyrrolizixenacetamide deacetylase and establishing its substrate and products.",
    "reason": "Identifying the precise reaction requires a specific enzyme-function assignment absent from the input; recognizing the sequence or its database entry would be lookup or memorization, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not distinguish the exact activity, but the reviewer evidence supports B as the annotated reaction. No alternative choice is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The exact sequence match supports applicability of the cited UniProt annotation to this protein.",
    "The author’s exact source snapshot is unknown; the archived annotation establishes that the reaction was recorded by the historical cutoff, not which source the author used."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt entry A0A2G0QDP0 (XHPG_XENHO, Pyrrolizixenacetamide deacetylase, EC 3.5.1.-) from Xenorhabdus hominickii. The catalytic activity annotation 'pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)' is recorded with evidence code ECO:0000269 (inferred from direct assay) from PubMed:39428351, corroborated by X-ray crystallography (PDB 8QZU, 1.18 Å, mutant Ala-94 in complex with acetate product). The sequence SHA256 matches between the benchmark input and the source entry.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One might note superficial hydrolase-like features in the sequence (e.g., a potential GxSxG nucleophile region near 'GCSHDH') and argue against a kinase (no canonical GxGxxG), PLP-dependent lyase, or viral protease. However, the substrate 'pyrrolizixenacetamide' is an extremely obscure, organism-specific bacterial alkaloid intermediate (first characterized in 2024, Angew. Chem. Int. Ed.). No general biological reasoning from a 266-residue amino acid sequence can predict this exact substrate name, its pyrrolizidine ring system, or the specific deacetylation reaction. The reaction is not a common metabolic transformation that would be inferable from enzyme family classification.


**Missing item-specific fact**

> The identity of the specific substrate 'pyrrolizixenacetamide' and its deacetylation to '3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one' is an experimentally determined, organism-specific biosynthetic step (Xenorhabdus hominickii pyrrolizwilline pathway) that cannot be deduced from the amino acid sequence through general enzymology. Access to the UniProt annotation or the 2024 Bode lab publication is required to distinguish B from the other options.


**Reason**

> While rough enzyme-class elimination (kinase vs. lyase vs. protease vs. hydrolase) is marginally possible from sequence motifs, the question demands identification of the exact chemical reaction including a highly specific, recently discovered natural-product substrate. This is an item-specific experimental fact absent from the input, making selection of B dependent on memorization or database lookup rather than general reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (kinase, specific deacetylase, amino acid lyase, viral protease) with very different mechanistic signatures. If a solver could determine the protein is a hydrolase, B is the only hydrolase option. However, arriving at B's specific substrate requires the same item-specific knowledge, so no ambiguity among choices is introduced by the wording itself.


### Important caveats

- The substrate 'pyrrolizixenacetamide' and the product '3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one' were first characterized in 2024 (PubMed:39428351), making this an extremely recent and obscure annotation unlikely to be in most training corpora.
- The UniProt entry was first public in April 2025; the benchmark author's source snapshot date is unknown, creating uncertainty about whether the annotation was available at question-construction time.
- The 'GTGGD' motif near the N-terminus could superficially mislead a solver toward Choice A (kinase), but it does not constitute a canonical kinase nucleotide-binding motif.
- Evidence code ECO:0000269 (direct assay) and supporting crystallographic structure (PDB 8QZU) provide strong experimental support for the annotated reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One might note superficial hydrolase-like features in the sequence (e.g., a potential GxSxG nucleophile region near 'GCSHDH') and argue against a kinase (no canonical GxGxxG), PLP-dependent lyase, or viral protease. However, the substrate 'pyrrolizixenacetamide' is an extremely obscure, organism-specific bacterial alkaloid intermediate (first characterized in 2024, Angew. Chem. Int. Ed.). No general biological reasoning from a 266-residue amino acid sequence can predict this exact substrate name, its pyrrolizidine ring system, or the specific deacetylation reaction. The reaction is not a common metabolic transformation that would be inferable from enzyme family classification.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the specific substrate 'pyrrolizixenacetamide' and its deacetylation to '3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one' is an experimentally determined, organism-specific biosynthetic step (Xenorhabdus hominickii pyrrolizwilline pathway) that cannot be deduced from the amino acid sequence through general enzymology. Access to the UniProt annotation or the 2024 Bode lab publication is required to distinguish B from the other options.",
    "reason": "While rough enzyme-class elimination (kinase vs. lyase vs. protease vs. hydrolase) is marginally possible from sequence motifs, the question demands identification of the exact chemical reaction including a highly specific, recently discovered natural-product substrate. This is an item-specific experimental fact absent from the input, making selection of B dependent on memorization or database lookup rather than general reasoning."
  },
  "case_id": "catalytic_activity_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A2G0QDP0 (XHPG_XENHO, Pyrrolizixenacetamide deacetylase, EC 3.5.1.-) from Xenorhabdus hominickii. The catalytic activity annotation 'pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)' is recorded with evidence code ECO:0000269 (inferred from direct assay) from PubMed:39428351, corroborated by X-ray crystallography (PDB 8QZU, 1.18 Å, mutant Ala-94 in complex with acetate product). The sequence SHA256 matches between the benchmark input and the source entry."
  },
  "important_caveats": [
    "The substrate 'pyrrolizixenacetamide' and the product '3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one' were first characterized in 2024 (PubMed:39428351), making this an extremely recent and obscure annotation unlikely to be in most training corpora.",
    "The UniProt entry was first public in April 2025; the benchmark author's source snapshot date is unknown, creating uncertainty about whether the annotation was available at question-construction time.",
    "The 'GTGGD' motif near the N-terminus could superficially mislead a solver toward Choice A (kinase), but it does not constitute a canonical kinase nucleotide-binding motif.",
    "Evidence code ECO:0000269 (direct assay) and supporting crystallographic structure (PDB 8QZU) provide strong experimental support for the annotated reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (kinase, specific deacetylase, amino acid lyase, viral protease) with very different mechanistic signatures. If a solver could determine the protein is a hydrolase, B is the only hydrolase option. However, arriving at B's specific substrate requires the same item-specific knowledge, so no ambiguity among choices is introduced by the wording itself."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A2G0QDP0 (XHPG_XENHO, Pyrrolizixenacetamide deacetylase, EC 3.5.1.-) from Xenorhabdus hominickii. The catalytic activity annotation 'pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)' is recorded with evidence code ECO:0000269 (inferred from direct assay) from PubMed:39428351, corroborated by X-ray crystallography (PDB 8QZU, 1.18 Å, mutant Ala-94 in complex with acetate product). The sequence SHA256 matches between the benchmark input and the source entry.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One might note superficial hydrolase-like features in the sequence (e.g., a potential GxSxG nucleophile region near 'GCSHDH') and argue against a kinase (no canonical GxGxxG), PLP-dependent lyase, or viral protease. However, the substrate 'pyrrolizixenacetamide' is an extremely obscure, organism-specific bacterial alkaloid intermediate (first characterized in 2024, Angew. Chem. Int. Ed.). No general biological reasoning from a 266-residue amino acid sequence can predict this exact substrate name, its pyrrolizidine ring system, or the specific deacetylation reaction. The reaction is not a common metabolic transformation that would be inferable from enzyme family classification.",
    "missing_item_specific_fact": "The identity of the specific substrate 'pyrrolizixenacetamide' and its deacetylation to '3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one' is an experimentally determined, organism-specific biosynthetic step (Xenorhabdus hominickii pyrrolizwilline pathway) that cannot be deduced from the amino acid sequence through general enzymology. Access to the UniProt annotation or the 2024 Bode lab publication is required to distinguish B from the other options.",
    "reason": "While rough enzyme-class elimination (kinase vs. lyase vs. protease vs. hydrolase) is marginally possible from sequence motifs, the question demands identification of the exact chemical reaction including a highly specific, recently discovered natural-product substrate. This is an item-specific experimental fact absent from the input, making selection of B dependent on memorization or database lookup rather than general reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (kinase, specific deacetylase, amino acid lyase, viral protease) with very different mechanistic signatures. If a solver could determine the protein is a hydrolase, B is the only hydrolase option. However, arriving at B's specific substrate requires the same item-specific knowledge, so no ambiguity among choices is introduced by the wording itself."
  },
  "important_caveats": [
    "The substrate 'pyrrolizixenacetamide' and the product '3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one' were first characterized in 2024 (PubMed:39428351), making this an extremely recent and obscure annotation unlikely to be in most training corpora.",
    "The UniProt entry was first public in April 2025; the benchmark author's source snapshot date is unknown, creating uncertainty about whether the annotation was available at question-construction time.",
    "The 'GTGGD' motif near the N-terminus could superficially mislead a solver toward Choice A (kinase), but it does not constitute a canonical kinase nucleotide-binding motif.",
    "Evidence code ECO:0000269 (direct assay) and supporting crystallographic structure (PDB 8QZU) provide strong experimental support for the annotated reaction."
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

**Accession:** `A0A2G0QDP0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 28. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.833416+00:00.  

```json
"A0A2G0QDP0"
```

Source SHA-256: `ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.833416+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39428351","source":"PubMed"}],"value":"Pyrrolizixenamide hydrolase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"value":"3.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39428351","source":"PubMed"}],"value":"Pyrrolizixenacetamide deacetylase"}}}
```

Source SHA-256: `ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.833416+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:83308"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"name":"pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:83307"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30089"},{"database":"ChEBI","id":"CHEBI:232461"},{"database":"ChEBI","id":"CHEBI:232462"}]}}
```

Source SHA-256: `ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.833416+00:00.  

```json
{"citation":{"authors":["Effert J.","Westphalen M.","Calderari A.","Shi Y.M.","Elamri I.","Najah S.","Gruen P.","Li Y.","Gruez A.","Weissman K.J.","Bode H.B."],"citationCrossReferences":[{"database":"PubMed","id":"39428351"},{"database":"DOI","id":"10.1002/anie.202411258"}],"citationType":"journal article","firstPage":"e202411258","id":"39428351","journal":"Angew. Chem. Int. Ed.","lastPage":"e202411258","publicationDate":"2024","title":"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal peptide synthetase and non-enzymatic dimerization.","volume":"63"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8QZU","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 17903 / CIP 109072 / KE01"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.18 ANGSTROMS) OF MUTANT ALA-94 IN COMPLEX WITH ACETATE","FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE","SUBUNIT","ACTIVE SITE","MUTAGENESIS OF ASN-35 AND SER-94"]}
```

Source SHA-256: `ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959052+00:00.  

```text
ID   XHPG_XENHO              Reviewed;         266 AA.
AC   A0A2G0QDP0;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   31-JAN-2018, sequence version 1.
DT   28-JAN-2026, entry version 28.
DE   RecName: Full=Pyrrolizixenacetamide deacetylase {ECO:0000305|PubMed:39428351};
DE            EC=3.5.1.- {ECO:0000269|PubMed:39428351};
DE   AltName: Full=Pyrrolizixenamide hydrolase {ECO:0000303|PubMed:39428351};
GN   Name=xhpG {ECO:0000303|PubMed:39428351};
GN   ORFNames=Xhom_00310 {ECO:0000312|EMBL:PHM57344.1};
OS   Xenorhabdus hominickii.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Morganellaceae; Xenorhabdus.
OX   NCBI_TaxID=351679;
```

Source SHA-256: `d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959052+00:00.  

```text
DE   RecName: Full=Pyrrolizixenacetamide deacetylase {ECO:0000305|PubMed:39428351};
DE            EC=3.5.1.- {ECO:0000269|PubMed:39428351};
DE   AltName: Full=Pyrrolizixenamide hydrolase {ECO:0000303|PubMed:39428351};
```

Source SHA-256: `d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)  
**Locator:** `lines 25-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959052+00:00.  

```text
RN   [2] {ECO:0007744|PDB:8QZU}
RP   X-RAY CRYSTALLOGRAPHY (1.18 ANGSTROMS) OF MUTANT ALA-94 IN COMPLEX WITH
RP   ACETATE, FUNCTION, CATALYTIC ACTIVITY, DISRUPTION PHENOTYPE, SUBUNIT,
RP   ACTIVE SITE, AND MUTAGENESIS OF ASN-35 AND SER-94.
RC   STRAIN=DSM 17903 / CIP 109072 / KE01;
RX   PubMed=39428351; DOI=10.1002/anie.202411258;
RA   Effert J., Westphalen M., Calderari A., Shi Y.M., Elamri I., Najah S.,
RA   Gruen P., Li Y., Gruez A., Weissman K.J., Bode H.B.;
RT   "Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal
RT   peptide synthetase and non-enzymatic dimerization.";
RL   Angew. Chem. Int. Ed. 63:e202411258-e202411258(2024).
```

Source SHA-256: `d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)  
**Locator:** `lines 39-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959052+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-
CC         pyrrolizin-1-one + acetate + H(+); Xref=Rhea:RHEA:83307,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30089,
CC         ChEBI:CHEBI:232461, ChEBI:CHEBI:232462;
CC         Evidence={ECO:0000269|PubMed:39428351};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83308;
CC         Evidence={ECO:0000269|PubMed:39428351};
```

Source SHA-256: `d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
